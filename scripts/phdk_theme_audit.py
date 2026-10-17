#!/usr/bin/env python3
"""Conservative static theme audit for a PHDK consumer; no runtime PASS claims."""
import argparse
import json
import os
from pathlib import Path
import re

SKIP_DIRS = {".git", ".next", ".nuxt", ".output", ".vercel", "node_modules", "dist", "build", "coverage", ".cache", "phdk-standards", "vendor", "__pycache__"}
UI_SUFFIXES = {".tsx", ".jsx", ".vue", ".svelte", ".html", ".css", ".scss", ".sass", ".less"}
CODE_SUFFIXES = UI_SUFFIXES | {".ts", ".js", ".mjs"}
REQUIRED_TOKENS = {"background", "foreground", "primary", "primary-foreground", "accent", "muted", "border", "ring", "popover"}
REQUIRED_TESTS = {"switching", "persistence", "visibility", "authorization"}
COLOR_LITERAL = re.compile(r"#[0-9a-fA-F]{3,8}\b|(?:rgba?|hsla?|oklch|color-mix)\s*\(", re.I)
CSS_COLOR_PROPERTY = re.compile(r"\b(?:color|background(?:-color)?|border(?:-[a-z]+)?-color|fill|stroke|outline-color|box-shadow)\s*:", re.I)
NAMED_CSS_COLOR = re.compile(r":\s*(?:white|black|red|green|blue|yellow|purple|orange|pink|gray|grey)\s*[;!}]", re.I)
JS_STYLE_COLOR = re.compile(r"\b(?:color|backgroundColor|borderColor|fill|stroke|outlineColor|boxShadow)\s*[:=]\s*['\"]", re.I)
TAILWIND_COLOR = re.compile(r"(?:bg|text|border|ring|from|via|to|fill|stroke)-\[\s*#[0-9a-fA-F]{3,8}\s*\]", re.I)
CONFIG_NAME = "phdk-theme.config.json"


def sources(root):
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for name in files:
            file = Path(base) / name
            if file.suffix.lower() in CODE_SUFFIXES and not name.endswith((".min.js", ".generated.ts", ".d.ts")):
                yield file


def checked_path(root, raw):
    if not isinstance(raw, str) or not raw.strip():
        return None
    p = Path(raw)
    if p.is_absolute() or ".." in p.parts:
        return None
    target = (root / p).resolve()
    if not target.is_relative_to(root.resolve()):
        return None
    return target


