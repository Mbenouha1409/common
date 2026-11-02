"""Exact completion apply/replay/final failure on isolated socket MariaDB."""
import json,sys,time
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'movee-app'));sys.path.insert(0,str(ROOT/'dev'))
from validate_admin_native_mariadb import setup as native_setup
from scripts.validate_booking_preferences_mariadb import disposable
from services.admin_completion_plan_service import AdminCompletionPlanService,sources
from services.admin_completion_metadata_contract import contract,IDENTITY
from services.mobile_booking_actions_loader import snapshot,fingerprints,canonical_row,digest


def setup(conn):
    native,plan,inspect=native_setup(conn)
    with patch.object(native.install,'inspect',side_effect=inspect):native.apply(plan,plan['plan_sha256'])
    s=AdminCompletionPlanService(conn);revision=contract();repo=s.repo
    # The disposable predecessor does not contain every application-owned Page;
    # seed only reviewed before-images absent from its fixture.
    for u in revision['updates']['pages']:
        row=u['before'];actual=repo.fetch_all('SELECT * FROM pages WHERE page_id=?',[row['page_id']])
        if not actual:repo.insert_record({'table':'pages'},row,[])
        else:assert dict(actual[0])==row,'fixture_predecessor_changed'
    conn.commit()
    with patch.object(s.install,'inspect',side_effect=inspect):before=s.inspect(False)
    post=snapshot(conn)
    for row in [u['after'] for u in revision['updates']['pages']]+revision['inserts']['pages']:post['pages'][str(row['page_id'])]=canonical_row('pages',row)
    now=int(time.time());plan={'kind':IDENTITY,'target':'movee_app_local','generated_at':now,'valid_until':now+3600,'sources':sources(),'inventory':before,'updates':revision['updates'],'inserts':revision['inserts'],'post_fingerprints':fingerprints(post),'private_fingerprints':before['private_table_fingerprints']};plan['plan_sha256']=digest(plan)
    return s,plan,inspect


def main():
    with disposable() as conn:
        s,p,inspect=setup(conn)
        with patch.object(s.install,'inspect',side_effect=inspect):
            result=s.apply(p,p['plan_sha256']);assert result['inserted']==7 and result['updated']==87
            before=fingerprints(snapshot(conn));assert s.apply(p,p['plan_sha256'])=={'inserted':0,'updated':0,'replayed':True};assert before==fingerprints(snapshot(conn))
            conn.execute("UPDATE pages SET page_name='Divergent completion' WHERE page_id=?",[p['inserts']['pages'][-1]['page_id']]);conn.commit();bad=fingerprints(snapshot(conn))
            try:s.apply(p,p['plan_sha256'])
            except ValueError:pass
            else:raise AssertionError('divergence_accepted')
            assert bad==fingerprints(snapshot(conn))
    with disposable() as conn:
        s,p,inspect=setup(conn);before=fingerprints(snapshot(conn))
        def fail_final(read_only=False):
            result=inspect(read_only)
            if result['preflight']['metadata_revision']==IDENTITY:raise ValueError('injected_final_failure')
            return result
        with patch.object(s.install,'inspect',side_effect=fail_final):
            try:s.apply(p,p['plan_sha256'])
            except ValueError as error:assert str(error)=='injected_final_failure',str(error)
            else:raise AssertionError('missing_final_guard')
        assert before==fingerprints(snapshot(conn))
    print(json.dumps({'disposable_mariadb':True,'inserted_pages':7,'updated_pages':87,'replay_writes':0,'divergence_refused':True,'final_preflight_failure_rollback_operations':94,'limits':'Actor/environment fixture inventory adapter, actual global SQL checks and transactions; AUTO_INCREMENT may advance after rollback.'}))
if __name__=='__main__':main()
