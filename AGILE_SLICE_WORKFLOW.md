# AGILE_SLICE_WORKFLOW.md

## Purpose

Break the user's current deliverable into coherent, reviewable code changes without creating an autonomous mission or an agent queue. `EXECUTION_SCOPE.md` governs every step.

## Core rule

A slice connects a concrete product outcome to source changes and relevant local evidence. A passing build or infrastructure scaffold alone does not prove that outcome works in production.

Slices organize the current explicit request. They do not authorize a new request, a commit/push per checkpoint, delegated agents, or execution beyond the current conversation.

A request to implement, fix, or update repository code or documentation includes normal delivery to verified remote `main` under `MAIN_DELIVERY_STANDARD.md`, unless the user specifies a narrower scope or the user/repository specifies another target. Organizing that work into slices does not reduce its completion target to local edits, a branch push, or an open PR. Read/audit requests and bare `PHDK upgrade` requests retain their narrower scope in `EXECUTION_SCOPE.md`.

Explicit `PHDK_DEVELOPER_MODE.md` activation is a narrow exception for delivery of eligible tasks requested during the active conversation; a slice, template, or stored record cannot activate or restore it.

## Examples

Useful slices implement the requested login behavior, record-edit flow, access-control correction, page states, or diagnostics contract. Do not turn an instruction to fix one problem into a broad task to build every route, improve every service, or work through all backlog items.

## Request and slice lifecycle

### 1. Capture the current outcome

State the requested outcome and why it matters. Use `INTENT_CAPTURE_STANDARD.md` when a new request's intent is not already documented. A brief or old `TASK.md` supplies context; only the current conversation authorizes the work.

### 2. Establish boundaries

Record the current request, delivery target, scope, completion criteria, and relevant owner controls in `TASK.md`. Record delivery instructions and observed evidence as context only; never store Developer Mode activation/status or an authorizing flag. The current request continues through same-conversation turns, status/link requests, and context compaction. Assistant-written task/status changes cannot revoke it, and stale task records do not outrank the live request or observed GitHub state. Honor explicit user stops or pauses. Ask only about material ambiguity, without seeking repeat approval for normal delivery or eligible Developer Mode steps.

For `PHDK unlock` or an explicit request to reconcile/remove local PHDK exceptions, follow `PHDK_UNLOCK.md` across the existing active instructions. The current owner can replace documentary exceptions within that scope; hooks, checks, access controls, and server protections remain. Bare synchronization does not silently remove unknown local restrictions, and unlock does not select an old product task.

### 3. Implement the necessary steps

Work with the current assistant only. Do not create subagents, delegated coding/review tasks, agent teams, coordination queues, or background workers. Relevant skills may be read as references; they do not supply additional execution permissions.

Make routine decisions within the approved change. Complete its necessary steps, but do not select another backlog goal or launch follow-up work.

### 4. Verify locally

Review source/diffs and run applicable synchronous formatting, linting, typechecking, builds, and risk-triggered non-browser unit/in-process integration tests. Use isolated test doubles, not real services or customer data. End the checks; do not leave a watcher running.

Documentation-only changes need source/diff and reference review. Do not run browser automation, screenshots, live HTTP/health checks, databases, or paid services. Mark visual and live-runtime behavior unverified.