def audit(root):
    root = root.resolve()
    problems = []
    def add(code, detail, file=None, line=None):
        finding = {"code": code, "detail": detail}
        if file is not None:
            finding["file"] = str(file)
        if line is not None:
            finding["line"] = line
        problems.append(finding)
    files = list(sources(root))
    config_file = root / CONFIG_NAME
    if not config_file.is_file():
        if any(f.suffix.lower() in UI_SUFFIXES for f in files):
            add("CONFIG_MISSING", CONFIG_NAME + " is mandatory for UI products")
            return {"status": "FAIL", "scope": "UI", "findings": problems, "runtime_verified": False}
        return {"status": "NOT_APPLICABLE", "scope": "NO_UI_SOURCE_DETECTED", "findings": [], "runtime_verified": False}
    try:
        config = json.loads(config_file.read_text(encoding="utf-8"))
        if not isinstance(config, dict):
            raise ValueError("must be a JSON object")
    except (OSError, ValueError) as exc:
        add("CONFIG_INVALID", str(exc))
        return {"status": "FAIL", "scope": "UNKNOWN", "findings": problems, "runtime_verified": False}
    for key in ("token_css", "editor_source", "runtime_source"):
        target = checked_path(root, config.get(key))
        if target is None or not target.is_file():
            add("MISSING_SOURCE", key + " must identify an existing in-repository file")
    css_file = checked_path(root, config.get("token_css"))
    selectors = config.get("selectors")
    if not isinstance(selectors, dict):
        selectors = {}
    if css_file and css_file.is_file():
        if css_file.suffix.lower() not in {".css", ".scss", ".sass", ".less"}:
            add("TOKEN_FORMAT", "token_css must be a CSS-family stylesheet")
        css = css_file.read_text(encoding="utf-8")
        for theme in ("light", "dark", "corporate"):
            selector = selectors.get(theme)
            if not isinstance(selector, str) or not selector.strip():
                add("SELECTOR_MISSING", "selector missing for " + theme)
                continue
            pat = re.escape(selector.strip()) + r"\s*\{([^{}]*)\}"
            match = re.search(pat, css, flags=re.S)
            if match is None:
                add("PALETTE_MISSING", "CSS selector not found: " + selector)
                continue
            present = set(re.findall(r"--([a-z][a-z0-9-]*)\s*:", match.group(1), re.I))
            for token in sorted(REQUIRED_TOKENS - present):
                add("TOKEN_MISSING", theme + " lacks --" + token)
    route = config.get("editor_route")
    if not isinstance(route, str) or not route.startswith("/") or not any(v in route.lower() for v in ("setting", "configur")):
        add("EDITOR_ROUTE", "editor_route must identify Superadmin settings")
    if not isinstance(config.get("corporate_visibility_setting"), str) or not config["corporate_visibility_setting"].strip():
        add("CORPORATE_FLAG", "persisted corporate visibility setting key missing")
    tests = config.get("tests")
    if not isinstance(tests, dict):
        tests = {}
    for key in sorted(REQUIRED_TESTS):
        target = checked_path(root, tests.get(key))
        if target is None or not target.is_file():
            add("TEST_MISSING", "tests." + key + " must identify a real test file")
    allowlist = config.get("exceptions", [])
    if not isinstance(allowlist, list):
        add("EXCEPTIONS_INVALID", "exceptions must be an array")
        allowlist = []
    valid_exceptions = set()
    for entry in allowlist:
        if not isinstance(entry, dict):
            add("EXCEPTION_INVALID", "each exception must be an object")
            continue
        name, value, reason = entry.get("file"), entry.get("value"), entry.get("reason")
        target = checked_path(root, name)
        if (target is None or not target.is_file() or not isinstance(value, str)
                or not COLOR_LITERAL.fullmatch(value.strip()) and not re.fullmatch(r"#[0-9a-fA-F]{3,8}", value.strip())
                or not isinstance(reason, str) or len(reason.strip()) < 12):
            add("EXCEPTION_INVALID", "file/value/reason must be narrow, valid and justified")
            continue
        valid_exceptions.add((target, value.strip().lower()))
    for file in files:
        if file == css_file or file.suffix.lower() not in UI_SUFFIXES:
            continue
        try:
            content = file.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            add("SOURCE_UNREADABLE", "cannot inspect source", file.relative_to(root))
            continue
        for i, line in enumerate(content.splitlines(), 1):
            match = COLOR_LITERAL.search(line)
            css_like = file.suffix.lower() in {".css", ".scss", ".sass", ".less"}
            candidate = ((css_like and (CSS_COLOR_PROPERTY.search(line) or NAMED_CSS_COLOR.search(line)))
                         or (not css_like and (TAILWIND_COLOR.search(line) or
                             (match and (JS_STYLE_COLOR.search(line) or "style=" in line or "className=" in line or "class=" in line or "fill=" in line or "stroke=" in line)))))
            if not candidate:
                continue
            if not match and not NAMED_CSS_COLOR.search(line):
                continue
            value = match.group(0) if match else NAMED_CSS_COLOR.search(line).group(0)
            if (file, value.strip().lower()) in valid_exceptions:
                continue
            add("HARDCODED_COLOR", "use semantic tokens; offending literal " + value, file.relative_to(root), i)
    return {"status": "FAIL" if problems else "STATIC_PASS", "scope": "UI", "findings": problems, "runtime_verified": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = audit(args.root)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(result["status"] + ": " + str(len(result["findings"])) + " finding(s); runtime unverified")
        for item in result["findings"]:
            print(item["code"], item.get("file", ""), item.get("line", ""), item["detail"])
    raise SystemExit(1 if result["status"] == "FAIL" else 0)


if __name__ == "__main__":
    main()
