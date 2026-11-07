#!/usr/bin/env python3
"""Fill copies of a blank import template with a project's synthetic UAT rows (offline)."""

import argparse
import codecs
import csv
import hashlib
import io
import json
import math
import posixpath
import re
import shutil
import tempfile
from datetime import date
from itertools import chain
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import BadZipFile, ZipFile

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
TAG = "{" + NS + "}"
LIMIT = 32 * 1024 * 1024
MAX_ROWS = 32
MAX_NEGATIVES = 8


def require(condition, message):
    if not condition:
        raise ValueError(message)


def keys(obj, allowed, label):
    require(isinstance(obj, dict) and not (obj.keys() - set(allowed)), f"unsupported {label} fields")


def value(v, xlsx):
    if isinstance(v, dict):
        require(xlsx and set(v) == {"date"} and isinstance(v["date"], str), "invalid typed value")
        return date.fromisoformat(v["date"])
    require(v is None or isinstance(v, (str, bool, int, float)), "unsupported cell value")
    if isinstance(v, float):
        require(math.isfinite(v), "non-finite number")
    if isinstance(v, str):
        require(len(v) <= 32767 and not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", v),
                "invalid spreadsheet string")
        if not xlsx:
            require(not re.match(r"\s*[=+@-]", v) or re.fullmatch(r"[+-]\d+(?:[.,]\d+)?", v),
                    "formula-like text in delimited fixture; use a safe synthetic literal")
    return v


