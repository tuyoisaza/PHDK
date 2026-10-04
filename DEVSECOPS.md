# DEVSECOPS.md

## Purpose

This file defines the security and operational safety baseline for all PHDK projects.

Its goal is to prevent AI developers from accidentally exposing secrets, weakening authentication, leaking private data, adding unsafe dependencies, or making risky deployment changes.

`EXECUTION_SCOPE.md` is the execution boundary. These standards govern repository code and local verification; they do not authorize the PHDK agent to configure or operate cloud services, real databases, external secrets, dashboards, scheduled jobs, or provider integrations. Deployment uses only the existing GitHub-connected push pipeline. Product security and diagnostics remain code requirements, tested without a browser or real-service calls.

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
- migration compatibility and user-supplied recovery requirements in repository documentation
- dependencies
- deployment configuration
- repository build/start configuration for an existing deployment pipeline
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
- Never create or operate external services from the PHDK agent; document any external prerequisite of requested integration code
- Application code that calls a metered or paid API must enforce a hard usage cap, request timeout, and loop/retry limit; the PHDK agent verifies it with test doubles and never invokes the live API
- Never ship a metered or paid integration without a kill switch that disables it immediately
- Never concatenate user-supplied content directly into an LLM system prompt without isolation/delimiting
- Never let content fetched from an external or attacker-reachable source (scraped pages, CMS fields, uploaded files, third-party API responses) trigger a tool call or side-effecting action directly — see LLM Integration Safety, Indirect Prompt Injection
- Never trust raw LLM output — validate it against the expected schema before use
- Never hardcode an LLM provider, model, or prompt string in application code
- Never build SQL queries or shell commands by concatenating unsanitized input — use parameterized queries and never pass unsanitized input to a shell
- Never execute destructive actions on live data; proposed data-changing code and migrations require the appropriate review and isolated verification
- Always validate inputs at every API boundary using Zod
- Always enforce authorization server-side on every protected route and endpoint
- Always redact sensitive data in all debug reports and copy diagnostics
- Always document security-relevant decisions in `ARCHITECTURE_DECISIONS.md`
- Always configure CORS as an explicit origin allowlist, CSP as default-deny, and the standard security header set — see HTTP Security Headers below
- Always enable request rate limiting on every API service, with a stricter limit on auth endpoints — see Rate Limiting below
- Always report a committed, logged, or otherwise exposed secret immediately and correct the repository code that caused the exposure; provider rotation is outside PHDK — see Secrets Rotation and Compromise Response below

---

## Authentication Standard

The default authentication method for all PHDK projects is custom Google OAuth 2.0.

PHDK does not use paid authentication vendors by default.

When login is required, implement Google OAuth 2.0 directly using environment-driven credential references. PHDK does not create credentials or operate Google Cloud Console.

Do not scaffold WorkOS, Clerk, Supabase Auth, Firebase Auth, Auth.js, or any other managed auth provider unless the project explicitly overrides this standard in `ARCHITECTURE_DECISIONS.md`.

### Required Google OAuth 2.0 implementation

- Credential names and callback requirements documented without real secret values
- Exact redirect URI validation in code, with existing provider configuration treated as an external prerequisite
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

### Google OAuth verification boundary

Verify state validation, callback parsing, session creation, cookie flags, authorization failures, and error redaction with local unit or in-process tests using mocked OAuth and database adapters. Do not open a browser, complete a real sign-in, or contact Google or a live application endpoint.

Cloud projects, consent screens, OAuth clients, allowed origins, and real secret values are external prerequisites. Document required names and callback paths in `.env.example` and repository documentation. If external configuration is unknown, report that limit; do not create or change it and do not make it an extra code-completion gate.

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

### Keeping Existing Dependencies Patched

Dependency updates are discrete code tasks requested by the user. Change only the relevant package declarations, lockfile, and compatibility code; explain the version change and run the applicable local static/build and isolated test checks before the normal git/GitHub review flow.

- Do not configure Dependabot, Renovate, maintenance agents, scheduled scans, recurring update PRs, or automatic merging
- Do not turn a foundation build, ordinary feature task, or discovered package age into an unsolicited update campaign
- Security fixes and minor/major upgrades still need a clear scope, dependency review, and verification appropriate to the change
- Report a security issue found during the task without starting a recurring maintenance process

---

## HTTP Security Headers

Every `apps/api` service sets these regardless of whether the project has "gotten to security yet" — they are foundation-slice defaults, not a later hardening pass.

Required:

