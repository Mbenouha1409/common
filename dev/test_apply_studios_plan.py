"""Isolated tests for the local operations executor; no live DB access."""
import copy,json,sys,time,unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'movee-app'))
sys.path.insert(0,str(ROOT/'dev'))
from apply_studios_plan import StudiosExecutor
from services.admin_studios_plan_service import sources
from services.mobile_booking_actions_loader import snapshot,fingerprints,canonical_row,digest
from tests.test_ia2b_booking import IA2BBookingTests
from tests.test_booking_preferences import install_isolated

class ExecutorTests(unittest.TestCase):
    def setUp(self):
        self.base=IA2BBookingTests();self.base.setUp();self.addCleanup(self.base.doCleanups)
        self.conn=self.base.conn;install_isolated(self.conn)
        self.executor=StudiosExecutor(self.conn);s=self.executor.service
        before,changes,new=s.resolve();at=int(time.time())
        def stored(row):return {k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in row.items()}
        after=stored({**before,**changes,'updated_by':99,'updated_at':at})
        page_id=self.conn.execute('SELECT MAX(page_id)+1 FROM pages').fetchone()[0]
        new=stored({**new,'page_id':page_id,'created_by':99,'updated_by':99,'created_at':at,'updated_at':at})
        permissions=[dict(r) for r in self.conn.execute('SELECT * FROM permissions')]
        permission_id=max(r['permission_id'] for r in permissions)+1
        added=s.permission_inserts(permissions,permission_id,99,at)
        initial=snapshot(self.conn);post=copy.deepcopy(initial)
        post['pages'][str(before['page_id'])]=canonical_row('pages',after)
        post['pages'][str(page_id)]=canonical_row('pages',{k:new.get(k) for k in before})
        for row in added:post['permissions'][str(row['permission_id'])]=canonical_row('permissions',row)
        self.inventory={'actor':{'user_id':99},'next_page_id':page_id,'next_permission_id':permission_id,
                        'fingerprints':fingerprints(initial),'private_table_fingerprints':s.install.private_fingerprints()}
        self.plan={'target':'movee_app_local','kind':'admin_studios_navigation_permissions_v2','sources':sources(),
                   'generated_at':at,'valid_until':at+3600,'total_inserted':4,'total_updated':1,
                   'eligibility':{'full_requested_scope_ready':True},'inventory':self.inventory,
                   'update_page':{'before':before,'after':after,'changed_columns':list(changes)+['updated_by','updated_at']},
                   'insert_page':new,'insert_permissions':added,'effective_pages':s.effective([after,new]),
                   'post_fingerprints':fingerprints(post),'post_private_table_fingerprints':s.install.private_fingerprints()}
        self.plan['plan_sha256']=digest(self.plan)
        def inventory():
            value=copy.deepcopy(self.inventory);value['fingerprints']=fingerprints(snapshot(self.conn))
            if value['fingerprints']==self.plan['post_fingerprints']:
                value['next_page_id']+=1;value['next_permission_id']+=3
            return value
        for obj,name,kw in [(self.executor,'inventory',{'side_effect':inventory}),
                            (self.executor.repo,'acquire_migration_lock',{'return_value':None}),
                            (self.executor.repo,'release_migration_lock',{'return_value':None})]:
            p=patch.object(obj,name,**kw);p.start();self.addCleanup(p.stop)

    def test_exact_apply_preservation_and_zero_write_replay(self):
        result=self.executor.apply(self.plan,self.plan['plan_sha256'])
        self.assertEqual(result,{'inserted':4,'updated':1,'replayed':False,'preserved':True})
        before=list(self.conn.iterdump())
        result=self.executor.apply(self.plan,self.plan['plan_sha256'])
        self.assertEqual(result,{'inserted':0,'updated':0,'replayed':True,'preserved':True})
        self.assertEqual(before,list(self.conn.iterdump()))

    def test_insert_failure_rolls_back_update_and_all_inserts(self):
        before=list(self.conn.iterdump());original=self.executor.repo.insert_record;calls=[0]
        def fail(*args):
            calls[0]+=1
            if calls[0]==3:raise RuntimeError('isolated_injected_failure')
            return original(*args)
        with patch.object(self.executor.repo,'insert_record',side_effect=fail):
            with self.assertRaises(RuntimeError):self.executor.apply(self.plan,self.plan['plan_sha256'])
        self.assertEqual(before,list(self.conn.iterdump()))

    def test_wrong_hash_expiry_inventory_and_partial_state_refused(self):
        before=list(self.conn.iterdump())
        with self.assertRaises(ValueError):self.executor.apply(self.plan,'0'*64)
        with patch('apply_studios_plan.time.time',return_value=self.plan['valid_until']):
            with self.assertRaisesRegex(ValueError,'expired'):self.executor.apply(self.plan,self.plan['plan_sha256'])
        self.assertEqual(before,list(self.conn.iterdump()))
        self.conn.execute("UPDATE pages SET page_name='Concurrent change' WHERE page_id=81");self.conn.commit()
        before=list(self.conn.iterdump())
        with self.assertRaisesRegex(ValueError,'inventory_changed'):self.executor.apply(self.plan,self.plan['plan_sha256'])
        self.assertEqual(before,list(self.conn.iterdump()))

    def test_global_final_preflight_failure_rolls_back_before_commit(self):
        before=list(self.conn.iterdump())
        with patch.object(self.executor,'inventory',side_effect=[self.inventory,ValueError('metadata_contract_mismatch:pages')]):
            with self.assertRaisesRegex(ValueError,'metadata_contract_mismatch'):
                self.executor.apply(self.plan,self.plan['plan_sha256'])
        self.assertEqual(before,list(self.conn.iterdump()))

if __name__=='__main__':unittest.main()
