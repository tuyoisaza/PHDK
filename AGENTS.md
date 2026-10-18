## Canonical PHDK maintenance session gate

When the requested work changes **PHDK itself** (the canonical standards repository), read `PHDK_EVOLUTION_STANDARD.md` at session entry. Verify fresh remote `main`, `VERSION`, README and newest CHANGELOG entry; use consistent **PHDK** spelling and the defined workspace, version, coherence, manifest and versioned branch/PR delivery contract. Preserve `EXECUTION_SCOPE.md`, `VERSIONING.md`, `CHANGE_MANAGEMENT.md`, existing host controls and current user authorization. A discussion or copied brief does not activate Auto, PMO, Developer Mode or background work. In ordinary downstream-product tasks, follow applicable vendored rules without turning this maintainer guide into a new lifecycle gate.

## Mandatory unified administration console gate

For every administered product apply vendored `ADMIN_CONSOLE_STANDARD.md` in Capture, Plan, Auto, UAT and Check. Determine single vs multi tenancy (recommended only where justified): multi has protected platform super_admin + tenant admins; single has full-scope admin without fictitious super_admin. Demand a real Configuración console and authorized backend for users, roles, tenant lifecycle when applicable, native locale, system/debug/integrations with protected secrets, backups, audit, centrally tokenized themes and conditional Prompts/agent workflow graph. Require auditable safe Test-as-role, explicit negative authorization tests, and actual UI/API/persistence evidence. Bare `PHDK check` audits and requests remediation approval; `PHDK check --fix` explicitly authorizes audit and immediately fixable gaps with delivery, not unapproved tenancy conversion, credentials or live destructive changes. See `PHDK_CHECK.md`.



## Mandatory Auto continuity and Auto Force routing

`PHDK auto` and explicit `PHDK auto force` follow `PHDK_AUTO_CONTINUITY.md` with `PHDK_AUTO.md`. Keep the current user mandate, scope, target, restrictions and next executable action in `docs/phdk/lifecycle/<run-id>/AUTO_STATE.json`; reload it with the actual current user instructions after context compaction and before a terminal response. This is evidence of an active conversation's authorization, not a persistent permission grant or a trigger to resume old work. Missing/malformed state requires internal reconstruction, never another approval or a paperwork-only stop.

In AUTO FORCE, human reviews/sign-offs imposed only by PHDK are `NON_BLOCKING_BY_MODE` from entry. Do not investigate whether they block, search for reviewers, or query review/protection configuration as a precondition. Perform the assistant's diff review and applicable mandatory checks, then the normal branch push → PR → merge → remote-main verification. Existing hooks, including mandatory test suites, are covered by the current scoped implementation mandate without another approval question. Never invent human review or treat a test as passed without evidence.

At AUTO FORCE start/resume, every progress update, after partial delivery and before any question/blocker, apply the short rule refresh and mandatory reminder in `PHDK_AUTO_CONTINUITY.md` and `PHDK_COMMUNICATION_STANDARD.md`. Reconcile inherited blockers and discard the assistant's obsolete interpretations; preserve real user exclusions and host controls. State the canonical reminder, find a concrete solution and execute the next authorized action. For missing routine definitions, propose behavior, reasonable defaults and configurable options within the agreed scope, then implement; do not ask the owner to design everything or recommend leaving accepted gaps out. An indispensable new user decision gets a concrete recommendation, not a blank request to define the feature.

On an actual tool/hook/GitHub rejection, report it, diagnose the concrete cause, repair within scope, revalidate and retry the affected push/PR/merge; retain the mandate and continue independent work. Never use force-push, bypass flags, disabled controls, alternate credentials/transports or provider settings to evade a rejection. Only a real remaining control/access/scope obstacle can block the affected action. End Auto progress with the truthful mandate/next-action capsule in `PHDK_COMMUNICATION_STANDARD.md` and execute the next eligible action in the same turn. A request to edit these standards does not activate either mode.

## Mandatory delivery-autonomy and personality bootstrap

