# TASK_TRACKING_STANDARD.md

## Purpose

This file defines how PHDK projects track tasks and plans across sessions: file structure, format, archiving, and the rule that task tracking never depends on GitHub Issues, GitHub Projects, or GitHub Actions.

Its goal is a task system that works fully offline, costs nothing, and cannot silently turn into a paid dependency.

`EXECUTION_SCOPE.md` defines the execution boundary for every task. Tracking files preserve context between human-initiated sessions; they never schedule, launch, or authorize future work.

---

## Status

Read this file when:

- starting `TASK.md` for a new working slice
- updating `STATUS.md`
- closing out a completed slice
- evaluating whether a proposed tool or integration is allowed to be the system of record for tasks

---

## Core Rule

Task and plan tracking is 100% local, plain-text, versioned markdown inside the project repo.

It must work fully offline, with no account, no paid tier, and no third-party service required to read or update it.

GitHub is the git remote for the code. It is never the system of record for tasks.

---

## Why This Exists

Left undefined, "how do we track tasks" tends to drift toward whatever the coding tool defaults to or scaffolds along the way — a GitHub Issue per task, a Projects board, a status-reporting Actions workflow. On a private repo, GitHub Actions minutes and some Projects usage are metered and billable. A project can end up with real cost and a broken tracking view with no single decision that caused it — just accumulated defaults. This file makes the default explicit so it never has to be rediscovered by billing surprise.

---

## Local-Only Rule

- No PHDK project may use GitHub Issues, GitHub Projects (boards), or GitHub Actions as the source of truth for what work is planned, in progress, or done.
- Agents must not create, enable, or scaffold GitHub Actions workflows or another CI automation, even if `ARCHITECTURE_DECISIONS.md` proposes it. Verification stays within the local checks allowed by `EXECUTION_SCOPE.md`. Deployment may only follow a git push through the project's existing pipeline; task tracking never creates or changes that pipeline or repository settings.
- Do not create scheduled tasks, cron jobs, maintenance queues, dependency-update bots, or agents that run outside the active session. A backlog entry is context for a later human-initiated session, not an execution trigger.
- If an AI developer notices a project has drifted toward GitHub Issues, Projects, or Actions for tracking, flag it in `STATUS.md` as a gap and propose migrating the tracked work back into `TASK.md`/`STATUS.md`.

---

## File Structure

- **`TASK.md`** — the live file for the current working slice **plus the mission header**. Replaced when the slice closes; the mission header is carried forward unchanged until the mission is complete.
- **`STATUS.md`** — persistent, cross-slice memory: Completed Slices, Current Slice, Next Slices, Blocked Slices, current version, gaps, and open questions. Format is defined in `AGILE_SLICE_WORKFLOW.md` Backlog Management.
- **`docs/completed-slices/`** — permanent archive folder in the project repo. One file per closed slice.
- **`docs/intents/`** — permanent archive folder for intent files. One file per feature/bug intent, created once and never overwritten — see `INTENT_CAPTURE_STANDARD.md`. Not every slice has one; see that file for when it applies.

---

## TASK.md Format

 ```md
# TASK — <slice name>

## Mission
Goal: ...
Done when:
- [ ] <mission completion criterion>
- [ ] <mission completion criterion>
In scope: ...
Out of scope: ...
Execution mode: Mission Autopilot (active session only)
Branch: <mission feature branch>

## Slice
User-visible outcome: ...
Depends on: ...
Intent: <path to docs/intents/... file, or "none — internal/already covered by PRD.md">

## Tasks
- [ ] <task description>
  - ID: <short-id>
  - Files: <files touched>
  - Acceptance: <permitted source/local verification and any unverified UI/runtime behavior>
  - Blocked by: <task id, or none>
```

Rules:

- One `TASK.md` per active slice. Do not accumulate multiple slices' implementation checkboxes in one file. The mission header persists across slices, while the remaining plan lives in `STATUS.md`'s Next Slices list.
- `Execution mode: Mission Autopilot (active session only)` is the default. The agent continues through planned code/documentation slices within the approved mission and active session, without asking for approval at each transition. It does not create new objectives, future triggers, or unattended execution.
- `In scope`, `Tasks`, and `Acceptance` must comply with `EXECUTION_SCOPE.md`: repository code/documentation and git/GitHub work, with source/diff review and permitted local checks. Record UI/runtime behavior that cannot be verified within that boundary; do not make human browser or manual runtime testing a completion requirement.
- The checkbox is the unit of tracking. When a task grows more sub-tasks mid-slice, add them as nested checkboxes under it — do not spin up a second tracking file.
- `Files` and `Acceptance` are optional but strongly recommended. They are what let the next session, or a different AI tool, resume without re-deriving scope.

---

## Closing a Slice — Archive Step

