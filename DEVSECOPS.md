# DEVSECOPS.md

## Purpose

This file defines the security and operational safety baseline for all PHDK projects.

Its goal is to prevent AI developers from accidentally exposing secrets, weakening authentication, leaking private data, adding unsafe dependencies, or making risky deployment changes.

---

## Status

This file is enforced whenever work touches security-sensitive behavior.

If you are unsure whether your current task touches security-sensitive behavior, assume it does and read this file.

---

## Applies To

Read this file before touching any of the following:

- authentication
- authorization
- roles or permissions
- sessions or cookies
- OAuth flows
- environment variables
- secrets or credentials
- database access or schema
- API routes
- logs or diagnostics
- external services or integrations
- metered or paid external APIs (billing/consumption-based: AI generation, LLM calls, SMS, email sending, etc.)
- LLM prompts, AI-powered features, and AI provider/model configuration
- any feature that feeds externally-sourced content (scraped pages, CMS fields, uploaded files, third-party API responses) into an LLM call — indirect prompt injection surface
- database backups and restore procedures
- dependencies
- deployment configuration
- CI/CD
- webhooks
- file uploads
- payment behavior

---

## Core Rules

These rules are non-negotiable. They apply to every task, every session, every agent.

- Never commit secrets, tokens, API keys, or credentials to the repository
- Never print secrets, tokens, cookies, or authorization headers in logs
- Never expose raw environment variables in responses, logs, or diagnostics
- Never weaken authentication or authorization silently to make a feature work
- Never bypass RBAC checks
- Never expose private user data in diagnostics or debug reports
- Never add a dependency without a clear reason
- Never add external services without an architecture decision entry
- Never call a metered or paid external API without a hard usage cap, request timeout, and loop/retry limit
- Never ship a metered or paid integration without a kill switch that disables it immediately
- Never concatenate user-supplied content directly into an LLM system prompt without isolation/delimiting
- Never let content fetched from an external or attacker-reachable source (scraped pages, CMS fields, uploaded files, third-party API responses) trigger a tool call or side-effecting action directly — see LLM Integration Safety, Indirect Prompt Injection
- Never trust raw LLM output — validate it against the expected schema before use
- Never hardcode an LLM provider, model, or prompt string in application code
- Never build SQL queries or shell commands by concatenating unsanitized input — use parameterized queries and never pass unsanitized input to a shell
- Never perform destructive data actions unless explicitly approved in the current task
- Always validate inputs at every API boundary using Zod
- Always enforce authorization server-side on every protected route and endpoint
- Always redact sensitive data in all debug reports and copy diagnostics
- Always document security-relevant decisions in `ARCHITECTURE_DECISIONS.md`

---

## Authentication Standard

The default authentication method for all PHDK projects is custom Google OAuth 2.0.

PHDK does not use paid authentication vendors by default.

When login is required, implement Google OAuth 2.0 directly using credentials created manually in Google Cloud Console.

Do not scaffold WorkOS, Clerk, Supabase Auth, Firebase Auth, Auth.js, or any other managed auth provider unless the project explicitly overrides this standard in `ARCHITECTURE_DECISIONS.md`.

### Required Google OAuth 2.0 implementation

- OAuth credentials created manually in Google Cloud Console
- Exact redirect URI match between code and Google Cloud Console configuration
- Secure callback handling with error states
- OAuth state parameter validated on every callback
- Secure session creation after successful callback
- Secure cookie settings: HttpOnly, Secure, SameSite
- Logout endpoint that clears session completely
- Current-user endpoint that returns safe user data only
- Failed login produces structured logs with safe redaction
- Auth failures appear in debug diagnostics with full redaction of sensitive values

### Google OAuth environment variables

```env
GOOGLE_OAUTH_CLIENT_ID=""
GOOGLE_OAUTH_CLIENT_SECRET=""
GOOGLE_OAUTH_REDIRECT_URI="http://localhost:4000/auth/google/callback"
GOOGLE_OAUTH_ALLOWED_DOMAIN=""
AUTH_SESSION_SECRET=""
```

### Google OAuth credential setup

Before implementing login, create credentials manually:

1. Go to `https://console.cloud.google.com/`
2. Create or select the Google Cloud project for this app
3. Go to `Google Auth Platform` → `Branding`
4. Configure consent screen: app name, support email, authorized domains, developer contact email
5. Go to `Google Auth Platform` → `Clients`
6. Create a new client — Application type: Web application
7. Add Authorized JavaScript origins:
   - Local: `http://localhost:3000`
   - Production: `https://[production-domain]`
