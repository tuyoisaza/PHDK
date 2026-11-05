## v2.79.0 — 2026-11-05

### Company Co commercial scenarios
- Add a fictional, structured commercial scenario with opportunities, draft campaigns, knowledge, agent configuration and example usage, linked to the existing Company Co service cases.
- Include the readable and JSON catalogs in the manifest. No external dispatch, actual billing, production seed or UAT is implied.

## v2.78.0 — 2026-11-05

### Auto learning closeout and risk-based critical-change assurance
- Add vendored `PHDK_RETROSPECTIVE_STANDARD.md`: every Auto/Force run prepares an evidence-based process review with the final authorized change and reports actual publication before learning/proposals. Distinguish canonical candidates, local-only actions, already-supported behavior, rejected proposals and missing evidence; zero findings and partial closeouts are valid. No new approval gate, automatic upstream issue/PR, cross-project write or report-only release loop.
- Add vendored `PHDK_CRITICAL_CHANGE_STANDARD.md`: conditional invariants, characterization/equivalence planning, material-decision provenance, idempotent transitions, checkpoints, reconciliation and recovery including post-cutover writes. Apply by integrity/value/access/continuity risk, not only to legacy or financial systems. Reuse existing plans and continuity records.
- Keep technical delivery, actual acceptance, cutover authorization and executed transition independently evidenced. Prevent a source merge/autodeploy from silently triggering an unauthorized critical operation. Preserve the existing machine-readable completion schema and source/requirement reconciliation.
- Wire the contracts through Auto, Plan, completion reporting, README, coherence review and the vendoring manifest; add `scripts/phdk_learning_risk_check.py` and bounded source-review scenarios. Existing agent/skill/native routes still load Auto/Plan/completion; no command or persistent authority flag is added.
- Preserve prior release history byte-for-byte in linked `CHANGELOG-through-v2.77.0.md`.

### Verification and limitations
- The two new policy texts passed the read-only contracts-only source check; three intentional document-marker omissions were correctly rejected. Python syntax compilation passed. These are static document checks, not application or agent-behavior tests.
- Full canonical/vendored coherence execution and the networked completion-gate CLI were not run in this connector-only workspace; no runtime, UAT, sandbox, migration or downstream-adoption PASS is claimed. Remote PR/main evidence is verified and reported separately during publication.
- The proposed local isolated-test exception is NOT activated. Local behavioral-test restrictions, explicit-only UAT, real controls, security Preflight, owner exclusions and spending boundaries remain unchanged. No downstream repository, infrastructure, model selection or background agent is changed by this release.

## Earlier releases

The complete preceding changelog is preserved in [CHANGELOG-through-v2.77.0.md](CHANGELOG-through-v2.77.0.md), including its links to older archives. Historical release notes are not current execution authority.
