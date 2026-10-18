# PHDK Auto

## Mandatory automation cleanup during final Check

Run the `PHDK_AUTOMATION_HYGIENE.md` gate as part of Auto's final `PHDK check`: inspect repository files **and** GitHub/Railway remote metadata when authorized read-only access exists. Reconcile active workflows, PHDK legacy agents/schedules, CI/deployment dependencies, Railway Wait for CI, cron/restart/redeploy loops and potential charges. Automatically repair clearly obsolete PHDK-generated source/configuration within the current goal and validate preserved GitHub-connected autodeploy, but **never** disable GitHub Actions, alter Railway settings or remove required security checks through provider writes. Report inaccessible external settings as UNVERIFIED / EXTERNAL and do not claim full alignment without evidence.


## Verified delivery

Before final success for a remote-main goal, comply with `PHDK_COMPLETION_GATE.md`, create evidence after merge, run the mechanical verifier where available, and independently reconcile PR merge, required checks and confirmed commitments. Without these proofs do not report COMPLETED. Apply `PHDK_AUTO_CONTINUITY.md` before a terminal blocker report; missing evidence is work to obtain when a permitted path remains, not an automatic reason to stop.


## Mandatory administration implementation and remediation

For every stateful/administered portal, use `ADMIN_CONSOLE_STANDARD.md` from Capture through Plan, implementation, UAT and Check. Resolve tenancy intentionally; build missing real Configuración pages, protected APIs, database models/policies, tenant/user/role/settings/backup/agent workflows and tests in the current authorized goal. Use `ADMIN_ARCHITECTURE.md`, `ADMIN_CAPABILITY_MATRIX.md`, `ADMIN_SETTINGS_REGISTRY.md` and conditional `AI_WORKFLOW_CATALOG.md`; do not mark admin readiness from a source doc or placeholder tabs. Single-tenant uses elevated admin; multi-tenant uses super_admin plus tenant-scoped admins. At final Check automatically remediate in-scope unambiguous gaps, never silently convert tenancy or operate live destructive resources.

## UX/UI in the autonomous lifecycle

When the goal includes UI or an existing interface, apply `PHDK_UX_UI.md` from Capture/Plan through Integration and UAT: architecture and design deliverables precede implementation; brownfield designs begin with existing-interface evidence and preserve correct flows; UAT examines real journeys, accessibility and visual consistency, repairs in-scope P0/P1 findings and retests. Stage handoffs and completion audit account for these deliverables. Browser use remains limited to UAT/UAT Fix. Do not claim success with unresolved P0/P1 UI findings.


## Commitment reconciliation and prohibition on false completion

Always apply `PHDK_COMMITMENT_STANDARD.md` through Capture, Plan, PMO, UAT and Delivery. Show the owner a PMO portfolio confirmation opportunity including additional defects/features if not already confirmed, then continuous milestone/status boards. Track each confirmed `PHDK_COMMITMENTS.md` ID through `PHDK_COMMITMENT_COVERAGE.md`, workstream, UAT, version, PR and verified remote target. Before a success statement, create `PHDK_COMPLETION_AUDIT.md`, reconcile the original plan and ALL in-scope open PRs, and fail closed if any confirmed commitment is missing, blocked, unverified or unmerged. Open PRs are unfinished delivery, even when code or tests passed. If a real merge/review/access blocker remains, report **PARTIALLY DELIVERED** or **BLOCKED** and itemized next actions, never `COMPLETED` or 100%. Only explicit owner decisions may defer/remove a commitment; preserve history. Include final commitment and PR reconciliation in the user-facing terminal board.

## Command and lifetime

Run `PHDK_PREFLIGHT.md` once at Auto entry, then validate handoffs and re-check only newly relevant capabilities when later lifecycle stages need them. Repeat full Preflight only if installation or manifest integrity has changed. See `PHDK_COHERENCE_STANDARD.md`. Auto also follows the stage input/output/handoff contracts in `PHDK_LIFECYCLE.md`. Do not repeat a noisy full preflight at every internal stage.

