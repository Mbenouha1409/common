"""Projected Admin metadata + executor on disposable MariaDB only, no TCP."""
import copy,json,sys,time
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];APP=ROOT/'movee-app';sys.path.insert(0,str(APP))
from scripts.validate_booking_preferences_mariadb import disposable,generate_contract
from scripts.baseline_v1 import future_migrations
from services.movee_migration_service import MoveeMigrationService
from services.studios_metadata_contract import contract as studios_contract
from services.admin_core_metadata_contract import contract
from services.admin_core_plan_service import AdminCorePlanService,sources
from services.mobile_booking_actions_loader import snapshot,fingerprints,digest
from services.booking_preferences_migration_service import stable_structure


def setup(conn):
    generate_contract(conn);s=AdminCorePlanService(conn);repo=s.repo
    repo.insert_record({'table':'users'},{'user_id':67,'full_name':'Disposable author','is_active':1,'data_status':1},[])
    migration=future_migrations()[0]
    repo.insert_record({'table':'configs'},{'config_name':'schema.migration.'+migration['id'],'config_value':migration['sha256'],'config_type':'string','data_status':1,'created_by':67,'created_at':1},[])
    def put(row):
        found=repo.fetch_value('SELECT COUNT(*) FROM pages WHERE page_id=?',[row['page_id']])
        if not found:repo.insert_record({'table':'pages'},row,[])
        else:
            keys=[k for k in row if k!='page_id']
            conn.execute('UPDATE pages SET '+','.join('`'+k+'`=?' for k in keys)+' WHERE page_id=?',[row[k] for k in keys]+[row['page_id']])
    studios=studios_contract()
    for row in studios['after_pages']:put(row)
    for row in studios['after_permissions']:repo.insert_record({'table':'permissions'},row,[])
    revision=contract()
    for update in revision['update_pages']:put(update['before'])
    conn.commit()
    def inspect(_read_only=False):
        return {'actor':{'user_id':67},'preflight':MoveeMigrationService(conn).preflight_schema(expected_database='movee_preferences_disposable',read_only=False),
            'fingerprints':fingerprints(snapshot(conn)),'structure':stable_structure(repo.migration_structure()),
            'next_page_id':int(repo.fetch_value("SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='pages'")),
            'private_table_fingerprints':s.install.private_fingerprints()}
    before=inspect();before['next_permission_id']=158;before['dml_capabilities']={'INSERT':True,'SELECT':True,'UPDATE':True};rows=snapshot(conn)
    from services.mobile_booking_actions_loader import canonical_row
    for row in [u['after'] for u in revision['update_pages']]+revision['insert_pages']:rows['pages'][str(row['page_id'])]=canonical_row('pages',row)
    for row in revision['insert_permissions']:rows['permissions'][str(row['permission_id'])]=canonical_row('permissions',row)
    at=int(time.time())
    plan={'format_version':1,'target':'movee_app_local','kind':'admin_core_reads_permissions_resolved_v2','generated_at':at,'valid_until':at+3600,
          'application_status':'ready_for_explicit_authorization','sources':sources(),'inventory':before,
          'update_pages':revision['update_pages'],'insert_pages':revision['insert_pages'],'insert_permissions':revision['insert_permissions'],'new_permissions':24,
          'post_fingerprints':fingerprints(rows),'private_fingerprints':s.install.private_fingerprints()}
    plan['plan_sha256']=digest(plan)
    return s,plan,inspect


def main():
    # The inventory adapter changes ONLY the DB identity / provisioning actor of
    # the disposable fixture. The global structure+metadata preflight is real.
    with disposable() as conn:
        service,plan,inspect=setup(conn)
        with patch.object(service.install,'inspect',side_effect=inspect):
            installed=service.apply(plan,plan['plan_sha256']);before=fingerprints(snapshot(conn))
            replay=service.apply(plan,plan['plan_sha256'])
            assert installed=={'inserted':35,'inserted_pages':11,'inserted_permissions':24,'updated':13,'replayed':False}
            assert replay=={'inserted':0,'inserted_pages':0,'inserted_permissions':0,'updated':0,'replayed':True}
            assert before==fingerprints(snapshot(conn))
            conn.execute("UPDATE pages SET page_name='Divergent' WHERE page_id=121");conn.commit();bad=fingerprints(snapshot(conn))
            try:service.apply(plan,plan['plan_sha256'])
            except ValueError as error:assert 'admin_core_metadata' in str(error)
            else:raise AssertionError('divergent_replay_accepted')
            assert bad==fingerprints(snapshot(conn))
    with disposable() as conn:
        service,plan,inspect=setup(conn);before=fingerprints(snapshot(conn));calls=[0]
        def final_failure(read_only=False):
            calls[0]+=1;result=inspect(read_only)
            if result['preflight']['metadata_revision']=='admin_core_reads_v2':raise ValueError('injected_global_postflight_failure')
            return result
        with patch.object(service.install,'inspect',side_effect=final_failure):
            try:service.apply(plan,plan['plan_sha256'])
            except ValueError as error:assert str(error)=='injected_global_postflight_failure'
            else:raise AssertionError('missing_global_guard')
        assert before==fingerprints(snapshot(conn))
    print(json.dumps({'disposable_mariadb':True,'networking':False,'projected_global_preflight':True,
        'inserted_pages':11,'inserted_permissions':24,'updated_pages':13,'replay_writes':0,'divergent_replay_refused':True,'global_failure_rolls_back_all_48':True,
        'limits':'Isolated actor/environment inventory adapter; global SQL metadata checks and transactions are real. AUTO_INCREMENT may advance after rollback.'}))

if __name__=='__main__':main()