When a slice is verified, committed, and pushed to the mission branch (Step 8 of `AGILE_SLICE_WORKFLOW.md`), before starting the next slice's `TASK.md`:

1. Copy the completed `TASK.md` to `docs/completed-slices/<vX.Y.Z>-<slice-name>.md`.
2. Add one line to `STATUS.md`'s Completed Slices list pointing at the archived file.
3. If the mission is not complete and the active session can continue, start a fresh `TASK.md` for the next planned slice, carrying forward the same Mission section, and continue. If the session ends, record the remaining work for a later human-initiated session without creating a scheduled resumption or background agent.
4. If the mission is complete, leave no synthetic "next slice" just to keep working; produce the mission report and request Human Diff Review for merge.

This gives a durable, browsable history of what was actually done per slice without relying on git log archaeology or an external issue tracker, and matches the Working Slice Version Rule in `VERSIONING.md`.

---

## Multiple Agents Sharing One Queue

If more than one AI agent or developer draws from the same `TASK.md` concurrently, append a claim marker next to the task being worked (`(@agent-id)`) instead of introducing a locking service. This stays a plain-text convention — no new infrastructure, no account.

Agents may coordinate only within the active, human-authorized mission. Do not create a standing agent queue, autonomous worker, or future invocation to consume `TASK.md` or `STATUS.md`.

### Branch and file ownership

Use isolated branches/worktrees for independent work, or explicitly assign disjoint files when a coordinator has arranged a shared branch. The claim marker provides visibility; branch and file ownership prevent conflicting edits.

- Before claiming a task, an agent checks whether any *other currently claimed* task in `TASK.md` touches the same files or the same `src/features/<feature-name>/` slice — if so, treat it as a soft conflict and either sequence the work (wait) or explicitly split the files between the two tasks before starting, rather than both agents editing the same feature folder in parallel branches
- Two agents producing overlapping changes on separate branches is a merge conflict, not a data-loss risk — git surfaces it at merge time. The claim marker exists so agents notice the overlap *before* investing work in it, not to prevent git from doing its job
- Reaching Step 8 (`AGILE_SLICE_WORKFLOW.md` Commit and push) does not authorize a merge. Preserve Human Diff Review before each merge. After an approved merge, another agent rebases onto the updated `main`/target branch and resolves conflicts before its own review — never force-push over another agent's already-merged work

### If a conflict is discovered mid-task

- Stop and note it in `TASK.md` next to both claimed tasks — do not silently resolve someone else's in-progress work
- If the conflicting task belongs to another live agent session, this is a Stop-and-Ask condition (scope expansion boundary, `AI_DEVELOPER_OPERATING_MODEL.md`) — ask the human how to sequence the two, don't decide unilaterally which agent yields
- If the conflicting task's claim marker is stale (the claiming agent's session ended without releasing it), the human confirms it is safe to reclaim before a new agent picks it up — a stale marker is not, by itself, permission to proceed

---

## Anti-Patterns

- Creating a GitHub Issue per task or per slice instead of a checkbox in `TASK.md`
- Using a GitHub Projects board as the plan
- Adding a GitHub Actions workflow because PHDK supposedly requires CI — it does not
- A GitHub Actions workflow whose job is to report status, sync tasks, or gate "done"
- Treating an architecture decision, backlog item, alert, or schedule as permission to create automation or start a new mission
- Turning dependency maintenance or an unfinished slice into a recurring task or unattended agent
- Leaving completed tasks in `TASK.md` indefinitely instead of archiving and starting fresh
- Multiple slices' implementation tasks piling up in one `TASK.md`
- Treating each slice archive as a reason to stop and wait for human permission
- Skipping the `docs/completed-slices/` archive step and relying on memory of what was done

---

## Verification

- [ ] `TASK.md` exists and reflects only the current slice
- [ ] `STATUS.md`'s Completed / Current / Next / Blocked lists are current
- [ ] The closed slice's `TASK.md` was archived to `docs/completed-slices/`
- [ ] No GitHub Issues, Projects, or Actions are the source of truth for tracking
- [ ] No GitHub Actions workflow, scheduler, maintenance task, dependency bot, or unattended agent was created or enabled
- [ ] Any deployment uses only a git push through the existing pipeline; external configuration and repository settings were not changed
- [ ] Acceptance evidence stays within `EXECUTION_SCOPE.md`; unverified UI/runtime behavior is reported without assigning manual tests to the human
- [ ] Unfinished work is recorded as context, without a future execution trigger
- [ ] Human Diff Review remains required before merge
- [ ] If multiple agents are active, each claimed task in `TASK.md` was checked against other claimed tasks for file/feature overlap before starting
- [ ] No agent force-pushed over another agent's already-merged work to resolve a conflict
