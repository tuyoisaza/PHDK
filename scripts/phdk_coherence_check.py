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
source_destinations = {}
# The canonical checkout uses manifest source paths. The documented installed
# layout uses destination paths, including uppercase aliases such as
# TECHNICAL_STACK.md; do not report those valid mappings as missing sources.
vendored_layout = root.name == "phdk-standards"
for n, raw in enumerate(
    (root / "PHDK_MANIFEST.txt").read_text(encoding="utf-8").splitlines(), 1
):
    line = raw.strip()
    if not line or line.startswith("#"):
        continue
    p = [x.strip() for x in line.split("|")]
    if len(p) != 2 or not all(p):
        errors.append(f"manifest line {n}: malformed")
        continue
    src, dst = p
    safe = True
    for path in p:
        if (
            Path(path).is_absolute()
            or ".." in Path(path).parts
            or "\\" in path
            or "\x00" in path
            or path == "."
        ):
            errors.append(f"manifest line {n}: unsafe path")
            safe = False
    if not safe:
        continue
    if src in sources or dst in destinations:
        errors.append(f"manifest line {n}: duplicate")
    sources.add(src)
    destinations.add(dst)
    source_destinations[src] = dst
    expected = dst if vendored_layout else src
    candidate = root / expected
    if not candidate.resolve().is_relative_to(root.resolve()):
        errors.append(f"manifest line {n}: path escapes standards root")
    elif not candidate.is_file():
        errors.append(f"manifest line {n}: missing {expected}")


def policy_path(source):
    """Resolve a known canonical policy name in either supported layout."""
    return root / (
        source_destinations.get(source, source) if vendored_layout else source
    )


for mandatory in [
    "VERSION",
    "README.md",
    "CHANGELOG.md",
    "AGENTS.md",
    "PHDK_PREFLIGHT.md",
    "PHDK_COHERENCE_STANDARD.md",
    "PHDK_EVOLUTION_STANDARD.md",
    "CHANGE_MANAGEMENT.md",
    "scripts/phdk_coherence_check.py",
    "PHDK_AUTO_CONTINUITY.md",
    "scripts/phdk_auto_gate.py",
    "PHDK_DESIGN.md",
    "SKILL.md",
    "PHDK_NATIVE_RULES.md",
    "UAT_STANDARD.md",
    "PHDK_UAT_PREP.md",
    "EXECUTION_SCOPE.md",
    "MAIN_DELIVERY_STANDARD.md",
    "TASK_TRACKING_STANDARD.md",
    "PHDK_PLAN.md",
    "PHDK_REUSE_CATALOG_STANDARD.md",
    "PHDK_STARTER_PROFILE.md",
    "PHDK_DEPLOYMENT_VERSION_STANDARD.md",
    "PHDK_DOCUMENTATION_STANDARD.md",
    "scripts/phdk_docs_audit.py",
    "PHDK_REUSE_CATALOG.json",
    "schemas/phdk-reuse-catalog.schema.json",
    "scripts/phdk_reuse_catalog_check.py",
]:
    if mandatory not in sources:
        errors.append(f"manifest lacks {mandatory}")
for entrypoint in [
    "README.md",
    "AGENTS.md",
    "PHDK_NATIVE_RULES.md",
    "CHANGE_MANAGEMENT.md",
    "SKILL.md",
]:
    file = policy_path(entrypoint)
    if not file.is_file() or "PHDK_EVOLUTION_STANDARD.md" not in file.read_text(
        encoding="utf-8"
    ):
        errors.append(f"{entrypoint} missing PHDK evolution standard reference")

