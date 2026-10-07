# CHANGELOG.md

## v2.33.0 — 2026-10-07

### Added

- Added `MAIN_DELIVERY_STANDARD.md` and its manifest/routing entry. A current implementation/fix/update request includes scoped versioned branch/PR delivery through the requested change and version verified on remote `main`, unless the user explicitly limits delivery or specifies another target.
- Included necessary normal integration conflict resolution, final version reconciliation, checks, required review, and merge within the same requested outcome; a branch push or open PR is not completion for a `main` target.

### Fixed

- Preserved current authorization across same-conversation status/link questions, clarifications, compaction, and assistant-written tracking updates. Task records cannot independently revoke permission; genuine owner stops remain binding, and old records cannot resume work in a new conversation.
- Removed PHDK's universal human-review gate for ordinary normal delivery. Human review remains required for high-risk changes and stricter owner/repository rules, with truthful review evidence and all existing controls intact.
- Reconciled QA/versioning wording: use the repository's version source, prepare the version on the working branch, and do not add another bump, version-only commit, or push merely because already-versioned changes were merged.
- Separated code integration from deployment. Existing provider GitHub autodeploy is allowed; PHDK must not disable it or add dummy never-matching watch filters to enforce restrictions on autonomous work. Observed deployment blockers/statuses are reported separately without granting provider configuration writes; valid service-specific filters and intended skips for unaffected services remain normal.

### Migration and limits

- Existing installations require a requested sync and reconciliation of conflicting assistant-written task-state snapshots. Preserve genuine owner restrictions and existing hooks/protections; a standards update does not change GitHub/Railway settings.
- Developer Mode retains explicit activation, its narrow direct-main path, and immediate hard stops. Bare `PHDK upgrade`, read/audit/plan requests, and explicit local/branch/PR-only requests retain their scope limits. No browser testing, live probes, provider writes, Actions dispatch, scheduled work, or autonomous continuation is added.

### Verification

- Verified all 43 original Git blobs, the 25 manifest mappings, version/skill metadata, new Markdown references, managed-rule markers, preserved history/hooks/scripts/archives, and diff whitespace.
- Reviewed 11 policy scenarios covering complete delivery, task continuity, real stops, new conversations, narrower targets, required review/hooks, integration conflicts, squash/version handling, Developer Mode failures, and provider deployment evidence. Clarified valid service-specific filters and the existing bounded read-only log exception after that review.

## v2.32.0 — 2026-10-06

### Added

- Added explicit, temporary `PHDK Developer Mode`, activated by `PHDK modo developer` or `PHDK Developer Mode` and exited with `PHDK salir de developer mode` or the end of the active conversation.
- Authorized the requested edit, repository-standard version bump, applicable local checks, version-prefixed commit, and fast-forward push to `main` for eligible small, low-risk tasks requested while the mode is active. Existing deployment connections may react to that push; provider deployment commands and configuration remain excluded.
- Added `PHDK_DEVELOPER_MODE.md` to the vendoring manifest and routed its commands through the skill, managed rules, onboarding, and task/git standards.

### Fixed

- Replaced the blanket ban on live-service logs with bounded read-only retrieval of existing logs through an authorized provider API/CLI/connector for a current requested diagnosis. This permission is independent of Developer Mode and requires finite target/time/result/timeout bounds and redaction of sensitive data.
- Kept authentication, authorization, secrets, data/migrations, payments, infrastructure, permission-policy changes, and other high-risk work in the normal review flow. Failed applicable checks, rejected/non-fast-forward pushes, and unsatisfied controls stop the direct-main flow; no hook/protection bypass, settings changes, forced updates, or automatic retry.
- Removed the legacy Finetuning flag as a separate direct-main permission and reconciled bootstrap text that could otherwise revive old missions. No activation persists in task files, flags, hooks, or later conversations.

### Verification

- Validated the skill metadata, version consistency, all 24 manifest mappings, new Markdown references, managed-rule markers, and diff whitespace. Existing source blobs and preserved history/hook/script files were checked against the canonical base.
- Reviewed 13 fresh-context policy scenarios covering activation, task boundaries, low/high risk, failed checks, protected or advancing `main`, exit, log reads, and unavailable hooks. Reconciled the normal verification-repair wording with Developer Mode's stop rule.

### Migration

- Existing projects need an explicitly requested standards sync to receive the new manifest entry and managed rules. A standards update never activates Developer Mode. Policy changes retain normal review even when they are documentation files.
- No agents, Actions, schedules, monitoring streams, browser tests, application probes, provider writes, or external configuration are introduced. Updating these instructions does not disable existing external automation.

## v2.31.1 — 2026-10-04

### Interactive-only execution; no delegated agents or GitHub Actions

- Removed active-session Mission Autopilot and bounded delegated-agent permissions. One assistant handles the current explicit user request; no subagents, teams, queues, autonomous reviewers, background work, or post-session continuation.
- Made audits read-only and commit/push/merge/release authority dependent on the current request. An explicit implement-and-merge instruction includes its necessary git/PR steps; old task files and checklists do not grant authorization.
- Prohibited creating, enabling, dispatching, rerunning, or scheduling GitHub Actions/hosted CI, in addition to cron jobs, bots, recurring backups, monitoring and maintenance loops.
- Kept relevant synchronous local code checks and isolated non-browser tests; no persistent watchers or automatic follow-up work.
- Preserved stricter owner controls during standards upgrades and clarified that updated instructions do not terminate external agents, revoke credentials, disable existing schedulers, or enforce remote branch protection.
- Updated the execution/routing, skill, managed native rules, task/slice, onboarding, summary, and git/version guidance for this boundary.
- Retained `EXECUTION_SCOPE.md` and the managed rules in the existing vendoring manifest. No workflows, agents, or schedules were added.

### Migration

The canonical `main` version becomes v2.31.1 after this patch is merged. Existing projects require their own explicitly requested standards sync. Their installed automation and external settings are not changed by updating this repository.

### Preserved history

The complete previous changelog is preserved byte-for-byte in [ORIGINALS/CHANGELOG-through-v2.31.0.md](ORIGINALS/CHANGELOG-through-v2.31.0.md). It describes historical releases only; its former autonomy or automation permissions are superseded by the current `EXECUTION_SCOPE.md`.
