"""Canonical PHDK source-only self-coherence regression cases."""
from pathlib import Path
from shutil import copyfile
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

ROOT = Path(__file__).resolve().parents[1]


def mappings():
    lines = (ROOT / "PHDK_MANIFEST.txt").read_text(encoding="utf-8").splitlines()
    return [tuple(x.strip() for x in line.split("|"))
            for line in lines if line.strip() and not line.lstrip().startswith("#")]


def run_checker(root):
    return subprocess.run([sys.executable, str(root / "scripts/phdk_coherence_check.py")],
                          cwd=root, capture_output=True, text=True, check=False)


class SelfCoherenceTest(unittest.TestCase):
    def test_python_budget(self):
        files = list((ROOT / "scripts").glob("*.py")) + list((ROOT / "tests").glob("*.py"))
        for file in files:
            with self.subTest(file=file.name):
                self.assertLessEqual(len(file.read_text(encoding="utf-8").splitlines()), 600)

    def test_manifest_dependencies(self):
        for file in ("phdk_coherence_check.py", "phdk_coherence_routing.py",
                     "phdk_coherence_quality.py"):
            path = "scripts/" + file
            self.assertEqual(mappings().count((path, path)), 1)

    def test_canonical_static_check(self):
        proc = run_checker(ROOT)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("static only", proc.stdout)

    def test_installed_layout_and_over_limit_rejection(self):
        with TemporaryDirectory() as temp:
            root = Path(temp) / "phdk-standards"
            root.mkdir()
            for source, destination in mappings():
                target = root / destination
                target.parent.mkdir(parents=True, exist_ok=True)
                copyfile(ROOT / source, target)
            proc = run_checker(root)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            with (root / "scripts/phdk_coherence_routing.py").open("a", encoding="utf-8") as out:
                out.write("# limit fixture\n" * 601)
            proc = run_checker(root)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("vendored Python exceeds 600 lines", proc.stderr)


if __name__ == "__main__":
    unittest.main()
