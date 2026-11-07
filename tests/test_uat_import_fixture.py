"""Static file round trips for UAT input fixtures. No product or service is run."""

import csv
import hashlib
import io
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from phdk_uat_import_fixture import generate

try:
    import openpyxl
except ImportError:
    openpyxl = None


class UatImportFixtureTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.template = self.root / "plantilla.csv"
        self.raw = 'Instrucciones para la carga\r\n"Código";Unidades;Título\r\n'.encode("utf-8-sig")
        self.template.write_bytes(self.raw)
        self.out = self.root / "fixtures"
        self.recipe = {
            "run": "r7k2", "header_row": 2, "text": {"delimiter": ";", "encoding": "utf-8-sig"},
            "rows": [{"Código": "0001", "Unidades": 2, "Título": "Silla; café\nBogotá"}],
            "negatives": [{"id": "missing-code", "row": 1, "column": "Código", "value": None,
                           "expected": "Missing required code on the first data row"}],
        }

    def render(self):
        p = self.root / "recipe.json"
        p.write_text(json.dumps(self.recipe), encoding="utf-8")
        return generate(self.template, p, self.out)

    def test_delimited_csv_and_declared_txt_round_trip(self):
        for ext in (".csv", ".txt"):
            with self.subTest(ext=ext):
                self.template = self.root / ("plantilla" + ext)
                self.template.write_bytes(self.raw)
                self.out = self.root / ext[1:]
                manifest = self.render()
                self.assertEqual(self.template.read_bytes(), self.raw)
                self.assertEqual(manifest["template_sha256"], hashlib.sha256(self.raw).hexdigest())
                for name, expected_code in (("valid", "0001"), ("invalid-missing-code", "")):
                    data = (self.out / (name + ext)).read_bytes()
                    self.assertTrue(data.startswith(self.raw))
                    rows = list(csv.reader(io.StringIO(data.decode("utf-8-sig")), delimiter=";"))
                    self.assertEqual(rows[-1], [expected_code, "2", "Silla; café\nBogotá"])
                    self.assertEqual(hashlib.sha256(data).hexdigest(), next(
                        item["sha256"] for item in manifest["files"] if item["file"] == name + ext))

    def test_rejects_nonblank_template_bad_header_and_unsafe_name(self):
        self.template.write_bytes(self.raw + b"real;5;record")
        with self.assertRaisesRegex(ValueError, "data rows"):
            self.render()
        self.template.write_bytes(self.raw)
        self.recipe["rows"][0]["Codigo"] = self.recipe["rows"][0].pop("Código")
        with self.assertRaisesRegex(ValueError, "headers"):
            self.render()
        self.recipe["rows"][0]["Código"] = self.recipe["rows"][0].pop("Codigo")
        self.recipe["negatives"][0]["id"] = "../escape"
        with self.assertRaisesRegex(ValueError, "unsafe"):
            self.render()
        self.assertFalse(self.out.exists())

    def test_refuses_existing_directory_and_reserved_git_path(self):
        self.out.mkdir()
        marker = self.out / "keep"
        marker.write_text("owner data")
        with self.assertRaisesRegex(ValueError, "fresh"):
            self.render()
        self.assertEqual(marker.read_text(), "owner data")
        self.out = self.root / ".git"
        with self.assertRaisesRegex(ValueError, "fresh"):
            self.render()

    def test_bounds_and_serialized_no_op_mutation(self):
        row = self.recipe["rows"][0]
        self.recipe["rows"] = [row] * 33
        with self.assertRaisesRegex(ValueError, "32 synthetic"):
            self.render()
        self.recipe["rows"] = [row]
        n = self.recipe["negatives"][0]
        self.recipe["negatives"] = [n] * 9
        with self.assertRaisesRegex(ValueError, "at most 8"):
            self.render()
        self.recipe["negatives"] = [dict(n, column="Unidades", value="2")]
        with self.assertRaisesRegex(ValueError, "matches valid bytes"):
            self.render()
        self.assertFalse(self.out.exists())

    @unittest.skipIf(openpyxl is None, "openpyxl not installed")
    def test_xlsx_preserves_other_parts_formula_and_native_types(self):
        self.template = self.root / "plantilla.xlsx"
        book = openpyxl.Workbook()
        sheet = book.active
        sheet.title = "Recepción"
        sheet.append(["Instrucciones"])
        sheet.append(["Código", "Unidades", "Fecha", "Total", "Título"])
        sheet["D3"] = "=B3*2"
        book.create_sheet("Instrucciones")["A1"] = "Complete solo los campos editables"
        book.save(self.template)
        original = self.template.read_bytes()
        del self.recipe["text"]
        self.recipe["sheet"] = "Recepción"
        self.recipe["rows"][0]["Fecha"] = {"date": "2026-11-07"}
        self.render()
        self.assertEqual(self.template.read_bytes(), original)
        with ZipFile(self.template) as old, ZipFile(self.out / "valid.xlsx") as new:
            self.assertEqual(old.namelist(), new.namelist())
            self.assertEqual([n for n in old.namelist() if new.read(n) != old.read(n)],
                             ["xl/worksheets/sheet1.xml"])
        for name, code in (("valid", "0001"), ("invalid-missing-code", None)):
            wb = openpyxl.load_workbook(self.out / (name + ".xlsx"))
            self.assertEqual([c.value for c in wb["Recepción"][3]],
                             [code, 2, date(2026, 11, 7), "=B3*2", "Silla; café\nBogotá"])
            wb.close()
        self.out = self.root / "would-overwrite-formula"
        self.recipe["rows"][0]["Total"] = 200
        with self.assertRaisesRegex(ValueError, "formula column"):
            self.render()
        del self.recipe["rows"][0]["Total"]
        with ZipFile(io.BytesIO(original)) as old, ZipFile(self.template, "w") as dangerous:
            for n in old.namelist():
                content = old.read(n)
                if n == "_rels/.rels":
                    content = content.replace(b"</Relationships>",
                        b'<Relationship Id="r99" TargetMode="External" Type="x" Target="https://example.test/" /></Relationships>')
                dangerous.writestr(n, content)
        with self.assertRaisesRegex(ValueError, "external workbook relationship"):
            self.render()
        self.template.write_bytes(original)
        with ZipFile(self.template, "a") as z:
            z.writestr("xl/vbaProject.bin", b"fake test part")
        with self.assertRaisesRegex(ValueError, "project.*adapter"):
            self.render()
