---
name: phdk
description: >-
  Use for a current explicit request to create or edit a PHDK project's code or
  documentation, run permitted static checks, deliver through GitHub, synchronize standards,
  run the full delivery lifecycle with PHDK auto or PHDK auto force, design solution architecture
  with PHDK plan, run hybrid security assurance with PHDK secure, establish a visual style guide and previews with PHDK design,
  coordinate multi-workstream delivery with PHDK PMO, prepare authenticated synthetic users
  with PHDK uat prep, run acceptance validation with PHDK uat, audit and close standards gaps
  with PHDK check, capture requirements with PHDK capture, repair PHDK blockers with PHDK unlock,
  retrieve bounded read-only provider metadata/logs, or activate/exit PHDK Developer Mode.
  Interactive-only; bounded in-session delegation follows PHDK_INTELLIGENT_EXECUTION.md.
  No unattended/background/scheduled work, GitHub Actions, unrestricted browser operation,
  local runtime tests, Docker, new environments or external infrastructure administration.
---

# PHDK

## Portfolio-first operating policy (v2.74.0)

PHDK is the owner's opinionated operating system for related software projects: share verified knowledge and versioned modules, with `technical_stack.md` (vendored as `TECHNICAL_STACK.md`) as an evolvable default. At relevant Plan/Auto work use `PHDK_REUSE_CATALOG_STANDARD.md` to assess REUSE/ADAPT/BUILD for plausibly common capabilities; `SPECIFICATION_ONLY` is not installable code. Cross-project extraction and publication require separate authorization. Source review, lint/typecheck and safe builds are local-safe; no Docker, local services/databases or local behavioral tests under `PHDK_PRODUCTION_VERIFICATION.md`. Keep GitHub-connected hosted production (Railway where configured) and explicit UAT; load only task-relevant rules.

## Project documentation standard (v2.73.0)

For project documents created/revised during Capture, Plan, Design, PMO, Auto, Check or a scoped development task, load [PHDK_DOCUMENTATION_STANDARD.md](PHDK_DOCUMENTATION_STANDARD.md). Resolve the active versions through `docs/INDEX.md`, retain `TASK.md` in root, store new versioned intent/brief/decision/plan documents under their stable `docs/` categories and design assets in `docs/images/<topic>/vN/`. In authorized write tasks, update index and audit via `scripts/phdk_docs_audit.py` (under `phdk-standards/scripts/` when installed). Bare Check is read-only; preserve legacy files and owner customizations rather than renaming them on Upgrade. Document status never grants user approval or UAT.


## Explicit-only UAT authorization

**Binding rule:** `PHDK auto` and `PHDK auto force` MUST NOT invoke, enter, provision, seed, or run UAT Prep (45), UAT (50), or UAT Fix (60), even after milestones, deployment, Check, or a failed prior UAT. Neither FORCE nor a generic full-lifecycle instruction grants UAT authorization. These stages are **DEFERRED — OWNER OPT-IN**, not BLOCKED, FAILED, or a completion prerequisite.

Auto/Force must implement **all authorized milestones first**, perform permitted static checks and integration review, version/commit/push/PR/merge each completed value milestone, finish applicable SEO/AEO and Check/remediation without invoking acceptance tests, deploy through the existing authorized production route, verify remote main and deployment with available non-UAT evidence, and report truthful **DEVELOPMENT COMPLETE / PARTIALLY DELIVERED / BLOCKED** separately from **UAT NOT RUN**. A deployment that cannot be verified must be reported as unverified, not complete. Preserve user stories, acceptance criteria and milestone-to-story mapping as *documentation only*; no synthetic accounts, fixtures, browser journeys, runtime acceptance, or UAT spending in Auto. Do not execute local behavioral tests, Docker, or unauthorized external services.

At the end, offer `PHDK uat` as an optional **future explicit command**, without waiting for an answer as a delivery gate. Only a fresh, explicit owner invocation of `PHDK uat` authorizes UAT and its necessary Prep prerequisite, subject to normal access, safety and spending controls. Standalone `PHDK uat prep` prepares identities only when explicitly requested; it does not authorize running UAT. `PHDK uat fix` requires explicit invocation or authorization within an active explicitly initiated UAT. Prior UAT failures never reopen the completed development goal or prevent subsequent independent development.

## Canonical PHDK maintenance

If the current request changes the canonical PHDK standards repository (as distinct from a product using PHDK), load `PHDK_EVOLUTION_STANDARD.md` before editing. Resolve live main/version/README/changelog/PR state; keep the defined spelling, workspace, SemVer, manifest, entrypoint and GitHub publication rules aligned with `VERSIONING.md`, `CHANGE_MANAGEMENT.md` and `MAIN_DELIVERY_STANDARD.md`. This is no new execution authorization or command; the current request and existing controls still govern.

## Auto security maintenance

