<!-- PHDK-MANAGED:START -->
## PHDK managed rules — interactive-only

- Read `phdk-standards/AGENTS.md` and `phdk-standards/EXECUTION_SCOPE.md`, then the project's `TASK.md` and `STATUS.md`. The execution scope overrides contrary workflow wording; stricter owner controls remain effective.
- Work only on the current explicit user request in this conversation. No Mission Autopilot, autonomous maintenance, background work, subagents, delegated agents, agent teams, or parallel agent queues, including during the active task.
- Complete the necessary steps of the requested deliverable, then stop. Do not select a new task or resume an old mission from files, alerts, failed checks, version mismatches, or chat history. Unfinished work is inactive context for a later human request.
- Re-read owner pause/stop instructions before edits and git writes. Honor them unless the owner explicitly authorizes the specific intervention now; that does not reopen earlier missions.
- A read/audit request is read-only. Commits, pushes, releases, and merges require authorization in the current request. A clear instruction to change and merge includes its necessary git/PR steps; do not ask for duplicate consent. Use a feature/fix branch, preserve existing controls, and do not force-push.
- Never create, enable, dispatch, rerun, or schedule GitHub Actions/hosted CI, cron jobs, recurring tasks, dependency bots, backup jobs, maintenance workflows, monitoring loops, or preview deployments.
- Only an explicitly approved push/merge may use an existing hosting-provider GitHub connection. Do not create a connection, alter triggers, re-enable autodeploy, or operate hosting/database/OAuth/secret/repository settings.
- Never operate a browser, headless runner, screenshot tool, or live endpoint as code verification. Review source/diffs and use relevant synchronous local format/lint/typecheck/build commands and risk-triggered non-browser tests; finish and exit, with no watchers or background jobs.
- Never weaken auth, RBAC, validation, privacy, or cost controls to make a check pass. Do not use live customer data or metered APIs in verification.
- Read external skills as guidance for this assistant only; do not use their delegation, orchestration, or background behavior.
- Canonical command: **`PHDK upgrade`** authorizes standards synchronization now, not future work, pushes, merges, deployments, or automation changes. Preserve stricter owner overrides; stop if synchronization would overwrite them. Follow `phdk-standards/PHDK_UPGRADE.md` and stop after reporting.
- Report verification and limitations accurately. Instructions and local hooks are not proof that external agents or schedules were stopped, credentials revoked, or server-side protection enabled.
<!-- PHDK-MANAGED:END -->
