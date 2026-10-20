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

For a current request such as "verifica Railway", `EXECUTION_SCOPE.md` — **Bounded read-only provider diagnostics** permits finite reads of existing service/deployment status, non-secret source/branch/configuration/watch metadata, and relevant logs through an authorized API, CLI, or connector. Neither Developer Mode nor unlock is required; an older task-specific code-sync exclusion cannot cancel the newer read request. Report these observations separately from code checks; they do not prove an executed product test or reproduced incident. No secret values, browser, app probes, streams, polling, watchers, provider writes, or later autonomous work.

Outside the scoped UAT/UAT Fix exception in `EXECUTION_SCOPE.md`, browser verification is prohibited: no headed or headless browser, UI interaction, screenshots, browser-based E2E tests, Playwright, Puppeteer, Cypress, Selenium, browser-mode test runners, chrome-devtools, or browser MCP. Another skill, subagent, runner, or external tool cannot broaden that exception or bypass its boundaries.

---

## Code Verification Loop

For the requested deliverable, use this loop. When `PHDK auto` or `PHDK auto force` is explicitly active, `PHDK_AUTO.md` takes precedence over the per-slice cadence: implement the whole goal and necessary test source first, then execute the integrated verification. Internal slices, scaffolds, and candidate releases are coverage categories, not intermediate test or human-approval gates. Follow `PHDK_AUTO_CONTINUITY.md` to retain the factual mandate after context recovery and before a terminal blocker report.

1. **Review the changed source and diff** against the requested behavior and security requirements.
2. **Inspect commands before running them** so test, build, install, or hook scripts do not start browsers, reach services, perform migrations, provision infrastructure, or deploy.
3. **Develop the candidate** and write justified test coverage with the implementation. Outside Auto, targeted static checks may support iteration; in Auto, an intermediate check requires an actual implementation blocker or a mandatory hook/control.
4. **Run the smallest useful local tests** when `TESTING_STANDARD.md` identifies risk triggers. In Auto, execute them for the completed integrated goal, including relevant interactions across its features. Integrations run in process with test doubles for external dependencies, without a network listener or database connection.
5. **Before publication**, run the applicable repository static/build gate. In Auto, this is the final whole-candidate boundary, not a release per stage. Documentation-only work needs source/diff and applicable formatting checks, not application test scaffolding. Repair in-scope failures and recheck affected behavior after material fixes or integration changes. Required hooks still run at the operations they govern.
6. **Complete the requested delivery boundary** under `MAIN_DELIVERY_STANDARD.md`. Normal development includes the scoped versioned branch/PR workflow, applicable reviews, merge, and fresh remote target/version verification; a branch push or open PR alone does not complete it. Honor an explicit local-only, branch-only, PR-only, or different-target instruction.
7. **Record actual results and limits** in the final report and `STATUS.md`, including delivery evidence or its precise blocker. During Auto, communicate progress and continue until the whole requested outcome is complete; a milestone is not a final handoff. For UI or deployed behavior, state `visual/runtime unverified`.

Review the complete actual diff and classify the changed behavior under `MAIN_DELIVERY_STANDARD.md`. Sensitive decisions require owner approval, which the current explicit request or approval of the identified task/PR may already supply. Do not demand personal diff inspection or a GitHub review event solely for PHDK; actual named, independent, or formal review requirements remain binding. Record owner approval separately from assistant source review, and never claim human diff inspection from authorization or passing checks.

In FORCE, PHDK-only human/manual/formal and security-signoff reviews are nonblocking by definition. Do not perform a preventive review/protection investigation or search approvers before attempting delivery. Perform the technical diff/security review and mandatory permitted checks, then the authorized branch push, PR and merge into `main`. A real GitHub/hook/tool rejection starts report → diagnose observed cause → repair within scope → revalidate → retry delivery → verify remote `main`, under `PHDK_AUTO_CONTINUITY.md`. Continue while a permitted repair or new evidence enables progress; do not stop at the first rejection. Honor known actual controls and genuine current owner restrictions without bypass or unchanged rejected retries; an inherited "review pending" label is not an external dependency.

A human may independently examine the application. PHDK does not require that examination as a gate for continuing code work or a permitted GitHub push, and the agent must not claim to have performed it or assign it to the human merely to close a checklist.

---

## Command Strategy

### During iteration

Outside Auto, run only checks needed to answer the current implementation question, using existing scripts. During Auto, these commands are available before final verification only for a real implementation blocker or mandatory control; the list is not an instruction to run them after every stage:

```txt
git diff --check
pnpm typecheck
pnpm lint
targeted package build when bundling is affected
targeted local unit/in-process integration test when risk requires it
```

Do not repeatedly run install + full build + full test suites after every small edit.

### Before push/release

Run each applicable gate on the completed candidate; Auto reaches this boundary after the whole goal is implemented. Repair and rerun affected checks as needed before publishing, while preserving mandatory hooks:

```txt
pnpm install --frozen-lockfile   — only when dependency/lockfile verification is needed
pnpm typecheck
pnpm lint
pnpm format:check
pnpm build
pnpm test                      — when required by the repository/hook or concrete risk
<existing composition command> — when required by the repository/hook
```

