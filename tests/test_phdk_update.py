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

if __name__ == "__main__":
    unittest.main()