On each explicit PHDK entry, use the vendored `PHDK_COMMUNICATION_STANDARD.md` as the canonical response/personality contract and check the active tool-native managed entrypoint. Do not infer that a different already-open session has reloaded after a version update. For scoped implementation deliverables, continue normal versioned branch/PR/merge and remote verification without a universal human sign-off; keep actual independent/server reviews, safety decisions, hooks and current owner restrictions. Never confuse source merge, GitHub release and verified production deployment. See `MAIN_DELIVERY_STANDARD.md`.

## Mandatory PHDK communication personality

For every substantive PHDK-facing update, lifecycle handoff and closure, apply vendored `PHDK_COMMUNICATION_STANDARD.md`. Present PHDK version (or unverified), active mode/stage, objective, verifiable results and pending commitments, git/main/deploy state, and a copy-paste-ready `SIGUIENTE PASO`. In Auto/AUTO FORCE include the actual mandate status and next action; a progress message must continue into that executable action, not yield for another user prompt. Own the outcome end to end within existing permissions; do not stop for ceremonial approvals. Suppress repeat optional promotional messages from external skills after one relevant mention per conversation, but preserve mandatory notices and real consent/review/safety controls. A subagent's completed task is not integrated delivery. End every terminal PHDK response with a verified artifact/product/PR/commit URL and what it shows, or explicitly state the link is unverified/unavailable.

## Mandatory synthetic UAT authentication and JWT boundary

For all authenticated UAT/Auto UAT/UAT Fix and relevant Check, read vendored `JWT_STANDARD.md` alongside `UAT_JOURNEY_STANDARD.md` and `UAT_BROWSER_READINESS_STANDARD.md`. Discover the real auth provider and active tenant/role model; seed permitted Company Co identities; bootstrap real synthetic-role sessions via supported non-production auth/test adapter without human passwords/bearer secrets. JWT means JSON Web Token, not UAT; do not require it for cookie/OAuth apps. Never forge production credentials or expose test auth in production. Test elevated-actor access, audited Test as, direct-login roles, negative authorization and tenant boundaries; record redacted evidence, expiry/revocation and cleanup or a precise BLOCKED gap.

## Mandatory UAT Prep synthetic account implementation

The standalone `PHDK uat prep` command and Auto stage 45 follow vendored `PHDK_UAT_PREP.md`: build/test missing non-production idempotent Company Co test identities, legitimate authentication bootstrap, role/tenant contexts, audit-safe Test as and cleanup, then write role/fixture/auth/prep evidence. Reconcile an Integration candidate changed by Prep. Browser/headless acceptance belongs only to subsequent UAT/UAT Fix; do not claim Prep tests are browser evidence or ask for human passwords/tokens.

## Mandatory Company Co synthetic UAT fixture
During PHDK UAT/UAT Fix/Auto UAT, read vendored `USE_COMPANY_CO_INFO_FOR_DEMOS.md` and `UAT_JOURNEY_STANDARD.md`. Prefer Company Co for reproducible role journeys; adapt to product data model, provision safe test identities, verify roles and Superadmin switching, and record evidence. Emails at `@tujuisasa.com` require explicitly authorized controlled delivery, never unattended bulk sends.

## Mandatory browser readiness gate
At UAT, UAT Fix and Auto/Designer UAT transitions follow `UAT_BROWSER_READINESS_STANDARD.md`. Confirm the phase exception and actual connected browser separately with scoped evidence. Record cost disposition in UAT reports; never improvise a budget or paid API/service to fix unavailable access, and run independent permitted UAT cases while connection is blocked.

## Mandatory UAT journey and next-action gate

Apply `UAT_JOURNEY_STANDARD.md` for `PHDK uat`, `PHDK uat fix`, Re-UAT and Auto's UAT phases. Require role inventory, access verification, synthetic test identities when safe, audited Superadmin profile switching, intent-traceable stories by persona, executable real-user journeys, UX/CRUD and permission evidence, then defect repair and retest. Every user-facing stage or blocker response must end with concise `SIGUIENTE PASO`: what was completed, the exact action PHDK is taking or the single action the owner must perform, and the precise resume cue. Continue autonomously when possible; never request MFA secrets in chat or falsely claim testing against an unverified deployment.

