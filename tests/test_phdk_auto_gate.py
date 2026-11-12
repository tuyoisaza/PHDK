"""Behavioral regressions for Auto continuity; synthetic state, no remote services."""
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "phdk_auto_gate.py"
SPEC = importlib.util.spec_from_file_location("phdk_auto_gate", SCRIPT)
GATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GATE)


def step(sid="deliver", kind="delivery", **updates):
    return {"id": sid, "kind": kind, "status": "pending", "action": f"Execute {sid}",
            "depends_on": [], "blocked_by": [], **updates}


def state():
    return {
        "session": {"id": "session-01", "started_at": datetime.now(timezone.utc).isoformat()},
        "schema_version": 1, "run_id": "current-user-goal", "mode": "auto_force",
        "repository": "example/project", "target_branch": "main", "goal": "Complete the scoped change",
        "candidate_ref": "a" * 40,
        "authorization": {"source_ref": "current-user-message", "instruction": "Complete this change with phdk auto force",
                          "scope": ["Implementation and normal delivery"], "restrictions": [], "status": "active"},
        "completion_criteria": ["Requested content and version verified on remote main"],
        "steps": [step()], "blockers": [],
        "delivery_watch": {"window_started_at": datetime.now(timezone.utc).isoformat(),
                           "active_minutes_before_session": 0, "active_milestones": ["MS-001"],
                           "product_files_pending": 0, "standards_files_pending": 0,
                           "nonprogress_cycles": 0, "observed_source": "actual git/PR snapshot"},
    }


def block(data, kind, **details):
    bid = details.pop("id", "blocking-record")
    data["blockers"].append({"id": bid, "kind": kind, "reason": "Observed task condition", **details})
    data["steps"][0]["blocked_by"].append(bid)
    data["steps"][0]["status"] = "blocked"


def external_details():
    return {"evidence": "Actual operation denied access; no alternate authorized access available",
            "observed_at": "2026-10-17T21:30:00-06:00", "source_ref": "observed-tool-error",
            "resolution_attempts": ["Checked the actual response and available scoped repair route"],
            "next_action": "Restore access to the identified repository"}


