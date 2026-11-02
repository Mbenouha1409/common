"""READ ONLY activation planning/verification; no SQL writes or service restart."""
import argparse,hashlib,json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];APP=ROOT/'movee-app';sys.path.insert(0,str(APP))
from services.admin_studios_plan_service import AdminStudiosPlanService,sources
from services.mobile_booking_actions_loader import digest,fingerprints,snapshot


def hashes():
    result={'movee-app/'+k:v for k,v in sources().items()}
    for name in ('dev/apply_studios_plan.py','dev/test_apply_studios_plan.py',
                 'dev/validate_studios_metadata_mariadb.py','dev/plan_studios_metadata_activation.py',
                 'movee-app/services/studios_metadata_contract.py',
                 'movee-app/sql/metadata_evolutions/studios_authorized_v1.json',
                 'movee-app/tests/test_studios_metadata_contract.py'):
        result[name]=hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
    return result


def inspect(conn):
    value=AdminStudiosPlanService(conn).install.inspect()
    if value['preflight'].get('metadata_revision')!='studios_authorized_v1':raise ValueError('exact_installed_revision_required')
    original=json.loads((APP/'docs/admin_studios_permissions_resolved_plan.json').read_text())
    if (value['fingerprints']!=original['post_fingerprints']
        or value['private_table_fingerprints']!=original['post_private_table_fingerprints']):
        raise ValueError('original_authorized_post_state_changed')
    return value


def check(conn,plan,confirmed):
    if (confirmed!=plan.get('plan_sha256') or digest({k:v for k,v in plan.items() if k!='plan_sha256'})!=confirmed
        or plan.get('kind')!='studios_metadata_recognition_activation_v1' or plan.get('target')!='movee_app_local'
        or plan.get('source_hashes')!=hashes() or plan.get('sql_writes')!=[]):raise ValueError('activation_plan_changed')
    if not plan['generated_at']<=int(time.time())<plan['valid_until']:raise ValueError('activation_plan_expired')
    # Two independent READ ONLY preflights and complete inventories, no repair.
    before=inspect(conn)
    if before!=plan['inventory']:raise ValueError('activation_inventory_changed')
    after=inspect(conn)
    if before!=after:raise ValueError('read_only_replay_divergence')
    return {'global_preflight':True,'replayed':True,'inserted':0,'updated':0,'deleted':0,'all_75_tables_preserved':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    mode=parser.add_mutually_exclusive_group();mode.add_argument('--prepare',action='store_true');mode.add_argument('--check-plan',type=Path)
    parser.add_argument('--confirm-database');parser.add_argument('--confirm-plan-sha256');parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if not(args.prepare or args.check_plan):print(json.dumps({'mode':'offline','database_opened':False}));return
    from config import DB_SETTINGS,DB_ENGINE,IS_PRODUCTION
    if (IS_PRODUCTION or DB_ENGINE not in ('mysql','mariadb') or DB_SETTINGS.get('database')!='movee_app_local'
        or DB_SETTINGS.get('host') not in ('localhost','127.0.0.1') or args.confirm_database!='movee_app_local'):
        raise ValueError('explicit_local_database_required')
    if args.output and args.output.exists():raise ValueError('report_or_plan_already_exists')
    from db import db,close_db
    conn=db()
    try:
        conn.execute('SET SESSION TRANSACTION READ ONLY')
        if args.prepare:
            at=int(time.time());inventory=inspect(conn)
            result={'format_version':1,'kind':'studios_metadata_recognition_activation_v1','target':'movee_app_local',
                'generated_at':at,'valid_until':at+3600,'inventory':inventory,'source_hashes':hashes(),
                'original_installation_plan_sha256':'6c18575b90be9bf530091334311598ecb46de5b9c28d4d3663328e5307b7ad6b',
                'sql_writes':[],'ddl':[],'new_accounts_permissions_or_receipts':0,
                'runtime_activation':['Recheck exact plan and inventories in READ ONLY before restart.',
                    'After separate explicit approval only: ./movee-dev restart backend from workspace root.',
                    'Run the same READ ONLY checker after restart; on any failure stop and diagnose, no repair or return plan.'],
                'rollback_plan_applied':False,'old_installation_plan_reexecution':'Refused: its sources no longer match. This new plan only recognizes installed rows; never inserts them again.'}
            result['plan_sha256']=digest(result)
        else:result=check(conn,json.loads(args.check_plan.read_text()),args.confirm_plan_sha256)
        if args.output:
            with args.output.open('x') as out:args.output.chmod(0o600);json.dump(result,out,ensure_ascii=False,indent=2);out.write('\n')
        print(json.dumps({k:v for k,v in result.items() if k not in ('inventory','source_hashes')}))
    finally:conn.rollback();close_db(conn)

if __name__=='__main__':main()
