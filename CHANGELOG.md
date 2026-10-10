## v2.45.0 — 2026-10-10

### Added

- Added `PHDK_LIFECYCLE.md` as the formal stage input/output/exit-gate/handoff standard.
- Added root `PHDK_LIFECYCLE.md` current-run dashboard and immutable historical run folders under `docs/phdk/lifecycle/<run-id>/`.
- Every lifecycle stage now produces a mandatory `HANDOFF.md` and snapshots material deliverables before the next stage starts.
- Defined canonical deliverables for Preflight, Capture, Plan, PMO/Workstreams, Integration Review, UAT, UAT Fix, Check, Remediation, and Delivery.
- Added new canonical artifacts:
  - `PHDK_PREFLIGHT_REPORT.md`
  - `INTEGRATION_REPORT.md`
  - `UAT_REMEDIATION.md`
  - `PHDK_REMEDIATION_REPORT.md`
  - `DELIVERY_REPORT.md`
- Added explicit downstream entry validation: each stage must verify the previous handoff/artifacts and exact candidate/revision before starting.
- Added upstream invalidation/reopen semantics when a later stage discovers stale/incorrect earlier artifacts.
- Auto transition messages now declare what the previous stage did, what it delivered, historical snapshot location, exit gate, what the next stage will do, and what inputs it must verify.
- Added final lifecycle historical closure so future humans/agents can reconstruct what Capture understood, Plan decided, PMO executed, Integration combined, UAT accepted/blocked, Check found, remediation changed, and Delivery shipped.

### Changed

- Wired lifecycle handoffs into Preflight, Capture, Plan, PMO, Integration Review, UAT/UAT Fix, Check/remediation, Delivery, Auto, task tracking, routing/native rules, onboarding, README, and summary guidance.
- Increased the vendoring manifest to include the lifecycle standard.

## v2.44.3 — 2026-10-10

### Added

- Added a mandatory Auto lifecycle communication contract.
- At `PHDK auto` startup, the assistant must show the full lifecycle board: Preflight, Capture, Plan, PMO/Workstreams, Integration Review, UAT, UAT Fix, Check, Remediation, and Delivery.
- Every stage is classified as PENDING, RUNNING, REUSED, COMPLETED, BLOCKED, or NOT APPLICABLE.
- On every lifecycle transition, Auto must state what closed/reused, the strongest artifact/evidence, the current stage, and the next stage.
- Status questions during Auto must answer with the lifecycle position first, rather than only implementation detail.
- Final Auto reporting now closes the lifecycle explicitly with terminal status for every applicable stage.

### Fixed

- Prevented Auto from explaining only permissions/scope ("puedo revisar, probar, versionar y entregar") without telling the owner where the process is in Capture/Plan/PMO/Integration/UAT/Check/Delivery.
- Lifecycle progress messages remain informational and must not become new approval gates.

## v2.44.2 — 2026-10-10

### Fixed

- Corrected `PHDK auto` behavior when a repository has multiple parallel project fronts but no single next TASK delivery.
- Generic Auto now inspects Capture, Plan, PMO artifacts, requirements, current work, UAT/Check findings and repository evidence for a coherent active portfolio.
- When multiple credible fronts exist, Auto enters PMO portfolio discovery and asks once to confirm/add/remove/reprioritize the detected workstreams.
- That confirmed portfolio becomes Auto's identified goal for the current conversation and the lifecycle continues.
- Auto no longer asks the owner to invent one arbitrary "resultado concreto" merely because TASK.md contains several open items.
- A missing-goal question is reserved for cases where neither a coherent single goal nor a coherent candidate portfolio can be derived.
- Updated PMO, SKILL, AGENTS, native routing, README and change-management guidance to match this behavior.

## v2.44.1 — 2026-10-10

### Fixed

- Corrected two README lifecycle remnants found during the repository-wide standards review.
- Replaced the obsolete "PHDK auto / PMO workers" wording with PMO workers using bounded Auto execution semantics.
- Corrected the single-workstream guidance so explicit stages include Plan, while `PHDK auto` is presented as the complete lifecycle orchestrator rather than one middle implementation step.
- Fixed the repository's version helper scripts so they use `VERSION` when `package.json` is absent, matching PHDK's documented version source.
- Updated the optional metadata generator so it does not create application `src/`/`dist/` directories in the standards repository.
- Repository-wide review otherwise confirmed the v2.44.0 manifest/preflight/routing model is coherent.

