"""Contrôles locaux explicites ; aucune migration ni création de compte.

--snapshot/--compare lisent MariaDB et n'enregistrent que des empreintes.
--http-acceptance utilise les comptes existants : last_login_at, updated_at, updated_by des comptes de recette et Redis évoluent.
Ce contrôle HTTP n'est PAS une recette navigateur.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.request

import pymysql
from dotenv import dotenv_values
from movee_dev import ROOT, PORTS, validate_backend


def snapshot():
    validate_backend()
    cfg = dotenv_values(ROOT / '.env')
    connection = pymysql.connect(host='127.0.0.1', port=3306, user=cfg['DB_USER'],
                                 password=cfg['DB_PASSWORD'], database='movee_app_local', charset='utf8mb4')
    output = {}
    try:
        with connection.cursor() as cursor:
            cursor.execute('START TRANSACTION WITH CONSISTENT SNAPSHOT, READ ONLY')
            cursor.execute('SHOW FULL TABLES WHERE Table_type = %s', ('BASE TABLE',))
            tables = [row[0] for row in cursor.fetchall()]
            for table in tables:
                quoted = '`' + table.replace('`', '``') + '`'
                cursor.execute('SELECT * FROM ' + quoted)
                columns = [item[0] for item in cursor.description]
                hashes = []
                for row in cursor.fetchall():
                    is_acceptance_user = table == 'users' and row[columns.index('email')] in {
                        'pages-coach-a@example.test', 'pages-coach-b@example.test',
                        'pages-member-a@example.test', 'pages-member-b@example.test', 'pages-member-c@example.test'}
                    values = [value for col, value in zip(columns, row) if not
                              (is_acceptance_user and col in ('last_login_at', 'updated_at', 'updated_by'))]
                    hashes.append(hashlib.sha256(json.dumps(values, default=str, ensure_ascii=False).encode()).hexdigest())
                hashes.sort()
                output[table] = {'rows': len(hashes), 'sha256': hashlib.sha256(''.join(hashes).encode()).hexdigest()}
    finally:
        connection.rollback(); connection.close()
    return output


def request(path, body=None, token=None, method=None):
    headers = {'Origin': f'http://localhost:{PORTS["expo"]}'}
    if token:
        headers['Authorization'] = 'Bearer ' + token
    if body is not None:
        headers['Content-Type'] = 'application/json'
    req = urllib.request.Request(f'http://127.0.0.1:{PORTS["backend"]}{path}', headers=headers,
                                  data=json.dumps(body).encode() if body is not None else None, method=method)
    if method == 'OPTIONS':
        req.add_header('Access-Control-Request-Method', 'POST')
        req.add_header('Access-Control-Request-Headers', 'authorization,content-type')
    try:
        response = urllib.request.urlopen(req, timeout=15)
    except urllib.error.HTTPError as error:
        response = error
    with response:
        raw = response.read()
        assert 'Access-Control-Allow-Credentials' not in response.headers, 'Cookies CORS activés'
        assert 'Set-Cookie' not in response.headers, 'Cookie inattendu sur API Mobile'
        assert response.headers.get('Access-Control-Allow-Origin') == '*', 'Origine non autorisée'
        assert 'retry-after' in response.headers.get('Access-Control-Expose-Headers', '').lower(), 'Retry-After non exposé'
        data = json.loads(raw) if raw else {}
        return response.status, data, response.headers


def acceptance():
    credentials = json.loads((Path.home() / '.config/movee/mobile-pages-acceptance-credentials.json').read_text())
    status, _, headers = request('/api/mobile-pages/config', method='OPTIONS')
    assert status == 200
    allowed = headers.get('Access-Control-Allow-Headers', '').lower()
    assert 'authorization' in allowed and 'content-type' in allowed
    assert 'gunicorn' in headers.get('Server', '').lower(), 'Backend non servi par Gunicorn'
    calls = 1
    for name in ('member_a', 'member_b', 'member_c', 'coach_a', 'coach_b'):
        status, data, _ = request('/api/mobile-auth/login', credentials[name])
        assert status == 200 and data.get('success'), 'Connexion de recette refusée'
        token = data['access_token']; calls += 1
        try:
            status, data, _ = request('/api/mobile-pages', token=token); calls += 1
            assert status == 200 and len(data['pages']) == 3, 'Catalogue inattendu'
            totals = []
            for page in data['pages']:
                uid = page['page_uid']
                status, _, _ = request('/api/mobile-pages/config', {'page_uid': uid}, token); calls += 1
                assert status == 200
                status, result, _ = request('/api/mobile-pages/data', {'page_uid': uid, 'limit': 20,
                                                   'offset': 0, 'sort': None, 'filters': []}, token); calls += 1
                assert status == 200
                totals.append(result['pagination']['total'])
            assert sorted(totals) == ([1, 1, 2] if name.startswith('coach') else [1, 1, 1]), 'Données de recette inattendues'
            print(name + ' : catalogue, configurations et listes conformes')
        finally:
            status, _, _ = request('/api/mobile-auth/logout', {}, token); calls += 1
            assert status == 200
        status, _, _ = request('/api/mobile-auth/me', token=token); calls += 1
        assert status == 401, 'Jeton non révoqué'
    # Quota via identifiant synthétique inexistant, sans modifier les comptes.
    # Respecte le quota réel : aucun effacement Redis ni changement des limites.
    for _ in range(6):
        status, _, headers = request('/api/mobile-auth/login', {'email': 'infra-quota@example.test',
                                                               'password': 'invalid-local-check'})
        calls += 1
        if status == 429:
            assert headers.get('Retry-After', '').isdigit()
            break
    else:
        raise AssertionError('Quota/Retry-After réel non observé')
    print(f'{calls} appels HTTP réels : Bearer, CORS, révocation et Retry-After conformes ; sans recette navigateur.')


def main():
    os.umask(0o077)
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--snapshot', type=Path)
    group.add_argument('--compare', type=Path)
    group.add_argument('--http-acceptance', action='store_true')
    args = parser.parse_args()
    if args.http_acceptance:
        acceptance()
    elif args.snapshot:
        # Ne jamais écraser silencieusement un état de référence.
        with args.snapshot.open('x') as stream:
            json.dump(snapshot(), stream)
        print('Empreintes de données enregistrées (audit de connexion des cinq comptes de recette exclu).')
    else:
        before = json.loads(args.compare.read_text()); after = snapshot()
        changed = sorted(table for table in set(before) | set(after) if before.get(table) != after.get(table))
        if changed:
            raise AssertionError('Tables modifiées : ' + ', '.join(changed))
        print(f'{len(after)} tables : nombres et empreintes des lignes inchangés (hors audit de connexion des cinq comptes de recette).')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        # Les exceptions SQL/HTTP peuvent contenir des données privées : pas de traceback ni repr.
        print('Contrôle interrompu : ' + type(error).__name__ +
              ((' — ' + str(error)) if isinstance(error, AssertionError) else ' (détail privé non affiché)'), file=sys.stderr)
        sys.exit(1)
