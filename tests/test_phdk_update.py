"""Regression checks for the PHDK conservative updater."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("updater", Path(__file__).resolve().parents[1] / "scripts" / "phdk_update.py")
updater = importlib.util.module_from_spec(spec)
spec.loader.exec_module(updater)

class UpdateTests(unittest.TestCase):
    def test_not_installed(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "not installed"):
                updater.sync(Path(tmp))

    def test_git_error_propagates(self):
        with self.assertRaises(Exception):
            updater.run("git", "this-command-does-not-exist")

    def test_no_implicit_network_calls_on_import(self):
        self.assertTrue(callable(updater.sync))

    def test_force_requires_explicit_upgrade_trigger(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "--force-owned requires"):
                updater.sync(Path(tmp), force_owned=True)

    def test_force_copier_never_claims_remote_main_published(self):
        report = updater.sync_result(
            "UPDATED", trigger="upgrade", installed="2.70.0",
            latest="2.71.1", upstream_sha="a" * 40, files=3,
            force_owned=True, overwritten=["phdk-standards/AGENTS.md"],
        )
        self.assertEqual(report["remote_main_verification"], "UNVERIFIED")
        self.assertEqual(report["forced_upgrade_publication"], "PENDING_REMOTE_MAIN_CHECKPOINT")
        self.assertEqual(report["auto_force_handoff"], "PENDING_PUBLICATION")
        self.assertEqual(report["overwritten_owned_paths"], ["phdk-standards/AGENTS.md"])

    def test_bare_upgrade_has_no_publication_authority(self):
        report = updater.sync_result(
            "CURRENT", trigger="upgrade", installed="2.71.1",
            latest="2.71.1", upstream_sha="a" * 40,
        )
        self.assertEqual(report["forced_upgrade_publication"], "NOT_AUTHORIZED_BY_COPIER")
        self.assertEqual(report["remote_main_verification"], "UNVERIFIED")

if __name__ == "__main__":
    unittest.main()
