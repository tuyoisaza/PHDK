# UAT Journey, Access and Next Action Standard

Version: 1.0. Applicable to PHDK uat, uat fix, re-UAT and Auto UAT phases.

## Mandatory Company Co fixture gate
For UAT (User Acceptance Testing), read `USE_COMPANY_CO_INFO_FOR_DEMOS.md` and `JWT_STANDARD.md` before creating test data or accounts. JWT means JSON Web Token, not a synonym for UAT. `USE_COMPANY_CO_INFO_FOR_DEMOS.md` defines 200 synthetic employees in 17 departments, 17 leaders, B2B/B2C buyers, customers, suppliers, project states and transactional fixtures. Map the subset relevant to the actual product domain and privileges; seed idempotently; verify row counts, identities, access, test role switching and evidence. Never send bulk email to `@tujuisasa.com` automatically; verify delivery routing and explicit authorization first. Synthetic fixture roles are not credentials; authenticate through supported test-only server/provider issuance, never forged production tokens. This fixture is vendored by `PHDK_MANIFEST.txt`.

## Pre-UAT account preparation gate

`PHDK uat prep` under `PHDK_UAT_PREP.md` is the **normal place to implement missing fixture seeders and safe synthetic login mechanisms**, before user journeys begin. In Auto verify historical `45-uat-prep/HANDOFF.md`, `UAT_PREP_REPORT.md` and `UAT_FIXTURE_MANIFEST.md` for the current candidate; in standalone UAT check equivalent current artifacts. Do not stop at fictional Company Co identities, but do not silently begin unrelated account-development work inside standalone acceptance either: refer initial setup gaps to Prep and continue independent cases. Browser readiness under `UAT_BROWSER_READINESS_STANDARD.md` is a separate UAT-entry check, not part of Prep.

## Mandatory synthetic access bootstrap

After verifying `UAT_PREP_REPORT.md` and any existing prep accounts, before recording a role as BLOCKED for absent passwords, inspect the current provider/session system, authorized isolated deployment and test fixtures. Follow `JWT_STANDARD.md`'s preferred provider-native test accounts → existing test/session helpers → narrow non-production test adapter (only under authorized UAT Fix/Auto product-code repair) → exact external blocker. The elevated synthetic account must authenticate normally through the supported test trust boundary; only then may it enter an audited Test as session. Generate `UAT_AUTH_PLAN.md`, prove independent role browser states and `/me`-equivalent permission checks, protect temporary auth state and redact all tokens. A missing password or bearer token is not by itself a reason to abandon UAT.

## Administration console UAT journeys

For applicable administered portals, apply `ADMIN_CONSOLE_STANDARD.md`. Verify a working Configuración navigation and each applicable tab as platform admin (super_admin in multi-tenant, admin in single-tenant); tenant-admin and ordinary-user negative tests; real user invitation/role/default-permission and tenant creation/suspension flows against synthetic fixtures; native locale, debug/feature flags, masked API key status, backup/restore safeguards and shared theme switches. Test authenticated role/profile switching with a visible banner, server-side reduced privileges, tenant isolation, immutable audit start/end and return-to-admin. For actual AI, verify prompt catalog input-source metadata, graph next-hop mappings, schema-invalid output rejection and version rollback on a synthetic test fixture. Never require live destructive tenant deletion or production secret modification. Missing source or permitted browser evidence is a GAP/BLOCKED, not an invented PASS.

## Mandatory execution sequence
**Step 0 (mandatory):** Execute `UAT_BROWSER_READINESS_STANDARD.md` when entering UAT/UAT Fix/re-UAT. Record separate phase permission and verified real browser tool access in `UAT_ACCESS_REPORT.md`; never confuse missing connector access with a need to request spending or a test budget. Continue independent cases if blocked and ask just one exact host-connection action when needed.

