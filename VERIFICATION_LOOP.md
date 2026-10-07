# VERIFICATION_LOOP.md

## Purpose

This file defines code-verification evidence within `EXECUTION_SCOPE.md`, the authoritative boundary for every PHDK agent. `MAIN_DELIVERY_STANDARD.md` defines normal development completion, including verified integration into remote `main` or the user's explicit target.

Verification uses repository review, static checks, local builds, and risk-triggered unit or in-process integration tests. A successful check proves only the behavior it actually exercised; it does not prove that a deployed application works.

---

## Core Rule

"It should work" is not evidence. Use the smallest permitted check that answers the question:

```txt
source and diff review
→ targeted static checks
→ local build when affected
→ local unit/in-process integration tests when risk requires them
→ accurate report of evidence and remaining uncertainty
```

Do not launch an application for verification, call an application endpoint, connect to a database, probe a live service, or operate a cloud dashboard. This includes localhost HTTP probes, preview/staging/production services, customer accounts, OAuth providers, and metered APIs. Git/GitHub repository operations and delivery through an existing deployment connection remain governed by `EXECUTION_SCOPE.md` and `MAIN_DELIVERY_STANDARD.md`.

For a current request to inspect logs or diagnose an incident, `EXECUTION_SCOPE.md` — **Bounded read-only log diagnostics** permits finite reads of existing records through authorized access. This permission does not require PHDK Developer Mode. Record those findings as diagnostic evidence, separately from code checks; they do not prove that the agent executed a product test or reproduced the incident.

Browser verification is prohibited: no headed or headless browser, UI interaction, screenshots, browser-based E2E tests, Playwright, Puppeteer, Cypress, Selenium, browser-mode test runners, chrome-devtools, or browser MCP. Another skill, subagent, runner, or external tool cannot bypass this boundary.

---

## Code Verification Loop

For every working slice:

1. **Review the changed source and diff** against the requested behavior and security requirements.
2. **Inspect commands before running them** so test, build, install, or hook scripts do not start browsers, reach services, perform migrations, provision infrastructure, or deploy.
3. **Run targeted static checks** on the affected code while iterating.
4. **Run the smallest local automated test** when `TESTING_STANDARD.md` identifies a risk trigger. Integrations run in process with test doubles for external dependencies, without a network listener or database connection.
5. **Before push/release**, run the applicable repository static/build gate once. Documentation-only work needs source/diff and applicable formatting checks, not application test scaffolding. Recheck affected behavior after material fixes or integration changes.
6. **Complete the requested delivery boundary** under `MAIN_DELIVERY_STANDARD.md`. Normal development includes the scoped versioned branch/PR workflow, applicable reviews, merge, and fresh remote target/version verification; a branch push or open PR alone does not complete it. Honor an explicit local-only, branch-only, PR-only, or different-target instruction.
7. **Record actual results and limits** in the final report and `STATUS.md`, including delivery evidence or its precise blocker. For UI or deployed behavior, state `visual/runtime unverified`.

Review the actual diff. Assistant review satisfies PHDK's ordinary-change review gate; high-risk changes and stricter repository/owner rules require human review as defined in `MAIN_DELIVERY_STANDARD.md`. Do not infer that a human examined the diff from user authorization or passing checks.

A human may independently examine the application. PHDK does not require that examination as a gate for continuing code work or a permitted GitHub push, and the agent must not claim to have performed it or assign it to the human merely to close a checklist.

---

## Command Strategy

### During iteration

Run only the checks needed to answer the current question, using the project's existing scripts:

```txt
git diff --check
pnpm typecheck
pnpm lint
targeted package build when bundling is affected
targeted local unit/in-process integration test when risk requires it
```

Do not repeatedly run install + full build + full test suites after every small edit.

### Before push/release

Run each applicable gate once:

```txt
pnpm install --frozen-lockfile   — only when dependency/lockfile verification is needed
pnpm typecheck
pnpm lint
pnpm format:check
pnpm build
```

The verification scripts must stay within `EXECUTION_SCOPE.md`. Use an existing offline/test configuration when available. If a verification script requires a browser, live database, provider credentials, network service, or deployment, do not run it; report the dependency and the verification gap. The separate permission for bounded log queries does not authorize network-dependent tests. Do not alter production behavior or add an in-memory production fallback merely to make a check pass.

