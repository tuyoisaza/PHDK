# QA_CHECKLIST.md

## Purpose

This file defines code quality gates for task completion, merging, and GitHub delivery. `EXECUTION_SCOPE.md` controls execution; `MAIN_DELIVERY_STANDARD.md` defines normal delivery through verified remote `main` integration and explicit narrower scopes.

Choose the smallest relevant QA scope. Review applicable requirements in the changed area, record source references and actual command results, and mark unrelated items `N/A` with a reason. Documentation-only work requires source/diff consistency and applicable formatting checks, not application builds or test scaffolding.

## Evidence Boundary

The product requirements below are checked through source/diff review, static checks, local builds, and risk-triggered local unit/in-process integration tests with deterministic doubles. A checked UI, auth, database, or diagnostics item confirms implementation evidence, not an exercised user flow. Requested status, non-secret configuration metadata, and existing logs follow **Bounded read-only provider diagnostics** in `EXECUTION_SCOPE.md`, independently of Developer Mode or unlock; they are separate diagnostic evidence, never an executed product test.

Do not launch a browser, preview server, or service; collect screenshots; use headed/headless E2E, Playwright, Puppeteer, Cypress, Selenium, chrome-devtools, browser MCP, or a browser-mode runner; call application HTTP endpoints, including localhost; connect to databases; use customer accounts; or call OAuth/metered providers. Tools, plugins, and delegated agents must follow the same boundary.

Record `visual/runtime unverified` for UI appearance and product execution, and report requested provider findings separately. A human may independently inspect the product; that inspection is not a PHDK gate and must not be assigned to the user merely to close a checklist. An existing GitHub pipeline status is delivery evidence only.

# QA Scope Levels

## Task QA

- Source/diff review against the approved slice and acceptance criteria.
- Affected static/build checks where applicable.
- Small local tests only when `TESTING_STANDARD.md` identifies a risk trigger.
- Source review of security/RBAC, i18n, routes, and migration files when touched.
- `STATUS.md` update and a final report of code evidence, delivery state, failures, and limits.

## Merge QA

- Applicable checklist sections and repository static/build gate.
- Risk-triggered local tests, with no browser or external runtime access.
- Actual diff review under `MAIN_DELIVERY_STANDARD.md` and the project's existing merge policy; re-review and affected checks after integration changes.
- Unresolved code blockers are reported; excluded runtime checks are not invented as merge prerequisites.

## Diff Review

Review the complete actual diff as the assistant. Ordinary changes need no PHDK-only human approval. Sensitive decisions require owner approval under `MAIN_DELIVERY_STANDARD.md`, which a clear current request can already supply. Actual required reviews, checks, hooks, and access controls remain effective. `PHDK_DEVELOPER_MODE.md` retains its separate activation, eligibility, and direct-main hard-stop rules.

For auth/authz, secrets, sensitive data, migrations, payments, infrastructure/deployment configuration, agent execution/permission-policy changes, and other material risks, classify the actual behavior and the decision needing approval. Before normal integration:

- [ ] The assistant reviewed the complete outgoing diff, integration result, scope, and security-sensitive behavior.
- [ ] Risk classification follows the changed behavior; a packaging fix restoring login does not itself change authentication policy.
- [ ] The owner's approval covers the sensitive decision; the current request or an identified-task/PR "push to main", "merge", or "aprobado" can supply it without a second ritual.
- [ ] Any named, independent, or formal GitHub review required by an actual applicable owner/repository control is satisfied; conversation approval does not replace that control.

Record owner approval, assistant source review, any actual required review, and check/delivery evidence separately. Never claim human diff inspection from approval or passing checks; a missing GitHub review event alone does not prove owner approval is absent. A requested `PHDK unlock` reconciles documentary blockers under `PHDK_UNLOCK.md`, preserving controls and current scope. Finish permitted work before asking only for a genuinely missing decision.

## Release QA

- Applicable code checks, release metadata, and changelog.
- Code/migration compatibility and documented rollback approach when relevant.
- Deployment through the project's existing GitHub-connected pipeline only; repository integration has its own completion evidence.
- Fresh remote target commit/version evidence and existing pipeline status when available, with live behavior explicitly unverified.
- Missing external prerequisites are reported without provisioning them.

# QA Execution Rules

- Run permitted commands from the repository root unless the task specifies a narrower package.
- Inspect install/build/test/hook scripts before running them; reject browser, service, database, infrastructure, or deployment side effects.
- Use an existing offline/test configuration when available; never weaken production behavior to make a check pass.
- Validate the task scope and any global breakage it causes.
- Report actual source evidence, exact commands, failures, skipped checks, and their reasons.
- Never claim a command passed unless it ran. Do not hide gaps or substitute source review for runtime proof.
- Do not add tests, recurring agents, CI workflows, dependency bots, monitoring, or backup jobs to satisfy a checklist.
- Do not alter cloud resources, provider credentials, or repository settings as QA.