For every explicit `PHDK auto` / `PHDK auto force`, Preflight performs one fresh Stack Security Review even when installed PHDK is already current. Findings that are compatible repository-owned maintenance are part of the Auto development mandate: apply supported same-major runtime security patches (for example Node.js patch releases), compatible dependency security updates, and aligned repo-owned runtime/build declarations or lockfiles using permitted project workflows; re-run affected static/security evidence and continue normal version/delivery. Do not ask for a second `PHDK upgrade force` or security-remediation command. Major migrations, material breaking dependency changes, provider writes/new infrastructure, spending, secrets/account operations and explicit owner exclusions remain outside this automatic maintenance scope.

## Deployment-revision visibility

In applicable HTTP products, follow `PHDK_DEPLOYMENT_VERSION_STANDARD.md`: implement `GET /health/version` with product version, vendored PHDK version, exact deployed build SHA and immutable builtAt, returning uncached safe JSON. After authorized GitHub-connected autodeploy or an explicit version check, compare the live response using only the tightly scoped non-UAT `EXECUTION_SCOPE.md` read-only GET exception. Missing/mismatched metadata is UNVERIFIED/STALE; no browser, UAT, polling, arbitrary endpoint probes, provider changes or new infrastructure.

## Universal preflight

Before any PHDK command or lifecycle stage, follow `PHDK_PREFLIGHT.md` and the applicable entry/exit/handoff contract in `PHDK_LIFECYCLE.md`. A stage may start only after verifying its required upstream artifacts/handoff, and every completed/reused stage must leave durable canonical outputs plus the historical run snapshot. Verify PHDK installation/version/manifest/managed rules, then inspect `SKILLS_REGISTRY.md` for relevant capabilities and check what is actually installed/connected in the active tool. Use relevant available skills unless the user explicitly disabled skills/plugins/connectors or a named capability. Missing optional skills do not block PHDK. Within Auto, reuse Preflight and refresh only newly relevant capabilities rather than reloading every standard at every stage.

This skill routes the current assistant to PHDK standards. It does not launch an agent, create a task, or authorize work just because a tool discovers or loads `SKILL.md`.

Read the current user request and `EXECUTION_SCOPE.md`. Its interactive-only execution boundary overrides contrary language in an older standard or external skill. `PHDK_PRODUCTION_VERIFICATION.md` governs local/static versus deployed behavioral verification. Auto approval/continuity semantics use `PHDK_AUTO_CONTINUITY.md`; no stale PHDK review template may recreate its waived human gate. `PHDK_DESIGN.md` supplies the specific visual-choice distinction: normal Auto asks, Auto Force decides. Honor current owner controls within their scope; the owner can explicitly replace older documentary exceptions. A file cannot veto that current instruction or remove actual access/security controls.

## Build and hook decision routing

When a build, packaging check or Git hook has ambiguous effects or conflicts with local verification policy, load and apply the [decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) **before executing the command, declaring BLOCKED, or requesting user input**. Inspect the actual command chain and provenance; run permitted static steps and repair only proven PHDK-managed or legacy PHDK-generated steps within the authorized task. Preserve independent owner/external/unknown controls and prepare a concrete gate-change proposal if authorization is missing. Never request a prohibited local-runtime exception or initiate UAT to satisfy the gate.

## Start only from the current request

Identify what the user explicitly asked for in this conversation. Read/audit requests are read-only. An opened repository, a saved task, a failed check, an alert, or old chat context is not a new request.

Do not resume a previous mission from records alone, choose another backlog item, or start a background job. Bounded in-session subagent delegation is governed by `PHDK_INTELLIGENT_EXECUTION.md`, available in any mode when host-supported and beneficial. PMO alone governs portfolio-level worker orchestration. Preserve the same current request across status/link questions, clarifications, and context compaction. Assistant-written task records cannot revoke the user's current authorization; real owner stops and narrower requests remain binding.

