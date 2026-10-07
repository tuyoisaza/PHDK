# DEBUG_DIAGNOSTICS_STANDARD.md

## Purpose

This file defines the debug mode behavior, copy diagnostics report specification, and auth diagnostics requirements for all PHDK app-style projects.

Debug diagnostics exist to reduce back-and-forth between the AI developer and the human. A human may supply a redacted diagnostics report as context for a code fix, without having to re-explain the failure.

---

## When This File Applies

This file applies to all app-style projects — projects with interactive features, user flows, login, dashboards, forms, workflows, or dynamic behavior.

For static or public-only projects, debug mode is a recommended technical note, not a required implementation.

---

## Product Implementation and Agent Scope

`EXECUTION_SCOPE.md` is authoritative. This document describes application features for authorized product users; it does not instruct the agent to operate them.

PHDK agents review diagnostics code and run permitted local static/build checks or risk-triggered unit/in-process integration tests. Browser APIs, OAuth, database access, network requests, and metered providers must be replaced with test doubles in those tests. Agents must not open a browser, press debug buttons, collect screenshots, copy reports from a live session, call application/health/probe endpoints, or change cloud settings. Requested non-secret provider metadata reads follow the separate boundary below; another tool, skill, or subagent cannot widen it.

For a current request such as "verifica Railway", follow `EXECUTION_SCOPE.md` — **Bounded read-only provider diagnostics**. Existing authorized API/CLI/connector access may retrieve finite service/deployment status, non-secret source/branch/configuration/watch metadata, and relevant logs. Neither Developer Mode nor unlock is required, and an older code-sync task exclusion cannot veto a newer read request. No secret values, application probes, browser use, streams, polling, watchers, writes, or recurring work. Report provider observations and user-supplied redacted diagnostics separately from source checks; retain `visual/runtime unverified` for behavior not exercised. Independent human product use is optional, never a checklist chore.

Do not create recurring diagnostics, monitoring jobs, or scheduled agents. Existing product behavior remains subject to its own authentication, redaction, and consumption controls.

---

## Required UI Controls

Near the version number in the app shell, every app-style project must include:

```txt
Copy diagnostics button — clipboard icon
Clear cache button — trash icon
```

The clear cache button must sit immediately next to the copy diagnostics button, not elsewhere in the shell — they are a single control pair so a developer can copy the report and reset state in one place, one after the other.

These controls must be visible in:

- App shell when debug mode is active
- Admin debug panel always

These controls must never appear in the customer-facing experience unless the user is an admin or developer.

---

## Debug Mode Behavior

### When debug mode is off (default)

- No floating panel
- No verbose console logs
- Normal production behavior

### When debug mode is on

- Important execution boundaries report high-signal status through the shared debug-log helper; trivial helpers are not blanket-instrumented — see `High-Signal Status Logging` below
- A floating panel appears in the top-left corner
- The panel shows the current version number
- The panel shows the copy diagnostics button with the clear cache button immediately next to it
- Auth failures emit structured logs with safe redaction
- API failures include correlation IDs
- Frontend captures recent console, error, and network history

### Activation

- App-style projects with login: debug mode is toggled from the admin or config panel
- App-style projects without login: debug mode is toggled via environment variable or local developer config
- **In every non-production environment (local, dev, preview, staging) debug mode defaults to ON.** It is not an opt-in the developer has to remember to flip — a fresh clone or a fresh deploy to a non-production environment must show the debug panel and populate the console without any manual setup step.
- Debug mode is never active in production by default
- Before a production release or promotion, review the code and committed configuration that keep the forced-on default limited to non-production. Cover risky default-selection logic with local tests when needed; do not change live environment settings or retrieve secret values. Requested bounded non-secret provider observations are separate evidence, not a completion gate or a product test. Record production runtime state as unverified. See `Debug Diagnostics QA` and `QA_CHECKLIST.md`.
- Debug mode activation must be audited when login and admin exist

---

## Clear Cache Button Behavior

Implement the following behavior for an authorized human pressing the clear cache button:

1. Clear browser cache
2. Clear service worker cache if applicable
3. Force logout if login exists
4. Force reload of cookies and session files
5. Reload the page

The action may clear only application-accessible cache/session state; it must report any browser-managed or platform state it cannot clear. It must never delete durable business data. This behavior is reviewed in code and tested with local adapters when risk warrants it; the agent does not press the control or reset a user's session.

