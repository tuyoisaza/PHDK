# PHDK JWT and Synthetic UAT Authentication Standard

**Applies to:** authenticated products during explicitly authorized PHDK UAT Prep, UAT, UAT Fix and retests. Check reviews the source contract and existing evidence without provisioning identities or launching acceptance. Auto and Auto Force never run Prep/UAT/Fix; they report **UAT NOT RUN** with those stages **DEFERRED — OWNER OPT-IN**. JWT-specific rules apply only when JWT is actually used. Vendor with `PHDK_MANIFEST.txt`. JWT means **JSON Web Token**; UAT means **User Acceptance Testing**. These are different concepts. PHDK does **not** mandate adding JWT to products that already use secure server sessions, OAuth/OIDC or managed authentication.

## 1. Required outcome and trust boundary

A UAT agent must be able to exercise every applicable product persona (including the platform administrator, tenant administrator, ordinary users, customers, suppliers and anonymous/denied users) on the **explicitly authorized existing deployed production candidate**, using only uniquely run-owned synthetic identities/data under `PHDK_PRODUCTION_VERIFICATION.md`, without requesting a person's password, MFA code, bearer token or secret in chat. Company Co's fictional data (`USE_COMPANY_CO_INFO_FOR_DEMOS.md`) supplies reproducible identities; it is not an authentication provider. **Synthetic data alone never authenticates anyone.**

Build an explicit `UAT_AUTH_PLAN.md` documenting the environment/revision, existing identity provider and login/session architecture, single- vs multi-tenant policy, role→identity mapping, test issuer/credential custody if applicable, bootstrap route or provider mechanism, isolation, revocation, cleanup and expected proof. Do not mark a role PASS until an actual browser or API run proves access and negative permissions. Do not require JWT merely to make UAT run.

**Production and real accounts:** never hand-mint privileged tokens, introduce a new trusted issuer/key to accept arbitrary test tokens, expose an unrestricted "login as anyone" endpoint, borrow an owner's credentials, turn off MFA, invent credentials, impersonate real people or authorize activity against real production records. Synthetic elevated identities must use existing legitimate authentication and server-enforced authorization, with exact run ownership, audit, expiry and cleanup. Production browsing/account interaction follows the explicit UAT authorization and safe scope in `UAT_STANDARD.md` and `PHDK_PRODUCTION_VERIFICATION.md`; it never permits an authentication bypass. A URL alone proves neither authorization nor isolation.

## 2. Bootstrap precedence: use existing trust, not an authentication bypass

Select the first supported mechanism and record why:

1. **Existing application/provider authentication.** Provision minimal run-owned synthetic users through already authorized application administration, seeders or supported identity-provider mechanisms without changing provider configuration. Authenticate through the real supported flow. Use an existing authorized service identity from its secure secret facility when necessary; never request secrets in chat or provision a new environment/provider tenant as a workaround.
2. **Existing first-party session mechanism.** Use an already supported authenticated administration/session flow only if it verifies the caller's actual authority, resolves an allowlisted run-owned synthetic subject server-side, preserves normal role/tenant checks, records audit attribution and enforces expiry/revocation. Do not manufacture a session by editing client-side state, forge claims or enable a local test adapter in production.
3. **Missing safe readiness support.** Explicit `PHDK uat prep`, necessary Prep within a fresh explicit `PHDK uat` run, or explicitly authorized UAT Fix may repair in-scope seeding/session integration while preserving the existing trust boundary. Deliver source changes and verify the deployed revision before using them. Do not create a new trusted issuer/key, public bypass route or arbitrary privileged session facility. If a safe supported mechanism cannot be established within scope, the affected roles remain BLOCKED.
4. **No supported safe mechanism, identity-provider permission, target or browser:** record precise `BLOCKED` cases in `UAT_ACCESS_REPORT.md`; continue independent cases and request only the minimal necessary external action. Do not request human passwords, JWT text, bearer secrets, MFA codes or payment approval as a substitute for safe authentication. An explicit UAT invocation includes its necessary Prep; standalone Prep alone does not start acceptance, and Auto never authorizes provisioning or acceptance.

Within explicit Prep/UAT/Fix scope, the agent may inspect auth configuration, prepare fixtures, create in-scope source support and execute permitted deployed readiness/acceptance calls; it does **not** gain an identity-provider permission it lacks merely by entering a phase. Browser/headless use is **allowed only in explicitly authorized UAT/UAT Fix** when a browser is connected/available under `UAT_STANDARD.md`, `TESTING_STANDARD.md` and `EXECUTION_SCOPE.md`. Never claim browser proof if the capability is absent.

## 3. Synthetic identity catalog and safe fixture behavior

