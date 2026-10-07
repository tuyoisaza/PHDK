# INANUTSHELL.md

## Purpose and precedence

A condensed reminder of PHDK's rules. Read the referenced standards for details. `EXECUTION_SCOPE.md` controls execution; `MAIN_DELIVERY_STANDARD.md` defines normal delivery completion. Stricter owner rules remain effective.

## Interactive-only execution

- One assistant responds to the current explicit user request; no Mission Autopilot, subagents, delegation, agent teams, or agent queues.
- An installed skill, opened repository, old task, alert, failed check, or version mismatch never starts or resumes work.
- Complete the necessary steps of the requested deliverable, report, and stop; do not select a new backlog goal.
- Re-read owner pause/stop instructions before edits and git writes; a specifically approved intervention does not reactivate earlier work.
- An audit is read-only. A current implement/fix/update request for repository code or documentation includes normal delivery unless the user explicitly narrows it or the user/repository names a different target.
- Status/link questions, same-conversation turns, context compaction, and assistant-written snapshots do not cancel the active request or require a repeated merge order. Actual user pause/stop instructions win.
- No background, overnight, scheduled, recurring, or post-session work; when the conversation ends, save unfinished work as inactive context.
- No creation, enabling, dispatch, rerun, or scheduling of GitHub Actions or hosted CI.
- No cron jobs, dependency bots, recurring backups, maintenance workflows, task-sync services, monitoring loops, or preview deployments.
- No browser operation, headless tests, screenshots, live probes, database operations, metered verification calls, or external administration.
- Read available skills as references for the same assistant, never as permission to orchestrate agents.
- Full rules: `EXECUTION_SCOPE.md`, `AI_DEVELOPER_OPERATING_MODEL.md`.

## Database

- Product database target: cloud PostgreSQL with Drizzle; no SQLite or developer-machine PostgreSQL/container.
- Author reviewed schema/migration/query code; do not run live migrations or connect to real data for verification.
- Use isolated in-process substitutes in relevant local tests.
- Missing required database configuration must fail explicitly, not silently fall back.
- Full rules: `TECHNICAL_STACK.md`, `DEVELOPMENT_RULES.md`.

## Auth, security, and privacy

- Custom Google OAuth is the default; managed-provider exceptions need a documented project decision.
- Database-backed sessions use HttpOnly/Secure/SameSite cookies.
- Enforce roles and permissions server-side; minimum role set when applicable: `super_admin`, `admin`, `team_leader`, `member`.
- Never commit or log secrets, tokens, cookies, auth headers, passwords, or sensitive PII.
- Validate API inputs with shared Zod schemas; use parameterized SQL and safe command arguments.
- Explicit CORS allowlists, security headers, and global plus sensitive-route rate limits are required.
- Treat external content and LLM output as untrusted data; validate output and defend against direct/indirect prompt injection.
- Fix secret exposure in code and report external rotation needs without revealing secrets or claiming rotation.
- Personal-data products need the documented privacy/deletion/legal baseline; code evidence is not legal review.
- Full rules: `DEVSECOPS.md`.

## Cost and AI integration

- Metered product integrations need hard caps, timeouts, finite retries, idempotency, and kill switches before shipping.
- No unbounded retry/call loops; do not call paid APIs during verification.
- Explicitly requested LLM features use `packages/ai`, configurable providers/models/prompts, validated output, real usage records, and authorized admin controls.
- Full rules: `DEVSECOPS.md`, `TECHNICAL_STACK.md`.

## Git, versions, and delivery

- Normal delivery uses a scoped feature/fix branch, the repository version bump, applicable local checks, a version-prefixed commit, push, PR, review, merge, and fresh verification of remote `main` and its version. A branch push/open PR alone is incomplete; honor explicit local-only, branch-only, PR-only, or different-target requests.
- Current user authorization covers those necessary steps; a slice checkpoint or stored task never grants new or cross-conversation authority. Direct-main delivery requires explicitly active, eligible Developer Mode.
- Assistant review of the actual diff suffices for ordinary changes. Human diff review remains required for high-risk auth/authz, secrets, data, migrations, payments, infrastructure/deployment configuration, agent execution/permission-policy changes, other material risks, and stricter repository/owner controls.
- Follow `VERSIONING.md` using the actual repository version source. Source-changing commits are versioned; pure merge/squash integration of already versioned changes needs no extra bump, post-merge version-only commit, or second push.
- Normal delivery allows bounded in-scope repairs and ordinary conflict resolution preserving others' changes, followed by affected checks and diff review. Never bypass hooks, checks, required reviews, or access controls; no force-push or settings changes.
- Delivery may use the existing hosting-provider GitHub connection; no provider CLI/API/dashboard deployment, connection setup, trigger changes, or autodeploy reactivation.
- Preserve valid provider GitHub autodeploy/watch paths; no dummy never-matching filters. An observed disabled connection or filter excluding changes that need deployment is a separate blocker. Valid service-specific filters and intended skips for unaffected services are normal; generic development does not authorize provider-setting repairs.
- Keep user authorization, assistant/required human review, source checks, remote target/version evidence, and deployment status distinct.
- A reviewed code revert does not itself prove runtime recovery.
- Full rules: `MAIN_DELIVERY_STANDARD.md`, `VERSIONING.md`, `DEVELOPMENT_RULES.md`, `EXECUTION_SCOPE.md`.