# Deployment-revision contract and its narrow non-UAT permission routing.
# This source-only guard checks document coherence, not implementation or a live
# HTTP response; users still need an authorized production readback.
deployment_version_sources = {
    "PHDK_DEPLOYMENT_VERSION_STANDARD.md": [
        "GET /health/version",
        "Cache-Control: no-store",
        "commitSha",
        "phdkVersion",
        "STALE_OR_DIFFERENT_REVISION",
    ],
    "EXECUTION_SCOPE.md": [
        "PHDK_DEPLOYMENT_VERSION_STANDARD.md",
        "GET /health/version",
    ],
    "PHDK_PRODUCTION_VERIFICATION.md": [
        "PHDK_DEPLOYMENT_VERSION_STANDARD.md",
        "GET /health/version",
    ],
    "MAIN_DELIVERY_STANDARD.md": [
        "PHDK_DEPLOYMENT_VERSION_STANDARD.md",
        "GET /health/version",
    ],
    "VERSIONING.md": [
        "PHDK_DEPLOYMENT_VERSION_STANDARD.md",
        "GET /health/version",
    ],
    "PHDK_AUTO.md": [
        "PHDK_DEPLOYMENT_VERSION_STANDARD.md",
        "GET /health/version",
    ],
    "PHDK_CHECK.md": [
        "PHDK_DEPLOYMENT_VERSION_STANDARD.md",
        "GET /health/version",
    ],
    "DEBUG_DIAGNOSTICS_STANDARD.md": [
        "PHDK_DEPLOYMENT_VERSION_STANDARD.md",
        "GET /health/version",
    ],
    "AGENTS.md": ["PHDK_DEPLOYMENT_VERSION_STANDARD.md", "GET /health/version"],
    "SKILL.md": ["PHDK_DEPLOYMENT_VERSION_STANDARD.md", "GET /health/version"],
    "PHDK_NATIVE_RULES.md": [
        "PHDK_DEPLOYMENT_VERSION_STANDARD.md",
        "GET /health/version",
    ],
}
for filename, required_markers in deployment_version_sources.items():
    candidate = policy_path(filename)
    if not candidate.is_file():
        errors.append(f"deployment-version contract missing: {filename}")
        continue
    body = candidate.read_text(encoding="utf-8")
    for marker in required_markers:
        if marker not in body:
            errors.append(f"deployment-version routing: {filename} lacks {marker}")


# Versioned project-documentation routing is a source-only consistency gate.
# It does not audit or mutate any downstream product, create docs/INDEX.md,
# approve a document, run local behavioral tests or activate UAT.
document_routes = {
    "PHDK_DOCUMENTATION_STANDARD.md": [
        "docs/INDEX.md", "docs/intents/", "docs/briefs/", "docs/decisions/",
        "docs/plans/", "docs/images/", "docs/evidence/", "kebab-case.vN.md",
        "TASK.md", "LEGACY_COMPATIBLE", "--sync-index",
    ],
    "PHDK_CAPTURE.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/INDEX.md"],
    "INTENT_CAPTURE_STANDARD.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/intents/"],
    "PHDK_PLAN.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/plans/"],
    "PHDK_DESIGN.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/images/"],
    "PHDK_DESIGNER_MODE.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/images/"],
    "PHDK_LIFECYCLE.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/INDEX.md"],
    "TASK_TRACKING_STANDARD.md": ["PHDK_DOCUMENTATION_STANDARD.md", "TASK.md"],
    "PHDK_PMO.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/INDEX.md"],
    "PHDK_PROJECT_MANAGEMENT_STANDARD.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/INDEX.md"],
    "PHDK_AUTO.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/INDEX.md", "--sync-index"],
    "PHDK_AUTO_CONTINUITY.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/INDEX.md"],
    "PHDK_CHECK.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/INDEX.md", "--check", "--sync-index"],
    "MAIN_DELIVERY_STANDARD.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/INDEX.md"],
    "PHDK_COMPLETION_GATE.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/INDEX.md"],
    "PHDK_UPGRADE.md": ["PHDK_DOCUMENTATION_STANDARD.md", "scripts/phdk_docs_audit.py"],
    "PHDK_EVOLUTION_STANDARD.md": ["PHDK_DOCUMENTATION_STANDARD.md", "scripts/phdk_docs_audit.py"],
    "UAT_STANDARD.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/INDEX.md"],
    "PHDK_INTELLIGENT_EXECUTION.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/INDEX.md"],
    "AGENTS.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/INDEX.md"],
    "SKILL.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/INDEX.md"],
    "PHDK_NATIVE_RULES.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/INDEX.md"],
    "README.md": ["PHDK_DOCUMENTATION_STANDARD.md", "docs/INDEX.md"],
}
for filename, markers in document_routes.items():
    file = policy_path(filename)
    if not file.is_file():
        errors.append(f"missing documentation routing file {filename}")
        continue
    body = file.read_text(encoding="utf-8")
    for marker in markers:
        if marker not in body:
            errors.append(f"documentation routing: {filename} missing {marker}")

# A policy header before YAML front matter prevents this entrypoint from
# retaining the conventional skill metadata structure.
skill_file = policy_path("SKILL.md")
if skill_file.is_file() and not skill_file.read_text(encoding="utf-8").startswith(
    "---\n"
):
    errors.append("SKILL.md metadata must remain the first front-matter block")