`PHDK auto` explicitly starts the complete PHDK delivery lifecycle for the identified current goal. Match case-insensitively after trimming whitespace; an accompanying brief, task, project goal, or coherent Capture baseline supplies the scope. If the current conversation already identifies that goal, start without another confirmation or a mandatory interview. If there is no single current delivery but the repository already exposes multiple parallel pillars/fronts through Capture, Plan, PMO artifacts, requirements, or current work, do not collapse them into a request for one arbitrary goal; enter PMO portfolio discovery instead. A request to add this command, quoted examples, installed files, and old task records do not activate it.

### AUTO FORCE — continue without PHDK review waits

`PHDK auto force` is the explicit FORCE variant of Auto for the identified current goal. It uses the same lifecycle, normal branch/PR delivery, completion evidence and conversation lifetime. The current invocation authorizes restoring that goal's factual mandate and continuing its scoped implementation, technical diff review, mandatory checks, branch push, PR, merge into `main` and remote verification without another approval. It is not Developer Mode, a force-push command or permission for unrelated work.

In FORCE, human, manual, formal, owner-diff-approval and security-signoff checkpoints imposed **only by PHDK** are **nonblocking by definition** (`NON_BLOCKING_BY_MODE`). Do not perform a preventive review/protection investigation, fetch those rules to decide whether to attempt delivery, search for approvers or wait for human approval before continuing. An inherited "review pending", missing review event or generic owner-decision label does not establish a blocker. Perform the technical source/diff/security review and mandatory permitted checks, then execute the authorized delivery operations. Scope, candidate/head/target and remote-result verification still apply.

FORCE does not fabricate a review, skip a hook, override a protection, change credentials/settings or erase a genuine current owner stop. Honor already-known applicable controls. An actual GitHub, hook or tool rejection is evidence for repair, **not an automatic execution endpoint**. Production access, destructive operations, new spending and provider writes retain their existing boundaries.

After an actual delivery rejection, follow the repair-and-retry cycle in `PHDK_AUTO_CONTINUITY.md`:

1. Report the observed rejection briefly in a nonterminal progress update.
2. Investigate its actual cause using relevant error, check, hook, candidate and target evidence. This is diagnosis after a real failure, not a preventive search for review requirements.
3. Repair the in-scope technical/check/conflict/state defect under the existing mandate.
4. Revalidate the affected result and retry the authorized branch push, PR or merge that updates `main`.
5. Independently verify the resulting remote `main`, or continue this cycle while another permitted repair or new evidence can produce progress.

Never end at the first rejection or ask again for the same delivery permission. Do not repeat an unchanged rejected write, weaken a gate, use an admin override/alternate credential or force-push to evade a control. Only an unresolved real boundary after permitted repairs and independent work can require an external action; preserve the mandate and state exactly what remains.

### Mandate and continuity for both variants

Follow `PHDK_AUTO_CONTINUITY.md` on entry, after context recovery, at checkpoints and before any terminal interruption/blocker report. Maintain `docs/phdk/lifecycle/<run-id>/AUTO_STATE.json` as factual evidence of the current request, mandate, decisions, restrictions, progress and next action; use the canonical contract rather than inventing another schema. This record does not independently activate a mode or grant reusable authority. The same unfinished current request survives status questions and context compaction. In a later conversation, a new explicit Auto/Force invocation supplies the current request to resume the identified goal; files alone never start execution.

FORCE resumes recoverable authorized work immediately. Its continuity check must not become a review/protection investigation or a new permission questionnaire. Normal Auto also retains existing authorization and completes independent work without ceremonial approval.

AUTO FORCE also applies the operative reminder and proposal contract in `PHDK_AUTO_CONTINUITY.md` and `PHDK_COMMUNICATION_STANDARD.md`: recover current relevant rules, discard stale agent interpretations, find solutions and propose missing behavior/defaults/configuration per in-scope gap. Resolve ordinary inferable details and execute without asking the owner to design everything or recommending that confirmed gaps be excluded. Keep this reminder in every substantive progress update, after partial deliveries and before proposed questions/blockers; a short context refresh does not rerun full Preflight. A truly new indispensable decision is presented with a concrete recommendation and impact after independent work is exhausted.

