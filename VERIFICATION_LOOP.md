# VERIFICATION_LOOP.md

## Purpose

This file defines what counts as proof that a working slice is complete.

Verification is not optional. A slice is not done until evidence exists.

---

## Core Rule

Saying "it should work" is not evidence.

Saying "lint passed" alone is not evidence.

Evidence is the actual output of running commands, checking the browser, and confirming the user-visible outcome exists.

---

## Required Verification Loop

Every working slice must pass through this loop before being reported complete:

```txt
Build
→ Verify
→ Show Evidence
→ Collect Feedback
→ Revise if needed
→ Update STATUS.md
→ Next Slice
```

Do not skip any step.

Do not report completion before showing evidence.

---

## Required Evidence Types

For every working slice, provide:

### 1. Command results

Show the actual output of:

```txt
pnpm install — no errors
pnpm typecheck — pass or honest failure report
pnpm lint — pass or honest failure report
pnpm build — pass or honest failure report
pnpm test — pass, partial, or honest failure report
```

### 2. Health check result

Show the actual response from:

```txt
GET /health
```

Expected:

```json
{
  "status": "ok",
  "service": "api",
  "version": "vX.Y.Z",
  "environment": "development"
}
```

### 3. Deep health result

Show the actual response from the protected deep health endpoint when available:

```txt
GET /health/deep
```

### 4. Browser verification

Confirm one of:

- The user-visible outcome is visible in the browser
- A screenshot or visual note describes what is shown
- A Playwright or test runner result confirms the outcome

### 5. Debug diagnostics result

When debug mode is implemented, confirm:

- Copy diagnostics button is present
- Diagnostics report copies safely with redaction
- No secrets or tokens appear in the report

### 6. Changed files list

List every file that was created or modified during the slice.

### 7. Known failures or gaps

Honestly report:

- Any verification step that failed
- Any step that could not be run and why
- Any gap that was discovered during the slice

Do not hide failures. A honest failure report is more useful than a false success claim.

---

## Health Check Standard

### Simple health check

Every API service must expose a public health endpoint:

```txt
GET /health
```

This endpoint:

- Is always public, no authentication required
- Returns HTTP 200 when the service is running
- Returns the minimum required metadata

Minimum response:

```json
{
  "status": "ok",
  "service": "api",
  "version": "vX.Y.Z",
  "environment": "production"
}
```

### Deep health check

Every app-style project should expose a protected deep health endpoint:

```txt
GET /health/deep
```

This endpoint:

- Requires authentication or is restricted to admin role
- Returns detailed system verification
- Is never public

Deep health must check:

```txt
API status
Database connection
Database migrations current or behind
Auth status when login exists
Session system operational
Required environment variables present
Current version and git SHA
Deployment environment
Build timestamp
Uptime
Current working slice status if tracked
Endpoint checks relevant to completed slices
```

Deep health response format:

```json
{
  "status": "ok",
  "version": "vX.Y.Z",
  "gitSha": "a1b2c3d",
  "buildTime": "2026-03-23T18:22:00Z",
  "environment": "production",
  "uptime": 3600,
  "database": {
    "status": "connected",
    "provider": "postgresql",
    "migrations": "current"
  },
  "auth": {
    "status": "configured",
    "provider": "google-oauth-2.0",
    "sessionSystem": "operational"
  },
  "checks": [
    { "name": "database", "status": "pass" },
    { "name": "migrations", "status": "pass" },
    { "name": "auth", "status": "pass" }
  ]
}
```

### Deep health security rules

Deep health must never expose:

```txt
Raw database URLs or connection strings
Secrets or tokens
Cookies or session values
Private user data or emails
Raw stack traces
Full server logs
Sensitive environment variable values
Payment credentials
```

---

## Verification by Slice Type

### Foundation slice

- [ ] `pnpm install` runs cleanly
- [ ] `pnpm typecheck` passes
- [ ] `pnpm lint` passes
- [ ] `pnpm build` passes for web and API
- [ ] `GET /health` returns correct response
- [ ] Web app renders without errors
- [ ] README documents how to run locally
- [ ] `.env.example` is complete

### Auth slice

- [ ] Login page renders
- [ ] Google OAuth redirect works
- [ ] Callback handles success
- [ ] Callback handles failure with useful diagnostics
- [ ] Session is created after successful login
- [ ] Protected routes redirect unauthenticated users
- [ ] Logout clears session
- [ ] Current-user endpoint returns safe data
- [ ] Auth failures appear in debug diagnostics with redaction

### Feature slice

- [ ] User-visible outcome is confirmed in browser
- [ ] Route exists and renders
- [ ] Loading, empty, and error states exist
- [ ] Server-side authorization enforced
- [ ] i18n strings present for configured languages
- [ ] Structured logs exist for important actions
- [ ] No fake data presented as real

### Data slice

- [ ] Migration runs cleanly from scratch
- [ ] Data is read and written correctly
- [ ] Empty state is honest
- [ ] Error state is clear
- [ ] No raw SQL without justification
- [ ] Soft delete implemented where required
- [ ] Audit fields present where required

---

## Honest Reporting Rule

If a verification step fails or cannot be run, report it honestly:

```txt
typecheck: FAILED
  — 3 type errors in src/features/auth/service.ts
  — not blocking merge but logged as known issue

/health/deep: NOT TESTED
  — deep health not yet implemented
  — planned for next slice
```

Do not omit failures from the report.

Do not claim a gate passed if it was not run.

---

## Verification Report Format

At the end of every slice, include this verification block in the final report:

```txt
Verification:

Commands:
  pnpm install:    pass / fail
  pnpm typecheck:  pass / fail / not run
  pnpm lint:       pass / fail / not run
  pnpm build:      pass / fail / not run
  pnpm test:       pass / fail / not run / partial

Health:
  GET /health:       [response or not applicable]
  GET /health/deep:  [response or not applicable]

Browser:
  [confirmed / note / not tested]

Debug diagnostics:
  [safe / not tested / not applicable]

Changed files:
  [list]

Known failures:
  [list or none]

Gaps flagged:
  [list or none]
```
