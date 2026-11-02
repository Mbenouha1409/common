"""Vérifications ciblées du pilotage, sans lancer de service ni écrire en base."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import plistlib

spec = importlib.util.spec_from_file_location('movee_dev', Path(__file__).with_name('movee_dev.py'))
dev = importlib.util.module_from_spec(spec); spec.loader.exec_module(dev)


class ControlTest(unittest.TestCase):
    def test_redaction(self):
        for line in ('Authorization: Bearer abc', 'password=bonjour', 'Cookie: secret', 'access_token=abc'):
            self.assertEqual(dev.safe_line(line, []), '[ligne sensible masquée]')
        self.assertNotIn('mv1_abc', dev.safe_line('session mv1_abc', []))
        self.assertNotIn('passe-privee', dev.safe_line('oops passe-privee', ['passe-privee']))
        self.assertNotIn('secret=value', dev.safe_line('GET /page?secret=value', []))
        self.assertNotIn('pwd', dev.safe_line('redis://user:pwd@localhost', []))

    def test_foreign_plist_is_preserved(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(dev, 'AGENTS', Path(tmp)):
            path = Path(tmp) / (dev.label('backend') + '.plist')
            raw = plistlib.dumps({'Label': dev.label('backend'), 'ProgramArguments': ['/bin/sleep', '100']})
            path.write_bytes(raw)
            with self.assertRaises(RuntimeError):
                dev.owned_plist('backend')
            self.assertEqual(path.read_bytes(), raw)

    def test_external_port_is_never_stopped(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(dev, 'AGENTS', Path(tmp)), \
             patch.object(dev, 'job', return_value=None), patch.object(dev, 'call') as execute:
            dev.stop('backend')
            execute.assert_not_called()

    def test_stop_waits_for_launchd_unload_before_restart(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(dev, 'AGENTS', Path(tmp)), \
             patch.object(dev, 'job', side_effect=[123, 123, None, None]), \
             patch.object(dev, 'listening', return_value=False), \
             patch.object(dev.time, 'sleep'), patch.object(dev, 'call') as execute:
            path = Path(tmp) / (dev.label('backend') + '.plist')
            path.write_bytes(plistlib.dumps({'Label': dev.label('backend'),
                'ProgramArguments': [str(dev.PYTHON), '-B', str(Path(dev.__file__).resolve()), '_run', 'backend']}))
            execute.return_value.returncode = 0
            dev.stop('backend')
            self.assertFalse(path.exists())
            execute.assert_called_once_with(['/bin/launchctl', 'bootout', f'{dev.DOMAIN}/{dev.label("backend")}'])

    def test_second_start_does_not_bootstrap(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(dev, 'AGENTS', Path(tmp)), \
             patch.object(dev, 'job', return_value=123), patch.object(dev, 'ready', return_value=True), \
             patch.object(dev, 'call') as execute:
            dev.start('backend')
            execute.assert_not_called()

    def test_conflict_does_not_bootstrap(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(dev, 'AGENTS', Path(tmp)), \
             patch.object(dev, 'job', return_value=None), patch.object(dev, 'listening', return_value=True), \
             patch.object(dev, 'call') as execute:
            with self.assertRaises(RuntimeError):
                dev.start('backend')
            execute.assert_not_called()

    def test_network_mode_is_explicit_private_and_check_stays_loopback(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(dev, 'STATE', Path(tmp)), patch.object(dev, 'PROFILE', 'local'):
            self.assertIsNone(dev.network_address())
            path = Path(tmp) / 'network.json'
            path.write_text('{"lan_address":"192.168.1.36"}')
            self.assertEqual(dev.network_address(), '192.168.1.36')
            with patch.object(dev, 'PROFILE', 'check'):
                self.assertIsNone(dev.network_address())
            path.write_text('{"lan_address":"0.0.0.0"}')
            with self.assertRaises(RuntimeError):
                dev.network_address()

    def test_iphone_mode_preserves_existing_redis_and_only_restarts_two_services(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(dev, 'STATE', Path(tmp)), patch.object(dev, 'PROFILE', 'local'), \
             patch.object(dev, 'validate_backend'), patch.object(dev, 'update_public_api') as api, patch.object(dev, 'owned_plist'), \
             patch.object(dev, 'job', return_value=123), patch.object(dev, 'stop') as stop, \
             patch.object(dev, 'start') as start, patch.object(dev, 'call') as execute:
            execute.return_value.returncode = 0
            execute.return_value.stdout = '192.168.1.36\n'
            dev.configure_network(True)
            self.assertEqual([c.args[0] for c in stop.call_args_list], ['expo', 'backend'])
            self.assertEqual([c.args[0] for c in start.call_args_list], ['backend', 'expo'])
            self.assertEqual(dev.network_address(), '192.168.1.36')
            api.assert_called_with('192.168.1.36')
            self.assertEqual((Path(tmp) / 'network.json').stat().st_mode & 0o777, 0o600)
            dev.configure_network(False)
            self.assertIsNone(dev.network_address())

    def test_non_private_wifi_is_refused_before_stopping_services(self):
        with patch.object(dev, 'PROFILE', 'local'), patch.object(dev, 'call') as execute, patch.object(dev, 'stop') as stop:
            execute.return_value.returncode = 0
            execute.return_value.stdout = '8.8.8.8\n'
            with self.assertRaises(RuntimeError):
                dev.configure_network(True)
            stop.assert_not_called()

    def test_native_virtual_env_and_supervisor_use_same_api_without_changing_other_values(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(dev, 'ROOT', Path(tmp)):
            folder = Path(tmp) / 'movee-mobile'
            folder.mkdir()
            path = folder / '.env.local'
            path.write_text('# configuration\nEXPO_PUBLIC_API_URL=http://127.0.0.1:5050\nOTHER_VALUE=preserved\n')
            dev.update_public_api('192.168.1.36')
            self.assertEqual(path.read_text(), '# configuration\nEXPO_PUBLIC_API_URL=http://192.168.1.36:5050\nOTHER_VALUE=preserved\n')
            dev.update_public_api(None)
            self.assertIn('EXPO_PUBLIC_API_URL=http://127.0.0.1:5050\n', path.read_text())
            self.assertIn('OTHER_VALUE=preserved\n', path.read_text())

    def test_user_facing_services_are_not_throttled_as_background_jobs(self):
        for service, policy in (('backend', 'Interactive'), ('expo', 'Interactive'), ('redis', 'Background')):
            with self.subTest(service=service), tempfile.TemporaryDirectory() as tmp, \
                 patch.object(dev, 'AGENTS', Path(tmp)), patch.object(dev, 'job', side_effect=[None, 123]), \
                 patch.object(dev, 'listening', side_effect=lambda port: port == 3306), \
                 patch.object(dev, 'ready', return_value=True), patch.object(dev, 'validate_backend'), \
                 patch.object(dev, 'call') as execute:
                execute.return_value.returncode = 0
                dev.start(service)
                data = plistlib.loads((Path(tmp) / (dev.label(service) + '.plist')).read_bytes())
                self.assertEqual(data['ProcessType'], policy)
                self.assertEqual(data['ProgramArguments'][-1], service)


if __name__ == '__main__':
    unittest.main()
