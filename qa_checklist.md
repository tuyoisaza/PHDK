# QA_CHECKLIST.md

## Purpose

This file defines the quality gates every agent and developer must pass before marking any task complete, merging to `main`, or releasing to production.

Run the appropriate QA scope before completion. Do not skip sections because they seem irrelevant. Mark items as `N/A` only when they genuinely do not apply and include a reason.

A task is not complete until the final QA report is written.

---

# QA Scope Levels

Use the smallest valid QA scope.

## Task QA

Required for every task:

- affected build/lint/typecheck
- affected tests
- scope-specific manual checks
- security/RBAC checks if touched
- i18n checks if UI touched
- database/migration checks if schema or queries changed
- final QA report

## Merge QA

Required before merging to `main`:

- full checklist sections relevant to changed areas
- full build
- full typecheck
- affected tests
- route checks if routes changed
- admin checks if admin changed
- auth/RBAC checks if permissions changed
- migration checks if database changed

## Release QA

Required before production release:

- full checklist
- smoke test plan
- rollback plan
- migration rollback notes if schema changed
- deployment validation
- cache/debug validation where relevant
- final release QA report

---

# QA Execution Rules

## Required Behavior

- Run QA from the repository root unless a task explicitly says otherwise.
- Validate only the task scope, but do not ignore global breakage caused by the task.
- Do not mark an item complete without evidence.
- Do not silently skip failed checks.
- If a check cannot run, document why.
- If a check is not applicable, mark it `N/A` with a reason.
- If a command fails, paste the exact command and the failure summary into the final report.
- Never claim build, lint, typecheck, or tests pass unless they were actually run.
- Skipped checks must be listed under `Failures / gaps`, not hidden under the summary.

## Required Evidence Format

Every final QA report must include:

```txt
QA Summary:
- Status: Pass / Pass with notes / Fail
- Scope checked:
- Branch:
- Version:
- Environment:

Commands run:
- command — result

Manual checks:
- item — result

Failures / gaps:
- severity — description — next action

N/A items:
- item — reason — approved by/source
```

## UI Evidence Requirement

For UI changes, the final QA report must include screenshots or a clear visual verification note for:

- desktop
- mobile
- loading state where changed
- empty state where changed
- error state where changed
- permission-denied state where changed

---

# QA Result Rules

## Failure Severity

Classify every failed item as one of these:

```txt
Blocker — cannot merge
Major   — must fix before release
Minor   — may defer with STATUS.md note
N/A     — not applicable with reason
```

## N/A Format

Use this format when marking an item as not applicable:

```txt
Item:
Reason:
Approved by / source:
```

## Merge Rules

- Blockers cannot be merged.
- Major issues cannot be released without explicit written approval in `STATUS.md`.
- Minor issues may be deferred only if logged in `STATUS.md` with owner and next step.
- N/A items require a real reason, not “not needed”.

---

# Required Validation Commands

Use the project’s actual package scripts. If names differ, use equivalent commands and document them.

## Root-Level Commands

```bash
pnpm install --frozen-lockfile
pnpm lint
pnpm typecheck
pnpm build
pnpm test
pnpm format:check
```

## App-Level Commands

```bash
pnpm --filter @repo/web lint
pnpm --filter @repo/web typecheck
pnpm --filter @repo/web build
pnpm --filter @repo/web test

pnpm --filter @repo/api lint
pnpm --filter @repo/api typecheck
pnpm --filter @repo/api build
pnpm --filter @repo/api test
```

## Database Commands

Use the project’s Drizzle scripts. Expected coverage:

```bash
pnpm --filter @repo/db db:generate
pnpm --filter @repo/db db:migrate
pnpm --filter @repo/db db:check
pnpm --filter @repo/db db:push:check
```

If a command does not exist yet, log it as a gap.

Do not require `db:studio` as a QA command. It opens a UI and is not an automated validation gate.

---

# Build Quality

Checklist:

- [ ] **Install:** `pnpm install --frozen-lockfile` runs cleanly from repository root.
- [ ] **Lint:** lint passes with no errors.
- [ ] **Typecheck:** TypeScript typecheck passes with no errors.
- [ ] **Web build:** build passes for `apps/web`.
- [ ] **API build:** build passes for `apps/api`.
- [ ] **Tests:** tests pass for affected packages/apps.
- [ ] **Format:** format check passes.
- [ ] **Imports:** no unused imports introduced.
- [ ] **Dead code:** no dead code introduced.
- [ ] **File size:** no files exceed 600 lines.
- [ ] **Architecture:** no business logic exists inside page components.
- [ ] **Dependencies:** no new dependency was added without task justification.
- [ ] **Frameworks:** no framework/library replacement happened without explicit approval.
- [ ] **Generated files:** no generated files were committed unless explicitly expected.

