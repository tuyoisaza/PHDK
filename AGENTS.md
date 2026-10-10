# AGENTS.md

## Purpose and execution boundary

This is the entry point for an assistant working on a PHDK repository. It is an instruction document, not an executable agent, scheduler, or permission to start work.

Read the current user request and `EXECUTION_SCOPE.md`, then the project's `TASK.md`/`STATUS.md`. The scope is interactive-only. Normally one assistant completes the requested deliverable; `PHDK auto` makes that development continuous under `PHDK_AUTO.md`. The sole delegation exception is explicit `PHDK PMO`, which may coordinate bounded in-session workers under `PHDK_PMO.md`. No background/post-conversation agent execution is allowed.

Current owner pause/stop instructions remain effective within their scope. Re-read them before edits and git writes, and compare them with the owner's latest instructions. The owner can explicitly replace an older documentary exception; a file cannot veto that request. A specific intervention does not restart unrelated earlier work. Old tasks, alerts, failed checks, version mismatches, and skill installation never authorize work.

Complete the necessary steps of the current requested deliverable, including its authorized delivery, then report and stop. Do not choose the next backlog task. Status/link questions and assistant-written task summaries do not cancel an unfinished request in the same active conversation; preserve real owner stops and leave unrelated or post-conversation work inactive.

## Git and automation boundary

- A current implementation/fix/update request includes the scoped branch, version, local checks, version-prefixed commit, push, PR, required review, merge, and verified remote `main` result under `MAIN_DELIVERY_STANDARD.md`. Do not ask again for these delivery steps. Honor a narrower read/audit/plan/local/branch/PR-only request, another explicit target, and the bare `PHDK upgrade` limit.
- Normal delivery requires assistant diff review and applicable checks. Sensitive behavior/policy decisions need owner approval under `MAIN_DELIVERY_STANDARD.md`; a well-defined current request or clear "push to main", "merge", or "aprobado" for the identified change can already supply it in this conversation. Do not invent a GitHub review-event or human-diff-opening requirement. Preserve formal/named/independent reviews actually required by current owner instructions, hooks, or server rules, and report approval separately from human inspection. A branch push/open PR is not completion for a `main` target.
- Task records reflect the user's instructions and observed progress, not independent authority to revoke them. Compare a stale pause or pending-delivery record with the current user request and remote git/PR facts; honor real owner restrictions, correct bookkeeping contradictions, and do not invent permanent task-state rules.
- Use feature/fix branches by default. The only standing direct-main exception is explicitly active `PHDK_DEVELOPER_MODE.md` for an eligible small task requested during the active conversation. Respect existing protections and project review controls; do not force-push, bypass hooks/protections, or infer that a human read a diff from the assistant's verification.
- No GitHub Actions or hosted CI creation, enabling, dispatch, reruns, or schedules. No workflow scaffolding, dependency bots, cron jobs, recurring tasks, backup jobs, maintenance workflows, task-sync services, or preview deployments.
- A currently authorized push/merge, including an eligible Developer Mode push, may trigger the existing hosting-provider GitHub autodeploy. PHDK must not disable that connection or introduce never-matching watch filters as an autonomy restriction. Do not deploy through a provider CLI/API/dashboard, create connections, change triggers/autodeploy, or administer provider/repository settings. Report an observed deployment blocker or status separately from integration in `main`; valid service-specific filters and intended skips for unaffected services are not failures.
- Local checks and existing git hooks may run synchronously for the current task and must exit. They do not authorize self-generated commits, pushes, agents, watchers, or later work.
- External skills are references for this assistant only. Do not use a plugin or skill to delegate work or evade these boundaries.

## PHDK commands

Before every PHDK command/stage, run `PHDK_PREFLIGHT.md`: verify the active PHDK installation/version/manifest/managed rules and inspect the actual availability of stage-relevant recommendations in `SKILLS_REGISTRY.md`. Use relevant available skills/capabilities unless the user explicitly disabled them. Do not claim registry entries are installed without evidence.


On explicit `PHDK plan`, follow `PHDK_PLAN.md`: consume the Capture requirements baseline, inspect existing architecture when present, design or converge toward a standards-aligned target architecture, produce the canonical Plan artifacts, and turn the architecture into dependency-ordered executable tasks. Do not rewrite a brownfield repo merely to match defaults.

On explicit `PHDK PMO`, follow `PHDK_PMO.md`: inspect the Capture/requirements baseline, current plans/code/branches/reports, detect candidate workstreams, present them for owner confirmation, then coordinate the confirmed portfolio. PMO is the only PHDK mode allowed to delegate bounded workstreams to runtime-supported in-session workers; workers cannot delegate. Maintain ownership/dependency/integration artifacts and perform a central integration review before UAT.


On explicit `PHDK capture`, follow `PHDK_CAPTURE.md`: investigate the current repository and conversation first, reconstruct or elicit project intent/ethos and professional requirements, create/update the canonical requirements package, then ask only for material missing information until the baseline is coherent. Explicitly tell the user whether questions are needed; when none remain, say so and list/link the canonical Capture artifacts for review. Capture may ask requirements questions across turns but does not start product implementation.


