"""Verify static UAT register parsing and reconciliation with synthetic Markdown."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/phdk_uat_defect_register.py"
HEADER = "| ID | Cases | Severity | Observed build | Initial evidence | State | Fixed build | Retest build | Retest result | Retest evidence | Next action |"
FIELDS = [field.strip() for field in HEADER.strip("|").split("|")]
BASE = dict(zip(FIELDS, ["DEF-01", "UAT-1", "P2", "sha-001", "evidence/first.png",
                         "OPEN", "-", "-", "-", "-", "Fix form field order"]))
FIXED = {"State": "VERIFIED_RESOLVED", "Fixed build": "sha-002", "Retest build": "sha-002",
         "Retest result": "PASS", "Retest evidence": "retest.md#UAT-1", "Next action": "-"}


class UatDefectRegisterTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.directory = Path(temp.name)

    def report(self, name, *rows):
        content = ["# UAT report", "", "## Defect register", "", HEADER, "|---" * len(FIELDS) + "|"]
        for changes in rows:
            row = {**BASE, **changes}
            content.append("| " + " | ".join(row[k] for k in FIELDS) + " |")
        path = self.directory / name
        path.write_text("\n".join(content) + "\n", encoding="utf-8")
        return path

    def check(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)

    def test_empty_register_and_nonblocking_finding(self):
        for rows, total in (([], 0), ([{}], 1)):
            with self.subTest(total=total):
                result = self.check(self.report("report.md", *rows))
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(f"OPEN={total},", result.stdout)
                self.assertNotIn("ACCEPTED", result.stdout)

    def test_deployed_retest_for_all_cases(self):
        current = {"Cases": "UAT-1, UAT-2", **FIXED,
                   "Retest result": "UAT-1=PASS, UAT-2=PASS"}
        prior = self.report("prior.md", {})
        result = self.check(self.report("now.md", current), "--previous", prior)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("VERIFIED_RESOLVED=1", result.stdout)
        for edit in ({"Retest build": "sha-003"}, {"Retest result": "UAT-1=PASS"},
                     {"Retest result": "PASS"}, {"Retest result": "UAT-1=PASS,UAT-2=BLOCKED"},
                     {"Retest result": "UAT-1=PASS,UAT-1=PASS"}, {"Retest evidence": "-"}):
            with self.subTest(edit=edit):
                self.assertNotEqual(self.check(self.report("now.md", {**current, **edit})).returncode, 0)

    def test_prior_pending_and_original_observation_survive(self):
        prior = self.report("prior.md", {"State": "RETEST_BLOCKED"})
        for rows in ([], [{"Cases": "UAT-2"}], [{"Observed build": "sha-002"}],
                     [{"Initial evidence": "replaced.md"}]):
            with self.subTest(rows=rows):
                self.assertNotEqual(self.check(self.report("now.md", *rows), "--previous", prior).returncode, 0)
        separate = self.report("old-resolved.md", FIXED)
        self.assertEqual(self.check(self.report("empty.md"), "--previous", separate).returncode, 0)

    def test_reopened_requires_observed_failed_attempt(self):
        reopened = {**FIXED, "State": "REOPENED", "Retest result": "FAIL", "Next action": "Repair regression"}
        self.assertEqual(self.check(self.report("now.md", reopened)).returncode, 0)
        for edit in ({"Retest result": "BLOCKED"}, {"Retest evidence": "-"}, {"Retest build": "-"}):
            with self.subTest(edit=edit):
                self.assertNotEqual(self.check(self.report("now.md", {**reopened, **edit})).returncode, 0)

    def test_duplicate_id_and_malformed_heading(self):
        result = self.check(self.report("duplicate.md", {}, {}))
        self.assertIn("duplicate DEF-01", result.stderr)
        path = self.report("empty.md")
        path.write_text("# No register\n", encoding="utf-8")
        self.assertNotEqual(self.check(path).returncode, 0)

    def test_relative_links_refer_to_the_original_and_a_new_replay(self):
        prior = self.report("prior.md", {"Initial evidence": "[old](#initial)"})
        closed = {**FIXED, "Initial evidence": "[old](prior.md#initial)"}
        result = self.check(self.report("new.md", closed), "--previous", prior)
        self.assertEqual(result.returncode, 0, result.stderr)
        repeated = {**closed, "Retest evidence": "[other label](./prior.md#initial)"}
        self.assertNotEqual(self.check(self.report("new.md", repeated)).returncode, 0)
        contradictory = {**closed, "State": "RETEST_BLOCKED", "Next action": "Reconnect"}
        self.assertNotEqual(self.check(self.report("new.md", contradictory)).returncode, 0)