## Required Evidence Format

```txt
QA Summary:
- Status: Pass / Pass with notes / Fail
- Scope checked:
- Branch and version:

Source/diff review:
- requirement — source reference — reviewed

Commands run:
- command — result

Local tests:
- risk trigger + command/result, or not required + reason

Provider diagnostics, only if requested:
- service/deployment, source and query bounds / non-secret metadata or redacted logs / limits; diagnostic evidence only

Visual/runtime:
- visual/runtime unverified — no browser or live product test/probe executed

GitHub delivery:
- target / PR / integrated SHA / freshly verified remote version / review evidence, or explicit narrower scope/blocker; existing pipeline status separately

Failures / gaps:
- severity — description — next code step or external dependency

N/A items:
- item — reason
```

# QA Result Rules

## Failure Severity

Classify every failed item as one of these:

```txt
Blocker — cannot merge
Major   — must fix before release
Minor   — may defer with STATUS.md note
N/A     — not applicable with reason
```

## Merge Rules

- Blockers cannot be merged.
- Major issues require the project's applicable approval; record existing conversation approval truthfully in `STATUS.md` without inventing a second approval step.
- Minor issues may be deferred only if logged in `STATUS.md` with owner and next step.
- N/A items require a real reason, not “not needed”.

# Required Validation Commands

Use existing project scripts and inspect their execution path first. Run the applicable gate once before push; use narrow checks while iterating.

```bash
git diff --check
pnpm lint
pnpm typecheck
pnpm format:check
pnpm build
# Run the smallest permitted local test only when TESTING_STANDARD.md risk triggers apply.
```

Use package-filtered equivalents for affected packages. Install with `pnpm install --frozen-lockfile` only when dependency/lockfile verification is needed and install hooks stay in scope. Do not repeatedly install dependencies or scaffold missing commands just to satisfy this document.

For schema changes, review generated migration SQL, schemas, and compatibility notes. Run generation or static schema checks only if the existing command is offline and has no database connection or mutation. Never run `db:migrate`, `db:push`, `db:studio`, restore commands, or live database checks as QA. Record database execution as unverified.

# Build Quality

- [ ] **Install:** dependency/lockfile verification ran when needed; lifecycle scripts stayed within the execution scope.
- [ ] **Lint:** lint passes with no errors.
- [ ] **Typecheck:** TypeScript typecheck passes with no errors.
- [ ] **Web build:** build passes for `apps/web`.
- [ ] **API build:** build passes for `apps/api`.
- [ ] **Risk-based tests:** when a mandatory trigger applies, the smallest permitted local tests pass or failures/gaps are reported; otherwise source review and applicable static/build checks are sufficient.
- [ ] **Format:** format check passes.
- [ ] **Imports:** no unused imports introduced.
- [ ] **Dead code:** no dead code introduced.
- [ ] **File size:** no files exceed 600 lines.
- [ ] **Architecture:** no business logic exists inside page components.
- [ ] **Dependencies:** no new dependency was added without task justification.
- [ ] **Frameworks:** no framework/library replacement happened without explicit approval.
- [ ] **Generated files:** no generated files were committed unless explicitly expected.

# LSP / Code Intelligence QA

Review existing local code-intelligence setup when relevant — see `TECHNICAL_STACK.md` LSP / Code Intelligence Setup. Use local IDE/LSP capabilities only; no browser or external-service session is required.

- [ ] Available local diagnostics, navigation, references, rename, hover/types, and symbol search are checked only when relevant to the task.
- [ ] Drizzle-generated types (from `packages/db`) resolve correctly, not as `any`.
- [ ] No second, conflicting `tsconfig.json` was created to make a tool work.
- [ ] Whether the AI coding agent has direct LSP access or only text/grep-based search is confirmed and reported, not assumed.

# Product Baseline

- [ ] **Project identity:** source places the project name and logo/icon in the top-left app shell.
- [ ] **Version placement:** source mounts the version in the app shell, login page, and admin panel.
- [ ] **Version format:** version format is correct: `vMAJOR.MINOR.PATCH (shortSHA · UTC timestamp)`.
- [ ] **Debug copy:** button, clipboard handler, and safe report formatter are wired in source.
- [ ] **Debug metadata:** debug report includes all required metadata.
- [ ] **Redaction:** debug report redacts all sensitive values.
- [ ] **Real data:** no fake production data is shown anywhere.
- [ ] **Empty states:** empty states are honest and tell the user what to do next.
- [ ] **Loading states:** loading states exist on all async operations.
- [ ] **Error states:** error states are clear and include recovery actions.
- [ ] **Success states:** success states exist where actions complete successfully.
- [ ] **Permission states:** permission-denied states exist where relevant.

