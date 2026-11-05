# PHDK Risk-Based Critical-Change Assurance

## Applicability, not a legacy-only mode

During Plan and material Auto replanning, assess whether the authorized change can materially affect data integrity, value, permissions/tenant isolation, irreversible external effects or continuity of an existing operation. Examples include migrations, imports, transformations, financial or inventory calculations, authorization changes and replacement of critical workflows. Apply this contract because of the risk, not because a project is old, financial, large or multi-tenant. For ordinary low-risk work, record a brief justified `NOT_APPLICABLE`; do not create empty documents or a new universal approval gate.

This standard supplements `PHDK_PLAN.md`, `PHDK_COMPLETION_GATE.md`, `PHDK_TENANT_RISK_STANDARD.md` where relevant and existing security/delivery rules. It does not authorize running tests, using real data, changing infrastructure or moving operations. `PHDK_PRODUCTION_VERIFICATION.md` and `EXECUTION_SCOPE.md` still govern execution, including the prohibition on local behavioral tests and explicit-only UAT. Auto/Force do not gain UAT or cutover permission.

## One contract in the existing plan

Add a risk/assurance section to the active indexed plan and link existing decision, milestone, test-case and evidence records. A dedicated `docs/plans/critical-change-contract.vN.md` is optional when the scope warrants it; do not create a competing task, status, approval or acceptance ledger. Reuse compatible existing material.

The contract records:

1. Change boundary, impacted capabilities/data/actors, source and target baselines, applicable PHDK version/ref, dependency and ownership boundaries, material failure scenarios and non-goals.
2. Domain invariants and characterization cases: source/rationale, expected outcome, edge cases, tolerance and its decision authority, evidence method, responsible reviewer and affected milestone. Unknowns stay explicit, not guessed defaults.
3. Verification plan: candidate/input identities, deterministic synthetic cases where appropriate, allowed environment and operations, authorization source, isolation/cleanup, resource/cost constraints, actual result and redacted evidence. Planned or authored cases remain `NOT RUN` until executed.
4. Operational transition and recovery when applicable: exact scope, prerequisites, reconciliation, abort criteria, recovery ownership, treatment of writes after transition and the separate cutover authorization/evidence.

Use project-specific domain rules here, not hard-coded business rules in canonical PHDK. Money-related work may need currency/period/state totals, decimal representation, rounding, reversals and historical continuity; inventory may need quantities and reservations; access changes may need deny-by-default and tenant isolation. These examples are not universal thresholds or policies.

## Characterization and equivalence

Preserve and inspect the original behavior/data contract before replacing it. Compare authoritative requirements, source evidence and permitted observations; an old system's output is not automatically correct. Label suspected legacy defects and obtain a domain decision before silently reproducing or correcting material behavior.

Define testable conservation, correspondence, uniqueness, ordering, authorization and historical-integrity rules as applicable. Include edge/failure/retry cases, not only a happy-path total. Define the oracle, agreed tolerances and the evidence needed for equivalence; no arbitrary monetary tolerance or invented approval. Static review, compilation, a successful import command, matching row counts or deployment metadata alone do not prove semantic equivalence.

The proposed isolated characterization profile must name inputs, environment, network/data access, write boundaries, cleanup, resource limits and approval needs before any execution. **This release does not activate a local-test exception.** Author cases during development; execute only through the currently permitted, explicitly authorized verification route. Do not relabel runtime tests as static checks, create a test environment as a workaround, use real data without authority, or infer that synthetic data alone makes execution safe. Where execution is unavailable, report `NOT RUN`/`UNVERIFIED`; block the dependent acceptance/cutover claim, not unrelated authorized source development.

## Material decisions are not routine defaults

Auto Force may resolve ordinary reversible implementation details. It must not invent balances, loss of history, mappings that change meaning, tolerances, entitlement expansions, destructive retention policies, accounting corrections or acceptance of material residual risk. Record the decision source and separate `OWNER_APPROVED`, `AGENT_PROPOSED` and `UNRESOLVED` using the project's existing provenance conventions.

Recover existing owner decisions first. For a genuinely unresolved material choice, provide a concrete recommendation, alternatives and impact, ask only for that decision, and continue independent safe work. A well-defined current request can already supply the authority; do not add a duplicate sign-off. A risk label alone does not block every task.

## Operational transition and recovery

Before any authorized production cutover or real-data transformation, define and evidence the applicable contract:

