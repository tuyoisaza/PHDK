# BUILD_APP_FOUNDATION_PROMPT.md

## Purpose

This file contains the prompt to give to an AI coding agent after a Project Handoff to Development Kit (PHDK) has been generated.

Its job is to build the initial scalable app foundation for a project using the standard PHDK stack.

This is not a folder-only scaffold.
This is not a fake demo app.
This is not random feature development.

This prompt builds the reusable technical foundation that future product features will be built on.

---

## How to Use This File

1. Create or open the project GitHub repository.
2. Add the PHDK project-specific files to the repository.
3. Fetch the latest standards files from the PHDK standards repo.
4. Open your AI coding agent, such as Claude Code, Cursor, Windsurf, or equivalent.
5. Paste the prompt below as the first build task.
6. The AI coding agent must build the app foundation according to the PHDK project mode.
7. Apply `QA_CHECKLIST.md` to the requested deliverable. During an active Auto goal, foundation items join the final integrated verification after all requested feature work; they are not an intermediate approval or test gate.

---

# Prompt

## Requested Foundation Work

Run this prompt when foundation work is explicitly requested or is a necessary part of the current authorized goal under `PHDK_AUTO.md`. Reading, editing, or quoting it does not start a build, activate Auto/Developer Mode, or resume earlier work.

Preserve the whole current requested goal. This template does not pause or replace an active Auto goal.

Use **Build App Foundation** as the implementation step described below.

Build the initial scalable foundation using the PHDK files and standards. When Auto includes later features, continue through all of them without a scaffold release or separate approval.

The execution boundary is code and repository documentation, git/GitHub, and deployment through an existing GitHub-connected pipeline. Read `EXECUTION_SCOPE.md` and `MAIN_DELIVERY_STANDARD.md` before planning. A current foundation-build request includes normal reviewed delivery through verified remote `main` integration unless the user explicitly narrows delivery or the user/repository names another target. This prompt does not authorize browser use, infrastructure operations, or recurring automation.

Honor current user pause/stop instructions; do not invent one from this template.
Do not build project-specific product features unless explicitly required by the current request; use `TASK.md` as context, not stored authorization.
Do not create fake dashboards, fake data, fake analytics, fake users, fake payments, fake integrations, or fake business logic.
Do not skip validation.
Do not mark the task complete until applicable quality gates, required reviews, and the requested delivery boundary are satisfied.

Give a brief progress update, for example:

```txt
I will build the foundation within the current requested scope.
I will read the PHDK files and standards before making changes.
If this is part of the active Auto goal, I will continue its remaining features before final verification.
```

---

## Execution Boundary

