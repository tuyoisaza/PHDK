# PHDK Auto

## Command and lifetime

Run `PHDK_PREFLIGHT.md` once at Auto entry, then re-check only newly relevant capabilities when later lifecycle stages need them. Auto also follows the stage input/output/handoff contracts in `PHDK_LIFECYCLE.md`. Do not repeat a noisy full preflight at every internal stage.

`PHDK auto` explicitly starts the complete PHDK delivery lifecycle for the identified current goal. Match case-insensitively after trimming whitespace; an accompanying brief, task, project goal, or coherent Capture baseline supplies the scope. If the current conversation already identifies that goal, start without another confirmation or a mandatory interview. If there is no single current delivery but the repository already exposes multiple parallel pillars/fronts through Capture, Plan, PMO artifacts, requirements, or current work, do not collapse them into a request for one arbitrary goal; enter PMO portfolio discovery instead. A request to add this command, quoted examples, installed files, and old task records do not activate it.

Before substantive execution, explain the lifecycle visibly to the user.

At Auto start, create/initialize the current lifecycle run defined by `PHDK_LIFECYCLE.md`: assign a run ID, create/update root `PHDK_LIFECYCLE_STATUS.md`, and identify the historical run folder.

The opening Auto message must include:
- the identified goal or detected portfolio;
- the complete applicable lifecycle;
- the current status of every stage;
- which stages are being reused from existing artifacts;
- which stage is starting now;
- any genuine blocker/decision that could interrupt the lifecycle.

Use these stage statuses:

- **PENDING** — not started yet.
- **RUNNING** — current stage.
- **REUSED** — existing artifacts/evidence are current and will be reused.
- **COMPLETED** — executed in this Auto run.
- **BLOCKED** — cannot proceed for a concrete reason.
- **NOT APPLICABLE** — genuinely irrelevant to this goal.

Present a compact lifecycle board such as:

```text
PHDK Auto — lifecycle
Goal: <goal / confirmed portfolio>

Preflight ............ COMPLETED
Capture .............. REUSED
Plan ................. RUNNING
PMO / Workstreams .... PENDING
Integration Review ... PENDING
UAT .................. PENDING
UAT Fix .............. PENDING
Check ................ PENDING
Remediation .......... PENDING
Delivery ............. PENDING

Current stage: Plan
Next: PMO / Workstreams
```

Do not replace this with only a prose summary of permissions such as "puedo revisar, probar, versionar y entregar." The owner must be able to see where Auto is in the PHDK lifecycle.

Then run the applicable lifecycle end-to-end:

```text
Capture → Plan → PMO/workstream execution → PMO Integration Review
→ UAT → UAT Fix → Check → in-scope Check remediation → delivery
```

Skip a stage only when its output is already current/coherent or it is genuinely not applicable. Do not rerun Capture or Plan merely for ceremony.

## Lifecycle communication contract

Before Auto enters a new stage, validate that stage's required upstream handoff/artifacts from `PHDK_LIFECYCLE.md`. If they are missing or stale, do not silently skip the contract: either repair/reopen the upstream stage or mark the transition BLOCKED with the exact missing deliverable.

Whenever Auto transitions to another lifecycle stage, first finalize the outgoing stage `HANDOFF.md` and snapshots, then send a concise progress update that states:

1. **Completed/reused stage** — what just closed and what that stage was responsible for.
2. **Delivered artifacts** — canonical paths and historical snapshot folder.
3. **Exit gate** — what conditions passed.
4. **Current stage** — what Auto is doing now.
5. **Entry validation** — what upstream artifacts the current stage verified.
6. **Next stage** — what follows and what it will require.
7. **Blockers** — only genuine blockers/decisions, with the exact affected stage.

Examples:

```text
Capture — REUSED
Evidence: PROJECT_INTENT.md + PRD.md + REQUIREMENTS_TRACEABILITY.md are coherent.

Plan — RUNNING
I am reconstructing the current architecture and updating the target/convergence plan.

Next: PMO / Workstreams.
```

```text
Plan — COMPLETED

Delivered:
- SOLUTION_ARCHITECTURE.md
- REPOSITORY_ARCHITECTURE.md
- UX_ARCHITECTURE.md
- IMPLEMENTATION_PLAN.md
Historical: docs/phdk/lifecycle/<run-id>/20-plan/

Exit gate:
- P0 requirements mapped
- boundaries/dependencies explicit
- workstream decomposition executable

PMO / Workstreams — RUNNING
Entry validated: Plan handoff + IMPLEMENTATION_PLAN.md + architecture ownership/dependencies.

Next: Integration Review
It will require completed workstream evidence + PMO ownership/dependency artifacts.
```

```text
UAT — COMPLETED: ACCEPTANCE INCOMPLETE
UAT Fix — RUNNING
I am repairing 1 local blocker and preparing explicit actions for 1 manual case.

Next: Check.
```