- Source/target mapping, provenance, completeness/integrity checks and reconciliation at meaningful partitions; backup and a verified recovery path rather than a backup-exists assertion.
- Idempotent operations, bounded batches/checkpoints, retry/resume and partial-failure handling; quarantine/exception handling rather than silently dropping records.
- A defined authoritative writer, or an explicitly designed and validated concurrent-write protocol; freeze/delta/catch-up sequence, synchronization and transition order.
- Measurable abort/stop conditions, responsible operator, precise rollback/roll-forward steps and recovery of writes created after cutover. Reverting application code alone is not a data rollback.
- Required access, approvals and cost scope; exact candidate/data boundary, execution evidence, residual risk and post-transition reconciliation/monitoring within the authorized interactive scope.

If a safeguard is genuinely inapplicable, explain why. No new database, locking service, scheduler, worker daemon or paid tool is required by this standard. Prefer existing controls and finite execution.

A source merge or GitHub-connected autodeploy must not silently perform an unapproved destructive migration, enable replacement traffic or transfer live operational ownership. Keep preparatory changes backwards-compatible or inactive where required; inspect startup/release migration hooks and feature activation paths. When source publication itself would trigger an unauthorized critical effect, block that dependent publication operation until a safe in-scope separation or actual scoped authority exists. Do not call this optional UAT or hide it behind `DEVELOPMENT COMPLETE`.

## Independent delivery, acceptance and cutover evidence

Retain the current PHDK delivery schema and its `IMPLEMENTED`, `PUBLISHED`, deployed-revision and acceptance evidence. Add these human-readable distinctions to the existing plan/delivery report when relevant; do not replace mandatory machine-gate fields or create an alternate completion verifier:

| State | Required meaning |
|---|---|
| `TECHNICALLY_DELIVERED` | The identified source/development goal satisfies the existing completion/delivery contract. This does not prove runtime correctness, business acceptance, a healthy deployment or cutover readiness. |
| `ACCEPTED` | The specified acceptance scope actually passed on the identified candidate with required cleanup and evidence under the applicable authorized UAT contract. A build, synthetic comparison alone or agent opinion is insufficient. |
| `CUTOVER_AUTHORIZED` | A current explicit owner decision covers the exact operational transition, candidate/data boundary, prerequisites, operator and recovery plan. It is not an execution result. |
| `CUTOVER_EXECUTED` | The authorized transition actually ran with recorded reconciliation/outcome and remaining risks. Authorization alone is insufficient. |

Report missing authorization as `NOT_AUTHORIZED`, missing evidence as `UNVERIFIED`, unexecuted cases as `NOT RUN`, and genuinely irrelevant cutover as `NOT_APPLICABLE`. Use the existing `UAT NOT RUN` / `DEFERRED — OWNER OPT-IN` disposition outside an initiated UAT. Do not require operational acceptance/cutover to finish a source-only development mandate, but never claim the whole user goal complete when that goal explicitly includes an unfinished authorized transition.

Material changes to candidate, data mapping, domain rules or recovery assumptions require revalidation of affected evidence and authority before the dependent transition; do not treat stale approval as a reusable flag. No universal expiry duration is invented.

## Continuity, baseline and economical execution

Use `PHDK_INTELLIGENT_EXECUTION.md`, existing `AUTO_STATE.json`, task/milestone records and normal Git handoffs. Record the adopted PHDK version/ref, source/candidate SHA, decisions, evidence, current coordinator/owned paths and next eligible action in a compact resume view. Before a new writer continues, reconcile fresh remote state and ownership; checkpoint only sanitized artifacts through the authorized Git route. Do not invent distributed locks or a parallel authority ledger.

An adopted standards update requires a bounded impact check on the active contract and refreshed affected worker context, not a silent change of business meaning. Preserve owner-excluded legacy code and existing security preflight; recording a baseline is not automatic version pinning or permission to suppress security maintenance. Load only relevant source/rules, prefer a single responsible reader for shared sensitive inputs and use workers only for genuinely independent work. Host-specific worker counts, model names and unmeasured allowance savings are not canonical policy.

## Check and closeout

Pass the applicable contract and its evidence into existing Integration/Check/delivery handoffs. Audit missing invariants, decision provenance, execution permissions, recovery and unverified claims without launching acceptance. An actual mandatory safety/control failure blocks only its dependent operation; optional unrun UAT remains separate from development completion. Propose generalizable framework improvements under `PHDK_RETROSPECTIVE_STANDARD.md`, retaining product-specific mappings and thresholds locally.
