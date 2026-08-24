# TASK_TRACKING_STANDARD.md

## Purpose

This file defines how PHDK projects track tasks and plans across sessions: file structure, format, archiving, and the rule that task tracking never depends on GitHub Issues, GitHub Projects, or GitHub Actions.

Its goal is a task system that works fully offline, costs nothing, and cannot silently turn into a paid dependency.

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
- GitHub Actions may exist in a project only for CI (build/lint/test on push) when explicitly approved — adding it is covered by the "Adding new external services" Stop-and-Ask condition in `AI_DEVELOPER_OPERATING_MODEL.md`. Even when approved, it must never be the mechanism that tracks or gates slice completion. Slice completion is proven by `VERIFICATION_LOOP.md` evidence, not by a workflow run.
- If an AI developer notices a project has drifted toward GitHub Issues, Projects, or Actions for tracking, flag it in `STATUS.md` as a gap and propose migrating the tracked work back into `TASK.md`/`STATUS.md`.

---

## File Structure

- **`TASK.md`** — the live file for the current working slice only. Replaced when the slice closes, per the archive step below.
- **`STATUS.md`** — persistent, cross-slice memory: Completed Slices, Current Slice, Next Slices, Blocked Slices, current version, gaps, and open questions. Format is defined in `AGILE_SLICE_WORKFLOW.md` Backlog Management.
- **`docs/completed-slices/`** — permanent archive folder in the project repo. One file per closed slice.

---

## TASK.md Format

```md
# TASK — <slice name>

## Slice
User-visible outcome: ...
In scope: ...
Out of scope: ...
Depends on: ...

## Tasks
- [ ] <task description>
  - ID: <short-id>
  - Files: <files touched>
  - Acceptance: <how this is verified>
  - Blocked by: <task id, or none>
- [ ] <task description>
  - ID: <short-id>
```

Rules:

- One `TASK.md` per active slice. Do not accumulate multiple slices' tasks in one file — future slices belong in `STATUS.md`'s Next Slices list, not in `TASK.md`.
- The checkbox is the unit of tracking. When a task grows more sub-tasks mid-slice, add them as nested checkboxes under it — do not spin up a second tracking file.
- `Files` and `Acceptance` are optional but strongly recommended. They are what let the next session, or a different AI tool, resume without re-deriving scope.

---

## Closing a Slice — Archive Step

When a slice is approved and committed (Step 8 of `AGILE_SLICE_WORKFLOW.md`), before starting the next slice's `TASK.md`:

1. Copy the completed `TASK.md` to `docs/completed-slices/<vX.Y.Z>-<slice-name>.md`.
2. Add one line to `STATUS.md`'s Completed Slices list pointing at the archived file.
3. Start a fresh `TASK.md` for the next slice.

This gives a durable, browsable history of what was actually done per slice without relying on git log archaeology or an external issue tracker, and matches the Working Slice Version Rule in `VERSIONING.md`.

---

## Multiple Agents Sharing One Queue

If more than one AI agent or developer draws from the same `TASK.md` concurrently, append a claim marker next to the task being worked (`(@agent-id)`) instead of introducing a locking service. This stays a plain-text convention — no new infrastructure, no account.

---

## Anti-Patterns

- Creating a GitHub Issue per task or per slice instead of a checkbox in `TASK.md`
- Using a GitHub Projects board as the plan
- A GitHub Actions workflow whose job is to report status, sync tasks, or gate "done"
- Leaving completed tasks in `TASK.md` indefinitely instead of archiving and starting fresh
- Multiple slices' tasks piling up in one `TASK.md`
- Skipping the `docs/completed-slices/` archive step and relying on memory of what was done

---

## Verification

- [ ] `TASK.md` exists and reflects only the current slice
- [ ] `STATUS.md`'s Completed / Current / Next / Blocked lists are current
- [ ] The closed slice's `TASK.md` was archived to `docs/completed-slices/`
- [ ] No GitHub Issues, Projects, or Actions are the source of truth for tracking
- [ ] Any GitHub Actions workflow present in the repo is CI only, was explicitly approved, and does not gate slice completion