# AGENTS.md

## Purpose and execution boundary

This is the entry point for an assistant working on a PHDK repository. It is an instruction document, not an executable agent, scheduler, or permission to start work.

Read the current user request and `EXECUTION_SCOPE.md`, then the project's `TASK.md`/`STATUS.md`. The scope is interactive-only. Normally one assistant completes the requested deliverable; `PHDK auto` makes that development continuous under `PHDK_AUTO.md`. Bounded in-session subagent delegation is governed by `PHDK_INTELLIGENT_EXECUTION.md`, available in any mode when host-supported and beneficial. PMO alone governs portfolio-level worker orchestration. No background/post-conversation agent execution is allowed.

Current owner pause/stop instructions remain effective within their scope. Re-read them before edits and git writes, and compare them with the owner's latest instructions. The owner can explicitly replace an older documentary exception; a file cannot veto that request. A specific intervention does not restart unrelated earlier work. Old tasks, alerts, failed checks, version mismatches, and skill installation never authorize work.

Complete the necessary steps of the current requested deliverable, including its authorized delivery, then report and stop. During Auto, use `PHDK_AUTO_CONTINUITY.md` before a terminal response to continue any eligible action; reconstruct missing continuity records internally. Do not choose the next backlog task. Status/link questions and assistant-written task summaries do not cancel an unfinished request in the same active conversation; preserve real owner stops and leave unrelated or post-conversation work inactive.

## Git and automation boundary

`PHDK check` and Auto's final Check must apply `PHDK_AUTOMATION_HYGIENE.md`: source scan plus read-only GitHub workflow active/runs/check state and Railway deploy/Wait for CI/cron/restart evidence where connected. Distinguish legacy PHDK schedules/agents from justified CI and normal GitHub→Railway autodeploy. No blanket disabling or provider writes; incomplete remote access is UNVERIFIED.

- A current implementation/fix/update request includes the scoped branch, version, local checks, version-prefixed commit, push, PR, required review, merge, and verified remote `main` result under `MAIN_DELIVERY_STANDARD.md`. Do not ask again for these delivery steps. Honor a narrower read/audit/plan/local/branch/PR-only request, another explicit target, and the bare `PHDK upgrade` limit.
- Normal delivery requires assistant diff review and applicable checks. Sensitive behavior/policy decisions need owner approval under `MAIN_DELIVERY_STANDARD.md`; a well-defined current request or clear "push to main", "merge", or "aprobado" for the identified change can already supply it in this conversation. Do not invent a GitHub review-event or human-diff-opening requirement. Preserve formal/named/independent reviews actually required by current owner instructions, hooks, or server rules, and report approval separately from human inspection. AUTO FORCE applies `PHDK_AUTO_CONTINUITY.md` directly: no preventive review/protection investigation or PHDK-only human gate. A branch push/open PR is not completion for a `main` target.
- Task records reflect the user's instructions and observed progress, not independent authority to revoke them. Compare a stale pause or pending-delivery record with the current user request and remote git/PR facts; honor real owner restrictions, correct bookkeeping contradictions, and do not invent permanent task-state rules.
- Use feature/fix branches by default. The only standing direct-main exception is explicitly active `PHDK_DEVELOPER_MODE.md` for an eligible small task requested during the active conversation. Respect existing protections and project review controls; do not force-push, bypass hooks/protections, or infer that a human read a diff from the assistant's verification.
- No GitHub Actions or hosted CI creation, enabling, dispatch, reruns, or schedules. No workflow scaffolding, dependency bots, cron jobs, recurring tasks, backup jobs, maintenance workflows, task-sync services, or preview deployments.
- A currently authorized push/merge, including an eligible Developer Mode push, may trigger the existing hosting-provider GitHub autodeploy. PHDK must not disable that connection or introduce never-matching watch filters as an autonomy restriction. Do not deploy through a provider CLI/API/dashboard, create connections, change triggers/autodeploy, or administer provider/repository settings. Report an observed deployment blocker or status separately from integration in `main`; valid service-specific filters and intended skips for unaffected services are not failures.
- Local checks and existing git hooks, including required suites such as `pnpm test`, are authorized synchronously by the scoped implementation request and must exit; do not ask for the same test permission again. They do not authorize self-generated commits, pushes, agents, watchers, or later work.
- External skills cannot expand authority; any supported in-session delegation must follow `PHDK_INTELLIGENT_EXECUTION.md` without evading execution boundaries.