---

# Product Baseline

Checklist:

- [ ] **Project identity:** project name appears in the top-left app shell.
- [ ] **Logo:** logo or icon appears in the top-left app shell.
- [ ] **App version:** version appears in the app shell.
- [ ] **Login version:** version appears on the login page.
- [ ] **Admin version:** version appears in the admin panel.
- [ ] **Version format:** version format is correct: `vMAJOR.MINOR.PATCH (shortSHA · UTC timestamp)`.
- [ ] **Debug copy:** copy-debug-report button exists and works.
- [ ] **Debug metadata:** debug report includes all required metadata.
- [ ] **Redaction:** debug report redacts all sensitive values.
- [ ] **Real data:** no fake production data is shown anywhere.
- [ ] **Empty states:** empty states are honest and tell the user what to do next.
- [ ] **Loading states:** loading states exist on all async operations.
- [ ] **Error states:** error states are clear and include recovery actions.
- [ ] **Success states:** success states exist where actions complete successfully.
- [ ] **Permission states:** permission-denied states exist where relevant.

---

# Routes

Checklist:

- [ ] **Dedicated routes:** every feature has a real URL route.
- [ ] **No hash routing:** no primary feature relies on hash-fragment navigation.
- [ ] **Unauthenticated access:** protected routes redirect unauthenticated users to login.
- [ ] **Unauthorized access:** protected routes block unauthorized roles server-side.
- [ ] **Permission UI:** permission denied state is shown where appropriate.
- [ ] **404:** 404 page exists and is user-friendly.
- [ ] **500/error boundary:** 500 page or error boundary exists where applicable.
- [ ] **Admin separation:** admin routes are separated from customer/member routes.
- [ ] **Route map:** route map is updated if routes changed.

---

# Authentication

Checklist:

- [ ] **Login:** login page works.
- [ ] **Google SSO:** Google SSO works.
- [ ] **Logout:** logout works and clears session.
- [ ] **Session expiry:** session expiry is configured.
- [ ] **Protected routes:** unauthenticated users cannot access protected routes.
- [ ] **Approved provider:** auth provider is custom Google OAuth 2.0, or an explicitly approved alternative in `ARCHITECTURE_DECISIONS.md`.
- [ ] **Single provider:** exactly one primary auth provider is scaffolded unless migration/comparison is explicitly in scope.
- [ ] **Redirect URI:** auth redirect URI is correctly configured.
- [ ] **Invalid auth state:** invalid auth state is handled without blank screen.
- [ ] **Session refresh:** session refresh behavior works as designed.

---

# Authorization and RBAC

Checklist:

- [ ] **super_admin:** `super_admin` permissions work correctly.
- [ ] **admin:** `admin` permissions work correctly.
- [ ] **team_leader:** `team_leader` permissions work correctly.
- [ ] **member:** `member` permissions work correctly.
- [ ] **Role escalation:** role escalation is blocked server-side.
- [ ] **API authorization:** authorization is enforced on every protected API endpoint.
- [ ] **Server actions:** authorization is enforced on every protected server action where applicable.
- [ ] **UI is not security:** hiding UI is not the only security layer.
- [ ] **Unauthorized status:** unauthorized API calls return `401` or `403`, not `200`.
- [ ] **Audit:** role changes create audit logs.
- [ ] **Self-escalation:** self-escalation is impossible.
- [ ] **Tenant isolation:** cross-tenant access is blocked where multi-tenancy exists.

---

# Admin Panel

Checklist:

- [ ] **Admin home:** `/admin` route is protected and works.
- [ ] **Users:** `/admin/users` works — list, create, edit, deactivate.
- [ ] **Roles:** `/admin/roles` works — assign and manage roles.
- [ ] **Debug:** `/admin/debug` works — toggle debug mode and access debug tools.
- [ ] **System:** `/admin/system` works — system info visible.
- [ ] **Audit:** `/admin/audit` works — audit log visible.
- [ ] **Debug permission:** debug mode can only be toggled by permitted roles.
- [ ] **Debug audit:** debug mode toggle creates an audit log entry.
- [ ] **Confirmations:** sensitive admin actions require confirmation.
- [ ] **Action logging:** sensitive admin actions log the actor, target, timestamp, and result.
- [ ] **Reason field:** sensitive admin actions require a reason field where appropriate.
- [ ] **Admin lists:** admin lists support loading, empty, error, pagination, sorting, and filtering where applicable.