# Routes

- [ ] **Dedicated routes:** every feature has a real URL route.
- [ ] **No hash routing:** no primary feature relies on hash-fragment navigation.
- [ ] **Unauthenticated access:** protected routes redirect unauthenticated users to login.
- [ ] **Unauthorized access:** protected routes block unauthorized roles server-side.
- [ ] **Permission UI:** permission denied state is shown where appropriate.
- [ ] **404:** 404 page exists and is user-friendly.
- [ ] **500/error boundary:** 500 page or error boundary exists where applicable.
- [ ] **Admin separation:** admin routes are separated from customer/member routes.
- [ ] **Route map:** route map is updated if routes changed.

# Authentication and Google OAuth 2.0

- [ ] Login, Google redirect, callback success/failure, logout, and session-refresh handlers are wired in source.
- [ ] Auth provider is custom Google OAuth 2.0, or an explicitly approved alternative in `ARCHITECTURE_DECISIONS.md`.
- [ ] Exactly one primary auth provider is implemented unless migration/comparison is explicitly in scope.
- [ ] Required OAuth variable names and redirect-URI expectations are documented in `.env.example`/setup docs without real credentials.
- [ ] Redirect construction uses validated configuration; actual provider registration is an external prerequisite, not an agent check.
- [ ] OAuth state is generated and validated; invalid state and callback failures have safe errors and correlation IDs.
- [ ] User create/update and session creation logic handles successful callbacks securely.
- [ ] Session expiry/refresh and logout invalidation are defined in code.
- [ ] Cookies use appropriate HttpOnly, Secure, and SameSite settings.
- [ ] Protected routes and APIs deny unauthenticated access; current-user responses expose safe data only.
- [ ] Failed auth produces structured redacted logs and diagnostics.
- [ ] No OAuth secrets are committed; managed auth alternatives require the recorded architecture approval.
- [ ] Changed security boundaries have local tests using fake OAuth/session/persistence adapters.
- [ ] Real Google login and provider configuration remain explicitly unverified.

# Authorization and RBAC

- [ ] **super_admin:** permission matrix is reviewed in source and covered locally when changed.
- [ ] **admin:** permission matrix is reviewed in source and covered locally when changed.
- [ ] **team_leader:** permission matrix is reviewed in source and covered locally when changed.
- [ ] **member:** permission matrix is reviewed in source and covered locally when changed.
- [ ] **Role escalation:** role escalation is blocked server-side.
- [ ] **API authorization:** authorization is enforced on every protected API endpoint.
- [ ] **Server actions:** authorization is enforced on every protected server action where applicable.
- [ ] **UI is not security:** hiding UI is not the only security layer.
- [ ] **Unauthorized status:** unauthorized API calls return `401` or `403`, not `200`.
- [ ] **Audit:** role changes create audit logs.
- [ ] **Self-escalation:** self-escalation is impossible.
- [ ] **Tenant isolation:** cross-tenant access is blocked where multi-tenancy exists.

# Admin Panel

- [ ] **Admin home:** `/admin` route and authorization are implemented.
- [ ] **Users:** `/admin/users` implements list, create, edit, and deactivate handlers.
- [ ] **Roles:** `/admin/roles` implements protected role assignment and management.
- [ ] **Debug:** `/admin/debug` implements authorized debug controls.
- [ ] **System:** `/admin/system` maps safe system information into its UI.
- [ ] **Audit:** `/admin/audit` maps authorized audit data into its UI.
- [ ] **Debug permission:** debug mode can only be toggled by permitted roles.
- [ ] **Debug audit:** debug mode toggle creates an audit log entry.
- [ ] **Confirmations:** sensitive admin actions require confirmation.
- [ ] **Action logging:** sensitive admin actions log the actor, target, timestamp, and result.
- [ ] **Reason field:** sensitive admin actions require a reason field where appropriate.
- [ ] **Admin lists:** admin lists support loading, empty, error, pagination, sorting, and filtering where applicable.

# Debug Mode