## v2.44.0 — 2026-10-10

### Added

- Added `PHDK_PREFLIGHT.md` as the universal first step for all PHDK lifecycle commands.
- Preflight verifies active PHDK installation, installed/canonical version, manifest completeness, managed-rule presence, and stage-relevant skills/capabilities.
- Clean stale PHDK-owned standards may be conservatively synchronized before the requested command continues; dirty PHDK-owned changes are never force-overwritten silently.
- Added stage-aware recommended-capability checks for Capture, Plan, PMO, Auto, Integration Review, UAT/UAT Fix, and Check.
- Relevant already-installed capabilities should actually be used unless the user explicitly disables skills/plugins/connectors or a named capability.
- Added explicit availability states: AVAILABLE, BUILT-IN EQUIVALENT, MISSING OPTIONAL, MISSING IMPORTANT, DISABLED BY USER, and INCOMPATIBLE / OUT OF SCOPE.
- Added `PHDK_PREFLIGHT.md` and `SKILLS_REGISTRY.md` to the vendoring manifest so downstream projects receive the operational skill registry.

### Changed

- Reworked `SKILLS_REGISTRY.md` from a passive reference list into an operational, stage-mapped capability registry.
- Missing optional skills no longer matter silently; important missing capabilities are surfaced when they materially affect quality, while core PHDK remains self-contained.
- Plugin/connector installation or connection continues to follow host-product consent requirements; PHDK never falsely claims installation.
- Updated AGENTS, SKILL, native rules, execution scope, core command standards, Upgrade, onboarding, README, change management, and version metadata for the universal Preflight.

## v2.43.0 — 2026-10-10

### Added

- Added `PHDK plan` and `PHDK_PLAN.md` as the architecture and implementation-planning stage between Capture and PMO.
- Plan supports both greenfield target design and brownfield architecture reconstruction/convergence.
- Added canonical Plan artifacts: `SOLUTION_ARCHITECTURE.md`, `REPOSITORY_ARCHITECTURE.md`, `UX_ARCHITECTURE.md`, `IMPLEMENTATION_PLAN.md`, architecture decisions, and TASK integration.
- Defined solution/system, repo topology, data/integration/security, AI, testing/observability, conceptual UX/information architecture, migration, dependency and workstream-planning requirements.
- Brownfield Plan explicitly preserves valid existing architecture and produces Current State → Gap/Risk → Target State → Migration Step → Validation rather than imposing a clean-slate scaffold.

### Changed

- `PHDK auto` is now the end-to-end lifecycle orchestrator for one authorized goal: Capture → Plan → PMO/workstream execution → PMO Integration Review → UAT → UAT Fix → Check → in-scope Check remediation → delivery.
- Auto reuses current/coherent Capture and Plan artifacts rather than rerunning stages for ceremony.
- PMO workers no longer recursively invoke the `PHDK auto` command; they use bounded Auto execution semantics only for their assigned workstream.
- PMO now consumes `IMPLEMENTATION_PLAN.md` and architecture ownership/dependency boundaries as primary workstream inputs.
- Under Auto, in-scope AUTO-FIXABLE / FIXABLE WITH VALIDATION Check gaps are remediated without an extra approval round; material decisions/external/manual/out-of-scope findings remain explicit.
- Updated README, execution scope, routing/native rules, onboarding, task tracking, delivery, Check, Capture, PMO, upgrade, operating model and summary guidance for the new lifecycle.

### Lifecycle

```text
Capture → Plan → PMO/workstreams → Integration Review → UAT → UAT Fix → Check → remediation → delivery
```

## v2.42.1 — 2026-10-10

### Changed