Before planning, use the verified applicable PHDK baseline in `PHDK_PLAN.md` to derive the brief/plan/task boundaries. At construction-to-publication transitions or a later owner scope change, apply [phase-transition reconciliation](MAIN_DELIVERY_STANDARD.md#phase-transition-reconciliation): preserve restriction provenance/history, refresh affected worker context and separate owner authorization, technical permission, costs and explicit UAT opt-in. Neither a stale phase limit nor an edited file determines the executor's actual permission; never duplicate a scoped approval already granted.

## Complete normal delivery to main

Read `MAIN_DELIVERY_STANDARD.md` for a current request to implement, fix, or update repository code or documentation. That request includes the scoped branch, version bump, applicable permitted checks, version-prefixed commit, branch push, PR, required review, merge, and verification on remote `main`. Do not stop at a pushed branch or open PR and ask for the same delivery permission again. Honor a narrower local/branch/PR-only request, another explicit target, and the bare `PHDK upgrade` limit.

Review the complete diff and apply the approval rules in `MAIN_DELIVERY_STANDARD.md`. Sensitive behavior/policy decisions need owner approval; a well-defined current request or "push to main", "merge", or "aprobado" for the identified change may already supply it in the conversation. Do not invent a GitHub review event or proof-of-opening-the-diff requirement. Preserve formal/named/independent reviews actually required by current owner instructions, hooks, or server rules, and never invent human inspection. In AUTO FORCE, PHDK-only human gates are non-blocking without preventive review/protection investigation under `PHDK_AUTO_CONTINUITY.md`. Resolve clear in-scope conflicts, reconcile versions, and recheck. Respect hooks/protections; explain an actual unmet control or decision without changing transports to evade it.

On the first eligible locally executed PHDK Auto/Force run after adoption, do a bounded **historical** branch/worktree inventory per `PHDK_GIT_WORKSPACE_CLOSEOUT.md` and use `scripts/phdk_git_history_cleanup.py` to process only evidence-proven merged PR heads, with exact SHAs, open-PR checks, no protected/dirty/locked/unknown branches and no forced overwrites. On every verified milestone merge, also retire its unchanged remote feature head using deletion-only SHA lease when supported. Report LOCAL_MAIN, LOCAL_CLEANUP and REMOTE_BRANCH independently; a GitHub-only agent cannot synchronize the owner's disk. Bare Upgrade/Check never triggers destructive cleanup.

Confirm the resulting remote version and change before calling delivery complete. A GitHub PR merge already updates `main`; do not invent a second version-only commit or push. After each verified merged milestone with a usable local checkout, apply `PHDK_GIT_WORKSPACE_CLOSEOUT.md` and `scripts/phdk_git_closeout.py`: safely fast-forward local main, confirm matching SHA, and retire only clean, proven-integrated milestone branches/worktrees. Retain dirty/divergent/active/unverified work with exact blockers. Remote-only connector sessions must not claim the user's local workspace was synchronized; distinguish LOCAL_MAIN and LOCAL_CLEANUP from remote publication. Compare stale task records with the live user request and git/PR state. An existing provider GitHub autodeploy may follow the authorized merge; do not disable it or add dummy watch filters as PHDK enforcement. Report deployment evidence or a skipped/disabled deployment separately, without provider writes.

## Conditional AI admin standard

When the current task or `PHDK check` establishes actual AI/LLM use, load `AI_ADMIN_STANDARD.md` together with `technical_stack.md` and `DEVSECOPS.md`. AI-bearing products require applicable privileged prompt management and consumption observability; non-AI projects do not receive these features. Detect applicability from source/configuration names and product intent without reading secret values.

## Consultative multi-tenant security

When a product is or may become multi-tenant, read `PHDK_TENANT_RISK_STANDARD.md` at Capture/Plan and recheck at UAT/Check. Evaluate source-backed exposure, confidentiality/impact and blast radius before asking one unanswered material question at a time. Produce `TENANT_RISK_ASSESSMENT.md` with justified risk tier, recommended baseline/advanced isolation and encryption controls, tradeoffs, owner decision and residual risk. Do not require per-tenant databases or KMS by default, incur external costs or violate `PHDK_PRODUCTION_VERIFICATION.md`.

## Optional reusable-capability planning

For Plan/Auto, load `PHDK_REUSE_CATALOG_STANDARD.md` before rebuilding common capabilities when a catalog match is plausible. Compare `REUSE | ADAPT | BUILD` using fit, integration/maintenance cost, dependencies, compatibility, security, license and evidence. Reuse is optional; only `ACCEPTED_VERSIONED` may be selected as REUSE. Record material comparisons in `REUSE_ASSESSMENT.md`. Candidate/reviewed implementations require current-project revalidation and may inform ADAPT; `SPECIFICATION_ONLY` has no implementation. Do not delay the project to generalize a donor prematurely.

## PHDK plan

For explicit `PHDK plan`, follow `PHDK_PLAN.md`. Use the Capture/requirements baseline and applicable PHDK standards to define solution, repository, data/integration/security, and conceptual UX architecture plus a dependency-ordered implementation plan. On brownfield projects, model current state first, preserve valid decisions, identify gaps, and produce an incremental convergence plan rather than imposing a greenfield scaffold.

Create/update `SOLUTION_ARCHITECTURE.md`, `REPOSITORY_ARCHITECTURE.md`, `UX_ARCHITECTURE.md`, `MILESTONE_PLAN.md`, `IMPLEMENTATION_PLAN.md`, applicable architecture decisions, TASK integration, and `REUSE_ASSESSMENT.md` when a common-capability comparison is material. For UI scope, retain UX journeys/baseline and draft `UI_DESIGN_SYSTEM.md` / `UX_UI_DECISIONS.md`; final visual selection follows in Design. Apply `PHDK_PROJECT_MANAGEMENT_STANDARD.md`: every in-scope task/workstream maps to a value milestone with a user capability/journey, scope/dependencies, acceptance/evidence, delivery target/authorization, next milestone and expected SemVer impact. Plan does not implement product code unless a parent Auto request includes execution; even then affected UI waits for the applicable Design decision.

## PHDK design

For explicit `PHDK design`, or applicable Auto stage **25-design**, follow `PHDK_DESIGN.md` after technical/content Plan and before dependent UI implementation. This authors the visible design package; it does not silently activate Designer Mode or the full product-development lifecycle.

Resolve visual identity, composition, graphic system and experience in context using supplied/recovered references, comparable alternatives, product-specific recommendations and representative previews. Ask one unresolved question at a time in standalone Design and normal Auto; wait for the answer and selected preview approval before dependent UI coding. **In Auto Force, make the choices, record `AGENT_SELECTED_AUTO_FORCE` with rationale and continue immediately.** Do not ask for PHDK visual sign-off or pretend the owner approved the agent's choice. Reuse current owner-approved baselines, respect real owner stops/brand/security constraints, and distinguish routine visual choices from material spending/security/scope decisions.

Refine the existing `UI_DESIGN_SYSTEM.md` and `UX_UI_DECISIONS.md`; retain actual permitted references/concepts/previews in `docs/design/`, map selected tokens/components to the single shared implementation source, update affected plan/milestone tasks, and snapshot `25-design/HANDOFF.md`. Default comparison boards are 16:9 HD, with mobile layouts represented without distortion. Missing visual capability must be disclosed: normal Auto needs an informed specification-only choice when no preview can be shown; FORCE chooses with visual evidence UNVERIFIED. A generated concept or unrendered specification is not observed application behavior. No browser, local runtime test/server, Docker, new staging or paid-service exception is created.

Normal Auto records a pending `design_choice` with reason `DESIGN_AWAITING_OWNER`, retains the mandate and continues only genuinely independent authorized work. The answer resumes that goal without another development command. A switch to FORCE resolves the ordinary wait by selecting and recording, not by bypassing Design. Later work receives compact selected-baseline pointers and relevant screen/component slices instead of the full rejected-concept history.

## PHDK PMO

For explicit `PHDK PMO`, read `PHDK_PMO.md`. Inspect Capture/requirements artifacts, TASK/STATUS, code areas, current branches/PRs, and UAT/Check evidence; detect candidate workstreams and ask the owner once to confirm/add/remove/prioritize the active portfolio. After confirmation, create/update `PMO.md`, `PMO_WORKSTREAMS.md`, `PMO_DEPENDENCIES.md`, and `PMO_STATUS.md`. Dependent UI work consumes the applicable selected Design baseline; independent non-UI work does not need a needless redesign.

Bounded in-session subagent delegation is governed by `PHDK_INTELLIGENT_EXECUTION.md`, available in any mode when host-supported and beneficial. PMO alone governs portfolio-level worker orchestration. Each worker gets one workstream contract and uses Auto semantics inside that scope; workers may not delegate or independently finalize shared/global integration. The PMO orchestrator owns shared-file conflicts, dependency order, milestone integration/version delivery, version collisions, final cross-milestone review, and handoff to Check/delivery. A separately explicit UAT reads `MILESTONE_PLAN.md`, creates `UAT_MILESTONE_MATRIX.md`, and gives every delivered milestone at least one intent-linked user-value story. If the runtime lacks subagent support, say so and coordinate sequentially without pretending workers were launched.

## PHDK capture

For explicit `PHDK capture`, follow `PHDK_CAPTURE.md`. Investigate first: use existing product docs, intents, source, routes, schemas, tests, configuration, and decisions to understand the product without forcing the user to repeat known information. Build the canonical requirements package: `PROJECT_INTENT.md`, `PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md`, and `REQUIREMENTS_TRACEABILITY.md`.

When material information is missing, say questions are needed and ask focused requirements questions until all blocking gaps are resolved and remaining assumptions/open questions are explicit. If no Blocking/Material questions are needed after investigation, say so explicitly. At completion, tell the user everything captured/formulated is stored in the canonical files and list/link PROJECT_INTENT.md, PROJECT_BRIEF.md, PRD.md, FEATURES.md, and REQUIREMENTS_TRACEABILITY.md for review. Capture may span multiple turns. Do not implement product code unless the current request separately includes development.

## Theme governance for UI projects

PHDK_THEME_STANDARD.md applies to new and existing UI products: centralized semantic CSS tokens, all three presets, applicable authorized platform-admin template editing and corporate-theme visibility. Design preserves one palette source and shared components; Designer Mode and PHDK Check invoke scripts/phdk_theme_audit.py and inspect application test source/evidence. Its STATIC_PASS is not behavioral or visual verification. Actual runtime verification follows the production-first policy.

## PHDK check

Apply `PHDK_AUTOMATION_HYGIENE.md` on every Check and inside Auto's final Check. Inspect checked-in workflows/agents/watchers and remotely active GitHub Actions plus Railway Wait for CI, cron, restarts and usage when read-only access is available; log cost/blocker risks. Preserve necessary CI and GitHub-connected autodeploy; provider-side disable/reconfigure is not an automatic fix.

For explicit `PHDK check`, follow `PHDK_CHECK.md`. First perform a read-only applicability/compliance audit across active PHDK standards and implementation, create or refresh `PHDK_CHECK_REPORT.md`, present prioritized gaps, and ask once whether the user wants AUTO-FIXABLE and FIXABLE WITH VALIDATION items executed. Do not begin remediation before that answer. Applicable Design checks include mode-correct decision provenance, retained previews or disclosed visual limitations, stage 25 handoff, task/component mappings and actual fidelity evidence; a file's existence is not PASS.

If the user answers yes to that report in the same conversation, treat the listed fixable gap IDs as authorized remediation scope. Implement them autonomously under normal PHDK controls, run applicable permitted static checks, deliver when requested by the remediation flow, rerun `PHDK check`, and report residual gaps. Do not auto-fix DECISION REQUIRED or EXTERNAL / MANUAL items. Explicit `PHDK check --fix` and parent Auto scopes retain their development/remediation authorization; neither starts UAT. Acceptance requires a fresh explicit `PHDK uat`.

## Mandatory UAT role authentication

Before explicitly authorized authenticated `PHDK uat` or `PHDK uat fix`, verify applicable `PHDK_UAT_PREP.md` readiness and apply `JWT_STANDARD.md` with `UAT_JOURNEY_STANDARD.md`, Company Co fixtures and governing `PHDK_PRODUCTION_VERIFICATION.md`. Provision uniquely run-owned synthetic identities and legitimate server/provider-issued sessions per role, then verify elevated role switching and negative permissions in real permitted deployed UAT journeys. Do not ask for passwords or bearer secrets in chat or forge a privileged session. A missing safely repairable bootstrap belongs in UAT Prep before acceptance (or UAT Fix if discovered during execution), not a permanent ceremonial approval stop. Check inspects source and available evidence without provisioning sessions or running UAT; verify cleanup/revocation on every executed Prep/UAT outcome.

## PHDK uat prep

For explicit `PHDK uat prep` (case-insensitive), or necessary Prep within an explicitly initiated `PHDK uat`, implement `PHDK_UAT_PREP.md`: inspect actual identity/provider/RBAC/tenancy, **develop** missing safe Company Co seeder, synthetic identities and legitimate sessions, verify role/tenant isolation only on the permitted deployed candidate, handle required audited Test as and document provisioning/cleanup. Create `UAT_AUTH_PLAN.md`, `UAT_ROLE_MATRIX.md`, `UAT_FIXTURE_MANIFEST.md`, `UAT_PREP_REPORT.md`; do not merely list accounts or ask for a password/JWT. Standalone Prep follows normal version/PR/merge delivery without launching UAT/Auto. Prep within an explicit UAT request precedes acceptance; Auto/Force do not start it. Browser only in actual UAT/UAT Fix; no local runtime tests, Docker, new environment, authentication bypass or unauthorized provider writes.

## PHDK uat fix

For explicit `PHDK uat fix`, read current `UAT_REPORT.md` and `UAT_CASES.md`. Convert every FAIL into an actionable defect and every unresolved BLOCKED/MANUAL case into an explicit unblock/manual action plan. Repair clearly in-scope fixable failures autonomously, rerun affected permitted deployed UAT/regression checks, and update repair/retest evidence. When nothing is auto-fixable, guide the owner through remaining prerequisites/manual validations and state exactly what to rerun afterward. Material visual direction changes reopen only affected Design decisions under the current mode; routine fidelity repairs do not trigger a fresh style interview.

## PHDK uat

For explicit `PHDK uat`, follow `UAT_STANDARD.md` and run necessary Prep under the same scoped authorization. Identify current intent, derive intent-aligned user stories and traceable cases for the deployed candidate, create/update `UAT_CASES.md`, execute permitted evidence autonomously, and create/update `UAT_REPORT.md`. Include selected Design baseline fidelity for applicable UI scope. Do not ask for approval between cases. Never pass an unexecuted behavioral case by inspection or from an approved/generated mockup; use BLOCKED or MANUAL when required evidence is unavailable or excluded.

UAT validates and reports the candidate after necessary Prep. Product-code repair requires explicit `PHDK uat fix` or authorization within the active explicitly initiated UAT. Auto/Force do not reopen prior acceptance failures; report UAT NOT RUN separately from the development result.

## PHDK auto

For explicit `PHDK auto` or `PHDK auto force`, follow `PHDK_AUTO.md` and `PHDK_AUTO_CONTINUITY.md` as the end-to-end lifecycle orchestrator. On every invocation, reread the complete intent/requirements baseline and compare it with actual product code before reusing Capture/Plan outputs; reuse requires current, coherent coverage of the authorized goal. Documentation or a scaffold does not establish an implemented product. Missing code requires construction; partial code requires completing gaps while preserving valid work. Unavailable source is UNVERIFIED, not proof no code exists.

Plan flows into applicable **Design**, then implementation in the same active goal. **Auto asks the unresolved visual choices and waits; Auto Force selects, records AGENT_SELECTED_AUTO_FORCE and continues.** Once the applicable Design decision is resolved, no separate development command or ceremonial stage approval is needed. Execute the entire authorized scope without shrinking it to an MVP. At Auto start show the lifecycle board: Preflight, Capture, Plan, Design, PMO/Workstreams, Integration Review, applicable SEO, AEO/GEO, Check, Remediation and Delivery. Show UAT Prep, UAT and UAT Fix separately as DEFERRED — OWNER OPT-IN, with UAT NOT RUN. At transitions state what closed, what is running, what comes next and strongest evidence. Updates are informational; normal Auto's actual Design choice remains product input.

If no single delivery goal is stated but Capture/Plan/repo evidence exposes multiple parallel fronts, enter PMO portfolio discovery and ask once to confirm those workstreams; do not force one arbitrary outcome because TASK has several items. Reuse/run the full applicable sequence, including Design before affected UI work. Reuse only stages whose required outputs/coverage are verified current, mark genuinely inapplicable stages N/A, and keep UAT stages deferred pending explicit owner opt-in; a completed plan/design does not complete implementation. Keep communicating without ending at milestones. Lifecycle stages do not trigger versions or optional full verification cycles; value milestones follow the project-management delivery contract. Actual controls remain effective; checks must stay within the production-first policy and cannot be bypassed.

Auto replaces Developer Mode for that goal; it grants no direct-main bypass, background execution, new mission, or persistent flag. Exit on `PHDK salir de auto`, clear stop, whole-goal completion, or conversation end. Files, examples, installation, standards/skill updates, and requests to implement the command never activate it. The command's specific cadence takes precedence over generic templates, with the explicit normal Auto Design-choice exception.

## PHDK auto force and continuity

For explicit `PHDK auto force` (case-insensitive), apply `PHDK_AUTO_CONTINUITY.md`. PHDK-imposed human reviews/sign-offs are `NON_BLOCKING_BY_MODE` immediately: do not investigate whether they block, query review/protection requirements preventively, seek reviewers, or ask for approval. Complete Design decisions autonomously with actual agent-selection provenance, then continue scoped implementation, assistant diff review, permitted checks, branch push, PR, merge and remote-main readback. No repeated permission for permitted mandatory checks. Apply the [hook decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) before reporting an unresolved conflicting hook as a blocker; never run excluded tests or bypass enforcement.

At start/resume, each FORCE progress update, after partial delivery and before a question/blocker, apply the short rule refresh and mandatory reminder in `PHDK_AUTO_CONTINUITY.md` and `PHDK_COMMUNICATION_STANDARD.md`. Reconcile inherited blockers, discard stale assistant interpretations and use the reminder. Missing routine definitions require a concrete proposal/defaults/configuration followed by authorized implementation; do not transfer routine design work to the owner or recommend omitting accepted gaps. Preserve real user exclusions/host controls and reserve questions for indispensable new sensitive/scope decisions, with a proposed solution already prepared.

An actual hook/tool/GitHub rejection starts report → diagnose → repair in scope → revalidate → retry push/PR/merge → verify remote main. Keep authorization active, finish independent tasks and retry only after meaningful repair or changed evidence. Preserve real owner restrictions, security, hooks, platform controls and provider boundaries; do not disable, bypass or change transports/credentials to evade them.

Both Auto variants record mandate/provenance, goal/scope, restrictions, progress and next action in `docs/phdk/lifecycle/<run-id>/AUTO_STATE.json`. Reload with current instructions after compaction and before ending a turn; malformed/missing state is reconstructed internally, never a duplicate permission gate. Use `scripts/phdk_auto_gate.py` where permitted as an advisory state reader. Its `design_choice` kind distinguishes ordinary Auto's owner answer from FORCE selection without ignoring a true `owner_stop`. The record is evidence, not authority. Perform the stated eligible next action in the same turn; a normal Auto Design question accurately reports waiting rather than claiming dependent work continues. Installation, examples and editing the command do not activate it.

## PHDK unlock

For current `PHDK unlock`, read `PHDK_UNLOCK.md`. Explain that it audits PHDK-related blockers and repairs documentary restrictions in this repository according to current owner instructions, preserving real checks, reviews, hooks, protections, access, security, and provider-write boundaries.

Inspect relevant existing native instructions, copied PHDK sources/in-repository skills, task records, actual hooks/toolchain, and GitHub evidence. Reconcile authorized local exceptions and stale task boundaries, then finish scoped normal versioned branch/PR delivery. Do not stop after fixing only one wrapper while another active copy retains the blocker.

Do not persist an unlocked flag, activate Developer Mode, resume old missions, merge unrelated PRs, weaken controls, or alter provider settings. Natural-language approval and bounded diagnosis requests already count without this command; quoted examples do not invoke it.

## PHDK Developer Mode

For explicit activation with `PHDK modo developer` or `PHDK Developer Mode`, read `PHDK_DEVELOPER_MODE.md` and briefly explain granted permissions. It applies only during the active conversation to small, low-risk changes requested while active: edit, repository-standard version bump, applicable permitted checks, version-prefixed commit, and fast-forward push directly to `main` if existing controls allow. That push may trigger the already connected deployment.

Deactivate on `PHDK salir de developer mode`, an unambiguous stop/exit, or conversation end. Quoted commands, briefs, skill loading, files, and prior sessions never activate or restore it. Keep no persistent activation flag. Activation alone starts no task, and audits remain read-only.

High-risk authentication, authorization, secrets, data/migrations, payments, infrastructure, and permission-policy changes follow normal review. Stop direct-main flow on a failed applicable check, rejected/non-fast-forward push, or unsatisfied control. No hook/protection bypass, forced update, settings changes, automatic retry, or provider CLI/API/dashboard deployment.

## Requested provider diagnostics

Follow `EXECUTION_SCOPE.md` — `Bounded read-only provider diagnostics` for a current request such as "verifica Railway", deployment/version check, or log/incident diagnosis. Read only relevant existing service/deployment/status/source/branch/non-secret configuration/watch metadata and logs through an authorized API/CLI/connector, with resolved target, finite bounds, and redaction. No second authorization phrase, Developer Mode, or unlock is needed; an older task-specific exclusion does not cancel the newer read request. No browser, streams/polling, app probes, database access, secret values, new permissions, settings writes, or deployment. Report provider evidence separately from product-test or recovery claims.

## Universal commands — `PHDK upgrade` / `PHDK upgrade force`

Exact `PHDK upgrade force` publishes changed vendored standards as its first remote-main milestone before creating fresh Auto Force worktrees. Reuse an unfinished same-goal branch/PR, verify remote manifest content with `scripts/phdk_upgrade_remote_gate.py` where local Git is available (and native rules/PR separately), then fast-forward clean local main and retire only the proven-integrated owned branch/worktree. The updater's CURRENT/UPDATED is not publication. Bare Upgrade and passive Preflight cannot publish by themselves.

**Composite Force behavior:** exact `PHDK upgrade force` does not end after synchronization. After the forced upgrade, security review, eligible central-status update and verification, transition immediately into `PHDK auto force` in the same foreground session. Continue the already identified authorized goal when present; otherwise use the bounded repository-maintenance goal from `PHDK_UPGRADE.md`. Do not ask the owner to type Auto separately and do not invent new features.

For exact `PHDK upgrade` or `PHDK upgrade force` (case-insensitive after trimming whitespace):

- Bare `PHDK upgrade` preserves local edits/conflicts inside the PHDK-owned surface and stops conflicting writes while continuing independent permitted review.
- `PHDK upgrade force` authorizes replacement only of the PHDK-owned surface from canonical upstream: manifest-owned `phdk-standards/` files plus exact `PHDK-MANAGED` blocks. It may discard dirty edits there and remove obsolete previously manifest-owned standards files.
- Force preserves all non-PHDK source/docs/config, owner instructions outside managed markers, hooks/settings, and unknown extra files.

1. Fetch current canonical PHDK `main` and read `VERSION` and upgrade instructions.
2. Follow `PHDK_UPGRADE.md` within the current request. Preserve dirty work and genuine owner overrides in a bare sync; apply any explicit current request to remove/reconcile local PHDK exceptions through `PHDK_UNLOCK.md`.
3. Synchronize manifest-controlled standards and the current tool's managed rule block.
4. Perform the bounded read-only [Stack Security Review](PHDK_SECURE.md#stack-security-review), including no-op/newer-local cases. Actual Preflight version adoption also requires it once; reuse current evidence at unchanged stages. Report STANDARDS_SYNC, STACK_REVIEW_COVERAGE and STACK_SECURITY_STATUS separately; pending helper output is not a completed audit.
5. For a verified `tuyoisaza/<repo>`, apply `PHDK_REPOSITORY_STATUS.md`. If this foreground session already has write access to canonical `tuyoisaza/PHDK`, refresh `docs/repos/<repo>/status.md` with evidence-backed PHDK, repository SHA, tech-stack and stack-review state. Missing access is `CENTRAL_STATUS: NOT_PUBLISHED`; never request credentials or schedule a retry.
6. Verify source copy and review evidence, report, and stop. Do not continue into product work or schedule a later upgrade.

The exact command authorizes standards synchronization and read-only review, not a push/merge, deployment, workflow run, or external administration. A current instruction explicitly requesting git delivery supplies that additional permission.

## Skill updates

Update an installed skill clone only when the current request explicitly includes installation, update, or synchronization. Use a safe fast-forward and never discard local modifications. Re-read updated `SKILL.md`, `EXECUTION_SCOPE.md`, and `VERSION` before proceeding.

Do not register auto-update hooks, scheduled refreshes, background pulls, or session-start jobs. Skill availability or a newer version is not authorization to mutate the project.

## New project

1. If the current request is for a new project and purpose is unclear, use `SPEC_INTERVIEW_PROMPT.md` to clarify the necessary decision.
2. Generate the requested kit through `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md`, without bots, schedules, backup jobs, CI, or external provisioning. Bounded in-session delegation can be used in any mode under `PHDK_INTELLIGENT_EXECUTION.md`.
3. When the request includes PHDK installation, read `PHDK_MANIFEST.txt` and vendor exactly its mappings under `phdk-standards/`.
4. Include the exact `PHDK_NATIVE_RULES.md` managed block in the current tool's instruction file per `ENFORCEMENT.md`. Preserve owner instructions and managed markers; do not generate files for unused tools.
5. Build product code only when the current request includes it. Use `BUILD_APP_FOUNDATION_PROMPT.md` for that scope, after applicable Plan/Design. In Auto, a foundation is one part of the whole goal; continue remaining agreed development and final verification/delivery under `PHDK_AUTO.md` rather than stopping at the scaffold.

A request for a kit, standalone design package or standards update is not permission to start full product implementation.

## Existing project

1. Read owner controls and `phdk-standards/AGENTS.md` / `EXECUTION_SCOPE.md` (or installed standards when no vendored copy exists).
2. Read `TASK.md` and `STATUS.md` as context, not standing authorization.
3. Load only detailed standards needed for the current request; preserve valid selected Design baselines and working interfaces.
4. Implement and verify necessary steps with this assistant. Explicit Auto follows `PHDK_AUTO.md` through agreed development and final integrated verification, including its Design decision policy. Explicit PMO coordinates portfolio workers; any mode may use bounded in-session task workers under `PHDK_INTELLIGENT_EXECUTION.md`. Never use unattended/future execution.
5. Complete normal delivery under `MAIN_DELIVERY_STANDARD.md`, including verified remote `main` unless the user set a narrower outcome. Developer Mode supplies only its separate bounded direct-main exception for eligible tasks; hard stops and high-risk exclusions remain effective. No extra releases or unrelated work.
6. Read relevant `SKILLS_REGISTRY.md` entries; use bounded delegation only under `PHDK_INTELLIGENT_EXECUTION.md`, never external background orchestration.
7. Report and stop when the whole requested goal and delivery are complete, not at an Auto stage; preserve unrelated ideas as inactive context.

## Never

- Regenerate existing project kit files as if the project were new.
- Replace a genuine current owner restriction with upstream defaults without scoped instruction; remove actual checks, access rights, or security controls as documentary cleanup.
- Treat `TASK.md`, `STATUS.md`, a skill trigger, or an old approval as a new request.
- Launch/delegate agents outside the bounded in-session contract; allow recursive PMO-worker delegation; create a schedule; or continue after the session.
- Create, enable, dispatch, rerun, or schedule GitHub Actions or hosted CI.
- Operate browsers or probe applications outside scoped permitted UAT/UAT Fix, access real customer data, or administer live services/provider settings/secrets/repositories. Requested existing provider metadata/log reads use only bounded read-only diagnostics.
- Claim a generated design concept is a tested application, an agent's choice is owner approval, or a standards upgrade disabled external automation/stopped a process.

## Production-first verification override (v2.58.0)

**Mandatory:** Apply [PHDK_PRODUCTION_VERIFICATION.md](PHDK_PRODUCTION_VERIFICATION.md). Owner-authorized production-only UAT supersedes earlier local unit/in-process/runtime testing, staging-only identity, and blanket production-test prohibitions. Local operations are limited to static analysis, lint, typecheck and safe builds; Docker, local runtime tests and separate staging/databases are prohibited. UAT uses existing versioned production deployment and database, strictly scoped run-owned synthetic identities/records, audit, automated cleanup and verified revocation on success, failure and interruption. Never touch real data or bypass security hooks; apply the [hook decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) before reporting an unresolved verification gate BLOCKED. Design adds no preview-server or browser-test exception.


## Hook compatibility (v2.61.0)

Apply the [hook decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) before executing an ambiguous build/packaging/hook command, declaring its conflict BLOCKED, or asking the owner. Inspect the command chain and provenance, automatically repair only proven PHDK-owned incompatibilities within authorized remediation, and preserve independent security/version/branch/commit gates. Owner-owned, external and unknown controls retain their authorization boundary; prepare a concrete proposal for any unresolved gate. Never request a prohibited local-runtime exception, execute excluded tests, use --no-verify or start UAT to satisfy a hook.