The continuity helper is advisory evidence, not an approval service or new execution veto. Missing/malformed `AUTO_STATE.json` means `REPAIR_STATE`: rebuild the factual record from available current-request evidence and continue internally, without requesting permission to repair bookkeeping. Use the canonical contract's dispositions for continuing, repair/retry, external waiting, delivery verification and an actual owner stop.

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
UAT Prep ............. PENDING
UAT .................. PENDING
UAT Fix .............. PENDING
SEO .................. PENDING
AEO/GEO .............. PENDING
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
→ UAT Prep → UAT → UAT Fix → SEO → AEO/GEO → Check → in-scope Check remediation → delivery
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

Every substantive Auto/Force progress update includes the mandate and next-action capsule in `PHDK_COMMUNICATION_STANDARD.md`. FORCE additionally carries the mandatory reminder to reload current rules, reconcile inherited blockers, find solutions and propose what is missing. Execute the next action in the same invocation; the reminder is not a substitute for execution or a promise of background work. If a real restriction blocks an action, name that action truthfully. Follow `PHDK_AUTO_CONTINUITY.md` for terminal status.

Do not narrate every command/file operation. Communicate lifecycle movement and material evidence.

At any user status question such as "¿qué estás haciendo?", "status", or "dónde vas", answer with the current lifecycle board/stage first, then relevant execution detail.

Send concise progress updates without turning them into approval questions or ending the task at a milestone.

Both variants last for this goal in the active conversation. Exit on `PHDK salir de auto`, a clear owner stop, completion of the whole requested outcome, or the conversation ending. A status/link question, context compaction, or assistant-written checkpoint does not end an unfinished goal. Keep the factual mandate and task evidence across turns under `PHDK_AUTO_CONTINUITY.md`, but never save a reusable `auto=true` authority flag or resume from files alone in another conversation. This is an instruction to the assistant, not a daemon, scheduler, or shell executable.

## Full lifecycle, one authorization

Auto's identified goal is the authorization boundary for the whole lifecycle.

### Mandatory intent-to-implementation reconciliation

On every explicit Auto invocation, reread the complete current intent and requirements baseline, including confirmed commitments, non-goals and acceptance criteria, and compare it with actual product source and current evidence. Review the whole baseline even when existing Capture/Plan artifacts look complete. Reuse them only after verifying freshness, coverage and consistency with the current request; record the reconciliation in `IMPLEMENTATION_PLAN.md` and `PHDK_COMMITMENT_COVERAGE.md`. Reviewing from the beginning does not mean recreating valid documents or rewriting working code. A narrower current goal still limits what may be implemented; record unrelated gaps without activating them.

Classify implementation from inspected product behavior and source, not from the existence of a repository, README, package manifest, PHDK installation or old stage folders:

| Observed state | Required action inside Auto |
|---|---|
| Readable repository with no meaningful product implementation, including requirements-only or scaffold-only projects | Treat required product development as greenfield: finish/reuse the architecture plan, then create and implement the complete authorized product. |
| Partially implemented product | Preserve valid code and complete every missing or incomplete in-scope requirement and its integration. |
| Implementation appears complete | Reconcile every in-scope requirement with current source and validation evidence; repair gaps and reuse verified work. |
| Source cannot be read or the inventory is incomplete | Record UNVERIFIED/access evidence, diagnose the actual blocker and continue independent permitted work; never infer an empty or complete project. |

For each confirmed in-scope requirement, record existing source/evidence, missing behavior, implementation task/owner, and acceptance evidence or its precise pending blocker. Missing code for an already confirmed requirement is authorized implementation work, not a new feature requiring another scope approval. Explicitly documentary or planning-only requests keep their stated deliverable.

**Plan completion must immediately lead to implementation in the same active invocation.** Execute dependency-ordered workstreams, creating the required application structure, domain logic, data/persistence, APIs, UI, permissions, integration wiring and test source only where the intent calls for them. Keep developing until the entire authorized scope is implemented and integrated; then continue through UAT Prep, UAT/repair, Check/remediation and delivery as applicable. A foundation, first feature or MVP does not replace a requested complete product. Missing external access may block dependent operations, but does not excuse stopping all development at a plan.

Do not mark required implementation, Integration or acceptance NOT APPLICABLE because the application has not been built yet. Plans, TODOs, placeholder tabs, disabled actions and fixture-only behavior do not establish implementation or acceptance. Update coverage with concrete source and executed validation evidence before marking commitments verified; unresolved required behavior remains unfinished.

