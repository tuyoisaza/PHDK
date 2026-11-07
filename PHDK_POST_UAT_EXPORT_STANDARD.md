# PHDK Post-UAT Export Modules Review

## Purpose, position and authorization

PHDK Auto/Auto Force **collects lightweight reusable-module observations while delivering the authorized product** and links them in the existing `docs/decisions/phdk-process-review.vN.md` retrospective. It does **not** run UAT Prep, UAT, UAT Fix or a full module-export inventory. UAT stages remain **DEFERRED — OWNER OPT-IN** and `UAT NOT RUN` does not block development delivery.

On a **separate explicitly owner-initiated `PHDK uat`**, run one bounded, local, **read-only** Export Modules evaluation **at the first verified final `ACCEPTED` conclusion for the current integrated deployed source revision**. This occurs:

- **After stage 50 UAT**, when all required cases passed, no product repair is required and UAT Fix is NOT APPLICABLE; or
- **After stage 60 UAT Fix**, only when the updated UAT report, defect register, authorized fixes and required deployed retests actually establish `ACCEPTED` on the final revision.

This review is automatically included in the *already authorized UAT closeout*; the owner need not invoke `PHDK export modules` a second time just to obtain the candidate list. It is **not a new Auto milestone, UAT authorization, mandatory product delivery gate or permission to publish**. A standalone explicit `PHDK export modules` remains available for an owner-invoked inventory at another time under `PHDK_EXPORT_MODULES.md`.

## Reuse review lifecycle

1. **During Auto:** retain only material, evidence-backed reuse/extension signals in the existing retrospective and link the product milestone/revision. Do not scan each milestone, add a recurring job or interrupt value delivery. Zero signals is valid. Auto offers `PHDK uat` at its normal completion without scheduling UAT or pretending the post-UAT review ran.
2. **At UAT closeout:** reconcile the actual `UAT_REPORT.md`, the final case catalog, UX acceptance where applicable, active defect register, deployed source SHA and `50-uat/HANDOFF.md`. When UAT Fix ran, also reconcile `UAT_RETEST_REPORT.md` and `60-uat-fix/HANDOFF.md`. A report label alone is not proof.
3. **Gate:** require an explicit current UAT mandate, real `ACCEPTED`, no unresolved required FAIL/BLOCKED/MANUAL or open required defects, verified fix/retest if needed, and a full 40-character accepted source SHA equal to the final currently deployed candidate SHA. Any missing or stale evidence leaves the review `DEFERRED`, `WAITING_FOR_UAT_FIX`, `ACCEPTANCE_INCOMPLETE`, `REVISION_UNVERIFIED`, or `STALE_ACCEPTANCE` as applicable. An incomplete or failed UAT does **not** trigger export discovery.
4. **Assess once on final accepted revision:** run the vendored local read-only `scripts/phdk_post_uat_export.py`, which gates and then invokes the existing `scripts/phdk_export_modules.py`. Compare relevant Auto retrospective findings, the installed public reuse catalog, and donor-local Git provenance when available. For a small set of promising candidates, perform proportionate authorized source review before claiming improvement. Missing local/source evidence remains `NEEDS_EVIDENCE`.
5. **Present one batch at UAT closure:** candidate ID/path, `NEW | EXTEND | STANDARD | LOCAL_ONLY | NEEDS_EVIDENCE`, prior catalog/module version when verified, what changed **and proof**, recommended action, portability/security/license/rights gaps and the intended private-library or PHDK-standard destination. `HIGH` packaging score is review priority, **not** quality evidence. Record `NO_CANDIDATES` when the bounded scan finds none; do not manufacture proposals.
6. **Record without a second ceremony:** add `POST_UAT_EXPORT_REVIEW` with gate, final revision, report/defect evidence links, stable `review_key`, recommendation table or `NO_CANDIDATES`, and `EXPORT_NOT_AUTHORIZED` to the current `UAT_REPORT.md` and final stage handoff. Use a versioned `docs/decisions/phdk-module-reuse.vN.md` and `docs/INDEX.md` only when substantial durable detail is genuinely needed and in scope. This is part of the authorized UAT artifact closeout; never force a new app version or PR merely to record post-merge evidence.
7. **After owner selection:** named candidate(s), specific destination and visibility authorize a *separate scoped contribution* subject to actual code rights, private-repo access, license, security and portability checks. Only then prepare sanitized generic code for private `PHDK-Modules` via its `propose/receive/verify` and private PR workflow. Generic, safe contracts/catalog metadata may be submitted by a separately authorized PHDK PR. Never auto-copy donor code or publish into public PHDK.