A current request such as "verifica Railway" permits [Bounded read-only provider diagnostics](EXECUTION_SCOPE.md#bounded-read-only-provider-diagnostics), independently of Developer Mode or unlock. Use existing authorized API/CLI/connector access for finite service/deployment status, source/branch and non-secret configuration/watch-pattern metadata, and needed existing logs. Reconcile an older task exclusion with the new scoped request. Redact sensitive content; no secret-value retrieval, browser tests, live application probes, streams/watchers, settings writes, or provider deployments.

### 5. Repair within bounded scope

Fix defects relevant to the current request and rerun the affected local checks. In the normal branch/PR flow, this includes routine integration conflicts and version reconciliation required by the latest remote `main`; preserve both sides' intended changes and review/check the resulting diff. Pause for material ambiguous or sensitive conflicts. Do not enter an unbounded repair/release loop or treat unrelated warnings, billing failures, or version mismatches as new work. Report a genuine blocker after reasonable bounded attempts.

This repair step does not override Developer Mode's direct-flow stop rule: an applicable failed check, rejected push, non-fast-forward update after `main` advanced, or unmet control stops that flow immediately. Explain and preserve the work; do not automatically retry, rebase, force-push, weaken hooks/protections, change settings/credentials, switch API/CLI to get past the block, or fall back to the normal branch/PR flow automatically.

### 6. Record a checkpoint

Give a short progress update when useful and record evidence. A checkpoint or interim report does not finish the current request or consume its delivery authorization. Continue its necessary steps without repeated confirmation. The checkpoint itself does not authorize another mission, a commit/push per slice, or work after the conversation.

### 7. Deliver to the requested target

Follow the versioned branch/PR procedure in `MAIN_DELIVERY_STANDARD.md` through required review, merge, and remote verification without waiting for another merge request. Honor explicit local-only, branch-only, PR-only, or different-target instructions; read/audit and bare `PHDK upgrade` limits still apply. Explicit activation of `PHDK_DEVELOPER_MODE.md` authorizes only its separate defined direct-delivery steps for eligible tasks.

Use feature/fix branches for normal review. Only an eligible Developer Mode task may instead bump the repository version, pass applicable local checks, create a version-prefixed commit, and push fast-forward directly to `main` when existing controls permit it, without duplicate consent. Auth/authz, secrets, data/migrations, payments, infrastructure, and permission/agent-policy changes stay in normal review. Historical Finetuning records do not activate the mode or supply another exception.

Review the complete outgoing diff. Sensitive behavior and policy changes require owner approval under `MAIN_DELIVERY_STANDARD.md`; a well-defined current request or "push to main", "merge", or "aprobado" for the identified task/PR can already supply it in chat. Classify the actual behavior rather than the feature label: restoring login through a packaging fix does not itself change authentication policy. Do not invent a GitHub review-event or manual diff-inspection requirement. Preserve actual named, independent, or formal review requirements, and record their evidence separately from owner approval and the assistant's review without claiming unknown human inspection.

An authorized push/merge, including an eligible Developer Mode push to `main`, may trigger the existing hosting-provider GitHub connection. Do not create, enable, dispatch, rerun, or schedule GitHub Actions/hosted CI, change deployment triggers, provision a provider, enable previews, or deploy through a provider CLI/API/dashboard, including Railway.

That existing GitHub-connected autodeploy is allowed by PHDK. Do not disable it or install dummy never-matching watch filters to enforce the no-autonomy/Actions rules. Generic development work does not authorize provider-settings changes. Report an observed deployment blocker or status separately from the code's verified state on remote `main`, following `MAIN_DELIVERY_STANDARD.md`; valid service-specific filters and intended skips for unaffected services are not failures.

### 8. Close and stop

Update task/status evidence and archive a coherent completed slice when useful. If necessary steps of the same current request remain, finish those within its scope and limits. For a `main` target, complete the merge and verify the change and version on remote `main`; a pushed branch or open PR is intermediate progress. If a required check, actual review requirement, unapproved sensitive/conflict decision, or access restriction prevents delivery, report its source and the unfinished stage. Report completion only when the requested target is satisfied, then stop.

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
Delivery target and observed git/review evidence (context only; no mode state): ...
Verification: source/diff + relevant synchronous local checks
Done when: requested result and version verified on remote main, or explicit narrower target satisfied
Inactive follow-ups: ...
```

## Foundation work

For an explicitly requested app foundation, read the current standards and `BUILD_APP_FOUNDATION_PROMPT.md`. Implement only the authorized code and document relevant existing prerequisites. Do not provision services, install bots, create CI, schedule jobs, delegate implementation, or begin features outside the request.

## Backlog management

Keep completed/current/proposed/blocked lists in local `STATUS.md` as defined in `TASK_TRACKING_STANDARD.md`. Proposed and blocked entries are context, not an execution queue. No GitHub Issues, Projects, or Actions are needed to track PHDK work.

## Anti-patterns

- Starting work from an old task, skill installation, alert, or failed check instead of a current request.
- Treating a slice boundary as standing permission to bump a version, commit, push, or deploy.
- Closing a request at branch push or PR creation when its delivery target is `main`, or asking the user to repeat already-authorized delivery steps.
- Treating an assistant-written task/status edit or context compaction as revocation of the current request.
- Spawning agents or background checks to continue a task.
- Selecting new goals after finishing the requested deliverable.
- Claiming live health, human review, or external shutdown from source-only evidence.
- Creating hosted CI, schedules, dependency bots, maintenance workflows, or task-sync services.