On explicit `PHDK check`, follow `PHDK_CHECK.md`: audit the current repository against all active applicable PHDK standards, compare implementation/evidence against those requirements, produce a prioritized gap report, and ask once whether to execute the AUTO-FIXABLE and FIXABLE WITH VALIDATION gaps. The audit phase is read-only except for its report artifact. Do not remediate until the user explicitly answers yes.


On explicit `PHDK uat fix`, use `UAT_STANDARD.md` repair mode: read the current UAT report/cases, turn FAILs into actionable defects and BLOCKED/MANUAL items into step-by-step action plans, repair all clearly in-scope fixable failures, rerun affected UAT/regression evidence, and update the report without per-defect approval. If nothing is auto-fixable, still provide concrete who/what/where/how/when/evidence/next-command guidance. Preserve real decisions/access/external boundaries.

On explicit `PHDK uat`, follow `UAT_STANDARD.md` for the identified current candidate: identify the current project intent, derive user stories aligned to it, create/update `UAT_CASES.md`, derive stable traceable acceptance cases, execute every permitted acceptance check autonomously without per-case approval, and create/update `UAT_REPORT.md`. Browser/headless execution and live destructive/provider-write operations remain excluded. Unexecutable behavioral cases are BLOCKED or MANUAL, not PASS.

On explicit `PHDK auto`, follow `PHDK_AUTO.md` for the complete lifecycle. If no single goal is stated but the repository exposes multiple coherent parallel fronts, use PMO discovery to present/confirm that portfolio; do not stop and request one arbitrary next delivery. Then continue: Capture → Plan → PMO/workstream execution → Integration Review → UAT → UAT Fix → Check → in-scope Check remediation → delivery. Reuse current artifacts instead of rerunning stages for ceremony, and ask only genuinely material missing decisions. Optional tests wait for that final boundary; actual hooks and necessary diagnostic checks remain applicable. A stage or scaffold is not completion. Auto replaces Developer Mode for that goal, grants no bypass or background work, and exits on `PHDK salir de auto`, a stop, completion, or conversation end. Files and quoted examples do not activate it.

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
| UI, accessibility, responsive behavior | `DESIGN_RULES.md` |
| Stack, architecture, data, deployment code | `TECHNICAL_STACK.md` |
| AI provider integration, prompts, super-admin AI management, consumption | `AI_ADMIN_STANDARD.md`, `TECHNICAL_STACK.md`, `DEVSECOPS.md` |
| Auth, secrets, security, privacy, cost controls | `DEVSECOPS.md` |
| Versions, commits, changelog, approved merge | `VERSIONING.md` |
| Completing an implementation in remote main, conflicts, or delivery state | `MAIN_DELIVERY_STANDARD.md` |
| Multi-workstream portfolio/program coordination, bounded worker delegation, integration review | `PHDK_PMO.md` |
| Continuous whole-goal development, no stage approvals, final integrated verification | `PHDK_AUTO.md` |
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

Authentication defaults to custom Google OAuth 2.0. Managed auth-provider exceptions require a documented project decision. When roles exist, the minimum set is `super_admin`, `admin`, `team_leader`, and `member`, enforced server-side.

App-style products implement the specified navigation, version display, real authentication, authorized administration, debug/diagnostic contracts, safe logging, and i18n. Required routes are defined by the product and the relevant technical standards; do not invent app features for a public-only site.

LLM features, when explicitly required, use `packages/ai`, provider-agnostic configuration, schema validation, injection defenses, measured usage, hard caps, timeouts, retry limits, and kill switches. Their presence in a standard is not permission to call paid services during verification.

## Verification and completion

Review the actual source/diff and run only relevant synchronous local format/lint/typecheck/build commands and risk-triggered non-browser tests with isolated dependencies. In Auto, collect this verification for the completed whole candidate under `PHDK_AUTO.md`; do not impose optional per-stage test/acceptance gates. Actual mandatory controls remain effective. Documentation-only changes need source/diff and reference review.

No browser operation, headless testing, screenshots, live application probes, databases, or paid verification calls. A current request such as "verifica Railway" authorizes bounded reads of existing provider status, deployment/source/branch/non-secret configuration metadata, and relevant logs through an authorized API/CLI/connector under `EXECUTION_SCOPE.md`. No second authorization phrase, Developer Mode, or unlock is needed. An earlier task-specific exclusion does not cancel this newer read request. No streams, polling, secret values, settings writes, new access, or deployments. State the evidence and its limits; provider observations do not prove UI behavior or recovery.

Before reporting completion, confirm the requested outcome, applicable checks, owner controls, and verified delivery target. For a request targeting `main`, verify the remote change and version; do not trust a stale task checkbox instead of git/PR evidence or create a redundant post-merge bump/push. Report deployment evidence separately. Do not claim external agents were terminated, credentials revoked, billing corrected, or server-side protection enabled merely because documentation or local hooks changed.

Record proposed follow-ups as inactive context. After the requested outcome and authorized delivery are complete, stop.