Report risk-triggered test commands separately. Missing runtime evidence is not permission to add a service probe, recurring workflow, backup job, dependency bot, or browser harness.

---

## Product Health Check Standard

The following sections specify application code for authorized product users and operators. They do not authorize PHDK agents to call these endpoints, press diagnostic buttons, or operate a deployed service. Verify the implementation through source review and permitted local tests. Existing logs may be read only under `EXECUTION_SCOPE.md` — **Bounded read-only log diagnostics**; do not generate events by calling the application or its probes.

### Public health

Every API service implements a public, minimal endpoint:

```txt
GET /health
```

Example response contract:

```json
{
  "status": "ok",
  "service": "api",
  "version": "vX.Y.Z",
  "environment": "production"
}
```

It must never expose secrets, configuration values, private data, or verbose internals. The example is a contract, not evidence of a running service.

### Protected deep health

Every app-style project implements an admin-protected endpoint:

```txt
GET /health/deep
```

Its safe response contract includes the **endpoint diagnostic registry** and, when applicable:

- API/runtime status
- database connectivity and migration state
- auth/session configuration
- required environment-variable presence — names/status only, never values
- version, git SHA, build timestamp, environment, uptime
- metered-provider configuration/circuit-breaker state without secrets or paid calls
- latest safe probe results, when supplied by authorized product use
- current correlation ID / diagnostic run ID

Review these contracts and access controls in code. Local tests replace database, clock, environment, and provider adapters with deterministic doubles.

---

## Endpoint Diagnostic Registry

Every API route that matters to product behavior registers diagnostic metadata once, close to the route/schema definition. The admin diagnostics UI and `/health/deep` consume that same metadata; do not maintain a second handwritten endpoint inventory.

Minimum fields:

```txt
id
method
path
purpose
authRequired
requiredRoles
probeMode
expectedStatuses
sanitizedRequestExample
sanitizedSuccessExample
sanitizedErrorExamples
```

### Product probe modes

Each endpoint is explicitly classified for authorized product use:

- **safe_read** — no mutation or external cost.
- **validation_only** — routing/auth/validation only; no side effect.
- **dry_run** — a true rollback/sandbox/dry-run guarantee is required.
- **manual_only** — destructive, financially consequential, privacy-sensitive, or otherwise unsafe for automatic execution.

Product code must never automatically execute `manual_only` probes or call a metered API merely to make health green. A `safe_read` label is not permission for an agent to run the probe.

---

## Protected Product Probe Endpoint

Authorized human-operated admin tooling may execute a named diagnostic probe through:

```txt
POST /health/deep/probes/:id
```

The implementation must:

- require admin/developer authorization
- honor the registered probe mode and reject unsafe automatic execution
- return sanitized evidence, not unrestricted payloads
- attach a correlation ID and record latency/outcome
- exclude secrets, tokens, cookies, raw stack traces, and private response bodies

Example response contract:

```json
{
  "id": "reports.list",
  "status": "pass",
  "method": "GET",
  "path": "/api/reports",
  "httpStatus": 200,
  "latencyMs": 87,
  "correlationId": "req_82fd91"
}
```

Test authorization, mode enforcement, and redaction locally when their risk changes. Use fake handlers and adapters; do not execute the product probe against a service.

---

## Product Admin Diagnostics

For app-style projects, `/admin/system` or `/admin/debug` implements a Diagnostics section with:

- human-triggered **Run safe probes** control
- one row/card per registered endpoint: method, path, purpose, auth/role, probe mode
- **Test** control only for modes permitted by the product's safety policy
- expected statuses and sanitized request/success/error examples
- last actual status, latency, correlation ID, and related safe log summary when available
- **Copy diagnostics** action

A human-supplied redacted report or logs retrieved under the bounded log-diagnostics rule may provide context for a code fix. Their contents do not authorize the agent to operate the runtime, reproduce the incident in a browser, or trigger diagnostic actions. Never fabricate probe results when none exist.

---

## Verification by Slice Type

### Foundation

