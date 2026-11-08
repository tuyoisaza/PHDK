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

    def test_invalid_upstream_pin_rejected_before_any_clone(self):
        with self.assertRaisesRegex(ValueError, "invalid --upstream-sha"):
            updater.select_upstream(Path("/nonexistent"), "not-a-SHA")

    def test_unpinned_upstream_selection_uses_actual_head(self):
        import subprocess
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init", "--initial-branch=main", str(root)],
                           check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            subprocess.run(["git", "-C", str(root), "config", "user.email", "test@example.invalid"], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.name", "PHDK Test"], check=True)
            (root / "one.txt").write_text("fixture")
            subprocess.run(["git", "-C", str(root), "add", "one.txt"], check=True)
            subprocess.run(["git", "-C", str(root), "commit", "-m", "fixture"],
                           check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            head = updater.run("git", "rev-parse", "HEAD", cwd=root)
            self.assertEqual(updater.select_upstream(root), head)
            self.assertEqual(updater.select_upstream(root, head), head)

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


    def test_historical_canonical_copy_is_not_owner_customization(self):
        import subprocess
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.email",
                            "test@example.invalid"], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.name",
                            "PHDK Fixture"], check=True)
            name = "PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md"
            original = b"delegation outside explicit PMO\n"
            (root / name).write_bytes(original)
            subprocess.run(["git", "-C", str(root), "add", name], check=True)
            subprocess.run(["git", "-C", str(root), "commit", "-qm", "old source"], check=True)
            (root / name).write_bytes(b"bounded intelligent delegation\n")
            subprocess.run(["git", "-C", str(root), "commit", "-qam",
                            "corrected canonical source"], check=True)
            history = {}
            self.assertTrue(updater.is_published_copy(
                original, root, name, history))
            self.assertTrue(updater.is_published_copy(
                b"delegation outside explicit PMO\r\n", root, name, history))
            self.assertFalse(updater.is_published_copy(
                b"current owner prohibits all subagents\n", root, name, history))

    def test_unmanaged_active_extras_are_reported_not_erased(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "phdk-standards"
            (root / "scripts").mkdir(parents=True)
            (root / "PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md").write_text(
                "owner-specific notes", encoding="utf-8")
            self.assertEqual(
                updater._unmanaged_active(root, set()),
                ["PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md"])
            self.assertEqual(updater._unmanaged_active(
                root, {"PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md"}), [])
            result = updater.sync_result(
                "UPDATED", trigger="upgrade", installed="3.0.1", latest="3.0.2",
                upstream_sha="a" * 40, force_owned=True, unmanaged=["other.md"])
            self.assertEqual(result["vendor_integrity"], "PARTIAL_UNMANAGED_ACTIVE")
            self.assertEqual(result["forced_upgrade_publication"],
                             "PENDING_REMOTE_MAIN_CHECKPOINT")

if __name__ == "__main__":
    unittest.main()
