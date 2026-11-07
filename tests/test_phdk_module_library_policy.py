"""Source-contract checks for the PHDK private module library routing; no provider access."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

def source(name):
    return (ROOT / name).read_text(encoding="utf-8")

class PrivateLibraryContract(unittest.TestCase):
    def test_vendored_policy_exists_exactly_once(self):
        manifest = source("PHDK_MANIFEST.txt")
        self.assertEqual(manifest.count("PHDK_MODULE_LIBRARY_STANDARD.md | PHDK_MODULE_LIBRARY_STANDARD.md"), 1)
        self.assertIn("PHDK_MODULE_LIBRARY_STANDARD.md", source("README.md"))

    def test_private_code_separated_from_public_metadata(self):
        policy = source("PHDK_MODULE_LIBRARY_STANDARD.md")
        self.assertIn("MODULES_CATALOG.json", policy)
        self.assertIn("PHDK_REUSE_CATALOG.json", policy)
        self.assertIn("private", policy.lower())
        self.assertIn("versions/<MAJOR.MINOR.PATCH>", policy)
        self.assertIn("SHA-256", policy)

    def test_agent_and_skill_route_to_private_policy(self):
        for name in ("AGENTS.md", "SKILL.md", "PHDK_NATIVE_RULES.md"):
            with self.subTest(name=name):
                self.assertIn("PHDK_MODULE_LIBRARY_STANDARD.md", source(name))

    def test_new_release_markers_aligned(self):
        version = source("VERSION").strip()
        self.assertEqual(version, "2.90.0")
        self.assertIn("**Version v2.90.0**", source("README.md"))
        self.assertTrue(source("CHANGELOG.md").startswith("## v2.90.0"))

    def test_not_an_automatic_public_module_publisher(self):
        policy = source("PHDK_MODULE_LIBRARY_STANDARD.md")
        self.assertIn("does not authorize copying", policy)
        self.assertIn("does not automatically", policy)
        self.assertIn("REPOSITORY_NOT_CREATED", policy)

if __name__ == "__main__":
    unittest.main()