- [ ] **Activation:** debug-mode activation handler and authorization are reviewed in source.
- [ ] **Deactivation:** debug-mode deactivation handler and authorization are reviewed in source.
- [ ] **Dev default:** debug mode is ON by default in local/dev/preview/staging, with no manual setup step.
- [ ] **Verbosity:** debug mode increases log verbosity.
- [ ] **Production default:** debug mode never activates in production by default.
- [ ] **Production code gate:** source/configuration keeps the forced-on default limited to non-production; actual deployment environment state remains unverified.
- [ ] **Diagnostic coverage:** important new or changed execution boundaries emit high-signal structured diagnostics; trivial helpers are not blanket-instrumented.
- [ ] **Activation audit:** debug mode activation is audited.
- [ ] **Deactivation audit:** debug mode deactivation is audited.
- [ ] **Authorized visibility:** debug indicator or panel appears only for authorized admin/developer roles when active.
- [ ] **Customer hiding:** debug UI never appears for normal customer/member roles.
- [ ] **Version display:** debug panel shows current version.
- [ ] **Scope display:** debug panel shows active debug scope.
- [ ] **Actor display:** debug panel shows who enabled debug mode and when, where available.
- [ ] **Expiry display:** debug panel shows expiry when applicable.
- [ ] **Copy report:** copy-report button copies sanitized diagnostics.
- [ ] **Error context:** debug report includes errors and correlation ID.
- [ ] **No raw logs:** debug report never includes unrestricted raw server logs.
- [ ] **Redaction:** debug report redacts passwords, tokens, cookies, API keys, authorization headers, and secrets.
- [ ] **Client context:** debug report includes browser, route, locale, environment, and build metadata.

# Full Force Cache Dump

The debug/admin tooling implements a full force cache dump action for authorized human users. Review handlers and safety limits in code; the agent does not press the control, clear a real user's browser/session, or access platform caches.

## Required Behavior

- [ ] Full force cache dump action exists in admin/debug tooling.
- [ ] Action is visible only to authorized admin/developer roles.
- [ ] Action requires confirmation before execution.
- [ ] Action creates an audit log entry.
- [ ] Action clears application cache where applicable.
- [ ] Action clears relevant browser storage where applicable.
- [ ] Action clears relevant server-side cache where applicable.
- [ ] Action clears relevant client query/cache state where applicable.
- [ ] Action invalidates or refreshes stale session state where applicable.
- [ ] Action forces logout when required to guarantee clean state.
- [ ] Action reloads the app after completion when required.
- [ ] Action reports what was cleared and what could not be cleared.
- [ ] Action does not expose secrets or raw session tokens.
- [ ] Action is safe to run repeatedly.
- [ ] Action cannot delete durable business data.

## Minimum Client-Side Targets Where Applicable

- [ ] localStorage
- [ ] sessionStorage
- [ ] IndexedDB
- [ ] Cache Storage API
- [ ] service worker caches
- [ ] app query/cache layer
- [ ] auth/session client state
- [ ] stale feature flag cache
- [ ] stale i18n cache

## Minimum Server-Side Targets Where Applicable

- [ ] server memory cache
- [ ] feature flag cache
- [ ] auth/session cache
- [ ] i18n/cache layer
- [ ] API response cache
- [ ] CDN/platform cache where supported by project tooling
- [ ] stale build/runtime metadata cache where applicable

## Never Clear

- durable business records
- audit logs
- user accounts
- billing/payment records
- production database tables
- uploaded files or permanent storage

## Safety Rules

- [ ] Full force cache dump is never available to normal users.
- [ ] Full force cache dump must not delete durable business records.
- [ ] Full force cache dump must not mutate production data except cache/session/debug state.
- [ ] Full force cache dump must be audited with actor, timestamp, environment, and result.
- [ ] If any cache layer cannot be cleared, the UI must say so explicitly.
- [ ] Production execution requires confirmation and clear warning text.

# Database and Migration Code

- [ ] PostgreSQL configuration and typed data access follow the project stack; actual local/cloud database operation is unverified.
- [ ] Environment examples distinguish development from production and never include real connection values.
- [ ] `DATABASE_URL` uses validated PostgreSQL format; no SQLite dependency, local DB file, or fallback is introduced.
- [ ] Missing/invalid database configuration fails clearly in code; no silent in-memory production store is added.
- [ ] Schema changes include migration files generated through the existing offline Drizzle workflow where available.
- [ ] Migration SQL is reviewed before commit, including clean-schema and existing-data assumptions.
- [ ] Compatibility, rollback, and backfill notes exist for affected schema/data changes.
- [ ] Destructive transformations are explicitly in task scope and have local deterministic coverage when risk requires it.
- [ ] Soft-delete logic and audit fields (`created_at`, `updated_at`, `created_by`, `updated_by`) exist where required.
- [ ] Raw SQL is justified and parameterized.
- [ ] Indexes, foreign keys, and uniqueness constraints cover the relevant query/data rules.
- [ ] Seed fixtures are dev/test-only and are never presented as real production data.
- [ ] Source/test fixtures use fake persistence adapters without replacing production storage behavior.
- [ ] No migration is applied to a database, no production state is mutated, and no cloud database is provisioned as QA.
- [ ] No backup policy, recurring export job, email delivery, backup branch, or restore test is created merely because PHDK is present.
- [ ] Existing external database/backup prerequisites are documented when relevant, without being operated by the agent.
- [ ] Migration execution and operational recovery are explicitly reported as unverified.

