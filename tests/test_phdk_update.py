"""Offline safety checks for the centralized updater."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("phdk_update", Path(__file__).resolve().parents[1] / "scripts" / "phdk_update.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class UpdateTests(unittest.TestCase):
    def test_manifest_requires_version(self):
        self.assertRaises(ValueError, mod.manifest, "a | b")
    def test_duplicate_manifest_destination(self):
        self.assertRaises(ValueError, mod.manifest, "VERSION | VERSION\na | VERSION")
    def test_safe_manifest(self):
        self.assertRaises(ValueError, mod.manifest, "VERSION | VERSION\nx | ../escape")
    def test_semver(self):
        self.assertEqual(mod.valid_version("2.51.0"), (2, 51, 0))
        self.assertRaises(ValueError, mod.valid_version, "2.51")
    def test_newer_local(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            local = p / "phdk-standards"
            local.mkdir()
            remote = p / "remote"
            remote.mkdir()
            (local / "VERSION").write_text("3.0.0")
            (remote / "VERSION").write_text("2.51.0")
            (remote / "PHDK_MANIFEST.txt").write_text("VERSION | VERSION\n")
            (local / "PHDK_MANIFEST.txt").write_text("VERSION | VERSION\n")
            self.assertEqual(mod.run(p, remote)["status"], "NEWER_LOCAL")

if __name__ == "__main__":
    unittest.main()