class AutoContinuityTests(unittest.TestCase):

    def test_premature_completed_with_pending_delivery_is_not_stopped(self):
        data = state()
        data["authorization"]["status"] = "completed"
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual(outcome["disposition"], "REPAIR_STATE")
        self.assertTrue(outcome["premature_completion"])
        self.assertEqual(outcome["unfinished_step_ids"], ["deliver"])

    def test_completed_state_with_no_commitments_stays_stopped(self):
        data = state()
        data["steps"][0].update(status="done", evidence="actual merge and SHA")
        data["authorization"]["status"] = "completed"
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "STOPPED")

    def test_all_steps_done_but_security_commitment_open_cannot_close(self):
        data = state()
        data["steps"][0].update(status="done", evidence="published")
        data["unresolved_commitments"] = ["Complete the authorized static security check"]
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual(outcome["disposition"], "REPAIR_STATE")
        self.assertIn("security", outcome["unresolved_commitments"][0])

    def test_time_budget_in_both_modes(self):
        for mode in ("auto", "auto_force"):
            data = state()
            data["mode"] = mode
            data["session"]["started_at"] = "2026-01-01T00:00:00Z"
            now = datetime(2026, 1, 1, 4, tzinfo=timezone.utc)
            self.assertEqual(GATE.evaluate(data, mode, now)["disposition"], "SESSION_HANDOFF")

    def test_next_slice_will_not_fit(self):
        data = state()
        data["session"].update(started_at="2026-01-01T00:00:00Z", next_slice_minutes=30)
        now = datetime(2026, 1, 1, 3, 20, tzinfo=timezone.utc)
        self.assertEqual(GATE.evaluate(data, "auto_force", now)["disposition"], "SESSION_HANDOFF")

    def test_closed_or_at_risk_never_dispatches_work(self):
        for field in ("closed", "close_early"):
            data = state()
            data["session"][field] = True
            self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "SESSION_HANDOFF")

    def test_legacy_record_requires_reconstruction(self):
        data = state()
        del data["session"]
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "REPAIR_STATE")

    def test_owner_stop_takes_precedence(self):
        data = state()
        data["authorization"]["status"] = "revoked"
        data["session"]["close_early"] = True
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "STOPPED")

    def test_force_skips_phdk_review_without_approval_or_source_research(self):
        data = state()
        block(data, "phdk_human_review")
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual(outcome["disposition"], "CONTINUE")
        self.assertEqual(outcome["review_disposition"], "NON_BLOCKING_BY_MODE")
        self.assertEqual(outcome["actions"][0]["action"], "Execute deliver")
        self.assertNotIn("investig", json.dumps(outcome).lower())
        self.assertNotIn("source_ref", data["blockers"][0])

    def test_force_clears_two_documentary_reviews_without_deleting_history(self):
        data = state()
        block(data, "phdk_human_review", id="pr-258-review")
        block(data, "phdk_human_review", id="fixtures-security-review")
        before = copy.deepcopy(data)
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual(outcome["disposition"], "CONTINUE")
        self.assertEqual(len(outcome["non_blocking_reviews"]), 2)
        self.assertEqual(data, before)

    def test_normal_auto_does_the_pending_technical_review(self):
        data = state()
        data["mode"] = "auto"
        block(data, "phdk_human_review")
        outcome = GATE.evaluate(data, "auto")
        self.assertEqual(outcome["disposition"], "CONTINUE")
        self.assertIn("technical diff review", outcome["actions"][0]["action"])

    def test_mandatory_vitest_suite_is_executable_work_not_permission_gate(self):
        data = state()
        data["steps"] = [step("pnpm-test", "required_check", action="pnpm test"), step()]
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual(outcome["disposition"], "CONTINUE")
        self.assertEqual([x["step_id"] for x in outcome["actions"]], ["pnpm-test"])

    def test_force_does_not_skip_actual_diff_review_or_checks(self):
        data = state()
        data["steps"] = [step(), step("diff", "review_diff"), step("composition", "required_check")]
        block(data, "phdk_human_review")
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual({x["step_id"] for x in outcome["actions"]}, {"diff", "composition"})

    def test_delivery_continues_after_observed_checks_pass(self):
        data = state()
        data["steps"] = [step("tests", "required_check", status="done", evidence="Observed isolated suite PASS"), step()]
        self.assertEqual(GATE.evaluate(data, "auto_force")["actions"][0]["step_id"], "deliver")

    def test_stale_blocked_label_does_not_stop_the_goal(self):
        data = state()
        data["steps"][0]["status"] = "blocked"
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "CONTINUE")

    def test_rejected_push_triggers_diagnosis_repair_and_retry(self):
        data = state()
        block(data, "real_failure", failed_operation="push working branch",
              evidence="Observed non-fast-forward rejection", observed_at="2026-10-17T21:30:00-06:00")
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual(outcome["disposition"], "REPAIR_AND_RETRY")
        self.assertIn("Diagnose", outcome["actions"][0]["action"])
        self.assertIn("retry", outcome["actions"][0]["then"])
        self.assertEqual(data["authorization"]["status"], "active")

    def test_check_failure_is_repaired_before_retrying_publication(self):
        data = state()
        data["steps"] = [step("tests", "required_check"), step()]
        block(data, "real_failure", failed_operation="pnpm test", evidence="Observed assertion failure in changed behavior",
              observed_at="2026-10-17T21:30:00-06:00", repair_action="Correct the implementation and rerun the affected test")
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual(outcome["disposition"], "REPAIR_AND_RETRY")
        self.assertEqual(outcome["actions"][0]["step_id"], "tests")
        self.assertNotIn("deliver", [x["step_id"] for x in outcome["independent_actions"]])

    def test_repair_then_retry_does_not_need_another_user_grant(self):
        data = state()
        block(data, "real_failure", failed_operation="merge", evidence="Observed stale head SHA",
              observed_at="2026-10-17T21:30:00-06:00", repair_action="Refresh target and reconcile the scoped diff")
        mandate = copy.deepcopy(data["authorization"])
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "REPAIR_AND_RETRY")
        data["steps"][0].update(status="pending", blocked_by=[])
        data["candidate_ref"] = "b" * 40
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "CONTINUE")
        self.assertEqual(data["authorization"], mandate)

    def test_real_external_dependency_does_not_stop_independent_work(self):
        data = state()
        block(data, "external_dependency", **external_details())
        data["steps"].append(step("independent-code", "work"))
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual(outcome["disposition"], "CONTINUE")
        self.assertEqual(outcome["actions"][0]["step_id"], "independent-code")
        self.assertEqual(len(outcome["waiting"]), 1)

    def test_wait_only_after_actual_dependency_and_attempted_resolution(self):
        data = state()
        block(data, "external_dependency", **external_details())
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "WAITING_EXTERNAL")
        data["blockers"][0]["resolution_attempts"] = []
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "REPAIR_STATE")

    def test_unsubstantiated_external_label_cannot_become_a_terminal_block(self):
        data = state()
        block(data, "external_dependency")
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual(outcome["disposition"], "REPAIR_STATE")
        self.assertIn("do not ask", outcome["actions"][0])

    def test_generic_failure_without_a_failed_operation_needs_internal_repair(self):
        data = state()
        block(data, "real_failure", evidence="A task says blocked", observed_at="2026-10-17")
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "REPAIR_STATE")

    def test_real_owner_stop_is_not_waived_by_force(self):
        for status in ("paused", "revoked"):
            with self.subTest(status=status):
                data = state()
                data["authorization"]["status"] = status
                block(data, "phdk_human_review")
                self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "STOPPED")

    def test_completed_record_does_not_reactivate_old_work(self):
        data = state()
        data["authorization"]["status"] = "completed"
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "STOPPED")

    def test_saved_mode_does_not_activate_force_by_itself(self):
        outcome = GATE.evaluate(state(), "auto")
        self.assertEqual(outcome["disposition"], "REPAIR_STATE")
        self.assertIn("No action executed", outcome["authority"])

    def test_all_done_requests_actual_remote_verification_not_false_completion(self):
        data = state()
        data["steps"][0].update(status="done", evidence="Observed merge result")
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "VERIFY_DELIVERY")
        del data["steps"][0]["evidence"]
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "REPAIR_STATE")

    def test_dependencies_order_development_then_delivery(self):
        data = state()
        data["steps"] = [step(depends_on=["code"]), step("code", "work")]
        self.assertEqual(GATE.evaluate(data, "auto_force")["actions"][0]["step_id"], "code")

    def test_completed_check_cannot_hide_unfinished_upstream_code(self):
        data = state()
        data["steps"] = [step("code", "work"),
                         step("check", "required_check", status="done", evidence="Old check PASS", depends_on=["code"]),
                         step(depends_on=["check"])]
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual(outcome["disposition"], "REPAIR_STATE")
        self.assertTrue(any("unfinished prerequisite" in message for message in outcome["errors"]))

    def test_missing_metadata_does_not_suppress_a_real_stop(self):
        data = state()
        data["authorization"]["status"] = "paused"
        del data["candidate_ref"]
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual(outcome["disposition"], "STOPPED")
        self.assertIn("bookkeeping only", outcome["actions"][0])
        self.assertIn("missing candidate_ref", outcome["state_errors"])

    def test_retry_preserves_an_explicit_alternate_target(self):
        data = state()
        data["target_branch"] = "release/next"
        block(data, "real_failure", failed_operation="push", evidence="Observed non-fast-forward rejection",
              observed_at="2026-10-17T21:30:00-06:00")
        outcome = GATE.evaluate(data, "auto_force")
        self.assertIn("verify remote release/next", outcome["actions"][0]["then"])

    def test_bad_graph_is_repaired_internally(self):
        for deps in (["missing"], ["deliver"]):
            with self.subTest(deps=deps):
                data = state()
                data["steps"][0]["depends_on"] = deps
                self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "REPAIR_STATE")

    def test_malformed_values_never_crash_or_grant_permission(self):
        for value in (None, [], {}, True, 1):
            with self.subTest(value=value):
                variants = [value]
                for section, key in (("authorization", "status"), ("step", "kind"), ("step", "status")):
                    data = state()
                    target = data["steps"][0] if section == "step" else data[section]
                    target[key] = value
                    variants.append(data)
                for data in variants:
                    self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "REPAIR_STATE")

    def test_cli_missing_record_is_internal_recovery_not_a_failed_hook(self):
        with tempfile.TemporaryDirectory() as temp:
            proc = subprocess.run([sys.executable, str(SCRIPT), "--state", str(Path(temp) / "absent.json"), "--mode", "auto_force"],
                                  capture_output=True, text=True, check=False)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertEqual(json.loads(proc.stdout)["disposition"], "REPAIR_STATE")

    def test_cli_operates_without_network_commands_or_state_mutations(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "AUTO_STATE.json"
            data = state()
            block(data, "phdk_human_review")
            original = json.dumps(data)
            path.write_text(original, encoding="utf-8")
            proc = subprocess.run([sys.executable, str(SCRIPT), "--state", str(path), "--mode", "auto_force"],
                                  capture_output=True, text=True, check=False)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertEqual(json.loads(proc.stdout)["disposition"], "CONTINUE")
            self.assertEqual(path.read_text(encoding="utf-8"), original)
            self.assertEqual({p.name for p in Path(temp).iterdir()}, {"AUTO_STATE.json"})


    def test_delivery_stop_loss_time_ladder(self):
        from datetime import timedelta
        data = state()
        start = datetime(2026, 11, 12, 12, tzinfo=timezone.utc)
        data["session"]["started_at"] = start.isoformat()
        data["delivery_watch"]["window_started_at"] = start.isoformat()
        for mins, expected in ((10, "CONTINUE"), (46, "FOCUS_DELIVERY"),
                               (80, "RECOVER_DELIVERY"), (121, "DELIVERY_STOP_LOSS")):
            with self.subTest(minutes=mins):
                self.assertEqual(GATE.evaluate(data, "auto_force",
                                 start + timedelta(minutes=mins))["disposition"], expected)

    def test_delivery_watch_wip_and_large_diff(self):
        data = state()
        data["delivery_watch"]["product_files_pending"] = 401
        data["delivery_watch"]["standards_files_pending"] = 115
        result = GATE.evaluate(data, "auto_force")
        self.assertEqual(result["disposition"], "FOCUS_DELIVERY")
        self.assertEqual(result["unintegrated_standards_files"], 115)
        data["delivery_watch"]["product_files_pending"] = 0
        data["delivery_watch"]["active_milestones"] = ["MS-001", "MS-002"]
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "FOCUS_DELIVERY")
        data["delivery_watch"]["wip_override_ref"] = "current owner instruction"
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "CONTINUE")

    def test_delivery_watch_cross_session_and_allowance(self):
        data = state()
        data["delivery_watch"]["active_minutes_before_session"] = 100
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "RECOVER_DELIVERY")
        data["delivery_watch"]["active_minutes_before_session"] = 121
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "DELIVERY_STOP_LOSS")
        data["delivery_watch"]["active_minutes_before_session"] = 0
        data["delivery_watch"].update(allowance_pct_since_delivery=50,
                                      allowance_source="observed host usage")
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "DELIVERY_STOP_LOSS")
        del data["delivery_watch"]["allowance_source"]
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "REPAIR_STATE")

    def test_delivery_watch_missing_and_owner_stop(self):
        data = state()
        del data["delivery_watch"]
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "REPAIR_STATE")
        data = state()
        data["delivery_watch"]["active_minutes_before_session"] = 160
        data["authorization"]["status"] = "paused"
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "STOPPED")

if __name__ == "__main__":
    unittest.main()