- Rebuilt `README.md` as a product-facing introduction to PHDK instead of a release-history document.
- Added a clearer value proposition, problem statement, delivery lifecycle, command guide, PMO/Auto distinction, UAT/Check flow, conditional AI capabilities, human-control model, safety boundaries, installation guidance, and documentation map.
- Removed release-by-release "What changed" sections from the README.
- Added `CHANGE_MANAGEMENT.md` for release/adoption policy, versioning, downstream migration guidance, and high-level capability milestones.
- Kept `CHANGELOG.md` as the detailed technical release history.

### Documentation model

- `README.md` explains what PHDK is and how to use it.
- `CHANGE_MANAGEMENT.md` explains how PHDK versions/releases are managed and adopted.
- `CHANGELOG.md` records exact technical changes by release.

## v2.42.0 — 2026-10-10

### Added

- Added `PHDK PMO` and `PHDK_PMO.md` for portfolio/program orchestration across multiple owner-confirmed project workstreams.
- PMO discovers candidate fronts from Capture/requirements, TASK/STATUS, code, current git work, UAT and Check evidence, then asks the owner to confirm/add/remove/prioritize the active portfolio.
- Added PMO coordination artifacts: `PMO.md`, `PMO_WORKSTREAMS.md`, `PMO_DEPENDENCIES.md`, and `PMO_STATUS.md`.
- Added stable workstream IDs, scope/outcome/intent/requirements traceability, dependency graphs, path/component ownership, risk/blocker state, worker/branch evidence, and integration readiness.
- Added central PMO Integration Review for shared-file conflicts, API/schema/data/navigation contracts, version/changelog reconciliation, integrated verification, and one coherent candidate before UAT.
- Documented the lifecycle: Capture → PMO → Auto/workers → PMO Integration Review → optional/required human integrated review → UAT → UAT Fix → Check → approved remediation → Done.
- Added the single-workstream shortcut: Capture → Auto → UAT → UAT Fix → Check.

### Controlled delegation exception

- PMO is the only PHDK mode that may delegate coding/review work to runtime-supported in-session worker/subagents.
- Only the PMO orchestrator may delegate; workers may not create or coordinate additional agents.
- Every worker receives one owner-confirmed workstream contract with intent/requirements, scope/non-goals, ownership, dependencies, branch/worktree and verification expectations.
- No unattended/background/post-conversation workers, recursive delegation, schedules, agent queues, GitHub Actions, or external orchestration semantics are authorized.
- When subagent capability is unavailable, PMO reports that limit and coordinates workstreams sequentially rather than pretending parallel workers exist.

### Governance

- Portfolio selection and material decisions remain human-accountable.
- Proposed fronts stay PROPOSED until owner confirmation.
- Auto remains the single-goal/workstream executor; PMO owns portfolio coordination and integrated delivery.
- Worker success does not equal product acceptance; UAT evaluates the integrated candidate and Check evaluates standards conformance.
- Updated execution scope, development/versioning/upgrade rules, agent/native routing, onboarding, handoff/foundation, task tracking, Auto, Capture, UAT, Check, main delivery and README to recognize the PMO exception without reopening general delegation.

## v2.41.1 — 2026-10-10

### Fixed

- UAT no longer treats "0 FAIL" as equivalent to "nothing actionable" when acceptance remains incomplete.
- Every unresolved FAIL, BLOCKED, and MANUAL case now requires an explicit action card: what blocks acceptance, why it matters, who/what acts, where, how, ordering/prerequisites, closure evidence, next retest/command, and whether PHDK can do it now.
- `PHDK uat fix` now treats repository-local missing verification infrastructure as a removable blocker. Missing permitted isolated fixtures, fake adapters, auth stubs, in-process API harnesses, and similar local test plumbing should be created/repaired and the affected case rerun.
- Genuine external/manual/browser/provider/access blockers remain unresolved, but the report must provide an exact step-by-step owner/manual action plan instead of a status-only response.
- When no FAIL exists but BLOCKED/MANUAL cases remain, the response must explicitly explain that acceptance is incomplete because of those prerequisites/validations and recommend the ordered next actions.

## v2.41.0 — 2026-10-10

### Added