- One assistant normally completes the current requested outcome. A standalone foundation request ends at foundation delivery; within Auto, the foundation is one step of the whole goal. Explicit PMO may assign the foundation as a bounded workstream to a supported in-session worker. No unattended Mission Autopilot, delegation outside PMO, recursive worker delegation, background work, or new unrequested goal.
- Work on code and documentation inside the project repository. The current build request normally includes the scoped branch, repository version bump, applicable local checks, version-prefixed commit, push, PR, review, merge, and fresh remote `main` version verification under `MAIN_DELIVERY_STANDARD.md`. Respect explicit local-only, branch-only, PR-only, or different-target instructions; a branch push/open PR alone does not finish normal delivery.
- Current authorization persists through status/link questions, same-conversation turns, context compaction, and assistant-written task snapshots. Do not ask for a repeated merge order. Actual user pause/stop instructions win; saved task/handoff text grants no authority in a different conversation.
- Review the complete actual diff. Owner approval of a sensitive decision may already be supplied by the current explicit request or identified-task/PR approval under `MAIN_DELIVERY_STANDARD.md`; do not impose a universal personal diff-inspection or GitHub-review-event gate. Preserve actual named, independent, or formal reviews and record approval separately from source review. Resolve ordinary integration conflicts preserving others' changes, then recheck affected behavior. Never bypass checks, hooks, required reviews, or access controls.
- Route a current `PHDK unlock` to `PHDK_UNLOCK.md` for PHDK/local documentary blocker repair and its scoped delivery. Current owner instructions can replace older documentary exceptions; the command does not disable controls, resume unnamed old work, or authorize a foundation build by itself.
- Follow explicitly activated `PHDK auto` under `PHDK_AUTO.md`: implement all agreed behavior and necessary test coverage, perform final integrated verification, repair in-scope failures, and complete normal branch/PR delivery without stage approvals or releases. Earlier checks require an actual implementation blocker or mandatory hook/control. `PHDK salir de auto` exits the mode; examples and generated files never activate it.
- `PHDK_DEVELOPER_MODE.md` applies only after an explicit activation command in the current conversation. This foundation prompt does not activate it or classify a full bootstrap as a small, low-risk change. Never persist active mode or authority for another conversation in generated files.
- Deployment may use only a pipeline already connected to GitHub and its configured deployment branch, recorded in `TASK.md`. Preserve valid provider GitHub autodeploy/watch paths; do not generate dummy never-matching filters or disable the connection under the no-autonomy/Actions rules. Report an observed disabled connection or filter excluding changes that need deployment as a separate blocker; valid service-specific filters and intended skips for unaffected services are not failures. Do not create a pipeline, change triggers/settings, or configure provider dashboards, secrets, environments, databases, or repository settings.
- Do not create or enable Dependabot, Renovate, scheduled GitHub Actions, cron jobs, recurring agents, backup jobs, periodic probes, or preview environments.
- Do not open, control, or test a browser, including headless browsers, screenshots, UI flows, or browser testing through a skill, plugin, MCP server, or subagent.
- Validate with code/diff review, lint, typecheck, formatting, build, and risk-triggered local non-browser tests. In Auto, these cover the entire completed goal at final verification before publication, not only this foundation stage. Tests remain isolated from running applications and real services; use in-process doubles and inspect scripts for indirect browser or infrastructure effects. Required hooks still run at the operations they govern.
- Health endpoints, diagnostics panels, auth flows, and integration adapters are product code. Implementing them does not authorize operating the app, invoking live probes, configuring credentials, or connecting external services.
- A current "verifica Railway" or similar request permits finite existing service/deployment status, non-secret source/branch/configuration/watch metadata, and relevant logs through authorized API/CLI/connector access under `EXECUTION_SCOPE.md` — Bounded read-only provider diagnostics. No Developer Mode or unlock is needed; an older code-sync task exclusion cannot veto that newer read. No secret values, streams, polling, watchers, app/database probes, or provider writes; these diagnostics are not a foundation gate.
- Put this boundary and the existing deployment target, if any, in `TASK.md` and `ARCHITECTURE_DECISIONS.md`. Replace obsolete handoff instructions that require browser checks, external administration, or recurring automation; do not carry them into the foundation plan.
- Missing infrastructure is outside PHDK's execution scope. Continue independent code work and report the precise dependency without making external setup a foundation completion gate. Do not claim runtime or deployment verification that was not performed.

`EXECUTION_SCOPE.md` is the canonical rule when another prompt or external skill suggests broader action.

---

## Step 1 — Read Required Files

Before writing or changing code, read these files:

### Project-specific PHDK files

- `README.md`
- `STATUS.md`
- `TASK.md`
- `PROJECT_BRIEF.md`
- `PRD.md`
- `FEATURES.md`
- `NAVTREE.md`
- `PUBLIC_CONTENT.md`
- `PRIVATE_CONTENT.md` if it exists
- `ARCHITECTURE_DECISIONS.md`

### Standards files

- `AGENTS.md`
- `EXECUTION_SCOPE.md`
- `MAIN_DELIVERY_STANDARD.md`
- `PHDK_AUTO.md` when explicitly active for the current goal
- `PHDK_DEVELOPER_MODE.md` when explicitly invoked in the current conversation
- `DEVELOPMENT_RULES.md`
- `DESIGN_RULES.md`
- `TECHNICAL_STACK.md`
- `QA_CHECKLIST.md`
- `BUILD_APP_FOUNDATION_PROMPT.md`

