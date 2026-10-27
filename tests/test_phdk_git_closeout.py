"""Regression scenarios for the safe post-merge Git workspace closeout.

Source only in Auto: PHDK production-first rules prohibit local runtime tests.
"""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "phdk_git_closeout.py"
spec = importlib.util.spec_from_file_location("phdk_git_closeout", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def git(folder, *args):
    return subprocess.run(["git", "-C", str(folder), *args], check=True,
                          text=True, capture_output=True).stdout.strip()

class GitWorkspaceCloseoutTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.bare, self.repo = root / "remote.git", root / "repo"
        self.bare.mkdir()
        self.repo.mkdir()
        git(self.bare, "init", "--bare", "--initial-branch=main")
        git(self.repo, "init", "--initial-branch=main")
        git(self.repo, "config", "user.name", "PHDK Test")
        git(self.repo, "config", "user.email", "test@example.invalid")
        (self.repo / "VERSION").write_text("0.1.0\n")
        git(self.repo, "add", ".")
        git(self.repo, "commit", "-m", "v0.1.0 feat: fixture")
        git(self.repo, "remote", "add", "origin", str(self.bare))
        git(self.repo, "push", "-u", "origin", "main")
    def tearDown(self):
        self.tmp.cleanup()
    def run_tool(self, *args):
        p = subprocess.run([sys.executable, str(SCRIPT), *args], cwd=self.repo,
                           capture_output=True, text=True)
        report = json.loads(p.stdout) if p.stdout else json.loads(p.stderr)
        return p.returncode, report
    def merged_feature(self):
        git(self.repo, "switch", "-c", "feature/milestone")
        (self.repo / "feature.txt").write_text("delivered\n")
        git(self.repo, "add", "feature.txt")
        git(self.repo, "commit", "-m", "v0.2.0 feat: milestone")
        head = git(self.repo, "rev-parse", "HEAD")
        git(self.repo, "push", "-u", "origin", "feature/milestone")
        git(self.repo, "switch", "main")
        git(self.repo, "merge", "--ff-only", "feature/milestone")
        git(self.repo, "push", "origin", "main")
        merge = git(self.repo, "rev-parse", "HEAD")
        # Simulate another local clone that has not fetched main.
        return head, merge
    def test_clean_merged_branch_closes_without_a_second_push(self):
        _, merged = self.merged_feature()
        code, report = self.run_tool("--apply", "--merged-sha", merged,
                                     "--branch", "feature/milestone")
        self.assertEqual(code, 0)
        self.assertEqual(report["local_main"], "SYNCED")
        self.assertEqual(report["branch_cleanup"], "REMOVED_VERIFIED_BRANCH")
        self.assertEqual(git(self.repo, "rev-parse", "main"),
                         git(self.repo, "rev-parse", "origin/main"))
    def test_local_main_fast_forwards_remote_commit(self):
        other = Path(self.tmp.name) / "other"
        subprocess.run(["git", "clone", str(self.bare), str(other)],
                       check=True, capture_output=True, text=True)
        git(other, "config", "user.name", "PHDK Other")
        git(other, "config", "user.email", "other@example.invalid")
        (other / "VERSION").write_text("0.2.0\n")
        git(other, "add", "VERSION")
        git(other, "commit", "-m", "v0.2.0 feat: remote milestone")
        git(other, "push", "origin", "main")
        expected = git(other, "rev-parse", "HEAD")
        code, report = self.run_tool("--apply", "--merged-sha", expected)
        self.assertEqual(code, 0)
        self.assertEqual(report["local_main"], "SYNCED")
        self.assertEqual(report["local_main_sha_after"], expected)

    def test_linked_worktree_of_merged_branch_is_removed(self):
        _, merged = self.merged_feature()
        linked = Path(self.tmp.name) / "linked-feature"
        git(self.repo, "worktree", "add", str(linked), "feature/milestone")
        code, report = self.run_tool("--apply", "--merged-sha", merged,
                                     "--branch", "feature/milestone")
        self.assertEqual(code, 0)
        self.assertEqual(report["branch_cleanup"], "REMOVED_VERIFIED_BRANCH")
        self.assertFalse(linked.exists())

    def test_unmerged_branch_retained_without_pr_head_proof(self):
        git(self.repo, "switch", "-c", "feature/not-merged")
        (self.repo / "unmerged").write_text("unique")
        git(self.repo, "add", ".")
        git(self.repo, "commit", "-m", "v0.2.0 feat: unique")
        git(self.repo, "switch", "main")
        base = git(self.repo, "rev-parse", "HEAD")
        code, report = self.run_tool("--apply", "--merged-sha", base,
                                     "--branch", "feature/not-merged")
        self.assertEqual(code, 3)
        self.assertEqual(report["branch_cleanup"],
                         "RETAINED_UNMERGED_OR_SQUASH_UNVERIFIED")
    def test_dirty_main_preserved(self):
        base = git(self.repo, "rev-parse", "HEAD")
        (self.repo / "local.txt").write_text("precious")
        code, report = self.run_tool("--apply", "--merged-sha", base)
        self.assertEqual(code, 2)
        self.assertEqual(report["local_main"], "BLOCKED_DIRTY_MAIN_WORKTREE")
        self.assertTrue((self.repo / "local.txt").exists())
    def test_reject_mismatched_pr_head_and_unrelated_merge(self):
        _, merged = self.merged_feature()
        code, report = self.run_tool("--apply", "--merged-sha", merged,
                                     "--branch", "feature/milestone",
                                     "--pr-head-sha", "0" * 40)
        self.assertEqual(code, 3)
        self.assertEqual(report["branch_cleanup"], "BLOCKED_PR_HEAD_SHA_MISMATCH")
    def test_ignore_classification_never_discards_secrets(self):
        self.assertTrue(module.safe_generated_ignored(
            ["!! node_modules/package/index.js", "!! dist/bundle.js"]))
        self.assertFalse(module.safe_generated_ignored(
            ["!! node_modules/package/index.js", "!! .env"]))
        self.assertFalse(module.safe_generated_ignored(["?? notes.txt"]))

if __name__ == "__main__":
    unittest.main()
