"""Synthetic source regression scenarios; execute only where current testing policy permits."""
import copy
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    "phdk_effort_status",
    Path(__file__).resolve().parents[1] / "scripts" / "phdk_effort_status.py",
)
subject = importlib.util.module_from_spec(spec)
spec.loader.exec_module(subject)


def sample():
    return {"schema_version": 1, "human_day_hours": 8, "baseline_total_hours": 24,
            "confidence": "MEDIUM", "milestones": [
                {"id": "MS-001", "baseline_hours": 8, "verified_equivalent_hours": 8,
                 "remaining_hours": 0, "status": "DONE", "evidence_ref": "synthetic-main"},
                {"id": "MS-002", "baseline_hours": 10, "verified_equivalent_hours": 6.4,
                 "remaining_hours": 3.6, "status": "IN_PROGRESS", "evidence_ref": "synthetic-slice"},
                {"id": "MS-003", "baseline_hours": 6, "verified_equivalent_hours": 0,
                 "remaining_hours": 6, "status": "PENDING", "evidence_ref": ""},
            ]}


class EffortTests(unittest.TestCase):
    def test_verified_work_reduces_remaining(self):
        summary = subject.summarize(sample())
        self.assertEqual((summary["initial_days"], summary["remaining_days"], summary["progress_percent"]),
                         (3.0, 1.2, 60.0))
        self.assertIn("1.2 jornadas", subject.render(summary))

    def test_new_work_increases_remaining_not_original(self):
        case = sample()
        case["milestones"][2]["remaining_hours"] += 8
        summary = subject.summarize(case)
        self.assertEqual(summary["initial_days"], 3.0)
        self.assertEqual(summary["remaining_days"], 2.2)
        self.assertLess(summary["progress_percent"], 60)

    def test_clock_time_does_not_count(self):
        case = sample()
        another = copy.deepcopy(case)
        another["updated_at"] = "later"
        self.assertEqual(subject.summarize(case), subject.summarize(another))

    def test_unverified_earned_work_rejected(self):
        case = sample()
        case["milestones"][1]["evidence_ref"] = ""
        with self.assertRaises(ValueError):
            subject.summarize(case)

    def test_invalid_effort_rejected(self):
        for value in (-1, float("nan"), True):
            with self.subTest(value=value):
                case = sample()
                case["milestones"][1]["remaining_hours"] = value
                with self.assertRaises(ValueError):
                    subject.summarize(case)

    def test_zero_without_completion_is_unverified(self):
        case = sample()
        for item in case["milestones"]:
            item["verified_equivalent_hours"] = 0
            item["remaining_hours"] = 0
            item["status"] = "IN_PROGRESS"
        self.assertIsNone(subject.summarize(case)["progress_percent"])

    def test_unfinished_work_never_reports_one_hundred(self):
        case = sample()
        for item in case["milestones"]:
            item["remaining_hours"] = 0
        self.assertIsNone(subject.summarize(case)["progress_percent"])

    def test_done_without_evidence_rejected(self):
        case = sample()
        case["milestones"][0]["evidence_ref"] = ""
        with self.assertRaises(ValueError):
            subject.summarize(case)

    def test_full_completion_is_evidenced(self):
        case = sample()
        for item in case["milestones"]:
            item["verified_equivalent_hours"] += item["remaining_hours"]
            item["remaining_hours"] = 0
            item["status"] = "DONE"
            item["evidence_ref"] = "synthetic-verified-delivery"
        summary = subject.summarize(case)
        self.assertTrue(summary["complete_with_evidence"])
        self.assertEqual(summary["progress_percent"], 100.0)


if __name__ == "__main__":
    unittest.main()