After reading, respond with:

```txt
PHDK and standards read.
Project mode identified: [public / authenticated / hybrid / unclear]
Login required: [yes / no / unclear]
Foundation scope understood.
Proceeding with implementation plan.
```

Resolve project mode and login from the current brief and existing code. If a material decision remains genuinely missing, complete independent authorized work before asking only for that decision; do not restart a setup interview in Auto.

---

## Step 2 — Identify Project Mode

Use the PHDK files to classify the foundation mode.

### Public mode

Use this when login is not required.

Build a public-facing scalable web app foundation.

Do not build:

- login
- dashboard
- account area
- user CRUD
- roles
- admin panel
- private routes
- session tables
- fake authenticated states

### Authenticated mode

Use this when login and accounts are required.

Build a web app foundation with authentication-ready and role-aware structure.

Build only the auth/account/admin pieces required by the PHDK.

Do not assume every authenticated app needs full SaaS admin CRUD unless the PHDK requires it.

### Hybrid mode

Use this when the project has both public marketing pages and a logged-in app area.

Build:

- public marketing/content shell
- login/account foundation
- private app shell
- role-aware navigation only where required

### Unclear mode

Use the current brief and existing behavior before treating mode as unknown. If the public/authenticated/hybrid decision is genuinely missing, isolate that dependency, complete independent authorized work, and ask one precise question. Do not invent login requirements or make a missing mode label stop the whole Auto goal.

---

## Step 3 — Standard Technical Architecture

Use the PHDK standard stack:

- pnpm
- Turborepo
- TypeScript monorepo
- `apps/web` — Next.js web app
- `apps/api` — NestJS + Fastify API
- `apps/mobile` — future Expo placeholder only
- `packages/*` — shared core packages
- Tailwind CSS
- shadcn/ui-compatible structure
- Zod validation
- Drizzle/PostgreSQL-ready when persistence is needed
- Redis-ready when cache is needed
- Stripe-ready only when payments are needed
- Custom Google OAuth 2.0-ready when login is needed
- OpenTelemetry-ready and Sentry-ready, but not implemented until the relevant task
- Deployment through an existing GitHub-connected pipeline, when one is already available and deployment is part of the task

If that existing deployment uses Railway:

- document the build/start commands for `@repo/web` and `@repo/api` using the repository root
- do not create services or change their root directories, environment variables, or provider settings

---

## Step 4 — Required Monorepo Foundation

Create or verify this structure:

```txt
apps/
  web/
  api/
  mobile/
packages/
  ui/
  types/
  validators/
  api-client/
  design-tokens/
  observability/
  db/
  config/
.env.example
.gitignore
package.json
pnpm-workspace.yaml
turbo.json
tsconfig.base.json
README.md
```

### Package responsibilities

- `packages/ui` — reusable UI primitives and app-shell components
- `packages/types` — shared TypeScript types
- `packages/validators` — shared Zod schemas
- `packages/api-client` — typed API client used by web now and mobile later
- `packages/design-tokens` — spacing, colors, typography, radius, shadows, motion
- `packages/observability` — logger and diagnostics wrappers
- `packages/db` — database package; implementation only when persistence is required
- `packages/config` — shared config actually used by apps/packages

Do not create unused placeholder config files.
Do not duplicate shared logic across apps.

---

## Step 5 — Root Workspace Requirements

Use pnpm only.

Do not generate:

- `package-lock.json`
- `npm-shrinkwrap.json`
- `yarn.lock`

Root scripts must include:

```json
{
  "scripts": {
    "dev": "turbo dev",
    "build": "turbo build",
    "start": "turbo start",
    "lint": "turbo lint",
    "typecheck": "turbo typecheck",
    "format": "turbo format",
    "format:check": "turbo format:check"
  }
}
```