8. Add Authorized redirect URIs:
   - Local: `http://localhost:4000/auth/google/callback`
   - Production: `https://[api-production-domain]/auth/google/callback`
9. Save and copy credentials to environment variables
10. Never commit OAuth credentials
11. Add all required variables to Railway for the API service

---

## Authorization Rules

- Authorization must be enforced server-side on every protected route and endpoint
- Hiding UI elements is not authorization
- Role escalation must be blocked at the server layer
- Every protected API endpoint must verify the session and role before processing
- Authorization failures must return 401 or 403, never 200
- Authorization failures must be logged with correlation ID

---

## Session and Cookie Rules

- Sessions must be database-backed when login exists
- Session tokens must be signed and validated server-side
- Cookies must use: HttpOnly, Secure, SameSite=Strict or SameSite=Lax
- Session expiry must be configured
- Logout must invalidate the server-side session, not only clear the cookie
- Never store sensitive data directly in cookies

---

## Logging and Diagnostics Safety

Logs must help debugging without leaking secrets.

### Required in logs

- Structured JSON format
- Event name
- Timestamp
- Environment
- Version
- Correlation ID
- User ID if authenticated
- User role if authenticated
- Route or operation
- Result or error code

### Never include in logs

- Passwords
- Tokens
- Cookies
- API keys
- Authorization headers
- Raw secrets
- Full database connection strings
- Raw server logs
- Private request or response bodies
- Payment data
- Sensitive PII unless explicitly approved and redacted

### Auth diagnostics when login exists

Debug diagnostics must safely capture:

- Auth route reached yes/no
- Google OAuth callback reached yes/no
- Redirect URI hostname only, never full URI with tokens
- Callback success or failure
- Session detected yes/no
- Auth error stage
- Auth error code
- User ID if authenticated
- Role if authenticated
- Cookie presence summary, never cookie values
- Correlation ID

---

## Dependency Safety

Before adding any dependency, verify:

- Why it is needed and what problem it solves
- Whether existing dependencies already solve the problem
- Whether it is actively maintained
- Whether it introduces security or licensing risk
- Whether it changes deployment or infrastructure requirements

Major new dependencies require an entry in `ARCHITECTURE_DECISIONS.md`.

Do not add dependencies speculatively or to satisfy a checklist item.

---

## Environment Variable Rules

- All secrets live in environment variables, never in code
- `.env` files are always in `.gitignore`
- `.env.example` contains all required variable names with empty values
- `.env.example` never contains real secrets
- Railway environment variables are set in the Railway dashboard, never committed
- Zod validates all required environment variables on application startup
- Missing required environment variables must cause startup failure with a clear error

---

## Deployment Safety Rules

- Never deploy from local CLI — no `railway up`, no uploading a local build/tarball to Railway
- Deployment is always triggered by GitHub push to `main`, connected once per `TECHNICAL_STACK.md` First-time Railway Setup
- Both Railway services use the repository root
- Never set Railway root directory to `apps/web` or `apps/api`
- Environment variables are never committed to the repository
- Production deployments must pass all quality gates before merging to `main`

---

## Data Backup and Recovery Safety

This covers backing up the live application database. Code backup is GitHub, always, and is out of scope here — see `TECHNICAL_STACK.md` Data Backup Policy for the product-level standard and the two recommended default policies (weekly email export, weekly git backup branch).

### Required

- Every project has an explicit, documented backup policy for its database — recorded in `ARCHITECTURE_DECISIONS.md`. "No policy" is only acceptable as an explicit, dated decision, not a default by omission
- Backup job failures are logged and surfaced — a silent failed backup is the same as no backup
- Minimum retention of the last 4 weekly backups unless the developer specifies otherwise
- A restore from a real backup has been tested at least once — an unverified backup is not a backup

### If the SQL export is delivered by email

- The dump is encrypted or password-protected before it is emailed if the database holds PII, credentials, payment data, or other sensitive data
- The destination address is the developer's configured address, never a shared or public distribution list
- The email itself is treated like any other channel that can leak sensitive data — see Logging and Diagnostics Safety above

### If the SQL export is committed to a git backup branch

