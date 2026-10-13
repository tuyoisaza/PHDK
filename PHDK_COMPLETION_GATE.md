# PHDK Verified Completion Gate

## Principle
An assistant may not equate effort, local edits, a passing formatter, an unmerged PR, or an optimistic status summary with successful delivery. For any current task whose target is remote `main`, COMPLETED requires independently verified delivery and relevant validation. This extends `MAIN_DELIVERY_STANDARD.md`, `PHDK_COMMITMENT_STANDARD.md` and `PHDK_DESIGNER_MODE.md`; it does not authorize background activity, bypass permissions, or silently start another task.

## Mandatory evidence contract
Before declaring COMPLETED, create or update `PHDK_DELIVERY_EVIDENCE.json` in the target project (or another documented, stable project-local evidence path). Use the JSON schema below, with evidence based on actual results, not invented PASS statuses. This is a machine-checkable release record, not a substitute for human judgment.

```json
{
  "version": "1",
  "goal": "current owner-authorized goal",
  "target_branch": "main",
  "expected_version": "0.1.1",
  "version_file": "VERSION",
  "merged_commit_sha": "actual remote main merge commit full SHA",
  "pr_url": "https://github.com/owner/repo/pull/123",
  "checks": {
    "lint": {"status": "PASS", "evidence": "command and result"},
    "typecheck": {"status": "PASS", "evidence": "command and result"},
    "build": {"status": "PASS", "evidence": "command and result"},
    "focused_tests": {"status": "PASS", "evidence": "command and result"},
    "uat": {"status": "PASS", "evidence": "allowed browser/acceptance run and result"}
  }
}
```

Use `NOT_APPLICABLE` with a specific documented explanation only if the check truly does not apply. Use `BLOCKED` when a relevant check could not be performed; never mark it PASS. A visual product must record truthful scoped browser evidence or a BLOCKED/MANUAL limitation. PHDK lifecycle may store evidence in its existing DELIVERY_REPORT and completion audit too, but the machine-readable evidence is mandatory when the gate applies.

## Deterministic gate
Run `python phdk-standards/scripts/phdk_completion_gate.py --evidence PHDK_DELIVERY_EVIDENCE.json` from the target repository when Python and a networked git remote are available. The evidence may specify `version_file` and, for JSON sources, a dot-separated `version_property`; plain-text version files need no property. For example, `services/web/package.json` with `version_property: "version"` reads the package's canonical version. `--version-file` and `--version-property` provide explicit CLI overrides when required. The script independently reads the remote target ref and selected version source; it rejects missing evidence, BLOCKED/FAIL checks, unsafe paths/properties, missing JSON properties, version mismatch, missing/invalid SHA, missing PR URL, and unverified remote delivery.

If tooling or network prevents the gate from executing, record BLOCKED and preserve concrete commands/output; do not declare COMPLETED. A script PASS verifies stated mechanical conditions, not visual quality, user acceptance, hosting deployment, PR review protections, or every scope commitment. The agent must still inspect the PR state, required approvals, task ledger, UAT evidence and actual diff under the existing standards.

## Recovery policy
A recoverable tool failure triggers investigation and bounded alternatives. In particular pnpm non-TTY workspace reconciliation is a packaging/tool invocation problem to diagnose, not automatically a terminal git blocker. Check lockfile/tool versions, repo-local bin and hooks, repair compatible in-scope invocation and retry. Preserve unrelated work and hooks. Do not force-push, use --no-verify, weaken approvals, or endlessly repeat the same failed command. STOP/BLOCKED is correct for genuine access, security, irreparable test or independent-review conditions.

## Final state
Always report: COMPLETE, PARTIALLY DELIVERED or BLOCKED; scope commitments; applicable check results; remote target SHA/version; PR URL and merge status; unresolved blockers. Never write COMPLETE when the mechanical gate fails or any required scope item remains unmerged.
