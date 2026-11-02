"""Configuration locale, sans modification de la configuration VPS."""
import os
import ipaddress
port = os.environ.get('MOVEE_DEV_BACKEND_PORT', '5050')
bind = ['127.0.0.1:' + port]
if os.environ.get('MOVEE_DEV_LAN_ADDRESS'):
    address = ipaddress.IPv4Address(os.environ['MOVEE_DEV_LAN_ADDRESS'])
    if not any(address in ipaddress.IPv4Network(net) for net in ('10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16')):
        raise ValueError('Adresse LAN privée requise')
    bind.append(f'{address}:{port}')
workers = 1
worker_class = 'sync'
preload_app = False
reload = False
accesslog = None  # Pas de requêtes, query strings, cookies ou Authorization dans les logs.
errorlog = '-'
loglevel = 'info'
capture_output = True
forwarded_allow_ips = ''  # Aucun proxy dans cette configuration.
umask = 0o077
# Désactiver l'interface de contrôle supplémentaire : launchd gère le processus.
control_socket_disable = True
