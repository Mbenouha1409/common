"""Local operations executor for the separately approved Studios metadata plan.

Lives alongside movee-dev tooling; does not modify pinned application sources.
Default is offline. No DDL, partial repair or automatic plan regeneration.
"""
import argparse
import hashlib
import json
import copy
import re
import sys
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
APP=ROOT/'movee-app'
sys.path.insert(0,str(APP))
from services.admin_studios_plan_service import AdminStudiosPlanService,sources
from services.mobile_booking_actions_loader import canonical_row,digest,fingerprints,snapshot


class StudiosExecutor:
    def __init__(self,conn):
        self.conn=conn
        self.service=AdminStudiosPlanService(conn)
        self.repo=self.service.repo

    def verify(self,plan,confirmed):
        if (confirmed!=plan.get('plan_sha256') or digest({k:v for k,v in plan.items() if k!='plan_sha256'})!=confirmed
            or plan.get('target')!='movee_app_local' or plan.get('kind')!='admin_studios_navigation_permissions_v2'
            or plan.get('sources')!=sources() or plan.get('total_inserted')!=4 or plan.get('total_updated')!=1
            or len(plan.get('insert_permissions',[]))!=3 or not plan['eligibility']['full_requested_scope_ready']):
            raise ValueError('plan_confirmation_or_sources_failed')
        if not plan['generated_at']<=int(time.time())<plan['valid_until']:
            raise ValueError('plan_expired')

    def inventory(self):
        value=self.service.install.inspect(False)
        value['next_permission_id']=int(self.repo.fetch_value("SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='permissions'"))
        return value

    def preserved(self,plan):
        if (fingerprints(snapshot(self.conn))!=plan['post_fingerprints']
            or self.service.install.private_fingerprints()!=plan['post_private_table_fingerprints']):
            raise ValueError('post_fingerprints_failed')
        rows=snapshot(self.conn)
        rows['pages'][str(plan['update_page']['before']['page_id'])]=canonical_row('pages',plan['update_page']['before'])
        del rows['pages'][str(plan['insert_page']['page_id'])]
        for row in plan['insert_permissions']:del rows['permissions'][str(row['permission_id'])]
        if fingerprints(rows)!=plan['inventory']['fingerprints']:
            raise ValueError('preexisting_data_not_preserved')
        effective=self.service.effective([plan['update_page']['after'],plan['insert_page']])
        if effective!=plan['effective_pages']:raise ValueError('effective_overrides_changed')

    def apply(self,plan,confirmed):
        self.verify(plan,confirmed)
        self.repo.acquire_migration_lock()
        try:
            with self.repo.transaction():
                self.verify(plan,confirmed)
                # Lock the full historical inventory, including insertion ranges,
                # before comparing state; prevent concurrent legacy writers too.
                snapshot(self.conn,lock=True)
                if self.conn.dialect.name!='sqlite':
                    for table in ('booking_preference_states','booking_preference_commands'):
                        self.repo.fetch_all('SELECT * FROM `'+table+'` FOR UPDATE')
                current=self.inventory()
                post=fingerprints(snapshot(self.conn))==plan['post_fingerprints']
                if post:
                    expected=copy.deepcopy(plan['inventory'])
                    expected['next_page_id']=plan['insert_page']['page_id']+1
                    expected['next_permission_id']=max(r['permission_id'] for r in plan['insert_permissions'])+1
                    expected['fingerprints']=plan['post_fingerprints']
                    for table,next_id in (('pages',expected['next_page_id']),('permissions',expected['next_permission_id'])):
                        definitions=expected.get('structure',{}).get('definitions',{})
                        if table in definitions:
                            definitions[table]=re.sub(r' AUTO_INCREMENT=\d+', ' AUTO_INCREMENT='+str(next_id), definitions[table])
                    if current!=expected:raise ValueError('replay_inventory_changed')
                    self.preserved(plan)
                    return {'inserted':0,'updated':0,'replayed':True,'preserved':True}
                if current!=plan['inventory']:raise ValueError('inventory_changed_no_application')
                before=plan['update_page']['before'];after=plan['update_page']['after']
                actual=self.repo.fetch_all('SELECT * FROM pages WHERE page_id=?',[before['page_id']])
                if len(actual)!=1 or dict(actual[0])!=before:raise ValueError('page_81_cas_failed')
                columns=plan['update_page']['changed_columns']
                if set(columns)!={'page_name','page_config','config_fields','config_filters','config_actions','updated_by','updated_at'}:
                    raise ValueError('unexpected_update_columns')
                self.conn.execute('UPDATE pages SET '+','.join('`'+k+'`=?' for k in columns)+' WHERE page_id=?',
                                  [after[k] for k in columns]+[before['page_id']])
                self.repo.insert_record({'table':'pages'},plan['insert_page'],[])
                for row in plan['insert_permissions']:self.repo.insert_record({'table':'permissions'},row,[])
                self.preserved(plan)
                # Mandatory global final-state validation INSIDE the transaction.
                self.inventory()
                self.verify(plan,confirmed)
                return {'inserted':4,'updated':1,'replayed':False,'preserved':True}
        finally:self.repo.release_migration_lock()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute',action='store_true');parser.add_argument('--confirm-database')
    parser.add_argument('--confirm-plan-sha256');parser.add_argument('--plan',type=Path,required=True)
    parser.add_argument('--report',type=Path)
    args=parser.parse_args()
    if not args.execute:
        print(json.dumps({'mode':'offline','database_opened':False}));return
    from config import DB_SETTINGS,DB_ENGINE,IS_PRODUCTION
    if (IS_PRODUCTION or DB_ENGINE not in ('mysql','mariadb') or DB_SETTINGS.get('database')!='movee_app_local'
        or DB_SETTINGS.get('host') not in ('localhost','127.0.0.1') or args.confirm_database!='movee_app_local'):
        raise ValueError('explicit_local_target_required')
    if args.report is None or args.report.exists():raise ValueError('new_report_path_required')
    plan=json.loads(args.plan.read_text())
    StudiosExecutor(None).verify(plan,args.confirm_plan_sha256)
    from db import db,close_db
    conn=db()
    try:
        executor=StudiosExecutor(conn)
        applied=executor.apply(plan,args.confirm_plan_sha256)
        replay=executor.apply(plan,args.confirm_plan_sha256)
        result={'plan_sha256':plan['plan_sha256'],'target':'movee_app_local','applied_at':int(time.time()),
                'executor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'application':applied,'replay':replay,'preservation_75_tables':True,
                'post_fingerprints':fingerprints(snapshot(conn)),
                'private_table_fingerprints':executor.service.install.private_fingerprints()}
        with args.report.open('x') as out:
            args.report.chmod(0o600);json.dump(result,out,indent=2);out.write('\n')
        print(json.dumps({k:v for k,v in result.items() if 'fingerprints' not in k}))
    finally:conn.rollback();close_db(conn)


if __name__=='__main__':main()
