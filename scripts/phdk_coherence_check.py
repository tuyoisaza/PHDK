#!/usr/bin/env python3
"""Static consistency checks; no claim of runtime or semantic correctness."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parent.parent
errors = []
version = (root / "VERSION").read_text(encoding="utf-8").strip()
readme = (root / "README.md").read_text(encoding="utf-8")
changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
if not re.fullmatch(r"\d+\.\d+\.\d+", version):
    errors.append("invalid VERSION")
if f"**Version v{version}**" not in readme:
    errors.append("README version mismatch")
releases = re.findall(r"^## v(\d+\.\d+\.\d+)\b", changelog, re.M)
if not releases or releases[0] != version:
    errors.append("newest CHANGELOG version mismatch")
sources, destinations = set(), set()
for n, raw in enumerate((root / "PHDK_MANIFEST.txt").read_text(encoding="utf-8").splitlines(), 1):
    line = raw.strip()
    if not line or line.startswith("#"):
        continue
    p = [x.strip() for x in line.split("|")]
    if len(p) != 2 or not all(p):
        errors.append(f"manifest line {n}: malformed")
        continue
    src, dst = p
    for path in p:
        if Path(path).is_absolute() or ".." in Path(path).parts:
            errors.append(f"manifest line {n}: unsafe path")
    if src in sources or dst in destinations:
        errors.append(f"manifest line {n}: duplicate")
    sources.add(src)
    destinations.add(dst)
    if not (root / src).is_file():
        errors.append(f"manifest line {n}: missing {src}")
for mandatory in ["VERSION", "README.md", "CHANGELOG.md", "AGENTS.md", "PHDK_PREFLIGHT.md", "PHDK_COHERENCE_STANDARD.md", "PHDK_EVOLUTION_STANDARD.md", "CHANGE_MANAGEMENT.md", "scripts/phdk_coherence_check.py", "PHDK_AUTO_CONTINUITY.md", "scripts/phdk_auto_gate.py"]:
    if mandatory not in sources:
        errors.append(f"manifest lacks {mandatory}")
for entrypoint in ["README.md", "AGENTS.md", "PHDK_NATIVE_RULES.md", "CHANGE_MANAGEMENT.md", "SKILL.md"]:
    file = root / entrypoint
    if not file.exists() and entrypoint == "SKILL.md":
        continue  # SKILL.md is canonical-tool-only, not in the vendoring manifest.
    if not file.is_file() or "PHDK_EVOLUTION_STANDARD.md" not in file.read_text(encoding="utf-8"):
        errors.append(f"{entrypoint} missing PHDK evolution standard reference")
if errors:
    print("\n".join("FAIL: " + x for x in errors), file=sys.stderr)
    sys.exit(1)
print(f"PASS: v{version}, {len(sources)} manifest mappings (static only)")
