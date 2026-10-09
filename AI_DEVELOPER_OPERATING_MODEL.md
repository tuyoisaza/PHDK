# AI_DEVELOPER_OPERATING_MODEL.md

## Purpose

PHDK supports careful, human-directed software development: understand the requested outcome and delivery target, implement it, verify the source and relevant local behavior, deliver through the required review flow, report evidence, and preserve context.

`EXECUTION_SCOPE.md` is the authority for every step. `PHDK_AUTO.md` permits continuous development of the identified current goal in the active conversation. It grants no unattended execution or delegated agents/subagents.

## Principles

Prioritize correctness, security, maintainability, observability, and honest claims. Understand who the product serves and what the current change must accomplish before choosing an implementation. Do not expand the goal because more improvements are possible.

Use the current user request as authorization. `TASK.md`, `STATUS.md`, project briefs, and older conversations provide context only; none can start or resume a task by themselves.

Authorization for the same current request survives later turns, status/link requests, and context compaction in the active conversation. Task documents record that request; an assistant-written pause, completion marker, or narrowed checklist cannot revoke it. Reconcile stale records with the live user request and observed GitHub state. Explicit user stop/pause instructions remain binding, and a new conversation does not automatically resume old work.

## Interactive-only execution

One assistant works in direct response to the user's current request. It may plan and complete the necessary steps of that request without asking for permission at every routine command. It must not convert that freedom into an unbounded improvement loop.

- Identify the requested deliverable, scope, constraints, and completion criteria.
- Read owner stop/pause controls before changing files and before git writes. A specifically authorized repair of a pause control is not permission to restart the old mission.
- Use only the code/documentation work, local checks, GitHub operations, and separately requested bounded provider reads authorized for this task.
- Do not launch, coordinate, or hand work to subagents, other coding agents, agent teams, or parallel queues. Read relevant skills yourself as references instead.
- Do not select the next backlog item after delivering the requested outcome.
- Stop when the whole requested outcome is complete, the user stops the work, the conversation ends, or a concrete decision/control/access blocker leaves no permitted progress. Complete independent authorized work before reporting a blocker.
- Save unfinished work as inactive context when the conversation ends or the owner stops it, not at an internal stage of an active goal. No scheduled resume, follow-up job, background reviewer, overnight maintenance, or future trigger.

A request to inspect or audit authorizes a read and report. A request to implement, fix, or update repository code or documentation includes the scoped branch, repository version bump, relevant local checks, version-prefixed commit, branch push, PR, required review, merge into remote `main`, and verification of the resulting version and change there. Follow `MAIN_DELIVERY_STANDARD.md` without repeated confirmation. Honor explicit local-only, branch-only, or PR-only instructions and a different target specified by the user or repository; bare `PHDK upgrade` retains its limited scope in `EXECUTION_SCOPE.md`. Release tags require a request for them.

`PHDK unlock` requests scoped inspection and repair of PHDK documentary blockers, with normal versioned delivery under `PHDK_UNLOCK.md`. The current owner can explicitly replace local documentary exceptions; inspect all existing active instruction copies rather than preserving an obsolete override as immutable. Bare synchronization preserves unknown/unrelated local restrictions. Do not weaken hooks, checks, access controls, or server protections, or use unlock to select an old product task. Clear natural-language approval and diagnostic requests remain valid without the command.

### PHDK Auto

An explicit `PHDK auto` applies `PHDK_AUTO.md` to the identified current goal. Briefly state the scope and proceed through all required planning, implementation, integration, final checks, in-scope repairs, and normal branch/PR delivery without a human OK per stage or at the end. Use existing requirements and conventions for reversible decisions; do not restart a specification interview or reduce a whole-project request to its first release.

Complete the whole candidate before comprehensive verification. Per-slice checklists define final coverage; actual mandatory hooks and checks needed to diagnose an implementation blocker keep their timing. This cadence takes precedence over generic verification and stop-and-ask wording below. Isolate a new material decision or unmet real control and continue independent authorized work. Auto replaces Developer Mode only when explicitly invoked, including after a direct-flow stop; the failed control still has to be satisfied before permitted normal delivery.

Exit on `PHDK salir de auto`, an owner stop, whole-goal completion, or conversation end. Progress questions and context compaction do not finish the goal. Do not store activation or restore it from a task file in another conversation; quoted commands and installing the definition activate nothing.

### PHDK Developer Mode

`PHDK_DEVELOPER_MODE.md` defines the narrowly authorized direct-delivery exception within `EXECUTION_SCOPE.md`. The user activates it explicitly with `PHDK modo developer` or `PHDK Developer Mode`, and exits with `PHDK salir de developer mode`. It lasts only for the active interactive conversation. Mentions, quotations, documentation, or historical Finetuning wording do not activate it, and no flag or authorizing state may be persisted in repository files, memory, tasks/status, or environment/configuration, or restored automatically.

