"""Offline synthetic regression cases for universal PHDK test runner."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RUNNER = Path(__file__).resolve().parents[1] / "scripts" / "phdk_test_runner.py"


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "tests").mkdir()
        (self.root / "ok.py").write_text("print('TEST_OK')\n", encoding="utf-8")
        (self.root / "fail.py").write_text("import sys; print('api_key=secret123'); sys.exit(3)\n", encoding="utf-8")
        self.checks = [{"id": "ok", "profile": "local", "kind": "unit",
                        "argv": [sys.executable, "ok.py"], "timeout_sec": 10}]

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, checks):
        (self.root / "tests" / "phdk-tests.json").write_text(
            json.dumps({"schema_version": 1, "checks": checks}), encoding="utf-8")

    def run_tool(self, *flags):
        return subprocess.run([sys.executable, str(RUNNER), "--root", str(self.root), *flags],
                              capture_output=True, text=True, timeout=20)

    def report(self):
        return json.loads(next((self.root / ".phdk-test-results").glob("*/report.json")).read_text())

    def test_local_pass_with_evidence(self):
        self.write(self.checks)
        p = self.run_tool()
        self.assertEqual(p.returncode, 0, p.stderr)
        report = self.report()
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["counts"]["PASS"], 1)
        self.assertIn("TEST_OK", (next((self.root / ".phdk-test-results").glob("*/ok.log"))).read_text())

    def test_failed_check_keeps_log_and_redacts(self):
        self.write([{**self.checks[0], "id": "bad", "argv": [sys.executable, "fail.py"]}])
        p = self.run_tool()
        self.assertEqual(p.returncode, 1)
        log = next((self.root / ".phdk-test-results").glob("*/bad.log")).read_text()
        self.assertNotIn("secret123", log)
        self.assertIn("[REDACTED]", log)
        self.assertEqual(self.report()["status"], "FAIL")

    def test_fail_fast_does_not_claim_other_check_passed(self):
        self.write([{**self.checks[0], "argv": [sys.executable, "fail.py"]},
                    {**self.checks[0], "id": "second"}])
        self.assertEqual(self.run_tool().returncode, 1)
        self.assertEqual([x["status"] for x in self.report()["checks"]], ["FAIL", "NOT_RUN"])

    def test_missing_profile_is_not_false_green(self):
        self.write([{**self.checks[0], "profile": "uat", "kind": "api"}])
        self.assertEqual(self.run_tool().returncode, 2)

    def test_shell_wrapper_rejected(self):
        self.write([{**self.checks[0], "argv": ["sh", "-c", "true"]}])
        self.assertEqual(self.run_tool().returncode, 2)

    def test_uat_requires_current_mandate_and_target(self):
        self.write([{**self.checks[0], "profile": "uat", "kind": "api"}])
        self.assertNotEqual(self.run_tool("--profile", "uat").returncode, 0)
        p = self.run_tool("--profile", "uat", "--uat-authorized",
                          "--uat-run-id", "test-run-0001", "--uat-target", "https://example.org")
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(self.report()["profile"], "uat")

    def test_unsafe_uat_mutations_without_cleanup_rejected(self):
        self.write([{**self.checks[0], "profile": "uat", "kind": "api",
                     "mutates": True, "run_owned_data": True}])
        self.assertEqual(self.run_tool("--profile", "uat", "--validate").returncode, 2)

    def test_validate_does_not_execute(self):
        self.write(self.checks)
        self.assertEqual(self.run_tool("--validate").returncode, 0)
        self.assertFalse((self.root / ".phdk-test-results").exists())


if __name__ == "__main__":
    unittest.main()