Progress updates are informational, not approval gates. Continue automatically unless a real decision/control blocks the affected stage.

Do not narrate every command/file operation. Communicate lifecycle movement and material evidence.

At any user status question such as "¿qué estás haciendo?", "status", or "dónde vas", answer with the current lifecycle board/stage first, then relevant execution detail.

Send concise progress updates without turning them into approval questions or ending the task at a milestone.

The mode lasts for this goal in the active conversation. Exit on `PHDK salir de auto`, a clear owner stop, completion of the whole requested outcome, or the conversation ending. A status/link question, context compaction, or assistant-written checkpoint does not end an unfinished goal. Keep task evidence across turns, but never save a reusable `auto=true` authority flag or resume from files alone in another conversation. This is an instruction to the assistant, not a daemon, scheduler, or shell executable.

## Full lifecycle, one authorization

Auto's identified goal is the authorization boundary for the whole lifecycle.

### 1. Capture

If the professional requirements baseline is missing/incoherent, run Capture semantics first. Ask only genuinely material missing requirements questions. If the baseline is already coherent and current, reuse it.

### 2. Plan

Run `PHDK plan` semantics against the captured requirements. For greenfield, define the target solution/repository/UX architecture and implementation plan. For brownfield, reconstruct current architecture first, preserve valid decisions, define target state, and create an incremental convergence plan.

Ask only for architecture decisions that materially change product/security/infrastructure scope and cannot be resolved from standards/current decisions.

### 3. PMO and workstream execution

Use PMO semantics to derive workstreams from the authorized goal, `IMPLEMENTATION_PLAN.md`, requirements, architecture ownership boundaries, and current repo state. When Auto was invoked without a narrower textual goal and the project evidence identifies several parallel fronts, treat the Auto command as authorization to discover and present the candidate portfolio, not as authorization to silently select only one front.

When the workstreams are unambiguously contained inside an already explicit Auto goal, do not ask the owner to reconfirm the same portfolio.

When Auto was invoked generically and no single delivery goal exists, but multiple credible active fronts can be reconstructed, present the detected portfolio and ask the PMO confirmation question once. That portfolio confirmation becomes the Auto goal for the current conversation.

Do not ask "¿qué resultado concreto debe completar Auto?" merely because there is no single next TASK item when project-level evidence already supplies a coherent set of parallel fronts.

Ask for a missing goal only when neither a single goal nor a coherent candidate portfolio can be established from current project evidence.

When runtime-supported workers are available, the PMO orchestrator may delegate confirmed/in-scope workstreams under `PHDK_PMO.md`. Workers use **Auto execution semantics** inside one workstream but do not activate a nested `PHDK auto` lifecycle or recursively invoke Capture/Plan/PMO.

### 4. Integration Review

After workstream execution, perform the PMO Integration Review and produce one coherent candidate. Reconcile shared files, APIs, schemas, data contracts, navigation, translations, version/changelog, and cross-workstream assumptions.

### 5. UAT and repair

Run `PHDK uat` on the integrated candidate. Automatically execute `PHDK uat fix` semantics for all in-scope FAILs and removable BLOCKED cases. Continue until acceptance succeeds or only concrete external/manual/material-decision blockers remain.

### 6. Check and remediation

Run `PHDK check` against the integrated candidate. Under Auto, AUTO-FIXABLE and FIXABLE WITH VALIDATION gaps that are within the authorized goal are automatically approved for remediation; repair them, rerun applicable validation, and rerun Check. DECISION REQUIRED / EXTERNAL-MANUAL / out-of-scope findings remain explicit.

### 7. Delivery

Complete final repository verification, version reconciliation, normal branch/PR delivery, merge, and remote verification under `MAIN_DELIVERY_STANDARD.md`.

No separate approval is required between these lifecycle stages when they stay inside the identified Auto goal.

## One complete goal, no stage approvals

Take scope from the owner's current request and the strongest available project requirements baseline. When `PHDK capture` artifacts exist, use `PROJECT_INTENT.md`, `REQUIREMENTS_TRACEABILITY.md`, `PRD.md`, and `FEATURES.md` as the canonical project-level scope/intent inputs. The goal may include multiple features, packages, stages, or an explicitly selected backlog. Break it into implementation steps internally and continue through all of them; finishing a slice, scaffold, feature, stage, candidate version, or PR is not finishing the whole goal. Do not reduce an explicitly requested complete project to its first release or MVP.

The activation authorizes necessary in-scope planning, implementation decisions, code/documentation/test-source changes, integration repairs, final verification, version metadata, commits, branch push, PR, and merge under `MAIN_DELIVERY_STANDARD.md`. Do not ask for an OK per plan, file, stage, feature, risk label, commit, or merge. Honor an explicitly narrower audit/local/branch/PR-only outcome or a different delivery target.