- Added `PHDK uat fix` as the explicit repair command for a completed UAT failure backlog.
- UAT reports now require an actionable diagnosis for every FAIL: observed/expected behavior, probable root cause, requirement/story/case links, affected component/files when identifiable, proposed repair, scope/risk, and exact retest.
- `PHDK uat fix` reads `UAT_REPORT.md` and `UAT_CASES.md`, repairs clearly in-scope fixable failures autonomously, reruns affected UAT/regression checks, and updates each defect to RESOLVED / STILL FAILING / BLOCKED.
- Active `PHDK auto` already includes this repair authority for in-scope UAT failures, so no separate command is required there.

### Boundaries

- New material product/security/infrastructure decisions remain blockers.
- Browser-only/manual/external/provider-write requirements are not silently executed.
- A standalone `PHDK uat` still validates/reports; repair requires `PHDK uat fix` unless Auto is already active.

## v2.40.0 — 2026-10-10

### Added

- Added `PHDK upgrade force` for authoritative replacement of the locally installed PHDK-owned standards surface from canonical upstream `main`.
- Force may overwrite dirty manifest-owned files under `phdk-standards/` and exact `PHDK-MANAGED` blocks.
- Force may remove obsolete files only when the previously installed manifest proves those paths were PHDK-owned.

### Safety boundary

- Product/application code, project requirements/docs, Capture artifacts, TASK/STATUS, intents, ADRs, hooks, workflows, package files, provider/repository settings, secrets, unknown extra files, and owner instructions outside managed markers are never overwritten by force.
- Bare `PHDK upgrade` remains conservative and stops on dirty PHDK-owned conflicts.
- Force supplies overwrite authority only; it does not authorize commit/push/merge/deployment or product work.
- Force verification must prove canonical PHDK byte equality and unchanged non-PHDK repository content.

## v2.39.1 — 2026-10-10

### Fixed

- Made `PHDK capture` explicitly explain its workflow to the user at the start.
- After repository investigation, Capture now states clearly whether Blocking/Material questions remain.
- When questions exist, Capture asks them under the gap-driven interview until the necessary information is resolved.
- When no questions remain, Capture explicitly says so instead of ending silently.
- On completion, Capture tells the owner that everything discovered/formulated was saved in the canonical requirements artifacts and lists/links `PROJECT_INTENT.md`, `PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md`, and `REQUIREMENTS_TRACEABILITY.md` for review.
- The completion summary must also identify remaining INFERRED or OPEN items without presenting them as owner-confirmed.

## v2.39.0 — 2026-10-10

### Added

- Added `PHDK capture` and `PHDK_CAPTURE.md` as the professional project discovery, intent/ethos capture, and requirements-reconstruction command.
- Supports both existing/advanced repositories and projects starting from zero.
- Existing-repo Capture investigates docs, intents, code, routes, schemas, tests, configuration, decisions, and relevant history before asking questions; code is treated as evidence, not automatic product truth.
- Added canonical project requirements artifacts: `PROJECT_INTENT.md`, `PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md`, and `REQUIREMENTS_TRACEABILITY.md`.
- Defined professional PRD domains, stable requirement/feature/intent IDs, provenance/confidence, acceptance signals, assumptions, open questions, and intent-to-UAT traceability.
- Added gap-driven interviewing: investigate first, rank missing information as Blocking/Material/Refinement, and ask only unresolved high-value questions until a coherent baseline exists.
- Integrated Capture as the strongest project-level requirements source for Auto, UAT, Check, onboarding, handoff, task tracking, and project-level intent.

### Clarified

- `PROJECT_INTENT.md` owns project-level ethos/purpose; `docs/intents/*-intent.md` continues to own later feature/bug/change intent.
- Existing implementation that conflicts with stated intent is recorded as a contradiction rather than silently promoted into a requirement.
- Capture produces requirements/documentation only unless the current request separately includes implementation or git delivery.
- `SPEC_INTERVIEW_PROMPT.md` remains a narrower reference; `PHDK capture` is the preferred full discovery/reconstruction workflow.

## v2.38.0 — 2026-10-09

### Added