### 1. Capture

After the full baseline reconciliation above, run Capture semantics if the professional requirements baseline is missing/incoherent. Ask only genuinely material missing requirements questions. If the baseline is already coherent and current, reuse it without restarting the interview merely because product code is absent.

### 2. Plan

Run `PHDK plan` semantics against the captured requirements. For greenfield, define the target solution/repository/UX architecture and implementation plan. For brownfield, reconstruct current architecture first, preserve valid decisions, define target state, and create an incremental convergence plan.

Ask only for architecture decisions that materially change product/security/infrastructure scope and cannot be resolved from standards/current decisions.

After Plan's exit gate passes, immediately start the next eligible implementation task through stage 3. Do not end with a plan, ask whether to start coding, or require a separate Developer Mode/PMO command for already-authorized development.

### 3. PMO and workstream execution

Use PMO semantics to derive workstreams from the authorized goal, `IMPLEMENTATION_PLAN.md`, requirements, architecture ownership boundaries, and current repo state. When Auto was invoked without a narrower textual goal and the project evidence identifies several parallel fronts, treat the Auto command as authorization to discover and present the candidate portfolio, not as authorization to silently select only one front.

When the workstreams are unambiguously contained inside an already explicit Auto goal, do not ask the owner to reconfirm the same portfolio.

Actually execute those workstreams. For a single straightforward stream, the current assistant implements it directly; the absence of parallel workers or PMO overhead never makes implementation optional. A PMO coordination document or worker assignment is not a completed workstream.

When Auto was invoked generically and no single delivery goal exists, but multiple credible active fronts can be reconstructed, present the detected portfolio and ask the PMO confirmation question once. That portfolio confirmation becomes the Auto goal for the current conversation.

Do not ask "¿qué resultado concreto debe completar Auto?" merely because there is no single next TASK item when project-level evidence already supplies a coherent set of parallel fronts.

Ask for a missing goal only when neither a single goal nor a coherent candidate portfolio can be established from current project evidence.

When runtime-supported workers are available, the PMO orchestrator may delegate confirmed/in-scope workstreams under `PHDK_PMO.md`. Workers use **Auto execution semantics** inside one workstream but do not activate a nested `PHDK auto` lifecycle or recursively invoke Capture/Plan/PMO.

### 4. Integration Review

After workstream execution, perform the PMO Integration Review and produce one coherent candidate. Reconcile shared files, APIs, schemas, data contracts, navigation, translations, version/changelog, and cross-workstream assumptions.

### Mandatory debug-widget verification

For every applicable app-style product, Auto must inspect `DEBUG_DIAGNOSTICS_STANDARD.md` as a separate required acceptance gate, alongside available skills and capability checks. Discover the *actual source implementation* and its usage sites: do not assume a version label or an old checklist establishes compliance. If absent, implement a single shared always-visible version → clipboard → trash icon-only component on public home, login, shell and admin, including unauthenticated visitors and debug OFF, compact fixed visual metrics (only `vX.Y.Z`, 12px text, 28×28px visible buttons, 14×14px icons, 4px gap; never SHA/date or oversized tiles), exact handlers, green checkmark success/revert, sanitized verbose report, cache reset and safe access gates. Add focused component/unit tests. Trace evidence to source files, test results and the final Check report; mark unresolved items BLOCKED/FAIL rather than silently skipping. For projects to which the standard does not apply, record an evidence-backed NOT APPLICABLE. Do not misrepresent code review as browser/runtime verification.

### 5. UAT Prep — mandatory implementation before acceptance

After Integration Review, execute `PHDK uat prep` under `PHDK_UAT_PREP.md`. **Build, seed and verify** missing Company Co synthetic users, secure provider-backed/test-only non-production session bootstrap, real role/tenant policies and in-process checks; implement safe required Test as functionality where in scope. Write `UAT_AUTH_PLAN.md`, `UAT_ROLE_MATRIX.md`, `UAT_FIXTURE_MANIFEST.md`, `UAT_PREP_REPORT.md` plus `45-uat-prep/HANDOFF.md`. If Prep edits product code, reconcile the integration revision and rerun impacted non-browser checks before entering UAT. Do not defer routine account development to UAT Fix. Browser access is not granted during Prep. Treat external provider authorization/production/paid blockers individually, not as a reason to skip all Prep.

