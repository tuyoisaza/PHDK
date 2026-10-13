# PHDK Coherence Standard

## Mandatory canonical release review
Before publishing PHDK, inventory applicable standards, manifest files, scripts, agent entrypoints and changed dependencies. Review contradictory requirements involving Preflight, AUTO/PMO, delegation, UAT/browser permissions, security scope, delivery, and completion evidence. Record exact conflicting files and smallest fixes. Documentation never substitutes for implementation and executed test evidence.

## Preflight policy
Run universal Preflight ONCE at each PHDK command entry. For stages inside Auto/PMO, validate upstream handoffs and check newly relevant capabilities without repeating full Preflight. Repeat the universal audit only if installation, VERSION, manifest, or managed instructions have changed or failed integrity checks.

## Release gates
- VERSION, README and newest CHANGELOG release must match.
- Every vendoring manifest source must exist, with unique safe source/destination paths.
- Run the static coherence checker and applicable existing repository checks when an execution environment is available. A static pass does not certify semantic coherence or behavior.
- Review full outgoing diff for conflicting instructions and non-vendored new dependencies.
- Reconcile PR checks, reviews, target main SHA, version and commit evidence after merge.
- Do not claim COMPLETE for untested behavior, open required PRs, or unverified remote main.

## Audit report
Use PHDK_COHERENCE_REPORT.md with baseline SHA, timestamp, scope and coverage; categorized findings (CONFLICT, GAP, RISK, VERIFIED, UNVERIFIED, N/A), severity, evidence, owners, remediation and exact next action. Distinguish sampled checks from exhaustive audit. A new conversation may run a fresh review on request; no passive background monitoring or inferred authorization to change unrelated repositories.