# Validation

- [ ] All API inputs are validated with Zod at the boundary.
- [ ] Shared Zod schemas live in `packages/validators`, following `TECHNICAL_STACK.md` and the foundation layout.
- [ ] Schemas are shared between `apps/web` and `apps/api`.
- [ ] No duplicate schemas exist across apps.
- [ ] No client-supplied data is trusted without server-side validation.
- [ ] Environment variables are validated with Zod on startup.
- [ ] App fails fast when required environment variables are missing or invalid.
- [ ] Form validation matches API validation where applicable.
- [ ] Validation errors are shown clearly in the UI.

# API Contracts

- [ ] API contracts are typed with shared Zod schemas.
- [ ] Request schemas live in the correct shared package.
- [ ] Response schemas live in the correct shared package where applicable.
- [ ] Breaking API changes include migration notes or a versioning strategy.
- [ ] API errors return stable error codes.
- [ ] Raw error internals are not exposed to clients.
- [ ] API responses do not expose fields the user is not allowed to see.
- [ ] Pagination, sorting, and filtering are implemented where list endpoints require them.
- [ ] Rate limiting is enforced on API routes, with stricter limits on sensitive/auth endpoints as required by `DEVSECOPS.md`.

## API Diagnostic Code Checks Where Applicable

- [ ] Public `/health` implements a minimal safe response contract; `/health/deep` enforces admin/developer authorization.
- [ ] Affected endpoints register method/path, purpose, auth/roles, probe mode, expected statuses, and sanitized examples.
- [ ] Local fake-handler tests cover changed authorization, validation, redaction, and probe-mode guards when risk requires them.
- [ ] Unsafe, destructive, private, or metered endpoints cannot execute through automatic product probes.
- [ ] Failure contracts include stable errors, correlation IDs, and safe log context.
- [ ] Deep-health code reports database/migration/auth/configuration state without secrets and without creating paid calls for health.
- [ ] Version, SHA, build timestamp, environment, registry, and last available probe results are represented in the response contract.
- [ ] No service endpoint was called for verification; actual live responses remain unverified.

# Logging and Observability

- [ ] Structured logs exist for all important actions.
- [ ] Logs include `event`, `timestamp`, `environment`, `version`, and `correlation_id`.
- [ ] Logs include user ID and role where available.
- [ ] No passwords, tokens, cookies, or secrets appear in logs.
- [ ] Correlation IDs flow through requests.
- [ ] Version-aware logs exist.
- [ ] Environment-aware logs exist.
- [ ] `/health` route and minimal response handler exist in `apps/api` source.
- [ ] Readiness endpoint exists where applicable.
- [ ] Debug mode increases log verbosity without exposing secrets.
- [ ] Error tracking integration is used only if explicitly tasked/configured.
- [ ] OpenTelemetry is used only if explicitly tasked/configured.
- [ ] Important admin actions are audited.
- [ ] Failed auth and authorization attempts are logged safely.
- [ ] If provider diagnostics were requested, retrieval followed **Bounded read-only provider diagnostics** in `EXECUTION_SCOPE.md`; source, bounds, non-secret metadata, redacted logs, and limits are reported separately from test results.

# Feature Flags

- [ ] Risky or incomplete features are behind feature flags.
- [ ] Feature flags default safely.
- [ ] Feature flags are scoped appropriately: global, tenant, or user.
- [ ] Feature flag changes are auditable where relevant.
- [ ] Temporary feature flags include cleanup notes.
- [ ] Disabled feature flags do not expose broken navigation or dead UI.

# i18n

- [ ] All user-facing strings use the i18n system, including admin and error messages.
- [ ] Configured languages have the required translation keys and a defined English fallback.
- [ ] Date, number, and currency formatting use the active locale where relevant.
- [ ] Locale switching and persistence are wired in code.
- [ ] Source styles accommodate longer translated labels; actual rendering remains unverified.

# Design, Responsive UI, and Accessibility

Review components, styles, markup, and handlers in source. Do not launch a browser, resize a viewport, collect screenshots, or run a browser accessibility scanner.

