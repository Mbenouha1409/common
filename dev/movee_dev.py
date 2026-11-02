"""Services locaux MOVEE : launchd supervise ; ce CLI ne tue aucun PID externe."""
import argparse
import fcntl
import json
import ipaddress
import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
import plistlib
import re
import signal
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
PYTHON = ROOT / 'movee-app/venv/bin/python'
NODE = Path('/opt/homebrew/opt/node@24/bin/node')
BREW = '/opt/homebrew/bin/brew'
PROFILE = os.environ.get('MOVEE_DEV_PROFILE', 'local')
if PROFILE not in ('local', 'check'):
    raise SystemExit('MOVEE_DEV_PROFILE doit être local ou check.')
PORTS = {'backend': 5050, 'redis': 6380, 'expo': 8081}
if PROFILE == 'check':
    PORTS = {'backend': 15050, 'redis': 16380, 'expo': 18081}
DOMAIN = f'gui/{os.getuid()}'
STATE = Path.home() / 'Library/Application Support/MOVEE' / PROFILE
LOGS = Path.home() / 'Library/Logs/MOVEE' / PROFILE
AGENTS = Path.home() / 'Library/LaunchAgents' if PROFILE == 'local' else STATE / 'agents'
ORDER = ('redis', 'backend', 'expo')


def network_address():
    path = STATE / 'network.json'
    if PROFILE != 'local' or not path.exists():
        return None
    value = json.loads(path.read_text())
    if set(value) != {'lan_address'}:
        raise RuntimeError('Configuration réseau locale non reconnue.')
    address = ipaddress.IPv4Address(value['lan_address'])
    if not any(address in ipaddress.IPv4Network(net) for net in ('10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16')):
        raise RuntimeError('Le mode iPhone exige une adresse IPv4 privée du Wi-Fi.')
    return str(address)


def update_public_api(address):
    # Expo SDK58 charge aussi .env.local comme module virtuel natif :
    # l'environnement du superviseur seul ne suffit pas à le remplacer.
    path = ROOT / 'movee-mobile/.env.local'
    before = path.read_text() if path.exists() else ''
    pattern = r'(?m)^EXPO_PUBLIC_API_URL=.*$'
    if len(re.findall(pattern, before)) > 1:
        raise RuntimeError('Plusieurs EXPO_PUBLIC_API_URL : configuration ambiguë, aucun changement.')
    line = f'EXPO_PUBLIC_API_URL=http://{address or "127.0.0.1"}:{PORTS["backend"]}'
    after = re.sub(pattern, lambda _: line, before) if re.search(pattern, before) else before + ('\n' if before and not before.endswith('\n') else '') + line + '\n'
    if after != before:
        path.write_text(after)
        path.chmod(0o600)


def configure_network(iphone):
    if PROFILE != 'local':
        raise RuntimeError('Le profil check reste en boucle locale.')
    address = None
    if iphone:
        result = call(['/usr/sbin/ipconfig', 'getifaddr', 'en0'])
        if result.returncode:
            raise RuntimeError('Wi-Fi en0 sans adresse : connecter le Mac au Wi-Fi avant de continuer.')
        address = str(ipaddress.IPv4Address(result.stdout.strip()))
        if not any(ipaddress.IPv4Address(address) in ipaddress.IPv4Network(net) for net in ('10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16')):
            raise RuntimeError('Adresse Wi-Fi hors réseau privé ; aucun changement.')
    validate_backend()
    for service in ('backend', 'expo'):
        owned_plist(service)
        if job(service) is None and listening(PORTS[service]):
            raise RuntimeError(f'{service} : port externe occupé ; aucun changement.')
    update_public_api(address)
    # Redis et MariaDB restent en service, donc les sessions Redis sont conservées.
    stop('expo')
    stop('backend')
    path = STATE / 'network.json'
    if address:
        path.write_text(json.dumps({'lan_address': address}) + '\n')
        path.chmod(0o600)
    else:
        path.unlink(missing_ok=True)
    if job('redis') is None:
        start('redis')
    start('backend')
    start('expo')
    if address:
        print(f'iPhone : exp://{address}:{PORTS["expo"]}')
        print(f'Backend Wi-Fi : http://{address}:{PORTS["backend"]}')
        print('Retour à la boucle locale : ./movee-dev loopback')
    else:
        print('Backend et Expo revenus en boucle locale.')


def label(service):
    return f'fr.movee.dev.{PROFILE}.{service}'


def call(args):
    return subprocess.run(args, capture_output=True, text=True)