# Restriction and transition guards check the active contract sections, not
# historical mentions elsewhere. Presence does not establish owner authority,
# resolve an executor denial, or prove that a phase transition actually ran.
transition_reference = "MAIN_DELIVERY_STANDARD.md#phase-transition-reconciliation"
required_transition_sections = {
    "EXECUTION_SCOPE.md": (
        "Restriction provenance and lifetime",
        [
            "PERMANENT_POLICY",
            "PHASE_LIMIT",
            "HISTORICAL_RECORD",
        ],
    ),
    "MAIN_DELIVERY_STANDARD.md": (
        "Phase-transition reconciliation",
        [
            "OWNER_AUTHORIZATION",
            "TECHNICAL_PERMISSION",
            "COST_AUTHORIZATION",
            "UAT_AUTHORIZATION",
            "TASK_TRACKING_STANDARD.md#restriction-record",
        ],
    ),
    "TASK_TRACKING_STANDARD.md": (
        "Restriction record",
        [
            "PERMANENT_POLICY",
            "PHASE_LIMIT",
            "HISTORICAL_RECORD",
            "HOST_OR_EXTERNAL",
            "UNKNOWN",
            "source_ref",
            "issued_at",
            "recorded_at",
            "scope",
            "closure_condition",
            "status",
            "superseded_by",
        ],
    ),
    "PHDK_PLAN.md": (
        "Current PHDK baseline and scope",
        [
            "PHDK_PREFLIGHT.md",
            "VERSION",
            "TASK_TRACKING_STANDARD.md#restriction-record",
        ],
    ),
}
for filename, (heading, markers) in required_transition_sections.items():
    file = policy_path(filename)
    if not file.is_file():
        errors.append(f"missing phase-transition contract file {filename}")
        continue
    section = re.search(
        r"^## " + re.escape(heading) + r"\s*\n(.*?)(?=^#{1,2}\s|\Z)",
        file.read_text(encoding="utf-8"),
        re.M | re.S,
    )
    if section is None:
        errors.append(f"{filename} missing section {heading}")
        continue
    for marker in markers:
        if marker not in section.group(1):
            errors.append(f"{filename} section {heading} missing {marker}")
for entrypoint in ["README.md", "AGENTS.md", "SKILL.md", "PHDK_AUTO_CONTINUITY.md"]:
    file = policy_path(entrypoint)
    if not file.is_file() or transition_reference not in file.read_text(
        encoding="utf-8"
    ):
        errors.append(f"{entrypoint} missing phase-transition routing")

# Hook guards verify routing and documented coverage, never actual agent behavior.
hook_reference = "PHDK_HOOK_COMPATIBILITY.md#decision-procedure"
native_hook_reference = "phdk-standards/" + hook_reference


def has_hook_trigger(body):
    # Wrapped prose stays together; separate bullets cannot supply trigger terms.
    for paragraph in re.split(r"\n[ \t]*\n|\n(?=[ \t]*[-+*][ \t]+)", body):
        if hook_reference in paragraph and all(
            re.search(pattern, paragraph, re.I)
            for pattern in [
                r"\b(?:build|packaging|hook)\b",
                r"\bload\b",
                r"\bbefore\b",
                r"\bexecut\w*\b",
                r"\bBLOCKED\b",
                r"\b(?:ask\w*|request\w*)\b",
            ]
        ):
            return True
    return False


for dependency in ["PHDK_HOOK_COMPATIBILITY.md", "PHDK_PRODUCTION_VERIFICATION.md"]:
    if source_destinations.get(dependency) != dependency:
        errors.append(f"manifest must vendor hook dependency at {dependency}")
for entrypoint in ["AGENTS.md", "SKILL.md", "PHDK_AUTO.md", "PHDK_AUTO_CONTINUITY.md"]:
    file = policy_path(entrypoint)
    if not file.is_file() or not has_hook_trigger(file.read_text(encoding="utf-8")):
        errors.append(
            f"{entrypoint} missing hook decision trigger before execution/block/question"
        )