- Added `AI_ADMIN_STANDARD.md` as a conditional standard for projects that actually use an LLM/AI provider.
- Defined applicability signals from provider API-key/config names, provider/model configuration, `packages/ai`, provider SDK references, and implemented AI workflows, without reading secret values.
- Required super-admin **Prompts** and AI consumption capabilities when AI applies.
- Defined the Prompts UI: left prompt/agent list and main editable Name, Personality prompt, Execution prompt, and Output JSON schema fields.
- Added persistent prompt/agent identity, revisions/audit, runtime schema validation, and usage attribution by prompt/agent ID and revision.
- Integrated the standard with `PHDK check`, design rules, technical stack, QA, routing, and the vendoring manifest.

### Conditional behavior

- Projects without AI do not receive these capabilities.
- A lone unused API-key placeholder with no established AI feature is UNKNOWN / DECISION NEEDED, not automatic product scope.
- Provider secrets are never stored in prompt records or exposed by the admin UI.

## v2.37.0 — 2026-10-09

### Added

- Added `PHDK check` and `PHDK_CHECK.md` for repository-wide compliance auditing against active applicable PHDK standards.
- The audit phase is read-only and produces `PHDK_CHECK_REPORT.md` with stable gap IDs, applicability, severity, standards references, repository evidence, remediation type, proposed fix, validation, dependencies, and execution order.
- Added compliance statuses COMPLIANT, GAP, PARTIAL, NOT APPLICABLE, UNKNOWN / DECISION NEEDED, and UNVERIFIED.
- Added remediation classes AUTO-FIXABLE, FIXABLE WITH VALIDATION, DECISION REQUIRED, and EXTERNAL / MANUAL.
- After presenting the report, PHDK asks exactly once whether the user wants the listed fixable gaps executed. A clear yes authorizes only those enumerated fixable gaps in the current report revision.
- Approved remediation runs autonomously under normal PHDK controls, then reruns `PHDK check` and reports the residual gap.

### Boundaries

- Conditional PHDK requirements are evaluated for applicability from project intent; absence of a non-applicable feature is not a gap.
- The audit does not silently upgrade stale PHDK, change product code, modify provider settings, or answer product decisions.
- DECISION REQUIRED and EXTERNAL / MANUAL findings remain outside a generic remediation yes.

## v2.36.1 — 2026-10-09

### Fixed

- Made project intent the mandatory upstream source for UAT user stories and acceptance cases.
- Added the required traceability chain: `Project Intent → User Story → Requirement / Acceptance Criterion → UAT Case → Evidence`.
- Added an Intent Alignment Gate: every applicable story must trace to intent, every case must link to a story, every applicable story must be covered, and UAT must not validate behavior outside or contrary to intent.
- Untraceable stories are marked `OUT OF INTENT` and excluded from acceptance counts rather than silently expanding product scope.
- UAT cannot conclude ACCEPTED unless intent alignment passes.

## v2.36.0 — 2026-10-09

### Added

- Added `PHDK uat` and `UAT_STANDARD.md` for autonomous, traceable user acceptance testing of the current candidate.
- UAT derives stable use/acceptance cases, writes `UAT_CASES.md`, executes every permitted acceptance channel available, and writes `UAT_REPORT.md` with PASS/FAIL/BLOCKED/MANUAL evidence and an ACCEPTED / NOT ACCEPTED / ACCEPTANCE INCOMPLETE conclusion.
- Integrated UAT with `PHDK auto`: applicable final UAT runs after the whole goal is implemented; in-scope failures are repaired and retested before final delivery.
- Added `UAT_STANDARD.md` to the vendoring manifest and routing instructions.

### Boundaries

- Browser/headless execution, screenshots, live app probes, destructive/live data operations, paid calls, provider writes, hosted CI dispatch, recurring monitoring, and background work remain excluded.
- Code inspection alone cannot make an unexecuted behavioral case PASS. Cases needing unavailable/excluded evidence are BLOCKED or MANUAL.
- Standalone UAT validates and reports the candidate; it does not silently broaden into unrelated product development.

### Verification

- Reviewed command routing, artifact schema, status semantics, Auto integration, manifest mapping, version metadata, and delivery behavior for the new standard.
- No browser, live-service write, provider administration, hosted CI, or background execution was used.

# CHANGELOG.md

## v2.35.0 — 2026-10-09

### Added

