# DEVELOPMENT_RULES.md

## Purpose and execution boundary

Development principles, code organization, and git safety for PHDK. `EXECUTION_SCOPE.md` governs every action. Work is interactive-only with the current assistant; no autopilot, subagents, delegated work, agent queues, or background execution.

Product requirements below describe repository code, not permission to provision services, run live checks, create automation, or start work from a stored task.

## Development principles

Prioritize correctness, security, maintainability, observability, user experience, then performance. Do not trade security/correctness for speed. Keep scope to the user's current requested outcome.

## Branching and authorization

Use `feature/`, `fix/`, `chore/`, `checkpoint/YYYY-MM-DD`, or `phdk/vX.Y.Z/short-slice-name` when relevant to an authorized git operation.

- Use a feature/fix branch for the current requested change. Do not launch concurrent agents or subagents on separate branches.
- Respect existing GitHub protection and review controls without administering or bypassing them.
- Commit/push/PR/merge/release authority must come from the current request. A slice checkpoint and `TASK.md` are not standing permission.
- A read/audit request remains read-only. A clear instruction to implement and merge includes the necessary branch/commit/push/PR steps, without duplicate confirmation.
- Do not force-push, overwrite another contributor's changes, or rewrite history to resolve a conflict silently.
- When an authorized major change warrants a recoverable checkpoint, create it within that request; do not create recurring backup branches or jobs.
- Follow `VERSIONING.md` when a commit is authorized. Do not generate commits merely to bump metadata.
- Deliver only a specifically approved release through the existing hosting-provider GitHub connection. Do not create or run GitHub Actions, add a provider connection, change triggers, enable previews, or use a provider deployment CLI/API/dashboard.
- Updating dependencies is a specifically requested code task, not a reason to install a dependency bot or schedule future maintenance.

### Finetuning Mode

The existing narrow pre-production exception for a user-authorized direct push does not grant autonomous execution. It may be activated only explicitly in the current conversation, for requested small changes to a product not serving real users, and only when existing repository controls permit it.

It does not persist in task files, environment flags, prior chats, or subsequent sessions. It never permits agents, delegation, Actions, schedules, background work, external administration, or bypassing protection. An owner pause remains effective unless the current owner request specifically authorizes the limited intervention.

Even in this mode, git writes must match the current request, relevant local checks must pass, scope/security controls remain intact, and actual human-review evidence must not be invented. The mode ends when the user ends it or the conversation ends.

## Commit rules

For an authorized commit, follow the versioned conventional format:

```txt
v0.3.1 fix(auth): handle OAuth callback failure
v0.3.2 refactor(auth): extract session service
v0.3.3 test(auth): cover callback regression
```

Update the appropriate version source in the same change, record meaningful user-facing changes, and keep unrelated edits out. `VERSIONING.md` is the detailed reference.

## Working slices and local checks

Use coherent slices only to organize the current deliverable. `AGILE_SLICE_WORKFLOW.md` does not authorize an automatic next task or a push per checkpoint.

Use source/diff review and relevant synchronous local formatting, linting, typechecking, builds, and risk-triggered non-browser unit/in-process tests. Checks must exit; no watchers, browser testing, live services, databases, or metered APIs. Documentation-only changes need source/diff and reference review. Report UI/live runtime behavior as unverified without inventing manual testing obligations.

## File and feature structure

Hard maximum: 600 lines per file; prefer fewer than 300. Split by responsibility and keep functions small. Do not put business logic in page components or create miscellaneous utility dumping grounds.

```txt
src/features/<feature-name>/
  components/
  services/
  repositories/
  schemas/
  permissions/
  logs/
  types.ts
```

Each feature requires real routes, server-side permissions, input validation, i18n, safe structured logs, and meaningful loading/empty/error/success states.

## Monorepo defaults

```txt
apps/
  web/              Next.js frontend
  api/              NestJS + Fastify backend
  mobile/           Expo placeholder only
packages/
  ui/
  types/
  validators/
  api-client/
  design-tokens/
  observability/
  db/               Drizzle schema and client
  config/
```

Use pnpm workspaces and Turborepo. Share reusable code in `packages/*`. Existing web/API service build configurations target the repository root; do not reconfigure live services or establish a hosting connection. Mobile stays a placeholder unless explicitly requested.

## Routes and product scope

Every meaningful feature uses a real route, such as `/admin/users` or `/settings/profile`, not a hash-fragment substitute. Do not add private-app features to a public-only website unless the product requirements explicitly call for them.

## Authentication and database

Custom Google OAuth 2.0 is the default. A managed provider exception requires a documented project decision. `DEVSECOPS.md` defines authentication, authorization, and session safety.

Use Drizzle and cloud-hosted PostgreSQL as the product data contract. Do not use SQLite, start local PostgreSQL, or run a database container. Author reviewed schema/query/migration code; do not retrieve live credentials, connect to production, or execute migrations as verification. Use isolated in-process dependency substitutes for local checks.

Use appropriate `id`, `created_at`, `updated_at`, `created_by`, `updated_by`, and soft-delete fields for important records.

## Validation

Validate at the API boundary with Zod, not only in the UI. Share schemas through `packages/validators`. Never trust client-supplied ownership, roles, references, or raw LLM output without validation and authorization.

## Logging and errors

Use structured logs at important execution boundaries. Include applicable event, timestamp, environment, version, correlation ID, actor/role, route/operation, and result. Never log passwords, secrets, cookies, tokens, auth headers, or sensitive PII.

Errors need stable codes, useful messages, safe technical detail, correlation IDs, and severity. Follow `DEBUG_DIAGNOSTICS_STANDARD.md` for diagnostic-code contracts without invoking live diagnostics.

## i18n

No hardcoded user-facing strings. Use configured languages and locale-aware dates, numbers, currency, and pluralization. Fallback order: user locale, app default, English.

## Data honesty and imports

Never present fake KPIs, random metrics, demo analytics, or undisclosed placeholder totals as real. Allowed states are empty, setup-required, loading, error, and success with actual data.

Explicitly requested repeatable/multi-source import code uses the stateful intake contract in `TECHNICAL_STACK.md`: batch references, reversible deactivation, auditable changes, and explicit user approval before data becomes official. Do not physically delete imported data merely to undo a bad batch.

The contract does not authorize scheduling imports or running them against live data. A one-off seed or admin CSV script may be exempt from the batch model, but writing it is not permission to execute it against a database.

## Definition of done

- The requested outcome is implemented and reviewed in source/diff.
- Relevant local evidence exists; security, permissions, validation, i18n, logs, accessibility, and state handling remain intact.
- Applicable file-size and code-quality rules are satisfied.
- User authorization, actual human review, git/merge state, and deployment evidence are reported accurately and separately.
- No agents, delegation, Actions, schedules, background work, external setup, or live verification was introduced.
- Task/status context is accurate; follow-ups are inactive.
- The requested deliverable is complete or honestly blocked. Report and stop, rather than selecting another mission.