---

# Debug Mode

Checklist:

- [ ] **Activation:** debug mode activates correctly.
- [ ] **Deactivation:** debug mode deactivates correctly.
- [ ] **Verbosity:** debug mode increases log verbosity.
- [ ] **Production default:** debug mode never activates in production by default.
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

---

# Full Force Cache Dump

The debug/admin tooling must include a full force cache dump action for authorized roles.

This is mandatory because cache, session, browser, and stale build state can create too much back-and-forth during debugging.

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

---

# Database

- [ ] PostgreSQL works in local development.
- [ ] PostgreSQL works in staging/production.
- [ ] Local PostgreSQL runs through approved local setup, such as Docker Compose or Railway local connection.
- [ ] No local-only database behavior differs from staging/production.
- [ ] `DATABASE_URL` uses PostgreSQL format.
- [ ] No SQLite configuration exists.
- [ ] No SQLite dependency or local DB file is introduced.
- [ ] All migrations run cleanly from scratch.
- [ ] No schema changes exist without a migration file.
- [ ] Migration rollback notes exist for every schema change.
- [ ] Destructive migrations have explicit approval.
- [ ] Soft delete works where required.
- [ ] Audit fields are present where required: `created_at`, `updated_at`, `created_by`, `updated_by`.
- [ ] No raw SQL exists without justification.
- [ ] No production schema was mutated manually.
- [ ] Local PostgreSQL setup instructions exist.
- [ ] Database indexes exist for common query paths where needed.
- [ ] Foreign key and uniqueness constraints exist where needed.
- [ ] Seed data, if present, is dev-only and never presented as production data.
- [ ] A data backup policy is recorded in `ARCHITECTURE_DECISIONS.md` (or an explicit "no policy yet" decision).
- [ ] The backup job (weekly email export, weekly git backup branch, or the chosen alternative) runs and produces a usable SQL dump.
- [ ] Backup job failures are logged and surfaced, not silent.
- [ ] If backups are emailed, sensitive dumps are encrypted or password-protected before sending.
- [ ] If backups are committed to git, they land only on dated backup branches in the private repo, never on `main` or a public repo.
- [ ] A restore from an actual backup has been tested at least once.

---

# Migrations and Rollback

- [ ] Migration was generated through Drizzle workflow.
- [ ] Migration was reviewed before commit.
- [ ] Migration was tested locally against PostgreSQL.
- [ ] Migration can run from a clean database.
- [ ] Migration can run against existing development data where applicable.
- [ ] Rollback notes exist.
- [ ] Destructive operations are explicitly approved.
- [ ] Data backfill plan exists where needed.
- [ ] Migration impact is documented in `STATUS.md` or release notes.

---

# Validation

- [ ] All API inputs are validated with Zod at the boundary.
- [ ] Zod schemas live in `packages/core`.
- [ ] Schemas are shared between `apps/web` and `apps/api`.
- [ ] No duplicate schemas exist across apps.
- [ ] No client-supplied data is trusted without server-side validation.
- [ ] Environment variables are validated with Zod on startup.
- [ ] App fails fast when required environment variables are missing or invalid.
- [ ] Form validation matches API validation where applicable.
- [ ] Validation errors are shown clearly in the UI.

---

# API Contracts

- [ ] API contracts are typed with shared Zod schemas.
- [ ] Request schemas live in the correct shared package.
- [ ] Response schemas live in the correct shared package where applicable.
- [ ] Breaking API changes include migration notes or a versioning strategy.
- [ ] API errors return stable error codes.
- [ ] Raw error internals are not exposed to clients.
- [ ] API responses do not expose fields the user is not allowed to see.
- [ ] Pagination, sorting, and filtering are implemented where list endpoints require them.
- [ ] Rate limiting is considered for sensitive endpoints.

## API Smoke Checks Where Applicable

