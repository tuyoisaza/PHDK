import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "phdk_completion_gate.py"
SPEC = importlib.util.spec_from_file_location("phdk_completion_gate", SCRIPT)
GATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GATE)


class VersionExtractionTests(unittest.TestCase):
    def test_plain_text_version_remains_supported(self):
        self.assertEqual(GATE.extract_version("v2.50.9\n"), "v2.50.9")

    def test_json_version_property_is_read(self):
        self.assertEqual(
            GATE.extract_version('{"name":"app","version":"5.1.2"}', "version"),
            "5.1.2",
        )

    def test_nested_json_version_property_is_read(self):
        self.assertEqual(
            GATE.extract_version('{"release":{"version":"5.1.2"}}', "release.version"),
            "5.1.2",
        )

    def test_missing_json_property_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "not found"):
            GATE.extract_version('{"name":"app"}', "version")

    def test_unsafe_json_property_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "unsafe version_property"):
            GATE.extract_version('{"version":"5.1.2"}', "../version")


class RemoteGateTests(unittest.TestCase):
    def git(self, cwd, *args):
        subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True)

    def test_remote_gate_accepts_json_version_from_merged_commit(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            remote = root / "remote.git"
            project = root / "project"
            remote.mkdir()
            project.mkdir()
            self.git(remote, "init", "--bare", "--initial-branch=main")
            self.git(project, "init", "--initial-branch=main")
            self.git(project, "config", "user.name", "PHDK Test")
            self.git(project, "config", "user.email", "phdk-test@example.invalid")
            (project / "package.json").write_text(
                json.dumps({"name": "fixture", "version": "5.1.2"}) + "\n",
                encoding="utf-8",
            )
            self.git(project, "add", "package.json")
            self.git(project, "commit", "-m", "fixture")
            sha = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=project,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            self.git(project, "remote", "add", "origin", str(remote))
            self.git(project, "push", "origin", "HEAD:refs/heads/main")
            evidence = {
                "goal": "JSON version gate regression",
                "target_branch": "main",
                "expected_version": "5.1.2",
                "version_file": "package.json",
                "version_property": "version",
                "merged_commit_sha": sha,
                "pr_url": "https://github.com/example/project/pull/1",
                "checks": {"focused_tests": {"status": "PASS", "evidence": "fixture"}},
            }
            evidence_path = root / "evidence.json"
            evidence_path.write_text(json.dumps(evidence), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--evidence", str(evidence_path)],
                cwd=project,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn(f"PASS: remote origin/main SHA={sha} VERSION=5.1.2", result.stdout)

            evidence["version_property"] = "missing"
            evidence_path.write_text(json.dumps(evidence), encoding="utf-8")
            override = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--evidence",
                    str(evidence_path),
                    "--version-property",
                    "version",
                ],
                cwd=project,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(override.returncode, 0, override.stdout + override.stderr)

            evidence["version_property"] = "version"
            evidence["expected_version"] = "5.1.3"
            evidence_path.write_text(json.dumps(evidence), encoding="utf-8")
            mismatch = subprocess.run(
                [sys.executable, str(SCRIPT), "--evidence", str(evidence_path)],
                cwd=project,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(mismatch.returncode, 1)
            self.assertIn("remote version source '5.1.2' != expected '5.1.3'", mismatch.stdout)


if __name__ == "__main__":
    unittest.main()