- Derive exact role and capability names from application code and `ADMIN_ARCHITECTURE.md`. **Multi-tenant:** one platform `super_admin`, tenant `tenant_admin`, domain managers, ordinary staff, B2B/B2C customer and supplier profiles where applicable, suspended/pending users and anonymous users. **Single-tenant:** top-level `admin` instead of fictitious `super_admin`; do not create tenant roles.
- Map Company Co's 200 fictional employees, 17 departments/leaders and commercial profiles to stable fixture IDs such as `EMP-001` and a `tenant_id` only where applicable. Seed the **minimum representative subset required for the actual product**, idempotently; do not turn every row into an account unless scenarios need it. Use separate synthetic organizations/tenants to prove isolation when multi-tenant.
- Create/reconcile identities through the supported application/provider APIs or an authorized transactional seeder. Validate verified provider subject, active/suspended state, tenant membership, roles, route entry, permissions and data scope. Establish a synthetic elevated actor using the *same trusted test bootstrap* as all other fixtures; do not treat Company Co's `superadmin` label as a credential.
- Never use shared hard-coded default passwords, email-delivered magic links, bulk real notifications, production user accounts or unconstrained production test data. Redirect notifications to a sink/mock and use mocked payment/third-party side effects. Treat `@tujuisasa.com` fixture addresses as data, not as automatically authorized outbound recipients.
- Fixture cleanup must terminate sessions, revoke test grants and remove/archive transient test records safely. Any deliberate persisted demo baseline stays explicitly scoped and documented.

## 4. JWT profile — only for applications using signed JWT access tokens

A legitimate session for a synthetic UAT identity must be **issued by the application's existing trusted authentication service**, never assembled or modified by the browser or arbitrary test scripts. Use the normal configured issuer/audience and secret custody for that deployed application; do not change production trust settings or make a separate test issuer trusted as a workaround. Verifiers must cryptographically validate the signature using the configured allowlist of algorithms and issuer-bound keys; reject `alg:none`, unexpected `kid`, wrong token type/`typ` or key confusion. Validate the applicable claims before authorizing an operation:

| Claim | Meaning and check |
| --- | --- |
| `iss`, `aud`, `typ` | Existing configured trusted issuer, app/API audience and appropriate token type; reject untrusted test issuers and mismatches. |
| `sub` | Existing pre-provisioned synthetic subject resolved server-side to current active account. |
| `exp`, `iat`, `nbf` | Server clock-bounded issuance; default UAT access lifetime **5 minutes** (may adapt to app policy, max **15 minutes**), no indefinite refresh. |
| `jti` | Cryptographically random unique token ID; enable audit and revocation/replay controls appropriate to the token use. |
| `tenant_id`, `scope` / `roles` | Only if required by the product; derive/validate membership and effective privileges **server-side** on each request, not from a caller-chosen tenant/role. |
| `purpose`, `env`, `run_id` | Where supported by the existing provider, record UAT intent, exact deployed environment and accountable run metadata; otherwise retain run ownership in server-side fixture/audit records. |
| `act` | When delegated/test-as authorization is supported, capture the original authenticated actor; never lose attribution to the admin/runner. |

Example **claims shape**, not a valid token or a license to generate credentials (dynamic times/IDs are supplied by the trusted issuer):

```json
{
  "iss": "https://existing-auth.example.invalid",
  "aud": "existing-app-api",
  "sub": "companyco:EMP-001",
  "iat": 0,
  "nbf": 0,
  "exp": 0,
  "jti": "<secure-random-id>",
  "tenant_id": "companyco-test",
  "purpose": "uat",
  "env": "production",
  "run_id": "<current-run-id>"
}
```

JWT claims are **signed, not encrypted** by default; put no passwords, API keys, sensitive customer records or real PII in payloads. Do not transmit tokens via query strings or log them. Prefer first-party `Secure`, `HttpOnly`, `SameSite` session cookies plus CSRF controls as appropriate for browser UAT; use short-lived bearer tokens only for legitimate API cases, transmitted via authorized headers. Do not store tokens in committed source, reports, screenshots or traces. Browser authentication state (such as Playwright `storageState`) is sensitive: create it in a temporary, access-restricted, gitignored path, one state per role/tenant and test worker where required, redact artifacts and delete it after the run. Honor session invalidation, account suspension and `jti`-based denial when the product relies on revocation.

## 5. Superadmin / admin "Ver como" is not the test bootstrap

The **bootstrap** logs the test runner into a synthetic elevated account through valid authentication. The application's actual **Test as / Ver como** feature (`ADMIN_CONSOLE_STANDARD.md`) must then allow an authorized, authenticated elevated actor to select a permitted synthetic target, tenant and profile. It issues a new **reduced-privilege** server-enforced context, logs actor, target, tenant, reason, start/expiry/end and provides a visible banner and **Return to admin**. It may not modify unsigned client role flags or make tenant-ID changes sufficient to elevate access. Sensitive operations are blocked or isolated. Test returning to elevated context and ensure the originating actor remains auditable.

Independent per-role login is also required when necessary to verify real authentication, direct sign-in/redirects, session isolation, logout, suspended users and authorization boundaries. A working test bootstrap does not prove that product-facing Test as works, nor that real OAuth/SSO user login works. Those are distinct UAT cases.

## 6. Required end-to-end automated UAT sequence