def variants(recipe, xlsx):
    rows = recipe.get("rows")
    require(isinstance(rows, list) and 1 <= len(rows) <= MAX_ROWS
            and all(isinstance(r, dict) and 1 <= len(r) <= 128 for r in rows),
            "use 1 to 32 synthetic rows with at most 128 inputs each")
    require(all(set(r) == set(rows[0]) for r in rows), "input rows must address the same headers")
    base = [{k: value(v, xlsx) for k, v in r.items()} for r in rows]
    yield "valid", base, None
    negatives = recipe.get("negatives", [])
    require(isinstance(negatives, list) and len(negatives) <= MAX_NEGATIVES, "use at most 8 negative fixtures")
    seen = set()
    for n in negatives:
        keys(n, ("id", "row", "column", "value", "expected"), "negative")
        ident, index, field = n.get("id"), n.get("row"), n.get("column")
        require(isinstance(ident, str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", ident)
                and len(ident) <= 64 and ident not in seen, "unsafe or duplicate negative id")
        seen.add(ident)
        require(type(index) is int and 1 <= index <= len(base) and isinstance(field, str)
                and field in base[index - 1] and "value" in n, "negative must address an existing input cell")
        require(isinstance(n.get("expected"), str) and n["expected"].strip(), "missing negative expectation")
        new = value(n["value"], xlsx)
        old = base[index - 1][field]
        require((type(old), old) != (type(new), new), "negative mutation did not change the cell")
        changed = base.copy()
        changed[index - 1] = {**base[index - 1], field: new}
        yield "invalid-" + ident, changed, {"data_row": index, "column": field, "expected": n["expected"]}


def check_headers(headers, fields):
    require(headers and all(isinstance(h, str) and h.strip() for h in headers)
            and len(set(headers)) == len(headers), "header contains blank or duplicate names; use a project adapter")
    require(set(fields) <= set(headers), "recipe headers do not match the downloaded template")


def text_writer(data, recipe, header, start):
    settings = recipe.get("text")
    keys(settings, ("encoding", "delimiter", "quotechar"), "delimited text")
    encoding = codecs.lookup(settings["encoding"]).name
    require(encoding in ("utf-8", "utf-8-sig", "cp1252", "iso8859-1", "utf-16"), "unsupported text encoding")
    require((encoding == "utf-8-sig") == data.startswith(codecs.BOM_UTF8), "UTF-8 BOM differs from recipe")
    delimiter, quote = settings.get("delimiter"), settings.get("quotechar", '"')
    require(isinstance(delimiter, str) and len(delimiter) == 1 and delimiter not in "\r\n\x00"
            and isinstance(quote, str) and len(quote) == 1 and quote not in "\r\n\x00" and quote != delimiter,
            "invalid declared delimiter or quote character")
    source = data.decode(encoding)
    require("\x00" not in source and not data.startswith(b"PK"), "binary data in delimited template")
    f = io.StringIO(source, newline="")
    reader = csv.reader(f, delimiter=delimiter, quotechar=quote, strict=True)
    headers, prefix_end, count = [], 0, 0
    for count, row in enumerate(reader, 1):
        if count == header:
            headers = row
        if count < start:
            prefix_end = f.tell()
        else:
            require(not any(cell != "" for cell in row), "downloaded text template contains data rows")
    check_headers(headers, recipe["rows"][0])
    eol = re.search(r"\r\n|\r|\n", source)
    newline = eol.group() if eol else "\r\n"
    prefix = source[:prefix_end]
    if prefix and not prefix.endswith(("\r", "\n")):
        prefix += newline
    prefix += newline * max(0, start - 1 - count)
    # Retain the input byte order on either native or non-native UTF-16 hosts.
    codec = ("utf-16-le" if data.startswith(codecs.BOM_UTF16_LE) else "utf-16-be") if encoding == "utf-16" else encoding
    bom = data[:2] if encoding == "utf-16" else b""

    def write(path, records):
        out = io.StringIO(newline="")
        out.write(prefix)
        writer = csv.writer(out, delimiter=delimiter, quotechar=quote, lineterminator=newline)
        for record in records:
            writer.writerow([record.get(k) for k in headers])
        rendered = out.getvalue()
        parsed = list(csv.reader(io.StringIO(rendered, newline=""), delimiter=delimiter, quotechar=quote, strict=True))
        wanted = [["" if r.get(h) is None else str(r[h]) for h in headers] for r in records]
        require(parsed[start - 1:] == wanted, "delimited fixture did not round-trip")
        path.write_bytes(bom + rendered.encode(codec))
    return write


def xlsx_writer(data, recipe, header, start):
    try:
        import openpyxl
        from openpyxl.utils import get_column_letter, range_boundaries
    except ImportError as exc:
        raise ValueError("XLSX inspection requires an installed openpyxl or a project workbook adapter") from exc

    def plain_package():
        # Fail closed on macros, signatures, external links, drawings, tables, pivots,
        # encryption and unfamiliar package parts. All untouched members are copied verbatim.
        allowed = r"(?:\[Content_Types\]\.xml|_rels/\.rels|docProps/(?:app|core)\.xml|xl/(?:workbook|styles|sharedStrings)\.xml|xl/_rels/workbook\.xml\.rels|xl/theme/theme\d+\.xml|xl/worksheets/sheet\d+\.xml)"
        with ZipFile(io.BytesIO(data)) as z:
            infos = z.infolist()
            names = z.namelist()
            require(len(names) == len(set(names)) and sum(i.file_size for i in infos) <= LIMIT,
                    "duplicate or oversized workbook parts")
            require(all(re.fullmatch(allowed, i.filename) and not (i.flag_bits & 1) for i in infos),
                    "complex or protected workbook requires the project's preserving adapter")
            parts = {n: z.read(n) for n in names}
        require(all(b"<!DOCTYPE" not in v.upper() and b"<!ENTITY" not in v.upper() for v in parts.values()),
                "unsupported workbook XML")
        for n, xml in parts.items():
            if n.endswith(".rels"):
                require(all(r.get("TargetMode", "Internal") == "Internal"
                            and not re.match(r"^(?:[a-z][a-z0-9+.-]*:|//)", r.get("Target", ""), re.I)
                            for r in ET.fromstring(xml)), "external workbook relationship requires a project adapter")
        require(b"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"
                in parts["[Content_Types].xml"], "expected plain .xlsx content type")
        return parts

    parts = plain_package()
    name = recipe.get("sheet")
    require(isinstance(name, str) and name, "XLSX needs a named data sheet")
    book = openpyxl.load_workbook(io.BytesIO(data), read_only=True, data_only=False)
    try:
        require(name in book.sheetnames, "named data sheet is missing")
        ws = book[name]
        require(ws.sheet_state == "visible" and ws.max_column and ws.max_column <= 512
                and ws.max_row and ws.max_row <= 100000, "unsupported sheet dimensions or visibility")
        headers = next(ws.iter_rows(min_row=header, max_row=header, values_only=True))
        check_headers(headers, recipe["rows"][0])
    finally:
        book.close()

    workbook = ET.fromstring(parts["xl/workbook.xml"])
    protection = workbook.find(TAG + "workbookProtection")
    require(protection is None or not any(v not in ("0", "false") for v in protection.attrib.values()),
            "protected workbook requires a project adapter")
    sheet = next(s for s in workbook.findall(f"{TAG}sheets/{TAG}sheet")
                 if s.get("name") == name)
    rel_id = sheet.get("{" + REL + "}id")
    rel = next((r for r in ET.fromstring(parts["xl/_rels/workbook.xml.rels"]) if r.get("Id") == rel_id), None)
    require(rel is not None and not rel.get("TargetMode"), "missing local worksheet relationship")
    target = rel.get("Target", "")
    member = target.lstrip("/") if target.startswith("/") else posixpath.normpath(posixpath.join("xl", target))
    require(re.fullmatch(r"xl/worksheets/sheet\d+\.xml", member) and member in parts, "unrecognized data sheet path")
    root = ET.fromstring(parts[member])
    unsupported = {"mergeCells", "sheetProtection", "extLst", "conditionalFormatting"}
    require(all(e.tag.startswith(TAG) and e.tag[len(TAG):] not in unsupported
                and all("}" not in k or k == "{http://www.w3.org/XML/1998/namespace}space"
                        for k in e.attrib) for e in root.iter()),
            "extended, merged or protected data sheet requires a project workbook adapter")
    sheetdata = root.find(TAG + "sheetData")
    require(sheetdata is not None, "worksheet has no sheetData")
    col = {h: i for i, h in enumerate(headers, 1)}
    inputs = set(recipe["rows"][0])
    formula_rows = {}
    for row in sheetdata.findall(TAG + "row"):
        if int(row.get("r")) < start:
            continue
        for c in row.findall(TAG + "c"):
            coord = re.fullmatch(r"([A-Z]+)([1-9]\d*)", c.get("r", ""))
            require(coord, "invalid worksheet cell reference")
            f = c.find(TAG + "f")
            if f is not None:
                require(f.get("t", "normal") == "normal", "array or shared formula requires a project adapter")
                formula_rows.setdefault(coord[1], set()).add(int(coord[2]))
            else:
                require(not c.findtext(TAG + "v") and not any(t.text for t in c.iter(TAG + "t")),
                        "downloaded workbook contains data rows")
    require(not any(get_column_letter(col[h]) in formula_rows for h in inputs), "recipe would overwrite a formula column")
    requested = set(range(start, start + len(recipe["rows"])))
    require(all(requested <= locations for locations in formula_rows.values()),
            "formula cells are not prefilled across the requested rows; use a project adapter")

    def write(path, records):
        tree = ET.fromstring(parts[member])
        sd = tree.find(TAG + "sheetData")
        rows = {int(r.get("r")): r for r in sd.findall(TAG + "row")}
        for index, record in enumerate(records, start):
            row = rows.get(index)
            if row is None:
                row = ET.Element(TAG + "row", r=str(index))
                sd.insert(sum(1 for prior in sd if int(prior.get("r")) < index), row)
            cells = {c.get("r"): c for c in row.findall(TAG + "c")}
            for h, v in record.items():
                if v is None:
                    continue
                letter = get_column_letter(col[h])
                ref = letter + str(index)
                c = cells.get(ref)
                if c is None:
                    c = ET.SubElement(row, TAG + "c", r=ref)
                else:
                    for child in list(c):
                        if child.tag in (TAG + "is", TAG + "v"):
                            c.remove(child)
                c.set("t", "inlineStr" if isinstance(v, str) else "b" if type(v) is bool else "d" if type(v) is date else "n")
                if isinstance(v, str):
                    e = ET.SubElement(ET.SubElement(c, TAG + "is"), TAG + "t")
                    if v != v.strip():
                        e.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
                    e.text = v
                else:
                    ET.SubElement(c, TAG + "v").text = str(int(v)) if type(v) is bool else str(v)
            row[:] = sorted(row, key=lambda c: openpyxl.utils.column_index_from_string(re.match("[A-Z]+", c.get("r"))[0]))
        dim = tree.find(TAG + "dimension")
        if dim is not None:
            x1, y1, x2, y2 = range_boundaries(dim.get("ref"))
            dim.set("ref", f"{get_column_letter(x1)}{y1}:{get_column_letter(x2)}{max(y2, start + len(records) - 1)}")
        ET.register_namespace("", NS)
        with ZipFile(path, "w") as output, ZipFile(io.BytesIO(data)) as original:
            for info in original.infolist():
                output.writestr(info, ET.tostring(tree, encoding="utf-8") if info.filename == member else parts[info.filename])
        restored = openpyxl.load_workbook(path, read_only=True, data_only=False)
        try:
            actual = restored[name].iter_rows(min_row=start, max_row=start + len(records) - 1, values_only=True)
            for got, wanted in zip(actual, records, strict=True):
                require(all(got[col[h] - 1] == v for h, v in wanted.items()), "XLSX values did not round-trip")
        finally:
            restored.close()
    return write


def generate(template, recipe_path, out):
    ext = template.suffix.lower()
    require(ext in (".csv", ".txt", ".xlsx"), "unsupported format; use the project's native adapter")
    for path in (template, recipe_path):
        require(path.is_file() and not path.is_symlink() and path.stat().st_size <= LIMIT, "expected a bounded local file")
    require(out.name and ".." not in out.parts and ".git" not in (p.lower() for p in out.parts)
            and not out.exists() and not out.is_symlink() and out.parent.is_dir()
            and not any(p.is_symlink() for p in out.parents), "output must be a fresh directory under a real parent")
    data = template.read_bytes()
    recipe = json.loads(recipe_path.read_text(encoding="utf-8-sig"))
    keys(recipe, ("run", "header_row", "start_row", "sheet" if ext == ".xlsx" else "text", "rows", "negatives"), "recipe")
    require(isinstance(recipe.get("run"), str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", recipe["run"]), "invalid run key")
    header = recipe.get("header_row", 1)
    require(type(header) is int and 1 <= header <= 100000, "invalid header row")
    start = recipe.get("start_row", header + 1)
    require(type(start) is int and header < start <= 100000, "invalid first data row")
    generated = variants(recipe, ext == ".xlsx")
    first = next(generated)
    writer = (xlsx_writer if ext == ".xlsx" else text_writer)(data, recipe, header, start)
    manifest = {"status": "GENERATED_ONLY", "run": recipe["run"], "template_sha256": hashlib.sha256(data).hexdigest(),
                "files": []}
    with tempfile.TemporaryDirectory(dir=out.parent) as temp:
        staging = Path(temp)
        total = 0
        for label, records, mutation in chain([first], generated):
            path = staging / (label + ext)
            writer(path, records)
            total += path.stat().st_size
            require(total <= 64 * 1024 * 1024, "fixture batch exceeds 64 MiB")
            item = {"file": path.name, "rows": len(records), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            if mutation:
                require(item["sha256"] != manifest["files"][0]["sha256"], "negative fixture matches valid bytes")
                item["mutation"] = mutation
            manifest["files"].append(item)
        (staging / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        out.mkdir()
        created = []
        try:
            for path in staging.iterdir():
                destination = out / path.name
                with destination.open("xb") as dst, path.open("rb") as src:
                    created.append(destination)
                    shutil.copyfileobj(src, dst)
        except OSError:
            for path in created:
                path.unlink(missing_ok=True)
            if not any(out.iterdir()):
                out.rmdir()
            raise
    return manifest


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for arg in ("template", "recipe", "out"):
        p.add_argument("--" + arg, type=Path, required=True)
    args = p.parse_args()
    try:
        result = generate(args.template, args.recipe, args.out)
    except (OSError, ValueError, TypeError, KeyError, LookupError, StopIteration, BadZipFile, ET.ParseError, csv.Error) as error:
        p.exit(2, f"Fixture generation stopped: {error}\n")
    print(f"Generated {len(result['files'])} fixtures and manifest.json; product import has not run.")


if __name__ == "__main__":
    main()