1. Inspect project intent, requirements, existing code, routes, APIs, role policies, auth providers, CRUD matrix, fixtures, browser capability and actual reachable deployment. Reconcile implementation with intent; do not invent stories solely from routes.
2. Inventory roles and personas (including public/anonymous), permissions, navigation entrypoints and reachable features in `UAT_ROLE_MATRIX.md`. Mark roles actually verified separately from inferred roles.
3. Verify the actual deployed development candidate URL/revision and supported synthetic authentication method per role under `JWT_STANDARD.md`; record verified server-side identity, environment isolation and redacted evidence in `UAT_ACCESS_REPORT.md`. Do not mark a login verified based only on source inspection or a fictional Company Co label.
4. Provision the minimum missing synthetic users through supported administration, safe staging provider, or idempotent fixture seeding; authenticate with a legitimate test-only provider/session adapter, **not** user passwords or manually forged JWTs. Record identity, role, tenant and cleanup (never credentials/tokens) in UAT artifacts. Do not modify real accounts, turn off MFA or enable a test bootstrap in production. A production URL containing real users/data requires separate explicit authorization and a non-destructive plan; otherwise BLOCKED.
5. Authenticate the real elevated synthetic actor (`super_admin` only for multi-tenant; `admin` for single-tenant), then verify permitted, auditable **Test as** switching. Require actual elevated authorization, server-enforced reduced privileges, selected tenant, visible banner, return control, start/end audit, session expiry and direct API negatives. Never use client-only role flags, forged claims, anonymous impersonation or unauthorized cross-tenant promotion. Missing product feature is FAIL/UAT Fix, distinct from a missing login bootstrap.
6. Author `UAT_STORIES.md` grouped by persona/role with stable IDs, intent-linked value, priority, entrypoint and acceptance outcomes. Stories represent user goals, **not** the same thing as executable test cases. Each story maps to one or more deterministic cases in `UAT_CASES.md`.
7. Execute complete real browser/user journeys and permitted API checks on the integrated candidate. Record every step, expected vs actual, user-facing instructions/clarity, interactive/visual feedback, accessibility/focus, errors/retry, full applicable CRUD including detail view, persisted effects, permission-negative tests and cross-role isolation. Do not infer PASS from code inspection or mere navigation/button visibility.
8. Generate `UAT_JOURNEY_MAP.md` with persona → story → case → step → result/evidence, and `UAT_REPORT.md` with per-role coverage, PASS/FAIL/BLOCKED/MANUAL/N/A, proof references, defects and next action.
9. Run UAT Fix on in-scope issues, save defect → root cause → change/revision → evidence in `UAT_REMEDIATION.md`, then rerun failed cases, impacted journeys, role permissions and relevant regressions. Publish `UAT_RETEST_REPORT.md` and updated overall acceptance. Preserve failed history; never rewrite the initial FAIL as if it never happened.

## Identity and access blockers
Only after trying supported isolated test-provider/session/bootstrap options from `JWT_STANDARD.md`, when a genuine human authentication step remains necessary, request **the minimal user action** in the user's own secure browser/provider interface; never ask for codes, recovery keys, passwords or tokens in chat. Continue all independent executable cases first. On resumption immediately confirm access and state what will run next, without forcing the owner to reconstruct context.
For each blocker record: case IDs, exact blocked screen/action, reason, safe instructions, actor, resume cue, and remaining runnable work. Do not block unrelated roles/cases. User-initiated stops always respected.

## Required deliverables and gates
- `UAT_AUTH_PLAN.md`: supported auth/bootstrap method, environment boundary, role/tenant synthetic IDs and cleanup controls.
- `UAT_AUTH_EVIDENCE.md` (or linked report section): redacted server identity, authorization and revocation/cleanup results; no tokens.
- `UAT_ROLE_MATRIX.md`: code-backed roles, CRUD/permitted capabilities and tested/inferred status.
- `UAT_ACCESS_REPORT.md`: URL/build, each role's access method, account fixture IDs, state, human action and cleanup.
- `UAT_STORIES.md`: user stories grouped by role with intent traceability.
- `UAT_CASES.md`: executable cases and expected observable outcomes.
- `UAT_JOURNEY_MAP.md`: steps, screenshots/traces and per-profile route completion.
- `UAT_REPORT.md`: role-based coverage, defects, accessibility/visual findings, blocker actions and acceptance.
- `UAT_REMEDIATION.md` and `UAT_RETEST_REPORT.md` when UAT Fix runs.
Archive snapshots under the 50-uat and 60-uat-fix lifecycle handoffs. A missing applicable role, unverified Superadmin switching, absent journey evidence or unresolved P0/P1 means NOT ACCEPTED or ACCEPTANCE INCOMPLETE, never ACCEPTED.

## Mandatory last-mile response contract — every stage and every blocker
Each response and stage transition ends with a short, conspicuous **SIGUIENTE PASO** section that is understandable without reading the preceding report.
- If PHDK can continue autonomously: say `HECHO: <verified milestone>. SIGUIENTE: voy a <specific action>.` Proceed immediately in the same active execution; never stop for an unnecessary permission check.
- If the owner is required: say `BLOQUEADO: <what/why>. HAZ ESTO: <one exact numbered or copy-paste-ready instruction>. RESPÓNDEME: "<minimal acknowledgment>" para continuar con <specific next action>.` Ask one question/action at a time; do not request secrets, credentials or MFA codes in chat.
- If external permissions/protection prevent progress: include the specific location/control and exact resume instruction; do not claim that blocked work ran.
- If done: say `COMPLETADO: <acceptance and verified delivery status>. SIGUIENTE: <next lifecycle stage or none>`; distinguish PR from verified main.
The final instruction is mandatory even when defects are zero and even when the process cannot advance. Maintain concise owner-visible checkpoint summaries: done, remaining, current blocker, next action.