- [ ] Responsive layouts account for phone (including 320px), tablet (768px), and desktop (1024px+) widths.
- [ ] Navigation and controls support keyboard interaction in their semantics and event handlers.
- [ ] Focus styles and logical tab order are defined; modal/dialog focus management is implemented where needed.
- [ ] Buttons and critical icon controls have accessible names; form fields have labels and linked error messages.
- [ ] Page headings have a logical structure.
- [ ] Source color tokens meet WCAG AA minimum contrast where calculable; color is not the only state indicator.
- [ ] Images have useful alt text or are marked decorative.
- [ ] Loading, empty, error, success, and permission-denied states are implemented where relevant.
- [ ] Destructive actions have confirmation flows.
- [ ] Critical actions do not rely on mystery icons or hover-only discovery.
- [ ] Critical errors remain available beyond a toast.
- [ ] Tables include responsive handling; media reserves layout space where needed.
- [ ] Charts and production views use real data paths, never fabricated data.
- [ ] No blank/error-only route or unusable navigation path is introduced by the code change.
- [ ] Actual browser/device appearance, interaction, and assistive-technology behavior are reported as `visual/runtime unverified`.

# Security

- [ ] No secrets are committed to the repository.
- [ ] No secrets are exposed in the frontend bundle.
- [ ] Logs redact all sensitive values.
- [ ] Debug report redacts all sensitive values.
- [ ] CSRF protection reviewed.
- [ ] XSS protection reviewed.
- [ ] SQL injection risk reviewed — parameterized queries used, no raw string concatenation into SQL.
- [ ] Command injection risk reviewed — no unsanitized input passed to a shell.
- [ ] SSRF reviewed where applicable.
- [ ] File upload rules exist if uploads are used.
- [ ] CORS is an explicit origin allowlist — never a wildcard on a credentialed route (`DEVSECOPS.md` HTTP Security Headers).
- [ ] CSP, HSTS (production), and the standard security header set are configured on `apps/api`.
- [ ] Rate limiting is active globally and enforced more strictly on auth endpoints (`DEVSECOPS.md` Rate Limiting) — not merely "considered."
- [ ] Any exposed secret is removed/redacted from the code deliverable and reported as requiring owner-managed rotation; the agent does not rotate provider credentials or claim rotation occurred.
- [ ] Sessions and cookies use secure settings where applicable.
- [ ] Admin actions are protected server-side.
- [ ] Sensitive API endpoints reject unauthorized access.
- [ ] Environment variables are not printed to client logs.
- [ ] If the project collects personal data, `/privacy` (and `/terms` if applicable) exist and a data-deletion request process is documented (`DEVSECOPS.md` Privacy and Legal Baseline).

# Cost and Consumption Safety

- [ ] Every metered/paid external API call (AI/image/video generation, LLM calls, SMS, email sending, third-party enrichment, etc.) has a hard usage cap enforced in code.
- [ ] Every metered API call has a request timeout.
- [ ] Every metered API call has a max retry limit with backoff — no indefinite retries.
- [ ] Any loop, queue, poller, or background job that can call a metered API repeatedly has an explicit max-iterations or max-cost bound.
- [ ] Expensive operations have idempotency keys or dedup checks so the same input cannot double-trigger cost.
- [ ] A kill switch (env var or feature flag) exists that disables each metered integration without a deploy.
- [ ] Per-user or per-session quota exists where the metered call is user-triggered.
- [ ] Metered calls are logged with operation, cost/units consumed, actor, and correlation ID.
- [ ] Product code exposes redacted usage/spend evidence through logs or authorized diagnostics; no provider call is made for agent verification.
- [ ] Metered-integration code applies a configurable unusual-spend threshold to existing usage records in its normal logging/diagnostic path, with isolated threshold tests; no external alert, recurring check, or monitoring job is created.
- [ ] No metered integration relies solely on the provider's own rate limit as its cost safety net.

# AI / LLM Configuration QA

- [ ] `/admin/ai` exists and is protected when the project uses any LLM-powered feature.
- [ ] Prompt template is visible and editable by an authorized admin without a code deploy.
- [ ] Expected output schema/format is visible and editable by an authorized admin.
- [ ] AI provider (Anthropic, OpenAI, Google, etc.) is set via configuration, not hardcoded.
- [ ] AI model is set via configuration, not hardcoded.
- [ ] Human-operated "Refresh model pricing" code maps provider pricing for models in use and records availability/version honestly.
- [ ] Pricing refresh is admin-triggered, not called on every request; PHDK does not add a recurring refresh schedule.
- [ ] User-supplied content is isolated from the system prompt — no direct concatenation.
- [ ] LLM output is validated against the expected schema before use or display.
- [ ] Invalid or malformed LLM output is rejected, not silently trusted.
- [ ] Prompt, output schema, provider, and model changes are audit-logged with actor, timestamp, and diff.
- [ ] AI provider API key is never exposed client-side.
- [ ] No feature or route imports a provider SDK directly — every LLM call goes through `packages/ai`.
- [ ] Every LLM call is recorded with the provider-reported token usage (input/output/cached/reasoning as applicable), computed cost, model, feature, and latency — see `TECHNICAL_STACK.md` AI Token & Cost Observability.
- [ ] Token counts come from the provider's `usage` response, not a local estimate, when the provider reports it.
- [ ] Cost calculation records which pricing table version/date was used.
- [ ] Full prompt/response content is not stored as part of token/cost tracking by default.
- [ ] Cost and Consumption Safety checks above apply to every LLM call in this feature.
- [ ] If the feature feeds externally-sourced content (scraped pages, CMS fields, uploaded files, third-party API responses) into an LLM call, that content is structurally delimited and never treated as instructions.
- [ ] Action-triggering (write, delete, publish, send, purchase, etc.) driven by a model call is scoped to the authenticated user's own request, never to text parsed out of externally-sourced content.
- [ ] Credentials/API tokens used by the feature are scoped per resource/tenant, not one shared key with broad cross-site or cross-tenant access.
- [ ] A confirmation/approval gate exists before any destructive or side-effecting action that a model call driven by external content could trigger.
- [ ] Cases where externally-sourced content is passed into an LLM call are logged, and flagged if the output contains action-like directives the user never requested.

