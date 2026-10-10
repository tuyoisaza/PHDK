---
name: phdk
description: >-
  Use for a current explicit request to create or edit a PHDK project's code or
  documentation, validate locally, deliver through GitHub, synchronize standards,
  run the full delivery lifecycle with PHDK auto, design solution architecture and execution plans with PHDK plan, coordinate multi-workstream delivery with PHDK PMO, run autonomous acceptance validation with PHDK uat, audit and close standards gaps with PHDK check, capture or reconstruct professional requirements with PHDK capture, repair PHDK blockers with
  PHDK unlock, retrieve bounded read-only provider
  status/configuration metadata or logs, or activate/exit PHDK Developer Mode.
  Interactive-only; PMO is the sole bounded in-session worker-delegation exception.
  No unattended/background/scheduled work, GitHub Actions, browser operation, or external
  infrastructure administration.
---

# PHDK

## Universal preflight

Before any PHDK command or lifecycle stage, follow `PHDK_PREFLIGHT.md` and the applicable entry/exit/handoff contract in `PHDK_LIFECYCLE.md`. A stage may start only after verifying its required upstream artifacts/handoff, and every completed/reused stage must leave durable canonical outputs plus the historical run snapshot. Verify PHDK installation/version/manifest/managed rules, then inspect `SKILLS_REGISTRY.md` for relevant capabilities and check what is actually installed/connected in the active tool. Use relevant available skills unless the user explicitly disabled skills/plugins/connectors or a named capability. Missing optional skills do not block PHDK.


This skill routes the current assistant to PHDK standards. It does not launch an agent, create a task, or authorize work just because a tool discovers or loads `SKILL.md`.

Read the current user request and `EXECUTION_SCOPE.md`. Its interactive-only, single-assistant boundary overrides contrary language in an older standard or external skill. Honor current owner controls within their scope; the owner can explicitly replace older documentary exceptions. A file cannot veto that current instruction or remove actual access/security controls.

## Start only from the current request

Identify what the user explicitly asked for in this conversation. Read/audit requests are read-only. An opened repository, a saved task, a failed check, an alert, or old chat context is not a new request.

Do not resume a previous mission from records alone, choose another backlog item, or start a background job. Outside explicit PMO, do not delegate to another agent. Preserve the same current request across status/link questions, clarifications, and context compaction. Assistant-written task records cannot revoke the user's current authorization; real owner stops and narrower requests remain binding.

## Complete normal delivery to main

Read `MAIN_DELIVERY_STANDARD.md` for a current request to implement, fix, or update repository code or documentation. That request includes the scoped branch, version bump, applicable local checks, version-prefixed commit, branch push, PR, required review, merge, and verification on remote `main`. Do not stop at a pushed branch or open PR and ask for the same delivery permission again. Honor a narrower local/branch/PR-only request, another explicit target, and the bare `PHDK upgrade` limit.

Review the complete diff and apply the approval rules in `MAIN_DELIVERY_STANDARD.md`. Sensitive behavior/policy decisions need owner approval; a well-defined current request or "push to main", "merge", or "aprobado" for the identified change may already supply it in the conversation. Do not invent a GitHub review event or proof-of-opening-the-diff requirement. Preserve formal/named/independent reviews actually required by current owner instructions, hooks, or server rules, and never invent human inspection. Resolve clear in-scope conflicts, reconcile versions, and recheck. Respect hooks/protections; explain an actual unmet control or decision without changing transports to evade it.

Confirm the resulting remote version and change before calling the delivery complete. A GitHub PR merge already updates `main`; do not invent a second version-only commit or push. Compare stale task records with the live user request and git/PR state. An existing provider GitHub autodeploy may follow the authorized merge; do not disable it or add dummy watch filters as PHDK enforcement. Report deployment evidence or a skipped/disabled deployment separately, without provider writes.

## Conditional AI admin standard

When the current task or `PHDK check` establishes actual AI/LLM use, load `AI_ADMIN_STANDARD.md` together with `technical_stack.md` and `DEVSECOPS.md`. AI-bearing products require super-admin prompt management and consumption observability; non-AI projects do not receive these features. Detect applicability from source/configuration names and product intent without reading secret values.

## PHDK plan