## Idempotence, corrections and re-entry

Use the same `review_key` for the same accepted revision plus identical inventory/catalog snapshot. Before creating a report, check the current UAT report and existing linked decision for that key. **Reuse** a prior review instead of duplicating it. A changed source revision invalidates the old review; a newer accepted candidate (after actual UAT Fix/retest) receives a fresh analysis and supersedes the old one. If the installed catalog changed materially, re-evaluate only the changed implications. A prior accepted build does not accept a newer build automatically. Neither a failed/partial UAT nor Auto session rollover initiates or resumes an unapproved acceptance run.

A material security or legal risk discovered while reviewing a candidate prevents **that candidate's export** but does not retroactively invalidate a genuinely completed product UAT run. Surface the risk and separately evaluate whether it actually affects product acceptance. Preserve the `PHDK_AUTO_CONTINUITY.md` bounded foreground session and owner stops. Do not start background workers, watchers, scheduled scanning, new paid services, additional UAT runs or provider operations to complete the review.

## Read-only deterministic helper

The helper is vendored under `phdk-standards/scripts/phdk_post_uat_export.py` (canonical location `scripts/phdk_post_uat_export.py`) alongside the existing inventory helper. An agent derives **this minimal JSON declaration from the real current UAT artifacts**, then passes it via stdin to avoid asking the owner to create a CSV/JSON file or maintaining a separate truth store. Synthetic example — **not real acceptance evidence**:

```json
{
  "schema_version": 1,
  "run_id": "uat-20261107-001",
  "explicit_uat": true,
  "conclusion": "ACCEPTED",
  "tested_revision": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "current_revision": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "open_required_defects": 0,
  "unverified_required_cases": 0,
  "fix_disposition": "NOT_APPLICABLE",
  "evidence_reference": "docs/phdk/lifecycle/uat-20261107-001/50-uat/HANDOFF.md"
}
```

Command (agent supplies actual state through stdin; shell here uses illustration only):

```sh
python3 phdk-standards/scripts/phdk_post_uat_export.py --root . --state - --json
```

`fix_disposition` is `NOT_APPLICABLE`, `VERIFIED_COMPLETE`, `PENDING` or `UNVERIFIED`. The helper accepts `--state <donor-local-path>` when a run already retains an equivalent JSON. It does not create, modify, publish or fetch any file. `READY_FOR_REVIEW` allows a **local inventory** only, not export. `evidence_status: CALLER_MUST_VERIFY_UAT_REPORT` is intentional: a self-declared JSON can never prove the actual source revision, required test coverage, owner permission or the legitimacy of UAT. The agent MUST reconcile the source artifacts and authorization before supplying it. The helper refuses malformed/missing fields, excessive input, unsafe state path or an optional explicit catalog path outside the authorized donor.

The stable `review_key` is a SHA-256 over accepted source revision and the current catalog/candidate inventory, for deduplication; it is not a security signature or package integrity attestation. No source code, credentials, customer files or private package coordinates are read or uploaded by the helper. Candidate evidence remains local to the authorized donor. The current explicit UAT owner's acceptance-testing scope permits this *read-only post-acceptance analysis*; it does not grant broader repository/provider writes, package receipt, customer-data disclosure, UAT restart or continuous monitoring.

## Gate result matrix

| Observed final condition | Review gate | What to report |
|---|---|---|
| Auto done, no explicit UAT | `DEFERRED_UAT_NOT_RUN` | `UAT NOT RUN`; signals retained only |
| UAT has required FAIL/open defects | `WAITING_FOR_UAT_FIX` | Action plan and next explicit UAT Fix decision |
| Required cases blocked/manual/unverified | `ACCEPTANCE_INCOMPLETE` | Missing evidence; no inventory |
| UAT Fix not verified | `WAITING_FOR_UAT_FIX` | Await required deployed retest |
| Missing exact revision evidence | `REVISION_UNVERIFIED` | No inventory; acquire proof in authorized scope |
| Code changed since passing UAT | `STALE_ACCEPTANCE` | Do not reuse old acceptance; explicit new acceptance needed |
| Final accepted revision verified | `READY_FOR_REVIEW` | One local batched candidate list or `NO_CANDIDATES` |

The policy is verified with `tests/test_phdk_post_uat_export.py` using synthetic state. Tests of this policy/helper are **not** application UAT, actual code-portability proof, license review or a real private-library receipt. Preserve `PHDK_REUSE_CATALOG_STANDARD.md` statuses: first implementation is at most `CANDIDATE` pending observed tests and second independent consumer.