- **CORS**: an explicit allowlist of origins (the deployed `apps/web` origin, plus `http://localhost:3000` in development) — never a wildcard `*` origin on any route that accepts credentials/cookies
- **CSP** (`Content-Security-Policy`): default-deny (`default-src 'self'`), with explicit allowances only for what the project actually serves (fonts, images, the API origin for `connect-src`) — never `unsafe-inline`/`unsafe-eval` without a documented reason in `ARCHITECTURE_DECISIONS.md`
- **HSTS** (`Strict-Transport-Security`): enabled in production with a sane max-age; not required in local development
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY` (or the CSP `frame-ancestors` equivalent) — unless the project explicitly needs to be framed, which is itself a Stop-and-Ask condition
- `Referrer-Policy: strict-origin-when-cross-origin` or stricter

Implementation: Fastify's `@fastify/helmet` (NestJS's Fastify adapter) sets sane defaults for the header set above — configure it at foundation build, not left to be added "when it matters." Next.js sets its own headers via `next.config.js` `headers()` for `apps/web`.

### Never

- Never set CORS to allow all origins (`*`) on any endpoint that reads or sets cookies
- Never ship a CSP that is effectively disabled (`default-src *` or missing entirely) because it was easier to get the app working
- Never disable these headers to "fix" a CORS or CSP error during development — fix the allowlist instead

---

## Rate Limiting

Rate limiting is required, not optional or merely "considered" — this section is the concrete requirement `QA_CHECKLIST.md` Security checks against.

Required:

- Every `apps/api` service has request rate limiting configured globally (e.g. `@nestjs/throttler` on the Fastify adapter) with a sane default (e.g. 100 requests/minute per IP) — foundation-slice default, not deferred
- Authentication endpoints (`/auth/google`, `/auth/google/callback`, any login/password-adjacent route) have a stricter, dedicated limit than the global default — this is brute-force protection, not general traffic shaping
- Rate-limit rejections return `429` with a structured log entry (see Logging and Diagnostics Safety), never a silent drop
- Rate limits are configurable per environment — a tight production limit should not make local development or CI unusable

### Never

- Never rely on a provider's own rate limit (Railway, Cloudflare, the LLM provider) as the only protection for the app's own endpoints — see Cost and Consumption Safety above for the equivalent rule on metered APIs
- Never exempt the login/auth endpoints from rate limiting because "it's just for testing"

---

## Secrets Rotation and Compromise Response

Environment Variable Rules cover prevention. When a secret is suspected or confirmed exposed, distinguish repository remediation from provider operations: removing a value from new code does not revoke it, and PHDK does not perform provider rotation.

Required:

- Keep credentials environment-driven so application code can accept replacement values without hardcoding them
- Report the affected credential type and exposure location immediately without repeating the value; a secret in git history remains exposed even after removal from the current file
- Remove the unsafe value from the current repository state, fix the logging/configuration path that leaked it, and verify the correction locally without the real credential
- State that revocation/rotation and deployment-environment updates remain outside PHDK and unverified unless the user supplies evidence of their completion
- Implement session-secret validation and invalidation behavior in code, and test it with dummy secrets and in-process session adapters

### Never

- Never claim an exposed credential is safe merely because the current code no longer contains it
- Never open provider dashboards, rotate external secrets, inspect live secret stores, or update deployment environments from the PHDK agent
- Never rewrite git history as routine remediation; any proposed history change remains subject to the existing authorization rules in `VERSIONING.md`

---

## Environment Variable Rules

- All secrets live in environment variables, never in code
- `.env` files are always in `.gitignore`
- `.env.example` contains all required variable names with empty values
- `.env.example` never contains real secrets
- Real deployment environment values are managed outside PHDK; the agent does not retrieve, set, or rotate them
- Zod validates all required environment variables on application startup
- Missing required environment variables must cause startup failure with a clear error

---

## Deployment Safety Rules

- Deploy only through an authorized GitHub push/merge to the existing connected pipeline and established release branch, per `EXECUTION_SCOPE.md`
- Do not create services, pipelines, CI/task workflows, scheduled deployments, or preview environments
- Do not use a provider dashboard, provider API/CLI, local artifact upload, or manual provider redeploy/rollback
- Repository build/start configuration may be updated for the existing target; no external service settings are changed
- Existing deployment triggers are preserved; no schedule, branch-trigger expansion, or maintenance workflow is added
- Environment variables are never committed to the repository
- Apply local code verification and the existing GitHub review rules before release; no browser, live HTTP, database, or metered-API probes
- Roll back through a reviewable revert or code fix on the same GitHub path; report deployment status only to the extent supported by available GitHub evidence

---

## Privacy and Legal Baseline

This is a documentation and process baseline, not a legal compliance guarantee — PHDK does not provide legal advice, and this section does not substitute for actual legal review on a project handling EU/CCPA-covered users, healthcare data, or payment data.

Whether a project collects personal data is decided during kit generation (`PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md` Question 5) and recorded in `ARCHITECTURE_DECISIONS.md`. Google OAuth login, the PHDK default whenever login exists, always means collecting at least a name and email — a project with login cannot answer "no personal data" honestly.

### Required when personal data is collected

- A Privacy Policy page (`/privacy`) describing what is collected, why, and how a user requests deletion
- A Terms of Service page (`/terms`) when the product involves accounts, paid features, or user-generated content
- A documented process for a user to request their data be deleted — a manual admin action is an acceptable starting point, self-service is not required from slice one
- A cookie consent mechanism if non-essential cookies (analytics, marketing) are used — a required session cookie for login is not the trigger for this by itself

### Never

- Never treat "no privacy policy yet" as a silent default when the product's data handling requires one; record the unresolved requirement explicitly
- Never assume this baseline satisfies GDPR, CCPA, HIPAA, or PCI obligations — flag explicitly when a project's data (EU users, health data, payment data) needs real legal review beyond what this file covers

---

## Data Backup and Recovery Safety

Live backup and restore operations belong outside PHDK, as defined in `EXECUTION_SCOPE.md` and `TECHNICAL_STACK.md` Data Backup Policy. PHDK does not add backup jobs or features as a baseline or incidental requirement. It does not export databases, email dumps, create git backup branches, schedule retention/pruning, configure provider backups, or run restore drills.

Keep repository work limited to migration compatibility notes and any relevant recovery requirements already supplied by the user. Do not invent a weekly policy, require an external backup task before completing code, or claim a backup/restore has been verified without evidence. Never commit live database dumps or private application data to any source branch.

---

## Cost and Consumption Safety

Any integration billed by usage — AI/image/video generation, LLM API calls, SMS, email sending, third-party enrichment APIs, or any other metered service — must never be able to spend money without a bound. An unbounded loop or retry storm against a metered API is a production incident, not a bug.

The following requirements constrain requested application code. They do not authorize the PHDK agent to call a live provider, create a background service, add a schedule, or operate a monitoring dashboard. Verification uses deterministic test doubles.

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
- Metered-integration code must apply a configurable threshold to existing usage records and flag unusual spend in its normal logging/diagnostic path. Verify the threshold with isolated tests; do not create external alerts, recurring checks, or monitoring jobs
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
- The baseline pricing refresh is an explicit product-admin action; do not infer scheduled refreshes, polling, or maintenance agents from this standard. Any explicitly requested recurring product feature remains code-only under `EXECUTION_SCOPE.md`; never invoke its live action from PHDK verification
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

Resolve material uncertainty before changing the following code or repository behavior. External operations excluded by `EXECUTION_SCOPE.md` remain excluded; these conditions do not authorize a provider action after a routine confirmation.

- Proposed destructive database code or migrations: drops, truncations, irreversible transitions
- Repository changes that conflict with recovery requirements supplied by the user
- Authentication provider changes
- Tenant model changes
- Permission model changes
- Payment behavior changes
- Deployment architecture changes
- Integration code that depends on external resources not already available; report the prerequisite without provisioning it
- Adding or enabling a metered/paid external API integration before its usage cap and kill switch are in place
- Adding an LLM-powered feature before its admin-manageable prompt/output section, provider/model config, and injection guardrails are in place
- Adding a feature that feeds externally-sourced or attacker-reachable content into an LLM call before indirect-injection guardrails and least-privilege credential scoping are in place
- Changing the default AI provider or model
- Adding high-risk or large dependencies
- Weakening validation, logging, or security checks
- Force-pushing to any branch
- Pushing directly to `main` without approval (Finetuning Mode, explicitly activated for the current conversation per `DEVELOPMENT_RULES.md`, is the one standing exception — everything else still requires asking)
- Deleting branches that have not been merged
- Disabling or weakening CORS, CSP, or rate limiting on any endpoint
- A known or suspected credential exposure; report it and perform only the repository remediation described above

Do not proceed with these actions based on assumptions. Wait for explicit approval.

---

## Verification

For the relevant code changes, record the applicable local evidence and any external limits:

- [ ] Relevant risk-triggered local unit or in-process integration tests pass
- [ ] Auth and permission behavior is verified using isolated adapters/test doubles, without a browser, UI automation, screenshots, or real-service probes
- [ ] Logs are structured and redact sensitive values
- [ ] Debug diagnostics are safe and redact sensitive values
- [ ] No secrets are committed to the repository
- [ ] Any metered/paid external API touched by this work has a usage cap, timeout, retry limit, and kill switch
- [ ] Any LLM feature touched by this work has admin-manageable prompt/output, configurable provider/model, injection guardrails, and output validation
- [ ] Any LLM feature that consumes externally-sourced content has indirect-injection guardrails: content treated as data, action-triggering scoped to authenticated user requests, per-resource credential scoping, and a confirmation gate before destructive actions
- [ ] Database changes include migration compatibility notes and any known external recovery dependency, without claiming a live database/restore test
- [ ] CORS allowlist, CSP, and standard security headers are configured on `apps/api`
- [ ] Rate-limiting code covers the service and auth endpoints and is verified with isolated requests
- [ ] Any suspected secret exposure is reported, repository leakage is corrected, and external revocation/rotation is accurately identified as outside PHDK and unverified unless evidence is supplied
- [ ] `.env.example` is up to date
- [ ] `ARCHITECTURE_DECISIONS.md` updated for any security-relevant decisions
- [ ] `STATUS.md` updated with current state