- Added the explicit `PHDK auto` command and `PHDK salir de auto` exit, with the canonical contract in `PHDK_AUTO.md`, the 27th manifest entry, and routing through active instructions, onboarding, and templates.
- Auto carries the entire identified current goal through development, final integrated verification, in-scope repairs, and normal versioned branch/PR delivery without human OKs between plans, features, stages, or release candidates. Progress updates do not end the task; completion refers to all agreed scope.

### Changed

- In Auto, write necessary test coverage with the code and run planned tests, including risk-triggered coverage, against the completed integrated candidate. Slice/foundation checklists specify final coverage rather than intermediate acceptance gates. Actual mandatory hooks and checks needed to diagnose implementation blockers remain effective when required; publication follows final verification.
- Include necessary non-semantic formatting repairs for a failing applicable gate, even in an existing workflow file when equivalence is established. Preserve workflow behavior and controls; this grants no CI execution, new workflow, or unrelated cleanup.
- Aligned interview, intent capture, handoff, foundation, QA, and task-tracking instructions so they do not pause an authorized Auto goal, request another go-ahead, or substitute an MVP/first release for an explicitly requested complete outcome.
- Preserve current scoped owner approval, resolve routine reversible implementation choices from existing conventions, and isolate genuinely unresolved material decisions while continuing independent authorized work. No PHDK-only human sign-off is added at final delivery.
- Auto explicitly replaces Developer Mode for the identified goal and uses the normal branch/PR repair and integration flow. It never inherits direct-main permissions or bypasses the control that stopped a prior direct push. Later explicit Developer Mode activation restores that separate eligible flow.

### Migration and limits

- Existing projects need a requested standards sync to receive the command and managed routing. Copying definitions, quoted commands, old tasks, and stored flags never activate Auto. Bare upgrade and narrower audit/local/branch/PR-only requests keep their scope limits.
- Auto operates only on the agreed goal in the active conversation. It adds no unattended/background/post-conversation execution, delegated agents, schedules, Actions, browser tests, live probes, provider writes, or new access. Existing hooks, actual review requirements, protections, and product security controls remain intact.
- Final evidence distinguishes completed code and local verification from remote integration, observed deployment state, and unverified application runtime. Existing GitHub-connected autodeploy remains permitted; a standards update does not change provider settings or installed projects automatically.

### Verification

- Reviewed fifteen behavioral scenarios covering complete multi-stage goals, final risk-based tests, necessary diagnostics and hooks, delivery without repeated approval, actual formal review, Developer Mode replacement, quoted commands, missing provider credentials, scope choices, exit/status continuity, missing goals, PR-only delivery, and necessary non-semantic workflow formatting.
- Verified all 45 canonical original blobs, 46 final files, 27 manifest mappings, new references/anchors and aliases, version/skill metadata, managed markers, unchanged prior history/hooks/scripts/archives/attributes, and diff whitespace. No application build, browser test, provider operation, or hosted CI dispatch was used for this documentation release.

## v2.34.0 — 2026-10-07

### Added

- Added `PHDK unlock`, an explicit interactive instruction to inspect PHDK blockers, reconcile documentary restrictions with the current owner's request, make bounded authorized repairs, and complete their normal versioned branch/PR delivery. Added `PHDK_UNLOCK.md` to the manifest and active routing, templates, and onboarding.
- Included existing native instruction files, managed blocks, owner prefaces, stale copied PHDK skills/standards, task records, actual hooks/toolchains, and fresh GitHub evidence in the blocker inventory. The current owner can replace local documentary exceptions; an old wrapper or task snapshot cannot veto that current request.

### Fixed

