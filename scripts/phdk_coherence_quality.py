#!/usr/bin/env python3
"""Read-only security, design, acceptance and obsolete-instruction checks."""
from pathlib import Path
import re


def run_quality_checks(root, errors, sources, policy_path,
                       transition_reference, native_hook_reference,
                       has_hook_trigger):
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
    # Source-only review: combined design decision board and independent motion contract.
    for entrypoint in [
        "PHDK_DESIGN.md", "PHDK_DESIGN_SYSTEM.md", "PHDK_UX_UI.md",
        "PHDK_AUTO.md", "PHDK_AUTO_CONTINUITY.md", "PHDK_PLAN.md",
        "PHDK_LIFECYCLE.md", "PHDK_CHECK.md", "UAT_STANDARD.md",
        "SKILL.md", "AGENTS.md", "PHDK_NATIVE_RULES.md",
    ]:
        document = policy_path(entrypoint)
        if not document.is_file():
            errors.append(f"missing bundled Design entrypoint {entrypoint}")
            continue
        if "one unresolved visual question at a time" in document.read_text(encoding="utf-8"):
            errors.append(f"{entrypoint} retains serial Design interview")
    for filename, fragments in {
        "PHDK_DESIGN.md": ["coded", "recommended", "approve all", "decision map:", "motion choice:", "composite preview:"],
        "PHDK_DESIGN_SYSTEM.md": ["motion interaction contract", "menu-switch", "expand-collapse", "prefers-reduced-motion", "AnimatePresence"],
        "PHDK_CHECK.md": ["motion interaction contract", "reduced-motion"],
        "UAT_STANDARD.md": ["motion interaction contract", "reduced-motion"],
    }.items():
        doc = policy_path(filename)
        if not doc.is_file():
            errors.append(f"missing design/motion contract {filename}")
            continue
        content = doc.read_text(encoding="utf-8").lower()
        for fragment in fragments:
            if fragment.lower() not in content:
                errors.append(f"{filename} missing bundled Design/motion marker {fragment}")
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
        "UAT_DEFECT_WORKFLOW.md": [
            "UAT_REPORT.md", "VERIFIED_RESOLVED", "phdk_uat_defect_register.py",
            "UAT_RETEST_REPORT.md", "PHDK_INTELLIGENT_EXECUTION.md",
        ],
        "UAT_SYNTHETIC_IDENTITY_STANDARD.md": [
            "COMPANY_CO_UAT_IDENTITIES.json", "phdk_uat_identity_plan.py",
            "tenant × role", "companyco.example.test", "SWITCHED", "DIRECT",
        ],
        "JWT_STANDARD.md": [
            "UAT_SYNTHETIC_IDENTITY_STANDARD.md", "PRELIVE_SYNTHETIC", "LIVE_OR_MIXED",
            "MFA EXEMPT — NOT EXERCISED", "phdk_uat_mfa_decision.py",
        ],
        "ADMIN_CONSOLE_STANDARD.md": ["UAT_SYNTHETIC_IDENTITY_STANDARD.md"],
        "UAT_STANDARD.md": [
            "TABULAR_DATA_EXCHANGE_STANDARD.md",
            "UAT_DEFECT_WORKFLOW.md",
            "UAT_SYNTHETIC_IDENTITY_STANDARD.md",
            "PHDK uat",
            "PHDK uat prep",
            "PHDK uat fix",
            "DEFERRED — OWNER OPT-IN",
            "UAT NOT RUN",
            "PHDK_PRODUCTION_VERIFICATION.md",
        ],
        "PHDK_UAT_PREP.md": [
            "UAT_SYNTHETIC_IDENTITY_STANDARD.md",
            "PHDK uat prep",
            "PHDK uat",
            "UAT_PREP_REPORT.md",
            "PHDK_PRODUCTION_VERIFICATION.md",
        ],
        "UAT_JOURNEY_STANDARD.md": ["PHDK_UX_UI.md#rendered-workflow-walkthrough", "UAT_SYNTHETIC_IDENTITY_STANDARD.md"],
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
                "phdk-standards/UAT_SYNTHETIC_IDENTITY_STANDARD.md",
                "phdk-standards/UAT_DEFECT_WORKFLOW.md",
                "phdk-standards/TABULAR_DATA_EXCHANGE_STANDARD.md",
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