hook_file = policy_path("PHDK_HOOK_COMPATIBILITY.md")
hook_body = hook_file.read_text(encoding="utf-8") if hook_file.is_file() else ""
for heading in ["Decision procedure", "Required decision scenarios"]:
    section = re.search(
        r"^## " + re.escape(heading) + r"\s*\n(.*?)(?=^#{1,2}\s|\Z)",
        hook_body,
        re.M | re.S,
    )
    if section is None:
        errors.append(f"PHDK_HOOK_COMPATIBILITY.md missing section {heading}")
    elif heading == "Decision procedure":
        for marker in ["import", "require", "runtime", "provenance"]:
            if marker not in section.group(1).lower():
                errors.append(
                    f"hook decision procedure missing classification marker {marker}"
                )
    else:
        rows = re.findall(
            r"^\|\s*`?(HC-[A-Z]+)`?\s*\|\s*([^\n]+)", section.group(1), re.M
        )
        for scenario in "HC-STATIC HC-LOAD HC-PHDK HC-OWNER HC-UNKNOWN HC-ORDER".split():
            matches = [cells for key, cells in rows if key == scenario]
            cells = (
                matches[0].strip().removesuffix("|").split("|")
                if len(matches) == 1
                else []
            )
            if len(cells) != 2 or not all(cell.strip() for cell in cells):
                errors.append(
                    f"hook decision scenarios missing complete unique row {scenario}"
                )

# Stack review routing is an instruction contract, not an advisory scanner.
# These guards never establish security clearance or deployed-version evidence.
stack_reference = "PHDK_SECURE.md#stack-security-review"
stack_outcomes = ["STANDARDS_SYNC", "STACK_REVIEW_COVERAGE", "STACK_SECURITY_STATUS"]
for mandatory in [
    "PHDK_SECURE.md",
    "PHDK_UPGRADE.md",
    "PHDK_CHECK.md",
    "PHDK_CENTRAL_UPDATE.md",
    "technical_stack.md",
    "scripts/phdk_update.py",
]:
    if mandatory not in sources:
        errors.append(f"manifest lacks stack review dependency {mandatory}")
for entrypoint in [
    "PHDK_UPGRADE.md",
    "PHDK_PREFLIGHT.md",
    "PHDK_PLAN.md",
    "PHDK_CHECK.md",
    "PHDK_CENTRAL_UPDATE.md",
    "README.md",
    "AGENTS.md",
    "SKILL.md",
    "PHDK_NATIVE_RULES.md",
    "EXECUTION_SCOPE.md",
    "MAIN_DELIVERY_STANDARD.md",
    "PHDK_AUTO.md",
]:
    file = policy_path(entrypoint)
    if not file.is_file() or stack_reference not in file.read_text(encoding="utf-8"):
        errors.append(f"{entrypoint} missing Stack Security Review routing")

secure_file = policy_path("PHDK_SECURE.md")
if secure_file.is_file():
    secure = secure_file.read_text(encoding="utf-8")
    stack = re.search(
        r"^## Stack Security Review\s*\n(.*?)(?=^#{1,2}\s|\Z)", secure, re.M | re.S
    )
    if stack is None:
        errors.append("PHDK_SECURE.md missing canonical Stack Security Review section")
    else:
        for marker in stack_outcomes + [
            "PHDK upgrade",
            "PHDK upgrade force",
            "UNVERIFIED",
        ]:
            if marker not in stack.group(1):
                errors.append(f"Stack Security Review missing contract marker {marker}")
        for term in ["declared", "resolved", "build", "deployed", "official"]:
            if not re.search(r"\b" + term + r"\b", stack.group(1), re.I):
                errors.append(
                    f"Stack Security Review missing {term} evidence distinction"
                )
    for marker in ["Active LTS", "Maintenance LTS"]:
        if marker not in secure:
            errors.append(
                f"PHDK_SECURE.md missing supported runtime selection {marker}"
            )

upgrade_file = policy_path("PHDK_UPGRADE.md")
if upgrade_file.is_file():
    upgrade = upgrade_file.read_text(encoding="utf-8")
    for marker in stack_outcomes:
        if marker not in upgrade:
            errors.append(f"PHDK_UPGRADE.md missing independent outcome {marker}")
    if not re.search(r"\b(?:no-op|already current|versions? match)\b", upgrade, re.I):
        errors.append("PHDK_UPGRADE.md missing explicit no-op review trigger")

