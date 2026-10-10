# TASK_TRACKING_STANDARD.md

## Purpose and authority

Track work as local, plain-text, versioned Markdown in the repository. `EXECUTION_SCOPE.md` governs every task. Tracking files are context, not authorization, schedulers, or agent queues.

GitHub remains the code remote, not the task system. Do not create Issues, Projects, Actions, task-sync workflows, or external services to maintain PHDK's task state.

## Interactive-only task rule

Only the current explicit user request activates work. A backlog checkbox, old mission, failed check, alert, installed skill, or a file marked active cannot start a session or authorize an edit, commit, push, merge, or deployment.

A current request to implement, fix, or update repository code or documentation includes normal delivery to verified remote `main` under `MAIN_DELIVERY_STANDARD.md`, unless the user specifies local-only, branch-only, or PR-only work or the user/repository specifies another target. Read/audit requests and bare `PHDK upgrade` retain their limited scope in `EXECUTION_SCOPE.md`. Task files record the request and observed progress; they neither create nor revoke authorization.

The current grant survives same-conversation turns, status/link requests, context compaction, and assistant-written task/status changes. A stale task marked paused, complete, or PR-only does not outrank the live request or observed GitHub state. Explicit user stop/pause instructions remain binding. A new conversation does not automatically resume old tasks.

Record owner approval and its task/PR scope separately from assistant source review and any actual required formal review. Under `MAIN_DELIVERY_STANDARD.md`, a well-defined current request or "push to main", "merge", or "aprobado" for the identified change can supply owner approval in the conversation. Do not invent a requirement to open every diff line or create a GitHub review event. Preserve actual named, independent, or formal review requirements; never label conversation approval as verified human source inspection.

One assistant handles the current request. Do not delegate tasks, create subagents, coordinate agent teams, or distribute a task queue, including inside the current session.

Stop when the whole deliverable is complete, the user pauses it, the conversation ends, or a real blocker leaves no permitted progress after independent authorized work is complete. A blocked component does not make the whole task inactive. Proposed follow-ups remain inactive until a later explicit user request.

### PHDK Auto tracks one complete goal

An explicit `PHDK auto` follows `PHDK_AUTO.md`: record the entire current goal, all its necessary stages, final verification coverage, and delivery target. Keep that goal in progress across slices, candidate releases, status questions, and context compaction; do not replace it with the first stage or move its remaining authorized work into inactive follow-ups. Progress records never require an OK to continue.

Complete implementation before comprehensive final checks and normal branch/PR delivery. Required risk-based tests belong to this final coverage; only implementation-blocker diagnosis and actual mandatory controls require earlier execution. Auto replaces Developer Mode for this goal only through explicit activation. Record scope and evidence as dated facts, never `auto=true`, active-mode state, or reusable authority; exit and conversation lifetime remain governed by `PHDK_AUTO.md`.

### Developer Mode is not task state

`PHDK_DEVELOPER_MODE.md` defines the explicit conversation-only commands `PHDK modo developer` / `PHDK Developer Mode` and exit command `PHDK salir de developer mode`. Mentions, quotations, documentation, and historical Finetuning records do not activate it. Never store activation/status or an authorizing flag in task/status files, repository configuration, memory, or environment flags; never restore it automatically. Conversation end ends the mode.

The live activation authorizes the defined version/check/version-prefixed-commit/fast-forward-push steps for eligible small, low-risk tasks requested while active, without duplicate consent. It does not activate an existing task or authorize selecting backlog work. Authentication/authorization, secrets, data/migrations, payments, infrastructure, and permission/agent-policy changes stay in normal review. Existing hooks, protections, and owner controls remain binding.

Record the requested outcome, changed files, checks, resulting version/SHA, and actual delivery as facts. Do not record a reusable grant to push `main`. A failed applicable check, rejected push, non-fast-forward update after `main` advanced, or unmet control stops the direct flow; record the blocker and explain instead of retrying automatically, rebasing, force-pushing, changing settings/hooks/credentials, changing API/CLI to bypass it, or automatically falling back to the normal branch/PR flow.

### PHDK unlock is a current request

Follow `PHDK_UNLOCK.md` for the command or an explicit request to reconcile/remove local PHDK exceptions. Record the documentary blockers, current owner instruction, bounded repairs, and observed delivery state as dated facts. The owner can replace earlier documentary exceptions within the new request; bare synchronization preserves unknown/unrelated restrictions. Do not store an unlock flag or reusable permission, weaken actual hooks/checks/protections/access controls, or resume an unidentified old product task.