def job(service):
    result = call(['/bin/launchctl', 'print', f'{DOMAIN}/{label(service)}'])
    if result.returncode:
        return None
    # Ne jamais afficher l'environnement complet retourné par launchctl.
    match = re.search(r'^\s*pid = (\d+)', result.stdout, re.M)
    return int(match[1]) if match else 0


def listening(port):
    # Détecte aussi un service IPv6 uniquement, comme Expo localhost.
    for host in ('127.0.0.1', '::1'):
        try:
            with socket.create_connection((host, port), timeout=.3):
                return True
        except OSError:
            pass
    return False


def ready(service):
    if service == 'backend' and (not listening(3306) or not ready('redis')):
        return False
    if service == 'redis':
        result = call(['/opt/homebrew/bin/redis-cli', '-h', '127.0.0.1', '-p', str(PORTS[service]), 'ping'])
        return result.returncode == 0 and result.stdout.strip() == 'PONG'
    host = 'localhost' if service == 'expo' else '127.0.0.1'
    path = '/status' if service == 'expo' else '/login'
    try:
        with urllib.request.urlopen(f'http://{host}:{PORTS[service]}{path}', timeout=2) as response:
            return response.status == 200
    except (OSError, urllib.error.URLError):
        return False


def owned_plist(service):
    path = AGENTS / (label(service) + '.plist')
    if path.exists():
        with path.open('rb') as stream:
            data = plistlib.load(stream)
        expected = [str(PYTHON), '-B', str(Path(__file__).resolve()), '_run', service]
        if data.get('Label') != label(service) or data.get('ProgramArguments') != expected:
            raise RuntimeError(f'{service} : configuration existante étrangère, aucune modification.')
    return path


def validate_backend():
    # Syntaxe et cible seulement ; aucune connexion ni écriture SQL.
    from dotenv import dotenv_values
    from urllib.parse import urlsplit
    cfg = {**dotenv_values(ROOT / '.env'), **os.environ}
    required = {'ENV': 'development', 'DB_ENGINE': 'mariadb', 'DB_HOST': '127.0.0.1',
                'DB_NAME': 'movee_app_local', 'MOVEE_ASSISTANT_ENABLED': '0',
                'MOVEE_NETWORK_ENABLED': '1', 'MOVEE_MOBILE_ENABLED': '1'}
    if any(cfg.get(k) != v for k, v in required.items()) or str(cfg.get('DB_PORT', '3306')) != '3306':
        raise RuntimeError('Configuration Backend différente de la cible locale attendue ; arrêt sans modification.')
    endpoint = urlsplit(cfg.get('ASSISTANT_REDIS_URL', ''))
    if endpoint.hostname != '127.0.0.1' or endpoint.port != 6380 or endpoint.path not in ('/0', ''):
        raise RuntimeError('Redis Backend doit cibler 127.0.0.1:6380/0 ; aucune modification du secret/config.')


def start(service):
    path = owned_plist(service)
    if job(service) is not None:
        if ready(service):
            print(f'{service} : déjà démarré, aucun doublon.')
            return
        # Ne pas créer une seconde instance si launchd attend ou relance déjà le job.
        print(f'{service} : déjà supervisé ; attente de disponibilité.')
    else:
        if listening(PORTS[service]):
            raise RuntimeError(f'{service} : port {PORTS[service]} occupé par un service externe. Arrête-le depuis son lancement d’origine ; aucun PID touché.')
        if service == 'backend':
            validate_backend()
            if not listening(3306) or not ready('redis'):
                raise RuntimeError('MariaDB 3306 et Redis sont requis avant le Backend.')
        data = {'Label': label(service),
                'ProgramArguments': [str(PYTHON), '-B', str(Path(__file__).resolve()), '_run', service],
                'WorkingDirectory': str(STATE),
                'EnvironmentVariables': {'MOVEE_DEV_PROFILE': PROFILE},
                'RunAtLoad': True, 'KeepAlive': True, 'ThrottleInterval': 10,
                'ProcessType': 'Background' if service == 'redis' else 'Interactive',
                'ExitTimeOut': 20, 'Umask': 0o077}
        path.write_bytes(plistlib.dumps(data)); path.chmod(0o600)
        # Un stop enlève le plist : les services arrêtés ne repartent pas au login.
        result = call(['/bin/launchctl', 'bootstrap', DOMAIN, str(path)])
        if result.returncode:
            path.unlink(missing_ok=True)
            raise RuntimeError(f'{service} : bootstrap launchd refusé (code {result.returncode}).')
    until = time.monotonic() + (60 if service == 'expo' else 25)
    while time.monotonic() < until:
        if job(service) and ready(service):
            print(f'{service} : prêt sur le port {PORTS[service]} (géré).')
            return
        time.sleep(.5)
    raise RuntimeError(f'{service} : pas prêt ; consulter ./movee-dev logs {service}. Le job reste supervisé.')


