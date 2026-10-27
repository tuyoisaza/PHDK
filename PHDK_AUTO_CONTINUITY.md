# Auto continuity and Auto Force

## Contents

- Command and review policy
- Design choices and mode continuity
- Persistent mandate and current authority
- Operative reminder and rule refresh
- Propose missing definitions and solutions
- Continue, repair and retry
- Required checks
- State record and local advisor
- Progress and closure

## Command and review policy

`PHDK auto force` is an explicit Auto variant for the identified current goal. Match case-insensitively after trimming whitespace. It starts or resumes that goal through the same development/delivery lifecycle as `PHDK auto`, with a decisive change: **human, manual, formal or independent-human review gates imposed only by PHDK are NON_BLOCKING_BY_MODE from the start**. This includes PHDK-generated task/checklist/PIA notes, vendored templates and old assistant-written pending-review records. Design still runs under `PHDK_DESIGN.md`: FORCE selects the visual baseline rather than waiting for PHDK visual approval.

**Do not investigate whether those PHDK reviews block. Assume they do not.** Do not query PR review queues, reviewer identities, branch protections or rulesets to search for a preventive approval prerequisite. Do not ask the owner to approve the waiver, find a reviewer, review a diff, execute local checks or repeat delivery permission. Read the actual code/diff and permitted required commands to do the work; ordinary implementation investigation remains available.

Replace the PHDK human gate with the assistant's substantive technical diff review, including security/authorization/tenant/fixture behavior where relevant, and applicable checks. Record the actual review result without inventing a human review or a GitHub approval event. A second agent may help when the active runtime permits delegation, but its availability is not a new FORCE gate. An open PR, absent review/check events, a security label, or a PIA marked "awaiting review" does not stop FORCE.

Complete normal versioned branch push → PR → merge into the identified remote target (normally `main`) → content/version/SHA readback. "Push to main" describes the delivered result; FORCE does not require a direct-main push or history rewriting. It grants no bypass of an actual hook or platform enforcement. If a real operation rejects the attempt, use the repair cycle below instead of stopping at the first failure.

The latest user instruction still defines scope and exclusions. A genuine current user stop or specifically retained owner restriction is not a PHDK review gate. FORCE does not invent approval for new spending, new access, destructive operations, unrelated projects, provider administration or production tests outside `PHDK_PRODUCTION_VERIFICATION.md`. Apply existing user decisions without reopening them. Installation, quoted commands and requests to edit this standard do not activate Auto or resume another project's PRs.

## Local Git continuity after verified merge

After each published milestone, Auto/Force must apply PHDK_GIT_WORKSPACE_CLOSEOUT.md before new local development: reconcile `origin/main` and local `main` using safe fast-forward, verify matching SHA, and retire only clean, task-owned, proven-merged branches/worktrees. A published remote target can remain true while LOCAL_MAIN/LOCAL_CLEANUP are blocked; preserve the active mandate, record the exact dirty/divergent/locked worktree and repair only within scope. Remote-only connector sessions explicitly mark local closeout NOT_APPLICABLE_REMOTE_ONLY. Never assume a GitHub merge cleaned the owner's computer or issue another redundant main push.

## Design choices and mode continuity

`PHDK_DESIGN.md` is the specific product-input exception to ordinary Auto's generic no-stage-approval/no-interview wording. Stage **25-design** follows technical/content Plan and precedes dependent UI implementation. **Auto asks one unresolved visual question at a time and waits for the owner's selection/preview approval. Auto Force compares alternatives, chooses, records `AGENT_SELECTED_AUTO_FORCE` with rationale and continues.** Neither mode may fabricate owner approval or runtime visual evidence. Reuse valid prior owner choices instead of repeating the interview.

A pending ordinary design choice is `design_choice`, not `phdk_human_review`, `real_failure`, or a new security/scope decision. Keep the Design selection as a pending `work` step and make dependent UI steps depend on it. Record the current options/preview evidence, source, observation time and single next unanswered question. Normal Auto reports stage BLOCKED with reason `DESIGN_AWAITING_OWNER`; it retains the active mandate and performs independent authorized work without implementing the dependent UI. The owner's answer resumes the same goal, not a fresh development authorization.

In FORCE, the advisor returns a concrete selection action instead of an owner wait. Perform that selection, record the chosen baseline/assets and limitations in `UX_UI_DECISIONS.md`, resolve the blocker and only then mark the Design work step done. Do not jump directly to UI implementation merely because the human wait was removed. A valid agent-selected baseline is not falsely relabeled owner-approved.