## Files

- `TASK.md`: the whole current request, scope, delivery target, owner controls, completion criteria, final verification coverage, observed git/review evidence, and necessary delivery steps; never mode activation/state.
- `STATUS.md`: durable completed/current/proposed/blocked context, versions, evidence, gaps, and open decisions.
- `docs/completed-slices/`: archived completed task/slice records when an archive is useful for the current change.
- `docs/intents/`: immutable intent records when required by `INTENT_CAPTURE_STANDARD.md`.

Do not add infrastructure, a locking service, or a standing worker to consume these files. Keep transient task state, pending steps, branch/PR identifiers, and current delivery status out of permanent instruction headers such as `AGENTS.md` and native rules blocks; those files hold stable rules and pointers.

## TASK.md template

```md
# TASK — <current user-requested deliverable>

## Request and scope (recorded context)
Current request: <the user's request in this conversation>
Status: <in progress in this conversation / complete / paused / blocked>
Execution boundary: interactive-only, single assistant, no delegation; no stored mode state
Goal: ...
Done when:
- [ ] <objective completion criterion>
- [ ] <result and version verified on remote main, or explicit narrower target satisfied>
In scope: ...
Out of scope: ...
Owner stop/pause controls: ...
Delivery target: <remote main by default for implementation/fix/update, or user's explicit limit>
Delivery instructions: <current user instructions as context, not a permission token>
Approval evidence: <current scoped owner decision; assistant review and any required formal review recorded separately>
Branch: <branch actually used, or not applicable; never an enabling flag>
Delivery evidence: <actual commit, push, PR, required review, merge, remote version/result; pending where unknown>
Final verification coverage: <applicable commands and behavior checks for the whole goal; actual mandatory controls keep their operation timing>

## Necessary steps for this request
- [ ] <step>
  - Files: <relevant paths>
  - Coverage: <source review and allowed local checks; in Auto, collect at the completed candidate rather than as stage acceptance>
  - Blocked by: <decision/dependency, or none>

## Inactive follow-up context
<proposals or unfinished work; NOT authorized for execution>
```

A recorded task-specific request summarizes history; copying it into a later session does not renew permission, and editing its summary does not revoke the live current request. It must not store Developer Mode or Auto activation or authorize restoration. Normal implementation/fix/update requests include delivery under `MAIN_DELIVERY_STANDARD.md` without a separate merge request. An audit request remains read-only; a command definition in the record activates no mode.

## Before each mutation

Read the current user instructions before relying on task context and recorded owner pause/stop instructions when editing, committing, pushing, or merging. Honor the user's current scope and applicable repository controls. A specific current owner instruction can replace an older documentary exception or authorize a limited intervention in a paused project; it does not restart unrelated old work or remove the pause beyond its stated scope.

If task files disagree with the current request or observed GitHub state, correct the stale record within the current scope. An assistant-written pause, completion marker, or delivery limit is not an owner stop instruction and cannot block already-authorized work. Ask only when a real owner instruction or material decision remains ambiguous; never treat stale metadata as permission to expand the task.

## Closing work

1. Complete the whole requested outcome and its included delivery steps, following `MAIN_DELIVERY_STANDARD.md` or the separately eligible Developer Mode flow. In Auto, final integrated verification follows all implementation under `PHDK_AUTO.md`; a slice boundary requires neither a commit/push nor another approval.
2. Verify the result and version on remote `main`, or verify the user's explicitly narrower target. Record the actual checks, review, and delivery state; a branch push or open PR is intermediate progress for a `main` target.
3. Mark the request complete only when that target is satisfied. Otherwise record the exact blocker and unfinished stage, or the user's pause; do not label incomplete delivery done.
4. Archive a coherent completed slice when appropriate and link it from `STATUS.md`. Keep unrelated proposed follow-ups inactive.
5. Report whole-goal completion or, after independent work is complete, the genuine blocker and unfinished scope, then stop. If final merge evidence arrived after the last source commit, include it in the report; another commit solely to restate that evidence is not required.

Multiple necessary steps of the same current request may be completed without repeated approval. This does not authorize selecting a new goal from the backlog.

