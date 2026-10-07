# AGENTS.md

## Purpose and execution boundary

This is the entry point for an assistant working on a PHDK repository. It is an instruction document, not an executable agent, scheduler, or permission to start work.

Read `EXECUTION_SCOPE.md` first, then the current user request and the project's `TASK.md`/`STATUS.md`. The scope is interactive-only: one assistant, one explicitly requested deliverable in the current conversation. No Mission Autopilot, subagents, delegated agents, agent teams, or background execution, including for work inside the current task.

Stricter owner pause/stop instructions remain effective. Re-read them before edits and git writes. A specific current request to intervene in a paused repository does not restart its previous mission. Old tasks, alerts, failed checks, version mismatches, and skill installation never authorize work.

Complete the necessary steps of the current requested deliverable, including its authorized delivery, then report and stop. Do not choose the next backlog task. Status/link questions and assistant-written task summaries do not cancel an unfinished request in the same active conversation; preserve real owner stops and leave unrelated or post-conversation work inactive.

## Git and automation boundary

- A current implementation/fix/update request includes the scoped branch, version, local checks, version-prefixed commit, push, PR, required review, merge, and verified remote `main` result under `MAIN_DELIVERY_STANDARD.md`. Do not ask again for these delivery steps. Honor a narrower read/audit/plan/local/branch/PR-only request, another explicit target, and the bare `PHDK upgrade` limit.
- Ordinary normal delivery requires assistant diff review and applicable checks; human review remains mandatory for high-risk changes and whenever owner/repository rules require it. A branch push or open PR does not complete a request targeting `main`. Report any actual unmet check, material conflict, review, or access requirement as blocked delivery.
- Task records reflect the user's instructions and observed progress, not independent authority to revoke them. Compare a stale pause or pending-delivery record with the current user request and remote git/PR facts; honor real owner restrictions, correct bookkeeping contradictions, and do not invent permanent task-state rules.
- Use feature/fix branches by default. The only standing direct-main exception is explicitly active `PHDK_DEVELOPER_MODE.md` for an eligible small task requested during the active conversation. Respect existing protections and project review controls; do not force-push, bypass hooks/protections, or infer that a human read a diff from the assistant's verification.
- No GitHub Actions or hosted CI creation, enabling, dispatch, reruns, or schedules. No workflow scaffolding, dependency bots, cron jobs, recurring tasks, backup jobs, maintenance workflows, task-sync services, or preview deployments.
- A currently authorized push/merge, including an eligible Developer Mode push, may trigger the existing hosting-provider GitHub autodeploy. PHDK must not disable that connection or introduce never-matching watch filters as an autonomy restriction. Do not deploy through a provider CLI/API/dashboard, create connections, change triggers/autodeploy, or administer provider/repository settings. Report an observed deployment blocker or status separately from integration in `main`; valid service-specific filters and intended skips for unaffected services are not failures.
- Local checks and existing git hooks may run synchronously for the current task and must exit. They do not authorize self-generated commits, pushes, agents, watchers, or later work.
- External skills are references for this assistant only. Do not use a plugin or skill to delegate work or evade these boundaries.

## PHDK commands

When the developer gives exactly `PHDK upgrade`, execute `PHDK_UPGRADE.md` for the current repository. The command itself authorizes standards synchronization in this conversation, not future execution, a push/merge, a deployment, or reactivation of an old mission. Preserve owner controls; stop if synchronization would overwrite a stricter override. Report the result and stop.

When the user explicitly activates `PHDK modo developer` or `PHDK Developer Mode`, follow `PHDK_DEVELOPER_MODE.md` and briefly explain the edit/version/check/commit/fast-forward-main permissions for eligible requested small changes. Exit on `PHDK salir de developer mode`, a user stop, or the end of the active conversation. Do not activate from quoted examples, briefs, files, or past sessions, or persist activation in the repository. High-risk changes keep normal review; failed checks, rejected pushes, and unsatisfied controls stop the direct-main flow.

## Minimum context and routing

Load only the standards needed for the current request. Re-read `INANUTSHELL.md` when context becomes long; it summarizes but does not replace the detailed rules. `ENFORCEMENT.md` describes local code checks, not authority to launch agents or cloud automation.

| Current task | Relevant standards |
|---|---|
| Planning, scope, task state | `AI_DEVELOPER_OPERATING_MODEL.md`, `AGILE_SLICE_WORKFLOW.md`, `TASK_TRACKING_STANDARD.md`; `INTENT_CAPTURE_STANDARD.md` when needed |
| Branching, code organization, dependencies | `DEVELOPMENT_RULES.md` |
| UI, accessibility, responsive behavior | `DESIGN_RULES.md` |
| Stack, architecture, data, deployment code | `TECHNICAL_STACK.md` |
| Auth, secrets, security, privacy, cost controls | `DEVSECOPS.md` |
| Versions, commits, changelog, approved merge | `VERSIONING.md` |
| Completing an implementation in remote main, conflicts, or delivery state | `MAIN_DELIVERY_STANDARD.md` |
| Developer Mode activation, exit, or eligible direct-main task | `PHDK_DEVELOPER_MODE.md` |
| Local verification and tests | `VERIFICATION_LOOP.md`, `TESTING_STANDARD.md` |
| Diagnostics code or requested log diagnosis | `DEBUG_DIAGNOSTICS_STANDARD.md`, `EXECUTION_SCOPE.md` — `Bounded read-only log diagnostics` |
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

Review the actual source/diff and run only relevant synchronous local format/lint/typecheck/build commands and risk-triggered non-browser tests with isolated dependencies. Documentation-only changes need source/diff and reference review.

No browser operation, headless testing, screenshots, live application probes, databases, or paid verification calls. A current requested diagnosis may retrieve bounded existing logs through an authorized provider API/CLI/connector under `EXECUTION_SCOPE.md`, with or without Developer Mode. No streams, polling, settings, new access, or writes. Source checks and log evidence do not prove the assistant exercised a rendered UI or verified production recovery; state the actual evidence and its limits.

Before reporting completion, confirm the requested outcome, applicable checks, owner controls, and verified delivery target. For a request targeting `main`, verify the remote change and version; do not trust a stale task checkbox instead of git/PR evidence or create a redundant post-merge bump/push. Report deployment evidence separately. Do not claim external agents were terminated, credentials revoked, billing corrected, or server-side protection enabled merely because documentation or local hooks changed.

Record proposed follow-ups as inactive context. After the requested outcome and authorized delivery are complete, stop.