- Backup branches are pushed only to the same private repository — never to a public repository or a different, less-controlled repo
- The dump is never committed to `main` or any feature branch — only to dedicated, dated backup branches
- Old backup branches are pruned per the project's stated retention window
- If the database holds sensitive data, treat the backup branch with the same access controls as production secrets — a public flip of the repository would leak every historical dump

### Never

- Never assume a backup policy exists — verify it is recorded in `ARCHITECTURE_DECISIONS.md` before treating a database feature as production-ready
- Never email or commit an unencrypted dump of a database containing PII, credentials, or payment data
- Never let a backup job run unmonitored — failures must be visible, not silent

---

## Cost and Consumption Safety

Any integration billed by usage — AI/image/video generation, LLM API calls, SMS, email sending, third-party enrichment APIs, or any other metered service — must never be able to spend money without a bound. An unbounded loop or retry storm against a metered API is a production incident, not a bug.

### Required before a metered integration ships

- A hard usage cap (request count, token count, or spend ceiling) enforced in code, not just documented
- A request timeout on every call to the metered API
- A max retry limit with backoff — never retry indefinitely
- Loop protection: any code path that can call the metered API repeatedly (queues, polling, background jobs, agent loops) must have an explicit max-iterations or max-cost bound
- Idempotency keys or dedup checks on expensive operations that could otherwise be triggered twice for the same input
- A kill switch (env var or feature flag) that disables the integration immediately without a deploy
- Per-user or per-session quota where the trigger is user-initiated, to stop one user or one runaway session from exhausting the budget
- Structured logging of every metered call: operation, cost/units consumed, actor, correlation ID

### Required for visibility

- Current usage/spend against the metered API is observable — in logs at minimum, in a dashboard or `/health/deep` field where feasible
- An alert or threshold check exists for unusual spend velocity, not just a monthly total
- The debug diagnostics report includes recent metered-call counts and failures when the feature touches a metered API — see `DEBUG_DIAGNOSTICS_STANDARD.md`

### Never

- Never call a metered API inside a loop without an explicit iteration cap
- Never retry a failed metered call indefinitely
- Never let a background job or queue consumer re-process the same expensive operation without an idempotency guard
- Never scaffold a metered integration "to see if it works" without the cap and kill switch already in place
- Never treat a provider's own rate limit as the only safety net — provider limits protect the provider, not the project's budget

---

## LLM Integration Safety

Any feature that calls an LLM must be admin-manageable and provider-agnostic. See `TECHNICAL_STACK.md` AI / LLM Integration and `AGENTS.md` AI/LLM Feature Requirements for the full product spec. This section covers the security and cost-visibility requirements.

### Required

