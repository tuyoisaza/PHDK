# PHDK Reusable Capability Catalog Standard

## Purpose and authority

This standard defines how PHDK evaluates reusable capabilities during Plan, records catalog maturity, accepts contributions, and separates reusable implementation packages from the PHDK methodology repository.

PHDK remains the methodology, contracts, schemas, validators and public catalog. Reusable implementations belong in separate versioned packages or repositories. A catalog entry is evidence metadata, not proof that software is safe, compatible, installed, operational or accepted in a particular consumer.

Current owner instructions, `EXECUTION_SCOPE.md`, `PHDK_PLAN.md`, `PHDK_PROJECT_MANAGEMENT_STANDARD.md`, security standards, package licenses and actual repository/provider controls remain authoritative.

## Reuse-first portfolio default in Plan

**Portfolio-first:** eligible projects benefit from previously verified project knowledge and reusable modules, and can offer their own proven improvements. At Plan or material feature replanning, inspect relevant existing shared/installed packages and `PHDK_REUSE_CATALOG.json` when a capability plausibly repeats across projects. This is a bounded, relevant check, not blanket cross-repository access or a new mandatory document for every feature.

Before implementing a common capability when a plausible implementation exists, Plan compares three legitimate outcomes:

- **REUSE** — consume an `ACCEPTED_VERSIONED` implementation without materially changing its contract.
- **ADAPT** — use a candidate/reviewed implementation or accepted package as an input, but make project-specific changes and validate the adapted result for this consumer.
- **BUILD** — implement locally because reuse/adaptation has worse fit, integration cost, maintenance burden, compatibility, security, licensing or evidence.

Reuse is never mandatory. Optimize the product outcome, not catalog utilization.

Prefer a compatible accepted package only when evidence supports its integration and maintenance; otherwise ADAPT or BUILD. When there is no eligible implementation, BUILD is legitimate without an empty assessment ritual. Do not block a current user-value milestone on extracting a reusable package.

When the comparison is material, create or update `REUSE_ASSESSMENT.md`. For each capability record:

- requirement/capability and affected milestone;
- catalog IDs or other candidates considered;
- `REUSE | ADAPT | BUILD` decision and rationale;
- functional fit and known gaps;
- integration cost/complexity and expected maintenance burden;
- dependencies and runtime/framework/database compatibility;
- security boundary and review evidence;
- license/redistribution status;
- tests present versus tests observed passing;
- implementation/package maturity and portability evidence;
- project-specific coupling or branding/data cleanup needed;
- delivery impact, including whether evaluation can proceed without delaying the active milestone.

A `REUSE` decision is valid only for `ACCEPTED_VERSIONED`. A `CANDIDATE` or `REVIEWED` entry may be investigated for `ADAPT` only after current-project revalidation. `SPECIFICATION_ONLY` has no implementation to consume.

Planning may identify promising donor modules, but must not delay the active project merely to extract or generalize them. Generalization is a separate contribution outcome after the project capability works.

### Contribute proven capabilities back to the portfolio

After a delivered in-scope milestone, a possibly shared capability may be **proposed** for catalog review. Never auto-extract private donor code, copy customer data, create a package/repository, publish private coordinates, update consumers or start a new task without authorization. A separately scoped contribution needs independently versioned implementation, maintained contracts, supported compatibility, security/license/rights review, and evidence. One observed working consumer can establish `CANDIDATE`, not `ACCEPTED_VERSIONED`; a second independent consumer and observed test evidence remain mandatory for acceptance. The immediate product goal does not wait for portfolio generalization.

## Catalog states

Every catalog entry uses exactly one state:

| State | Meaning |
|---|---|
| `SPECIFICATION_ONLY` | Contract/target exists, but no reusable implementation is published. `implementation: null` and `downloadable: false` are mandatory. |
| `CANDIDATE` | An implementation exists and may merit adaptation/evaluation, but reusable quality/portability has not been established. |
| `REVIEWED` | Contract, dependencies, security/license posture and evidence have been reviewed, but acceptance requirements are still incomplete. |
| `ACCEPTED_VERSIONED` | A separately versioned implementation satisfies the contribution gate, including observed passing tests and portability in at least two distinct consumers. |
| `DEPRECATED` | No longer recommended for new adoption; replacement or withdrawal guidance is required. |

Catalog status is not transitive to a consumer. An accepted package can still be rejected for a specific project.

## Evidence discipline

The canonical machine-readable catalog is `PHDK_REUSE_CATALOG.json`, constrained by `schemas/phdk-reuse-catalog.schema.json` and checked by `scripts/phdk_reuse_catalog_check.py`.

Evidence must be literal:

- tests existing in source is `tests_present: true`, not `test_status: PASS`;
- `PASS` requires observed execution evidence for the cited implementation version;
- an unexecuted check is `NOT_RUN` or `UNKNOWN`, never PASS;
- a mock, screenshot, read-only preview, fixture or specification is not a functional implementation;
- implementation, publication, deployment and user acceptance are separate states;
- acceptance requires its own evidence and never follows automatically from catalog acceptance.

