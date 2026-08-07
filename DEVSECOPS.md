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

- Never deploy from local CLI
- Deployment is always triggered by GitHub push to `main`
- Both Railway services use the repository root
- Never set Railway root directory to `apps/web` or `apps/api`
- Environment variables are never committed to the repository
- Production deployments must pass all quality gates before merging to `main`

---

## Stop-and-Ask Conditions

Stop immediately and ask before performing any of the following:

- Destructive database operations: drops, truncations, irreversible migrations
- Authentication provider changes
- Tenant model changes
- Permission model changes
- Payment behavior changes
- Deployment architecture changes
- Adding new external services
- Adding high-risk or large dependencies
- Weakening validation, logging, or security checks
- Force-pushing to any branch
- Pushing directly to `main` without approval
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
- [ ] `.env.example` is up to date
- [ ] `ARCHITECTURE_DECISIONS.md` updated for any security-relevant decisions
- [ ] `STATUS.md` updated with current state
