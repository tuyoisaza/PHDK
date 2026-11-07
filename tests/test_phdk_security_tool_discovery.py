"""Read-only discovery regressions; synthetic filesystem, no software executed."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

source = Path(__file__).resolve().parents[1] / "scripts" / "phdk_security_tool_discovery.py"
spec = importlib.util.spec_from_file_location("discovery", source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ToolDiscoveryTests(unittest.TestCase):
    def test_windows_user_local_uv_is_found_outside_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            folder = home / ".local" / "bin"
            folder.mkdir(parents=True)
            (folder / "uv.exe").write_bytes(b"fixture; not executed")
            result = module.discover(
                "uv", project=tmp,
                env={"USERPROFILE": str(home), "LOCALAPPDATA": str(home / "AppData/Local"),
                     "APPDATA": str(home / "AppData/Roaming"), "PATH": ""},
                windows=True,
            )
            self.assertEqual(result["status"], "FOUND_PATH")
            self.assertEqual(result["candidates"][0]["source"], "KNOWN_LOCATION")
            self.assertFalse(result["executed"])

    def test_not_located_is_not_declared_absent(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = module.discover(
                "uv", project=tmp, env={"HOME": tmp, "PATH": ""}, windows=False
            )
            self.assertEqual(result["status"], "NOT_LOCATED_IN_BOUNDED_SEARCH")
            self.assertEqual(result["installed_or_usable"], "UNVERIFIED")

    def test_rejects_unexpected_tool_names(self):
        with self.assertRaises(ValueError):
            module.discover("../../unexpected")


if __name__ == "__main__":
    unittest.main()
