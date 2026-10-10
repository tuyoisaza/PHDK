# DEVELOPMENT_RULES.md

## Purpose and execution boundary

Development principles, code organization, and git safety for PHDK. `EXECUTION_SCOPE.md` governs every action. Work stays in the active conversation; `PHDK_AUTO.md` permits continuous development of one identified goal. Explicit `PHDK PMO` may coordinate bounded in-session workers for owner-confirmed workstreams under `PHDK_PMO.md`. No unattended/background execution or delegation outside PMO.

Product requirements below describe repository code, not permission to provision services, run live checks, create automation, or start work from a stored task.

## Development principles

Prioritize correctness, security, maintainability, observability, user experience, then performance. Do not trade security/correctness for speed. Keep scope to the user's current requested outcome.

## Branching and authorization

Use `feature/`, `fix/`, `chore/`, `checkpoint/YYYY-MM-DD`, or `phdk/vX.Y.Z/short-slice-name` when relevant to an authorized git operation.

- Use a feature/fix branch for the current requested change, except for an eligible direct-to-`main` task under explicitly active `PHDK_DEVELOPER_MODE.md`. Concurrent worker branches/worktrees are allowed only under explicit PMO with ownership/dependency coordination; otherwise do not launch agents/subagents on separate branches.
- Respect existing GitHub protection and review controls without administering or bypassing them.
- A current request to implement, fix, or update repository code or documentation includes normal delivery: a scoped branch, the repository's version bump, relevant local checks, a version-prefixed commit, branch push, PR, required review, merge into remote `main`, and verification of the resulting version and change there. Follow `MAIN_DELIVERY_STANDARD.md` without asking the user to repeat those steps.
- Respect an explicit local-only, branch-only, or PR-only instruction and a different target specified by the user or repository. A read/audit request remains read-only; a bare `PHDK upgrade` retains its limited scope under `EXECUTION_SCOPE.md`. Release tags require a request for them.
- Current authorization continues through turns, status/link requests, and context compaction in the same conversation. Task records describe it; an assistant-written task/status change cannot grant or revoke it. Explicit user stop/pause instructions remain binding, and a new conversation does not automatically resume stored work.
- Do not force-push, overwrite another contributor's changes, or rewrite history to resolve a conflict silently.
- In the normal branch/PR flow, refresh remote `main` and resolve routine integration conflicts within the authorized scope while preserving both contributors' intended changes. Reconcile the branch version, review the resulting diff, and rerun affected checks before merging. Isolate a genuinely unresolved material decision or unmet check, required review, or access restriction; continue independent authorized work and report the affected operation without bypassing its control.
- When an authorized major change warrants a recoverable checkpoint, create it within that request; do not create recurring backup branches or jobs.
- Follow `VERSIONING.md` and include required metadata in the scoped change. Reconcile the branch version before merge; pure integration does not require another version-only commit or extra push.
- Deliver only through a currently authorized push/merge and the existing hosting-provider GitHub connection. An eligible Developer Mode push to `main` may trigger that existing deployment. Do not create or run GitHub Actions, add a provider connection, change triggers, enable previews, or deploy through a provider CLI/API/dashboard, including Railway.
- Updating dependencies is a specifically requested code task, not a reason to install a dependency bot or schedule future maintenance.

Review the complete outgoing diff. Changes to authentication/authorization, secrets, sensitive data/schema/migrations, payments, infrastructure, deployment configuration, or agent execution/permissions use normal branch delivery and require owner approval of the sensitive decision under `MAIN_DELIVERY_STANDARD.md`. A well-defined current request or "push to main", "merge", or "aprobado" for the identified task/PR can supply that approval in the conversation. PHDK does not require a separate GitHub review event or proof that the owner opened every diff line. Classify the actual behavior: a package-format fix restoring login is not automatically an authentication-policy change. Preserve actual named, independent, or formal review requirements; record owner approval, assistant review, and any required formal review separately without inventing human inspection.

Use `PHDK_UNLOCK.md` when the owner requests `PHDK unlock` or explicitly asks to reconcile/remove local PHDK exceptions. Reconcile obsolete documentary blockers across existing active instructions within that request; the current owner can replace an earlier documentary rule. Bare synchronization preserves unrelated/unknown local restrictions. Never weaken hooks, checks, access controls, or server protections, and do not demand this command to recognize an already clear approval.

The existing hosting-provider GitHub autodeploy connection is an allowed consequence of authorized code delivery. PHDK's restrictions on unattended execution and Actions do not require disabling it. Do not disable that connection or install dummy never-matching watch filters as enforcement. A generic development request grants no provider-settings changes. Report an observed disabled connection, a filter excluding changes that need deployment, or the relevant deployment status separately from verified code delivery to remote `main`. Valid service-specific filters and intended skips for unaffected services are not failures.

### PHDK Auto

Follow `PHDK_AUTO.md` when the owner issues `PHDK auto` for the identified current goal. Complete all its features and stages without approval pauses, a mandatory interview, or a release per slice. Use existing requirements and conventions for reversible decisions; the current request already approves the behavior it describes. A new material decision or actual unmet control does not require stopping independent authorized work.

