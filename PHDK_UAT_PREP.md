# PHDK UAT Prep — Synthetic Identity Readiness

## Command, position and authority

**Command:** `PHDK uat prep`, case-insensitive after whitespace trim; also mandatory **stage 45 UAT Prep** within `PHDK auto`, between Integration Review (40) and UAT (50). This is an **implementation and provisioning** command, not a planning-only audit. A request to define this command does not activate it in another product. It does not activate Auto, UAT, background work or any browser exception.

On a standalone invocation, complete permitted in-scope application edits, non-browser verification, versioned branch/PR/merge and remote verification under `MAIN_DELIVERY_STANDARD.md`. Inside Auto, develop on the same integrated candidate and **do not merge or release at stage 45**; use Auto's final delivery.

Read `PHDK_PREFLIGHT.md`, `EXECUTION_SCOPE.md`, `JWT_STANDARD.md`, `UAT_JOURNEY_STANDARD.md`, `USE_COMPANY_CO_INFO_FOR_DEMOS.md` and `ADMIN_CONSOLE_STANDARD.md`. Preserve the existing app's actual auth provider, roles and tenant boundaries. A Company Co employee or role label alone never authenticates an account. JWT is optional; do not impose JWT on an OAuth/cookie/session app.

## Required implementation sequence

1. **Inspect and pin:** project goal and requirements, exact candidate/revision, deployment, source-backed auth/session/provider flows, membership/RBAC, tenancy, existing seeders, `Ver como` feature and available local test harness. In Auto verify the Integration handoff. Determine whether the target is an explicitly authorized isolated local/test/staging environment; a production-looking URL or a `TEST_MODE` flag is not proof.
2. **Design the minimum role fixture:** inventory anonymous, inactive/suspended, real ordinary/manager/customer/supplier profiles, and correct platform authority (**multi tenant = platform `super_admin` and tenant admins; single tenant = application `admin`, no redundant super-admin**). Map a *representative subset* of Company Co's 200 fictional employees and commercial profiles to stable synthetic IDs. For multi-tenant create two **synthetic** tenants when isolated testing needs cross-tenant denial. No unnecessary mass-account creation.
3. **Build or repair repeatable identity provisioning:** implement checked-in idempotent seed/upsert scripts, safe schema/migration changes where necessary, or the existing approved sandbox identity-provider administration path. Bind provider `sub`, active status, tenant membership, permissions, domain records and fixture owner/run ID. Prove repeated runs do not duplicate records or escalate permissions. **Actually provision** safe local/test accounts when permitted; record exact missing external steps instead of claiming they exist.
4. **Build/reuse authenticated session bootstrap:** prefer real supported provider test accounts and first-party server sessions. When necessary, implement a narrowly authenticated and allowlisted **non-production-only test adapter** that is excluded from production builds/routes even if an environment toggle is mis-set, accepts only pre-seeded synthetic subjects, validates a trusted runner and current role/tenant membership, uses test-only issuer/keys for JWT apps, expires/revokes state and never lets the browser forge claims. No public "login as superadmin" endpoint, default password, MFA disablement, hand-minted bearer string or production auth bypass.
5. **Support role test:** prepare independent synthetic identities/sessions for each applicable user and an elevated actor. If the application already requires `Ver como / Test as`, implement/fix the authenticated server-enforced restricted-role switch (actor/target/tenant/expiry/audit, visible banner and return) **within authorized feature scope**. Do not confuse test bootstrap with product impersonation. Escalation, cross-tenant access and real-user impersonation are prohibited.
6. **Isolate and prove:** route email to a sink and financial side effects to mocks, exclude real people/data and new paid dependencies, set cleanup/revocation/TTL. Write and **run** allowed local or in-process tests for seed idempotency, actual resolved identity, per-role allow/deny, tenant isolation, suspended users, expiry/revocation, and production adapter exclusion. JWT-specific wrong issuer/audience/signature tests apply only for JWT apps. Record real results; no invented API/browser/SSO evidence.
7. **Handoff:** write the four canonical artifacts below, record blockers individually and move to UAT when permitted. A missing buildable seeder/auth harness is an implementation issue in Prep, **not** a reason to ask for the owner's personal passwords or defer routine work until UAT Fix.