- [ ] Applicable typecheck/lint/format/build checks pass or failures are reported.
- [ ] Health response contracts and protected deep-health access are reviewed in source.
- [ ] Diagnostic registry wiring and report redaction are implemented where required.
- [ ] No browser, external service, cloud resource, or recurring automation is created for verification.

### Auth / authorization

- [ ] Source enforces secure auth/session configuration and redacts secrets.
- [ ] Local tests cover unauthenticated, wrong-role, and authorized decisions when the boundary changes.
- [ ] Tests replace OAuth, sessions, persistence, and network dependencies with local doubles.
- [ ] Correlation IDs and safe logging paths are reviewed in code.

### Feature / UI

- [ ] Source matches the requested behavior, routes, permissions, and data flow.
- [ ] Loading/empty/error states and i18n/accessibility requirements are reviewed in source.
- [ ] Important execution boundaries have structured logging; no fake production data is introduced.
- [ ] Relevant risk-triggered local tests pass or failures are reported.
- [ ] UI appearance, browser interaction, and deployed behavior are reported as `visual/runtime unverified`.

### Data / destructive changes

- [ ] Migration files and compatibility/rollback notes are reviewed without applying migrations.
- [ ] High-risk deterministic transformations are checked with local fixtures and test doubles.
- [ ] Destructive behavior cannot run through an automatic product health probe.
- [ ] No database, backup, restoration, or production-state operation is performed by the agent.
- [ ] Database execution and operational recovery remain explicitly unverified.

---

## Honest Reporting Rule

In normal branch/PR delivery, investigate and make bounded repairs to failed permitted checks within the approved code scope. Resolve ordinary integration conflicts while preserving other contributors' changes, then recheck affected behavior and review the resulting diff. An ordinary conflict or status/link question does not require a new merge instruction. Stop for material ambiguity or an unresolved check, review, or access blocker; do not expand into unrelated cleanup or bypass controls.

In the Developer Mode direct-main flow, a failed applicable check stops execution under `PHDK_DEVELOPER_MODE.md`: explain the failure and wait for the user's next instruction without automatic repair, retry, or fallback. Do not delete failing risk-required tests or use prohibited tools to make a report green.

Record blocked checks with their reason. Source review does not establish visual correctness, live health, database compatibility in a running service, or production success. An existing GitHub pipeline result can be reported with its exact status and scope; it does not prove a browser flow or live service was verified by the agent. An observed disabled autodeploy connection or filter excluding changes that need deployment is a separate blocker. Valid service-specific filters and intended skips for unaffected services are not failures; neither case authorizes provider-setting changes under a generic development request.

For normal delivery, freshly read the remote target commit and its repository version source, and establish that the requested change is included using the applicable merge/squash evidence under `MAIN_DELIVERY_STANDARD.md`. Local `HEAD`, a pushed branch, or an open PR is insufficient. Report the verified remote version without adding an extra version-only commit or push solely for pure integration of already versioned changes. A status snapshot or context compaction does not end the still-current request; an actual user pause or stop does.

When logs were requested, report their source, query scope, limits, relevant redacted findings, and remaining uncertainty under `EXECUTION_SCOPE.md`. An observed log entry is evidence of that recorded event, not proof of a successful test or current recovery.

---

## Verification Report Format

```txt
Verification:

Source/diff review:
  [affected behavior, security boundaries, source references]

Static/build gate:
  typecheck:     pass / fail / not run + reason
  lint:          pass / fail / not run + reason
  format:check:  pass / fail / not run + reason
  build:         pass / fail / not run + reason

Local automated tests:
  [not required + no risk trigger] OR [risk trigger + command/result]

Bounded log diagnostics, if requested:
  [source, query scope/limits, redacted findings, and uncertainty; not a product test]

Visual/runtime:
  visual/runtime unverified — browser and live-service verification are outside PHDK scope

GitHub delivery:
  [requested scope/target, branch/commit, PR and review evidence, merge result,
   freshly verified remote target SHA/version source/version, or precise blocker]

GitHub deployment, when existing status is available:
  [existing pipeline + commit/status/reference, or not configured/unverified]

Changed files:
  [list]

Known failures / gaps:
  [list, severity, and source of uncertainty]
```