Use existing product requirements, architecture, design tokens, and repository conventions to resolve routine choices. Prefer a reversible choice consistent with them and record material assumptions. Do not restart a specification interview, handoff-approval cycle, or bootstrap approval merely because another PHDK template contains one.

If there is no identifiable single current goal, inspect Capture/Plan/PMO artifacts, requirements, active branches/changes, UAT/Check findings, and current plans for a coherent active portfolio. If one exists, enter PMO portfolio confirmation rather than asking for a single goal. Only ask for a missing goal when no coherent single goal or portfolio can be derived. Do not select an arbitrary stale TASK item or unrelated backlog entry.

Current authorization covers the sensitive behavior actually described in the goal; authentication, data, payments, infrastructure, and policy labels do not create a second PHDK-only human-review gate. Review the actual behavior carefully. A broad statement that there is no risk does not prove that fact or authorize undisclosed destructive behavior, unrelated access, new spending, or a new material product/security decision. Use a safe in-scope alternative where possible. Isolate a genuinely unresolved decision and continue independent authorized work before asking only for that missing decision.

## Keep development moving

1. Read the current request, active repository instructions, actual worktree, target, toolchain, hooks, and requirements. Define the completion criteria for the whole goal and identify final verification commands and access prerequisites early. Use the reconciliation rules in `PHDK_UNLOCK.md` to correct actual stale documentary stops contradicting this authorization; no extra unlock command is required. This does not silently start a full standards upgrade unrelated to the goal.
2. Use a suitable existing task branch or create one from a known target. Preserve unrelated edits and other contributors' work. Keep one cohesive candidate for the whole goal; do not create a release, push to `main`, or require acceptance after every stage.
3. Implement the complete agreed behavior and necessary tests, documentation, states, permissions, and integration wiring. A TODO, disabled path, scaffold, fabricated data, or claimed future stage does not satisfy a requested working feature. Do not silently shrink the goal to report completion.
4. Maintain concise factual task/progress records. Complete the next necessary step within the same goal without requesting permission to continue. New issues may be repaired when they prevent the requested behavior or its verification; unrelated enhancements remain outside scope.
5. When a component is blocked, diagnose and make bounded in-scope repairs, use an already permitted route, or continue independent parts. A dependency or actual control may block one operation without blocking all development. Do not repeat an unchanged failing command or wait in a polling loop. When no permitted progress remains, report the precise blocker and completed work instead of claiming success or asking for a generic OK.

## Verify the whole candidate at the end

Do the full development first. Write necessary test coverage with the implementation, but execute planned tests and comprehensive QA on the completed integrated candidate. This includes risk-triggered coverage required for final acceptance; its being required does not itself mean running it after each slice. PHDK slice checklists, stage reviews, and foundation checks describe coverage to collect at this final boundary; they are not intermediate permission or acceptance gates in Auto.

Use an intermediate local check only when it is necessary to diagnose an implementation blocker or an actual mandatory hook/control requires it. Do not run full install/build/test cycles after each stage. Preserve mandatory controls at the operation they govern: delaying final QA never permits skipping a hook, publishing unverified code, or postponing a required pre-push check until after `main` is updated. Avoid unnecessary checkpoint commits that would create early validation cycles; any necessary checkpoint still obeys repository rules and is not a release.

After every in-scope part is implemented and integrated, run `PHDK uat` under `UAT_STANDARD.md` when the goal includes end-user behavior or acceptance criteria, then review the entire outgoing diff and run all applicable local verification for the whole goal: repository-required format/lint/typecheck/build gates, meaningful unit/in-process integration tests, and cross-feature regression checks justified by the changed behavior. Use existing isolated fixtures/doubles. Documentation-only goals use complete source/reference and policy-scenario review where relevant; do not invent an application build for a standards repository.

Fix in-scope failures, including UAT FAIL cases attributable to this goal, and rerun the affected UAT cases/checks until the candidate meets the completion criteria or a concrete unsatisfied control/access/decision blocks it. Expand verification only to address remaining risk or a required gate. Do not delete meaningful failing tests, weaken a check, label a failure passed, or declare all tests passed when any required check did not run. The assistant performs the permitted checks; do not hand routine local verification to the owner.

Necessary mechanical formatting repairs for an applicable failing gate are part of this goal, including an existing workflow file when its meaning is demonstrably unchanged. Review the exact diff and use appropriate parsed/source evidence to retain commands, triggers, jobs, permissions, and other behavior. Do not demand another OK solely for a non-semantic format repair. This narrow permission does not authorize workflow behavior changes, CI execution, unrelated cleanup, or removing the gate. If equivalence or scope cannot be established, isolate that blocker and finish independent work.