# Data Import / Intake QA

- [ ] Applies when approved product code imports multiple source types, supports repeated user-initiated imports, or explicitly implements recurring import logic; no schedule or live import is configured or run.
- [ ] A one-off seed script or single admin-only CSV import is exempt only when it has no repeated or recurring execution, per `DEVELOPMENT_RULES.md`.
- [ ] Every import is a batch with an explicit lifecycle state (`pending`/`processed`/`approved`/`deactivated`), not a bare insert.
- [ ] Every business row created by an import carries a reference to the batch that created it.
- [ ] A batch requires explicit manual approval before its data is treated as official — approval never moves or copies rows.
- [ ] "Delete this import" in the UI or API is wired to deactivate, never to a physical row `DELETE`.
- [ ] Deactivating a batch records who, when, and why — and leaves rows and files in place.
- [ ] Business queries (dashboards, reports, forecasts) reading import-populated tables apply the shared active-batch filter, not a one-off `WHERE` clause per query.
- [ ] The active-batch filter excludes only `deactivated` batches — rows with no batch reference (legacy data) are always live.
- [ ] Exact-duplicate detection (content hash) runs before insert and skips files already imported in a non-deactivated batch.
- [ ] Semantic-duplicate detection (content fingerprint independent of file bytes) runs before insert for re-exported files with the same underlying data.
- [ ] Every file in a batch gets a recorded outcome (parsed/errored/duplicate) with counts and a warnings/errors payload — parsing never fails silently.
- [ ] Cutoff/period date is derived from file content, not requested from the user.

# Dependency and Supply Chain QA

- [ ] No dependency added without task justification.
- [ ] Lockfile changes are expected and reviewed.
- [ ] No duplicate package added when existing utility covers the need.
- [ ] No package with known unacceptable license added.
- [ ] No abandoned/high-risk package added without approval.
- [ ] Dependency upgrade, if any, is documented.
- [ ] No Dependabot/Renovate configuration or recurring dependency-update workflow is added or enabled by PHDK.
- [ ] Any dependency change received the same source/lockfile and Dependency Safety review, regardless of who authored it.

# Performance QA

- [ ] No obvious unnecessary client component introduced.
- [ ] No large library imported for a small utility.
- [ ] Images use optimized loading where applicable.
- [ ] Layout shift is avoided for images/media.
- [ ] Expensive operations are not run on every render unnecessarily.
- [ ] Pagination or virtualization considered for large lists.
- [ ] API calls are not duplicated unnecessarily.
- [ ] Core page remains usable while async data loads.

# Monorepo and GitHub Deployment

- [ ] Applicable root/package builds cover changed `apps/web`, `apps/api`, and shared packages.
- [ ] Existing repository deployment configuration is reviewed; valid GitHub autodeploy/watch paths are preserved, with no dummy never-matching filters or provider-setting changes.
- [ ] Deployment uses only the authorized push/merge path consumed by an existing GitHub connection; remote target integration is verified separately.
- [ ] No provider CLI/API/dashboard deployment or local build upload is performed.
- [ ] No GitHub Actions, preview deployment, new trigger/schedule, dependency bot, or maintenance workflow is scaffolded as a PHDK prerequisite.
- [ ] `.env.example` documents required names with safe placeholders; real `.env` files are ignored.
- [ ] Missing hosting/OAuth/database/secrets prerequisites and an observed disabled autodeploy connection or filter excluding changes that need deployment are reported as separate blockers without reconfiguration; valid service-specific filters and intended unaffected-service skips are not failures.
- [ ] GitHub deployment status is recorded when available; no live `/health` or browser check is used to certify delivery.
- [ ] `apps/mobile` remains untouched unless explicitly tasked.

# Documentation QA

