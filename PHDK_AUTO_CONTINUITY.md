## Universal test budget and carryover (v3.4.0)

Use one bounded local profile from `PHDK_TEST_AUTOMATION_STANDARD.md` to verify a milestone without spending chat allowance re-running every case. Persist only the latest relevant report path, candidate SHA, actual failures/untested risks and necessary next fix in existing Auto state. Failed checks do not reset delivery_watch or justify an indefinite repair loop. Hermetic unit/contract tests are permitted locally; live application/browser/provider/UAT remains separately explicit-only.

# Auto continuity and Auto Force

## Delivery stop-loss across sessions (v3.3.0)

Apply `PHDK_DELIVERY_STOP_LOSS_STANDARD.md` before new Auto/Force work and at handoff. Maintain `delivery_watch` within existing schema-v1 AUTO_STATE with real git/PR source, active milestones, product/PHDK file counts and cumulative foreground minutes without verified merge. The read-only advisor returns `FOCUS_DELIVERY`, `RECOVER_DELIVERY` or `DELIVERY_STOP_LOSS`: focus on completion, safely integrate existing code or end speculative allowance consumption with an exact preserved-code/branch/blocker handoff. New conversations, PHDK upgrades, commits and draft PRs do not reset the window. Missing fields are internal REPAIR_STATE; provider allowance is UNKNOWN unless observed.

## Post-UAT Export Modules continuity (v2.91.0)

Keep only material reusable observations in Auto's existing retrospective and preserve source revision in the normal delivery handoff. Do not scan modules or launch UAT on a session boundary. When the owner later explicitly starts UAT, its accepted revision controls a separate read-only post-UAT review under `PHDK_POST_UAT_EXPORT_STANDARD.md`; the stable review key prevents duplicate proposals. A historical state file never authorizes UAT, code publication, or resuming an export task.

**Document context at resume (v2.73.0):** When reloading `AUTO_STATE.json`, resolve active versioned intent, brief, ADR and plan artifacts through `docs/INDEX.md` under [PHDK_DOCUMENTATION_STANDARD.md](PHDK_DOCUMENTATION_STANDARD.md). Store links/IDs and the observed revision in the existing state/handoff rather than copying entire documents or launching a new task. A stale/missing legacy index is a recoverable documentation gap, not a new permission or a reason to restart Capture.


## Bounded work sessions

One authorized goal may need several foreground conversations. At entry record a stable session identifier and start time in the existing run state. Preserve both through messages, compaction, worktree/worker changes and mode switches. Before dispatching or beginning any new slice, after a milestone or tool wait, and after a context warning, compare the trustworthy clock, remaining work and expected closeout cost. Use four hours per session as the default ceiling. Honor a shorter owner/host limit. Start closing at the last safe checkpoint if the next slice plus publication, readback and handoff would not fit. Close early for material context pressure, repeated reconstruction, or unreliable session history. Unknown timing is a reason for an early safe handoff. The elapsed session clock is independent of PMO human-workday estimates.

When the boundary is due, end assignment of new work in both modes. Collect and stop owned workers safely, preserve in-flight operations and record unfinished details. Finish an already authorized coherent milestone through its normal PR, remote main readback and bounded production readback under `PHDK_DEPLOYMENT_VERSION_STANDARD.md` for an applicable service if feasible within the boundary. A partial milestone stays on the owned branch or draft PR. Never force a release to satisfy the timer or leave a worker running. If remote writes are unavailable, provide a portable scoped handoff/patch when authorized, explain what is local-only and leave merge/deployment unverified. Respect an explicit stop immediately. Honor any ban on further writes and present only permitted existing evidence. A handoff keeps the outstanding goal open and doesn't grant fresh conversation authority.

The existing advisor reads the additive `session` object in schema v1. Use the same `id` and timezone-qualified ISO `started_at` throughout this conversation. Optional `budget_minutes` is 1–240 (default 240), `next_slice_minutes` is the current work estimate, and `closeout_minutes` reserves time for delivery and handoff (default 15). Set `close_early` for context pressure or unknown timing and `closed` at handoff. The advisor returns `SESSION_HANDOFF` before dispatch when due. On a legacy record, reconstruct the original start from observed history, or set `close_early` and close immediately. Only an actual new owner-invoked conversation enters another session under this run. Do not reset the clock to repair an old record.

