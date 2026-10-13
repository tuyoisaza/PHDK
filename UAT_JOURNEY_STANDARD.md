# UAT Journey, Access and Next Action Standard

Version: 1.0. Applicable to PHDK uat, uat fix, re-UAT and Auto UAT phases.

## Mandatory Company Co fixture gate
For UAT/JWT (when JWT is used colloquially to mean user acceptance testing), read `USE_COMPANY_CO_INFO_FOR_DEMOS.md` before creating test data. It defines 200 synthetic employees in 17 departments, 17 leaders, B2B/B2C buyers, customers, suppliers, project states and transactional fixtures. Map the subset relevant to the actual product domain and privileges; seed idempotently; verify row counts, identities, access, test role switching and evidence. Never send bulk email to `@tujuisasa.com` automatically; verify delivery routing and explicit authorization first. If the term JWT instead means JSON Web Token, never use demo fixture profiles to bypass token authentication/security. This fixture is vendored by `PHDK_MANIFEST.txt`.

## Mandatory execution sequence
1. Inspect project intent, requirements, existing code, routes, APIs, role policies, auth providers, CRUD matrix, fixtures, browser capability and actual reachable deployment. Reconcile implementation with intent; do not invent stories solely from routes.
2. Inventory roles and personas (including public/anonymous), permissions, navigation entrypoints and reachable features in `UAT_ROLE_MATRIX.md`. Mark roles actually verified separately from inferred roles.
3. Verify the actual deployed development candidate URL/revision and authenticate or otherwise access each role; record in `UAT_ACCESS_REPORT.md`. Do not falsely mark a login verified based on source inspection.
4. For absent test users, provision minimal synthetic accounts for each applicable role through existing supported administration or safe seeded fixtures; record account identifiers and cleanup obligations, never credentials, passwords, recovery codes or tokens in UAT artifacts. Do not modify live people's accounts, disable MFA, create privileged backdoors or privilege escalation. Even if the development candidate is hosted at its production URL, treat it as safe for mutations only after verifying that it is a development deployment with synthetic data and the owner-authorized scope. If real users or real production data exist, require explicit authorization and a non-destructive plan; otherwise BLOCKED.
5. Make Superadmin able to choose and test permitted profiles using explicit, auditable role switching/impersonation. Prefer isolated test-user sessions or a deliberately implemented test-mode role switch controlled server-side. Require actual Superadmin permission, unmistakable active-role banner, return-to-superadmin control, start/end audit trail, tenant boundaries, session expiry and server-side authorization checks. Never implement client-side-only role flags, anonymous impersonation, bypasses of MFA, or promotion to disallowed roles. If the feature is missing, record as a requirement/FAIL and route to UAT Fix; test accounts alone are not a substitute.
6. Author `UAT_STORIES.md` grouped by persona/role with stable IDs, intent-linked value, priority, entrypoint and acceptance outcomes. Stories represent user goals, **not** the same thing as executable test cases. Each story maps to one or more deterministic cases in `UAT_CASES.md`.
7. Execute complete real browser/user journeys and permitted API checks on the integrated candidate. Record every step, expected vs actual, user-facing instructions/clarity, interactive/visual feedback, accessibility/focus, errors/retry, full applicable CRUD including detail view, persisted effects, permission-negative tests and cross-role isolation. Do not infer PASS from code inspection or mere navigation/button visibility.
8. Generate `UAT_JOURNEY_MAP.md` with persona → story → case → step → result/evidence, and `UAT_REPORT.md` with per-role coverage, PASS/FAIL/BLOCKED/MANUAL/N/A, proof references, defects and next action.
9. Run UAT Fix on in-scope issues, save defect → root cause → change/revision → evidence in `UAT_REMEDIATION.md`, then rerun failed cases, impacted journeys, role permissions and relevant regressions. Publish `UAT_RETEST_REPORT.md` and updated overall acceptance. Preserve failed history; never rewrite the initial FAIL as if it never happened.

## Identity and access blockers
When interactive authentication requires a human MFA approval or authenticator code, request **the minimal user action** in the user's own secure browser/provider interface; never ask for codes, recovery keys, passwords or tokens in chat. Continue all independent executable cases first. On resumption immediately confirm access and state what will run next, without forcing the owner to reconstruct context.
For each blocker record: case IDs, exact blocked screen/action, reason, safe instructions, actor, resume cue, and remaining runnable work. Do not block unrelated roles/cases. User-initiated stops always respected.

## Required deliverables and gates
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
