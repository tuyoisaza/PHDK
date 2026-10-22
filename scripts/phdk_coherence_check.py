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
for mandatory in ["VERSION", "README.md", "CHANGELOG.md", "AGENTS.md", "PHDK_PREFLIGHT.md", "PHDK_COHERENCE_STANDARD.md", "PHDK_EVOLUTION_STANDARD.md", "CHANGE_MANAGEMENT.md", "scripts/phdk_coherence_check.py", "PHDK_AUTO_CONTINUITY.md", "scripts/phdk_auto_gate.py", "PHDK_DESIGN.md", "SKILL.md", "PHDK_NATIVE_RULES.md", "UAT_STANDARD.md", "PHDK_UAT_PREP.md"]:
    if mandatory not in sources:
        errors.append(f"manifest lacks {mandatory}")
for entrypoint in ["README.md", "AGENTS.md", "PHDK_NATIVE_RULES.md", "CHANGE_MANAGEMENT.md", "SKILL.md"]:
    file = root / entrypoint
    if not file.is_file() or "PHDK_EVOLUTION_STANDARD.md" not in file.read_text(encoding="utf-8"):
        errors.append(f"{entrypoint} missing PHDK evolution standard reference")

# A policy header before YAML front matter prevents this entrypoint from
# retaining the conventional skill metadata structure.
skill_file = root / "SKILL.md"
if skill_file.is_file() and not skill_file.read_text(encoding="utf-8").startswith("---\n"):
    errors.append("SKILL.md metadata must remain the first front-matter block")

# Design routing guards are source-level signals, never evidence of an owner
# decision, rendered preview, actual execution, or downstream adoption.
for entrypoint in ["README.md", "AGENTS.md", "PHDK_NATIVE_RULES.md", "SKILL.md",
                   "PHDK_PLAN.md", "PHDK_LIFECYCLE.md", "PHDK_AUTO.md",
                   "PHDK_AUTO_CONTINUITY.md", "PHDK_UX_UI.md"]:
    file = root / entrypoint
    if not file.is_file() or "PHDK_DESIGN.md" not in file.read_text(encoding="utf-8"):
        errors.append(f"{entrypoint} missing Design stage routing")
required_design_markers = {
    "PHDK_DESIGN.md": ["25-design", "AGENT_SELECTED_AUTO_FORCE", "OWNER_APPROVED",
                       "OWNER_ACCEPTED_SPEC_ONLY", "DESIGN_AWAITING_OWNER",
                       "UI_DESIGN_SYSTEM.md", "UX_UI_DECISIONS.md", "docs/design/",
                       "PHDK_PRODUCTION_VERIFICATION.md"],
    "PHDK_LIFECYCLE.md": ["## 25", "25-design/", "DESIGN_AWAITING_OWNER"],
    "PHDK_AUTO_CONTINUITY.md": ["design_choice", "AGENT_SELECTED_AUTO_FORCE", "DESIGN_AWAITING_OWNER"],
    "scripts/phdk_auto_gate.py": ["design_choice", "AGENT_SELECTED_AUTO_FORCE", "DESIGN_AWAITING_OWNER"],
}
for filename, markers in required_design_markers.items():
    file = root / filename
    if not file.is_file():
        errors.append(f"missing Design contract file {filename}")
        continue
    body = file.read_text(encoding="utf-8")
    for marker in markers:
        if marker not in body:
            errors.append(f"{filename} missing Design marker {marker}")
ux_file = root / "PHDK_UX_UI.md"
if ux_file.is_file() and "No new independent stage is required" in ux_file.read_text(encoding="utf-8"):
    errors.append("PHDK_UX_UI.md retains obsolete no-independent-Design-stage wording")

# Acceptance routing must remain coherent in the body and in the installed
# managed block. A precedence header never suppresses a conflicting directive.
# These are source-level regression signals, not proof of authorization or UAT.
required_uat_markers = {
    "UAT_STANDARD.md": ["PHDK uat", "PHDK uat prep", "PHDK uat fix",
                        "DEFERRED — OWNER OPT-IN", "UAT NOT RUN",
                        "PHDK_PRODUCTION_VERIFICATION.md"],
    "PHDK_UAT_PREP.md": ["PHDK uat prep", "PHDK uat", "UAT_PREP_REPORT.md",
                         "PHDK_PRODUCTION_VERIFICATION.md"],
    "PHDK_AUTO.md": ["DEFERRED — OWNER OPT-IN", "UAT NOT RUN"],
    "PHDK_LIFECYCLE.md": ["45-uat-prep/", "50-uat/", "60-uat-fix/",
                          "DEFERRED — OWNER OPT-IN", "UAT NOT RUN"],
}
for filename, markers in required_uat_markers.items():
    file = root / filename
    if not file.is_file():
        errors.append(f"missing explicit-UAT contract file {filename}")
        continue
    body = file.read_text(encoding="utf-8")
    for marker in markers:
        if marker not in body:
            errors.append(f"{filename} missing explicit-UAT marker {marker}")
    if "explicit" not in body.lower():
        errors.append(f"{filename} missing explicit UAT authorization routing")

native_file = root / "PHDK_NATIVE_RULES.md"
if native_file.is_file():
    native = native_file.read_text(encoding="utf-8")
    managed = re.search(r"<!-- PHDK-MANAGED:START -->(.*?)<!-- PHDK-MANAGED:END -->",
                        native, re.S)
    if managed is None:
        errors.append("PHDK_NATIVE_RULES.md missing managed instruction block")
    else:
        for marker in ["PHDK auto", "PHDK auto force", "PHDK uat", "PHDK uat prep",
                       "PHDK uat fix", "DEFERRED — OWNER OPT-IN", "UAT NOT RUN"]:
            if marker not in managed.group(1):
                errors.append(f"PHDK_NATIVE_RULES.md managed block missing {marker}")