- Distinguished owner approval in the conversation from assistant source review and actual required formal review. A well-defined current request or an identified-task/PR "push to main", "merge", or "aprobado" can already supply owner approval. PHDK adds no requirement to repeat approval, attest to opening every diff line, or create a GitHub review event. Existing formal/named/independent review requirements remain binding.
- Classified sensitive changes by their actual diff and behavior. A package-format repair restoring login does not itself change authentication policy; an explicitly requested PHDK policy correction does not create another approval ritual for that same decision.
- Expanded bounded read-only provider diagnostics from logs to relevant service/deployment status, source/branch and non-secret configuration/watch metadata, and existing logs. A current "verifica Railway" request supplies this read scope without a second authorization phrase, Developer Mode, or unlock. An earlier code-task exclusion does not cancel the newer request. Kept the old log-section anchor for compatibility.
- Distinguished empty check/status evidence and unavailable ruleset visibility from an actual failed check or missing review. An already-authorized ordinary merge may be attempted with all known gates satisfied when that route preserves server enforcement; an actual rejection remains a blocker.
- Required checking overlapping PR content and version metadata before integration. A standards PR does not implicitly include a separate product fix or authorize merging every open PR.

### Migration and limits

- Existing installations need a requested sync or unlock to receive these instructions. Bare `PHDK upgrade` retains its synchronization-only contract and preserves genuine owner exceptions; explicit reconciliation/removal supplies that additional documentary scope.
- Unlock is not a shell executable, persistent flag, access credential, Developer Mode activation, or resumption of old product work. It preserves real hooks/checks/reviews/protections/security/access controls and provider-write boundaries. No browser tests, application probes, secret-value retrieval, provider deployment/configuration, Actions dispatch, recurring monitoring, or autonomous continuation is added.
- Existing GitHub-connected autodeploy remains permitted. A PHDK update does not change provider settings or establish that a deployment or application recovery succeeded.

### Verification

- Reviewed twelve policy scenarios covering conversation approval, actual formal review and hook failures, requested provider reads, unavailable deployed-version evidence, owner stops and new conversations, quoted commands, Developer Mode rejection, overlapping PRs, ruleset visibility, and removal of documentary exceptions. Clarified the ordinary server-enforced merge route after that review.
- Verified all 44 original Git blobs, 45 final source files, 26 manifest mappings, version/skill metadata, new Markdown references and diagnostic anchors, managed-rule markers, preserved history/hooks/scripts/archives, and diff whitespace. This documentation release uses source/reference and scenario review, with no application build or browser test.

## v2.33.0 — 2026-10-07

### Added

- Added `MAIN_DELIVERY_STANDARD.md` and its manifest/routing entry. A current implementation/fix/update request includes scoped versioned branch/PR delivery through the requested change and version verified on remote `main`, unless the user explicitly limits delivery or specifies another target.
- Included necessary normal integration conflict resolution, final version reconciliation, checks, required review, and merge within the same requested outcome; a branch push or open PR is not completion for a `main` target.

### Fixed

- Preserved current authorization across same-conversation status/link questions, clarifications, compaction, and assistant-written tracking updates. Task records cannot independently revoke permission; genuine owner stops remain binding, and old records cannot resume work in a new conversation.
- Removed PHDK's universal human-review gate for ordinary normal delivery. Human review remains required for high-risk changes and stricter owner/repository rules, with truthful review evidence and all existing controls intact.
- Reconciled QA/versioning wording: use the repository's version source, prepare the version on the working branch, and do not add another bump, version-only commit, or push merely because already-versioned changes were merged.
- Separated code integration from deployment. Existing provider GitHub autodeploy is allowed; PHDK must not disable it or add dummy never-matching watch filters to enforce restrictions on autonomous work. Observed deployment blockers/statuses are reported separately without granting provider configuration writes; valid service-specific filters and intended skips for unaffected services remain normal.

### Migration and limits

- Existing installations require a requested sync and reconciliation of conflicting assistant-written task-state snapshots. Preserve genuine owner restrictions and existing hooks/protections; a standards update does not change GitHub/Railway settings.
- Developer Mode retains explicit activation, its narrow direct-main path, and immediate hard stops. Bare `PHDK upgrade`, read/audit/plan requests, and explicit local/branch/PR-only requests retain their scope limits. No browser testing, live probes, provider writes, Actions dispatch, scheduled work, or autonomous continuation is added.

### Verification

- Verified all 43 original Git blobs, the 25 manifest mappings, version/skill metadata, new Markdown references, managed-rule markers, preserved history/hooks/scripts/archives, and diff whitespace.
- Reviewed 11 policy scenarios covering complete delivery, task continuity, real stops, new conversations, narrower targets, required review/hooks, integration conflicts, squash/version handling, Developer Mode failures, and provider deployment evidence. Clarified valid service-specific filters and the existing bounded read-only log exception after that review.