The final test boundary covers everything applicable to this complete goal, not every possible future feature or a browser/live-service test. `EXECUTION_SCOPE.md` still excludes browser/headless tests, application probes, live databases, paid verification calls, and provider writes. Requested bounded provider metadata/log reads remain available as separate diagnostic evidence. If the owner wants final acceptance, present the complete result and actual evidence then; do not require human testing after every stage or invent a human-acceptance prerequisite for an otherwise permitted merge.

## Deliver once the complete candidate is verified

Reconcile the final version and changelog against fresh remote `main` using the repository standard. Bump for the complete delivery, not each internal stage. Ensure the source-changing commit subjects start with the resulting version; if integration changes version metadata or behavior, refresh the affected final checks. Follow existing commit rules without unnecessary checkpoint releases.

Finish the scoped branch push, PR, actual required controls, merge, and remote content/version verification. Current owner approval is already present for the identified outcome; no additional PHDK-only human sign-off is required at the end. A server-required or current explicitly required named/independent/formal review remains a real control: finish all otherwise permitted work and report that exact requirement if it prevents integration. Never use an admin override, force-push, skipped hook, alternate credential, or fabricated review to evade it.

A permitted update to `main` may trigger the existing GitHub-connected autodeploy. Do not disable it, create Actions/workflows, deploy through Railway/provider CLI/API/dashboard, or change provider/repository settings. Report code integration and any observed deployment state separately; neither a local test nor a merge proves production health.

## Relationship to PMO

Auto is now the end-to-end lifecycle orchestrator for one authorized project goal. PMO is the multi-workstream coordination stage inside that lifecycle and remains independently invocable with `PHDK PMO`.

A PMO worker does **not** recursively activate Auto as a command. It uses Auto's bounded execution semantics only for its assigned workstream.

When a PMO worker uses Auto execution semantics:
- its scope is exactly one confirmed/in-scope workstream contract;
- PMO supplies the intent/requirement links, ownership boundaries, dependencies, and branch/worktree;
- the worker completes that workstream without per-stage approval, but does not run Capture/Plan/PMO/UAT/Check lifecycle stages independently;
- Auto returns changed files/commits/checks/assumptions/blockers to PMO;
- PMO, not the worker, owns shared/global version/changelog/schema/navigation integration and the combined candidate;
- the worker does not select another workstream or delegate further.

A standalone explicit Auto invocation owns the complete lifecycle described above.

## Relationship to other PHDK commands

- Auto uses the normal branch/PR delivery route. An explicit `PHDK auto` for the identified goal replaces Developer Mode for that goal, including a currently identified task whose direct push stopped. Diagnose and satisfy the failed control before the permitted normal delivery; this is a new owner instruction, not a retry/bypass of the stopped direct push. A later explicit Developer Mode activation replaces Auto for its eligible requested task; neither mode silently inherits the other's permissions.
- Unlock repairs documentary blockers; Auto also carries the whole authorized development goal through final verification and delivery. A scoped rule repair does not start unrelated product work or cancel the rest of the current Auto goal.
- A bare `PHDK upgrade` keeps its synchronization-only contract. Include synchronization in Auto delivery only when the owner includes it in the identified goal. Installing/updating command definitions activates no mode.
- Auto changes PHDK's development cadence and eliminates PHDK-only approval pauses for the current goal. Its specific cadence takes precedence over generic per-slice verification, interview, stop-and-ask, or handoff templates. Standalone Auto grants no delegated agents; when invoked as a PMO worker, delegation authority belongs only to the PMO orchestrator and the worker itself may not delegate. Auto never grants unattended/background/post-conversation execution, recurring work, expanded credentials, or removal of actual security/access/repository controls.

## Completion report

The final report must close the lifecycle explicitly. Include a compact final board showing the terminal status of every applicable stage, links/paths to principal canonical artifacts, and the historical run folder. Verify the run-level historical `LIFECYCLE.md` is complete before claiming lifecycle completion.

Example:

```text
PHDK Auto — final lifecycle
Preflight ............ COMPLETED
Capture .............. REUSED
Plan ................. COMPLETED
PMO / Workstreams .... COMPLETED
Integration Review ... COMPLETED
UAT .................. COMPLETED — ACCEPTED
UAT Fix .............. NOT APPLICABLE
Check ................ COMPLETED — ALIGNED
Remediation .......... NOT APPLICABLE
Delivery ............. COMPLETED
```

Report once the entire requested outcome and permitted delivery are complete: implemented scope, final verification and repairs, version/commit/PR/remote target, and remaining evidence limits. During work, keep communicating without surrendering the task at an intermediate stage. If a real blocker prevents full completion, identify its source and affected operation, finish everything independent, and report the unfinished scope explicitly. Never call a partial release the completed goal.
