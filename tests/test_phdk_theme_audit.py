"""Unit tests for the vendorable PHDK static theme checker."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "phdk_theme_audit.py"
spec = importlib.util.spec_from_file_location("phdk_theme_audit", MODULE)
audit_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit_module)

TOKENS = ("background", "foreground", "primary", "primary-foreground", "accent", "muted", "border", "ring", "popover")


class ThemeAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "src").mkdir()
        (self.root / "tests").mkdir()
        stylesheet = "".join(selector + " {\n" + "".join(f"  --{token}: #333;\n" for token in TOKENS) + "}\n"
                             for selector in (":root", ".dark", ".corporate"))
        (self.root / "src" / "tokens.css").write_text(stylesheet)
        (self.root / "src" / "editor.tsx").write_text("export const Editor = () => null;\n")
        (self.root / "src" / "runtime.tsx").write_text("export const Theme = () => null;\n")
        (self.root / "tests" / "themes.test.tsx").write_text("test('theme', () => {});\n")
        self.config = {
            "token_css": "src/tokens.css",
            "selectors": {"light": ":root", "dark": ".dark", "corporate": ".corporate"},
            "editor_route": "/superadmin/settings/templates",
            "editor_source": "src/editor.tsx",
            "runtime_source": "src/runtime.tsx",
            "corporate_visibility_setting": "theme.corporate.enabled",
            "tests": {key: "tests/themes.test.tsx" for key in ("switching", "persistence", "visibility", "authorization")},
            "exceptions": [],
        }
        self.write_config()

    def write_config(self):
        (self.root / "phdk-theme.config.json").write_text(json.dumps(self.config))

    def check(self):
        return audit_module.audit(self.root)

    def test_static_pass_not_runtime_pass(self):
        result = self.check()
        self.assertEqual(result["status"], "STATIC_PASS")
        self.assertIs(result["runtime_verified"], False)

    def test_detect_hardcoded_css_and_jsx(self):
        (self.root / "src" / "rogue.css").write_text(".button { color: #fff; }\n")
        (self.root / "src" / "button.tsx").write_text("export const A = () => <div className='bg-[#ff00ff]'/>;\n")
        result = self.check()
        self.assertEqual(len([x for x in result["findings"] if x["code"] == "HARDCODED_COLOR"]), 2)

    def test_missing_palette_token_and_test(self):
        css = self.root / "src" / "tokens.css"
        css.write_text(css.read_text().replace("  --ring: #333;\n", "", 1))
        self.config["tests"]["authorization"] = "tests/missing.test.tsx"
        self.write_config()
        codes = {x["code"] for x in self.check()["findings"]}
        self.assertTrue({"TOKEN_MISSING", "TEST_MISSING"} <= codes)

    def test_missing_config_is_fail_for_ui(self):
        (self.root / "phdk-theme.config.json").unlink()
        self.assertEqual(self.check()["findings"][0]["code"], "CONFIG_MISSING")

    def test_specific_exception_only(self):
        (self.root / "src" / "badge.css").write_text(".brand { color: #f00; background-color: #00f; }\n")
        self.config["exceptions"] = [{"file": "src/badge.css", "value": "#f00", "reason": "Fixed official external logo color"}]
        self.write_config()
        result = self.check()
        self.assertEqual(len([x for x in result["findings"] if x["code"] == "HARDCODED_COLOR"]), 1)

    def test_path_traversal_rejected(self):
        self.config["editor_source"] = "../editor.tsx"
        self.write_config()
        self.assertIn("MISSING_SOURCE", {x["code"] for x in self.check()["findings"]})


if __name__ == "__main__":
    unittest.main()
