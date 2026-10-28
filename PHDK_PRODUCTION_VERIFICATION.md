# PHDK Production-First Verification and Synthetic UAT Cleanup Standard

## Authority and scope

This policy applies to PHDK Auto/Auto Force, development, Check, Integration, UAT Prep, UAT, UAT Fix, workers and downstream installations. It supersedes prior PHDK guidance requiring local behavioral tests, in-process tests, local/test/staging deployments, staging-only synthetic identities, or prohibiting all scoped production UAT. Preserve actual repository hooks, legal/security controls, host capability limits and explicit later owner restrictions. Before executing, declaring BLOCKED or asking about an ambiguous/conflicting build, packaging check or hook, apply the [hook decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure). Repair only within its authority; a mandatory control still requiring prohibited execution blocks the dependent publication operation with a concrete proposed resolution. Never bypass protection.

## Local boundary

Permitted locally: editing/source and diff review, formatting, linting, static typechecking, compilation/builds, and static security/dependency analysis. Inspect scripts before execution: they must not start an application/server, run tests, connect to a database or live service, or launch containers. Do not run local unit, integration, acceptance, browser, API or in-process runtime tests, even against mocks. Do not launch Docker, Compose, local containers, preview servers, local PostgreSQL, SQLite, or other test databases. Tests can be authored locally but must execute only against the authorized deployed production candidate.

Executing a compiler or other static tool is not itself an application runtime test. Loading compiled application/API modules through `import()` or `require()` to verify that they load is runtime verification, even without networking/listeners. A build that includes that load check is mixed; use the [decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) to classify and reconcile it before execution or a permission prompt. Static parsing/resolution without application evaluation remains distinct from a runtime load check.

## Existing production only

Reuse the application's already existing production deployment, database, identity provider and GitHub-connected autodeploy exactly as configured. Do not create staging, preview, dedicated test environments, new databases, cloud services, credentials, jobs, workflows, provider connections or recurring agents. Do not change provider configuration as a workaround. This policy does not by itself grant unauthenticated access, arbitrary provider writes, deployment CLI privileges, paid API use or secrets access. Source delivery follows normal authorized versioned branch/PR/merge-to-main controls; confirm deployed commit/version after existing autodeploy. Never claim that a merge alone establishes deployment or UAT success.

## Narrow non-UAT deployment revision readback

After an authorized GitHub→production release, or a specific request to check the live version, use `PHDK_DEPLOYMENT_VERSION_STANDARD.md`: a single bounded read-only `GET /health/version` to the existing public production hostname may compare returned version and full build commit SHA to the expected deployed artifact. No provider dashboard, site navigation, browser, credentials or paid/new service is required. It is **revision evidence only**, not functional health, replica-wide readiness, UAT or a general exception for application API probes. A missing/mismatched/unreachable endpoint is UNVERIFIED or STALE, never a reason to fabricate deployment completion. Respect current owner/host limits, and never poll; a second GET requires separate provider-completion evidence.

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

Apply the [hook decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) before execution, BLOCKED or a question about a build/packaging/hook conflict. A proven PHDK-owned local runtime-test invocation may be repaired within authorized implementation/Auto/Check Fix while preserving independent controls and disclosing runtime coverage as NOT RUN. Preserve owner/external/unknown gates except a specifically authorized owner-controlled change; prepare a concrete unresolved decision and block only the operation still prevented by the real control. Never execute prohibited tests, ask for a local-testing exception or use --no-verify.