This resolves the most common vibe-coding debugging pain point: stale cache causing confusing behavior that looks like a bug.

---

## Copy Diagnostics Report

### What the report must include

```txt
project name
environment
version
git SHA
build timestamp
client timestamp
current route
locale and timezone
browser name and version
viewport dimensions
screen size
auth state — authenticated yes/no
user ID if authenticated
user role if authenticated
feature flags
debug mode state
API base URL — hostname only, never full URL with tokens
/health status
deep-health status if available
DB provider if available
recent frontend logs — last 20 entries
recent frontend runtime errors
recent failed API requests — endpoint and status only
safe backend diagnostics if available
recent API errors with correlation IDs
last endpoint probe — id, method, path, expected status, actual status, latency, correlation ID
sanitized request/response examples for the affected registered endpoint
current correlation ID
recent metered API call counts and failures, if the feature touches a metered API
```

### What must always be redacted

```txt
passwords
tokens of any kind
cookies and cookie values
API keys
authorization headers
secrets
private user data
payment data
sensitive environment variable values
full database connection strings
raw server logs
full URLs containing tokens or private query params
request or response bodies unless explicitly sanitized
```

### Report format

The copy diagnostics button copies a structured text report:

```txt
=== PHDK Debug Diagnostics Report ===

Project: [name]
Environment: [development / staging / production]
Version: [vX.Y.Z]
Git SHA: [shortSHA or unavailable]
Build: [UTC timestamp or unavailable]
Client: [UTC timestamp]

Route: [current route]
Locale: [locale]
Timezone: [timezone]
Browser: [name and version]
Viewport: [width x height]
Screen: [width x height]

Auth: [authenticated yes/no]
User ID: [ID or not authenticated]
Role: [role or not authenticated]

Debug mode: [on/off]
Feature flags: [list or none]

API: [hostname only]
/health: [status or unavailable]
/health/deep: [status or unavailable / protected]
DB provider: [provider or unavailable]

Recent frontend logs:
[last 20 entries or none]

Recent errors:
[list or none]

Recent failed API requests:
[endpoint and status code only, or none]

Endpoint probe:
[id / method / path / probe mode / expected / actual / latency / correlation ID, or none]

Expected example:
[sanitized example or unavailable]

Correlation ID: [ID]

=== End of Report ===
[SENSITIVE VALUES REDACTED]
```

---

## Auth Diagnostics Requirements

When login exists, diagnostics must safely capture the following without exposing sensitive data:

```txt
Auth route reached — yes/no
Google OAuth redirect triggered — yes/no
OAuth callback reached — yes/no
Redirect URI — hostname only, never full URI with tokens or state params
Callback result — success/failure
Session detected — yes/no
Auth error stage — which step failed
Auth error code — safe error code only
User ID — if authenticated
Role — if authenticated
Cookie presence — summary only, never cookie values
Correlation ID
```

This information lets the AI developer trace likely code faults from a supplied diagnostics report without operating the login flow or accessing the OAuth provider.

---

## Metered API / Cost Diagnostics Requirements

When a feature calls a metered or paid external API (AI/image/video generation, LLM calls, SMS, email sending, etc.), diagnostics must safely capture:

```txt
Metered API name/provider
Call count in current session or last N minutes
Failure count and last failure reason
Retry count on the most recent call
Usage cap configured — yes/no
Kill switch state — enabled/disabled
Correlation ID
```

Never include request or response payloads from the metered API, and never include API keys or provider account identifiers.

This lets a supplied report identify code paths that may need a bounded retry, quota, or kill-switch fix — see `DEVSECOPS.md` Cost and Consumption Safety. The agent does not query provider billing, invoke the metered integration, or operate the kill switch as verification. Requested provider observations remain governed by `EXECUTION_SCOPE.md` — **Bounded read-only provider diagnostics**.

---

## Implementation Notes

### Frontend

- Capture recent console logs in a circular buffer (last 50 entries)
- Capture recent unhandled errors
- Capture recent failed fetch or axios requests (status and endpoint only)
- Do not capture request or response bodies
- Clear the buffer on clear cache

### High-Signal Status Logging

The goal is diagnostic signal, not log volume.

Every project exposes one shared debug-log helper (for example `debugLog(scope, status, detail)`) that writes structured entries into the diagnostic buffer. Ad hoc `console.log` calls do not satisfy this requirement.

When debug mode is active, instrument **important execution boundaries**, not every helper function:

