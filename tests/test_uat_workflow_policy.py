"""Static policy regression. Reads Markdown and never exercises an application."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class UatWorkflowPolicyTests(unittest.TestCase):
    def test_coherence_rejects_missing_visual_result_and_journey_route(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = Path(temp) / "PHDK"
            shutil.copytree(ROOT, fixture, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            check = [sys.executable, str(fixture / "scripts/phdk_coherence_check.py")]
            baseline = subprocess.run(check, capture_output=True, text=True, check=False)
            self.assertEqual(baseline.returncode, 0, baseline.stderr)

            policy = fixture / "UAT_STANDARD.md"
            body = policy.read_text(encoding="utf-8").replace("Workflow UX result", "Functional result")
            # An unrelated mention must not satisfy the actual acceptance decision.
            policy.write_text(body + "\n## Historical note\nWorkflow UX result\n", encoding="utf-8")

            journey = fixture / "UAT_JOURNEY_STANDARD.md"
            route = "PHDK_UX_UI.md#rendered-workflow-walkthrough"
            body = journey.read_text(encoding="utf-8").replace(route, "PHDK_UX_UI.md")
            journey.write_text(body, encoding="utf-8")

            result = subprocess.run(check, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 1)
            self.assertIn("Workflow acceptance decision missing Workflow UX result", result.stderr)
            self.assertIn(f"UAT_JOURNEY_STANDARD.md missing explicit-UAT marker {route}", result.stderr)