# Design routing guards are source-level signals, never evidence of an owner
# decision, rendered preview, actual execution, or downstream adoption.
for entrypoint in [
    "README.md",
    "AGENTS.md",
    "PHDK_NATIVE_RULES.md",
    "SKILL.md",
    "PHDK_PLAN.md",
    "PHDK_LIFECYCLE.md",
    "PHDK_AUTO.md",
    "PHDK_AUTO_CONTINUITY.md",
    "PHDK_UX_UI.md",
]:
    file = policy_path(entrypoint)
    if not file.is_file() or "PHDK_DESIGN.md" not in file.read_text(encoding="utf-8"):
        errors.append(f"{entrypoint} missing Design stage routing")
required_design_markers = {
    "PHDK_DESIGN.md": [
        "25-design",
        "AGENT_SELECTED_AUTO_FORCE",
        "OWNER_APPROVED",
        "OWNER_ACCEPTED_SPEC_ONLY",
        "DESIGN_AWAITING_OWNER",
        "UI_DESIGN_SYSTEM.md",
        "UX_UI_DECISIONS.md",
        "docs/design/",
        "PHDK_PRODUCTION_VERIFICATION.md",
    ],
    "PHDK_LIFECYCLE.md": ["## 25", "25-design/", "DESIGN_AWAITING_OWNER"],
    "PHDK_AUTO_CONTINUITY.md": [
        "design_choice",
        "AGENT_SELECTED_AUTO_FORCE",
        "DESIGN_AWAITING_OWNER",
    ],
    "scripts/phdk_auto_gate.py": [
        "design_choice",
        "AGENT_SELECTED_AUTO_FORCE",
        "DESIGN_AWAITING_OWNER",
    ],
}
for filename, markers in required_design_markers.items():
    file = policy_path(filename)
    if not file.is_file():
        errors.append(f"missing Design contract file {filename}")
        continue
    body = file.read_text(encoding="utf-8")
    for marker in markers:
        if marker not in body:
            errors.append(f"{filename} missing Design marker {marker}")
ux_file = policy_path("PHDK_UX_UI.md")
if ux_file.is_file() and "No new independent stage is required" in ux_file.read_text(
    encoding="utf-8"
):
    errors.append("PHDK_UX_UI.md retains obsolete no-independent-Design-stage wording")

# Reuse/catalog routing is source-level contract verification, not package acceptance.
reuse_reference = "PHDK_REUSE_CATALOG_STANDARD.md"
for entrypoint in ["README.md", "AGENTS.md", "PHDK_NATIVE_RULES.md", "SKILL.md", "PHDK_PLAN.md"]:
    file = policy_path(entrypoint)
    if not file.is_file() or reuse_reference not in file.read_text(encoding="utf-8"):
        errors.append(f"{entrypoint} missing reusable-capability catalog routing")

required_reuse_markers = {
    "PHDK_REUSE_CATALOG_STANDARD.md": [
        "REUSE",
        "ADAPT",
        "BUILD",
        "SPECIFICATION_ONLY",
        "ACCEPTED_VERSIONED",
        "second independent consumer",
        "tests_present",
        "test_status",
    ],
    "PHDK_STARTER_PROFILE.md": [
        "Composition target only",
        "super_admin",
        "Synthetic identities",
        "AI prompt administration",
        "Theme system",
        "Internationalization",
    ],
    "PHDK_PROJECT_MANAGEMENT_STANDARD.md": [
        "user capability",
        "user journey",
        "IMPLEMENTED",
        "PUBLISHED",
        "DEPLOYED",
        "ACCEPTED",
    ],
    "AGILE_SLICE_WORKFLOW.md": [
        "A slice is not a milestone",
        "milestone publication boundary",
    ],
}
for filename, markers in required_reuse_markers.items():
    file = policy_path(filename)
    if not file.is_file():
        errors.append(f"missing reuse/milestone contract file {filename}")
        continue
    body = file.read_text(encoding="utf-8")
    for marker in markers:
        if marker not in body:
            errors.append(f"{filename} missing reuse/milestone marker {marker}")