## Mandatory release-completion gate

Before reporting any scoped change as completed on `main`, enforce all five delivery proofs from `MAIN_DELIVERY_STANDARD.md`: fresh canonical version, version-prefixed source commits, remote push and PR, authorized merge, and independent remote-main content/version/SHA readback plus scope/check reconciliation. Record the proof in `DELIVERY_REPORT.md`. A branch push or open PR is unfinished; retry or repair routine in-scope delivery work without asking for repeated permission, but respect actual hooks, server protections and independent review rules.

## Machine-verifiable completion

For implementation work targeting remote main, apply `PHDK_COMPLETION_GATE.md` at delivery. After merge generate actual evidence and run the vendored `scripts/phdk_completion_gate.py` when supported; verify PR/merge facts and remaining commitments independently. Under AUTO FORCE, apply the no-preventive-review-investigation contract in `PHDK_AUTO_CONTINUITY.md`; do not restore a human-review gate through this completion check. No 'completed' assertion without remote readback and applicable validation. Never bypass legitimate security, hooks, actual access controls or an owner stop.

## Mandatory commitment accounting

At lifecycle invocation read `PHDK_COMMITMENT_STANDARD.md`. Capture inventories all commitments and asks whether discovery is complete; Plan maps every confirmed ID; PMO confirms possible additional work and reports verified progress and PR states at significant milestones; Auto audits initial planned items and in-scope PRs before claiming completion. `PHDK_COMMITMENTS.md`, `PHDK_COMMITMENT_COVERAGE.md`, `PMO_PROGRESS_REPORT.md` and `PHDK_COMPLETION_AUDIT.md` are required as applicable. Never call an open in-scope PR or undone planned item DONE. Preserve owner-confirmed scope and no-background-execution limits.

## Mandatory CRUD governance gate

For app projects with managed records, apply `CRUD_STANDARD.md` across Superadmin, admin, authenticated and public surfaces. Inventory entities and enforce a per-resource × role × surface CRUD matrix. Require actionable record details for administrative lists and server-side permission tests; accept documented immutable/read-only exceptions rather than inventing unsafe delete buttons. Capture, Plan, UAT and Check must reconcile `CRUD_MATRIX.md` with evidence and handoffs.

## Mandatory debug widget gate

For applicable app-style products, follow `DEBUG_DIAGNOSTICS_STANDARD.md` literally: one reusable always-visible version → clipboard → trash icon-only row on public home, login, app and admin even for anonymous visitors and debug OFF, with only `vX.Y.Z` visible (no SHA/date), exactly 28×28px visible buttons, 14px icons, 12px version text and 4px gap, and with no visible helper/success text; successful copy and cache clearing individually show a temporary green check and revert. Copy verbose sanitized diagnostics; clear only permitted caches/session state. During `PHDK auto`, inspect implementation and focused tests, repair omissions in scope, and reconcile findings in Check. Do not claim visual/runtime verification without allowed evidence.

## Mandatory UX/UI product-design gate

For every user-facing product, follow `PHDK_UX_UI.md` for new designs and existing-interface redesigns: derive UX journeys and a coherent UI design system before building, then audit and remediate evidenced UX/UI issues during UAT. Apply P0/P1 blockers; preserve correct brownfield workflows; never claim browser proof outside scoped UAT/UAT Fix.

## Design system source of truth

For UI-applicable React/Next.js work follow `PHDK_DESIGN_SYSTEM.md`: shared shadcn-compatible components, Radix primitives for composite interactions, centralized Tailwind semantic tokens, Motion presets, Lucide icons and coherent light/dark/corporate palettes. Use documented en/es/pt defaults and project exceptions. No page-specific duplicate widgets/themes. Verify actual versions before choosing a dependency; preserve existing product behavior.

