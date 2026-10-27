"""Regression contract for Git history reconciliation and remote retirement.

Not executed during PHDK Auto: production-first policy forbids local runtime tests.
"""
import importlib.util
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "phdk_git_history_cleanup.py"
spec = importlib.util.spec_from_file_location("phdk_git_history_cleanup", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class HistoricalCleanupProofTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime.now(timezone.utc)
        self.sha = "a" * 40
        self.merge = "b" * 40
        self.proof = {
            "branch": "feature/completed", "state": "closed", "merged": True,
            "base": "main", "head": "feature/completed",
            "head_sha": self.sha, "merge_sha": self.merge,
            "merged_at": (self.now - timedelta(days=3)).isoformat(),
            "open_pr_count": 0,
            "pr_url": "https://github.com/example/project/pull/12"
        }
    @patch.object(mod, "branch_valid", return_value=True)
    @patch.object(mod, "ancestor", return_value=True)
    def test_verified_historical_pr_eligible(self, *_):
        self.assertIsNone(mod.validate_proof(
            Path("."), "origin", "main", self.proof,
            "example/project", self.now, True))
    @patch.object(mod, "branch_valid", return_value=True)
    def test_open_pr_is_never_eligible(self, *_):
        self.proof["open_pr_count"] = 1
        self.assertEqual(mod.validate_proof(
            Path("."), "origin", "main", self.proof,
            "example/project", self.now, False),
            "PR_NOT_EXCLUSIVELY_MERGED_TO_TARGET")
    @patch.object(mod, "branch_valid", return_value=True)
    def test_wrong_pr_repository_rejected(self, *_):
        self.proof["pr_url"] = "https://github.com/other/project/pull/12"
        self.assertEqual(mod.validate_proof(
            Path("."), "origin", "main", self.proof,
            "example/project", self.now, False),
            "PR_REPOSITORY_OR_URL_MISMATCH")
    @patch.object(mod, "branch_valid", return_value=True)
    def test_recent_merge_is_not_historical(self, *_):
        self.proof["merged_at"] = self.now.isoformat()
        self.assertEqual(mod.validate_proof(
            Path("."), "origin", "main", self.proof,
            "example/project", self.now, True),
            "RECENT_MERGE_NOT_HISTORICAL")
    @patch.object(mod, "branch_valid", return_value=True)
    @patch.object(mod, "ancestor", return_value=False)
    def test_merge_sha_not_in_main_is_retained(self, *_):
        self.assertEqual(mod.validate_proof(
            Path("."), "origin", "main", self.proof,
            "example/project", self.now, False), "MERGE_SHA_NOT_IN_TARGET")
    def test_protected_branches_are_rejected_before_deletion(self):
        self.assertFalse(mod.branch_valid(Path("."), "main", "main"))
        self.assertFalse(mod.branch_valid(Path("."), "production", "main"))
    def test_malformed_sha_rejected(self):
        self.proof["head_sha"] = "not-a-sha"
        with patch.object(mod, "branch_valid", return_value=True):
            self.assertEqual(mod.validate_proof(
                Path("."), "origin", "main", self.proof,
                "example/project", self.now, False), "MISSING_FULL_SHA")

if __name__ == "__main__":
    unittest.main()
