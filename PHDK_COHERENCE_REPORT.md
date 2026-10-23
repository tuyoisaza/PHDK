# PHDK coherence report — v2.63.1

Baseline: `ca9f0b1e6555936cd131304ead26ecc2f60c8807` / v2.63.0. Review date: 2026-10-23. Scope: the owner-supplied phase-transition brief and its planning, task, delivery, delegation and managed-entrypoint dependencies; not an exhaustive audit of every PHDK rule.

## Focused findings and resolution

| Category / severity | Evidence | Resolution |
|---|---|---|
| GAP / High | Existing delivery rules said task files cannot revoke current owner authorization, but did not define a complete construction-to-publication reconciliation record. | Classify restriction lifetime/provenance; retain source, dates, scope, closure and supersession in existing TASK/plan/STATUS. |
| GAP / High | A worker's build-only boundary could be reused without distinguishing the coordinator's later scoped publication authorization or an executor denial. | Refresh affected worker context, preserve history and separate OWNER_AUTHORIZATION, TECHNICAL_PERMISSION, COST_AUTHORIZATION and UAT_AUTHORIZATION. Documents remain evidence, never permission tokens. |
| GAP / Medium | Plan baseline and transition references were not consistently required at task derivation and agent entrypoints. | Record adopted versus verified canonical PHDK version/ref; align Plan, delegation, Auto continuity, AGENTS, SKILL and the native managed block. |
| DEFECT / Medium | The baseline static checker failed because the Secure manifest entry included literal escaped newline characters in its source path. | Restore the intended existing mapping and touched formatting without adding new authority or changing Secure policy. |

## Verification and limits

The 105 baseline files matched canonical blob hashes. The complete changed source and independent authorization/distribution review were examined. Static coherence passed for v2.63.1 and 78 mappings; changed Python AST, relative Markdown references and whitespace checks passed. Guard additions check active sections, fields, routing and distribution, not runtime decisions.

Source review covers the owner's later publication authorization, independent UAT/cost controls, continuing technical denial, unchanged real owner stops and unknown provenance. No behavioral tests, UAT, runtime permission-transition test, provider write or downstream upgrade was executed. DEBATE's later build and executor events are owner-reported; this release does not resolve or independently reproduce that incident.

This report predates publication. The branch/PR/merge and fresh remote main version/SHA/content must be established from actual operations and the final delivery evidence. Previous report follows as historical evidence.

---

# PHDK coherence report — v2.62.1

Baseline: `5e2cf5a1f43c4833a4e294999cd7af05b41805fa` (canonical main, v2.62.0).
Review: 2026-10-22 15:06 UTC.
Scope: reconcile the reported Auto/UAT contradiction with the existing explicit-only acceptance policy. This is a focused source audit and correction, not an exhaustive semantic audit or downstream product verification. The PHDK maintainer owns the fixes below.

## Findings and resolution

| Category / severity | Evidence | Resolution |
|---|---|---|
| CONFLICT / High | UAT_STANDARD.md and PHDK_UAT_PREP.md retained integrated Auto acceptance and stage-45 preparation instructions. | Keep Auto stages 45/50/60 deferred. Fresh explicit UAT includes necessary Prep; standalone Prep stops before acceptance; Fix needs explicit invocation or repair authorization in the active explicit UAT run. |
| CONFLICT / High | PHDK_AUTO.md, PHDK_LIFECYCLE.md, PMO and milestone/delivery guidance still carried automatic acceptance sequences, handoffs and completion examples. | Reconcile executable stage order, dashboards, stale Auto-state handling and final outcomes. Report development/delivery independently from UAT NOT RUN; preserve acceptance criteria as documentation. |
| CONFLICT / High | Check, SEO/AEO, commitment, completion, hook, theme and UX/UI guidance could indirectly require acceptance before development delivery. | Audit source/static evidence and actual product gaps while retaining optional acceptance separately. Preserve real owner/host/security checks and do not fabricate runtime PASS or reopen development from historical UAT failures. |
| GAP / High | The v2.62.0 native policy preface was outside PHDK-MANAGED boundaries; SKILL policy text preceded YAML metadata. | Put the binding authorization rule inside the installed managed block and restore front matter to the first line. Existing manifest mappings remain intact. |
| CONFLICT / Medium | Affected acceptance/JWT/security guidance retained non-production issuers, local runtime or staging assumptions that conflicted with production-first verification. | Use only existing authorized deployment/authentication paths, uniquely run-owned synthetic identities/records, server-side role/tenant enforcement, expiry/revocation and verified cleanup during explicit acceptance. |
| GAP / Medium | Static checks and UAT Prep regression source still allowed or asserted legacy Auto preparation. | Add bounded legacy-clause, deferred-row, managed-rule and entrypoint guards; require vendored SKILL and valid front matter; protect active-policy reads from unsafe paths. Update the existing regression source, including the renamed explicit-preparation heading. |

## Executed verification

- `python scripts/phdk_coherence_check.py`: PASS, v2.62.1, 77 unique manifest mappings; static only.
- AST parsing of `scripts/phdk_coherence_check.py` and `tests/test_uat_prep_policy.py`: PASS; this does not execute behavioral tests.
- `git diff --check`: PASS.
- Complete outgoing source/diff review plus independent cross-reviews of acceptance/security, Auto/lifecycle/delivery and checker logic: completed; identified heading, guard-path and indirect-gate issues were corrected.
- Completion-evidence JSON example: parses as JSON. The executable completion verifier is unchanged.
- VERSION, README and top CHANGELOG release: v2.62.1. Baseline source files were independently matched to their canonical Git blob hashes before edits; actual Git history was subsequently fetched and the baseline index verified.

## Reviewed command boundaries

| Entry | Expected result |
|---|---|
| Auto / Auto Force | Implement the authorized goal, perform permitted source/static checks, deliver and verify the target; Prep/UAT/Fix remain DEFERRED — OWNER OPT-IN with UAT NOT RUN. |
| Fresh explicit PHDK uat | Perform necessary Prep and acceptance within existing access/safety/spending boundaries; report real acceptance and cleanup outcomes. |
| Explicit PHDK uat prep | Prepare/readiness-check authorized run-owned identities and artifacts; no acceptance journeys or implicit continuation. |
| Explicit PHDK uat fix, or repair authorized within active explicit UAT | Repair the authorized acceptance defects and validate within that scope. |
| Designer or Check remediation | Complete authorized source work and permitted checks; user-facing changes do not themselves authorize acceptance. |
| Missing or historical UAT evidence | Keep its truthful separate status; do not fabricate PASS or convert it into an automatic development blocker. |

## Evidence limits and publication

UNVERIFIED: behavioral regression coverage of the checker changes, external agents following the rules, deployed application behavior and downstream adoption. Local behavioral tests and runtime UAT were NOT RUN under the existing execution policy. No live identities, fixtures, production records, provider settings or independent controls were changed.

This source report predates publication. The normal versioned branch/PR merge, final commit prefix, remote main SHA/version/content and unchanged completion-verifier result must be established from actual post-publication readback, retained in the delivery evidence and PR. Next action at this checkpoint: publish the reviewed candidate and verify those results; no background work or downstream upgrade is implied.
