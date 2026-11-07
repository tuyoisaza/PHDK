"""Synthetic isolated Git regressions for forced-upgrade remote object proof."""
import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "gate", Path(__file__).resolve().parents[1] / "scripts" / "phdk_upgrade_remote_gate.py"
)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


def run(cwd, *args):
    return subprocess.check_output(["git", "-C", str(cwd), *args], stderr=subprocess.PIPE).decode().strip()


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

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.repo, self.origin = root / "repo", root / "origin.git"
        self.repo.mkdir()
        run(self.repo, "init", "--initial-branch=main")
        run(self.repo, "config", "user.email", "test@example.invalid")
        run(self.repo, "config", "user.name", "Test")
        run(self.repo, "config", "core.autocrlf", "false")
        run(root, "init", "--bare", str(self.origin))
        run(self.repo, "remote", "add", "origin", str(self.origin))
        standards = self.repo / "phdk-standards"
        standards.mkdir()
        (self.repo / ".gitattributes").write_text("* text=auto\n", encoding="utf-8")
        (standards / "VERSION").write_bytes(b"2.91.1\n")
        (standards / "PHDK_MANIFEST.txt").write_bytes(
            b"VERSION | VERSION\nPHDK_MANIFEST.txt | PHDK_MANIFEST.txt\n"
            b"README.md | README.md\nsample.bin | sample.bin\n"
        )
        (standards / "README.md").write_bytes(b"First\nSecond\n")
        (standards / "sample.bin").write_bytes(b"abc\x00def\r\n")
        run(self.repo, "add", ".")
        run(self.repo, "commit", "-m", "fixture")
        run(self.repo, "push", "-u", "origin", "main")

    def tearDown(self):
        self.tmp.cleanup()

    def check(self):
        return gate.verify(self.repo, "origin", "main", "2.91.1")

    def test_exact_git_blobs_pass(self):
        proof = self.check()
        self.assertEqual(proof["status"], "PASS")
        self.assertEqual(proof["representation_only_count"], 0)

    def test_crlf_checkout_is_representation_not_mismatch(self):
        (self.repo / "phdk-standards/README.md").write_bytes(b"First\r\nSecond\r\n")
        run(self.repo, "config", "core.autocrlf", "true")
        proof = self.check()
        self.assertEqual(proof["status"], "PASS", proof["mismatches"])
        self.assertGreaterEqual(proof["representation_only_count"], 1)

    def test_actual_text_change_is_not_hidden(self):
        (self.repo / "phdk-standards/README.md").write_bytes(b"Different\r\nSecond\r\n")
        run(self.repo, "config", "core.autocrlf", "true")
        proof = self.check()
        self.assertEqual(proof["status"], "BLOCKED")
        self.assertTrue(any("CONTENT_MISMATCH" in x for x in proof["mismatches"]))

    def test_binary_change_is_not_normalized(self):
        (self.repo / "phdk-standards/sample.bin").write_bytes(b"abc\x00DIFFERENT\r\n")
        self.assertEqual(self.check()["status"], "BLOCKED")

    def test_changed_local_attributes_fail_closed(self):
        (self.repo / ".gitattributes").write_text("* text=auto\n*.md -text\n", encoding="utf-8")
        (self.repo / "phdk-standards/README.md").write_bytes(b"First\r\nSecond\r\n")
        proof = self.check()
        self.assertEqual(proof["status"], "BLOCKED")
        self.assertTrue(any("ATTRIBUTE_MISMATCH" in x for x in proof["mismatches"]))

    def test_custom_filter_is_not_executed(self):
        (self.repo / ".gitattributes").write_text(
            "* text=auto\nphdk-standards/README.md filter=danger\n", encoding="utf-8"
        )
        run(self.repo, "add", ".gitattributes")
        run(self.repo, "commit", "-m", "set filter attribute")
        run(self.repo, "push", "origin", "main")
        marker = Path(self.tmp.name) / "unexpected.txt"
        run(self.repo, "config", "filter.danger.clean",
            f"python -c \"open('{marker.as_posix()}','w').write('bad')\"")
        (self.repo / "phdk-standards/README.md").write_bytes(b"First\r\nSecond\r\n")
        proof = self.check()
        self.assertEqual(proof["status"], "BLOCKED")
        self.assertTrue(any("CUSTOM_FILTER_UNVERIFIED" in x for x in proof["mismatches"]))
        self.assertFalse(marker.exists())

    def test_manifest_mapping_drift_blocks(self):
        path = self.repo / "phdk-standards/PHDK_MANIFEST.txt"
        path.write_bytes(path.read_bytes() + b"extra | extra\n")
        with self.assertRaisesRegex(RuntimeError, "manifest mappings differ"):
            self.check()


if __name__ == "__main__":
    unittest.main()