### 6. UAT and repair
**Auto UAT Browser Gate:** At the UAT Prep → UAT boundary run `UAT_BROWSER_READINESS_STANDARD.md` as a required phase transition, confirm **Navegador UAT: permiso de fase ACTIVO; acceso real VERIFICADO / NO DISPONIBLE / REQUIERE CONEXIÓN**, and log actual evidence in UAT Access/Report. Recheck on UAT Fix or re-entry as needed. Do not ask for budget caps, paid testing/browser APIs or discretionary owner approval of already permitted browser use. Continue independent cases and isolate the actual host connection/target blocker without fabricating a PASS or broadening production/provider permissions.


Run `PHDK uat` **after verifying the current Prep handoff** against the reconciled integrated candidate. Reuse legitimate synthetic sessions and test real authenticated browser/API roles and tenant isolation in UAT. Newly broken Prep items are repaired in UAT Fix, followed by impacted Prep-check reruns; routine account provisioning belongs to stage 45. Never create a production test-auth backdoor or infer browser access when disconnected. Automatically execute `PHDK uat fix` semantics for all in-scope FAILs and removable BLOCKED cases. Continue until acceptance succeeds or only concrete external/manual/material-decision blockers remain.

### 7. SEO and AEO/GEO

After UAT and UAT Fix, run `PHDK_SEO.md` on public indexable pages and then `PHDK_AEO_GEO.md` on applicable public answer/discovery content. Show separate status-board rows and transitions, preserve `65-seo/` and `67-aeo-geo/` handoffs, execute safe in-scope source fixes and revalidate impacted UAT. Mark either NOT APPLICABLE only with evidence when a product has no relevant public discovery goal. Neither stage silently authorizes browser, live probes, paid calls, production changes or fabricated AI visibility. Do not proceed to Check without verifying both gates/explicit N/A records. Reconcile resulting tasks with the commitment ledger.

### 8. Check and remediation

Run `PHDK check` against the integrated candidate. Under Auto, AUTO-FIXABLE and FIXABLE WITH VALIDATION gaps that are within the authorized goal are automatically approved for remediation; repair them, rerun applicable validation, and rerun Check. DECISION REQUIRED / EXTERNAL-MANUAL / out-of-scope findings remain explicit.

### 9. Delivery

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
5. When a component is blocked, make bounded in-scope repairs, use an already permitted route, or continue independent parts. Apply `PHDK_AUTO_CONTINUITY.md`: pending assistant work and stale state are not external blockers; in FORCE, PHDK-only reviews are nonblocking without investigation. After an actual rejection, report, diagnose, repair, revalidate and retry the affected authorized delivery operation; continue while permitted progress remains. A dependency, current owner restriction or actual control may block one operation without blocking all development. Do not repeat an unchanged failing command or wait in a polling loop. Only when no permitted progress remains may a terminal report identify the exact affected operation, observed reason, unfinished work and precise resumption action instead of asking for a generic OK.

## Verify the whole candidate at the end

Do the full development first. Write necessary test coverage with the implementation, but execute planned tests and comprehensive QA on the completed integrated candidate. This includes risk-triggered coverage required for final acceptance; its being required does not itself mean running it after each slice. PHDK slice checklists, stage reviews, and foundation checks describe coverage to collect at this final boundary; they are not intermediate permission or acceptance gates in Auto.

Use an intermediate local check only when it is necessary to diagnose an implementation blocker or an actual mandatory hook/control requires it. Do not run full install/build/test cycles after each stage. Preserve mandatory controls at the operation they govern: delaying final QA never permits skipping a hook, publishing unverified code, or postponing a required pre-push check until after `main` is updated. Avoid unnecessary checkpoint commits that would create early validation cycles; any necessary checkpoint still obeys repository rules and is not a release.