- [ ] `GET /health` returns `200`.
- [ ] Protected endpoint rejects unauthenticated request.
- [ ] Protected endpoint rejects unauthorized role.
- [ ] Valid request returns expected shape.
- [ ] Invalid request returns validation error.

---

# Logging and Observability

- [ ] Structured logs exist for all important actions.
- [ ] Logs include `event`, `timestamp`, `environment`, `version`, and `correlation_id`.
- [ ] Logs include user ID and role where available.
- [ ] No passwords, tokens, cookies, or secrets appear in logs.
- [ ] Correlation IDs flow through requests.
- [ ] Version-aware logs exist.
- [ ] Environment-aware logs exist.
- [ ] `/health` endpoint exists and responds on `apps/api`.
- [ ] Readiness endpoint exists where applicable.
- [ ] Debug mode increases log verbosity without exposing secrets.
- [ ] Error tracking integration is used only if explicitly tasked/configured.
- [ ] OpenTelemetry is used only if explicitly tasked/configured.
- [ ] Important admin actions are audited.
- [ ] Failed auth and authorization attempts are logged safely.

---

# Feature Flags

- [ ] Risky or incomplete features are behind feature flags.
- [ ] Feature flags default safely.
- [ ] Feature flags are scoped appropriately: global, tenant, or user.
- [ ] Feature flag changes are auditable where relevant.
- [ ] Temporary feature flags include cleanup notes.
- [ ] Disabled feature flags do not expose broken navigation or dead UI.

---

# i18n

- [ ] No hardcoded user-facing strings exist anywhere in the codebase.
- [ ] All strings use the i18n system.
- [ ] All configured project languages render correctly.
- [ ] Fallback to English works when locale string is missing.
- [ ] Date formatting respects locale.
- [ ] Number formatting respects locale.
- [ ] Currency formatting respects locale where relevant.
- [ ] Longer translated labels do not break layout.
- [ ] Locale switching works as designed.
- [ ] Admin and error messages are translated where user-facing.

---

# Design and UX

- [ ] All core flows work on mobile.
- [ ] All core flows work on tablet.
- [ ] All core flows work on desktop.
- [ ] Keyboard navigation works end to end.
- [ ] Visible focus states exist on all interactive elements.
- [ ] All buttons have accessible names.
- [ ] All form fields have labels.
- [ ] Form errors are linked to their fields.
- [ ] Destructive actions require confirmation.
- [ ] Color contrast meets WCAG AA minimum.
- [ ] Images have alt text unless decorative.
- [ ] No blank pages exist.
- [ ] All states are handled: loading, empty, error, success, permission denied where relevant.
- [ ] No mystery icons are used for critical actions.
- [ ] Primary actions are not hidden behind hover-only UI.
- [ ] Toasts are not the only place critical errors appear.
- [ ] Tables support responsive behavior.
- [ ] Charts show real data only.

---

# Browser and Device QA

Minimum manual check where UI changed:

- [ ] Chrome or Chromium desktop.
- [ ] Safari desktop if available.
- [ ] Mobile viewport at 320px width.
- [ ] Tablet viewport at 768px width.
- [ ] Desktop viewport at 1024px or wider.
- [ ] Keyboard-only navigation for changed flow.

If browser/device checks are not possible, document why.

---

# Accessibility QA

- [ ] Page has logical heading structure.
- [ ] Interactive elements are reachable by keyboard.
- [ ] Focus order is logical.
- [ ] Focus state is visible.
- [ ] Forms have labels.
- [ ] Errors are linked to fields.
- [ ] Buttons and icon buttons have accessible names.
- [ ] Images have useful alt text or are marked decorative.
- [ ] Color is not the only indicator of state.
- [ ] Modal/dialog focus behavior works where applicable.

---

# Security

- [ ] No secrets are committed to the repository.
- [ ] No secrets are exposed in the frontend bundle.
- [ ] Logs redact all sensitive values.
- [ ] Debug report redacts all sensitive values.
- [ ] CSRF protection reviewed.
- [ ] XSS protection reviewed.
- [ ] SQL injection risk reviewed.
- [ ] SSRF reviewed where applicable.
- [ ] File upload rules exist if uploads are used.
- [ ] API rate limiting considered.
- [ ] Sessions and cookies use secure settings where applicable.
- [ ] Admin actions are protected server-side.
- [ ] Sensitive API endpoints reject unauthorized access.
- [ ] Environment variables are not printed to client logs.

---

# Cost and Consumption Safety