- [ ] `TASK.md` acceptance criteria are satisfied.
- [ ] `STATUS.md` updated with current state if required.
- [ ] `ARCHITECTURE_DECISIONS.md` updated if stack or architecture changed.
- [ ] Route map updated if routes changed.
- [ ] `.env.example` updated if env vars changed.
- [ ] README or setup docs updated if developer workflow changed.
- [ ] Known gaps are documented, not hidden.
- [ ] If `phdk-standards/` is vendored, `phdk-standards/VERSION` matches the PHDK standards repo's current version, or the gap is flagged in `STATUS.md`.

# Release

- [ ] Source-changing commits update the repository's actual version source and derived metadata per `VERSIONING.md`; do not assume every repository uses `package.json`.
- [ ] Source-changing commit messages begin with the resulting version (`vX.Y.Z`); integration commit handling follows `VERSIONING.md`.
- [ ] Pure merge/squash integration of already versioned changes adds no extra bump, post-merge version-only commit, or second push.
- [ ] The requested change is integrated into remote `main` or the explicit target, with fresh commit/ancestry and version-source evidence; a branch push/open PR is incomplete unless the user expressly narrowed delivery.
- [ ] Health/version code and build metadata are wired to identify the released commit; actual deployed responses are unverified.
- [ ] Checkpoint branch created if this is a major update.
- [ ] `STATUS.md` updated with current state.
- [ ] `TASK.md` records remaining steps of the still-current request; later follow-ups stay inactive and snapshots do not pause authorized delivery.
- [ ] All gap notes from this session are logged in `STATUS.md`.
- [ ] High-risk delivery has a documented code rollback/revert approach compatible with the existing GitHub pipeline; no provider operation is performed.
- [ ] Migration rollback notes exist if schema changed.
- [ ] Deployment-impacting changes list source/local evidence and remaining visual/runtime limits; no browser or service smoke test is a PHDK gate.
- [ ] Release notes or changelog entry exists where applicable.

# Working Slice and Diagnostics QA

- [ ] The approved scope and intended outcome are clear before coding.
- [ ] Required task context was read; the agent stayed within `EXECUTION_SCOPE.md` and the approved files.
- [ ] Code verification evidence, changed files, and known gaps are reported without hiding failures.
- [ ] `TASK.md` and `STATUS.md` reflect completion or the next active slice; no unnecessary approval pause is added between authorized slices.
- [ ] For debug diagnostics, source review covers the full contract in `DEBUG_DIAGNOSTICS_STANDARD.md`: version badges, paired copy/cache controls, safe reports, auth/metered metadata, and authorized visibility.
- [ ] Cache and clipboard handlers are wired in source; any local test uses fake browser adapters, never a browser session.
- [ ] Source defaults debug mode ON in non-production and OFF in production; risky default-selection logic is locally covered when needed.
- [ ] Diagnostic buffers, registry/UI mapping, sanitized examples, correlation IDs, status/latency, and safe probe guards are reviewed in code.
- [ ] No live report, health request, endpoint probe, browser interaction, or external settings confirmation is required to mark diagnostics code complete.
- [ ] Product execution remains explicitly `visual/runtime unverified`; requested bounded provider findings are separate diagnostic evidence.

# Enforcement QA

Review local enforcement when foundation work or the current change touches it. See `ENFORCEMENT.md`; repository settings remain outside agent administration.

- [ ] Existing required `commit-msg`, `pre-commit`, and `pre-push` hooks are reviewed and checked locally when changed.
- [ ] Local hook checks cover malformed commit messages, staged secrets, formatting, and the applicable static/build gate without browser or external-runtime execution.
- [ ] `pre-push` validates the outgoing commit range; tests remain risk-triggered evidence rather than a universal hook.
- [ ] No workflow, dependency bot, scheduled job, or repository-settings change is added merely to satisfy PHDK.
- [ ] Existing repository merge/review constraints are respected; missing external prerequisites are reported without provisioning them.
- [ ] The current tool's native rule block matches canonical `PHDK_NATIVE_RULES.md` and includes the `EXECUTION_SCOPE.md` boundary.
- [ ] No hook, check, required review, or access control was bypassed, disabled, or weakened to complete delivery.

# Final QA Rule

Unresolved required checks, reviews, or access blockers prevent claiming delivery completion; major release issues require the project's recorded approval. Normal delivery allows bounded in-scope repair and ordinary conflict resolution under `MAIN_DELIVERY_STANDARD.md`; Developer Mode hard stops remain unchanged. Browser/live product tests are excluded scope, and requested bounded provider diagnostics remain separate evidence.

The final response states what source was reviewed, actual check results, remote target/version evidence or the precise delivery blocker/narrower scope, and what remains `visual/runtime unverified`.