Do not add a root `test` script or install test runners until a risk-triggered local non-browser test is actually required by `TESTING_STANDARD.md`. When that happens, add the smallest needed tooling and script. Never install or run browser test tooling for foundation verification.

Use workspace protocol imports for internal packages where appropriate:

```json
{
  "dependencies": {
    "@repo/types": "workspace:*",
    "@repo/validators": "workspace:*",
    "@repo/api-client": "workspace:*"
  }
}
```

Required package names:

- `apps/web` package name: `@repo/web`
- `apps/api` package name: `@repo/api`
- `packages/ui` package name: `@repo/ui`
- `packages/types` package name: `@repo/types`
- `packages/validators` package name: `@repo/validators`
- `packages/api-client` package name: `@repo/api-client`
- `packages/design-tokens` package name: `@repo/design-tokens`
- `packages/observability` package name: `@repo/observability`
- `packages/db` package name: `@repo/db`
- `packages/config` package name: `@repo/config`

---

## Step 6 — Build `apps/api`

Build a NestJS + Fastify API foundation.

Required behavior:

- bind to `0.0.0.0`
- read `process.env.PORT`
- default to `4000` locally
- expose public `GET /health`
- implement the public health response contract in `VERIFICATION_LOOP.md` Product Health Check Standard, including the version metadata required by `VERSIONING.md`; verify the handler in source or permitted in-process tests

Required API structure:

```txt
apps/api/src/
  main.ts
  app.module.ts
  modules/
    health/
  common/
    guards/
    pipes/
    interceptors/
    filters/
    decorators/
  config/
  observability/
```

Rules:

- use Zod validation at API boundaries where inputs exist
- return structured errors with stable error codes
- log important actions through `@repo/observability`
- do not expose raw error internals to clients
- do not add database/auth/payment integrations unless their code is required by the project mode and PHDK task; do not provision or call the real services

### If login = yes

Add auth-ready API structure only as required by PHDK.

Allowed:

- current user endpoint if needed
- protected-route guard structure
- role-check utility structure if roles are required
- server-side authorization boundaries

Do not create fake users or fake roles.
Do not create full user CRUD unless required by the PHDK.

### If login = no

Do not create auth endpoints, session endpoints, user management endpoints, role endpoints, or private API routes.

---

## Step 7 — Build `apps/web`

Build a Next.js web foundation.

Required:

- Next.js App Router
- React
- TypeScript strict
- Tailwind CSS
- shadcn/ui-compatible structure
- centralized design tokens from `@repo/design-tokens`
- shared UI primitives from `@repo/ui`
- typed API calls through `@repo/api-client`
- responsive mobile-first layout
- accessibility-ready structure
- light/dark mode readiness
- app version visible in a developer-safe location
- client-side API health check that does not require the API during build

Required route behavior:

- public routes come from `NAVTREE.md`
- do not invent routes not supported by the PHDK
- every meaningful route must handle loading, empty, error, and success states where relevant
- browser zoom must not break layout
- no tiny tap targets
- no inaccessible color contrast

### If login = yes

Build the login/account/private foundation required by the PHDK.

Allowed if required:

- login route
- protected app shell
- account route
- dashboard route
- admin/config route
- role-aware navigation
- private route guards

Do not create full admin modules unless explicitly required.
Do not create fake account data.
Do not create user CRUD unless required.

### If login = no

Build only public routes and public workflows.

Do not create:

- login page
- dashboard
- account area
- admin panel
- role navigation
- user profile pages

---

## Step 8 — Shared Packages

### `packages/types`

Include shared TypeScript types used by both web and API.

Must include `HealthResponse` matching:

```ts
export type HealthResponse = {
  status: "ok";
  service: "api";
};
```

### `packages/validators`

Include shared Zod schemas.

Must include health schema matching:

```ts
{ "status": "ok", "service": "api" }
```

### `packages/api-client`