For explicit `PHDK plan`, follow `PHDK_PLAN.md`. Use the Capture/requirements baseline and applicable PHDK standards to define solution, repository, data/integration/security, and conceptual UX architecture plus a dependency-ordered implementation plan. On brownfield projects, model current state first, preserve valid decisions, identify gaps, and produce an incremental convergence plan rather than imposing a greenfield scaffold.

Create/update `SOLUTION_ARCHITECTURE.md`, `REPOSITORY_ARCHITECTURE.md`, `UX_ARCHITECTURE.md`, `IMPLEMENTATION_PLAN.md`, applicable architecture decisions, and TASK integration. Plan does not implement product code unless a parent Auto request includes execution.

## PHDK PMO

For explicit `PHDK PMO`, read `PHDK_PMO.md`. Inspect Capture/requirements artifacts, TASK/STATUS, code areas, current branches/PRs, and UAT/Check evidence; detect candidate workstreams and ask the owner once to confirm/add/remove/prioritize the active portfolio. After confirmation, create/update `PMO.md`, `PMO_WORKSTREAMS.md`, `PMO_DEPENDENCIES.md`, and `PMO_STATUS.md`.

PMO is the only PHDK context allowed to delegate bounded workstreams to runtime-supported in-session workers. Each worker gets one workstream contract and uses Auto semantics inside that scope; workers may not delegate or independently finalize shared/global integration. The PMO orchestrator owns shared-file conflicts, dependency order, version collisions, integration review, and the handoff to UAT/UAT Fix/Check. If the runtime lacks subagent support, say so and coordinate sequentially without pretending workers were launched.

## PHDK capture

For explicit `PHDK capture`, follow `PHDK_CAPTURE.md`. Investigate first: use existing product docs, intents, source, routes, schemas, tests, configuration, and decisions to understand the product without forcing the user to repeat known information. Build the canonical requirements package: `PROJECT_INTENT.md`, `PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md`, and `REQUIREMENTS_TRACEABILITY.md`.

When material information is missing, say that questions are needed and ask focused requirements questions until all blocking gaps are resolved and remaining assumptions/open questions are explicit. If no Blocking/Material questions are needed after investigation, say so explicitly. At completion, tell the user that everything captured/formulated is stored in the canonical files and list/link PROJECT_INTENT.md, PROJECT_BRIEF.md, PRD.md, FEATURES.md, and REQUIREMENTS_TRACEABILITY.md for review. Capture may span multiple turns. Do not implement product code unless the current request separately includes development.

## PHDK check

For explicit `PHDK check`, follow `PHDK_CHECK.md`. First perform a read-only applicability/compliance audit across the repository's active PHDK standards and implementation, create or refresh `PHDK_CHECK_REPORT.md`, present the prioritized gaps, and ask once whether the user wants the AUTO-FIXABLE and FIXABLE WITH VALIDATION items executed. Do not begin remediation before that answer.

If the user answers yes to that report in the same conversation, treat the listed fixable gap IDs as the authorized remediation scope. Implement them autonomously under normal PHDK controls, run applicable checks/UAT, deliver when requested by the remediation flow, rerun `PHDK check`, and report residual gaps. Do not auto-fix DECISION REQUIRED or EXTERNAL / MANUAL items.

## PHDK uat fix

For explicit `PHDK uat fix`, read the current `UAT_REPORT.md` and `UAT_CASES.md`. Convert every FAIL into an actionable defect and every unresolved BLOCKED/MANUAL case into an explicit unblock/manual action plan. Repair all clearly in-scope fixable failures autonomously, rerun affected UAT/regression checks, and update the report with repair/retest evidence. When nothing is auto-fixable, do not stop at that observation: guide the owner step-by-step through the remaining prerequisites/manual validations and state exactly what to rerun afterward.

## PHDK uat

For explicit `PHDK uat`, follow `UAT_STANDARD.md`. Identify the project's current intent first, derive user stories that explicitly align to that intent, then derive traceable acceptance cases for the current candidate and create/update `UAT_CASES.md`, execute all permitted acceptance evidence autonomously, and create/update `UAT_REPORT.md`. Do not ask for approval between cases. Never pass an unexecuted behavioral case by inspection; use BLOCKED or MANUAL when the required evidence is unavailable or excluded.

Standalone UAT validates and reports the candidate. Under active `PHDK auto`, repair in-scope UAT failures and rerun affected cases before final delivery.

## PHDK auto

