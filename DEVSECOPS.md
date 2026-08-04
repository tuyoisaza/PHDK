# DEVSECOPS.md

## Purpose

This file defines the DevSecOps best practices for every project built on this standard.

Security is not a release phase. It is a continuous practice wired into development, CI/CD, deployment, and runtime. Treat every item here as a baseline expectation, and adjust scope to the project's actual risk level.

Like all tooling guidance in this repo, the specific tools named are recommendations. Adopt them when they fit the project; skip or replace when they do not. The underlying practices remain.

---

# Principles

- **Shift left:** find and fix security issues as early as possible — in the IDE and CI, not in production.
- **Least privilege:** every account, service, and token gets the minimum access it needs.
- **Defense in depth:** never rely on a single control. Layer validation, auth, rate limiting, and monitoring.
- **Fail secure:** when something fails, fail closed, not open.
- **Audit everything important:** sensitive actions leave a trace.
- **Secrets never enter the repo:** tokens, keys, and credentials live in the secret manager only.

---

# Secret Management

## Rules

- Never commit secrets to the repository. Never store secrets in `.env` files that reach git.
- `.env.example` contains placeholder values only.
- Real environment variables live in Railway dashboard or an approved secret manager.
- Rotate secrets on a schedule and immediately on suspected exposure.
- Never log secrets, tokens, passwords, cookies, or authorization headers.
- Never copy raw secrets into debug reports or support screenshots.
- Use one secret per purpose. Do not reuse a key across environments.

## Recommended Tooling

- Secret scanning in CI: Gitleaks, TruffleHog, or git-secrets.
- GitHub secret scanning and push protection on the repository.
- Pre-commit secret scan so secrets are caught before the commit exists.

---

# Supply Chain Security

## Rules

- Commit lockfiles (`pnpm-lock.yaml`). Never install with a partial or regenerated lockfile in CI.
- Use `pnpm install --frozen-lockfile` in CI for reproducible installs.
- Review dependency alerts and updates on a schedule.
- Do not add a dependency when the existing stack already covers the need.
- Do not upgrade dependencies without task scope or a documented reason.
- Audit the dependency tree before release.

## Recommended Tooling

- `pnpm audit` / `npm audit` for known-vulnerability scanning.
- Dependabot or equivalent automated dependency alerts.
- Software Composition Analysis (SCA): Snyk, OWASP Dependency-Check, or Trivy.
- SBOM generation (Syft or CycloneDX) for production releases.
- Verify package provenance where supported (`npm` provenance / registry trust).

---

# Static and Dynamic Analysis

## Recommended Tooling

- SAST — static application security testing: Semgrep, CodeQL, or ESLint security plugins.
- Secret scanning: Gitleaks, TruffleHog, git-secrets.
- DAST — dynamic testing against a running staging environment where budget allows.
- Container image scanning: Trivy or Grype for any built image.
- IaC scanning where infrastructure-as-code exists: Checkov, tfsec/Trivy.

## Rules

- SAST and secret scanning run on every pull request, not only on merge.
- Block merge on critical or high severity findings.
- Fix findings in the feature branch, not in a later security pass.
- Document any finding marked as acceptable risk, with owner and expiry.

---

# CI/CD Pipeline Security

## Rules

- Never deploy from a local CLI. Deployment is triggered by the hosting provider detecting a GitHub push to `main`.
- Every push to `main` runs build, lint, typecheck, tests, SAST, secret scanning, and dependency audit.
- Pipeline steps run with least-privilege credentials.
- Never paste secrets into pipeline logs; mask or redact them.
- Protect `main` with branch protection: required pull request, required reviews, required status checks, no force push.
- Require signed commits (GPG or SSH) on `main` where the team supports it.
- Use short-lived, scoped tokens instead of long-lived credentials.
- Never let a pull request skip required checks.

---

# Code Review and Change Security

## Rules

- Every change to `main` goes through a pull request and review.
- Reviewers check for security impact, not just logic: auth, validation, injection, secrets, and data exposure.
- Never merge code that references TODO security gaps.
- Keep changes small and focused so review is meaningful.
- Block role escalation, privilege changes, and destructive actions server-side, and audit them.

---

# Runtime Security

## Rules

- Enforce authorization server-side on every protected route and endpoint. Hiding UI is not security.
- Validate all input with Zod at the API boundary. Never trust client-supplied data.
- Return stable error codes. Never expose raw error internals, stack traces, or SQL details to clients.
- Rate limit sensitive endpoints: authentication, password flows, and public write endpoints.
- Set secure cookies and session flags where sessions are used.
- Protect against CSRF, XSS, SQL injection, and SSRF as applicable.
- Always serve over HTTPS in production.

## Recommended Web Headers

```txt
Content-Security-Policy
Strict-Transport-Security
X-Content-Type-Options
Referrer-Policy
X-Frame-Options or equivalent
```

Apply through the web framework's header/middleware configuration, not per-page.

## Database Security

- Use a dedicated least-privilege database user for the application.
- Connect over TLS where the provider supports it.
- Restrict database network access to the application environment.
- Never expose the database to the public internet.
- Back up production data and test restore on a schedule.

---

# Logging and Audit for Security

## Rules

- Log important security events: login failures, role changes, permission changes, debug mode toggles, and destructive admin actions.
- Logs include actor, target, timestamp, environment, result, and correlation ID where applicable.
- Logs never include secrets, tokens, cookies, passwords, or authorization headers.
- Alert on repeated auth failures and privilege escalation attempts.
- Preserve audit logs; do not allow normal users to modify or delete them.

---

# Monitoring and Incident Response

## Rules

- Define what triggers a security alert: auth failures, unexpected access, dependency findings, deployment anomalies.
- Define an incident response runbook: how to detect, contain, fix, and learn.
- Define how access is revoked in an incident: disable account, rotate secrets, restrict network.
- Define a rollback path for every release.
- Track open security issues to closure; do not let them accumulate silently.

## Recommended Baseline

- `/health` endpoint on `apps/api` for liveness checks.
- Alerts on error rates, failed deploys, and failed logins where tooling allows.
- A documented owner for security issues.

---

# Vulnerability Management

## Rules

- Track known vulnerabilities to a clear SLA, for example:
  - Critical: patch or mitigate within days.
  - High: patch or mitigate within the release cycle.
  - Medium/low: scheduled with documented owner.
- Re-run dependency audit before every release.
- Document any accepted risk with owner, reason, and expiry.

---

# DevSecOps Checklist

Before marking a release complete, verify:

- [ ] No secrets are committed or exposed in CI logs.
- [ ] Lockfile is committed and `pnpm install --frozen-lockfile` is used.
- [ ] Dependency audit runs and has no unmitigated critical findings.
- [ ] SAST and secret scanning run on pull requests and `main`.
- [ ] `main` has branch protection and required status checks.
- [ ] No local CLI deployment exists.
- [ ] Authorization is enforced server-side on every protected route and endpoint.
- [ ] Inputs are validated with Zod at the API boundary.
- [ ] Sensitive endpoints are rate limited.
- [ ] Production is HTTPS-only with recommended security headers.
- [ ] Security events are logged and auditable.
- [ ] A rollback path exists for every release.
- [ ] Secrets are rotated on schedule and on exposure.
- [ ] Documented security findings have owners and expiry.