Build a typed API client consumed by `apps/web`.

Must include a health request helper.

Use `NEXT_PUBLIC_API_URL` as the API base URL.

The web build must not require the API to be reachable.

### `packages/design-tokens`

Define tokens for:

- colors
- spacing
- typography
- radius
- shadows
- motion
- light mode
- dark mode

### `packages/ui`

Build reusable UI primitives only.

Allowed:

- Button
- Card
- AppShell
- VersionBadge
- DebugPanel shell if debug mode is required
- CopyDiagnosticsButton if debug mode is required

Do not build project-specific product UI inside `packages/ui`.

### `packages/observability`

Build a minimal logger and diagnostics wrapper.

Use a tiny wrapper around `console` unless the PHDK explicitly requires a real logging package.

Methods:

- `info`
- `warn`
- `error`
- optional `debug` when debug mode is enabled

Never log:

- passwords
- tokens
- cookies
- API keys
- authorization headers
- secrets
- sensitive PII unless explicitly approved and redacted

### `packages/db`

If persistence is not required yet, keep this documentation-only or minimal.

If persistence is required by the PHDK, implement according to `TECHNICAL_STACK.md` and `DEVELOPMENT_RULES.md`.

Keep schema, migrations, and adapters in the repository. Do not provision databases, apply migrations to real databases, or configure backups.

Do not add database code just to satisfy a checklist.

### `packages/config`

Include only config files that are actually imported or extended.

Do not create unused placeholder configs.

---

## Step 9 — Debug Foundation

Debug mode is a developer-support capability, not an end-user feature.

### App-style projects

If the project has interactive features, user flows, login, dashboards, forms, workflows, or dynamic behavior, include debug mode foundation.

### Static or public-only projects

If the project is a public marketing site, landing page, or simple content site, include debug mode as a recommended technical note or environment-gated developer utility, not as visible product UI.

### Required behavior when implemented

These are requirements for the generated product code. Validate their implementation statically or with isolated non-browser tests; do not open the diagnostics UI, start application services for verification, or invoke live endpoints/probes.

- debug mode is off by default in production
- debug mode can be enabled only through safe developer/admin control
- important execution boundaries emit high-signal structured logs when active; do not blanket-log every helper function
- diagnostic payloads include useful context
- protected deep health exposes the endpoint diagnostic registry
- authorized admin diagnostics can run safe endpoint probes and show sanitized request/response examples
- diagnostic payloads redact sensitive values
- activation is auditable when login/admin exists

### Copy diagnostics report

If debug diagnostics are implemented, the report must include this sanitized payload:

```txt
project name
environment
version
git SHA
build timestamp
client timestamp
current route
locale and timezone
browser info and viewport
screen size and viewport size
user ID if authenticated
user role if authenticated
auth state if applicable
feature flags
debug mode state
API base URL hostname only
DB provider if available
recent frontend logs
safe backend diagnostics if available
recent client errors
recent API errors with correlation IDs
last endpoint probe with expected/actual status and latency
sanitized expected request/response example for the affected endpoint
correlation ID
```

Always redact:

```txt
passwords
tokens
cookies
API keys
authorization headers
secrets
private user data
payment data
sensitive environment variables
full connection strings
raw server logs
```

Never copy unrestricted raw server logs.
Never include full URLs containing tokens or private query parameters.
Never include request or response bodies unless explicitly sanitized.

---

## Step 10 — Environment Variable Documentation

Create `.env.example` at repository root.

Use placeholders only. Do not create or rotate credentials, change provider/GitHub secrets, or connect infrastructure.

Minimum:

```env
# App
APP_NAME=""
APP_ENV="development"
APP_VERSION="0.0.1"
APP_GIT_SHA=""
APP_BUILD_TIME=""

# Web
NEXT_PUBLIC_API_URL="http://localhost:4000"

# API
PORT="4000"
NODE_ENV="development"

# Debug
DEBUG_MODE="false"
```