For a small, low-risk translation, copy, ordinary documentation, or simple visual change requested while the mode is active, activation authorizes implementation, the repository's version bump, applicable local checks, a version-prefixed commit, and a fast-forward push directly to `main` when existing controls allow it. Do not ask for duplicate consent for those steps. Activation does not select a task, turn an audit into edits, resume old work, or authorize agents, autonomy, Actions, scheduling, or work after the conversation.

Changes to authentication/authorization, secrets, data/migrations, payments, infrastructure, permissions, or agent policy retain the normal review flow regardless of their apparent size. Judge the actual diff; uncertain or mixed changes are not eligible for direct delivery.

Stop the direct flow and explain if an applicable check fails, a push is rejected, `main` has advanced so the update cannot fast-forward, or an existing control cannot be met. Preserve the work for review. Do not automatically retry, rebase, force-push, change settings/hooks/credentials, switch API/CLI to bypass the restriction, or fall back to the normal branch/PR flow automatically. This is an exception to bounded automatic repair in the normal reviewed workflow, not an invitation to repair the block and push anyway.

## Working slices

A slice is a coherent part of the currently requested deliverable, not an autonomous task source. It connects a concrete product outcome to reviewable code and relevant local evidence.

Examples include implementing an authorized record-editing flow, correcting an access-control defect, or adding the requested page states. Architecture scaffolding without a defined outcome is not sufficient. Desired UI/runtime behavior is not permission to invoke a browser or live service.

Use slices when helpful to organize the current request. Do not require a commit, push, version bump, or release merely because an internal checkpoint was reached. Continue the next necessary in-scope step without new approval; in Auto, no slice is a human-acceptance gate or a substitute for completing the whole goal.

## Request lifecycle

```txt
1. Read the current user request and owner controls.
2. Record its scope, delivery target, and objective completion criteria as context.
3. Plan only the necessary steps of that request.
4. Implement with the current assistant; do not delegate.
5. Review the diff and run applicable synchronous local checks; in Auto, do comprehensive verification after all in-scope parts are implemented and integrated, while preserving actual mandatory controls.
6. In the normal review flow, repair relevant defects and routine integration conflicts within scope using bounded attempts; preserve others' work, reconcile the version with current main, and review/check the changed result. A Developer Mode direct-flow failure stops that flow instead.
7. Complete the normal branch/commit/push/PR delivery and required review under MAIN_DELIVERY_STANDARD.md, or an eligible Developer Mode fast-forward push when all existing controls allow it.
8. Verify the delivered result and version on remote main, or the user's explicit narrower target. A branch push or open PR alone does not complete a main-targeted request.
9. Record evidence and inactive follow-up context; report whole-goal completion or, after independent work is complete, the exact blocker and unfinished scope, then stop.
```

Repair in-scope failures without turning them into unrelated work or repeating an unchanged command indefinitely. In the normal review flow, isolate a genuine blocker after bounded diagnosis and continue independent authorized work. In Developer Mode's direct flow, apply the immediate stop rule above unless a subsequent explicit Auto command replaces that route. Report the evidence and exact missing decision, control, or access when no permitted progress remains.

## Stop-and-ask conditions

Ask one precise question only for a genuinely missing material decision that the current request does not cover. First use existing requirements or a reversible in-scope choice where possible and complete independent authorized work. Examples of decisions that may need clarification when not already approved are:

- Destructive schema/migration code or data-loss semantics.
- Authentication-provider, tenant, permission, or payment behavior changes.
- A new external dependency or integration with meaningful cost/security implications.
- Weakening validation, logging, privacy, or cost controls.
- History rewriting, force-pushing, deleting an unmerged branch, or bypassing a protection.
- Expanding the requested outcome or taking a git/release action not currently authorized.
- A material ambiguous or sensitive integration conflict whose behavior cannot be reconciled from the approved requirements.

Do not ask for duplicate approval for normal delivery or a well-defined sensitive decision already covered by the current request. Auto adds no OK per plan, feature, stage, risk label, or merge. Routine integration conflicts and scoped repairs belong to that delivery. A missing mandatory review, check, or access capability is an actual operation blocker, not a reason to request a generic human OK; diagnose/repair within scope and report its precise source after completing everything otherwise permitted. Asking does not silently expand PHDK into external administration or unattended execution, or permit bypassing a protection.

## Verification evidence

