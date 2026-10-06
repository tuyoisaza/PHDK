# TASK_TRACKING_STANDARD.md

## Purpose and authority

Track work as local, plain-text, versioned Markdown in the repository. `EXECUTION_SCOPE.md` governs every task. Tracking files are context, not authorization, schedulers, or agent queues.

GitHub remains the code remote, not the task system. Do not create Issues, Projects, Actions, task-sync workflows, or external services to maintain PHDK's task state.

## Interactive-only task rule

Only the current explicit user request activates work. A backlog checkbox, old mission, failed check, alert, installed skill, or a file marked active cannot start a session or authorize an edit, commit, push, merge, or deployment.

One assistant handles the current request. Do not delegate tasks, create subagents, coordinate agent teams, or distribute a task queue, including inside the current session.

Stop when the deliverable is complete or blocked, the user pauses it, or the conversation ends. Proposed follow-ups remain inactive until a later explicit user request.

### Developer Mode is not task state

`PHDK_DEVELOPER_MODE.md` defines the explicit conversation-only commands `PHDK modo developer` / `PHDK Developer Mode` and exit command `PHDK salir de developer mode`. Mentions, quotations, documentation, and historical Finetuning records do not activate it. Never store activation/status or an authorizing flag in task/status files, repository configuration, memory, or environment flags; never restore it automatically. Conversation end ends the mode.

The live activation authorizes the defined version/check/version-prefixed-commit/fast-forward-push steps for eligible small, low-risk tasks requested while active, without duplicate consent. It does not activate an existing task or authorize selecting backlog work. Authentication/authorization, secrets, data/migrations, payments, infrastructure, and permission/agent-policy changes stay in normal review. Existing hooks, protections, and owner controls remain binding.

Record the requested outcome, changed files, checks, resulting version/SHA, and actual delivery as facts. Do not record a reusable grant to push `main`. A failed applicable check, rejected push, non-fast-forward update after `main` advanced, or unmet control stops the direct flow; record the blocker and explain instead of retrying automatically, rebasing, force-pushing, changing settings/hooks/credentials, or changing API/CLI to bypass it.

## Files

- `TASK.md`: the current request, scope, owner controls, completion criteria, task-specific git request, and necessary implementation steps; never mode activation/state.
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
Execution boundary: interactive-only, single assistant, no delegation; no stored mode state
Goal: ...
Done when:
- [ ] <objective completion criterion>
In scope: ...
Out of scope: ...
Owner stop/pause controls: ...
Task-specific git request: <current instructions as historical context, not a permission token>
Branch: <branch actually used, or not applicable; never an enabling flag>

## Necessary steps for this request
- [ ] <step>
  - Files: <relevant paths>
  - Acceptance: <source review and allowed local checks>
  - Blocked by: <decision/dependency, or none>

## Inactive follow-up context
<proposals or unfinished work; NOT authorized for execution>
```

A recorded task-specific request summarizes history; copying it into a later session does not renew permission. It must not store Developer Mode activation or authorize restoration. A current request to implement and merge includes the necessary branch/commit/push/PR steps. An audit request remains read-only even while Developer Mode is active.

## Before each mutation

Re-read the current task and owner pause/stop instructions before editing, committing, pushing, or merging. Honor the narrowest restriction. A specific current owner instruction may authorize a limited intervention in a paused project; it does not restart old work or remove the pause generally.

If task files disagree with the current request, resolve only the ambiguity needed for that request. Never treat stale metadata as permission to expand the task.

## Closing work

1. Record the completed outcome and actual verification evidence.
2. Archive a coherent completed slice when appropriate and link it from `STATUS.md`.
3. Mark the request complete, paused, or blocked.
4. Keep unfinished and proposed follow-ups inactive.
5. Perform git actions only when currently authorized, including eligible delivery under explicitly active `PHDK_DEVELOPER_MODE.md`; a slice boundary does not supply permission or require a commit/push.
6. Report and stop when the requested deliverable is complete.

Multiple necessary steps of the same current request may be completed without repeated approval. This does not authorize selecting a new goal from the backlog.

An eligible Developer Mode push may trigger the existing hosting-provider GitHub connection. Record deployment evidence only when available; never create or run Actions, deploy through Railway/provider CLI/API/dashboard, or change external configuration. Separately authorized, finite read-only API/CLI log queries follow [Bounded read-only log diagnostics](EXECUTION_SCOPE.md#bounded-read-only-log-diagnostics), with redaction and no runtime probes, watchers, or writes; they do not require Developer Mode or authorize git delivery.

## Concurrent edits

Do not create or use a multiple-agent queue. If another human or independently active session changes overlapping files, preserve their work and stop on material conflicts. Do not decide that an old claim marker is safe to reclaim or force-push over another change. Use current branch and commit identifiers when preparing authorized git writes.

## Verification

- [ ] Current user authorization and owner restrictions are accurately recorded.
- [ ] Only necessary steps of the requested deliverable were executed.
- [ ] No subagents, agent team, delegated work, scheduler, recurring task, or background watcher was started.
- [ ] No GitHub Actions/hosted CI job was created, enabled, dispatched, rerun, or scheduled.
- [ ] Local checks are synchronous and relevant; UI/live runtime limitations are stated.
- [ ] Commit/push/PR/merge actions match the current user's authorization.
- [ ] Developer Mode was not stored or restored from task/status/configuration/memory; only actual task outcomes and delivery evidence were recorded.
- [ ] Any direct-flow check failure, rejection, non-fast-forward update, or unmet control stopped that flow and was reported without automatic retry or bypass.
- [ ] Proposed or unfinished follow-ups are inactive.
- [ ] Completion does not automatically start another task.