Add only relevant future placeholders based on PHDK scope.

Examples:

```env
# Future database
DATABASE_URL=""

# Future cache
REDIS_URL=""

# Future auth — Google OAuth 2.0
GOOGLE_OAUTH_CLIENT_ID=""
GOOGLE_OAUTH_CLIENT_SECRET=""
GOOGLE_OAUTH_REDIRECT_URI=""
GOOGLE_OAUTH_ALLOWED_DOMAIN=""
AUTH_SESSION_SECRET=""

# Future payments
STRIPE_SECRET_KEY=""
STRIPE_WEBHOOK_SECRET=""

# Future observability
SENTRY_DSN=""
OTEL_EXPORTER_OTLP_ENDPOINT=""
```

Do not wire unused services yet.

Create `.gitignore` including:

```txt
.env
.env.local
.env.*.local
node_modules
.next
dist
.turbo
*.db
```

---

## Step 11 — i18n Readiness

Do not hardcode user-facing text in a way that makes future translation difficult.

If the PHDK defines supported languages or requires i18n:

- configure the selected i18n system
- create locale files
- route all user-facing strings through the i18n system
- use locale-aware formatting for dates, numbers, currency, and pluralization

If i18n is not required yet:

- keep user-facing strings centralized and easy to extract later
- do not overbuild full translation infrastructure unless requested

---

## Step 12 — Data Honesty Rules

Production must never show fake data as real.

Allowed states:

- empty state
- setup required state
- missing integration state
- loading state
- error state
- success state with real data

Never allowed:

- fake KPIs
- random numbers
- demo analytics presented as real
- placeholder totals without clear disclosure
- fake users
- fake payments
- fake database records

---

## Step 13 — Documentation Output

Update or create project README documentation explaining:

- how to install
- how to run locally
- how to run web and API together
- how to run typecheck, lint, format checks, build, and any required isolated non-browser tests
- app mode: public/authenticated/hybrid
- the existing GitHub deployment branch/pipeline, or `not connected` if none is known
- build/start commands for the configured target
- required environment variables
- how to use the PHDK files
- how `PHDK unlock` routes a current blocker-repair request to `PHDK_UNLOCK.md`, preserving hooks/protections and leaving old missions inactive
- how explicit `PHDK auto` / `PHDK salir de auto` routes to `PHDK_AUTO.md` for full-goal implementation, final integrated verification, and normal delivery without stage approvals
- how to use `TASK.md` as context for the current goal or next explicit request, without resuming stored work or persisting Auto/Developer Mode

For an existing Railway deployment, document these commands:

API service:

```bash
pnpm --filter @repo/api build
pnpm --filter @repo/api start
```

Web service:

```bash
pnpm --filter @repo/web build
pnpm --filter @repo/web start
```

The commands assume the repository root. They are documentation for the existing target, not instructions for the agent to create or reconfigure services.

Do not create GitHub Actions or require external setup to complete the code foundation. Document runtime behavior as unverified where it cannot be established with allowed checks.

---

## Step 14 — Enforcement & Diagnostics Scaffolding

Implement repository code and configuration from `ENFORCEMENT.md`, `VERIFICATION_LOOP.md`, and `DEBUG_DIAGNOSTICS_STANDARD.md` within `EXECUTION_SCOPE.md`. In Auto, complete this and all other requested implementation before final verification; do not remove or delay an actual hook at its governed operation.

### Tier 1 — mechanical enforcement (`ENFORCEMENT.md`)

