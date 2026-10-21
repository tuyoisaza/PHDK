"""Design-choice regression source; execute only where current policy permits tests."""
import copy
import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "phdk_auto_gate.py"
SPEC = importlib.util.spec_from_file_location("phdk_design_gate_subject", SCRIPT)
GATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GATE)


def design_state(mode="auto"):
    return {
        "schema_version": 1, "run_id": "design-regression", "mode": mode,
        "repository": "example/product", "goal": "Implement the requested interface",
        "target_branch": "main", "candidate_ref": "a" * 40,
        "authorization": {
            "source_ref": "synthetic-current-message", "instruction": f"PHDK {mode}",
            "scope": ["Requested interface and normal delivery"], "restrictions": [], "status": "active"
        },
        "completion_criteria": ["Selected interface implemented and delivered"],
        "steps": [
            {"id": "design", "kind": "work", "status": "blocked", "action": "Finalize design",
             "depends_on": [], "blocked_by": ["visual-choice"]},
            {"id": "ui", "kind": "work", "status": "pending", "action": "Implement selected UI",
             "depends_on": ["design"], "blocked_by": []}
        ],
        "blockers": [{
            "id": "visual-choice", "kind": "design_choice", "reason": "Unresolved visual direction",
            "source_ref": "synthetic-design-session", "evidence": "Synthetic alternatives are available",
            "observed_at": "2026-10-20T23:35:00-06:00", "next_action": "Choose direction A or B"
        }]
    }


class DesignChoiceTests(unittest.TestCase):
    def test_auto_waits_for_one_owner_answer_without_ui_execution(self):
        outcome = GATE.evaluate(design_state(), "auto")
        self.assertEqual(outcome["disposition"], "WAITING_EXTERNAL")
        self.assertEqual(len(outcome["actions"]), 1)
        self.assertEqual(outcome["actions"][0]["reason"], "DESIGN_AWAITING_OWNER")
        self.assertEqual(outcome["actions"][0]["action"], "Choose direction A or B")

    def test_force_selects_before_dependent_ui_and_does_not_mutate_state(self):
        data = design_state("auto_force")
        before = copy.deepcopy(data)
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual(outcome["disposition"], "CONTINUE")
        self.assertEqual([a["step_id"] for a in outcome["actions"]], ["design"])
        self.assertIn("AGENT_SELECTED_AUTO_FORCE", outcome["actions"][0]["action"])
        self.assertIn("visual evidence limits", outcome["actions"][0]["action"])
        self.assertEqual(data, before)

    def test_independent_work_continues_while_auto_waits(self):
        data = design_state()
        data["steps"].append({"id": "backend", "kind": "work", "status": "pending",
                              "action": "Implement independent API", "depends_on": [], "blocked_by": []})
        outcome = GATE.evaluate(data, "auto")
        self.assertEqual(outcome["disposition"], "CONTINUE")
        self.assertEqual([a["step_id"] for a in outcome["actions"]], ["backend"])
        self.assertEqual(outcome["waiting"][0]["reason"], "DESIGN_AWAITING_OWNER")

    def test_recorded_decision_releases_dependent_ui(self):
        for mode in ("auto", "auto_force"):
            with self.subTest(mode=mode):
                data = design_state(mode)
                data["steps"][0].update(status="done", blocked_by=[], evidence="Synthetic recorded decision")
                outcome = GATE.evaluate(data, mode)
                self.assertEqual(outcome["disposition"], "CONTINUE")
                self.assertEqual([a["step_id"] for a in outcome["actions"]], ["ui"])

    def test_force_does_not_waive_an_actual_scoped_owner_stop(self):
        data = design_state("auto_force")
        data["blockers"].append({
            "id": "actual-stop", "kind": "owner_stop", "reason": "Explicit retained owner restriction",
            "source_ref": "synthetic-stop-message", "evidence": "Do not implement until I approve",
            "observed_at": "2026-10-20T23:35:00-06:00",
            "resolution_attempts": ["Reconciled retained restriction against current instruction"],
            "next_action": "Owner must replace the explicit restriction"
        })
        data["steps"][0]["blocked_by"].append("actual-stop")
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual(outcome["disposition"], "WAITING_EXTERNAL")
        self.assertEqual(outcome["actions"][0]["blocker_id"], "actual-stop")

    def test_paused_mandate_stops_both_modes(self):
        for mode in ("auto", "auto_force"):
            with self.subTest(mode=mode):
                data = design_state(mode)
                data["authorization"]["status"] = "paused"
                self.assertEqual(GATE.evaluate(data, mode)["disposition"], "STOPPED")

    def test_mode_switch_requires_factual_reconciliation_then_force_selects(self):
        data = design_state()
        self.assertEqual(GATE.evaluate(data, "auto_force")["disposition"], "REPAIR_STATE")
        data["mode"] = "auto_force"
        data["authorization"]["instruction"] = "Synthetic explicit current PHDK auto force request"
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual(outcome["disposition"], "CONTINUE")
        self.assertIn("AGENT_SELECTED_AUTO_FORCE", outcome["actions"][0]["action"])

    def test_done_cannot_hide_an_unresolved_design_choice(self):
        data = design_state("auto_force")
        data["steps"][0].update(status="done", evidence="Stale completion label")
        outcome = GATE.evaluate(data, "auto_force")
        self.assertEqual(outcome["disposition"], "REPAIR_STATE")
        self.assertTrue(any("unresolved design_choice" in e for e in outcome["errors"]))

    def test_missing_choice_provenance_requires_internal_repair(self):
        for key in ("source_ref", "evidence", "observed_at", "next_action"):
            with self.subTest(key=key):
                data = design_state()
                del data["blockers"][0][key]
                self.assertEqual(GATE.evaluate(data, "auto")["disposition"], "REPAIR_STATE")

    def test_multiple_ready_choices_do_not_create_a_questionnaire(self):
        data = design_state()
        second = copy.deepcopy(data["blockers"][0])
        second.update(id="density-choice", next_action="Choose compact or comfortable density")
        data["blockers"].append(second)
        data["steps"].append({"id": "density", "kind": "work", "status": "blocked",
                              "action": "Finalize density", "depends_on": [], "blocked_by": ["density-choice"]})
        outcome = GATE.evaluate(data, "auto")
        self.assertEqual(outcome["disposition"], "WAITING_EXTERNAL")
        self.assertEqual(len(outcome["actions"]), 1)
        self.assertEqual(outcome["pending_design_choices"], 2)


if __name__ == "__main__":
    unittest.main()