### Session close package

Use `docs/phdk/lifecycle/<run-id>/sessions/<NN>/HANDOFF.md` for each closure, with `status.json` and `board/status-01.svg` in that same numbered folder. From the active TASK, plan, milestone ledger, current AUTO_STATE and observed delivery evidence, produce a short HANDOFF.md, a derived status snapshot and the standard status image. Stage these artifacts in the current authorized change or checkpoint them on the owned working branch. Include the handoff prompt text in HANDOFF.md and in the final reply. Add the verified URLs in the reply once the branch or merge SHA is known. For facts observed after merge, supply real links in the response with optional existing evidence records; do not cause another release just to record its own SHA. Link these artifacts in the current run record. Retain prior session folders when advancing to the next session. Redact credentials, provider secrets, tenant data and private URLs beyond the project's permitted audience.

For the image, use the vendored `scripts/phdk_session_status.py SNAPSHOT.json OUTPUT_DIR` with a new/empty output directory. Use the [sample JSON](examples/session-status.example.json) and [design](docs/images/session-status/v1/session-status.example.svg). The output is one or more accessible 1920×1080 SVGs. Show page one inline and provide all pages. If the host needs bitmap images, convert with an available offline renderer. With image or write tools unavailable, deliver the full textual equivalent plus the portable source when available and state which output could not be rendered/saved. Map each actual roadmap milestone to DONE (green), IN_PROGRESS (yellow), PENDING (red) or BLOCKED (red labeled), in plan order. Tie the active-work panel to its milestone IDs. The image shows the session, goal, current work, confirmed configuration names/status, next steps and separate publication, deployment and acceptance evidence. Missing proof stays unverified. Deferred UAT is not a failed milestone. Do not silently discard overflow. The same board also closes completed, blocked or stopped sessions where permitted.

When work remains on rollover, deliver one directly copyable text block in the owner's language. Place the original unquoted mode on its own first line. Treat the rest of that owner-sent message as the scoped brief. Fill every applicable slot with actual observed values and absolute repository URLs, including inside the block; name unavailable artifacts. Local paths alone do not suffice in a different workspace.

```text
PHDK auto
Resume [goal] in [repository URL]. Use run [run ID]. Preserve [scope, target and exclusions].
Start from [handoff URL at actual branch or immutable ref]. Read [TASK URL], [active intent/index and plan URLs],
[milestone ledger URL] and [AUTO_STATE URL]. Board: [status image URLs].
At close: [completed milestone + PR/main SHA/link]; [current milestone, partial branch/PR and revision];
[deployment proof or exact reason unverified]; [acceptance status]. [Configuration established and limits].
Remaining: [milestone IDs]. The first next action is [concrete task]. [Blockers and applicable constraints].
Recheck current main, candidate branch and PR before writing. Reuse verified work, reconcile changes
since the checkpoint and honor the active session handoff standard.
```

Use `PHDK auto force` on line one only if that mode applies. At rollover explicitly say that execution in this conversation has stopped. Ordinary replies, compaction, and a newly spawned worker do not start another session. In a fresh conversation the owner's pasted instruction activates the indicated scope. Verify current remote state, reconcile drift and actual authority, retain the run and start a new session clock. A historical file or copied quotation alone never triggers work. When the goal is complete, present its final board and real delivery evidence with no fabricated next task.

## Contents