- Configure Husky (or the project's chosen git-hooks tool) with `commit-msg`, `pre-commit`, and `pre-push` hooks per `ENFORCEMENT.md` Git Hooks
- Configure Prettier (`.prettierrc`, `.prettierignore`) as the canonical formatter per `TECHNICAL_STACK.md`, wired into `pre-commit` via `lint-staged` so staged files are auto-formatted, not just checked
- Add a pre-commit secrets scan per `ENFORCEMENT.md` Secrets Scanning
- Configure `pre-push` to validate every outgoing commit message and run the required local static/build gate: lint, typecheck, build, and format:check, per `ENFORCEMENT.md`. Isolated non-browser tests are task-level and risk-triggered, not a universal hook requirement
- Do **not** scaffold GitHub Actions, new CI/deployment workflows, Dependabot, Renovate, schedules, or automatic dependency updates. Use the existing GitHub deployment pipeline only when release is in scope
- Do not change GitHub branch protection, merge methods, secrets, or repository/provider settings. Existing settings remain constraints on the release; configuring them is not a bootstrap task or completion gate

### Tier 2 — context-persistence (`ENFORCEMENT.md`)

- Generate the current tool's native always-loaded rule file (`CLAUDE.md`, `.cursor/rules/phdk.mdc`, `.windsurfrules`, or project-root `AGENTS.md`) per `ENFORCEMENT.md` Tool-native always-loaded rule files — only for the tool actually in use, not all four speculatively

### Diagnostics product code

- Implement protected `GET /health/deep` for app-style projects
- Implement the endpoint diagnostic registry defined in `VERIFICATION_LOOP.md`
- Implement authorized `POST /health/deep/probes/:id` execution for safe/validation/dry-run probes
- Add the Diagnostics section to `/admin/system` or `/admin/debug` with Run safe probes, per-endpoint Test, examples, status/latency/correlation ID, and Copy diagnostics
- Implement these capabilities as code for authorized product users; do not invoke them as agent verification or schedule their execution
- Do **not** scaffold a test harness by default; browser testing tools are prohibited
- Add only isolated non-browser test tooling when `TESTING_STANDARD.md` identifies a concrete risk trigger

---

## Step 15 — Quality Gates

For a standalone foundation delivery, verify the items below before claiming completion. Within Auto, retain them as coverage for the entire goal's final integrated verification after all requested features are implemented; a finished scaffold is not a test, release, or human-approval boundary. Inspect scripts for allowed behavior and use repository review, local static/build commands, or isolated tests. Do not start the app, access live endpoints, open browsers, or change external settings:

- `pnpm install` runs cleanly from repository root
- `pnpm typecheck` passes or failures are reported honestly
- `pnpm lint` passes or failures are reported honestly
- `pnpm format:check` passes or failures are reported honestly
- `pnpm build` passes or failures are reported honestly
- `pnpm dev` is wired to web and API through Turborepo in repository scripts; runtime startup is outside agent verification
- API startup code binds to `0.0.0.0`
- API startup code uses `process.env.PORT`, defaulting to `4000` locally
- the `GET /health` handler implements the canonical response and version metadata from `VERIFICATION_LOOP.md` and `VERSIONING.md`
- web health-call code uses `@repo/api-client`
- web build does not require the API to be running
- shared types and validators are actually imported and used
- package names use the `@repo/*` names
- internal package dependencies use `workspace:*` where appropriate
- public/private routes match the PHDK login branching rule
- no unauthorized auth/dashboard/admin code exists in public-only mode
- debug mode is off by default in production
- diagnostic reports redact sensitive data
- no fake data is presented as real
- no file exceeds the line limit defined in `DEVELOPMENT_RULES.md`
- no secrets are committed
- README documents the existing GitHub deployment target or records that none is connected; no new deployment setup was performed
- available LSP/code intelligence or text-search access is reported honestly; installing external tool integrations is not a foundation gate
- repository git-hook definitions (`commit-msg`, `pre-commit`, `pre-push`) enforce the allowed local commands; do not create deliberate bad commits or remote pushes to prove them
- no external administration or confirmation of repository/provider settings was made a foundation gate
- the current tool's native always-loaded rule file exists per `ENFORCEMENT.md` Tier 2
- protected `GET /health/deep` and endpoint registry code exist for app-style projects and have been reviewed or tested in-process
- admin diagnostics code enforces safe-probe permissions and sanitized outputs; browser/runtime behavior is not claimed verified
- no test runner was scaffolded without a concrete risk trigger
- no browser checks, live-service probes, recurring jobs/bots/agents, or new CI/deployment workflows were added or executed
- CORS allowlist, CSP, and standard security headers are configured on `apps/api` per `DEVSECOPS.md` HTTP Security Headers
- rate-limiting code is configured globally and specifically on auth endpoints per `DEVSECOPS.md` Rate Limiting
- source-changing commits update the repository's actual version source and use version-prefixed subjects per `VERSIONING.md`; pure merge/squash integration of already versioned changes requires no extra bump, post-merge version-only commit, or second push
- normal delivery includes required review, integration into remote `main` or the explicit target, and fresh target commit/version evidence under `MAIN_DELIVERY_STANDARD.md`; report an explicit narrower delivery scope or precise blocker when applicable
- owner approval, assistant source review, and any actual named/independent/formal review are recorded separately; current approval is not replaced by an invented GitHub-review-event or personal diff-inspection requirement

If an allowed quality gate cannot be run, explain why. Report browser/runtime verification as outside scope; it is not a pending gate for the agent.

Do not claim success if an applicable required check failed or was not run, an actual required review/access blocker remains, or the whole requested delivery boundary has not been reached. In Auto, repair in-scope final-verification failures and recheck affected behavior before publication; finish independent work before reporting an unresolved blocker. No additional PHDK-only human acceptance is needed. Developer Mode direct-main hard stops apply while that mode remains active; explicit Auto replaces it for the identified goal under `PHDK_AUTO.md`, preserving the failed control.

---

## Final Report Format

Use this final report only for a standalone foundation outcome. If the foundation is an internal Auto step, give a progress update and continue the remaining goal; do not end the turn or publish a stage release because this template has a report. Choose `APP FOUNDATION COMPLETE` only when the actual requested outcome and delivery boundary are satisfied; otherwise identify the precise unfinished scope or blocker:

```txt
[APP FOUNDATION COMPLETE / APP FOUNDATION DELIVERY BLOCKED / APP FOUNDATION INCOMPLETE]

Project mode:
[public / authenticated / hybrid]

Repository structure:
[list of created directories and key files]

Routes created:
[list]

API endpoints created:
[list]

Shared packages created:
[list]

Debug foundation:
[implemented / documented only / not applicable + reason]

Quality gates:
[pass/fail/not run for each item]

Delivery scope:
[normal main / explicit different target / explicit local-only, branch-only, or PR-only scope]

GitHub delivery:
[branch, versioned commit, PR/review, merge result, fresh remote target SHA/version source/version; or precise blocker/narrower scope]

Deployment:
[existing GitHub pipeline commit/status/reference / not connected / unverified; separate from code and integration evidence]

Verification limits:
[what code checks establish; browser and live-runtime behavior not verified]

Warnings or gaps:
[list or "none"]

Next step:
[stop only after the whole requested outcome and verified delivery; in Auto continue any remaining agreed features, final verification, and repairs. Keep unrequested follow-ups inactive; report a precise blocker only after independent work is complete]
```

---

## Non-Negotiable Rules

- Build this foundation within the requested scope; an Auto goal also includes its explicitly agreed product features.
- Respect the PHDK files as the product source of truth.
- Respect the standards files as the technical source of truth.
- Do not invent features.
- Do not fake integrations.
- Do not add auth if login = no.
- Do not add admin/dashboard/user CRUD unless required.
- Do not invent mobile app features outside the current request.
- Keep `apps/mobile` as a future placeholder unless its implementation is explicitly included in the current goal.
- Use pnpm only.
- Follow `EXECUTION_SCOPE.md` and `MAIN_DELIVERY_STANDARD.md`: repository code and normal reviewed git/GitHub delivery, with deployment only through an existing connected pipeline.
- Do not operate browsers, configure infrastructure/settings, or create recurring automation.
- Do not claim success without validation.
