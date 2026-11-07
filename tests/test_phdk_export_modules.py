"""Local, synthetic source-inventory contract tests. No application/UAT execution."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("phdk_export_modules", ROOT / "scripts" / "phdk_export_modules.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class ExportModulesTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "packages").mkdir()
        self.catalog = [{"id": "starter.themes", "title": "Starter theme system", "status": "SPECIFICATION_ONLY", "implementation": None, "capabilities": ["Light and dark theme"]}]

    def create(self, name="theme", marker=None):
        path = self.root / "packages" / name
        path.mkdir()
        (path / "package.json").write_text("{}", encoding="utf-8")
        (path / "README.md").write_text("Test only", encoding="utf-8")
        (path / "test").mkdir()
        if marker is not None:
            (path / "phdk-module.json").write_text(json.dumps(marker), encoding="utf-8")
        return path

    def test_spec_only_not_accepted_package(self):
        self.create(marker={"schema_version": 1, "catalog_id": "starter.themes"})
        got = MOD.report(self.root, self.catalog)
        self.assertEqual(got["candidates"][0]["category"], "SPECIFICATION_IMPLEMENTATION")
        self.assertEqual(got["candidates"][0]["test_result"], "NOT_RUN")
        self.assertEqual(got["candidates"][0]["contribution_state"], "PROPOSAL_ONLY")
        self.assertEqual(got["publication"], "NOT_AUTHORIZED_BY_SCAN")

    def test_without_catalog_does_not_claim_novelty(self):
        self.create()
        self.assertEqual(MOD.report(self.root, None)["candidates"][0]["category"], "UNCLASSIFIED")

    def test_name_overlap_not_exact_provenance(self):
        self.create("theme")
        entry = MOD.report(self.root, self.catalog)["candidates"][0]
        self.assertEqual(entry["category"], "POSSIBLE_OVERLAP")
        self.assertEqual(entry["match_evidence"], "POSSIBLE_NAME_OVERLAP")

    def test_missing_and_invalid_baseline(self):
        self.create(marker={"schema_version": 1, "catalog_id": "starter.themes", "upstream_commit": "f"*40})
        entry = MOD.report(self.root, self.catalog)["candidates"][0]
        self.assertEqual(entry["baseline_comparison"], "BASELINE_UNAVAILABLE")
        self.assertIsNone(entry["changed_files_count"])

    def test_real_local_history_comparison_is_metadata_only(self):
        path = self.create(marker={"schema_version": 1, "catalog_id": "starter.themes"})
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "add", "."], check=True)
        subprocess.run(["git", "-C", str(self.root), "-c", "user.email=test@example.invalid", "-c", "user.name=Fixture", "commit", "-qm", "baseline"], check=True)
        baseline = subprocess.check_output(["git", "-C", str(self.root), "rev-parse", "HEAD"], text=True).strip()
        marker = {"schema_version": 1, "catalog_id": "starter.themes", "upstream_commit": baseline}
        (path / "phdk-module.json").write_text(json.dumps(marker), encoding="utf-8")
        self.assertEqual(MOD.report(self.root, self.catalog)["candidates"][0]["baseline_comparison"], "NO_TRACKED_CHANGES")
        (path / "README.md").write_text("Actual source documentation improvement", encoding="utf-8")
        self.assertEqual(MOD.report(self.root, self.catalog)["candidates"][0]["baseline_comparison"], "LOCAL_CHANGES_DETECTED")

    def test_rejects_unknown_metadata_and_no_network(self):
        self.create(marker={"schema_version": 1, "catalog_id": "starter.themes", "unsafe": "x"})
        entry = MOD.report(self.root, self.catalog)["candidates"][0]
        self.assertEqual(entry["signals"]["provenance"], "INVALID_METADATA")
        self.assertEqual(entry["baseline_comparison"], "NOT_DECLARED")

    def test_ignores_symlink_and_excluded_parent(self):
        self.create("normal")
        (self.root / "packages" / "escape").symlink_to(self.root, target_is_directory=True)
        (self.root / "src" / "secrets").mkdir(parents=True)
        (self.root / "src" / "secrets" / "README.md").write_text("secret")
        entries = MOD.report(self.root, self.catalog)["candidates"]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["id"], "packages/normal")

    def test_read_only_and_deterministic(self):
        self.create("b")
        self.create("a")
        before = sorted(str(p.relative_to(self.root)) for p in self.root.rglob("*"))
        one = MOD.report(self.root, self.catalog)
        two = MOD.report(self.root, self.catalog)
        after = sorted(str(p.relative_to(self.root)) for p in self.root.rglob("*"))
        self.assertEqual(one, two)
        self.assertEqual(before, after)
        self.assertEqual([v["id"] for v in one["candidates"]], ["packages/a", "packages/b"])


    def test_declared_unknown_catalog_id_not_fuzzy_mapped(self):
        self.create("theme", {"schema_version": 1, "catalog_id": "other.theme"})
        record = MOD.report(self.root, self.catalog)["candidates"][0]
        self.assertEqual(record["match_evidence"], "DECLARED_ID_NOT_FOUND")
        self.assertEqual(record["category"], "UNVERIFIED_CATALOG_REFERENCE")

    def test_three_way_overlap_only_when_local_ancestry_available(self):
        path = self.create("theme", {"schema_version": 1, "catalog_id": "starter.themes"})
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "add", "."], check=True)
        config = ["git", "-C", str(self.root), "-c", "user.email=test@example.invalid", "-c", "user.name=Fixture"]
        subprocess.run(config + ["commit", "-qm", "baseline"], check=True)
        baseline = subprocess.check_output(["git", "-C", str(self.root), "rev-parse", "HEAD"], text=True).strip()
        (path / "README.md").write_text("upstream change")
        subprocess.run(["git", "-C", str(self.root), "add", "."], check=True)
        subprocess.run(config + ["commit", "-qm", "upstream"], check=True)
        head = subprocess.check_output(["git", "-C", str(self.root), "rev-parse", "HEAD"], text=True).strip()
        (path / "README.md").write_text("local change to same file")
        (path / "phdk-module.json").write_text(json.dumps({"schema_version": 1, "catalog_id": "starter.themes", "upstream_commit": baseline, "upstream_head_commit": head}))
        result = MOD.report(self.root, self.catalog)["candidates"][0]
        self.assertEqual(result["upstream_comparison"], "THREE_WAY_PATH_COMPARISON")
        self.assertEqual(result["upstream_changed_files_count"], 1)
        self.assertEqual(result["changed_path_overlap_count"], 1)

    def test_cli_json_and_markdown(self):
        self.create()
        command = ["python3", str(ROOT / "scripts" / "phdk_export_modules.py"), "--root", str(self.root)]
        data = json.loads(subprocess.check_output(command + ["--json"], text=True))
        self.assertEqual(data["count"], 1)
        text = subprocess.check_output(command, text=True)
        self.assertIn("nothing exported or published", text)
        self.assertIn("packages/theme", text)


if __name__ == "__main__":
    unittest.main()
