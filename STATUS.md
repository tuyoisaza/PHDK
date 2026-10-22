# PHDK publication status

## v2.62.1 explicit-only UAT coherence correction

Owner request: fix the documented Auto/UAT contradiction. Baseline main: 5e2cf5a1f43c4833a4e294999cd7af05b41805fa / v2.62.0. Candidate branch: fix/v2.62.1-explicit-uat-coherence. VERSION, README and CHANGELOG agree on v2.62.1.

Active acceptance, Auto/lifecycle, delivery, Check and affected entrypoints now defer Prep/UAT/Fix in Auto, preserve explicit command boundaries and separate development completion from UAT NOT RUN. Managed native rules, SKILL metadata and bounded static regression guards are reconciled. Existing security and independent controls remain binding.

Static coherence (77 mappings), changed Python AST syntax and whitespace checks pass; focused independent source reviews are complete. No behavioral tests, runtime UAT, product deployment or downstream upgrade was performed. This is a prepublication checkpoint: actual branch/PR merge, remote-main content and completion-verifier evidence follow in the PR and delivery evidence. Read live publication state before resuming; do not repeat completed publication solely because this checkpoint predates it.

## v2.60.1 historical architecture audit publication

Owner request: publish the prior audit with its own version and verified main link. Baseline main before work: 73c81341d280262343e253687da3b6127d472fbf / v2.60.0. Branch: codex/publish-intelligent-architecture-audit.

The report audits 12bfc70134fca8b5350fde84c01e3110f6d54544 / v2.56.0 and clearly identifies later delegation/context policy changes. It is a historical optional document, not an active standard. No product code, execution policy, infrastructure or downstream repository is changed.

Validation: complete report/diff/reference review, static coherence v2.60.1/75 mappings PASS, and whitespace checks PASS. Delivery: scoped commit, PR, merge and independent remote-main SHA/version/content readback follow. No local behavioral tests or runtime benchmarks are part of this documentary change. Remote publication is not established by this pre-merge status record; consult the PR and remote content for actual outcome.