- Provider (Anthropic, OpenAI, Google, or other) and model are set via configuration, never hardcoded
- The prompt template and expected output schema are editable by an authorized admin from `/admin/ai`, without a code deploy
- User-supplied content is isolated/delimited from the system prompt — never concatenated in directly — to prevent prompt injection
- LLM output is validated against the expected schema before it is used or displayed
- Every prompt/output-schema/provider/model change is audit-logged with actor, timestamp, and diff
- The AI admin section includes a "refresh model pricing" action that fetches current per-model pricing (from the provider's published pricing or a maintained internal pricing table) and displays cost per model currently in use
- Every LLM call goes through `packages/ai`, never a provider SDK called directly from feature code, and is recorded with the full per-call token/cost schema — see `TECHNICAL_STACK.md` AI Token & Cost Observability
- Token counts come from the provider's reported `usage`, never a local estimate, when the provider reports it
- Cost and loop safeguards from Cost and Consumption Safety above apply to every LLM call

### Never

- Never let user input override or escape the system prompt
- Never trust LLM output as safe to render, execute, or store without validation
- Never hardcode a provider, model, or prompt string in application code
- Never expose the AI provider API key client-side
- Never let the pricing-refresh action call the provider on an unbounded schedule — it is admin-triggered or scheduled with a sane interval, not called on every request
- Never store full prompt or response content as part of token/cost tracking by default — that tracking is metrics and metadata only; capturing content is a separate, explicit opt-in that follows the project's data retention policy

### Indirect Prompt Injection

This is a distinct threat category from the direct-injection guardrails above, and distinct from classical injection (SQL injection, command injection) — treat all three as required, not interchangeable.

**Direct prompt injection** is an attacker typing malicious instructions into a chat or form the LLM reads directly — covered above (isolate/delimit user input from the system prompt).

**Indirect prompt injection** is different and often more dangerous: the payload arrives hidden inside data the system fetches and feeds to the LLM later — a scraped web page, a CMS field (e.g. a WordPress post's `post_content`), an uploaded file, a third-party API response, a webhook payload — and the model itself, not a deterministic parser, decides to interpret that text as an instruction instead of as data. OWASP tracks this in its own list (OWASP Top 10 for LLM Applications, LLM01: Prompt Injection — indirect subtype) rather than folding it into classical Injection (the OWASP Top 10 web A03 category) alongside SQL/command injection: the attack surface, root cause, and mitigations are structurally different — classical injection exploits a deterministic parser (the SQL engine, the shell), indirect prompt injection exploits the model's own judgment. MITRE ATLAS classifies it under AML.T0051 (LLM Prompt Injection).

It gets materially worse when combined with **Excessive Agency** (OWASP LLM08) — an integration with more permission or autonomy than the specific task needs, e.g. one API key or token valid across every connected site/tenant instead of scoped per resource, with no confirmation gate before a destructive action. The classic security framing for this combination is a **confused deputy**: the application has legitimate elevated privilege, and the attacker's hidden instruction tricks it into misusing that privilege on the attacker's behalf.

Required wherever a feature feeds externally-sourced content into an LLM call:

- Treat that content as data, never as instructions, no matter how it's phrased — it never gets to alter the system prompt, override guardrails, or trigger a tool call/action on its own
- Only an authenticated user's own explicit request, or explicit application logic, may trigger an action — never text parsed out of fetched external content
- Scope credentials and API tokens per resource/per tenant wherever the integration touches more than one external target — never one shared key with broad cross-site or cross-tenant access
- Require a confirmation/approval gate before any destructive or side-effecting action (write, delete, publish, send, purchase, etc.) that a model call driven by external content could trigger
- Structurally delimit externally-sourced content passed into a prompt (clearly labeled data blocks) so the model has a signal distinguishing it from instructions
- Log every case where externally-sourced content is passed into an LLM call, and flag it if the model's output contains action-like directives the authenticated user never asked for

This is in addition to, not instead of, classical injection protection — see Core Rules above and `QA_CHECKLIST.md` Security.

---

## Stop-and-Ask Conditions

Stop immediately and ask before performing any of the following:

- Destructive database operations: drops, truncations, irreversible migrations
- Changing or disabling the project's configured backup policy
- Authentication provider changes
- Tenant model changes
- Permission model changes
- Payment behavior changes
- Deployment architecture changes
- Adding new external services
- Adding or enabling a metered/paid external API integration before its usage cap and kill switch are in place
- Adding an LLM-powered feature before its admin-manageable prompt/output section, provider/model config, and injection guardrails are in place
- Adding a feature that feeds externally-sourced or attacker-reachable content into an LLM call before indirect-injection guardrails and least-privilege credential scoping are in place
- Changing the default AI provider or model
- Adding high-risk or large dependencies
- Weakening validation, logging, or security checks
- Force-pushing to any branch
- Pushing directly to `main` without approval (Finetuning Mode, explicitly activated for the current conversation per `DEVELOPMENT_RULES.md`, is the one standing exception — everything else still requires asking)
- Deleting branches that have not been merged

Do not proceed with these actions based on assumptions. Wait for explicit approval.

---

## Verification

Security-sensitive work is not complete until all of the following are true:

- [ ] Relevant tests pass
- [ ] Auth and permission behavior verified through the browser or test runner
- [ ] Logs are structured and redact sensitive values
- [ ] Debug diagnostics are safe and redact sensitive values
- [ ] No secrets are committed to the repository
- [ ] Any metered/paid external API touched by this work has a usage cap, timeout, retry limit, and kill switch
- [ ] Any LLM feature touched by this work has admin-manageable prompt/output, configurable provider/model, injection guardrails, and output validation
- [ ] Any LLM feature that consumes externally-sourced content has indirect-injection guardrails: content treated as data, action-triggering scoped to authenticated user requests, per-resource credential scoping, and a confirmation gate before destructive actions
- [ ] Any database work has a recorded backup policy in `ARCHITECTURE_DECISIONS.md`, or an explicit "no policy yet" decision
- [ ] `.env.example` is up to date
- [ ] `ARCHITECTURE_DECISIONS.md` updated for any security-relevant decisions
- [ ] `STATUS.md` updated with current state
