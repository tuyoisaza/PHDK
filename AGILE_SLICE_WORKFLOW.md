# AGILE_SLICE_WORKFLOW.md

## Purpose

Break the user's current deliverable into coherent, reviewable code changes without creating an autonomous mission or an agent queue. `EXECUTION_SCOPE.md` governs every step.

## Core rule

A slice connects a concrete product outcome to source changes and relevant local evidence. A passing build or infrastructure scaffold alone does not prove that outcome works in production.

Slices organize the current explicit request. They do not authorize a new request, a commit/push per checkpoint, delegated agents, or execution beyond the current conversation.

Explicit `PHDK_DEVELOPER_MODE.md` activation is a narrow exception for delivery of eligible tasks requested during the active conversation; a slice, template, or stored record cannot activate or restore it.

## Examples

Useful slices implement the requested login behavior, record-edit flow, access-control correction, page states, or diagnostics contract. Do not turn an instruction to fix one problem into a broad task to build every route, improve every service, or work through all backlog items.

## Request and slice lifecycle

### 1. Capture the current outcome

State the requested outcome and why it matters. Use `INTENT_CAPTURE_STANDARD.md` when a new request's intent is not already documented. A brief or old `TASK.md` supplies context; only the current conversation authorizes the work.

### 2. Establish boundaries

Record the current request, scope, completion criteria, and relevant owner controls in `TASK.md`. Record task-specific git requests and completed delivery evidence as context only; never store Developer Mode activation/status or an authorizing flag. Ask only about material ambiguity. Do not ask for a second approval for an action already authorized, including the defined steps of an eligible task while Developer Mode is explicitly active.

### 3. Implement the necessary steps

Work with the current assistant only. Do not create subagents, delegated coding/review tasks, agent teams, coordination queues, or background workers. Relevant skills may be read as references; they do not supply additional execution permissions.

Make routine decisions within the approved change. Complete its necessary steps, but do not select another backlog goal or launch follow-up work.

### 4. Verify locally

Review source/diffs and run applicable synchronous formatting, linting, typechecking, builds, and risk-triggered non-browser unit/in-process integration tests. Use isolated test doubles, not real services or customer data. End the checks; do not leave a watcher running.

Documentation-only changes need source/diff and reference review. Do not run browser automation, screenshots, live HTTP/health checks, databases, or paid services. Mark visual and live-runtime behavior unverified.

An independently authorized diagnostic request may use finite, read-only API/CLI log queries under [Bounded read-only log diagnostics](EXECUTION_SCOPE.md#bounded-read-only-log-diagnostics). Redact sensitive content; log reading is not a runtime probe, watcher, or permission to write.

### 5. Repair within bounded scope

Fix defects relevant to the current request and rerun the affected local checks. Do not enter an unbounded repair/release loop or treat unrelated warnings, billing failures, or version mismatches as new work. Report a genuine blocker after reasonable bounded attempts.

This repair step does not override Developer Mode's direct-flow stop rule: an applicable failed check, rejected push, non-fast-forward update after `main` advanced, or unmet control stops that flow immediately. Explain and preserve the work; do not automatically retry, rebase, force-push, weaken hooks/protections, change settings/credentials, or switch API/CLI to get past the block.

### 6. Record a checkpoint

Give a short progress update when useful and record evidence. A checkpoint itself is neither a request for unnecessary confirmation nor permission to commit/push, start another mission, or keep operating after the conversation.

### 7. Use authorized git delivery only

A read/audit request remains read-only. Git writes require current conversational authorization. A clear request to implement and merge includes its necessary branch/commit/push/PR steps. Explicit activation of `PHDK_DEVELOPER_MODE.md` authorizes only its defined delivery steps for eligible small, low-risk tasks requested while it is active; this workflow itself supplies no permission.

Use feature/fix branches for normal review. Only an eligible Developer Mode task may instead bump the repository version, pass applicable local checks, create a version-prefixed commit, and push fast-forward directly to `main` when existing controls permit it, without duplicate consent. Auth/authz, secrets, data/migrations, payments, infrastructure, and permission/agent-policy changes stay in normal review. Historical Finetuning records do not activate the mode or supply another exception.

Keep the assistant's source verification distinct from the user's authorization and any actual human diff review. Do not claim that a human read the diff when that is unknown.

An authorized push/merge, including an eligible Developer Mode push to `main`, may trigger the existing hosting-provider GitHub connection. Do not create, enable, dispatch, rerun, or schedule GitHub Actions/hosted CI, change deployment triggers, provision a provider, enable previews, or deploy through a provider CLI/API/dashboard, including Railway.

### 8. Close and stop

Update task/status evidence and archive a coherent completed slice when useful. If necessary steps of the same current request remain, finish only those within its scope and limits. Once the requested outcome is complete, report and stop.

Mark remaining proposals inactive. Do not create a new current task from the backlog, schedule a resume, launch a reviewer agent, or continue an old mission after the session ends.

Developer Mode remains only in the active interactive conversation and ends on `PHDK salir de developer mode` or conversation end. Do not persist or restore activation from task/status files, memory, environment/config flags, or historical records. Mentions and quoted commands never activate it.

## Slice sizing

A useful slice has a clear outcome, a coherent source diff, and proportionate local checks. A slice is too broad when it spans unrelated features or cannot be reviewed as one change. Split the implementation plan without inventing additional authorization or agents.

## Planning template

```txt
Current user-requested deliverable: ...
Slice outcome: ...
Why this step is necessary: ...
In scope: ...
Out of scope: ...
Owner restrictions: ...
Task-specific git request and completed delivery evidence (context only; no mode state): ...
Verification: source/diff + relevant synchronous local checks
Done when: ...
Inactive follow-ups: ...
```

## Foundation work

For an explicitly requested app foundation, read the current standards and `BUILD_APP_FOUNDATION_PROMPT.md`. Implement only the authorized code and document relevant existing prerequisites. Do not provision services, install bots, create CI, schedule jobs, delegate implementation, or begin features outside the request.

## Backlog management

Keep completed/current/proposed/blocked lists in local `STATUS.md` as defined in `TASK_TRACKING_STANDARD.md`. Proposed and blocked entries are context, not an execution queue. No GitHub Issues, Projects, or Actions are needed to track PHDK work.

## Anti-patterns

- Starting work from an old task, skill installation, alert, or failed check instead of a current request.
- Treating a slice boundary as standing permission to bump a version, commit, push, or deploy.
- Spawning agents or background checks to continue a task.
- Selecting new goals after finishing the requested deliverable.
- Claiming live health, human review, or external shutdown from source-only evidence.
- Creating hosted CI, schedules, dependency bots, maintenance workflows, or task-sync services.