An eligible Developer Mode push may trigger the existing hosting-provider GitHub connection. Record deployment evidence only when available; never create or run Actions, deploy through Railway/provider CLI/API/dashboard, or change external configuration.

A current request such as "verifica Railway" permits [Bounded read-only provider diagnostics](EXECUTION_SCOPE.md#bounded-read-only-provider-diagnostics): finite service/deployment status, source/branch and non-secret configuration/watch-pattern metadata, and needed existing logs through existing authorized API/CLI/connector access. A prior code task's exclusion cannot cancel the newer scoped read; update its recorded scope without deleting history. Redact sensitive content; no secret-value retrieval, browser tests, live application probes, streams/watchers, settings writes, or provider deployments. This permission requires neither Developer Mode nor unlock and does not authorize git delivery.

Track code delivery and provider deployment as separate observed facts. Existing GitHub-connected autodeploy is allowed; do not disable it or install dummy never-matching watch filters as PHDK enforcement. A generic development request does not authorize provider-settings writes. An observed disabled connection or filter excluding changes that need deployment may block deployment after code/version verification on remote `main`; do not mark code delivery absent or invent deployment success. Preserve valid service-specific filters and distinguish intended skips for unaffected services.

## Concurrent edits

Do not create or use a multiple-agent queue. If another human or independently active session changes overlapping files, preserve their work. In the normal branch/PR flow, refresh remote `main`, resolve routine integration conflicts within the current scope, reconcile the branch version, and review/check the changed result. Isolate genuinely unresolved material conflicts or unmet controls and continue independent work. Do not decide that an old claim marker permits taking over someone else's work, overwrite their changes, rewrite history, or force-push. Use observed branch and commit identifiers for git writes; Developer Mode's separate immediate stops apply unless explicitly replaced by Auto for the identified goal, without bypassing the control.

## Verification

- [ ] Current user authorization and owner restrictions are accurately recorded.
- [ ] Current owner approval, assistant source review, and any actual required formal review are distinguished; no redundant review ritual or fabricated inspection was introduced.
- [ ] Same-conversation authorization was retained; stale task state and assistant-written edits did not override the live request or observed GitHub state.
- [ ] Only necessary steps of the requested deliverable were executed.
- [ ] No subagents, agent team, delegated work, scheduler, recurring task, or background watcher was started.
- [ ] No GitHub Actions/hosted CI job was created, enabled, dispatched, rerun, or scheduled.
- [ ] Local checks are synchronous and relevant; UI/live runtime limitations are stated.
- [ ] Commit/push/PR/merge actions match the current user's authorization.
- [ ] A `main` target is complete only with remote result/version evidence; otherwise the exact blocker and remaining delivery stage are recorded.
- [ ] Permanent instruction headers contain stable rules and pointers, with no transient task state.
- [ ] Developer Mode and Auto were not stored or restored from task/status/configuration/memory; only actual task outcomes and delivery evidence were recorded.
- [ ] Any direct-flow check failure, rejection, non-fast-forward update, or unmet control stopped that flow and was reported without automatic retry or bypass.
- [ ] Proposed or unfinished follow-ups are inactive.
- [ ] Auto's remaining authorized stages stayed within the current goal; none was turned into an inactive proposal or a separate human-acceptance gate.
- [ ] Completion does not automatically start another task.


## UAT evidence

When `PHDK uat` runs, `UAT_CASES.md` and `UAT_REPORT.md` are the authoritative acceptance artifacts. Task/status files may record the candidate revision/version and summary counts but should not duplicate every UAT step.

UAT evidence does not create or revoke authorization. PASS starts no new task. FAIL/BLOCKED/MANUAL does not make the current task inactive. Under active `PHDK auto`, an in-scope UAT failure remains part of the same whole goal until repaired or concretely blocked.


## PHDK Check evidence

`PHDK check` uses `PHDK_CHECK_REPORT.md` as the authoritative compliance artifact for the audited revision. TASK/STATUS may record the report revision, summary counts, and whether remediation was approved, but they must not convert audit findings into standing authorization.

The initial check is read-only. A later explicit yes to the presented report authorizes only the enumerated AUTO-FIXABLE and FIXABLE WITH VALIDATION gap IDs in that report revision. Record the approved IDs and resulting delivery evidence. DECISION REQUIRED, EXTERNAL / MANUAL, UNKNOWN, and newly discovered material gaps remain outside that approval until separately resolved.