Both Auto and FORCE preauthorize the existing synchronous isolated checks required to deliver this goal, including a complete `pnpm test`/Vitest suite, lint, typecheck, format, build and composition when the repository requires them. Inspect their actual scripts for scope and side effects, then run them without asking again because they are tests, a full suite or a pre-push requirement. Avoiding optional tests does not prohibit mandatory checks. Preserve an explicit current owner ban on the actual operation and excluded browser/live/paid/provider effects; isolate that concrete conflict, not a hypothetical need for approval. Do not bypass a hook to avoid a required suite.

After every in-scope part is implemented and integrated, run `PHDK uat prep` then `PHDK uat` under `UAT_STANDARD.md` when the goal includes end-user behavior or acceptance criteria, then review the entire outgoing diff and run all applicable local verification for the whole goal: repository-required format/lint/typecheck/build gates, meaningful unit/in-process integration tests, and cross-feature regression checks justified by the changed behavior. Use existing isolated fixtures/doubles. Documentation-only goals use complete source/reference and policy-scenario review where relevant; do not invent an application build for a standards repository.

Fix in-scope failures, including UAT FAIL cases attributable to this goal, and rerun the affected UAT cases/checks until the candidate meets the completion criteria or a concrete unsatisfied control/access/decision blocks it. Expand verification only to address remaining risk or a required gate. Do not delete meaningful failing tests, weaken a check, label a failure passed, or declare all tests passed when any required check did not run. The assistant performs the permitted checks; do not hand routine local verification to the owner.

Necessary mechanical formatting repairs for an applicable failing gate are part of this goal, including an existing workflow file when its meaning is demonstrably unchanged. Review the exact diff and use appropriate parsed/source evidence to retain commands, triggers, jobs, permissions, and other behavior. Do not demand another OK solely for a non-semantic format repair. This narrow permission does not authorize workflow behavior changes, CI execution, unrelated cleanup, or removing the gate. If equivalence or scope cannot be established, isolate that blocker and finish independent work.

The final test boundary covers everything applicable to this complete goal, not every possible future feature or a browser/live-service test. `EXECUTION_SCOPE.md` permits browser/headless tests only during the Auto run's UAT and UAT Fix phases, on local/staging test targets by default; unauthorized application probes, live databases, paid verification calls and provider writes remain excluded. Requested bounded provider metadata/log reads remain available as separate diagnostic evidence. If the owner wants final acceptance, present the complete result and actual evidence then; do not require human testing after every stage or invent a human-acceptance prerequisite for an otherwise permitted merge.

## Deliver once the complete candidate is verified

Reconcile the final version and changelog against fresh remote `main` using the repository standard. Bump for the complete delivery, not each internal stage. Ensure the source-changing commit subjects start with the resulting version; if integration changes version metadata or behavior, refresh the affected final checks. Follow existing commit rules without unnecessary checkpoint releases.

Finish the scoped branch push, PR, actual required controls, merge, and remote content/version verification. Current owner approval is already present for the identified outcome; no additional PHDK-only human sign-off is required at the end. FORCE treats PHDK-only human/manual/formal reviews as nonblocking without investigating them and proceeds with technical diff review, mandatory checks and permitted delivery. Honor already-known actual controls and use real rejection evidence for the report/diagnose/repair/revalidate/retry cycle above; do not turn it into a preventive FORCE review/protection lookup or stop at the first rejection. Finish permitted repairs and independent work before reporting an operation genuinely prevented by a current owner restriction or actual control. Never use an admin override, force-push, skipped hook, alternate credential, or fabricated review to evade it.

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