auto_file = root / "PHDK_AUTO.md"
if auto_file.is_file():
    auto = auto_file.read_text(encoding="utf-8")
    rows = re.findall(r"^\s*(UAT Prep|UAT Fix|UAT)\s*\.{2,}\s*(.*?)\s*$", auto, re.M)
    if {stage for stage, _ in rows} != {"UAT Prep", "UAT", "UAT Fix"}:
        errors.append("PHDK_AUTO.md missing deferred acceptance rows in lifecycle boards")
    for stage, status in rows:
        if status != "DEFERRED — OWNER OPT-IN":
            errors.append(f"PHDK_AUTO.md lifecycle board {stage} must be DEFERRED — OWNER OPT-IN")
    completion = re.search(r"^## Completion report\s*\n(.*?)(?=^## |\Z)", auto, re.M | re.S)
    if completion is None or "UAT NOT RUN" not in completion.group(1):
        errors.append("PHDK_AUTO.md completion report missing separate UAT NOT RUN outcome")

# Match known obsolete affirmative clauses, not every mention of Auto + UAT.
# Optional explicit UAT flows, prohibitions and cleanup evidence remain valid.
legacy_auto_uat_patterns = [
    re.compile(r"Under active Auto, UAT becomes part of the final integrated acceptance boundary", re.I),
    re.compile(r"Under active `PHDK auto`, this repair authority is already included", re.I),
    re.compile(r"Under active `PHDK auto`, repair in-scope UAT failures", re.I),
    re.compile(r"For explicit `PHDK uat prep` \(case-insensitive\) or Auto stage 45", re.I),
    re.compile(r"Standalone `PHDK uat prep` and Auto stage 45 follow", re.I),
    re.compile(r"At `PHDK uat prep` \(standalone or Auto stage 45\)", re.I),
    re.compile(r"\bIn Auto (?:it is stage 45|Prep follows Integration)\b", re.I),
    re.compile(r"Under Auto, `45-uat-prep/HANDOFF\.md` must exist", re.I),
    re.compile(r"Inside Auto create immutable sanitized snapshots", re.I),
    re.compile(r"do not run UAT Prep or UAT;\s*then `PHDK uat`", re.I),
    re.compile(r"Sequence: Capture → Plan → Design → PMO/workstream execution → Integration → UAT Prep", re.I),
    re.compile(r"Then: reuse/run Capture, Plan, Design, PMO/workstream execution, Integration Review, UAT Prep", re.I),
    re.compile(r"Run \*\*SEO after UAT and UAT Fix and before Check\*\* in `PHDK auto`", re.I),
]
active_policy_paths = set(root.glob("*.md"))
active_policy_paths.update(
    root / source for source in sources
    if source.endswith(".md") and not Path(source).is_absolute()
    and ".." not in Path(source).parts
)
for path in sorted(active_policy_paths):
    try:
        relative = path.relative_to(root)
        path.resolve().relative_to(root.resolve())
    except ValueError:
        errors.append(f"unsafe active policy path: {path.name}")
        continue
    if (not path.is_file() or "ORIGINALS" in relative.parts or "docs" in relative.parts
            or path.name.startswith("CHANGELOG") or path.name.endswith("_REPORT.md")
            or path.name in {"STATUS.md", "TASK.md"}):
        continue
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if any(pattern.search(line) for pattern in legacy_auto_uat_patterns):
            errors.append(f"{relative}:{lineno}: obsolete automatic UAT directive")

# Guard against reintroducing the deprecated PMO-only task-delegation prohibition.
# Scan active Markdown instructions only; archival CHANGELOG/ORIGINALS are historical.
legacy_delegation_patterns = [
    re.compile(r"delegation (?:is )?(?:allowed|permitted) only (?:under|inside|during|in) (?:explicit )?PMO", re.I),
    re.compile(r"(?:outside|unless) (?:explicit )?(?:`PHDK `)?PMO.{0,110}(?:do not |no |prohibit)(?:use |launch |create |delegate )?(?:subagents|delegat|workers|agent teams)", re.I),
    re.compile(r"PMO is the only PHDK (?:mode|context) (?:allowed|that may) to delegate", re.I),
    re.compile(r"(?:sole|only) (?:bounded |controlled )?delegation exception.*PMO", re.I),
    re.compile(r"(?:delegation outside|no delegation outside) (?:explicit )?PMO", re.I),
]
for path in root.rglob("*.md"):
    if "ORIGINALS" in path.parts or path.name.startswith("CHANGELOG") or path.name == "PHDK_COHERENCE_REPORT.md":
        continue
    body = path.read_text(encoding="utf-8")
    for lineno, line in enumerate(body.splitlines(), 1):
        if any(pattern.search(line) for pattern in legacy_delegation_patterns):
            errors.append(f"{path.relative_to(root)}:{lineno}: deprecated PMO-only delegation rule")
if not (root / "PHDK_INTELLIGENT_EXECUTION.md").is_file():
    errors.append("missing universal intelligent execution contract")

if errors:
    print("\n".join("FAIL: " + x for x in errors), file=sys.stderr)
    sys.exit(1)
print(f"PASS: v{version}, {len(sources)} manifest mappings (static only)")
