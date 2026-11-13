"""Source-only regression checks for the official Node 26 PHDK default."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def source(name):
    return (ROOT / name).read_text(encoding="utf-8")


class Node26PolicyTests(unittest.TestCase):
    def test_greenfield_default_in_all_active_routes(self):
        paths = (
            "technical_stack.md", "PHDK_SECURE.md", "PHDK_PLAN.md",
            "PHDK_AUTO.md", "PHDK_CHECK.md", "README.md", "AGENTS.md",
            "SKILL.md", "PHDK_NATIVE_RULES.md", "PHDK_COHERENCE_STANDARD.md",
        )
        for path in paths:
            with self.subTest(path=path):
                self.assertIn("Node.js 26", source(path))
                self.assertIn("LTS", source(path))
        self.assertIn("Node runtime:       Node.js 26.x Active LTS",
                      source("technical_stack.md"))
        self.assertNotIn("Node runtime:       Supported, security-patched LTS",
                         source("technical_stack.md"))
        self.assertIn("New projects MUST target patched Node.js 26.x",
                      source("PHDK_PLAN.md"))

    def test_existing_major_requires_scope_and_support(self):
        stack = source("technical_stack.md")
        secure = source("PHDK_SECURE.md").lower()
        native = source("PHDK_NATIVE_RULES.md").lower()
        for token in ("Node 24", "Node 22", "Node 20", "ADR", "rollback"):
            with self.subTest(token=token):
                self.assertIn(token, stack)
        self.assertIn("never silently bump", secure)
        self.assertIn("same-major security patch", secure)
        self.assertIn("no automatic major upgrades", native)
        self.assertIn("uat", secure)

    def test_version_and_manifest_consistent(self):
        version = source("VERSION").strip()
        self.assertRegex(version, r"^\\d+\\.\\d+\\.\\d+$")
        self.assertIn(f"**Version v{version}**", source("README.md"))
        self.assertTrue(source("CHANGELOG.md").startswith(f"## v{version}"))
        self.assertTrue(source("PHDK_EVOLUTION_STANDARD.md").startswith(f"## v{version}"))
        manifest = source("PHDK_MANIFEST.txt").splitlines()
        for entry in (
            "VERSION | VERSION", "README.md | README.md",
            "CHANGELOG.md | CHANGELOG.md",
            "technical_stack.md | TECHNICAL_STACK.md",
            "PHDK_SECURE.md | PHDK_SECURE.md",
            "PHDK_PLAN.md | PHDK_PLAN.md",
            "PHDK_CHECK.md | PHDK_CHECK.md",
            "PHDK_AUTO.md | PHDK_AUTO.md",
            "AGENTS.md | AGENTS.md", "SKILL.md | SKILL.md",
            "PHDK_NATIVE_RULES.md | PHDK_NATIVE_RULES.md",
        ):
            with self.subTest(entry=entry):
                self.assertEqual(manifest.count(entry), 1)


if __name__ == "__main__":
    unittest.main()
