# VERIFICATION_LOOP.md

## Purpose

This file defines what counts as proof that a working slice is complete.

PHDK is **diagnostics-first**: verify the real running path as directly as possible, then add automated tests only when the risk profile justifies them.

Verification is not optional. Expensive ceremony is.

---

## Core Rule

"It should work" is not evidence.

A giant test suite is also not proof that the live system is healthy.

Prefer the shortest path to trustworthy evidence:

```txt
targeted static checks
→ live health
→ affected endpoint probe
→ browser/user-visible confirmation when applicable
→ copy diagnostics
→ risk-triggered automated test only when justified
```

Do not create a separate synthetic harness when the real application can answer the question safely.

---

## Clinical Verification Loop

For every working slice:

1. **Check the changed surface** — typecheck/lint the affected code; do not repeatedly run the whole world while iterating.
2. **Run the app or target service** and confirm `GET /health`.
3. **Run protected deep health** and the probes relevant to the changed path.
4. **Confirm the user-visible outcome** in the browser when the slice has UI.
5. **Copy the diagnostics report** for failures or meaningful verification.
6. **Run risk-triggered automated tests** only if `TESTING_STANDARD.md` says the slice needs them.
7. **Before push/release**, run the full required static/build gate once.
8. Record failures honestly and update `STATUS.md`.

The goal is high-signal evidence with the least duplicated work.

---

## Command Strategy

### During iteration

Run only the narrow checks needed to answer the current question. Examples:

```txt
pnpm typecheck
pnpm lint
targeted package build when the change affects bundling
GET /health
GET /health/deep
one affected endpoint probe
```

Do not repeatedly run install + full build + full test suites after every small edit.

### Before push/release

Run once:

```txt
pnpm install --frozen-lockfile   — when dependencies/lockfile need verification
pnpm typecheck
pnpm lint
pnpm format:check
pnpm build
```

If the current slice triggered mandatory automated tests, also run the smallest relevant test command and report it separately.

---

## Health Check Standard

### Public health

Every API service exposes:

```txt
GET /health
```

It is public and minimal.

Example:

```json
{
  "status": "ok",
  "service": "api",
  "version": "vX.Y.Z",
  "environment": "production"
}
```

It must never expose secrets, configuration values, private data, or verbose internals.

### Protected deep health

Every app-style project exposes an admin-protected endpoint:

```txt
GET /health/deep
```

It returns safe operational state and the **endpoint diagnostic registry**.

Deep health checks, when applicable:

- API/runtime status
- database connectivity
- migration state
- auth/session configuration
- required environment-variable presence — names/status only, never values
- version, git SHA, build timestamp, environment, uptime
- metered-provider configuration/circuit-breaker state without secrets
- endpoint registry and latest safe probe results
- current correlation ID / diagnostic run ID

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

### Probe modes

Each endpoint is explicitly classified:

- **safe_read** — can be called directly; no mutation or external cost.
- **validation_only** — verifies routing/auth/validation without performing the side effect.
- **dry_run** — executes only with a true rollback/sandbox/dry-run guarantee.
- **manual_only** — destructive, financially consequential, privacy-sensitive, or otherwise unsafe to trigger automatically.

Never automatically execute `manual_only` probes.

Never call a metered API merely to make health green.

---

## Protected Probe Endpoint

Admin tooling may execute a named diagnostic probe through:

```txt
POST /health/deep/probes/:id
```

This endpoint:

- requires admin/developer authorization
- runs only the registered probe mode
- refuses unsafe automatic execution
- returns sanitized evidence, not unrestricted payloads
- attaches a correlation ID
- records latency and outcome
- never returns secrets, tokens, cookies, raw stack traces, or private response bodies

Example result:

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

---

## Admin Diagnostics Verification

For app-style projects, `/admin/system` or `/admin/debug` exposes a Diagnostics section with:

- **Run safe probes** button
- one row/card per registered endpoint
- method + path + purpose
- auth/role requirement
- probe mode
- **Test** button when the probe is safe to execute
- expected statuses
- sanitized request example
- sanitized success/error examples
- last actual status and latency
- correlation ID
- related safe log summary
- **Copy diagnostics** action

A failing endpoint should produce enough sanitized information that the report can be pasted directly into the IDE/AI coding session without the human re-explaining the failure.

---

## Browser Verification

When the slice changes UI, confirm the actual user-visible outcome in a browser.

A screenshot or concise visual note is enough unless the risk profile requires automated E2E coverage.

Do not create Playwright automation simply because a page exists.

---

## Debug Diagnostics Evidence

When debug diagnostics are implemented, verify:

- diagnostics UI is accessible only to authorized roles
- safe probes execute correctly
- failure evidence includes a correlation ID
- Copy Diagnostics produces a useful redacted report
- no secrets or unrestricted raw logs appear

---

## Verification by Slice Type

### Foundation

- [ ] install succeeds when dependencies changed
- [ ] typecheck/lint/format/build pass before push
- [ ] `GET /health` returns the minimal response
- [ ] protected `GET /health/deep` works for app-style projects
- [ ] admin diagnostics console can display the endpoint registry
- [ ] Copy Diagnostics works with redaction
- [ ] web app renders without runtime errors

### Auth / authorization

- [ ] auth configuration is visible in protected diagnostics without secrets
- [ ] unauthorized request is denied
- [ ] wrong-role request is denied
- [ ] successful authorized path works
- [ ] auth failures have correlation IDs and safe logs
- [ ] mandatory automated authorization test exists when the boundary changed

### Feature

- [ ] user-visible outcome works
- [ ] affected endpoint is represented in the diagnostic registry
- [ ] relevant safe probe passes, or failure is captured
- [ ] loading/empty/error states are honest
- [ ] structured logs exist at important execution boundaries
- [ ] no fake production data is presented as real

### Data / destructive changes

- [ ] migration/state transition was verified against the correct non-production target
- [ ] deep health reports migration state
- [ ] destructive behavior is never triggered by an automatic health probe
- [ ] rollback/recovery path is known
- [ ] risk-triggered automated test exists when required by `TESTING_STANDARD.md`

---

## Honest Reporting Rule

If something fails or cannot be verified, say so. Do not loop indefinitely trying alternate synthetic scripts to make the report green.

Example:

```txt
Endpoint probe: FAIL
  id: reports.list
  GET /api/reports → 500
  correlation_id: req_82fd91
  database: pass
  auth: pass
  copy diagnostics: attached

Automated tests: not required for this slice
```

A high-quality failure report is valid evidence. It tells the next iteration exactly where to work.

---

## Verification Report Format

```txt
Verification:

Static/build gate:
  typecheck:     pass / fail / not run
  lint:          pass / fail / not run
  format:check:  pass / fail / not run
  build:         pass / fail / not run

Health:
  GET /health:       [result]
  GET /health/deep:  [result / not applicable]

Affected probes:
  [endpoint id → pass/fail, status, latency, correlation ID]

Browser:
  [confirmed / note / not applicable]

Diagnostics:
  [copied / safe / failure report reference]

Automated tests:
  [not required + reason] OR [required trigger + command/result]

Changed files:
  [list]

Known failures / gaps:
  [list or none]
```