## Mandatory app artifacts and proof

| Artifact | Required evidence |
| --- | --- |
| `UAT_AUTH_PLAN.md` | environment/revision, existing provider + chosen safe bootstrap, trust boundary/secret references (never values), exact role/tenant access plan, revocation and cleanup |
| `UAT_ROLE_MATRIX.md` | source-backed personas, fixture IDs, actual allowed/denied permissions, tenant boundaries, elevated and anonymous/inactive identities, coverage |
| `UAT_FIXTURE_MANIFEST.md` | seed source/command, deterministic Company Co subset, per-role account/subject/tenant/status (no passwords/tokens), provisioning result, idempotency and rollback/cleanup |
| `UAT_PREP_REPORT.md` | candidate + environment, source changes, actual seed/provider actions and non-browser tests/results, per-role `READY`/`BLOCKED`/`UNVERIFIED`/`N/A`, security/production isolation evidence, exact next action |

Inside Auto create immutable sanitized snapshots plus `docs/phdk/lifecycle/<run-id>/45-uat-prep/HANDOFF.md`. A standalone invocation does not fabricate a lifecycle run.

**READY:** all required safe accounts are provably provisioned (or local isolated fixtures are explicitly identified with *external accounts still blocked*), trusted issuance and local/in-process authorization checks pass, and cleanup/production exclusion is evidenced. Never mark an externally missing role READY. **PARTIAL/BLOCKED:** missing provider permission, safe target, account, test-as feature, needed runtime proof or owner policy decision; continue all independent permitted work and enumerate impacted role/cases. **N/A:** truly no authenticated user surface with source evidence. **REUSED:** revalidate source, candidate revision, environment, role scope, state expiry, tests and cleanup; do not reuse stale assertion.

## UAT transition, source changes and browser boundary

Auto order: **40 Integration → 45 UAT Prep → 50 UAT → 60 UAT Fix**. Prep **must not** launch Playwright, browser/headless tests, screenshots, OAuth login pages or full acceptance journeys. The browser exception only starts on entry to UAT/UAT Fix under `UAT_BROWSER_READINESS_STANDARD.md`. At UAT entry separately verify real connected browser availability and safe target; a complete Prep handoff does not prove browser access.

When Prep alters application code/schema after the prior Integration Review, rerun affected integration/non-browser verification, **refresh the current `INTEGRATION_REPORT.md` to identify the changed candidate** and preserve the earlier immutable history. UAT must inspect this reconciled candidate and exact Prep outputs before attempting logged-in stories. UAT may repair a newly discovered missing Prep item in authorized UAT Fix and re-run its Prep checks, but UAT Fix must not be the normal initial provisioning phase.

**Never** provision production privileged test identities, write to live identity-provider/hosting settings, access real customer data, send unsolicited invitations, purchase services, request arbitrary spending caps or ask humans to paste secrets. If such an action is genuinely required, name one specific legitimate external authorization/action and mark dependent work BLOCKED. Do not claim success for unrun tests or accounts not actually created.

**Final status contract:** `COMPLETADO: Prep READY/PARTIAL/BLOCKED/N/A, version and verified files/test paths, outstanding role blockers. SIGUIENTE PASO: PHDK uat` (or the single required safe owner action). Auto proceeds to applicable UAT without requesting a ceremonial approval.


## Production-first verification override (v2.58.0)

**Mandatory:** Apply [PHDK_PRODUCTION_VERIFICATION.md](PHDK_PRODUCTION_VERIFICATION.md). Owner-authorized production-only UAT supersedes earlier local unit/in-process/runtime testing, staging-only identity, and blanket production-test prohibitions. Local operations are limited to static analysis, lint, typecheck and safe builds; Docker, local runtime tests and separate staging/databases are prohibited. UAT must use existing versioned production deployment and existing database, strictly scoped run-owned synthetic identities/records, audit, automated cleanup and verified revocation on success, failure and interruption. Never touch real data or bypass existing security hooks; a conflicting gate is BLOCKED.