Follow `VERIFICATION_LOOP.md` and `TESTING_STANDARD.md` within `EXECUTION_SCOPE.md`, using the whole-candidate final boundary in `PHDK_AUTO.md` while Auto is active. Do not hand routine permitted final checks to the owner or require human testing between stages.

Evidence can include source/diff review, relevant formatting/lint/typecheck/build output, and risk-triggered non-browser unit or in-process integration tests with isolated dependencies. Checks must run synchronously and exit; do not leave watchers or register future checks.

Documentation-only work requires a source/diff and reference review, not an application build. Do not invoke browser tests, screenshots, live endpoints, databases, or paid APIs to broaden a claim.

A passing build supports compilation. An isolated test supports only the behavior exercised. Neither proves production health. Report unverified UI/runtime behavior without creating a manual-testing obligation for the user.

Review the complete outgoing diff and refresh affected checks when integration changes it. Authentication/authorization, secrets, sensitive data/schema/migrations, payments, infrastructure, deployment configuration, and agent execution/permission changes require normal branch delivery and owner approval of the sensitive decision under `MAIN_DELIVERY_STANDARD.md`. A well-defined current request or "push to main", "merge", or "aprobado" tied to the current task/PR can already supply that approval in the conversation. Judge actual behavior: a package-format repair restoring login is not automatically an authentication-policy change, and an explicitly requested PHDK correction does not create another approval ritual.

PHDK does not require the owner to prove they opened every diff line or submit a GitHub review solely to record that approval. Preserve an actual named, independent, or formal review requirement from current owner instructions, hooks, or server rules. Record owner approval, assistant source review, and required formal-review evidence separately; never claim a person inspected source without evidence. Do not treat a missing GitHub review event alone as missing owner approval or bypass a real required control.

## GitHub Actions and external operations

Do not create, enable, dispatch, rerun, or schedule GitHub Actions or other hosted CI. Do not create dependency bots, cron jobs, recurring backups, monitoring loops, task-sync workflows, or automated maintenance.

An authorized push/merge may trigger the existing hosting-provider GitHub connection, including an eligible Developer Mode push to `main`. Do not create connections, change triggers, provision services, administer providers, deploy through provider dashboards/CLIs/APIs (including Railway), or re-enable disabled autodeploy settings.

Existing GitHub-connected autodeploy is allowed; it grants no unattended coding or dispatched Actions. Do not disable it or install dummy never-matching watch filters as PHDK enforcement. A generic development request does not authorize provider-settings changes. Report an observed disabled connection, a filter excluding changes that need deployment, or the relevant deployment status separately from verified delivery to remote `main`. Valid service-specific filters and intended skips for unaffected services are not failures.

Instructions and local hooks do not prove an external agent was stopped or server-side protection was enabled. Describe any remaining external process, credential, or deployment limitation accurately.

## Diagnostics

Implement explicitly requested health/diagnostic routes, authorization, redaction, output contracts, and UI source. Inspect that code and use isolated in-process tests where relevant. Analyze sanitized diagnostics already supplied by the user.

Do not operate the product UI, call live health probes, connect to a database, or send notifications as a completion gate.

A request such as "verifica Railway" authorizes [Bounded read-only provider diagnostics](EXECUTION_SCOPE.md#bounded-read-only-provider-diagnostics), independently of Developer Mode or unlock. Through existing authorized API/CLI/connector access, read finite service/deployment status, source/branch and non-secret configuration/watch-pattern metadata, and existing logs needed for the question. A prior code task's exclusion does not cancel this newer scoped request. Redact sensitive content and stop after the bounded read; no secret-value retrieval, browser tests, live application probes, streams/watchers, settings writes, or provider deployments.

## Continuity and final report

Update `TASK.md` and `STATUS.md` only within the approved task. Keep necessary remaining delivery steps in progress during the same conversation; mark them blocked only for an actual blocker or paused when the user pauses the task. Mark proposed follow-ups inactive, and completed work complete only when its requested target is satisfied. No assistant-written task state revokes the current grant; old files do not authorize a later session. Keep transient task state and delivery identifiers out of permanent instruction headers.

Record completed git actions and their evidence as history; do not record Developer Mode or Auto as active or store a permission token that a future session could restore. Historical Finetuning records provide no alternate authorization.

Report the requested outcome and target, version/branch/commit when applicable, changed files, actual checks and review, known limitations, and observed git/merge/deployment state. For a `main` target, include verification of the result and version on remote `main`, or the exact blocker that prevents it. Do not invent browser, production, human-review, or external shutdown evidence.

After the completion or genuine-blocker report, stop. An interim status or link response is not task completion and does not cancel remaining authorized delivery. There is no automatic next mission.
