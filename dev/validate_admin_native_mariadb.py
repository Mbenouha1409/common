"""Native DML application and rollback in disposable MariaDB, never local target."""
import copy,json,sys,time
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'movee-app'));sys.path.insert(0,str(ROOT/'dev'))
from validate_admin_core_mariadb import setup as core_setup
from scripts.validate_booking_preferences_mariadb import disposable
from services.admin_native_metadata_contract import contract,IDENTITY
from services.admin_native_plan_service import AdminNativePlanService,sources
from services.mobile_booking_actions_loader import snapshot,fingerprints,canonical_row,digest


def setup(conn):
    core,core_plan,inspect=core_setup(conn)
    with patch.object(core.install,'inspect',side_effect=inspect):core.apply(core_plan,core_plan['plan_sha256'])
    service=AdminNativePlanService(conn);revision=contract();repo=service.repo
    # Application-owned historical Pages 76..90 and Designer36 are part of
    # the reviewed exact predecessor; the minimal baseline fixture lacks them.
    for u in revision['updates']['pages']:
        row=u['before'];pk=row['page_id'];existing=repo.fetch_all('SELECT * FROM pages WHERE page_id=?',[pk])
        if existing:
            keys=[k for k in row if k!='page_id'];conn.execute('UPDATE pages SET '+','.join('`'+k+'`=?' for k in keys)+' WHERE page_id=?',[row[k] for k in keys]+[pk])
        else:repo.insert_record({'table':'pages'},row,[])
    conn.commit()
    original_inspect=inspect
    def adapted(read_only=False):
        return original_inspect(read_only)
    with patch.object(service.install,'inspect',side_effect=adapted):before=service.inspect(False)
    post=snapshot(conn)
    for table,pk in (('pages','page_id'),('actions','action_id'),('fields','field_id')):
        for row in [u['after'] for u in revision['updates'].get(table,[])]+revision['inserts'][table]:post[table][str(row[pk])]=canonical_row(table,row)
    at=int(time.time());plan={'kind':IDENTITY,'target':'movee_app_local','generated_at':at,'valid_until':at+3600,'sources':sources(),'inventory':before,'updates':revision['updates'],'inserts':revision['inserts'],'post_fingerprints':fingerprints(post),'private_fingerprints':before['private_table_fingerprints']};plan['plan_sha256']=digest(plan)
    return service,plan,adapted


def main():
    with disposable() as conn:
        service,plan,inspect=setup(conn)
        with patch.object(service.install,'inspect',side_effect=inspect):
            result=service.apply(plan,plan['plan_sha256']);assert result['inserted']==57 and result['updated']==38
            before=fingerprints(snapshot(conn));replay=service.apply(plan,plan['plan_sha256']);assert replay=={'inserted':0,'updated':0,'replayed':True};assert before==fingerprints(snapshot(conn))
            conn.execute("UPDATE pages SET page_name='Divergent native' WHERE page_id=?",[plan['inserts']['pages'][-1]['page_id']]);conn.commit();bad=fingerprints(snapshot(conn))
            try:service.apply(plan,plan['plan_sha256'])
            except ValueError:pass
            else:raise AssertionError('divergence_accepted')
            assert bad==fingerprints(snapshot(conn))
    with disposable() as conn:
        service,plan,inspect=setup(conn);before=fingerprints(snapshot(conn))
        def fail_final(read_only=False):
            result=inspect(read_only)
            if result['preflight']['metadata_revision']==IDENTITY:raise ValueError('injected_final_failure')
            return result
        with patch.object(service.install,'inspect',side_effect=fail_final):
            try:service.apply(plan,plan['plan_sha256'])
            except ValueError as error:assert str(error)=='injected_final_failure',str(error)
            else:raise AssertionError('missing_final_guard')
        assert before==fingerprints(snapshot(conn))
    print(json.dumps({'disposable_mariadb':True,'inserted':57,'updated':38,'replay_writes':0,'divergence_refused':True,'global_precommit_failure_rolls_back_95':True,'limits':'Environment/actor inventory adapter on isolated socket MariaDB; true global metadata and transaction checks. Counters may advance on rollback.'}))
if __name__=='__main__':main()