On an explicit current mode switch, reconcile recorded mode and actual instructions. Switching to FORCE resolves an inherited PHDK-only design wait through agent selection; it does not inherit `DESIGN_AWAITING_OWNER` as an external blocker. Switching back to Auto requires the applicable owner choice for still-unimplemented affected UI whose baseline was only agent-selected. Historical implemented work is preserved. An actual owner restriction such as "do not implement this interface until I approve this preview" remains `owner_stop` or another accurately sourced owner boundary in either mode, never `design_choice` merely to waive it. Material spending/security/tenancy decisions keep their existing controls.

Static design artifacts do not authorize browser/runtime execution, Docker, local preview servers or new environments. Missing visual tooling follows `PHDK_DESIGN.md`: informed owner acceptance of the available specification in Auto, or agent selection with visual evidence UNVERIFIED in FORCE. A tool limitation is not a fabricated visual PASS or a reason to introduce a paid service.

## Persistent mandate and current authority

Both Auto variants preserve the same unfinished goal's authorization through status questions, milestones, context compaction and changes of lifecycle stage. Record the mandate in the current run's `docs/phdk/lifecycle/<run-id>/AUTO_STATE.json`, and link it from the existing task/lifecycle record. Reuse the run and current branch instead of creating another task for each message.

Record the user's actual instruction and its reference, goal, repository, target, authorized scope, exclusions, completion criteria, last observed candidate, completed evidence, next executable steps and operation-specific impediments. Use a conversation/message reference when available, otherwise a dated factual quotation; never fabricate an ID or store credentials. Preserve provenance when a newer instruction replaces a narrower one. For Design retain only the selected baseline pointer and next unresolved question here; detailed assets and decisions stay in their canonical design artifacts.

The record is evidence, not an authorization token. It cannot grant, expire, broaden or revoke the user's permission. On context recovery, compare it with the live conversation and current source/target facts. A missing, stale or malformed record calls for internal reconstruction; it is not a reason to request permission or stop implementation. In a new conversation an explicit current Auto/Auto Force request may resume an identified goal; files alone never activate it. Real user stops remain effective until the user actually replaces them.