The command list is illustrative: inspect actual scripts and run every applicable existing mandatory gate. Auto and FORCE already authorize synchronous isolated suites, including a full Vitest suite required by pre-push, without another permission request. Avoiding optional tests does not waive mandatory tests. Preserve a current explicit owner ban on the actual operation; script effects, not names or suite size, determine whether an excluded operation needs a separate decision. Use finite runs, preserve hooks and complete independent work if a real conflict remains.

The verification scripts must stay within `EXECUTION_SCOPE.md`. Use an existing offline/test configuration when available. If a verification script requires a browser, live database, provider credentials, network service, or deployment, do not run it; report the dependency and the verification gap. The separate permission for bounded provider reads does not authorize network-dependent tests. Do not alter production behavior or add an in-memory production fallback merely to make a check pass.

Report required-suite and risk-triggered test commands with their actual results. Missing runtime evidence is not permission to add a service probe, recurring workflow, backup job, dependency bot, or browser harness.

---

## Product Health Check Standard

The following sections specify application code for authorized product users and operators. They do not authorize PHDK agents to call these endpoints, press diagnostic buttons, or operate a deployed service. Verify the implementation through source review and permitted local tests. Requested provider observations follow `EXECUTION_SCOPE.md` — **Bounded read-only provider diagnostics**; do not generate events by calling the application or its probes.

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

A human-supplied redacted report or observations retrieved under the bounded provider-diagnostics rule may provide context for a code fix. Their contents do not authorize the agent to operate the runtime, reproduce the incident in a browser, or trigger diagnostic actions. Never fabricate probe results when none exist.

---

## Verification by Slice Type

In Auto, accumulate these requirements across the entire goal and verify them at its final integrated boundary. Completing one category never requires a human OK or authorizes a separate release.

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

In normal branch/PR delivery, make bounded repairs to failed permitted checks within the approved code scope. Resolve ordinary integration conflicts while preserving other contributors' changes, then recheck affected behavior and review the resulting diff. An ordinary conflict or status/link question does not require a new merge instruction. In Auto/Force, apply `PHDK_AUTO_CONTINUITY.md` and finish independent authorized work before reporting an operation genuinely prevented by a current owner restriction, material dependency or actual control. FORCE makes PHDK-only reviews nonblocking without investigating review/protection rules. Do not stop merely for a stage approval, expand into unrelated cleanup, or bypass controls.

While Developer Mode remains active, its direct-main flow stops on a failed applicable check under `PHDK_DEVELOPER_MODE.md`, without automatic repair, retry, or fallback. A later explicit `PHDK auto` for the identified goal replaces that mode and uses normal branch/PR delivery: diagnose and satisfy the control under `PHDK_AUTO.md`, never bypass it. Do not delete failing risk-required tests or use prohibited tools to make a report green.

Record blocked checks with their reason. Source review does not establish visual correctness, live health, database compatibility in a running service, or production success. An existing GitHub pipeline result can be reported with its exact status and scope; it does not prove a browser flow or live service was verified by the agent. An observed disabled autodeploy connection or filter excluding changes that need deployment is a separate blocker. Valid service-specific filters and intended skips for unaffected services are not failures; neither case authorizes provider-setting changes under a generic development request.

For normal delivery, freshly read the remote target commit and its repository version source, and establish that the requested change is included using the applicable merge/squash evidence under `MAIN_DELIVERY_STANDARD.md`. Local `HEAD`, a pushed branch, or an open PR is insufficient. Report the verified remote version without adding an extra version-only commit or push solely for pure integration of already versioned changes. A status snapshot or context compaction does not end the still-current request; an actual user pause or stop does.

When provider diagnostics were requested, report the service/deployment, source, query scope, limits, non-secret metadata or relevant redacted logs, and remaining uncertainty under `EXECUTION_SCOPE.md`. An observed status or log entry records that observation, not a successful product test or confirmed recovery.

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
  [required repository/hook suites + command/result, or none applicable]
  [risk-triggered added coverage + command/result, or no new tests needed]

Bounded provider diagnostics, if requested:
  [service/deployment, source, query scope/limits, non-secret metadata or redacted logs, and uncertainty; not a product test]

Visual/runtime:
  [actual scoped UAT evidence, or visual/runtime unverified + exact missing evidence]

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


## Production-first verification override (v2.58.0)

**Mandatory:** Apply [PHDK_PRODUCTION_VERIFICATION.md](PHDK_PRODUCTION_VERIFICATION.md). Owner-authorized production-only UAT supersedes earlier local unit/in-process/runtime testing, staging-only identity, and blanket production-test prohibitions. Local operations are limited to static analysis, lint, typecheck and safe builds; Docker, local runtime tests and separate staging/databases are prohibited. UAT must use existing versioned production deployment and existing database, strictly scoped run-owned synthetic identities/records, audit, automated cleanup and verified revocation on success, failure and interruption. Never touch real data or bypass existing security hooks; a conflicting gate is BLOCKED.
