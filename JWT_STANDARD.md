# PHDK JWT and Synthetic UAT Authentication Standard

**Applies to:** all authenticated products during PHDK UAT, UAT Fix, re-UAT, Auto UAT and Check; JWT-specific rules apply only when JWT is actually used. Vendor with `PHDK_MANIFEST.txt`. JWT means **JSON Web Token**; UAT means **User Acceptance Testing**. These are different concepts. PHDK does **not** mandate adding JWT to products that already use secure server sessions, OAuth/OIDC or managed authentication.

## 1. Required outcome and trust boundary

A UAT agent must be able to exercise every applicable product persona (including the platform administrator, tenant administrator, ordinary users, customers, suppliers and anonymous/denied users) on an **authorized non-production candidate** without requesting a person's password, MFA code, bearer token or secret in chat. Company Co's fictional data (`USE_COMPANY_CO_INFO_FOR_DEMOS.md`) supplies reproducible identities; it is not an authentication provider. **Synthetic data alone never authenticates anyone.**

Build an explicit `UAT_AUTH_PLAN.md` documenting the environment/revision, existing identity provider and login/session architecture, single- vs multi-tenant policy, role→identity mapping, test issuer/credential custody if applicable, bootstrap route or provider mechanism, isolation, revocation, cleanup and expected proof. Do not mark a role PASS until an actual browser or API run proves access and negative permissions. Do not require JWT merely to make UAT run.

**Production and real accounts:** never mint production super-admin tokens, issue self-signed bearer tokens accepted by production, expose an unrestricted "login as anyone" endpoint, borrow an owner's credentials, turn off MFA, invent credentials, impersonate real people or silently authorize activity against real production records. Production browsing/account interaction is governed separately by `UAT_STANDARD.md`, always requires explicit authorization and a non-destructive plan, and must not introduce a synthetic privileged bootstrap into production. A production URL is not proof of a test environment.

## 2. Bootstrap precedence: use existing trust, not an authentication bypass

Select the first supported mechanism and record why:

1. **Best: isolated app/identity-provider test tenant.** Provision synthetic users through approved application administration, seeders or documented sandbox identity-provider APIs; authenticate through the real supported provider flow or a provider-supported test facility. Keep test provider keys separate from production. Use an official test credential/service identity from the provider's secure secret facility if required and already authorized; never ask the user to paste it into chat.
2. **Existing integration-test/session hook.** Use the application's established test fixtures, in-process backend test helpers, a signed test service identity or server-created first-party session. It must be limited to local/private staging, verify its calling test runner, resolve the target from a server allowlist of synthetic records and apply all normal authorization checks. Do not manufacture a session by editing client-side state.
3. **Missing bootstrap in explicit `PHDK uat prep`, authorized Auto stage 45, or UAT Fix when newly discovered during acceptance.** Implement a narrow **test-only adapter** at the authentication boundary of the current stack. It may create a session for a *pre-seeded synthetic user* only when the test runner's trusted identity, allowed environment, fixture ID, tenant and run scope have been verified server-side. Build/exclude it so production deployments cannot register or enable the adapter, even if an environment variable is accidentally set. Do not make a public production route. Sign with an independent test issuer/key when JWT is appropriate; otherwise use ordinary secure first-party session issuance.
4. **No supported safe mechanism, identity-provider permissions, environment or browser:** record the precise `BLOCKED` cases in `UAT_ACCESS_REPORT.md`; continue other cases; request only the minimal authorized external setup when unavoidable. Do not ask for human passwords, JWT text, bearer secrets, MFA codes or payment approval as a substitute for a properly isolated test harness. Standalone `PHDK uat` verifies prior `PHDK_UAT_PREP.md` evidence and directs missing initial harness development to `PHDK uat prep`, rather than silently creating an auth backdoor.

The agent may inspect auth configuration, synthesize fixtures, create code and run authorized test-only paths; it does **not** gain an identity-provider permission it lacks merely by entering UAT. Browser/headless use is **allowed only in the scoped UAT/UAT Fix phase** when a browser is connected/available under `UAT_STANDARD.md`, `TESTING_STANDARD.md` and `EXECUTION_SCOPE.md`. Never claim browser proof if the capability is absent.

## 3. Synthetic identity catalog and safe fixture behavior

