#!/usr/bin/env python3
"""Read-only policy-routing, documentation, browser and hook checks."""
import re


def run_routing_checks(errors, source_destinations, policy_path):
    # Verify the published session policy and compact routing on either manifest layout.
    for source, markers in {
        "PHDK_AUTO_CONTINUITY.md": ["SESSION_HANDOFF", "bounded work session", "status", "fresh conversation"],
        "PHDK_AUTO.md": ["bounded work session", "SESSION_HANDOFF"],
        "PHDK_NATIVE_RULES.md": ["session boundary", "fresh"],
        "PHDK_COMMUNICATION_STANDARD.md": ["session handoff", "copyable prompt"],
        "scripts/phdk_auto_gate.py": ["SESSION_HANDOFF", "session_boundary"],
    }.items():
        document = policy_path(source)
        body = document.read_text(encoding="utf-8").lower() if document.is_file() else ""
        for marker in markers:
            if marker.lower() not in body:
                errors.append(f"session handoff: {source} lacks {marker}")

    # Browser transport is not application acceptance: verify both independent paths.
    # This is a source-only regression guard, not proof of connected tools or live writes.
    browser_routes = {
        "PHDK_BROWSER_CONFIGURATION_STANDARD.md": [
            "PHDK browser on", "PHDK browser off", "PHDK browser allow",
            "PRODUCT_UAT", "EXTERNAL_CONFIG", "CONFIGURATION_VERIFIED",
        ],
        "EXECUTION_SCOPE.md": [
            "PHDK_BROWSER_CONFIGURATION_STANDARD.md",
            "PHDK browser on", "PHDK browser off", "PHDK browser allow",
            "product browser testing",
        ],
        "AGENTS.md": ["PHDK_BROWSER_CONFIGURATION_STANDARD.md", "PHDK browser on", "PHDK browser off"],
        "SKILL.md": ["PHDK_BROWSER_CONFIGURATION_STANDARD.md", "PHDK browser on", "PHDK browser off"],
        "PHDK_NATIVE_RULES.md": ["PHDK_BROWSER_CONFIGURATION_STANDARD.md", "PHDK browser on", "PHDK browser off"],
        "PHDK_AUTO.md": ["PHDK_BROWSER_CONFIGURATION_STANDARD.md", "Product browser testing"],
        "PHDK_PRODUCTION_VERIFICATION.md": ["PHDK_BROWSER_CONFIGURATION_STANDARD.md", "product browser testing"],
        "README.md": ["PHDK_BROWSER_CONFIGURATION_STANDARD.md", "PHDK browser on", "PHDK browser off"],
        "INANUTSHELL.md": ["PHDK_BROWSER_CONFIGURATION_STANDARD.md", "PHDK browser on", "PHDK browser off"],
        "PHDK_UPGRADE.md": ["PHDK_BROWSER_CONFIGURATION_STANDARD.md"],
        "UAT_BROWSER_READINESS_STANDARD.md": ["PHDK_BROWSER_CONFIGURATION_STANDARD.md"],
    }
    for filename, markers in browser_routes.items():
        file = policy_path(filename)
        if not file.is_file():
            errors.append(f"browser routing missing: {filename}")
            continue
        body = file.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in body:
                errors.append(f"browser routing: {filename} lacks {marker}")

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

    # Portfolio-first routing is a source-only consistency guard, not proof of
    # installed modules, actual tests or deployed downstream behavior.
    portfolio_routes = {
        "README.md": ["Portfolio-first", "PHDK_REUSE_CATALOG_STANDARD.md", "PHDK_PRODUCTION_VERIFICATION.md"],
        "PHDK_EVOLUTION_STANDARD.md": ["Portfolio-first", "technical_stack.md", "PHDK_REUSE_CATALOG_STANDARD.md"],
        "PHDK_REUSE_CATALOG_STANDARD.md": ["Portfolio-first", "Reuse-first portfolio default", "ACCEPTED_VERSIONED"],
        "PHDK_PLAN.md": ["Portfolio-first", "REUSE, ADAPT and BUILD", "technical_stack.md"],
        "technical_stack.md": ["Portfolio-first", "safe builds", "PHDK_PRODUCTION_VERIFICATION.md"],
        "PHDK_PRODUCTION_VERIFICATION.md": ["Portfolio-first", "not a ban on builds", "Do not launch Docker"],
        "PHDK_STARTER_PROFILE.md": ["Portfolio-first", "SPECIFICATION_ONLY"],
        "PHDK_INTELLIGENT_EXECUTION.md": ["Portfolio-first", "PHDK_REUSE_CATALOG_STANDARD.md"],
        "PHDK_CHECK.md": ["Portfolio-first", "PHDK_REUSE_CATALOG_STANDARD.md"],
        "PHDK_NATIVE_RULES.md": ["Portfolio-first", "TECHNICAL_STACK.md", "PHDK_REUSE_CATALOG_STANDARD.md"],
        "AGENTS.md": ["Portfolio-first", "PHDK_REUSE_CATALOG_STANDARD.md"],
        "SKILL.md": ["Portfolio-first", "PHDK_REUSE_CATALOG_STANDARD.md"],
        "INANUTSHELL.md": ["Portfolio-first", "TECHNICAL_STACK.md", "PHDK_REUSE_CATALOG_STANDARD.md"],
        "PHDK_COHERENCE_STANDARD.md": ["Portfolio-first", "scripts/phdk_coherence_check.py"],
    }
    for filename, markers in portfolio_routes.items():
        candidate = policy_path(filename)
        if not candidate.is_file():
            errors.append(f"portfolio policy routing missing: {filename}")
            continue
        body = candidate.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in body:
                errors.append(f"portfolio policy routing: {filename} missing {marker}")

    for obsolete in [
        "Use isolated in-process substitutes in relevant local tests.",
        "After all milestones, run final cross-milestone UAT/Check",
        "Agent orchestration remains allowed only through explicit PMO",
    ]:
        if obsolete in policy_path("INANUTSHELL.md").read_text(encoding="utf-8"):
            errors.append(f"obsolete nutshell policy: {obsolete}")

    # A policy header before YAML front matter prevents this entrypoint from
    # retaining the conventional skill metadata structure.
    skill_file = policy_path("SKILL.md")
    if skill_file.is_file() and not skill_file.read_text(encoding="utf-8").startswith(
        "---\n"
    ):
        errors.append("SKILL.md metadata must remain the first front-matter block")

    # Section guards check the active contract sections, not
    # historical mentions elsewhere. Presence does not establish owner authority,
    # resolve an executor denial, or prove that a phase transition actually ran.
    transition_reference = "MAIN_DELIVERY_STANDARD.md#phase-transition-reconciliation"
    required_policy_sections = {
        "EXECUTION_SCOPE.md": (
            "## Restriction provenance and lifetime",
            [
                "PERMANENT_POLICY",
                "PHASE_LIMIT",
                "HISTORICAL_RECORD",
            ],
        ),
        "MAIN_DELIVERY_STANDARD.md": (
            "## Phase-transition reconciliation",
            [
                "OWNER_AUTHORIZATION",
                "TECHNICAL_PERMISSION",
                "COST_AUTHORIZATION",
                "UAT_AUTHORIZATION",
                "TASK_TRACKING_STANDARD.md#restriction-record",
            ],
        ),
        "TASK_TRACKING_STANDARD.md": (
            "## Restriction record",
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
            "## Current PHDK baseline and scope",
            [
                "PHDK_PREFLIGHT.md",
                "VERSION",
                "TASK_TRACKING_STANDARD.md#restriction-record",
            ],
        ),
        "UAT_STANDARD.md": (
            "### Workflow acceptance decision",
            ["Functional result", "Workflow UX result", "FAIL", "ACCEPTANCE INCOMPLETE", "NOT APPLICABLE"],
        ),
        "PHDK_UX_UI.md": (
            "### Rendered workflow walkthrough",
            ["UAT_JOURNEY_MAP.md", "CRUD_MATRIX.md", "redacted evidence reference",
             "UAT_STANDARD.md#workflow-acceptance-decision"],
        ),
    }
    for filename, (heading, markers) in required_policy_sections.items():
        file = policy_path(filename)
        if not file.is_file():
            errors.append(f"missing policy contract file {filename}")
            continue
        level = heading.index(" ")
        section = re.search(
            rf"^{re.escape(heading)}[ \t]*\n(.*?)(?=^#{{1,{level}}}\s|\Z)",
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

    return transition_reference, native_hook_reference, has_hook_trigger
