"""Synthetic isolated tests; no application runtime, provider, UAT or exporting."""
import contextlib
from copy import deepcopy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

SRC = Path(__file__).with_name("phdk_post_uat_export.py")
spec = importlib.util.spec_from_file_location("phdk_post_uat_export", SRC)
MOD = importlib.util.module_from_spec(spec)
spec.loader.exec_module(MOD)
SHA_A, SHA_B = "a" * 40, "b" * 40


def state(**overrides):
    x = {
        "schema_version": 1, "run_id": "uat-20261107-001", "explicit_uat": True,
        "conclusion": "ACCEPTED", "tested_revision": SHA_A, "current_revision": SHA_A,
        "open_required_defects": 0, "unverified_required_cases": 0,
        "fix_disposition": "NOT_APPLICABLE", "evidence_reference": "docs/phdk/lifecycle/uat-20261107-001/50-uat/HANDOFF.md",
    }
    x.update(overrides)
    return x


class FakeExport:
    calls = 0

    @classmethod
    def catalog_at(cls, root, catalog):
        cls.calls += 1
        return catalog

    @classmethod
    def load_catalog(cls, path):
        cls.calls += 1
        return [{"id": "starter.themes"}]

    @classmethod
    def report(cls, root, entries):
        cls.calls += 1
        return {"candidates": [{"id": "packages/theme", "category": "POSSIBLE_OVERLAP", "priority": "HIGH"}], "catalog_status": "AVAILABLE"}


class PostUATExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        FakeExport.calls = 0

    def test_accepted_without_fix_runs_only_read_only_inventory(self):
        result = MOD.evaluate(self.root, MOD.state_from_text(json.dumps(state())), FakeExport)
        self.assertEqual(result["gate"], "READY_FOR_REVIEW")
        self.assertEqual(result["candidates"][0]["id"], "packages/theme")
        self.assertEqual(result["publication"], "NOT_AUTHORIZED_BY_REVIEW")
        self.assertIsNotNone(result["review_key"])
        self.assertEqual(FakeExport.calls, 3)

    def test_accepted_after_verified_fix(self):
        r = MOD.evaluate(self.root, state(fix_disposition="VERIFIED_COMPLETE"), FakeExport)
        self.assertEqual(r["gate"], "READY_FOR_REVIEW")

    def test_no_automatic_uat_from_auto(self):
        result = MOD.evaluate(self.root, state(explicit_uat=False, conclusion="NOT_RUN"), FakeExport)
        self.assertEqual(result["gate"], "DEFERRED_UAT_NOT_RUN")
        self.assertEqual(FakeExport.calls, 0)

    def test_false_accepted_without_explicit_uat_never_scans(self):
        result = MOD.evaluate(self.root, state(explicit_uat=False), FakeExport)
        self.assertEqual(result["gate"], "DEFERRED_UAT_NOT_RUN")
        self.assertEqual(FakeExport.calls, 0)

    def test_failed_uat_waits_for_fix(self):
        r = MOD.evaluate(self.root, state(conclusion="NOT_ACCEPTED", open_required_defects=3), FakeExport)
        self.assertEqual(r["gate"], "WAITING_FOR_UAT_FIX")
        self.assertEqual(FakeExport.calls, 0)

    def test_acceptance_incomplete_never_scans(self):
        r = MOD.evaluate(self.root, state(conclusion="ACCEPTANCE_INCOMPLETE", unverified_required_cases=1), FakeExport)
        self.assertEqual(r["gate"], "ACCEPTANCE_INCOMPLETE")
        self.assertEqual(FakeExport.calls, 0)

    def test_zero_unverified_required_but_fix_pending_never_scans(self):
        r = MOD.evaluate(self.root, state(fix_disposition="PENDING"), FakeExport)
        self.assertEqual(r["gate"], "WAITING_FOR_UAT_FIX")
        self.assertEqual(FakeExport.calls, 0)

    def test_changed_revision_never_scans(self):
        r = MOD.evaluate(self.root, state(current_revision=SHA_B), FakeExport)
        self.assertEqual(r["gate"], "STALE_ACCEPTANCE")
        self.assertEqual(FakeExport.calls, 0)

    def test_unverified_revision_never_scans(self):
        r = MOD.evaluate(self.root, state(current_revision=None), FakeExport)
        self.assertEqual(r["gate"], "REVISION_UNVERIFIED")
        self.assertEqual(FakeExport.calls, 0)

    def test_missing_case_evidence_blocks_even_accepted_label(self):
        r = MOD.evaluate(self.root, state(unverified_required_cases=1), FakeExport)
        self.assertEqual(r["gate"], "ACCEPTANCE_INCOMPLETE")
        self.assertEqual(FakeExport.calls, 0)

    def test_revision_consistent_key_is_idempotent(self):
        one = MOD.evaluate(self.root, state(), FakeExport)
        two = MOD.evaluate(self.root, state(), FakeExport)
        self.assertEqual(one["review_key"], two["review_key"])

    def test_prevent_unsafe_state_file_symlink(self):
        other = self.root / "external.json"
        other.write_text(json.dumps(state()))
        link = self.root / "link.json"
        link.symlink_to(other)
        with self.assertRaises(ValueError):
            MOD.load_state(self.root, "link.json", io.StringIO())

    def test_state_file_is_read_only(self):
        path = self.root / "state.json"
        payload = json.dumps(state())
        path.write_text(payload)
        result = MOD.load_state(self.root, "state.json", io.StringIO())
        self.assertEqual(result["tested_revision"], SHA_A)
        self.assertEqual(path.read_text(), payload)

    def test_unhashable_conclusion_is_rejected_cleanly(self):
        with self.assertRaises(ValueError):
            MOD.state_from_text(json.dumps(state(conclusion=["ACCEPTED"])))

    def test_unhashable_fix_disposition_is_rejected_cleanly(self):
        with self.assertRaises(ValueError):
            MOD.state_from_text(json.dumps(state(fix_disposition={"state": "VERIFIED_COMPLETE"})))

    def test_invalid_unknown_fields_rejected(self):
        with self.assertRaises(ValueError):
            MOD.state_from_text(json.dumps(state(approval=True)))

    def test_int_as_bool_is_rejected(self):
        with self.assertRaises(ValueError):
            MOD.state_from_text(json.dumps(state(explicit_uat=1)))

    def test_invalid_sha_is_rejected(self):
        with self.assertRaises(ValueError):
            MOD.state_from_text(json.dumps(state(tested_revision="short")))

    def test_gigantic_state_is_rejected(self):
        with self.assertRaises(ValueError):
            MOD.state_from_text(" " * (MOD.MAX_STATE_BYTES + 1))

    def test_no_candidates_is_valid(self):
        class Empty(FakeExport):
            @classmethod
            def report(cls, root, entries):
                return {"candidates": [], "catalog_status": "AVAILABLE"}
        r = MOD.evaluate(self.root, state(), Empty)
        self.assertEqual(r["candidates"], [])
        self.assertIn("No module candidates", MOD.markdown(r))

    def test_evidence_not_independently_verified(self):
        r = MOD.evaluate(self.root, state(), FakeExport)
        self.assertEqual(r["evidence_status"], "CALLER_MUST_VERIFY_UAT_REPORT")
        self.assertEqual(r["approval"], "NAMED_OWNER_SELECTION_REQUIRED_FOR_EXPORT")

    def test_rejects_catalog_outside_donor(self):
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = MOD.main(["--root", str(self.root), "--state", "-", "--catalog", "../outside.json"], io.StringIO(json.dumps(state())))
        self.assertEqual(result, 2)
        self.assertIn("invalid", buf.getvalue())

    def test_cli_non_accepted_does_not_require_inventory_helper(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = MOD.main(["--root", str(self.root), "--state", "-", "--json"], io.StringIO(json.dumps(state(explicit_uat=False, conclusion="NOT_RUN"))))
        self.assertEqual(rc, 0)
        self.assertEqual(json.loads(buf.getvalue())["gate"], "DEFERRED_UAT_NOT_RUN")


if __name__ == "__main__":
    unittest.main()
