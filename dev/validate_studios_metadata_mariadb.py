"""Full global preflight on disposable MariaDB only; no TCP networking."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'movee-app'))
from scripts.validate_booking_preferences_mariadb import disposable,generate_contract
from scripts.baseline_v1 import future_migrations
from services.movee_migration_service import MoveeMigrationService
from services.studios_metadata_contract import contract
from repositories.movee_migration_repository import MoveeMigrationRepository
from services.mobile_booking_actions_loader import snapshot,fingerprints


def main():
    with disposable() as conn:
        generate_contract(conn)
        repo=MoveeMigrationRepository(conn);migration=future_migrations()[0]
        repo.insert_record({'table':'users'},{'user_id':67,'full_name':'Disposable author','is_active':1,'data_status':1},[])
        repo.insert_record({'table':'configs'},{'config_name':'schema.migration.'+migration['id'],'config_value':migration['sha256'],'config_type':'string','data_status':1,'created_by':67,'created_at':1},[])
        conn.commit();conn.execute('SET SESSION TRANSACTION READ ONLY')
        original=MoveeMigrationService(conn).preflight_schema(expected_database='movee_preferences_disposable')
        assert original['metadata_revision'] is None
        conn.rollback();conn.execute('SET SESSION TRANSACTION READ WRITE')
        revision=contract()
        # Only synthetic metadata and the required existing-id audit reference in disposable storage.
        if not repo.fetch_value('SELECT COUNT(*) FROM users WHERE user_id=67'):
            repo.insert_record({'table':'users'},{'user_id':67,'full_name':'Disposable author','is_active':1,'data_status':1},[])
        for row in revision['after_pages']:
            if row['page_id']==81:
                cols=[k for k in row if k!='page_id']
                conn.execute('UPDATE pages SET '+','.join('`'+k+'`=?' for k in cols)+' WHERE page_id=81',[row[k] for k in cols])
            else:repo.insert_record({'table':'pages'},row,[])
        for row in revision['after_permissions']:repo.insert_record({'table':'permissions'},row,[])
        conn.commit();conn.execute('SET SESSION TRANSACTION READ ONLY')
        before=fingerprints(snapshot(conn))
        for _ in range(2):
            result=MoveeMigrationService(conn).preflight_schema(expected_database='movee_preferences_disposable')
            assert result['metadata_revision']==revision['id']
        assert before==fingerprints(snapshot(conn))
        conn.rollback();conn.execute('SET SESSION TRANSACTION READ WRITE')
        cases=["UPDATE pages SET page_name='Divergence' WHERE page_id=81",
               'UPDATE permissions SET is_allowed=0 WHERE permission_id=157',
               'DELETE FROM pages WHERE page_id=110']
        for sql in cases:
            conn.execute(sql)
            try:MoveeMigrationService(conn).preflight_schema(expected_database='movee_preferences_disposable',read_only=False)
            except ValueError as e:assert 'studios_metadata' in str(e)
            else:raise AssertionError('divergent_state_accepted')
            conn.rollback()
        print(json.dumps({'disposable_mariadb':True,'networking':False,'historical_preflight':True,
                          'installed_preflight':True,'zero_write_replay':True,'divergent_states_refused':3}))

if __name__=='__main__':main()