- Derive exact role and capability names from application code and `ADMIN_ARCHITECTURE.md`. **Multi-tenant:** one platform `super_admin`, tenant `tenant_admin`, domain managers, ordinary staff, B2B/B2C customer and supplier profiles where applicable, suspended/pending users and anonymous users. **Single-tenant:** top-level `admin` instead of fictitious `super_admin`; do not create tenant roles.
- Map Company Co's 200 fictional employees, 17 departments/leaders and commercial profiles to stable fixture IDs such as `EMP-001` and a `tenant_id` only where applicable. Seed the **minimum representative subset required for the actual product**, idempotently; do not turn every row into an account unless scenarios need it. Use separate synthetic organizations/tenants to prove isolation when multi-tenant.
- Create/reconcile identities through the supported application/provider APIs or an authorized transactional seeder. Validate verified provider subject, active/suspended state, tenant membership, roles, route entry, permissions and data scope. Establish a synthetic elevated actor using the *same trusted test bootstrap* as all other fixtures; do not treat Company Co's `superadmin` label as a credential.
- Never use shared hard-coded default passwords, email-delivered magic links, bulk real notifications, production user accounts or unconstrained production test data. Redirect notifications to a sink/mock and use mocked payment/third-party side effects. Treat `@tujuisasa.com` fixture addresses as data, not as automatically authorized outbound recipients.
- Fixture cleanup must terminate sessions, revoke test grants and remove/archive transient test records safely. Any deliberate persisted demo baseline stays explicitly scoped and documented.

## 4. JWT profile — only for applications using signed JWT access tokens

A UAT JWT must be **issued by the trusted test auth service**, never assembled or modified by the browser or by arbitrary test scripts. Test JWTs cannot share a signing key or trusted issuer/audience with production. Verifiers must cryptographically validate the signature using an explicitly configured allowlist of algorithms and issuer-bound keys; reject `alg:none`, unexpected `kid`, wrong token type/`typ` or key confusion. Validate the applicable claims before authorizing an operation:

| Claim | Meaning and check |
| --- | --- |
| `iss`, `aud`, `typ` | Fixed allowed test issuer, app/API audience and appropriate token type; production must reject this profile. |
| `sub` | Existing pre-provisioned synthetic subject resolved server-side to current active account. |
| `exp`, `iat`, `nbf` | Server clock-bounded issuance; default UAT access lifetime **5 minutes** (may adapt to app policy, max **15 minutes**), no indefinite refresh. |
| `jti` | Cryptographically random unique token ID; enable audit and revocation/replay controls appropriate to the token use. |
| `tenant_id`, `scope` / `roles` | Only if required by the product; derive/validate membership and effective privileges **server-side** on each request, not from a caller-chosen tenant/role. |
| `purpose`, `env`, `run_id` | UAT-only intent, non-production binding and accountable run metadata as private claims. |
| `act` | When delegated/test-as authorization is supported, capture the original authenticated actor; never lose attribution to the admin/runner. |

Example **claims shape**, not a valid token or a license to generate credentials (dynamic times/IDs are supplied by the trusted issuer):

```json
{
  "iss": "https://uat-issuer.example.invalid",
  "aud": "phdk-uat-api",
  "sub": "companyco:EMP-001",
  "iat": 0,
  "nbf": 0,
  "exp": 0,
  "jti": "<secure-random-id>",
  "tenant_id": "companyco-test",
  "purpose": "uat",
  "env": "staging",
  "run_id": "<current-run-id>"
}
```

JWT claims are **signed, not encrypted** by default; put no passwords, API keys, sensitive customer records or real PII in payloads. Do not transmit tokens via query strings or log them. Prefer first-party `Secure`, `HttpOnly`, `SameSite` session cookies plus CSRF controls as appropriate for browser UAT; use short-lived bearer tokens only for legitimate API cases, transmitted via authorized headers. Do not store tokens in committed source, reports, screenshots or traces. Browser authentication state (such as Playwright `storageState`) is sensitive: create it in a temporary, access-restricted, gitignored path, one state per role/tenant and test worker where required, redact artifacts and delete it after the run. Honor session invalidation, account suspension and `jti`-based denial when the product relies on revocation.

## 5. Superadmin / admin "Ver como" is not the test bootstrap

The **bootstrap** logs the test runner into a synthetic elevated account through valid authentication. The application's actual **Test as / Ver como** feature (`ADMIN_CONSOLE_STANDARD.md`) must then allow an authorized, authenticated elevated actor to select a permitted synthetic target, tenant and profile. It issues a new **reduced-privilege** server-enforced context, logs actor, target, tenant, reason, start/expiry/end and provides a visible banner and **Return to admin**. It may not modify unsigned client role flags or make tenant-ID changes sufficient to elevate access. Sensitive operations are blocked or isolated. Test returning to elevated context and ensure the originating actor remains auditable.

