# CHANGELOG.md

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
