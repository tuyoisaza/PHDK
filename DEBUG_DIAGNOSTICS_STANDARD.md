# DEBUG_DIAGNOSTICS_STANDARD.md

## Purpose

This file defines the debug mode behavior, copy diagnostics report specification, and auth diagnostics requirements for all PHDK app-style projects.

Debug diagnostics exist to reduce back-and-forth between the AI developer and the human. When implemented correctly, the human can copy a diagnostics report and paste it into the next session, giving the AI developer full context without needing to re-explain what happened.

---

## When This File Applies

This file applies to all app-style projects — projects with interactive features, user flows, login, dashboards, forms, workflows, or dynamic behavior.

For static or public-only projects, debug mode is a recommended technical note, not a required implementation.

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

- All functions report verbose structured logs to the console
- A floating panel appears in the top-left corner
- The panel shows the current version number
- The panel shows the copy diagnostics button with the clear cache button immediately next to it
- Auth failures emit structured logs with safe redaction
- API failures include correlation IDs
- Frontend captures recent console, error, and network history

### Activation

- App-style projects with login: debug mode is toggled from the admin or config panel
- App-style projects without login: debug mode is toggled via environment variable or local developer config
- Debug mode is never active in production by default
- Debug mode activation must be audited when login and admin exist

---

## Clear Cache Button Behavior

When the clear cache button is pressed:

1. Clear browser cache
2. Clear service worker cache if applicable
3. Force logout if login exists
4. Force reload of cookies and session files
5. Reload the page

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

This information allows the AI developer to diagnose auth failures from a diagnostics report without the human having to describe what they saw.

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

This lets the AI developer catch a runaway loop against a metered API from the diagnostics report before it becomes an expensive incident — see `DEVSECOPS.md` Cost and Consumption Safety.

---

## Implementation Notes

### Frontend

- Capture recent console logs in a circular buffer (last 50 entries)
- Capture recent unhandled errors
- Capture recent failed fetch or axios requests (status and endpoint only)
- Do not capture request or response bodies
- Clear the buffer on clear cache

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

Before marking debug diagnostics complete, verify:

- [ ] Version badge is visible in app shell
- [ ] Version badge is visible on login page
- [ ] Version badge is visible in admin panel
- [ ] Copy diagnostics button is present
- [ ] Clear cache button is present immediately next to the copy diagnostics button
- [ ] Copy diagnostics report copies to clipboard
- [ ] Report includes all required fields
- [ ] Report redacts all sensitive values
- [ ] No tokens, cookies, secrets, or passwords appear in the report
- [ ] Auth diagnostics section captures required fields when login exists
- [ ] Auth diagnostics section redacts sensitive values
- [ ] Metered API diagnostics section captures required fields when the feature touches a metered API
- [ ] Metered API diagnostics section redacts payloads, keys, and account identifiers
- [ ] Clear cache triggers logout, cache clear, and page reload
- [ ] Debug floating panel appears when debug mode is active
- [ ] Debug floating panel does not appear in production by default
- [ ] Debug controls do not appear in customer-facing experience