## v2.32.0 — 2026-10-06

### Added

- Added explicit, temporary `PHDK Developer Mode`, activated by `PHDK modo developer` or `PHDK Developer Mode` and exited with `PHDK salir de developer mode` or the end of the active conversation.
- Authorized the requested edit, repository-standard version bump, applicable local checks, version-prefixed commit, and fast-forward push to `main` for eligible small, low-risk tasks requested while the mode is active. Existing deployment connections may react to that push; provider deployment commands and configuration remain excluded.
- Added `PHDK_DEVELOPER_MODE.md` to the vendoring manifest and routed its commands through the skill, managed rules, onboarding, and task/git standards.

### Fixed

- Replaced the blanket ban on live-service logs with bounded read-only retrieval of existing logs through an authorized provider API/CLI/connector for a current requested diagnosis. This permission is independent of Developer Mode and requires finite target/time/result/timeout bounds and redaction of sensitive data.
- Kept authentication, authorization, secrets, data/migrations, payments, infrastructure, permission-policy changes, and other high-risk work in the normal review flow. Failed applicable checks, rejected/non-fast-forward pushes, and unsatisfied controls stop the direct-main flow; no hook/protection bypass, settings changes, forced updates, or automatic retry.
- Removed the legacy Finetuning flag as a separate direct-main permission and reconciled bootstrap text that could otherwise revive old missions. No activation persists in task files, flags, hooks, or later conversations.

### Verification

- Validated the skill metadata, version consistency, all 24 manifest mappings, new Markdown references, managed-rule markers, and diff whitespace. Existing source blobs and preserved history/hook/script files were checked against the canonical base.
- Reviewed 13 fresh-context policy scenarios covering activation, task boundaries, low/high risk, failed checks, protected or advancing `main`, exit, log reads, and unavailable hooks. Reconciled the normal verification-repair wording with Developer Mode's stop rule.

### Migration

- Existing projects need an explicitly requested standards sync to receive the new manifest entry and managed rules. A standards update never activates Developer Mode. Policy changes retain normal review even when they are documentation files.
- No agents, Actions, schedules, monitoring streams, browser tests, application probes, provider writes, or external configuration are introduced. Updating these instructions does not disable existing external automation.

## v2.31.1 — 2026-10-04

### Interactive-only execution; no delegated agents or GitHub Actions

- Removed active-session Mission Autopilot and bounded delegated-agent permissions. One assistant handles the current explicit user request; no subagents, teams, queues, autonomous reviewers, background work, or post-session continuation.
- Made audits read-only and commit/push/merge/release authority dependent on the current request. An explicit implement-and-merge instruction includes its necessary git/PR steps; old task files and checklists do not grant authorization.
- Prohibited creating, enabling, dispatching, rerunning, or scheduling GitHub Actions/hosted CI, in addition to cron jobs, bots, recurring backups, monitoring and maintenance loops.
- Kept relevant synchronous local code checks and isolated non-browser tests; no persistent watchers or automatic follow-up work.
- Preserved stricter owner controls during standards upgrades and clarified that updated instructions do not terminate external agents, revoke credentials, disable existing schedulers, or enforce remote branch protection.
- Updated the execution/routing, skill, managed native rules, task/slice, onboarding, summary, and git/version guidance for this boundary.
- Retained `EXECUTION_SCOPE.md` and the managed rules in the existing vendoring manifest. No workflows, agents, or schedules were added.

### Migration

The canonical `main` version becomes v2.31.1 after this patch is merged. Existing projects require their own explicitly requested standards sync. Their installed automation and external settings are not changed by updating this repository.

### Preserved history

The complete previous changelog is preserved byte-for-byte in [ORIGINALS/CHANGELOG-through-v2.31.0.md](ORIGINALS/CHANGELOG-through-v2.31.0.md). It describes historical releases only; its former autonomy or automation permissions are superseded by the current `EXECUTION_SCOPE.md`.