- [ ] Every metered/paid external API call (AI/image/video generation, LLM calls, SMS, email sending, third-party enrichment, etc.) has a hard usage cap enforced in code.
- [ ] Every metered API call has a request timeout.
- [ ] Every metered API call has a max retry limit with backoff — no indefinite retries.
- [ ] Any loop, queue, poller, or background job that can call a metered API repeatedly has an explicit max-iterations or max-cost bound.
- [ ] Expensive operations have idempotency keys or dedup checks so the same input cannot double-trigger cost.
- [ ] A kill switch (env var or feature flag) exists that disables each metered integration without a deploy.
- [ ] Per-user or per-session quota exists where the metered call is user-triggered.
- [ ] Metered calls are logged with operation, cost/units consumed, actor, and correlation ID.
- [ ] Current usage/spend is observable in logs, a dashboard, or `/health/deep`.
- [ ] No metered integration relies solely on the provider's own rate limit as its cost safety net.

---

# AI / LLM Configuration QA

- [ ] `/admin/ai` exists and is protected when the project uses any LLM-powered feature.
- [ ] Prompt template is visible and editable by an authorized admin without a code deploy.
- [ ] Expected output schema/format is visible and editable by an authorized admin.
- [ ] AI provider (Anthropic, OpenAI, Google, etc.) is set via configuration, not hardcoded.
- [ ] AI model is set via configuration, not hardcoded.
- [ ] "Refresh model pricing" action exists and shows current cost per model in use.
- [ ] Pricing refresh is admin-triggered or interval-scheduled, not called on every request.
- [ ] User-supplied content is isolated from the system prompt — no direct concatenation.
- [ ] LLM output is validated against the expected schema before use or display.
- [ ] Invalid or malformed LLM output is rejected, not silently trusted.
- [ ] Prompt, output schema, provider, and model changes are audit-logged with actor, timestamp, and diff.
- [ ] AI provider API key is never exposed client-side.
- [ ] Cost and Consumption Safety checks above apply to every LLM call in this feature.

---

# Dependency and Supply Chain QA

- [ ] No dependency added without task justification.
- [ ] Lockfile changes are expected and reviewed.
- [ ] No duplicate package added when existing utility covers the need.
- [ ] No package with known unacceptable license added.
- [ ] No abandoned/high-risk package added without approval.
- [ ] Dependency upgrade, if any, is documented.

---

# Performance QA

- [ ] No obvious unnecessary client component introduced.
- [ ] No large library imported for a small utility.
- [ ] Images use optimized loading where applicable.
- [ ] Layout shift is avoided for images/media.
- [ ] Expensive operations are not run on every render unnecessarily.
- [ ] Pagination or virtualization considered for large lists.
- [ ] API calls are not duplicated unnecessarily.
- [ ] Core page remains usable while async data loads.

---

# Monorepo and Deployment

- [ ] `pnpm install` runs cleanly from repository root.
- [ ] Turborepo build runs cleanly.
- [ ] `apps/web` builds independently.
- [ ] `apps/api` builds independently.
- [ ] Railway uses repository root by default.
- [ ] Any change to Railway root directory is explicitly documented and approved.
- [ ] No local CLI deployment was used.
- [ ] `.env.example` is up to date.
- [ ] No real secrets exist in `.env.example`.
- [ ] `.env` files are in `.gitignore`.
- [ ] Environment variables are configured in Railway dashboard or approved secret manager.
- [ ] `apps/mobile` was not built or deployed unless explicitly tasked.

---

# Documentation QA

- [ ] `TASK.md` acceptance criteria are satisfied.
- [ ] `STATUS.md` updated with current state if required.
- [ ] `ARCHITECTURE_DECISIONS.md` updated if stack or architecture changed.
- [ ] Route map updated if routes changed.
- [ ] `.env.example` updated if env vars changed.
- [ ] README or setup docs updated if developer workflow changed.
- [ ] Known gaps are documented, not hidden.

---

# Release

- [ ] Version updated if the merge changes deployable behavior.
- [ ] Release-impacting commit or merge includes version context where appropriate.
- [ ] Checkpoint branch created if this is a major update.
- [ ] `STATUS.md` updated with current state.
- [ ] `TASK.md` updated for next session if work continues.
- [ ] All gap notes from this session are logged in `STATUS.md`.
- [ ] Rollback plan exists if deployment is high risk.
- [ ] Migration rollback notes exist if schema changed.
- [ ] Smoke test plan exists for deployment-impacting changes.
- [ ] Release notes or changelog entry exists where applicable.