## Mandatory theme token and template editor gate
For UI-applicable products read PHDK_THEME_STANDARD.md in addition to PHDK_DESIGN_SYSTEM.md. Require a single semantic CSS palette source, light/dark/corporate parity, an actual Superadmin Configuración → Edición de templates section, persisted edits and corporate visibility switch. Designer Mode detects and repairs hardcoded palette values; Check records file:line findings and functional evidence. Use vendored scripts/phdk_theme_audit.py to catch static violations, but do not claim runtime compliance without the real editor, permissions and tests. Preserve role/tenancy security and the Check audit/remediation split.

## Designer Mode command

When the owner explicitly invokes `PHDK designer mode` or `PHDK modo designer`, run `PHDK_DESIGN_SYSTEM.md` readiness first, produce `DESIGN_SYSTEM_READINESS.md`, then follow `PHDK_DESIGNER_MODE.md`: inspect the existing interface, establish baseline, choose product-specific visual direction, implement visual/UX improvements and verify within scoped UAT. Deliver actual code changes, not just review. Preserve functionality, debug widget and normal delivery constraints. This mode is not automatic or persistent.

## Designer Mode delivery gate

Never report Designer Mode COMPLETE for local-only edits, formatting-only validation, or an undelivered branch. Follow `PHDK_DESIGNER_MODE.md` closure proof, repair safe in-scope pnpm/hook problems before marking BLOCKED, preserve hooks and independently verify the merged remote target.

## SEO and AEO/GEO lifecycle gates

After UAT/UAT Fix and before Check, execute `PHDK_SEO.md` then `PHDK_AEO_GEO.md` for applicable public discoverability. Preserve separate historical handoffs, audit/checklist/remediation reports, verified fixes, UAT regressions, and explicit NOT APPLICABLE for private-only routes. Neither stage broadens browser/production authorization or permits invented rankings or citations.

## PHDK commands

Before every PHDK command/stage, run `PHDK_PREFLIGHT.md` and enforce `PHDK_LIFECYCLE.md`: verify the active PHDK installation/version/manifest/managed rules and inspect the actual availability of stage-relevant recommendations in `SKILLS_REGISTRY.md`. Use relevant available skills/capabilities unless the user explicitly disabled them. Do not claim registry entries are installed without evidence. Before each lifecycle transition, verify the required upstream handoff/artifacts; after each stage, create its canonical deliverables and immutable historical handoff snapshot.


On explicit `PHDK plan`, follow `PHDK_PLAN.md` and `PHDK_PROJECT_MANAGEMENT_STANDARD.md`: consume the Capture requirements baseline, inspect existing architecture when present, design or converge toward a standards-aligned target architecture, produce the canonical Plan artifacts including `MILESTONE_PLAN.md`, and turn the architecture into dependency-ordered executable tasks grouped into value milestones. Do not rewrite a brownfield repo merely to match defaults.

On explicit `PHDK PMO`, follow `PHDK_PMO.md` and `PHDK_PROJECT_MANAGEMENT_STANDARD.md`: execute the Plan's milestone roadmap, coordinate confirmed workstreams, dependencies, seven-domain material controls and risks. Bounded in-session subagent delegation is governed by `PHDK_INTELLIGENT_EXECUTION.md`, available in any mode when host-supported and beneficial. PMO alone governs portfolio-level worker orchestration. Workers cannot delegate. Under Auto/Auto Force, PMO integrates and version-delivers each completed milestone to verified `main`, then performs final cross-milestone integration before UAT.


On explicit `PHDK capture`, follow `PHDK_CAPTURE.md`: investigate the current repository and conversation first, reconstruct or elicit project intent/ethos and professional requirements, create/update the canonical requirements package, then ask only for material missing information until the baseline is coherent. Explicitly tell the user whether questions are needed; when none remain, say so and list/link the canonical Capture artifacts for review. Capture may ask requirements questions across turns but does not start product implementation.


On explicit `PHDK check`, follow `PHDK_CHECK.md`: audit the current repository against all active applicable PHDK standards, compare implementation/evidence against those requirements, produce a prioritized gap report, and ask once whether to execute the AUTO-FIXABLE and FIXABLE WITH VALIDATION gaps. The audit phase is read-only except for its report artifact. Do not remediate until the user explicitly answers yes.