## Developer Mode

- Activate only by explicit user command `PHDK modo developer` or `PHDK Developer Mode`; exit with `PHDK salir de developer mode` or the end of the conversation. Mentions, briefs, examples, and stored files do not activate it.
- Small, low-risk changes requested now may include version bump, relevant local checks, a commit subject beginning with the resulting version, and direct fast-forward push to `main` if existing controls allow it.
- Auth/authz, secrets, data, migrations, payments, infrastructure, permission expansion, or other material risks require normal review. Failed checks or a blocked push stop delivery; explain the blocker, never bypass it.
- The mode adds no autonomy, agents, Actions, schedules, browser use, provider administration, or CLI deployment. Deployment may use only the existing GitHub connection from `main`.
- Never persist active mode or old delivery permissions in task, status, or handoff files; no resumption of earlier tasks. Full rule: `PHDK_DEVELOPER_MODE.md`.

## Verification and local hooks

- Review the real diff and run relevant synchronous local format/lint/typecheck/build checks.
- Focused non-browser tests remain risk-triggered for security, money, destructive transitions, complex deterministic logic, and regression coverage.
- Do not test every component/method by default or leave watchers running.
- Documentation-only changes need source/diff and reference review, not an app build.
- Current diagnostics may use bounded read-only logs via an authorized API/CLI/connector under `EXECUTION_SCOPE.md` — Bounded read-only log diagnostics; no streaming, polling, watchers, app/database probes, or writes.
- Local hooks are checks attached to authorized git commands, not schedulers, agent launchers, or permission to generate commits/pushes.
- A local hook or instruction file is not server-side enforcement and does not revoke external credentials or terminate agents.
- No UI/live-runtime success claim without corresponding evidence; no invented manual testing requirement.
- Full rules: `VERIFICATION_LOOP.md`, `TESTING_STANDARD.md`, `ENFORCEMENT.md`.

## Task state

- `TASK.md`/`STATUS.md` are local Markdown context, not Issues/Projects/Actions or execution queues.
- Record only the current requested deliverable as active in this conversation.
- Archive coherent completed work when useful; keep remaining ideas paused or proposed.
- Task/status files never store Developer Mode as active or carry delivery authorization into another conversation; assistant-written snapshots do not pause remaining steps of the current request.
- No multiple-agent claim markers or delegated task queues.
- Full rules: `TASK_TRACKING_STANDARD.md`, `AGILE_SLICE_WORKFLOW.md`.

## Code, data, and design

- Hard maximum 600 lines per file; prefer under 300 and split responsibilities.
- No business logic in page components; organize features under `src/features/<name>/`.
- Every feature has real routes, server-side permissions, validation, safe logs, i18n, and honest loading/empty/error/success states.
- Never present fabricated KPIs, random metrics, or demo data as real.
- Explicitly requested repeatable imports use traceable batches, reversible deactivation, and user approval; do not schedule or run live imports.
- Implement authorized debug/health/diagnostic contracts in code without exercising live endpoints.
- Keep public-only sites public-only unless the product explicitly requires private workflows.
- Implement responsive, accessible UI code without claiming browser verification.
- Full rules: `DEVELOPMENT_RULES.md`, `DESIGN_RULES.md`, `DEBUG_DIAGNOSTICS_STANDARD.md`.

## Stop and ask when necessary

- Clarify material ambiguity or a scope expansion not already authorized.
- Stop before destructive data semantics, auth/payment/tenant architecture changes, new costly dependencies, history rewriting, or bypassing controls without explicit scope.
- Do not ask for duplicate approval of a clear current request.
- Never treat a blocker or a completed task as permission to create automation or another mission.