---

# Final QA Rule

A task cannot be marked complete if any blocker remains unresolved.

A release cannot proceed if any blocker or major issue remains unresolved without explicit written approval in `STATUS.md`.

The final response must clearly state what passed, what failed, what was not
---

## Google OAuth 2.0 QA

- [ ] Google OAuth credentials are documented in `.env.example`
- [ ] README explains how to create OAuth credentials in Google Cloud Console
- [ ] Login route redirects to Google OAuth
- [ ] Callback route handles success correctly
- [ ] Callback route handles failure with safe diagnostics
- [ ] Redirect URI exactly matches the URI configured in Google Cloud Console
- [ ] OAuth state parameter is validated
- [ ] User record is created or updated after successful login
- [ ] Session is created securely after callback
- [ ] Session cookie uses HttpOnly, Secure, SameSite settings
- [ ] Logout clears the session completely
- [ ] Current-user endpoint returns safe user data only
- [ ] Protected routes reject unauthenticated users with 401 or 403
- [ ] Failed login creates structured logs with redaction
- [ ] Failed login appears in debug diagnostics safely
- [ ] OAuth credentials are not committed to the repository
- [ ] WorkOS, Clerk, Supabase Auth, Firebase Auth, and Auth.js are not installed unless explicitly approved in `ARCHITECTURE_DECISIONS.md`

---

## Working Slice QA

- [ ] User-visible outcome is clearly defined before work starts
- [ ] Scope is confirmed before coding begins
- [ ] Slice produces something a human can see, use, or test
- [ ] Verification evidence is produced — not just claimed
- [ ] Feedback is collected before moving to the next slice
- [ ] `STATUS.md` is updated after the slice
- [ ] Next slice is proposed with a user-visible outcome

---

## Verification Loop QA

- [ ] `pnpm install` runs cleanly
- [ ] `pnpm typecheck` passes or failures are honestly reported
- [ ] `pnpm lint` passes or failures are honestly reported
- [ ] `pnpm build` passes or failures are honestly reported
- [ ] `GET /health` returns correct response
- [ ] `GET /health/deep` returns correct response or is noted as not yet implemented
- [ ] Browser verification is confirmed or honestly noted as not tested
- [ ] Changed files list is complete
- [ ] Known failures are honestly reported — none hidden

---

## Debug Diagnostics QA

- [ ] Version badge is visible in app shell
- [ ] Version badge is visible on login page
- [ ] Version badge is visible in admin panel
- [ ] Copy diagnostics button is present
- [ ] Clear cache button is present immediately next to the copy diagnostics button
- [ ] Copy diagnostics report copies to clipboard
- [ ] Report includes all required fields per `DEBUG_DIAGNOSTICS_STANDARD.md`
- [ ] Report redacts all sensitive values
- [ ] No tokens, cookies, secrets, or passwords appear in the report
- [ ] Auth diagnostics section captures required fields when login exists
- [ ] Clear cache triggers logout, cache clear, and page reload
- [ ] Debug floating panel appears when debug mode is active
- [ ] Debug floating panel does not appear in production by default
- [ ] Debug controls do not appear in customer-facing experience

---

## Deep Health QA

- [ ] `GET /health` is public and returns correct minimal response
- [ ] `GET /health/deep` is protected and requires authentication
- [ ] Deep health checks database connection
- [ ] Deep health checks migration status
- [ ] Deep health checks auth status when login exists
- [ ] Deep health checks required environment variables
- [ ] Deep health returns version, git SHA, build timestamp, and environment
- [ ] Deep health never exposes secrets, tokens, connection strings, or raw logs
- [ ] Deep health response format matches the standard in `VERIFICATION_LOOP.md`

---

## AI Developer Operating Model QA

- [ ] AI developer read all required files before starting the task
- [ ] Working slice had a clearly defined user-visible outcome
- [ ] AI developer worked autonomously inside the approved scope
- [ ] AI developer stopped and asked at security or scope boundaries
- [ ] Verification evidence was produced and shown
- [ ] `STATUS.md` was updated after the slice
- [ ] No secrets were committed
- [ ] No fake data was presented as real
- [ ] Final report followed the format in `AI_DEVELOPER_OPERATING_MODEL.md`