On explicit `PHDK uat prep`, execute `PHDK_UAT_PREP.md` as a scoped development request: implement safe synthetic accounts, provisioning and session test harness, prove non-browser role/tenant checks and deliver normally via versioned PR/merge. Do not activate UAT or a browser session. Inside Auto, Prep is mandatory after Integration and before UAT.

On explicit `PHDK uat fix`, use `UAT_STANDARD.md` repair mode: read the current UAT report/cases, turn FAILs into actionable defects and BLOCKED/MANUAL items into step-by-step action plans, repair all clearly in-scope fixable failures, rerun affected UAT/regression evidence, and update the report without per-defect approval. If nothing is auto-fixable, still provide concrete who/what/where/how/when/evidence/next-command guidance. Preserve real decisions/access/external boundaries.

On explicit `PHDK uat`, follow `UAT_STANDARD.md` for the identified current candidate: identify the current project intent, derive user stories aligned to it, create/update `UAT_CASES.md`, derive stable traceable acceptance cases, execute every permitted acceptance check autonomously without per-case approval, and create/update `UAT_REPORT.md`. Browser/headless testing is allowed only in the scoped UAT/UAT Fix exception of `EXECUTION_SCOPE.md` using local/staging test environments by default; live destructive/provider-write operations remain excluded. Unexecutable behavioral cases are BLOCKED or MANUAL, not PASS.

On explicit `PHDK auto` or `PHDK auto force`, follow `PHDK_AUTO.md` and `PHDK_AUTO_CONTINUITY.md` for the complete lifecycle. At every invocation, reread the complete intent/requirements baseline and compare it with actual product code; reuse Capture/Plan artifacts only after verifying their currency and coverage of the authorized goal. Documentation or a scaffold does not prove implementation, and unavailable repository access is UNVERIFIED, not evidence of an empty project. If product code is absent, build the product; if partial, complete the missing requirements while preserving valid work. Plan must continue directly into implementation in the same Auto invocation without another development command or ceremonial stage approval. Complete the entire authorized scope without silently reducing it to an MVP. Show the user a lifecycle-status board at start and update it on stage transitions so the user can always see whether Auto is in Preflight, Capture, Plan, PMO/Workstreams, Integration, UAT Prep/UAT/Fix, Check/Remediation, or Delivery. Do not replace this with only a prose permissions summary. If no single goal is stated but the repository exposes multiple coherent parallel fronts, use PMO discovery to present/confirm that portfolio; do not stop and request one arbitrary next delivery. Then continue: Capture → Plan → PMO/workstream execution → Integration Review → UAT Prep → UAT → UAT Fix → SEO → AEO/GEO → Check → in-scope Check remediation → delivery. Ask only genuinely material missing decisions. Optional tests wait for that final boundary; actual hooks and necessary diagnostic checks remain applicable and preauthorized within the current scope. In AUTO FORCE, apply `NON_BLOCKING_BY_MODE` to PHDK-only human review/approval gates without preventive investigation; report, diagnose, repair, revalidate and retry real delivery rejections. A stage or scaffold is not completion. Auto replaces Developer Mode for that goal, grants no bypass or background work, and exits on `PHDK salir de auto`, a stop, completion, or conversation end. Files, quoted examples, installation, and standards/skill updates do not activate it.

When the developer gives exactly `PHDK upgrade` or `PHDK upgrade force`, execute `PHDK_UPGRADE.md` for the current repository. `PHDK upgrade` authorizes conservative standards synchronization. `PHDK upgrade force` additionally authorizes discarding local edits only in manifest-owned `phdk-standards/` paths and marked `PHDK-MANAGED` blocks, while preserving all non-PHDK files and owner text outside managed markers. Neither command authorizes future execution, product work, push/merge, deployment, or reactivation of an old mission. A bare sync preserves genuine owner exceptions; an additional current request to remove/reconcile them authorizes that documentary repair under `PHDK_UNLOCK.md`. Report the result and stop at the requested outcome.