def stop(service):
    path = owned_plist(service)
    if job(service) is None:
        path.unlink(missing_ok=True)
        print(f'{service} : non géré / arrêté ; aucun processus externe touché.')
        return
    if not path.exists():
        raise RuntimeError(f'{service} : job sans configuration reconnue ; arrêt refusé.')
    result = call(['/bin/launchctl', 'bootout', f'{DOMAIN}/{label(service)}'])
    if result.returncode:
        raise RuntimeError(f'{service} : bootout refusé (code {result.returncode}).')
    path.unlink(missing_ok=True)
    until = time.monotonic() + 20
    while (job(service) is not None or listening(PORTS[service])) and time.monotonic() < until:
        time.sleep(.2)
    if job(service) is not None or listening(PORTS[service]):
        raise RuntimeError(f'{service} : arrêt encore en cours ou port occupé ; aucun autre PID touché.')
    print(f'{service} : arrêté ; démarrage au login retiré.')


def safe_line(line, secrets):
    # En-têtes et payloads sensibles ne sont jamais des messages de diagnostic.
    if re.search(r'(?i)authorization|set-cookie|\bcookie\s*:|password|passwd|secret|api[_-]?key|access_token|refresh_token', line):
        return '[ligne sensible masquée]'
    for value in secrets:
        line = line.replace(value, '[masqué]')
    line = re.sub(r'mv1_[A-Za-z0-9_-]+', '[jeton masqué]', line)
    line = re.sub(r'(?i)Bearer\s+\S+', 'Bearer [masqué]', line)
    line = re.sub(r'([a-zA-Z][\w+.-]*://)[^\s/@]+:[^\s/@]+@', r'\1[masqué]@', line)
    line = re.sub(r'\?[^\s\"\']+', '?[paramètres masqués]', line)
    return line.rstrip()[:2000]


def private_values():
    from dotenv import dotenv_values
    values = []
    for path in (ROOT / '.env', ROOT / 'movee-mobile/.env.local', ROOT / 'movee-mobile/.env'):
        if path.exists():
            for key, value in dotenv_values(path).items():
                if value and re.search(r'(?i)password|secret|token|key', key):
                    values.append(str(value))
    credential_file = Path.home() / '.config/movee/mobile-pages-acceptance-credentials.json'
    def collect(value):
        if isinstance(value, dict):
            for key, item in value.items():
                if isinstance(item, str) and re.search(r'(?i)password|secret|token|key', key):
                    values.append(item)
                else:
                    collect(item)
        elif isinstance(value, list):
            for item in value:
                collect(item)
    if credential_file.exists():
        collect(json.loads(credential_file.read_text()))
    return sorted(set(values), key=len, reverse=True)


def run_service(service):
    os.umask(0o077)
    env = {k: v for k, v in os.environ.items() if k in ('HOME', 'USER', 'LOGNAME', 'TMPDIR', 'LANG', 'LC_ALL', 'MOVEE_DEV_PROFILE')}
    # Pas d'héritage de variables injectées par un terminal ou par launchd pour le métier.
    env.update(PATH=f'{NODE.parent}:/opt/homebrew/bin:/usr/bin:/bin', PYTHONDONTWRITEBYTECODE='1',
               PYTHONUNBUFFERED='1', FORCE_COLOR='0')
    if service == 'backend':
        validate_backend()
        env['MOVEE_DEV_BACKEND_PORT'] = str(PORTS['backend'])
        address = network_address()
        if address:
            env['MOVEE_DEV_LAN_ADDRESS'] = address
        if PROFILE == 'check':
            env['ASSISTANT_REDIS_URL'] = f'redis://127.0.0.1:{PORTS["redis"]}/0'
        command = [str(PYTHON), '-B', '-m', 'gunicorn', '-c', str(ROOT / 'dev/gunicorn.local.py'), 'app:app']
        cwd = ROOT / 'movee-app'
    elif service == 'redis':
        command = ['/opt/homebrew/bin/redis-server', '--bind', '127.0.0.1', '--port', str(PORTS['redis']),
                   '--save', '', '--appendonly', 'no', '--daemonize', 'no', '--dir', str(STATE)]
        cwd = STATE
    else:
        env.pop('CI', None)
        env.update(BROWSER='none', EXPO_NO_TELEMETRY='1')
        if PROFILE == 'check':
            env['EXPO_PUBLIC_API_URL'] = f'http://127.0.0.1:{PORTS["backend"]}'
        address = network_address()
        if address:
            env.update(REACT_NATIVE_PACKAGER_HOSTNAME=address,
                       EXPO_PUBLIC_API_URL=f'http://{address}:{PORTS["backend"]}')
        command = [str(NODE), str(ROOT / 'movee-mobile/node_modules/expo/bin/cli'),
                   'start', '--web', *(['--go', '--lan'] if address else ['--localhost']),
                   '--port', str(PORTS['expo'])]
        cwd = ROOT / 'movee-mobile'
    handler = RotatingFileHandler(LOGS / f'{service}.log', maxBytes=2_000_000, backupCount=3)
    handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    logger = logging.getLogger(service); logger.setLevel(logging.INFO); logger.addHandler(handler)
    secrets = private_values()
    logger.info('Démarrage géré, profil=%s, port=%s', PROFILE, PORTS[service])
    child = subprocess.Popen(command, cwd=cwd, env=env, stdin=subprocess.DEVNULL,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors='replace')
    def terminate(signum, frame):
        child.terminate()
    signal.signal(signal.SIGTERM, terminate)
    signal.signal(signal.SIGINT, terminate)
    for line in child.stdout:
        logger.info('%s', safe_line(line, secrets))
    result = child.wait()
    logger.info('Processus terminé, code=%s', result)
    return result


