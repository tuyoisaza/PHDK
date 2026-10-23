# Case study: bounded planning and implementation in DEBATE

**Optional, non-normative working case study.** Snapshot: 23 October 2026 UTC (22 October evening in Mexico City). This describes a user-selected collaboration pattern, not a new PHDK command, standard, runtime policy or completed-product claim. Current owner instructions and canonical PHDK controls remain authoritative.

## Why record this pattern?

DEBATE is intended to validate a physical debate-card game's experience through an online tactile table before expensive print corrections. The owner requested a detailed plan from Sol 6.1 followed by implementation with Luna, with a coordinator retaining integration responsibility.

The useful separation is **product judgment → precise plan → bounded implementation → evidence review → owner acceptance**. Model names are a dated project choice, not a mandatory routing rule or evidence of lower cost, faster delivery or better quality.

## Roles and durable outputs

| Responsibility | Output | Boundary |
|---|---|---|
| Owner intent and visual decisions | Intent, constraints, chosen direction and decision provenance | A suggested concept is not owner approval. |
| Planner | Work packets, source references, file ownership, dependency order and acceptance criteria | A plan is not implemented behavior. |
| Implementer | In-scope source changes and actual check results | Does not invent unresolved rules or expand infrastructure/spending scope. |
| Coordinator | Diff review, integration, evidence-backed state and scoped delivery | A worker summary alone does not establish completion. |
| Owner review / explicit acceptance | Recorded feedback or acceptance against the identified candidate | Not presumed from silence or from source publication. |

This illustrates existing [intelligent execution](../../PHDK_INTELLIGENT_EXECUTION.md), [Design](../../PHDK_DESIGN.md), [project management](../../PHDK_PROJECT_MANAGEMENT_STANDARD.md) and [delivery](../../MAIN_DELIVERY_STANDARD.md) contracts; it does not replace them.

## A work packet that can be executed

Give the implementer:
- One concrete outcome and its requirement.
- Exact repository, baseline revision and relevant source/design references.
- Allowed write paths, read-only shared paths and dependencies.
- Explicit inputs, interfaces and supported behavior.
- Review criteria and permitted verification.
- Exclusions, unresolved decisions and escalation conditions.
- Expected handoff: changed paths, commit/PR, observed results and remaining limitations.

Prefer independent file ownership for genuine parallel work. Keep shared interfaces, root configuration, versions and changelog under one integration owner. Serialize dependent edits; do not use multiple agents merely to appear parallel. Actual host support and current authorization are prerequisites, not consequences of this document. Follow existing limits on delegation and execution; this case study grants no unattended operation, new scheduling, recursive delegation, publication or deployment authority.

## DEBATE evidence at this snapshot

The planning baseline is [DEBATE PR #1](https://github.com/tuyoisaza/debate/pull/1), draft branch `docs/luna-build-plan`, commit [1ce25f253a4202dd318e5d434df1485d9789888e](https://github.com/tuyoisaza/debate/commit/1ce25f253a4202dd318e5d434df1485d9789888e).

- [Implementation plan](https://github.com/tuyoisaza/debate/blob/1ce25f253a4202dd318e5d434df1485d9789888e/IMPLEMENTATION_PLAN.md): PLAN-000–006, ordered as one MS-001 candidate.
- [Bounded builder brief](https://github.com/tuyoisaza/debate/blob/1ce25f253a4202dd318e5d434df1485d9789888e/docs/execution/LUNA_MS001_PROMPT.md): source implementation handoff.
- The plan references canonical PHDK v2.62.1 at `a0f01defab8c38b1ea70a2363081d12eeea42b69`; newer policy is reconciled explicitly, not silently mixed.
- Luna implementation is in progress at this snapshot. This report establishes no completed implementation, successful build, merged candidate, deployment or runtime acceptance.

MS-001 is a tactile, non-scoring sandbox: EN/ES, card handling, independent tabletop/environment choices and a Rules Lab. It is not the complete multiplayer/AI platform. The plan protects canonical Classic rules and supports explicit experimental variants and immutable per-session rule snapshots. Editable data does not promise arbitrary new mechanics without code.

## Evidence ladder

Record these separately, with links and the exact candidate:
1. Plan exists.
2. Source implements the specified slice.
3. Diff and integration reviewed.
4. Named permitted static checks actually executed, with result.
5. Branch and PR remotely verified.
6. Main integration verified, only when within scope.
7. Deployment independently evidenced, only when within scope.
8. Acceptance explicitly initiated and evidenced, only when authorized.

Missing evidence stays NOT RUN, UNVERIFIED or the specific blocker. A safe build is not interaction proof; a merged PR is not deployment; deployment is not UAT. Apply [production verification](../../PHDK_PRODUCTION_VERIFICATION.md) and explicit-only UAT: generic development, this guide, and a model handoff do not initiate acceptance.

## Monthly learning review

The owner requested a monthly review, beginning 1 November 2026, on the first day in the morning, Mexico City time. Review current decisions, source revisions, stale claims, repeated rework, ownership boundaries and useful examples. Return a concise proposed documentation update with sources.

This is a review cadence, not repository automation or permission to auto-publish, merge, change controls or launch implementation. This optional case study is not a distributed execution dependency and does not change the manifest or policy entrypoints. No performance or cost improvement is claimed without comparable measurements.
