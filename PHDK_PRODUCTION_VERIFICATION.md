# PHDK Production-First Verification and Synthetic UAT Cleanup Standard

## Authority and scope

This policy applies to PHDK Auto/Auto Force, development, Check, Integration, UAT Prep, UAT, UAT Fix, workers and downstream installations. It supersedes prior PHDK guidance requiring local behavioral tests, in-process tests, local/test/staging deployments, staging-only synthetic identities, or prohibiting all scoped production UAT. Preserve actual repository hooks, legal/security controls, host capability limits and explicit later owner restrictions. A mandatory existing hook is not silently bypassed: if it demands a prohibited runtime test, stop that publication operation as BLOCKED, report the conflict and propose an authorized gate change; never bypass protection.

## Local boundary

Permitted locally: editing/source and diff review, formatting, linting, static typechecking, compilation/builds, and static security/dependency analysis. Inspect scripts before execution: they must not start an application/server, run tests, connect to a database or live service, or launch containers. Do not run local unit, integration, acceptance, browser, API or in-process runtime tests, even against mocks. Do not launch Docker, Compose, local containers, preview servers, local PostgreSQL, SQLite, or other test databases. Tests can be authored locally but must execute only against the authorized deployed production candidate.

## Existing production only

Reuse the application's already existing production deployment, database, identity provider and GitHub-connected autodeploy exactly as configured. Do not create staging, preview, dedicated test environments, new databases, cloud services, credentials, jobs, workflows, provider connections or recurring agents. Do not change provider configuration as a workaround. This policy does not by itself grant unauthenticated access, arbitrary provider writes, deployment CLI privileges, paid API use or secrets access. Source delivery follows normal authorized versioned branch/PR/merge-to-main controls; confirm deployed commit/version after existing autodeploy. Never claim that a merge alone establishes deployment or UAT success.

## Production UAT authorization and safe scope

Only a fresh explicit owner invocation of `PHDK uat` authorizes bounded acceptance against the **existing production application and database**, including its necessary Prep and creating, updating and deleting **only uniquely owned synthetic test records and synthetic identities** needed for the scoped run. Standalone explicit `PHDK uat prep` authorizes preparation/readiness only. UAT Fix requires explicit invocation or repair authorization within an active explicitly initiated UAT run. Auto and Auto Force never invoke, provision, seed or execute these stages; reading this policy, deployment or a prior failure report grants no UAT authorization.

The authorized UAT run is narrowly scoped to test-owned data; it is not permission to modify real users, roles, tenants, records, billing, email delivery, infrastructure or live identity-provider settings. Prefer existing legitimate admin/provider session flows; never expose public login-as-superadmin, weaken MFA, fabricate tokens or introduce a production auth bypass. If safe synthetic authentication or isolation cannot be established, mark impacted tests BLOCKED and continue independently safe cases.

Before any write, establish a run ID, unique test namespace/owner tag, precise enumerated IDs, tenant boundary, allowed operations, data ownership proof, rollback/cleanup design and an automatic expiry/revocation plan. Use synthetic records that cannot be confused with real users. Never run destructive, load, payment, email, external side-effect, permission escalation or cross-tenant mutation tests against real data. Limit writes to test-owned IDs with server-enforced authorization; avoid bulk/unscoped DELETE/UPDATE and avoid destructive schema migrations. If safe targeting and rollback cannot be proved, do not perform the write: report BLOCKED. This safety restriction remains even in Auto Force.

## Sequence, evidence and cleanup

1. Implement candidate and run only allowed static local checks/builds.
2. Version, commit, deliver to `main` through authorized GitHub workflow; use existing production autodeploy.
3. Read back deployed revision/URL/provider status without claiming runtime success from deployment metadata alone.
4. Auto/Force complete their authorized development delivery with the actual development/deployment state and **UAT NOT RUN**; Prep/UAT/Fix remain **DEFERRED — OWNER OPT-IN**, not a completion prerequisite. Offer optional future `PHDK uat` without waiting as a delivery gate. Only after an explicit Prep/UAT invocation, prepare repeatable minimal synthetic fixtures and legitimate sessions in the existing production database, enforcing safe ownership and tenant boundaries. Standalone Prep stops after readiness and cleanup; browser work remains confined to explicitly authorized UAT/UAT Fix.
5. Within an active explicitly initiated UAT run, execute permitted functional/integration/acceptance/browser tests against **that deployed revision in production** and record real outcomes. Never substitute in-process/local tests or run acceptance from Auto.
6. When UAT Fix is explicitly authorized, repair failures through new versioned delivery and rerun affected permitted cloud tests. Each cloud test report records SHA, version, environment, timestamps, cases, observations and redacted evidence. Prior UAT failures never reopen completed development or authorize a new acceptance run.
7. At end of each run **including PASS, FAIL, BLOCKED, interruption or cancellation**, clean up in a fail-safe controlled closeout: revoke test sessions/tokens and temporary permissions, delete only run-owned synthetic users/tenants/records using exact IDs and safe dependency order, remove only temporary UAT-only mechanisms, and verify absence with scoped readback. Never remove legitimate product features or real user accounts. Preserve sanitized evidence, no secrets.
8. Cleanup must be idempotent, audited and retryable; use short expiry and an approved recovery path for interruptions. If cleanup cannot complete or be verified, report `CLEANUP_BLOCKED`, identify remaining resources and risk, and never report COMPLETED/ACCEPTED or claim clean production. Do not silently defer cleanup or invent evidence.

## Gate semantics and policy coherence

Local static PASS is not behavioral PASS; merged or deployed is not accepted. Required runtime cases left unexecuted within an authorized UAT run are BLOCKED/UNVERIFIED as appropriate. Outside such a run, report **UAT NOT RUN** and keep development status independent; absence of optional acceptance is neither BLOCKED nor FAILED development. Existing required hooks/security gates cannot be skipped; reconcile conflicts under `PHDK_HOOK_COMPATIBILITY.md` rather than running forbidden local runtime tests. PHDK Check must detect conflicting authorization, environment and evidence requirements without launching acceptance. No new CI or paid resources may be created for this policy.


## Hook compatibility (v2.61.0)

Apply [PHDK_HOOK_COMPATIBILITY.md](PHDK_HOOK_COMPATIBILITY.md). Inspect effective Git hooks and nested package scripts before push; a local behavioral test required by a legacy PHDK hook is an AUTO-FIXABLE policy violation, not a reason to request a local-testing exception. Within authorized Auto/Auto Force/Check Fix, replace **only proven PHDK-owned** prohibited test invocations with permitted static checks while preserving security/version/branch/commit gates. Owner-owned, external, or unknown hooks remain unchanged absent explicit authorization; report BLOCKED if they prevent push. Never execute prohibited tests or use --no-verify.