# Acceptance routing must remain coherent in the body and in the installed
# managed block. A precedence header never suppresses a conflicting directive.
# These are source-level regression signals, not proof of authorization or UAT.
required_uat_markers = {
    "UAT_STANDARD.md": [
        "PHDK uat",
        "PHDK uat prep",
        "PHDK uat fix",
        "DEFERRED — OWNER OPT-IN",
        "UAT NOT RUN",
        "PHDK_PRODUCTION_VERIFICATION.md",
    ],
    "PHDK_UAT_PREP.md": [
        "PHDK uat prep",
        "PHDK uat",
        "UAT_PREP_REPORT.md",
        "PHDK_PRODUCTION_VERIFICATION.md",
    ],
    "PHDK_AUTO.md": ["DEFERRED — OWNER OPT-IN", "UAT NOT RUN"],
    "PHDK_LIFECYCLE.md": [
        "45-uat-prep/",
        "50-uat/",
        "60-uat-fix/",
        "DEFERRED — OWNER OPT-IN",
        "UAT NOT RUN",
    ],
}
for filename, markers in required_uat_markers.items():
    file = policy_path(filename)
    if not file.is_file():
        errors.append(f"missing explicit-UAT contract file {filename}")
        continue
    body = file.read_text(encoding="utf-8")
    for marker in markers:
        if marker not in body:
            errors.append(f"{filename} missing explicit-UAT marker {marker}")
    if "explicit" not in body.lower():
        errors.append(f"{filename} missing explicit UAT authorization routing")

native_file = policy_path("PHDK_NATIVE_RULES.md")
if native_file.is_file():
    native = native_file.read_text(encoding="utf-8")
    managed = re.search(
        r"<!-- PHDK-MANAGED:START -->(.*?)<!-- PHDK-MANAGED:END -->", native, re.S
    )
    if managed is None:
        errors.append("PHDK_NATIVE_RULES.md missing managed instruction block")
    else:
        for marker in [
            "PHDK auto",
            "PHDK auto force",
            "PHDK uat",
            "PHDK uat prep",
            "PHDK uat fix",
            "DEFERRED — OWNER OPT-IN",
            "UAT NOT RUN",
            transition_reference,
            stack_reference,
            native_hook_reference,
        ]:
            if marker not in managed.group(1):
                errors.append(f"PHDK_NATIVE_RULES.md managed block missing {marker}")
        if not has_hook_trigger(managed.group(1)):
            errors.append(
                "PHDK_NATIVE_RULES.md managed block missing hook decision trigger"
            )

auto_file = policy_path("PHDK_AUTO.md")
if auto_file.is_file():
    auto = auto_file.read_text(encoding="utf-8")
    rows = re.findall(r"^\s*(UAT Prep|UAT Fix|UAT)\s*\.{2,}\s*(.*?)\s*$", auto, re.M)
    if {stage for stage, _ in rows} != {"UAT Prep", "UAT", "UAT Fix"}:
        errors.append(
            "PHDK_AUTO.md missing deferred acceptance rows in lifecycle boards"
        )
    for stage, status in rows:
        if status != "DEFERRED — OWNER OPT-IN":
            errors.append(
                f"PHDK_AUTO.md lifecycle board {stage} must be DEFERRED — OWNER OPT-IN"
            )
    completion = re.search(
        r"^## Completion report\s*\n(.*?)(?=^## |\Z)", auto, re.M | re.S
    )
    if completion is None or "UAT NOT RUN" not in completion.group(1):
        errors.append(
            "PHDK_AUTO.md completion report missing separate UAT NOT RUN outcome"
        )