For explicit `PHDK auto`, follow `PHDK_AUTO.md` as the end-to-end lifecycle orchestrator. At Auto start, show the lifecycle board (Preflight, Capture, Plan, PMO/Workstreams, Integration Review, UAT, UAT Fix, Check, Remediation, Delivery) with PENDING/RUNNING/REUSED/COMPLETED/BLOCKED/NOT APPLICABLE statuses. At every lifecycle transition, state what closed, what is running, what comes next, and the strongest evidence. These updates are informational, not approval gates. If no single delivery goal is stated but Capture/Plan/repo evidence exposes multiple parallel fronts, enter PMO portfolio discovery and ask once to confirm those workstreams; do not ask the user to invent one arbitrary concrete outcome merely because TASK.md has several open items. Reuse or run Capture, then Plan, PMO/workstream execution, PMO Integration Review, UAT, UAT Fix, Check, in-scope Check remediation, and final delivery as applicable. Skip only stages whose outputs are already current/coherent or genuinely not applicable. Keep communicating without ending at milestones; do not create a release or optional full test cycle per stage. Actual mandatory hooks and necessary diagnostic checks remain applicable.

Auto replaces Developer Mode for that goal; it grants no direct-main bypass, background execution, new mission, or persistent flag. Exit on `PHDK salir de auto`, a clear stop, whole-goal completion, or conversation end. Source files, examples, installation, and a request to implement this command never activate it. The command's specific cadence takes precedence over generic interview, slice, and handoff approval templates.

## PHDK unlock

For the current command `PHDK unlock`, read `PHDK_UNLOCK.md`. Explain briefly that it audits PHDK-related blockers and repairs documentary restrictions in this repository according to the owner's current instructions, while preserving real checks, reviews, hooks, protections, access, security, and provider-write boundaries.

Inspect all relevant existing active native instruction files, copied PHDK sources and in-repository skills, task records, actual hooks/toolchain, and current GitHub evidence. Reconcile the authorized local exceptions and stale task boundaries, then finish the scoped normal versioned branch/PR delivery. Do not stop after fixing only one wrapper while another active copy retains the blocker.

Do not persist an unlocked flag, activate Developer Mode, resume old missions, merge unrelated PRs, weaken controls, or alter provider settings. Natural-language approval and bounded diagnosis requests already count without this command; quoted examples do not invoke it.

## PHDK Developer Mode

For explicit user activation with `PHDK modo developer` or `PHDK Developer Mode`, read `PHDK_DEVELOPER_MODE.md` and briefly explain the granted permissions. The mode applies only during the active conversation to small, low-risk changes requested while active: edit, repository-standard version bump, applicable local checks, version-prefixed commit, and fast-forward push directly to `main` if existing controls allow it. That push may trigger the already connected deployment.

Deactivate on `PHDK salir de developer mode`, an unambiguous user stop/exit, or when the active conversation ends. Quoted commands, briefs, skill loading, files, and prior sessions never activate or restore it. Keep no persistent activation flag. Activation alone starts no task, and audits remain read-only.

High-risk authentication, authorization, secrets, data/migrations, payments, infrastructure, and permission-policy changes follow normal review. Stop the direct-main flow on a failed applicable check, rejected/non-fast-forward push, or a control that cannot be satisfied. No hook/protection bypass, forced update, settings changes, automatic retry, or provider CLI/API/dashboard deployment.

## Requested provider diagnostics

Follow `EXECUTION_SCOPE.md` — `Bounded read-only provider diagnostics` for a current request such as "verifica Railway", a deployment/version check, or log/incident diagnosis. Read only relevant existing service/deployment/status/source/branch/non-secret configuration/watch metadata and logs through an authorized API/CLI/connector, with a resolved target, finite bounds, and redaction. No second authorization phrase, Developer Mode, or unlock is needed; an older task-specific exclusion does not cancel the newer read request. No browser, streams/polling, app probes, database access, secret values, new permissions, settings writes, or deployment. Report provider evidence separately from product-test or recovery claims.

## Universal commands — `PHDK upgrade` / `PHDK upgrade force`

For exact `PHDK upgrade` or `PHDK upgrade force` (case-insensitive after trimming whitespace):

