"""Regression contract for Git history reconciliation and remote preservation.

Not executed during PHDK Auto: production-first policy forbids local runtime tests.
"""
import importlib.util
import json
from types import SimpleNamespace
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
    def test_protected_branches_are_rejected_before_local_retirement(self):
        self.assertFalse(mod.branch_valid(Path("."), "main", "main"))
        self.assertFalse(mod.branch_valid(Path("."), "production", "main"))
    def _assert_local_only(self, remote_sha):
        evidence = {
            "schema_version": 1, "repository": "example/project", "target": "main",
            "remote": "origin", "scope": "historical",
            "observed_at_utc": self.now.isoformat(), "inventory_exhaustive": True,
            "out_of_scope_count": 0, "candidates": [self.proof]
        }
        outcome = {"branch_cleanup": "REMOVED_VERIFIED_BRANCH", "local_main": "SYNCED"}
        closeout = SimpleNamespace(returncode=0, stdout=json.dumps(outcome), stderr="")
        with (patch.object(mod, "repo_identity", return_value="example/project"),
              patch.object(mod, "git", return_value=""),
              patch.object(mod, "rev", return_value=self.sha),
              patch.object(mod, "remote_head", return_value=remote_sha),
              patch.object(mod, "validate_proof", return_value=None),
              patch.object(mod, "save_state", return_value=".git/phdk/state.json"),
              patch.object(mod.subprocess, "run", return_value=closeout) as run):
            result = mod.apply(Path(__file__).resolve().parent, "origin", "main",
                               evidence, max_candidates=5)
        self.assertEqual(run.call_count, 1)
        self.assertIn("phdk_git_closeout.py", " ".join(map(str, run.call_args.args[0])))
        self.assertNotIn("push", run.call_args.args[0])
        self.assertEqual(result["remote_policy"], "PRESERVE_REMOTE_BRANCHES")
        self.assertEqual(result["results"][0]["remote"], "RETAINED_BY_POLICY")
        self.assertEqual(result["results"][0]["local"], "REMOVED_VERIFIED_BRANCH")
        self.assertEqual(result["pending"], 0)
        self.assertTrue(result["history_complete"])
        return result

    def test_merged_local_branch_retires_without_remote_deletion(self):
        result = self._assert_local_only(self.sha)
        self.assertNotIn("remote_head_changed_since_merge", result["results"][0])

    def test_advanced_remote_is_preserved_without_blocking_safe_local_cleanup(self):
        result = self._assert_local_only("c" * 40)
        self.assertTrue(result["results"][0]["remote_head_changed_since_merge"])

    def test_malformed_sha_rejected(self):
        self.proof["head_sha"] = "not-a-sha"
        with patch.object(mod, "branch_valid", return_value=True):
            self.assertEqual(mod.validate_proof(
                Path("."), "origin", "main", self.proof,
                "example/project", self.now, False), "MISSING_FULL_SHA")

if __name__ == "__main__":
    unittest.main()