- API route entry/result and client API calls
- auth and authorization decisions
- form submissions and meaningful mutations
- service operations containing business rules
- database/migration/import state transitions
- existing product background jobs and queue consumers, when present; this is not an instruction to create or schedule them
- metered or paid external API calls
- caught errors that affect user-visible behavior

Do not add entry/success/failure logging to pure helpers, trivial getters, rendering-only functions, or other low-signal code merely to satisfy a rule.

When debug mode is off, debug-only logging is a no-op or minimal-overhead path.

Source review must confirm that important new execution boundaries propagate correlation IDs into relevant safe logs. Local tests cover risky logging/redaction behavior with synthetic fixtures; a live request or probe is not a completion requirement.

### Endpoint Diagnostics Console

App-style projects expose an authorized Diagnostics section in `/admin/system` or `/admin/debug`.

It consumes the endpoint diagnostic registry defined in `VERIFICATION_LOOP.md` and shows:

- endpoint id, method, path, and purpose
- auth and role requirements
- probe mode
- sanitized request example
- sanitized success and common-error examples
- expected status codes
- last actual status and latency
- correlation ID
- safe related log summary
- a human-operated **Test** button only when the registered probe mode permits safe execution
- human-triggered **Run safe probes** for the registered safe modes, without creating a schedule
- **Copy diagnostics** for the current result

The endpoint registry is the source of truth. Do not maintain a second manually duplicated list in the UI.

Unsafe, destructive, private, or metered operations must be `manual_only`, `validation_only`, or true `dry_run`; diagnostics must never create real side effects just to prove health. These are product controls, not agent verification tools. PHDK agents do not execute even a `safe_read` probe against a service.

### Backend

- Include correlation ID in every API response header
- Include correlation ID in every error response
- Expose safe diagnostics through `/health/deep` when available
- Do not include sensitive data in any diagnostic response

### Version badge component

The version badge must:

- Display in app shell, login page, and admin panel
- Show format: `vX.Y.Z (shortSHA · UTC timestamp)`
- Include copy diagnostics button with clipboard icon, and the clear cache button with trash icon immediately next to it — always paired, never separated elsewhere in the UI
- Be positioned consistently — top area of the shell or admin panel
- Never obstruct primary UI

---

## Debug Diagnostics QA

Before marking diagnostics code complete, record source references and applicable permitted local checks for these requirements. A checked item confirms the implementation evidence only; it does not claim the UI was rendered or a live action succeeded.

- [ ] Source mounts the version badge in the app shell, login page, and admin panel.
- [ ] Source pairs Copy diagnostics and Clear cache controls immediately next to each other.
- [ ] Clipboard handler and report formatting are wired; any local test stubs the clipboard API.
- [ ] Report schema includes all required fields and handles unavailable data honestly.
- [ ] Redaction excludes passwords, tokens, cookies, secrets, private data, and sensitive URLs.
- [ ] Auth diagnostics map the required safe fields when login exists.
- [ ] Metered diagnostics map counts, failures, retry bounds, cap/kill-switch state, and correlation IDs without payloads, keys, or provider account identifiers.
- [ ] Clear-cache handler implements authorized cache/session reset and reload, reports unsupported clearing, and cannot delete durable data.
- [ ] Floating-panel visibility depends on debug mode and the authorized role.
- [ ] Code defaults debug mode to ON in non-production and OFF in production; risky default-selection changes have a local test.
- [ ] Production runtime state is not claimed from source/configuration review.
- [ ] Important execution boundaries emit structured correlated diagnostics without blanket logging on trivial helpers.
- [ ] Endpoint registry access and diagnostic actions enforce admin/developer permissions server-side.
- [ ] Probe-mode guards refuse unsafe automatic execution; local tests use fake probes when these security boundaries change.
- [ ] Request/success/error examples are sanitized.
- [ ] Failure-report mapping includes expected/actual status, latency, correlation ID, and safe log context when available.
- [ ] Diagnostic buffering collects meaningful bounded entries and does not invent successful live results.
- [ ] No browser, application/health/probe request, metered integration call, service administration, or recurring job was used as verification.
- [ ] Any requested provider observations followed `EXECUTION_SCOPE.md` — **Bounded read-only provider diagnostics**, including finite query limits and redaction; non-secret metadata and relevant logs are reported as diagnostic evidence rather than a product test.
- [ ] Final evidence states `visual/runtime unverified` for the actual UI and deployed behavior.