- Auto and `PHDK auto force` use the normal branch/PR delivery route. Either explicit invocation for the identified goal replaces Developer Mode for that goal, including a currently identified task whose direct push stopped. Satisfy the actual failed control before the permitted normal delivery; this is a new owner instruction, not a retry/bypass of the stopped direct push. FORCE adds no investigation of PHDK-only reviews. A later explicit Developer Mode activation replaces Auto for its eligible requested task; neither mode silently inherits the other's permissions.
- Unlock repairs documentary blockers; Auto also carries the whole authorized development goal through final verification and delivery. A scoped rule repair does not start unrelated product work or cancel the rest of the current Auto goal.
- A bare `PHDK upgrade` keeps its synchronization-only contract. Include synchronization in Auto delivery only when the owner includes it in the identified goal. Installing/updating command definitions activates no mode.
- Auto changes PHDK's development cadence and eliminates PHDK-only approval pauses for the current goal. Its specific cadence takes precedence over generic per-slice verification, interview, stop-and-ask, or handoff templates. Standalone Auto may delegate bounded in-session tasks under `PHDK_INTELLIGENT_EXECUTION.md`; PMO workers themselves cannot delegate. Auto never grants unattended/background/post-conversation execution, recurring work, expanded credentials, or removal of actual security/access/repository controls.

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
UAT Prep ............. COMPLETED / REUSED / BLOCKED
UAT .................. COMPLETED — ACCEPTED
UAT Fix .............. NOT APPLICABLE
SEO .................. COMPLETED / NOT APPLICABLE
AEO/GEO .............. COMPLETED / NOT APPLICABLE
Check ................ COMPLETED — ALIGNED
Remediation .......... NOT APPLICABLE
Delivery ............. COMPLETED
```

Report once the entire requested outcome and permitted delivery are complete: implemented scope, final verification and repairs, version/commit/PR/remote target, and remaining evidence limits. During work, keep communicating without surrendering the task at an intermediate stage. If a real blocker prevents full completion, identify its source and affected operation, finish everything independent, and report the unfinished scope explicitly. Never call a partial release the completed goal.


## Mandatory forward progress, resumability, and truthful closing

**A lifecycle stage is a checkpoint, not an execution endpoint.** In a single active invocation, after every successfully closed stage, validate its exit handoff, persist status, and immediately begin the next eligible stage. Do not return a terminal assistant answer merely because Preflight, Capture, Plan, PMO, Integration, UAT, SEO, AEO/GEO, or Check produced its deliverables. Progress messages must be nonterminal. A required question is a stop only when the answer changes an actual material decision and there is no independent in-scope work left to execute.

**Deterministic restart from repository evidence.** On each new explicit `PHDK auto` or `PHDK auto force` invocation:
1. Reread the complete current intent/requirements baseline and actual source under the mandatory intent-to-implementation reconciliation above, then read the current owner goal, `PHDK_LIFECYCLE_STATUS.md`, run-level historical `LIFECYCLE.md`, `PHDK_COMMITMENTS.md`, `PHDK_COMMITMENT_COVERAGE.md`, `IMPLEMENTATION_PLAN.md`, handoffs, and current git/PR facts.
2. Recover the factual mandate and checkpoint from `docs/phdk/lifecycle/<run-id>/AUTO_STATE.json` under `PHDK_AUTO_CONTINUITY.md`, and reconcile evidence with the current authorized goal. Treat stored state as context, never as authorization to launch unattended work. Do not assume a stage passed because its folder exists: verify its technical exit criteria, freshness, and missing commitments. In FORCE, PHDK-only reviews are nonblocking without review/protection investigation.
3. Reuse verified stages, repair incomplete/stale handoffs, and resume at the earliest stage whose required exit gate is not satisfied. Never reset to Preflight/Capture/Plan for ceremony. Preflight still performs its short invocation-level safety/version check.
4. Preserve the same goal/run history when appropriate; record an explicit continuation entry with timestamp, previous checkpoint, and recovered next stage. If an earlier prerequisite changes, reopen it and invalidate the affected downstream gates.
5. Inspect in-scope open PRs and incomplete delivery artifacts before declaring the goal complete. A partial merge, open PR, or undone planned task remains unfinished.

**Mandatory progress loop (conceptual, not an unattended scheduler):**
```text
while authorized goal not complete:
    validate current stage prerequisites
    execute or reuse current stage
    write canonical artifacts + historical HANDOFF.md + checkpoint
    apply PHDK_AUTO_CONTINUITY.md; update factual AUTO_STATE.json
    treat pending assistant work, stale state and FORCE PHDK-only reviews as nonblocking
    if actual operation rejection:
        report briefly, diagnose actual cause, repair within scope, revalidate
        retry authorized delivery when repair or new evidence changes the result
        verify remote main after success; keep going while permitted progress remains
    if unresolved actual control, current owner restriction or material dependency:
        execute independent authorized work
        if no permitted progress remains: report precise BLOCKED evidence and resumption action
    else:
        advance immediately to the next eligible stage in this same invocation
