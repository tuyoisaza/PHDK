"""Regressions for read-only automation hygiene collector."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "phdk_automation_audit.py"
SPEC = importlib.util.spec_from_file_location("phdk_automation_audit", SCRIPT)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class AutomationAuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, path, body):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8")

    def codes(self):
        return [x["code"] for x in MOD.scan(self.root)["findings"]]

    def test_clean_repo_is_not_remote_compliant(self):
        result = MOD.scan(self.root)
        self.assertEqual(result["findings"], [])
        self.assertEqual(result["remote_state"], "UNVERIFIED")

    def test_scheduled_action_is_high_risk(self):
        self.write(".github/workflows/nightly.yml", "on:\n  schedule:\n    - cron: '0 * * * *'\n")
        self.assertIn("SCHEDULED_ACTION", self.codes())
        self.assertIn("WORKFLOW_REVIEW", self.codes())

    def test_push_workflow_requires_remote_review_not_automatic_deletion(self):
        self.write(".github/workflows/ci.yml", "on:\n  push:\n    branches: [main]\n")
        issues = MOD.scan(self.root)["findings"]
        self.assertEqual([f["code"] for f in issues], ["WORKFLOW_REVIEW"])
        self.assertEqual(issues[0]["severity"], "REVIEW_REMOTE")

    def test_railway_cron_and_always_restart(self):
        self.write("apps/api/railway.json", json.dumps({
            "deploy": {"cronSchedule": "*/5 * * * *", "restartPolicyType": "ALWAYS"}}))
        self.assertIn("RAILWAY_CRON", self.codes())
        self.assertIn("RAILWAY_RESTART", self.codes())

    def test_normal_railway_watch_patterns_and_bounded_restart_not_flagged(self):
        self.write("railway.json", json.dumps({
            "build": {"watchPatterns": ["/apps/api/**"]},
            "deploy": {"restartPolicyType": "ON_FAILURE", "restartPolicyMaxRetries": 5}}))
        self.assertEqual(self.codes(), [])

    def test_production_watcher_flagged_development_watcher_not_flagged(self):
        self.write("package.json", json.dumps({
            "scripts": {"dev": "nodemon server.js", "start": "node server.js"}}))
        self.assertNotIn("PRODUCTION_WATCH", self.codes())
        self.write("package.json", json.dumps({
            "scripts": {"dev": "nodemon server.js", "start": "nodemon server.js"}}))
        self.assertIn("PRODUCTION_WATCH", self.codes())

    def test_vendored_rules_are_not_scanned_as_product(self):
        self.write("phdk-standards/.github/workflows/nightly.yml",
                   "on:\n  schedule:\n    - cron: '* * * * *'\n")
        self.assertEqual(self.codes(), [])

    def test_dependency_bot_is_review_only(self):
        self.write(".github/dependabot.yml", "version: 2\nupdates: []\n")
        self.assertEqual(self.codes(), ["DEPENDENCY_BOT"])


if __name__ == "__main__":
    unittest.main()
