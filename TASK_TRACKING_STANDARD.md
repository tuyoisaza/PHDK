# TASK_TRACKING_STANDARD.md

## Purpose and authority

Track work as local, plain-text, versioned Markdown in the repository. `EXECUTION_SCOPE.md` governs every task. Tracking files are context, not authorization, schedulers, or agent queues.

GitHub remains the code remote, not the task system. Do not create Issues, Projects, Actions, task-sync workflows, or external services to maintain PHDK's task state.

## Interactive-only task rule

Only the current explicit user request activates work. A backlog checkbox, old mission, failed check, alert, installed skill, or a file marked active cannot start a session or authorize an edit, commit, push, merge, or deployment.

One assistant handles the current request. Do not delegate tasks, create subagents, coordinate agent teams, or distribute a task queue, including inside the current session.

Stop when the deliverable is complete or blocked, the user pauses it, or the conversation ends. Proposed follow-ups remain inactive until a later explicit user request.

## Files

- `TASK.md`: the current request, scope, owner controls, completion criteria, git authorization, and necessary implementation steps.
- `STATUS.md`: durable completed/current/proposed/blocked context, versions, evidence, gaps, and open decisions.
- `docs/completed-slices/`: archived completed task/slice records when an archive is useful for the current change.
- `docs/intents/`: immutable intent records when required by `INTENT_CAPTURE_STANDARD.md`.

Do not add infrastructure, a locking service, or a standing worker to consume these files.

## TASK.md template

```md
# TASK — <current user-requested deliverable>

## Authorization and scope
Current request: <the user's request in this conversation>
Status: <in progress in this conversation / complete / paused / blocked>
Execution mode: interactive-only, single assistant, no delegation
Goal: ...
Done when:
- [ ] <objective completion criterion>
In scope: ...
Out of scope: ...
Owner stop/pause controls: ...
Git actions authorized now: <none / commit / push / create PR / merge>
Branch: <authorized feature/fix branch, or not applicable>

## Necessary steps for this request
- [ ] <step>
  - Files: <relevant paths>
  - Acceptance: <source review and allowed local checks>
  - Blocked by: <decision/dependency, or none>

## Inactive follow-up context
<proposals or unfinished work; NOT authorized for execution>
```

A recorded authorization summarizes the current conversation; copying it into a later session does not renew permission. A current request to implement and merge includes the necessary branch/commit/push/PR steps. An audit request remains read-only.

## Before each mutation

Re-read the current task and owner pause/stop instructions before editing, committing, pushing, or merging. Honor the narrowest restriction. A specific current owner instruction may authorize a limited intervention in a paused project; it does not restart old work or remove the pause generally.

If task files disagree with the current request, resolve only the ambiguity needed for that request. Never treat stale metadata as permission to expand the task.

## Closing work

1. Record the completed outcome and actual verification evidence.
2. Archive a coherent completed slice when appropriate and link it from `STATUS.md`.
3. Mark the request complete, paused, or blocked.
4. Keep unfinished and proposed follow-ups inactive.
5. Perform git actions only when currently authorized; a slice boundary does not require a commit or push.
6. Report and stop when the requested deliverable is complete.

Multiple necessary steps of the same current request may be completed without repeated approval. This does not authorize selecting a new goal from the backlog.

## Concurrent edits

Do not create or use a multiple-agent queue. If another human or independently active session changes overlapping files, preserve their work and stop on material conflicts. Do not decide that an old claim marker is safe to reclaim or force-push over another change. Use current branch and commit identifiers when preparing authorized git writes.

## Verification

- [ ] Current user authorization and owner restrictions are accurately recorded.
- [ ] Only necessary steps of the requested deliverable were executed.
- [ ] No subagents, agent team, delegated work, scheduler, recurring task, or background watcher was started.
- [ ] No GitHub Actions/hosted CI job was created, enabled, dispatched, rerun, or scheduled.
- [ ] Local checks are synchronous and relevant; UI/live runtime limitations are stated.
- [ ] Commit/push/PR/merge actions match the current user's authorization.
- [ ] Proposed or unfinished follow-ups are inactive.
- [ ] Completion does not automatically start another task.