# Match known obsolete affirmative clauses, not every mention of Auto + UAT.
# Optional explicit UAT flows, prohibitions and cleanup evidence remain valid.
legacy_auto_uat_patterns = [
    re.compile(
        r"Under active Auto, UAT becomes part of the final integrated acceptance boundary",
        re.I,
    ),
    re.compile(
        r"Under active `PHDK auto`, this repair authority is already included", re.I
    ),
    re.compile(r"Under active `PHDK auto`, repair in-scope UAT failures", re.I),
    re.compile(
        r"For explicit `PHDK uat prep` \(case-insensitive\) or Auto stage 45", re.I
    ),
    re.compile(r"Standalone `PHDK uat prep` and Auto stage 45 follow", re.I),
    re.compile(r"At `PHDK uat prep` \(standalone or Auto stage 45\)", re.I),
    re.compile(r"\bIn Auto (?:it is stage 45|Prep follows Integration)\b", re.I),
    re.compile(r"Under Auto, `45-uat-prep/HANDOFF\.md` must exist", re.I),
    re.compile(r"Inside Auto create immutable sanitized snapshots", re.I),
    re.compile(r"do not run UAT Prep or UAT;\s*then `PHDK uat`", re.I),
    re.compile(
        r"Sequence: Capture → Plan → Design → PMO/workstream execution → Integration → UAT Prep",
        re.I,
    ),
    re.compile(
        r"Then: reuse/run Capture, Plan, Design, PMO/workstream execution, Integration Review, UAT Prep",
        re.I,
    ),
    re.compile(
        r"Run \*\*SEO after UAT and UAT Fix and before Check\*\* in `PHDK auto`", re.I
    ),
]
legacy_stack_patterns = [
    re.compile(r"\bNode minimum:\s*(?:18|20)\.x\b", re.I),
    re.compile(r"\b(?:retains|keeps) its synchronization-only contract\b", re.I),
    re.compile(r"\ba bare sync does not start that investigation\b", re.I),
    re.compile(r"\ba bare `PHDK upgrade` still authorizes only its sync\b", re.I),
    re.compile(r"including `pnpm test` when required", re.I),
]
# Match known affirmative local-test clauses, not prohibitions or scenarios.
legacy_local_runtime_patterns = [
    re.compile(pattern, re.I)
    for pattern in [
        "Auto and FORCE already authorize synchronous isolated suites",
        "→ local unit/in-process integration tests when risk requires them",
        "Run risk-triggered unit or in-process integration tests with test doubles",
        (
            "Verification uses repository review, static checks, local builds, and "
            "risk-triggered unit or in-process integration tests"
        ),
        "Run the smallest useful local tests",
        "targeted local unit/in-process integration test when risk requires it",
    ]
]
active_policy_paths = set(root.glob("*.md"))
active_policy_paths.update(
    policy_path(source)
    for source in sources
    if source.endswith(".md")
    and not Path(source).is_absolute()
    and ".." not in Path(source).parts
)
for path in sorted(active_policy_paths):
    try:
        relative = path.relative_to(root)
        path.resolve().relative_to(root.resolve())
    except ValueError:
        errors.append(f"unsafe active policy path: {path.name}")
        continue
    if (
        not path.is_file()
        or "ORIGINALS" in relative.parts
        or "docs" in relative.parts
        or path.name.startswith("CHANGELOG")
        or path.name.endswith("_REPORT.md")
        or path.name in {"STATUS.md", "TASK.md"}
    ):
        continue
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if any(pattern.search(line) for pattern in legacy_auto_uat_patterns):
            errors.append(f"{relative}:{lineno}: obsolete automatic UAT directive")
        if any(pattern.search(line) for pattern in legacy_local_runtime_patterns):
            errors.append(f"{relative}:{lineno}: obsolete local-runtime directive")
        if any(pattern.search(line) for pattern in legacy_stack_patterns):
            errors.append(
                f"{relative}:{lineno}: obsolete stack review or verification directive"
            )

# Guard against reintroducing the deprecated PMO-only task-delegation prohibition.
# Scan active Markdown instructions only; archival CHANGELOG/ORIGINALS are historical.
legacy_delegation_patterns = [
    re.compile(
        r"delegation (?:is )?(?:allowed|permitted) only (?:under|inside|during|in) (?:explicit )?PMO",
        re.I,
    ),
    re.compile(
        r"(?:outside|unless) (?:explicit )?(?:`PHDK `)?PMO.{0,110}(?:do not |no |prohibit)(?:use |launch |create |delegate )?(?:subagents|delegat|workers|agent teams)",
        re.I,
    ),
    re.compile(
        r"PMO is the only PHDK (?:mode|context) (?:allowed|that may) to delegate", re.I
    ),
    re.compile(
        r"(?:sole|only) (?:bounded |controlled )?delegation exception.*PMO", re.I
    ),
    re.compile(r"(?:delegation outside|no delegation outside) (?:explicit )?PMO", re.I),
]
for path in root.rglob("*.md"):
    if (
        "ORIGINALS" in path.parts
        or path.name.startswith("CHANGELOG")
        or path.name == "PHDK_COHERENCE_REPORT.md"
    ):
        continue
    body = path.read_text(encoding="utf-8")
    for lineno, line in enumerate(body.splitlines(), 1):
        if any(pattern.search(line) for pattern in legacy_delegation_patterns):
            errors.append(
                f"{path.relative_to(root)}:{lineno}: deprecated PMO-only delegation rule"
            )
if not policy_path("PHDK_INTELLIGENT_EXECUTION.md").is_file():
    errors.append("missing universal intelligent execution contract")

if errors:
    print("\n".join("FAIL: " + x for x in errors), file=sys.stderr)
    sys.exit(1)
print(f"PASS: v{version}, {len(sources)} manifest mappings (static only)")