### Machine-readable evidence contract

All declared fields are required, including explicit `implementation: null`; omission is not equivalent to null. Unknown fields and wrong types are rejected. Text fields and reference items must contain non-whitespace text. The schema and standard-library checker share these structural requirements.

Evidence references use records of the form `{"version": "<implementation version>", "references": ["<evidence locator>"]}`:

- `security.evidence` records the review and its threat/isolation assumptions.
- `license.evidence` records the rights review; `license.identifier` names the license or permission basis, and `license.rights` documents applicable use/redistribution rights and conditions. An SPDX identifier is welcome, **not mandatory**: a documented custom license or authorized permission basis is valid. The catalog does not invent redistribution rights.
- `evidence.test_runs` points to observed test-execution results, not just test source or a test-present flag.
- Each `evidence.portability_consumers` item has `consumer`, `version` and `references`, tying evidence to that particular consumer. Two different labels alone do not establish independence.

For `ACCEPTED_VERSIONED`, implementation version and maintenance owner must be assigned (not null, blank or `UNASSIGNED`); maintenance policy must be nonblank. Security must be `REVIEWED`, license `VERIFIED`, tests present and `PASS`. Each evidence category must have records with nonempty references, license identifier/rights must be documented, and at least two distinct consumer identities must each have evidence. All record versions must exactly match `implementation.version`. Specification-only starters retain empty evidence arrays, null license rights/identifier, `NOT_RUN`, no implementation and no download.

The JSON Schema enforces structure, field types and conditional acceptance requirements. The stdlib checker additionally enforces equal implementation/evidence versions and unique entry/consumer identities: standard JSON Schema does not compare values across these records. **Run the checker as well as schema validation**, not one as a substitute for the other. This is an explicit catalog contract, not a general-purpose hand-written JSON Schema engine.

A successful check verifies metadata only. It does not fetch references, prove observed execution, establish license rights or security adequacy, verify independent consumers, or authorize UAT. A reviewer must inspect the cited evidence and its version binding before promotion; stale, fabricated or inaccessible evidence cannot be promoted merely because the record validates. This preserves current-project compatibility and rights review before REUSE.

The regression suite in `tests/test_reuse_milestone_policy.py` generates shared synthetic negative fixtures for missing/extra fields, types, empty evidence and acceptance gates. They are not published packages or real acceptance evidence. Schema parity uses `jsonschema` only if already available and reports a skip otherwise; the distributed checker itself stays standard-library-only. Report any unavailable or unexecuted checks as **NOT RUN**, never PASS.

## Contribution checklist

Before `ACCEPTED_VERSIONED`, a proposed reusable implementation must document:

- purpose and user/product value;
- explicit limits and non-goals;
- stable contracts/interfaces and extension points;
- installation and removal;
- runtime/build/data dependencies;
- supported framework/runtime/database versions;
- owner and maintenance policy;
- license and redistribution rights;
- tests present and the observed result for the proposed version;
- security review and relevant threat/isolation assumptions;
- evidence references and known unverified behavior;
- update/versioning compatibility policy;
- deprecation/withdrawal path;
- portability evidence from a second independent consumer.

The contribution must exclude secrets, personal/customer data, donor-specific branding, environment identifiers, proprietary fixtures and avoidable donor coupling. Extract generic contracts and synthetic examples instead.

## Package separation and portability

Do not place reusable product implementation inside PHDK merely because it is useful across projects. Evaluate it as a separate, independently versioned package or repository with explicit license and maintenance ownership.

A first donor proves only that extraction may be possible. A first consumer proves integration once. A **second independent consumer** is required before `ACCEPTED_VERSIONED`; portability must be demonstrated rather than inferred from architecture or test presence.

PHDK never modifies donor projects or upgrades consumers automatically as part of catalog maintenance.

## Public/private boundary

The canonical PHDK repository is public. Do not publish private repository names, source, inventories, evidence, screenshots, package coordinates or donor-specific implementation details without specific authorization and rights review.

Private candidates may be evaluated inside an authorized private planning context, but the public catalog uses generic contracts and synthetic examples unless publication is separately authorized. A public entry must be safe to disclose independently of its donor.

## Starter composition

`PHDK_STARTER_PROFILE.md` defines a target reusable base for administration/tenancy/roles, synthetic UAT tooling, AI prompt administration, theming and internationalization.

The starter profile is a composition target, not a claim that packages exist. Its canonical catalog entries remain `SPECIFICATION_ONLY` until separate implementations satisfy this standard.

Synthetic identities are always subordinate to `PHDK_UAT_PREP.md`, `JWT_STANDARD.md` and explicit UAT authorization. They never authorize production impersonation, authentication bypass or weakened authorization controls.