Independent per-role login is also required when necessary to verify real authentication, direct sign-in/redirects, session isolation, logout, suspended users and authorization boundaries. A working test bootstrap does not prove that product-facing Test as works, nor that real OAuth/SSO user login works. Those are distinct UAT cases.

## 6. Required end-to-end automated UAT sequence

**Phase boundary:** `PHDK uat prep`/Auto stage 45 implements and locally verifies the fixture/identity/session/bootstrap steps, generating `UAT_PREP_REPORT.md` before any UAT browser action. Only `PHDK uat`/Auto stage 50 (and UAT Fix) performs live browser/role journeys and claims acceptance results. A seeded user or passing unit test alone never means UAT PASS.

1. **Discover:** inspect exact environment, build SHA, auth/session implementation, OAuth/SSO configuration, role/tenant policies, existing fixtures, deployed candidate, browser ability and product intent.
2. **Plan:** create `UAT_AUTH_PLAN.md` with provider/adapter choice, trust boundaries, per-role Company Co IDs, ephemeral credential source (reference only), negative tests, cleanup and approvals. A real production target or new sensitive permission is a decision gate, not an automatic fix.
3. **Seed:** provision/synchronize minimal synthetic identities, two tenants if applicable, role grants and test-safe sample data. Verify database/provider identity links and record nonsecret fixture IDs.
4. **Authenticate:** acquire supported short-lived sessions for the elevated actor and every needed role; never hand-author a JWT or ask the owner for a password. Prove backend identity with an authenticated `/me`-equivalent and server-side permission/tenant checks.
5. **Exercise:** in UAT browser contexts isolated by role/tenant (for example Playwright storage states), execute real click/navigation/form/CRUD journeys, including actual elevated Test as, banner, return and negative direct API/IDOR tests. The backend must enforce all permissions irrespective of visible UI.
6. **Verify:** test allowed/denied paths; wrong tenant, nonexistent/deactivated account, forged/wrong-audience/expired/revoked token (when JWT is used), session expiry, logout, cross-role state leakage, direct URL/API access and forbidden sensitive writes. Verify provider login separately when within scope.
7. **Capture:** write `UAT_ACCESS_REPORT.md` and a `UAT_AUTH_EVIDENCE.md` or equivalent linked section with role, tenant, synthetic subject, mechanism, revision, case ID, authorization verdict, redacted trace reference, cleanup and PASS/FAIL/BLOCKED. **Never include raw tokens, passwords, secrets or authentication state files.**
8. **Clean up and retest:** revoke test grants/sessions, remove temporary state and rollback isolated mutations; after UAT Fix rerun impacted login, role-switch, permission, tenancy and journey cases. Preserve initial failures in history.

## 7. Acceptance and blocker classification

- **PASS:** runtime proof of real authenticated UI/API journey with correct role/tenant, Test as behavior when applicable, negative enforcement and cleaned-up credentials.
- **FAIL / UAT FIX:** product's required role test facility or test-only authorized harness is missing/broken and can be repaired safely within authorized scope; never treat inability to log in as an acceptable pass.
- **BLOCKED:** external provider permission, disconnected browser, no authorized isolated target, MFA participation or incompatible hosted auth that PHDK cannot lawfully/safely supply. Name the blocked roles/cases and continue independent cases; ask for exactly one necessary owner action if unavoidable.
- **MANUAL:** an explicitly non-automatable human SSO/MFA or policy sign-off step with runnable independent work completed.
- **NOT APPLICABLE:** no authenticated actors in the actual product (with source evidence); never use this to avoid testing an administered application.

Required `PHDK check` gate: locate concrete auth provider configuration, non-production test identity bootstrap, lifecycle expiry/revocation, no production exposure, supported personas, actual role/tenant permissions, test-as behavior, redaction and browser/API evidence. Record GAP or UNVERIFIED when absent; a written claim, fake bearer token or a fixture catalog is not compliance. `PHDK auto` must provision/fix safe in-scope UAT support before declaring authentication-blocked testing complete.

## 8. Normative public references

- [OWASP JWT Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html) — signed claims, validation, issuer/audience, key isolation, revocation and secrecy.
- [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) — JWT verification and server-side authorization.
- [Playwright Authentication](https://playwright.dev/docs/auth) — authenticated browser state per role and multiple independent user contexts.

These references inform the safeguards; they do not authorize production access or replace the project's established identity provider.
