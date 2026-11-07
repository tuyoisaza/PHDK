#!/usr/bin/env python3
"""Static consistency checks; no claim of runtime or semantic correctness."""

from pathlib import Path
import json
import re
import sys

from phdk_coherence_routing import run_routing_checks
from phdk_coherence_quality import run_quality_checks

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
    "PHDK_HELP.md",
    "PHDK_COMMANDS.json",
    "scripts/phdk_help.py",
    "PHDK_COHERENCE_STANDARD.md",
    "PHDK_EVOLUTION_STANDARD.md",
    "CHANGE_MANAGEMENT.md",
    "scripts/phdk_coherence_check.py",
    "PHDK_AUTO_CONTINUITY.md",
    "scripts/phdk_auto_gate.py",
    "scripts/phdk_session_status.py",
    "examples/session-status.example.json",
    "docs/images/session-status/v1/session-status.example.svg",
    "PHDK_DESIGN.md",
    "SKILL.md",
    "PHDK_NATIVE_RULES.md",
    "UAT_SYNTHETIC_IDENTITY_STANDARD.md",
    "COMPANY_CO_UAT_IDENTITIES.json",
    "scripts/phdk_uat_identity_plan.py",
    "scripts/phdk_uat_mfa_decision.py",
    "TABULAR_DATA_EXCHANGE_STANDARD.md",
    "scripts/phdk_uat_import_fixture.py",
    "examples/uat-data-exchange/README.md",
    "examples/uat-data-exchange/template.csv",
    "examples/uat-data-exchange/recipe.json",
    "UAT_DEFECT_WORKFLOW.md",
    "scripts/phdk_uat_defect_register.py",
    "examples/uat-defect-workflow/initial.md",
    "examples/uat-defect-workflow/retest.md",
    "UAT_STANDARD.md",
    "UAT_JOURNEY_STANDARD.md",
    "PHDK_UX_UI.md",
    "PHDK_UAT_PREP.md",
    "EXECUTION_SCOPE.md",
    "MAIN_DELIVERY_STANDARD.md",
    "TASK_TRACKING_STANDARD.md",
    "PHDK_PLAN.md",
    "PHDK_REUSE_CATALOG_STANDARD.md",
    "PHDK_STARTER_PROFILE.md",
    "PHDK_DEPLOYMENT_VERSION_STANDARD.md",
    "PHDK_DOCUMENTATION_STANDARD.md",
    "PHDK_BROWSER_CONFIGURATION_STANDARD.md",
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

# Help/catalog routing is source-only evidence, not proof of assistant behavior.
try:
    catalog = json.loads(policy_path("PHDK_COMMANDS.json").read_text(encoding="utf-8"))
    if catalog.get("schema_version") != 1 or not isinstance(catalog.get("commands"), list):
        errors.append("help catalog: unsupported format")
    else:
        names = set()
        for item in catalog["commands"]:
            canonical = item["command"]
            if not canonical.casefold().startswith("phdk "):
                errors.append(f"help catalog: invalid command {canonical}")
            for name in [canonical, *item.get("aliases", [])]:
                normalized = " ".join(name.casefold().split())
                if normalized in names:
                    errors.append(f"help catalog: duplicated alias/command {name}")
                names.add(normalized)
            reference = item["standard"]
            if (
                Path(reference).is_absolute()
                or ".." in Path(reference).parts
                or not policy_path(reference).is_file()
            ):
                errors.append(f"help catalog: invalid standard {reference}")
        for required in (
            "phdk help", "phdk capture", "phdk plan", "phdk design", "phdk auto",
            "phdk auto force", "phdk check", "phdk uat", "phdk upgrade",
            "phdk upgrade force", "phdk export modules",
        ):
            if required not in names:
                errors.append(f"help catalog: missing {required}")
except (OSError, ValueError, KeyError, TypeError) as exc:
    errors.append(f"help catalog: invalid/unreadable ({exc})")
for source in (
    "README.md", "AGENTS.md", "SKILL.md", "PHDK_NATIVE_RULES.md",
    "PHDK_PREFLIGHT.md", "ONBOARDING_AI_DEVELOPER.md", "INANUTSHELL.md",
):
    file = policy_path(source)
    if not file.is_file() or "PHDK help" not in file.read_text(encoding="utf-8"):
        errors.append(f"help routing: no PHDK help entry in {source}")

# PHDK must obey its own 600-line rule in canonical and installed layouts.
PYTHON_LINE_LIMIT = 600
for source in sorted(sources):
    if not source.endswith(".py"):
        continue
    file = policy_path(source)
    if file.is_file():
        nlines = len(file.read_text(encoding="utf-8").splitlines())
        if nlines > PYTHON_LINE_LIMIT:
            errors.append(f"vendored Python exceeds 600 lines: {source} ({nlines})")
if not vendored_layout:
    for file in sorted((root / "tests").glob("*.py")):
        if file.is_file() and not file.is_symlink():
            nlines = len(file.read_text(encoding="utf-8").splitlines())
            if nlines > PYTHON_LINE_LIMIT:
                errors.append(f"canonical Python test exceeds 600 lines: {file.name} ({nlines})")

transition_reference, native_hook_reference, has_hook_trigger = run_routing_checks(
    errors, source_destinations, policy_path
)
run_quality_checks(
    root, errors, sources, policy_path,
    transition_reference, native_hook_reference, has_hook_trigger,
)

if errors:
    print("\n".join("FAIL: " + x for x in errors), file=sys.stderr)
    sys.exit(1)
print(f"PASS: v{version}, {len(sources)} manifest mappings (static only)")