def main():
    os.umask(0o077)
    for folder in (STATE, LOGS, AGENTS):
        folder.mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['start', 'stop', 'restart', 'status', 'logs', 'iphone', 'loopback', '_run'])
    parser.add_argument('service', nargs='?', choices=ORDER)
    parser.add_argument('--with-expo', action='store_true')
    args = parser.parse_args()
    if args.action == '_run':
        if not args.service:
            parser.error('_run exige un service')
        return run_service(args.service)
    if args.action == 'logs':
        if not args.service:
            parser.error('logs exige backend, redis ou expo')
        path = LOGS / f'{args.service}.log'
        print(path)
        if path.exists():
            print('\n'.join(path.read_text().splitlines()[-60:]))
        return 0
    if args.action == 'status':
        print(f'Profil {PROFILE} — {ROOT}')
        address = network_address()
        if address:
            print(f'Mode iPhone : exp://{address}:{PORTS["expo"]} ; API http://{address}:{PORTS["backend"]}')
        print('MariaDB 3306 : ' + ('disponible (service partagé, jamais arrêté ici)' if listening(3306) else 'indisponible'))
        for service in ORDER:
            pid = job(service)
            state = 'prêt' if ready(service) else 'indisponible'
            owner = f'géré, PID superviseur {pid}' if pid is not None else ('externe' if listening(PORTS[service]) else 'arrêté')
            print(f'{service:8} {PORTS[service]} : {owner}, {state}')
        return 0
    with (STATE / 'control.lock').open('w') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError('Une autre commande MOVEE est en cours.')
        if args.action in ('iphone', 'loopback'):
            if args.service or args.with_expo:
                parser.error('iphone/loopback pilotent uniquement Backend et Expo, sans argument supplémentaire')
            configure_network(args.action == 'iphone')
            return 0
        selected = [args.service] if args.service else list(ORDER if args.with_expo or args.action == 'stop' else ORDER[:2])
        if args.action != 'stop':
            for service in selected:
                owned_plist(service)
                if job(service) is None and listening(PORTS[service]):
                    raise RuntimeError(f'{service} : port {PORTS[service]} occupé par un service externe ; aucun démarrage ni arrêt effectué.')
            if 'backend' in selected:
                validate_backend()
                if not listening(3306):
                    result = call([BREW, 'services', 'start', 'mariadb@11.4'])
                    if result.returncode:
                        raise RuntimeError('Impossible de démarrer le service MariaDB Homebrew existant.')
                    until = time.monotonic() + 20
                    while not listening(3306) and time.monotonic() < until:
                        time.sleep(.5)
                    if not listening(3306):
                        raise RuntimeError('MariaDB 3306 reste indisponible ; aucun service applicatif démarré.')
        if args.action == 'restart':
            for service in reversed(selected):
                stop(service)
        if args.action == 'stop':
            for service in reversed(selected):
                stop(service)
        else:
            if args.service == 'backend' and job('redis') is None:
                start('redis')
            for service in selected:
                start(service)
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (RuntimeError, OSError, ValueError) as error:
        print(f'MOVEE : {error}', file=sys.stderr)
        sys.exit(1)