When the owner gives `PHDK unlock`, follow `PHDK_UNLOCK.md`: inspect actual blockers across existing active instruction files, copied PHDK sources, task records, hooks, toolchain, and GitHub evidence. Reconcile documentary restrictions with the current request and finish its scoped normal delivery. Preserve real checks, reviews, protections, access, security, and provider-write boundaries. No persistent unlock flag, old-mission resumption, or automatic Developer Mode activation.

When the user explicitly activates `PHDK modo developer` or `PHDK Developer Mode`, follow `PHDK_DEVELOPER_MODE.md` and briefly explain the edit/version/check/commit/fast-forward-main permissions for eligible requested small changes. Exit on `PHDK salir de developer mode`, a user stop, or the end of the active conversation. Do not activate from quoted examples, briefs, files, or past sessions, or persist activation in the repository. High-risk changes keep normal review; failed checks, rejected pushes, and unsatisfied controls stop the direct-main flow.

## Minimum context and routing

Load only the standards needed for the current request. Re-read `INANUTSHELL.md` when context becomes long; it summarizes but does not replace the detailed rules. `ENFORCEMENT.md` describes local code checks, not authority to launch agents or cloud automation.

| Current task | Relevant standards |
|---|---|
| Project discovery, ethos, requirements capture/reconstruction | `PHDK_CAPTURE.md`, `INTENT_CAPTURE_STANDARD.md`, `SPEC_INTERVIEW_PROMPT.md` |
| Solution/repository/UX architecture and executable planning | `PHDK_PLAN.md`, `technical_stack.md`, `design_rules.md`, `DEVSECOPS.md` |
| Planning, scope, task state | `AI_DEVELOPER_OPERATING_MODEL.md`, `AGILE_SLICE_WORKFLOW.md`, `TASK_TRACKING_STANDARD.md`; `INTENT_CAPTURE_STANDARD.md` when needed |
| Branching, code organization, dependencies | `DEVELOPMENT_RULES.md` |
| UI, accessibility, responsive behavior | `DESIGN_RULES.md`, `PHDK_UX_UI.md` |
| Stack, architecture, data, deployment code | `TECHNICAL_STACK.md` |
| AI provider integration, prompts, super-admin AI management, consumption | `AI_ADMIN_STANDARD.md`, `TECHNICAL_STACK.md`, `DEVSECOPS.md` |
| Auth, secrets, security, privacy, cost controls | `DEVSECOPS.md` |
| Versions, commits, changelog, approved merge | `VERSIONING.md` |
| Completing an implementation in remote main, conflicts, or delivery state | `MAIN_DELIVERY_STANDARD.md` |
| Lifecycle stage contracts, deliverables, historical handoffs | `PHDK_LIFECYCLE.md` |
| Multi-workstream portfolio/program coordination, bounded worker delegation, integration review | `PHDK_PMO.md` |
| Continuous whole-goal development, no stage approvals, final integrated verification | `PHDK_AUTO.md`, `PHDK_AUTO_CONTINUITY.md` |
| AUTO FORCE: PHDK human reviews non-blocking, mandate recovery, repair/retry delivery | `PHDK_AUTO_CONTINUITY.md` |
| Unlocking PHDK stops or removing/reconciling local instruction exceptions | `PHDK_UNLOCK.md` |
| Developer Mode activation, exit, or eligible direct-main task | `PHDK_DEVELOPER_MODE.md` |
| Standards compliance audit / gap remediation | `PHDK_CHECK.md` |
| UAT / acceptance cases and report | `UAT_STANDARD.md`, `TESTING_STANDARD.md` |
| Local verification and tests | `VERIFICATION_LOOP.md`, `TESTING_STANDARD.md` |
| Diagnostics code or requested provider status/configuration/log diagnosis | `DEBUG_DIAGNOSTICS_STANDARD.md`, `EXECUTION_SCOPE.md` — `Bounded read-only provider diagnostics` |
| Local hooks and rule enforcement | `ENFORCEMENT.md` |