- [Bounded work sessions](#bounded-work-sessions)
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

## Historical and remote branch continuity

Within a currently initiated Auto/Force run, perform the bounded historical **local-only** Git inventory once after adoption and retain unresolved local candidates in `.git/phdk/git-hygiene-state.json`. After every verified PR merge, synchronize local main and retire only independently proven integrated, clean **local** branches/worktrees. GitHub remote branches are read-only evidence and intentionally retained (`REMOTE_BRANCH=RETAINED_BY_POLICY`) even if merged. Retention never blocks continuation or completion. GitHub-only agents mark local cleanup NOT_APPLICABLE_REMOTE_ONLY; they must not claim to clean the user's PC or delete remote refs.

## Design choices and mode continuity

`PHDK_DESIGN.md` is the specific product-input exception to ordinary Auto's generic no-stage-approval/no-interview wording. Stage **25-design** follows technical/content Plan and precedes dependent UI implementation. **Auto presents one complete coded visual/motion choice map, recommended bundle and combined preview for a single approve-all/override owner answer. Auto Force compares alternatives, chooses, records `AGENT_SELECTED_AUTO_FORCE` with rationale and continues.** Neither mode may fabricate owner approval or runtime visual evidence. Reuse valid prior owner choices instead of repeating the interview.

A pending ordinary design choice is `design_choice`, not `phdk_human_review`, `real_failure`, or a new security/scope decision. Keep the Design selection as a pending `work` step and make dependent UI steps depend on it. Record the decision-map revision, pending codes, recommendation bundle, combined preview/transition storyboard evidence or limits, source, observation time and **one next approve-all/override request**. Normal Auto reports stage BLOCKED with reason `DESIGN_AWAITING_OWNER`; it retains the active mandate and performs independent authorized work without implementing the dependent UI. The owner's answer resumes the same goal, not a fresh development authorization.

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

Before a proposed interruption ask internally: **Does this impediment affect the entire goal or only particular operations? What can I implement, repair, define or prepare now within the current mandate?** Execute an eligible action when one exists. Within an open session, a partial delivery updates progress and is followed by the next in-scope task; writing its report does not close the goal. Ordinary Auto's actual unanswered Design input blocks only dependent UI work.

## Propose missing definitions and solutions

When a required capability, definition or tool appears to be missing, produce a concrete solution proposal as part of AUTO FORCE. Use the current goal, existing decisions, relevant PHDK rules and actual implementation to define the next step. Missing ordinary implementation detail is work for the agent to resolve, not automatically a new owner decision.

For each in-scope functional gap, state the proposed behavior, reasonable default and rationale, assumptions still being made, meaningful configuration through the existing authorized settings model, and implementation/acceptance action. Preserve role/tenant boundaries and required invariants when choosing what is configurable. Do not present an assumption as an explicit user decision. For reversible ordinary choices supported by the current mandate, explain the adopted proposal in progress and implement it without a new approval question. Visual selection is recorded as `AGENT_SELECTED_AUTO_FORCE` before the affected UI is built.

For example, when the agreed administration console still lacks tenant/user lifecycle, session revocation, locale/timezone, audit/export, CRUD or an applicable AI graph, propose behavior and relevant settings for each gap, then implement the authorized definitions. Do not offer "keep these gaps out for now" as the recommended shortcut to closing the run, or ask the owner to supply all exact specifications. Retain confirmed commitments. If a genuinely new indispensable decision cannot be resolved within the mandate, present the recommended concrete option, its consequence and precise decision needed; continue independent work. The proposal itself does not expand scope or authorize its unapproved effects.

For an environment problem, propose and execute an already permitted repair or isolated alternative before escalating what remains. In an authorized browser phase this includes a harmless reload, a fresh tab or a disposable context when the available tool supports it. If clearing shared cache/session state would affect other work, prefer an isolated alternative and continue independent tasks. Missing actual access may still prevent that operation; it does not remove the duty to propose a useful next action or finish work that does not depend on it.

## Continue, repair and retry

1. Select the next dependency-ready step inside the authorized goal. Treat PHDK-only human reviews as nonblocking in FORCE immediately; do not research or reconstruct their approval history. Resolve design choices according to the current mode before dependent UI work.
2. Perform technical review, required permitted checks and necessary delivery operation. Before the next eligible action, check the bounded session. Continue only while it remains open.
3. **If the operation actually fails or is rejected: report the observed failure briefly, investigate its cause, repair it, revalidate affected permitted checks, and retry push/PR/merge.** Keep the mandate active throughout. A rejected write is not a revoked grant.
4. Repair bounded hook/toolchain errors, test-source failures caused by the change, formatting, ordinary integration conflicts, stale head/version metadata and clearly fixable source defects. Refresh the target and intended diff before retrying a stale write; preserve other contributors' work and evidence already valid for unchanged content.
5. Repeat while there is a new correction or useful diagnostic step. Do not blindly resend an unchanged failing command, poll indefinitely, skip a hook, remove meaningful checks, forge approval, force-push or change credentials/protections just to defeat enforcement.
6. An actually unsatisfied external requirement is operation-specific. Record the failed operation, error/evidence, repairs attempted and precise remaining action. Continue independent implementation, permitted checks and other eligible deliveries. A failed operation is not permission to declare the entire goal blocked while executable work remains.
7. End with a real unresolved external requirement only after available in-scope repairs and independent work are exhausted. Ask only for a specific indispensable missing action/decision; normal Auto may ask its one unresolved Design question. Never replace this cycle with "review pending", "owner approval needed" or "control de estado bloqueado" copied from a PHDK record. FORCE must choose ordinary visual details rather than inherit that wait.

Do not classify a merely pending permitted mandatory check as an external blocker: run it. Do not classify a pending diff/security review as a human dependency: perform it. Do not equate a metadata label such as `mergeable` with verified completion; complete the actual merge and readback.

## Required checks

`PHDK_PRODUCTION_VERIFICATION.md` and `PHDK_TEST_AUTOMATION_STANDARD.md` govern this Auto/Force goal: local source/static analysis, lint, typecheck, formatting, safe builds and inspected bounded hermetic unit/contract/in-process tests are permitted; local app servers, databases, network/browser/provider probes and acceptance are prohibited outside separately explicit UAT.

When a build, packaging check or Git hook has ambiguous effects or conflicts with local verification policy, load and apply the [decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) **before executing the command, declaring BLOCKED, or requesting user input**. Inspect the actual command chain and provenance; run permitted static steps and repair only proven PHDK-managed or legacy PHDK-generated steps within the authorized task. Preserve independent owner/external/unknown controls and prepare a concrete gate-change proposal if authorization is missing. Never request a prohibited local-runtime exception or initiate UAT to satisfy the gate.

No separate approval is needed for permitted required checks. Avoid redundant full cycles after each stage; perform applicable diagnostics and mandatory controls at the operation they govern. Behavioral acceptance is not an Auto check. It requires a separate explicit `PHDK uat` and then uses only the authorized deployed candidate, safe run-owned synthetic data and verified cleanup. After the decision procedure, an unresolved actual mandatory hook remains an operation-specific blocker; do not bypass it, execute the excluded operation or report PASS. Continue independent permitted work with the exact gate, provenance and proposed resolution recorded. Failures of permitted checks enter the repair/revalidate/retry cycle. Static analysis of the advisor's source is not an executed behavioral regression test.

## State record and local advisor

Use one factual JSON record, not multiple competing authorization ledgers. Keep existing domain task/commitment reports as their own sources of progress; reference them rather than copying the whole project into this file. The minimal structure remains schema version 1:

```json
{
  "schema_version": 1,
  "session": {"id": "01", "started_at": "2026-10-17T09:00:00Z"},
  "run_id": "2026-10-17-current-goal",
  "mode": "auto_force",
  "repository": "owner/project",
  "target_branch": "main",
  "goal": "The currently requested outcome",
  "candidate_ref": "Observed branch SHA or dated working-copy checkpoint",
  "delivery_watch": {"window_started_at": "2026-10-17T09:00:00Z",
    "active_minutes_before_session": 0, "active_milestones": ["MS-001"],
    "product_files_pending": 0, "standards_files_pending": 0,
    "nonprogress_cycles": 0, "observed_source": "actual git/PR snapshot"},
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

Use `scripts/phdk_auto_gate.py` directly in the PHDK source repository. Supply mode from the current active instruction, never infer authority from a saved mode. The advisor makes no network calls, queries no reviews/protections, runs no external commands and changes no state. Its dispositions include `FOCUS_DELIVERY`, `RECOVER_DELIVERY`, `DELIVERY_STOP_LOSS`, `SESSION_HANDOFF`, `CONTINUE`, `REPAIR_AND_RETRY`, `REPAIR_STATE`, `WAITING_EXTERNAL`, `VERIFY_DELIVERY` and `STOPPED`. For ordinary Auto's Design input, `WAITING_EXTERNAL` carries reason `DESIGN_AWAITING_OWNER`; this means a user answer, not a technical failure. Independent work is returned as executable while the choice remains waiting. FORCE returns the selection action, never a skip-design instruction. Multiple otherwise ready Design choices are presented one at a time.

`REPAIR_STATE` means fix bookkeeping internally and continue, not wait for approval. This helper is not a hook, publication prerequisite, permission grant, product runtime test or proof of owner approval. If unavailable or execution is excluded by current controls, apply this contract directly. Do not run behavioral/unit tests of the helper locally contrary to `PHDK_PRODUCTION_VERIFICATION.md`.

`VERIFY_DELIVERY` does not mean COMPLETED. Use `PHDK_COMPLETION_GATE.md` for real remote target/content/version evidence; its generic review wording never restores a PHDK human gate in FORCE. The record and advisor cannot detect a fabricated observation or substitute for real checks, selected design evidence or current user instructions.

## Human-effort estimate must not block Auto

At the post-PMO pre-implementation point and material evidence-backed milestones, apply [PHDK_EFFORT_ESTIMATION_STANDARD.md](PHDK_EFFORT_ESTIMATION_STANDARD.md). The original and remaining human-equivalent days and progress bar are **reporting projections**, not a wait condition, new `AUTO_STATE.json` step kind, authorization token or AI ETA. Link the factual current-run `EFFORT_STATE.json` without duplicating mandates; do not create `owner_decision` solely to display effort. Both Auto and Force continue the next authorized action. Preserve real owner/Design/security/external blockers and explicit-only UAT.

## Composite Upgrade Force completeness (v2.92.1)

After an exact Upgrade Force publishes the pinned standards milestone, carry the *original current mandate* into AUTO FORCE. Record remaining security/lock remediation, Check, delivery, deployed-revision checks and local closeout as runnable steps in the existing AUTO_STATE.json; keep any other verified unresolved scope commitments in the optional unresolved_commitments string list. The original upgrade PR is only one completed milestone, not a full-run completion signal. Report any later canonical upstream SHA as new-version information, not permission to create a second forced upgrade loop in the same invocation.

The read-only phdk_auto_gate.py advisor treats a stale assistant-written authorization.status=completed with outstanding steps or commitments as REPAIR_STATE rather than STOPPED, and likewise refuses VERIFY_DELIVERY when unresolved_commitments remain. Reconstruct the real scope from the current instruction and GitHub evidence; continue eligible work while the session remains open. Do not override a real owner stop or assert that a state file itself supplies authorization. A genuine session boundary triggers an honest handoff and prompt, never background work. UAT remains separately opt-in, and no PHDK-only reviewer wait blocks AUTO FORCE.

## Progress and closure

In every substantive AUTO FORCE progress update include the operative continuation cue from `PHDK_COMMUNICATION_STANDARD.md`:

```text
AUTO FORCE activo · autorización vigente para [objetivo/alcance].
RECORDATORIO: recargar las reglas vigentes, reconciliar bloqueos heredados, buscar soluciones y proponer lo que falte.
SIGUIENTE PASO: [acción concreta]. Continúo con el trabajo autorizado.
```

The reminder is an instruction to apply, not a claim that a reread, repair or proposal already happened. Report completed actions only with actual evidence. Normal Auto retains its mandate/next-action cue. While the current session remains open, execute the stated eligible action in the same invocation; do not end the turn with a promise to continue while permitted work is ready. On a rejection the next action is diagnosis/repair/retry. When a definition is missing, propose and resolve what can be decided inside the current mandate before asking about a remaining indispensable decision. For normal Auto awaiting Design input, state the actual question and waiting condition, not a claim that dependent coding continues.

At actual development completion report the verified result and target link, the actual `DEVELOPMENT COMPLETE` / `PARTIALLY DELIVERED` / `BLOCKED` outcome, and `UAT NOT RUN` separately. Offer optional future `PHDK uat` without waiting for an answer as a delivery gate. Mark the development goal complete only from its required evidence; do not claim an active mandate to start unrelated work. On a genuine user stop, exhausted external dependency or required normal Auto Design input, report the factual limitation and one precise resume action/question. Preserve the existing PHDK version, lifecycle and final-link contract without repeating long permission prose.