- Bare `PHDK upgrade` preserves local edits/conflicts inside the PHDK-owned surface and stops rather than overwriting them.
- `PHDK upgrade force` explicitly authorizes replacement of only the PHDK-owned surface from canonical upstream: manifest-owned `phdk-standards/` files plus exact `PHDK-MANAGED` blocks. It may discard dirty edits there and remove obsolete previously manifest-owned standards files.
- Force must preserve all non-PHDK source/docs/config, owner instructions outside managed markers, hooks/settings, and unknown extra files.

1. Fetch the current canonical PHDK `main` and read its `VERSION` and upgrade instructions.
2. Follow `PHDK_UPGRADE.md` within the current request. Preserve dirty work and genuine owner overrides in a bare sync; apply any explicit current request to remove/reconcile local PHDK exceptions through `PHDK_UNLOCK.md`.
3. Synchronize the manifest-controlled standards and the current tool's managed rule block.
4. Verify the source copy, report, and stop. Do not continue into product work or schedule a later upgrade.

The exact command authorizes the sync, not a push/merge, deployment, workflow run, or external administration. A current instruction that also explicitly requests git delivery supplies that additional permission.

## Skill updates

Update an installed skill clone only when the current request explicitly includes installation, update, or synchronization. Use a safe fast-forward and never discard local modifications. Re-read the updated `SKILL.md`, `EXECUTION_SCOPE.md`, and `VERSION` before proceeding.

Do not register auto-update hooks, scheduled refreshes, background pulls, or session-start jobs. Skill availability or a newer version is not authorization to mutate the project.

## New project

1. If the current request is for a new project and its purpose is unclear, use `SPEC_INTERVIEW_PROMPT.md` to clarify the necessary decision.
2. Generate the requested kit through `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md`, without adding bots, schedules, backup jobs, CI, or external provisioning. Worker delegation is unavailable unless the user explicitly activates PMO later.
3. When the request includes PHDK installation, read `PHDK_MANIFEST.txt` and vendor exactly its mappings under `phdk-standards/`.
4. Include the exact `PHDK_NATIVE_RULES.md` managed block in the current tool's instruction file per `ENFORCEMENT.md`. Preserve existing owner instructions and the managed markers; do not generate files for unused tools.
5. Build product code only when the current request includes it. Use `BUILD_APP_FOUNDATION_PROMPT.md` for that authorized scope. In Auto, a foundation is one part of the whole goal; continue the remaining agreed development and final verification/delivery under `PHDK_AUTO.md` rather than stopping at the scaffold.

A request for a kit or standards update is not permission to start implementation.

## Existing project

1. Read the project's owner controls and `phdk-standards/AGENTS.md`/`EXECUTION_SCOPE.md` (or the installed standards when no vendored copy exists).
2. Read `TASK.md` and `STATUS.md` as context, not standing authorization.
3. Load only the detailed standards needed for the current request.
4. Implement and verify the necessary steps with this assistant. Explicit Auto follows `PHDK_AUTO.md` through all agreed development and final integrated verification. Explicit PMO may coordinate bounded in-session workers under `PHDK_PMO.md`; otherwise do not use subagents/delegated reviewers/parallel queues. Never use unattended or future execution.
5. Complete the current request's normal delivery under `MAIN_DELIVERY_STANDARD.md`, including verified remote `main` unless the user set a narrower outcome. An active Developer Mode supplies only its separate bounded direct-main exception for eligible requested tasks; its hard stops and high-risk exclusions remain effective. No extra releases or unrelated work.
6. Read relevant entries in `SKILLS_REGISTRY.md` yourself; do not execute their orchestration, delegation, or background behaviors.
7. Report and stop when the whole requested goal and delivery are complete, not at an Auto stage; preserve unrelated ideas as inactive context.

## Never

- Regenerate existing project kit files as if the project were new.
- Replace a genuine current owner restriction with upstream defaults without the owner's scoped instruction; remove actual checks, access rights, or security controls as documentary cleanup.
- Treat `TASK.md`, `STATUS.md`, a skill trigger, or an old approval as a new request.
- Launch/delegate another agent outside explicit PMO; allow a PMO worker to recursively delegate; create a schedule; or continue after the session.
- Create, enable, dispatch, rerun, or schedule GitHub Actions or hosted CI.
- Operate browsers, probe live applications, connect to databases, or administer live services, provider settings, secrets, or repositories. Requested existing provider metadata/log reads use only the bounded read-only diagnostic rule.
- Claim a standards upgrade disabled external automation or stopped a running process.