**Phase boundary:** standalone explicit `PHDK uat prep`, or necessary Prep within a fresh explicit `PHDK uat` run, implements safe readiness support and performs permitted non-browser provisioning checks on the deployed candidate, generating `UAT_PREP_REPORT.md` before any UAT browser action. Only explicitly authorized UAT/UAT Fix performs browser/role journeys and claims acceptance results. Auto and Auto Force never enter stages 45–60. A seeded user or static source check alone never means UAT PASS; no local unit/in-process tests are permitted.

1. **Discover:** inspect exact environment, build SHA, auth/session implementation, OAuth/SSO configuration, role/tenant policies, existing fixtures, deployed candidate, browser ability and product intent.
2. **Plan:** create `UAT_AUTH_PLAN.md` with the existing provider/session mechanism, trust boundaries, per-role Company Co IDs, ephemeral credential source (reference only), negative cases, cleanup and current explicit authorization. Confirm the exact existing production target and safe synthetic scope; a new sensitive permission or provider configuration change remains outside that authorization.
3. **Seed:** provision/synchronize minimal synthetic identities, two tenants if applicable, role grants and test-safe sample data. Verify database/provider identity links and record nonsecret fixture IDs.
4. **Authenticate:** acquire supported short-lived sessions for the elevated actor and every needed role; never hand-author a JWT or ask the owner for a password. Prove backend identity with an authenticated `/me`-equivalent and server-side permission/tenant checks.
5. **Exercise:** in UAT browser contexts isolated by role/tenant (for example Playwright storage states), execute real click/navigation/form/CRUD journeys, including actual elevated Test as, banner, return and negative direct API/IDOR tests. The backend must enforce all permissions irrespective of visible UI.
6. **Verify:** test allowed/denied paths; wrong tenant, nonexistent/deactivated account, forged/wrong-audience/expired/revoked token (when JWT is used), session expiry, logout, cross-role state leakage, direct URL/API access and forbidden sensitive writes. Verify provider login separately when within scope.
7. **Capture:** write `UAT_ACCESS_REPORT.md` and a `UAT_AUTH_EVIDENCE.md` or equivalent linked section with role, tenant, synthetic subject, mechanism, revision, case ID, authorization verdict, redacted trace reference, cleanup and PASS/FAIL/BLOCKED. **Never include raw tokens, passwords, secrets or authentication state files.**
8. **Clean up and retest:** revoke test grants/sessions, remove temporary state and rollback isolated mutations; after UAT Fix rerun impacted login, role-switch, permission, tenancy and journey cases. Preserve initial failures in history.

## 7. Acceptance and blocker classification

- **PASS:** runtime proof of real authenticated UI/API journey with correct role/tenant, Test as behavior when applicable, negative enforcement and cleaned-up credentials.
- **FAIL / UAT FIX:** product's required role test facility or test-only authorized harness is missing/broken and can be repaired safely within authorized scope; never treat inability to log in as an acceptable pass.
- **BLOCKED:** external provider permission, disconnected browser, no authorized deployed target or provable synthetic isolation, MFA participation or incompatible hosted auth that PHDK cannot lawfully/safely supply. Name the blocked roles/cases and continue independent cases; ask for exactly one necessary owner action if unavoidable.
- **MANUAL:** an explicitly non-automatable human SSO/MFA or policy sign-off step with runnable independent work completed.
- **NOT APPLICABLE:** no authenticated actors in the actual product (with source evidence); never use this to avoid testing an administered application.

Required `PHDK check` gate: inspect concrete auth provider configuration, safe synthetic identity/session design, expiry/revocation, absence of authentication bypasses, supported personas, role/tenant permissions, test-as behavior, redaction and any existing browser/API evidence. Check does not seed identities or execute acceptance. During Auto/Auto Force, missing optional runtime UAT evidence is **UAT NOT RUN**, with Prep/UAT/Fix **DEFERRED — OWNER OPT-IN**; do not turn that absence into a failed development gate. Real source/security defects remain findings within authorized development scope. Within an explicitly initiated UAT run, a missing required identity or runtime proof is GAP/BLOCKED/UNVERIFIED as appropriate; a written claim, fake bearer token or fixture catalog is not compliance.

## 8. Normative public references

- [OWASP JWT Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html) — signed claims, validation, issuer/audience, key isolation, revocation and secrecy.
- [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) — JWT verification and server-side authorization.
- [Playwright Authentication](https://playwright.dev/docs/auth) — authenticated browser state per role and multiple independent user contexts.

These references inform the safeguards; they do not authorize production access or replace the project's established identity provider.


## Production-first verification override (v2.58.0)

**Mandatory:** Apply [PHDK_PRODUCTION_VERIFICATION.md](PHDK_PRODUCTION_VERIFICATION.md). Owner-authorized production-only UAT supersedes earlier local unit/in-process/runtime testing, staging-only identity, and blanket production-test prohibitions. Local operations are limited to static analysis, lint, typecheck and safe builds; Docker, local runtime tests and separate staging/databases are prohibited. UAT must use existing versioned production deployment and existing database, strictly scoped run-owned synthetic identities/records, audit, automated cleanup and verified revocation on success, failure and interruption. Never touch real data or bypass existing security hooks; a conflicting gate is BLOCKED.