verify all commitments + in-scope PRs + final delivery gates
only then report COMPLETED
```
No generic response-length, task-count, stage-count, or conversational milestone limit authorizes stopping at a successful stage. Respect real host/tool execution limits: when work cannot continue in this invocation, checkpoint accurately and say `INTERRUPTED — NOT COMPLETE`, without pretending to schedule a background continuation.

**Every exit response must include actionable next-step guidance**, even when the task is interrupted:
```text
PHDK Auto — <COMPLETED | BLOCKED | INTERRUPTED — NOT COMPLETE>
Goal: <goal>
Last verified stage: <stage>
Next pending stage: <stage / NONE>
Unfinished commitments: <IDs or NONE>
In-scope open PRs: <numbers or NONE>
Why execution stopped: <completed delivery / exact blocker / host execution boundary>
Next action: <automatic continuation in this invocation, exact owner action for blocker,
or "Run PHDK auto again to resume from <stage>">
Checkpoint: PHDK_LIFECYCLE_STATUS.md
History: docs/phdk/lifecycle/<run-id>/
```
Use `COMPLETED` only after the final completion audit, required checks, all scoped PR integration, and verified delivery. `INTERRUPTED` must never be presented as success or as an automatic background task. When no owner action is required, do not tell the user to rerun at each stage; continue now. When the active session is genuinely over, the next invocation must recover from persisted evidence rather than demand repeated stage commands.

## Mandatory terminal delivery gate


### Milestone publication loop before final UAT

Plan's `MILESTONE_PLAN.md` is executable delivery structure. During PMO/workstream execution, Auto completes milestones in dependency order. A milestone is not a lifecycle stage and must not be created merely to force a commit.

When a milestone's included workstreams are integrated and its declared non-browser technical acceptance evidence is satisfied, apply `PHDK_PROJECT_MANAGEMENT_STANDARD.md` and `MAIN_DELIVERY_STANDARD.md` to publish that milestone: refresh `main`, reconcile the actual SemVer increment, update version/changelog metadata, create version-prefixed commit(s), push the scoped branch, open/update the PR, satisfy applicable controls, merge to `main`, and independently read back the new main SHA/version. Record the actual delivery evidence against the milestone, refresh subsequent work from that verified `main`, and continue immediately.

Do **not** run the complete UAT/Check lifecycle or stop for acceptance after each milestone. After all planned milestones are implemented and delivered, run the final cross-milestone Integration Review, UAT Prep and UAT. UAT consumes the milestone plan and creates milestone-to-user-story acceptance coverage. If later UAT/Fix/Check remediation changes source, that change receives its own normal versioned delivery; no version-only final bump is created when the last milestone already represents the final source state.


At the delivery stage, run the five-field proof gate in `MAIN_DELIVERY_STANDARD.md`. Auto must attempt the required version bump, version-prefixed source commits, remote branch push, PR and authorized merge, then independently read back remote `main`. Preserve milestone-based version reconciliation: one delivery version per completed value milestone, never one per lifecycle stage/task/slice. The terminal delivery gate verifies the final goal state and does not add a version-only bump when the latest verified milestone/main already contains the final source. Include each field's evidence in `DELIVERY_REPORT.md`, the historical `90-delivery/HANDOFF.md`, and the terminal lifecycle board. No success wording while any field is not PASS; never interpret an open PR as complete. Existing checks, hooks and enforced reviews remain binding.


## Initial debug-widget implementation gate

**Immediately after Preflight and before treating Capture/Plan artifacts as reusable**, read `DEBUG_WIDGET_READINESS.md` for the current candidate and verify every applicable surface against `DEBUG_DIAGNOSTICS_STANDARD.md`. Missing or stale evidence must be repaired by inspection, not silently marked passed. Put functional failures into the authorized workstream implementation plan: wrong placement, visible commit/date, oversized buttons, absent diagnostic event collection, fake clipboard/checkmark, fake cache clear, missing logout/cookie invalidation, missing tests. Implement and regression-test these defects within the authorized goal before UAT/Check; recheck them after integration because later UI work can regress shared mounts. Preserve safe authorization/redaction and avoid browser-wide cache claims. If a defect is out of scope of the specifically authorized goal, report it explicitly as an unresolved gate; never call the app fully PHDK-compliant.