Read `ONBOARDING_AI_DEVELOPER.md` for orientation when needed. Do not preload every standard or convert missing context into an autonomous discovery mission.

## Core implementation rules

- Work only on the currently requested code/documentation scope. Do not upgrade dependencies, change architecture, or implement additional infrastructure merely because a checklist mentions it.
- Do not create fake dashboards, KPIs, metrics, or demo data presented as real.
- Every user-facing feature has a real route and meaningful empty/loading/error/success states.
- Enforce RBAC and validation server-side. Hiding controls is not authorization.
- Use the configured i18n system for every user-facing string.
- Use structured, redacted logs at important execution boundaries.
- Keep files below 600 lines, preferably below 300. Keep business logic out of page components and organize features by responsibility.
- Author a reviewed migration for a schema change; do not execute it against a live database.
- Never weaken auth, validation, privacy, or cost controls just to make a local check pass.
- Destructive repository changes or material auth/payment/tenant changes require explicit task scope.

## Product and architecture defaults

Public marketing/content sites do not acquire login, dashboards, user management, or app-style private flows unless the product requirements explicitly call for them.

The standard monorepo is `apps/web` (Next.js), `apps/api` (NestJS + Fastify), optional `apps/mobile`, and shared `packages/*`. Existing web/API service builds target the repository root; this describes source configuration, not permission to reconfigure Railway.

Authentication defaults to custom Google OAuth 2.0. Managed auth-provider exceptions require a documented project decision. When owner-supplied OAuth variables are needed, follow `TECHNICAL_STACK.md` — **Required Railway Variables handoff**: name the service/environment and provide exact code-consumed `KEY=value` blocks with the real public callback/origin and safe placeholders; request secret entry directly in the provider, never in chat. When roles exist, the minimum set is `super_admin`, `admin`, `team_leader`, and `member`, enforced server-side.

App-style products implement the specified navigation, version display, real authentication, authorized administration, debug/diagnostic contracts, safe logging, and i18n. Required routes are defined by the product and the relevant technical standards; do not invent app features for a public-only site.

LLM features, when explicitly required, use `packages/ai`, provider-agnostic configuration, schema validation, injection defenses, measured usage, hard caps, timeouts, retry limits, and kill switches. Their presence in a standard is not permission to call paid services during verification.

## Verification and completion

Review the actual source/diff and run only relevant synchronous local format/lint/typecheck/build commands and risk-triggered non-browser tests with isolated dependencies. In Auto, collect this verification for the completed whole candidate under `PHDK_AUTO.md`; do not impose optional per-stage test/acceptance gates. Actual mandatory controls remain effective. Documentation-only changes need source/diff and reference review.

No browser operation, headless testing or screenshots outside scoped UAT/UAT Fix; no unauthorized live application probes, databases or paid verification calls. A current request such as "verifica Railway" authorizes bounded reads of existing provider status, deployment/source/branch/non-secret configuration metadata, and relevant logs through an authorized API/CLI/connector under `EXECUTION_SCOPE.md`. No second authorization phrase, Developer Mode, or unlock is needed. An earlier task-specific exclusion does not cancel this newer read request. No streams, polling, secret values, settings writes, new access, or deployments. State the evidence and its limits; provider observations do not prove UI behavior or recovery.

Before reporting completion, confirm the requested outcome, applicable checks, owner controls, and verified delivery target. For a request targeting `main`, verify the remote change and version; do not trust a stale task checkbox instead of git/PR evidence or create a redundant post-merge bump/push. Report deployment evidence separately. Do not claim external agents were terminated, credentials revoked, billing corrected, or server-side protection enabled merely because documentation or local hooks changed.

Record proposed follow-ups as inactive context. After the requested outcome and authorized delivery are complete, stop.

## Widget functionality gate

At Auto entry, inspect actual app source and create `DEBUG_WIDGET_READINESS.md` before trusting visual controls. The widget must be top-left below product name; clipboard must copy a real sanitized events/errors/routes/version report; trash must actually clear supported origin-scoped caches, app storage, app cookies and logout/session via server when needed. An animated green check without awaited successful effects is FAIL. Preserve public-safe reporting and report unsupported browser controls accurately.
