"""Source-only regression scenarios for forced-upgrade remote-main proof."""
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "gate", Path(__file__).resolve().parents[1] / "scripts" / "phdk_upgrade_remote_gate.py"
)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class RemoteUpgradeGateTests(unittest.TestCase):
    def test_manifest_requires_version_and_manifest(self):
        with self.assertRaisesRegex(ValueError, "incomplete manifest"):
            gate.manifest_paths("README.md | README.md")

    def test_manifest_rejects_path_traversal(self):
        with self.assertRaisesRegex(ValueError, "unsafe manifest"):
            gate.manifest_paths(
                "VERSION | VERSION\nX | ../secrets\n"
                "PHDK_MANIFEST.txt | PHDK_MANIFEST.txt"
            )

    def test_manifest_rejects_duplicates(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            gate.manifest_paths(
                "VERSION | VERSION\nVERSION | VERSION\n"
                "PHDK_MANIFEST.txt | PHDK_MANIFEST.txt"
            )

    def test_manifest_accepts_legitimate_paths(self):
        self.assertEqual(
            gate.manifest_paths(
                "VERSION | VERSION\n# comment\n"
                "PHDK_MANIFEST.txt | PHDK_MANIFEST.txt\n"
            ),
            ["VERSION", "PHDK_MANIFEST.txt"],
        )


if __name__ == "__main__":
    unittest.main()