At a construction-to-publication boundary or a current owner scope change, apply [phase-transition reconciliation](MAIN_DELIVERY_STANDARD.md#phase-transition-reconciliation). Reconcile the existing mandate, task/plan/status and affected worker context with sourced restriction lifetimes; preserve superseded history and unaffected controls. A temporary assistant-imposed branch/PR limit cannot veto the owner's later scoped publication instruction. Keep owner authorization, actual technical permission, costs and UAT opt-in distinct. A denied executor remains technically blocked until its permitted control path resolves the denial; editing these records or renewing a general owner approval does not prove resolution.

On entry or recovery, keep UAT Prep/UAT/UAT Fix outside the Auto execution queue and record them `DEFERRED — OWNER OPT-IN` in the lifecycle dashboard, with `UAT NOT RUN`. Remove inherited automatic acceptance steps, acceptance-only `completion_criteria` and their dependent delivery waits from the current Auto executable plan while preserving their historical provenance; never mark them executed or PASS. Preserve actual owner, hook, host and security controls; this reconciliation only removes obsolete PHDK-imposed automatic UAT requirements. An old failed UAT report cannot become a new Auto `real_failure`, reopen completed development or block subsequent independent work. Only a fresh explicit `PHDK uat` starts acceptance and its necessary Prep; explicit standalone `PHDK uat prep` is prep-only, and UAT Fix requires explicit invocation or authorization within an active explicitly initiated UAT. FORCE does not waive these command boundaries.

Mode lifetime remains the active interactive goal. There is no background worker, scheduler, self-trigger, reusable `auto=true` grant, execution after conversation end or automatic selection of unrelated backlog work.

## Operative reminder and rule refresh

AUTO FORCE carries its operating instructions into the active context through the mandatory reminder in `PHDK_COMMUNICATION_STANDARD.md`. Apply it at start/resume, in every substantive progress update, after a partial delivery and before a question or blocker report. The reminder covers the current mandate, reloading relevant rules, reconciling inherited blockers, finding solutions, proposing what is missing and executing the next authorized action. The user does not need to append "keep going", "refresh the rules" or "propose it" to the command.

At entry/recovery and before treating a gap as a reason to ask or stop, reread the current Auto Force/communication contract and relevant domain rule, reconcile with the latest user instruction, and discard obsolete interpretations or restrictions invented by the agent. This short refresh does not rerun the full preflight or rescan every standard at each message. In progress updates keep the operative reminder visible; use newly relevant source when needed. A rule refresh preserves actual user restrictions and host controls. PHDK-only human reviews remain nonblocking immediately, without investigating their approval history or protections. For Design, use the current mode's decision policy rather than a stale assistant-created owner wait.

Before a proposed interruption ask internally: **Does this impediment affect the entire goal or only particular operations? What can I implement, repair, define or prepare now within the current mandate?** Execute an eligible action when one exists. A partial delivery updates progress and is followed by the next in-scope task; writing its report does not close the goal. Ordinary Auto's actual unanswered Design input blocks only dependent UI work.

## Propose missing definitions and solutions

When a required capability, definition or tool appears to be missing, produce a concrete solution proposal as part of AUTO FORCE. Use the current goal, existing decisions, relevant PHDK rules and actual implementation to define the next step. Missing ordinary implementation detail is work for the agent to resolve, not automatically a new owner decision.

For each in-scope functional gap, state the proposed behavior, reasonable default and rationale, assumptions still being made, meaningful configuration through the existing authorized settings model, and implementation/acceptance action. Preserve role/tenant boundaries and required invariants when choosing what is configurable. Do not present an assumption as an explicit user decision. For reversible ordinary choices supported by the current mandate, explain the adopted proposal in progress and implement it without a new approval question. Visual selection is recorded as `AGENT_SELECTED_AUTO_FORCE` before the affected UI is built.

For example, when the agreed administration console still lacks tenant/user lifecycle, session revocation, locale/timezone, audit/export, CRUD or an applicable AI graph, propose behavior and relevant settings for each gap, then implement the authorized definitions. Do not offer "keep these gaps out for now" as the recommended shortcut to closing the run, or ask the owner to supply all exact specifications. Retain confirmed commitments. If a genuinely new indispensable decision cannot be resolved within the mandate, present the recommended concrete option, its consequence and precise decision needed; continue independent work. The proposal itself does not expand scope or authorize its unapproved effects.

For an environment problem, propose and execute an already permitted repair or isolated alternative before escalating what remains. In an authorized browser phase this includes a harmless reload, a fresh tab or a disposable context when the available tool supports it. If clearing shared cache/session state would affect other work, prefer an isolated alternative and continue independent tasks. Missing actual access may still prevent that operation; it does not remove the duty to propose a useful next action or finish work that does not depend on it.

## Continue, repair and retry

1. Select the next dependency-ready step inside the authorized goal. Treat PHDK-only human reviews as nonblocking in FORCE immediately; do not research or reconstruct their approval history. Resolve design choices according to the current mode before dependent UI work.
2. Perform technical review, required permitted checks and necessary delivery operation. Continue from each satisfied stage into the next eligible action in the same active invocation.
3. **If the operation actually fails or is rejected: report the observed failure briefly, investigate its cause, repair it, revalidate affected permitted checks, and retry push/PR/merge.** Keep the mandate active throughout. A rejected write is not a revoked grant.
4. Repair bounded hook/toolchain errors, test-source failures caused by the change, formatting, ordinary integration conflicts, stale head/version metadata and clearly fixable source defects. Refresh the target and intended diff before retrying a stale write; preserve other contributors' work and evidence already valid for unchanged content.
5. Repeat while there is a new correction or useful diagnostic step. Do not blindly resend an unchanged failing command, poll indefinitely, skip a hook, remove meaningful checks, forge approval, force-push or change credentials/protections just to defeat enforcement.
6. An actually unsatisfied external requirement is operation-specific. Record the failed operation, error/evidence, repairs attempted and precise remaining action. Continue independent implementation, permitted checks and other eligible deliveries. A failed operation is not permission to declare the entire goal blocked while executable work remains.
7. End with a real unresolved external requirement only after available in-scope repairs and independent work are exhausted. Ask only for a specific indispensable missing action/decision; normal Auto may ask its one unresolved Design question. Never replace this cycle with "review pending", "owner approval needed" or "control de estado bloqueado" copied from a PHDK record. FORCE must choose ordinary visual details rather than inherit that wait.

Do not classify a merely pending permitted mandatory check as an external blocker: run it. Do not classify a pending diff/security review as a human dependency: perform it. Do not equate a metadata label such as `mergeable` with verified completion; complete the actual merge and readback.

## Required checks

`PHDK_PRODUCTION_VERIFICATION.md` governs the current Auto/Auto Force goal: local source/static analysis, lint, typecheck, formatting and safe builds are permitted; local unit/in-process/mock/runtime tests, Docker, local application servers and new staging/databases are not. Inspect actual commands and side effects. Do not invent application commands in the standards repository or treat a command's name as proof that it is static.

When a build, packaging check or Git hook has ambiguous effects or conflicts with local verification policy, load and apply the [decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) **before executing the command, declaring BLOCKED, or requesting user input**. Inspect the actual command chain and provenance; run permitted static steps and repair only proven PHDK-managed or legacy PHDK-generated steps within the authorized task. Preserve independent owner/external/unknown controls and prepare a concrete gate-change proposal if authorization is missing. Never request a prohibited local-runtime exception or initiate UAT to satisfy the gate.

No separate approval is needed for permitted required checks. Avoid redundant full cycles after each stage; perform applicable diagnostics and mandatory controls at the operation they govern. Behavioral acceptance is not an Auto check. It requires a separate explicit `PHDK uat` and then uses only the authorized deployed candidate, safe run-owned synthetic data and verified cleanup. After the decision procedure, an unresolved actual mandatory hook remains an operation-specific blocker; do not bypass it, execute the excluded operation or report PASS. Continue independent permitted work with the exact gate, provenance and proposed resolution recorded. Failures of permitted checks enter the repair/revalidate/retry cycle. Static analysis of the advisor's source is not an executed behavioral regression test.

## State record and local advisor

Use one factual JSON record, not multiple competing authorization ledgers. Keep existing domain task/commitment reports as their own sources of progress; reference them rather than copying the whole project into this file. The minimal structure remains schema version 1:

```json
{
  "schema_version": 1,
  "run_id": "2026-10-17-current-goal",
  "mode": "auto_force",
  "repository": "owner/project",
  "target_branch": "main",
  "goal": "The currently requested outcome",
  "candidate_ref": "Observed branch SHA or dated working-copy checkpoint",
  "authorization": {
    "source_ref": "Actual current user message or dated quotation reference",
    "instruction": "Actual user instruction, without secrets",
    "scope": ["Confirmed implementation and normal delivery"],
    "restrictions": [],
    "status": "active"
  },
  "completion_criteria": ["Requested behavior verified on remote main"],
  "steps": [
    {
      "id": "delivery",
      "kind": "delivery",
      "status": "pending",
      "action": "Push the verified branch, open its PR and merge to main",
      "depends_on": [],
      "blocked_by": ["old-phdk-review"]
    }
  ],
  "blockers": [
    {
      "id": "old-phdk-review",
      "kind": "phdk_human_review",
      "reason": "A PHDK-generated task previously asked for human review"
    }
  ]
}
```

This is an illustrative record, not evidence of executed work. Add real `review_diff` and `required_check` steps when pending; completed steps need observed `evidence`. Step kinds are `work`, `review_diff`, `required_check`, `delivery`, `verify_delivery`; statuses are `pending`, `running`, `blocked`, `done`. Dependencies and `blocked_by` entries reference IDs in the same record. The advisor keeps unfinished diff/check steps before delivery even if a dependency was omitted. Only permitted non-UAT checks belong in this Auto list; deferred acceptance phases are reported in the lifecycle dashboard rather than inserted as pending checks, delivery dependencies or unresolved blockers. The helper does not grant permission merely because an action string appears in saved state.

For Design, add a `work` step such as `design-select` and make affected UI steps depend on it. A pending choice is a blocker with `kind: design_choice`, actual `reason`, `source_ref`, `evidence`, `observed_at`, and `next_action` containing the single current question. It does not need fictional failed `resolution_attempts`: intentional owner input is not a technical failure. A done step cannot retain an unresolved `design_choice` blocker. Remove resolved references only after recording the actual owner choice or FORCE agent selection and keep prior observations in history.

Blocker kinds:

| Kind | Meaning and action |
|---|---|
| `phdk_human_review` | In FORCE, `NON_BLOCKING_BY_MODE` immediately, with no source lookup or approval research. Perform actual technical diff review and delivery. Do not use this kind for a visual choice. |
| `design_choice` | Ordinary visual input under `PHDK_DESIGN.md`: Auto waits for one owner answer with reason `DESIGN_AWAITING_OWNER`; FORCE returns an action to select and record `AGENT_SELECTED_AUTO_FORCE` before dependent implementation. Never use it to erase an actual owner restriction. |
| `real_failure` | An observed failing operation. Record `failed_operation`, `evidence`, `observed_at` and next `repair_action` when known. Diagnose/repair/revalidate/retry; never stop merely because this entry exists. |
| `external_dependency` | Actual unmet external requirement after attempted repairs. Record `source_ref`, `evidence`, `observed_at`, `resolution_attempts` and precise `next_action`. It blocks only affected steps. |
| `owner_decision` | A genuinely new indispensable scope/security decision not resolved by current instructions. Record the same evidence fields and finish independent work. A PHDK review or routine FORCE visual choice is never this kind merely to stop execution. |
| `owner_stop` | A genuine user stop on the affected operation, with actual provenance and the same evidence fields. Never relabel it as a PHDK gate or design_choice to erase it. |

Authorization status is `active`, `paused`, `revoked` or `completed`, describing actual user/task facts. Never mark a rejected push or a pending Design answer as revoked. Remove resolved blocker references from steps; keep prior observations in the run's history. The additive `design_choice` kind requires the corresponding current vendored advisor; an older advisor's schema error calls for bounded standards/state reconciliation, never a fabricated choice.

When permitted and useful, the static-state advisor can inspect the factual record synchronously:

```bash
python phdk-standards/scripts/phdk_auto_gate.py --state docs/phdk/lifecycle/<run-id>/AUTO_STATE.json --mode auto_force
```

Use `scripts/phdk_auto_gate.py` directly in the PHDK source repository. Supply mode from the current active instruction, never infer authority from a saved mode. The advisor makes no network calls, queries no reviews/protections, runs no external commands and changes no state. Its dispositions remain `CONTINUE`, `REPAIR_AND_RETRY`, `REPAIR_STATE`, `WAITING_EXTERNAL`, `VERIFY_DELIVERY` and `STOPPED`. For ordinary Auto's Design input, `WAITING_EXTERNAL` carries reason `DESIGN_AWAITING_OWNER`; this means a user answer, not a technical failure. Independent work is returned as executable while the choice remains waiting. FORCE returns the selection action, never a skip-design instruction. Multiple otherwise ready Design choices are presented one at a time.

`REPAIR_STATE` means fix bookkeeping internally and continue, not wait for approval. This helper is not a hook, publication prerequisite, permission grant, product runtime test or proof of owner approval. If unavailable or execution is excluded by current controls, apply this contract directly. Do not run behavioral/unit tests of the helper locally contrary to `PHDK_PRODUCTION_VERIFICATION.md`.

`VERIFY_DELIVERY` does not mean COMPLETED. Use `PHDK_COMPLETION_GATE.md` for real remote target/content/version evidence; its generic review wording never restores a PHDK human gate in FORCE. The record and advisor cannot detect a fabricated observation or substitute for real checks, selected design evidence or current user instructions.

## Progress and closure

In every substantive AUTO FORCE progress update include the operative continuation cue from `PHDK_COMMUNICATION_STANDARD.md`:

```text
AUTO FORCE activo · autorización vigente para [objetivo/alcance].
RECORDATORIO: recargar las reglas vigentes, reconciliar bloqueos heredados, buscar soluciones y proponer lo que falte.
SIGUIENTE PASO: [acción concreta]. Continúo con el trabajo autorizado.
```

The reminder is an instruction to apply, not a claim that a reread, repair or proposal already happened. Report completed actions only with actual evidence. Normal Auto retains its mandate/next-action cue. Execute the stated eligible action in the same invocation; do not end the turn with a promise to continue while permitted work is ready. On a rejection the next action is diagnosis/repair/retry. When a definition is missing, propose and resolve what can be decided inside the current mandate before asking about a remaining indispensable decision. For normal Auto awaiting Design input, state the actual question and waiting condition, not a claim that dependent coding continues.

At actual development completion report the verified result and target link, the actual `DEVELOPMENT COMPLETE` / `PARTIALLY DELIVERED` / `BLOCKED` outcome, and `UAT NOT RUN` separately. Offer optional future `PHDK uat` without waiting for an answer as a delivery gate. Mark the development goal complete only from its required evidence; do not claim an active mandate to start unrelated work. On a genuine user stop, exhausted external dependency or required normal Auto Design input, report the factual limitation and one precise resume action/question. Preserve the existing PHDK version, lifecycle and final-link contract without repeating long permission prose.