Implement the whole candidate before final integrated verification, repair in-scope failures, then complete normal versioned branch/PR delivery. Mandatory hooks still run at the operations they govern. Auto replaces Developer Mode for this goal only when explicitly invoked; it is not an automatic fallback from a failed direct push. Respect its exit, scope, and conversation-lifetime rules.

### PHDK Developer Mode

Follow `PHDK_DEVELOPER_MODE.md` and `EXECUTION_SCOPE.md`. Activate only when the user explicitly issues `PHDK modo developer` or `PHDK Developer Mode` as a command in the current interactive conversation. Exit with `PHDK salir de developer mode` or when that conversation ends. Mentions, quotations, documentation, historical Finetuning records, or reading an instruction file do not activate it.

While active, the mode authorizes the necessary steps of small, low-risk translations, copy, ordinary documentation, or simple visual edits requested during that mode: implement, bump the version according to the repository, run applicable local checks, create a commit whose subject begins with the resulting version, and push fast-forward directly to `main` when existing controls allow it. Do not ask for duplicate consent for those steps. Activation alone selects no work, and read/audit requests remain read-only.

Judge eligibility by the actual diff, not the task label. Changes to authentication, authorization, secrets, data, migrations, payments, infrastructure, permissions, or agent policy require the normal review flow, even when expressed as a small documentation edit. Mixed or uncertain changes do not qualify for the direct flow.

Do not persist activation or an authorizing flag/state in repository files, environment/config flags, memory, tasks, or status records; never restore it automatically. Owner pause/stop controls remain effective. The mode permits no agents, autonomy, Actions, cron, scheduled/background work, old-task execution, or work after the conversation.

If an applicable check fails, `main` rejects the push, `main` has advanced so the planned update cannot fast-forward, or any existing control cannot be satisfied, stop the direct flow and explain. Preserve the work for review. Do not automatically retry, rebase, force-push, change settings/hooks/credentials, or use an alternative API/CLI to get around the failure or restriction. Do not automatically switch to the normal branch/PR flow after a direct-flow failure.

### Historical Finetuning Mode

Earlier Finetuning wording is historical. It neither activates Developer Mode nor supplies an independent direct-to-`main` exception or standing permission. Use only the explicit, conversation-limited exception in `PHDK_DEVELOPER_MODE.md`; preserve all other project controls.

## Commit rules

For an authorized commit, follow the versioned conventional format:

```txt
v0.3.1 fix(auth): handle OAuth callback failure
v0.3.2 refactor(auth): extract session service
v0.3.3 test(auth): cover callback regression
```

Update the appropriate version source in the same change, record meaningful user-facing changes, and keep unrelated edits out. `VERSIONING.md` is the detailed reference.

## Working slices and local checks

Use coherent slices only to organize the current deliverable. `AGILE_SLICE_WORKFLOW.md` does not authorize an automatic next task or a push per checkpoint. In Auto, continue every in-scope slice and collect the verification below at the completed integrated candidate under `PHDK_AUTO.md`; intermediate checks are only for an implementation blocker or an actual mandatory control.

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

A request such as "verifica Railway" authorizes [Bounded read-only provider diagnostics](EXECUTION_SCOPE.md#bounded-read-only-provider-diagnostics), independently of Developer Mode or unlock. Through existing authorized API/CLI/connector access, read finite service/deployment status, source/branch and non-secret configuration/watch-pattern metadata, and existing logs needed for that question. An earlier task's exclusion does not cancel a later scoped read request. Redact sensitive content; do not retrieve secret values, run browser tests or live application probes, stream/watch, write settings, or deploy.

## i18n

No hardcoded user-facing strings. Use configured languages and locale-aware dates, numbers, currency, and pluralization. Fallback order: user locale, app default, English.

## Data honesty and imports

Never present fake KPIs, random metrics, demo analytics, or undisclosed placeholder totals as real. Allowed states are empty, setup-required, loading, error, and success with actual data.

Explicitly requested repeatable/multi-source import code uses the stateful intake contract in `TECHNICAL_STACK.md`: batch references, reversible deactivation, auditable changes, and explicit user approval before data becomes official. Do not physically delete imported data merely to undo a bad batch.

The contract does not authorize scheduling imports or running them against live data. A one-off seed or admin CSV script may be exempt from the batch model, but writing it is not permission to execute it against a database.

## Definition of done

- The entire requested outcome is implemented and reviewed in source/diff; an Auto stage, first release, or scaffold is not completion of a larger agreed goal.
- Relevant local evidence exists; security, permissions, validation, i18n, logs, accessibility, and state handling remain intact.
- Applicable file-size and code-quality rules are satisfied.
- For the normal `main` target, the scoped change is merged and its result and version are verified on remote `main` under `MAIN_DELIVERY_STANDARD.md`. A local commit, pushed branch, or open PR is an intermediate state. An explicitly narrower target is complete only when that target is satisfied.
- Owner approval, assistant source/diff review, any actual required formal review, git/merge state, and deployment evidence are reported accurately and separately.
- No delegation outside explicit PMO, Actions, schedules, background work, external setup, or live verification was introduced.
- Task/status context is accurate; follow-ups are inactive.
- Report completion only when the whole requested scope and target are satisfied. If no permitted progress remains, report the exact blocker and unfinished scope after completing independent work. Stop after that report, without selecting another mission.
