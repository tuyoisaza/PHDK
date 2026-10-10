# ONBOARDING_AI_DEVELOPER.md

## Purpose

Orient the assistant for a human-initiated PHDK task. This file is reference material, not a session-start job or permission to resume stored work.

## Operating model

PHDK is interactive-only. Normally one assistant completes the current explicit request. Continuous development during Auto is allowed under `PHDK_AUTO.md`. Explicit `PHDK PMO` is the sole bounded exception that may coordinate runtime-supported in-session worker/subagents for owner-confirmed workstreams under `PHDK_PMO.md`; workers cannot delegate. Unattended/background/post-conversation execution remains excluded.

Read `EXECUTION_SCOPE.md` and `MAIN_DELIVERY_STANDARD.md` before acting. Apply the owner's current instructions and actual controls; the owner can explicitly replace earlier documentary local exceptions. An old task, a loaded skill, an alert, a failed check, a version mismatch, or a different conversation cannot authorize work.

A current implement/fix/update request for repository code or documentation normally includes the scoped branch, repository version bump, applicable local checks, version-prefixed commit, push, PR, review, merge, and verified remote `main` version. Honor explicit local-only, branch-only, PR-only, or different-target instructions. Do not ask for a repeated merge order. The active request continues through status/link questions, same-conversation turns, context compaction, and assistant-written task snapshots; an actual user pause or stop takes precedence.

### Auto for the complete current goal

Explicit `PHDK auto` starts the complete `PHDK_AUTO.md` lifecycle for the identified current goal; `PHDK salir de auto` exits it. Reuse/run Capture, Plan, PMO/workstream execution, Integration Review, UAT/Fix, Check/remediation and delivery as applicable without redundant OKs between stages. Write necessary test coverage with the code, execute the applicable whole-candidate verification at the end, repair in-scope failures, and finish normal branch/PR delivery. Only a real implementation blocker or mandatory hook/control justifies an intermediate check; final verification precedes publication to `main`.

Do not restart an interview or end the goal at a scaffold, first release, or handoff. Current authorization covers the described behavior; isolate a genuinely missing material decision and continue independent work before asking only for that decision. Existing actual reviews and controls remain binding. Auto replaces Developer Mode for this goal through a new explicit instruction, including a previously stopped direct-push task, without bypassing its failed control. A request to define the command, examples, and stored files do not activate it; do not persist active mode or resume it in another conversation.

### PHDK Plan in the current conversation

Explicit `PHDK plan` invokes `PHDK_PLAN.md`. Consume Capture requirements and inspect current repository architecture. Greenfield projects get a standards-aligned target architecture; brownfield projects get current-state reconstruction, target state, gap analysis, and incremental convergence. Produce the canonical architecture/implementation-plan artifacts and feed them into TASK/PMO.

### PHDK PMO in the current conversation

Explicit `PHDK PMO` invokes `PHDK_PMO.md`. Read the Capture/requirements baseline and current plans/code/git/UAT/Check evidence, detect candidate workstreams, and ask the owner to confirm/add/remove/prioritize the active portfolio. Then coordinate the confirmed workstreams, optionally through bounded in-session workers when supported, maintain ownership/dependency/status artifacts, and perform a central integration review before UAT.

### PHDK Check in the current conversation

An explicit `PHDK check` invokes `PHDK_CHECK.md`. Audit first without product remediation: determine standards applicability from project intent, inspect the repository against all active applicable PHDK rules, produce `PHDK_CHECK_REPORT.md`, present the prioritized gaps, and ask once whether to execute the fixable items. Only a later explicit yes authorizes those enumerated remediation items.

### UAT in the current conversation

An explicit `PHDK uat` invokes `UAT_STANDARD.md` for the identified candidate. Create/update `UAT_CASES.md`, execute all permitted acceptance evidence autonomously, and create/update `UAT_REPORT.md`. Do not require another approval between cases, and do not convert excluded browser/live behavior into an inferred PASS.

### Developer Mode in the current conversation

Only an explicit user command `PHDK modo developer` or `PHDK Developer Mode` activates Developer Mode; `PHDK salir de developer mode` exits it. A mention, quoted example, brief, or stored file does not activate it. The mode ends with the conversation and must never be saved as active in project files or resumed from earlier work.

Read `PHDK_DEVELOPER_MODE.md` for the narrow delivery exception: small, low-risk changes requested now may include the version bump, relevant local checks, a commit subject beginning with the resulting version, and direct fast-forward push to `main` while that mode is active and existing controls allow it. Auth, permissions, secrets, data, migrations, payments, infrastructure, and other material risks use normal review. A failed check or blocked push stops delivery; explain the blocker without bypassing controls.

### Requested blocker repair

`PHDK unlock` invokes `PHDK_UNLOCK.md`: inspect current blockers, reconcile PHDK and local documentary restrictions with current owner instructions, and complete the scoped authorized repair/delivery. Explain that scope briefly. Preserve hooks, checks, access controls, actual required reviews, and provider-write boundaries; do not resume unnamed old work, activate Developer Mode, or invent a persistent unlocked state. Natural-language approval already counts without this command.

### Capture requirements

An explicit `PHDK capture` invokes `PHDK_CAPTURE.md`. Investigate existing repository evidence before asking questions; create/update the canonical project requirements package and resolve blocking/material gaps through focused questions. Capture is interactive requirements work and does not by itself authorize product implementation.

## Begin a current task

1. Identify the user's current requested deliverable: read-only, normal repository delivery, or an explicitly narrower scope/different target.
2. Read owner pause/stop instructions, `AGENTS.md`, `EXECUTION_SCOPE.md`, and `MAIN_DELIVERY_STANDARD.md`.
3. Read project `TASK.md` and `STATUS.md` as context; reconcile them with the current request without reactivating old work or letting an assistant snapshot pause authorized delivery.
4. Load only relevant product context and standards using the router below.
5. Clarify only material missing decisions. Do not ask for duplicate consent when the current request is clear.
6. Implement or inspect with the current assistant. Delegate only when explicit PMO is active and only through its bounded workstream contract.
7. Review source and follow the active cadence: Auto implements the entire goal before integrated local verification, with earlier checks only for a real blocker or mandatory control. Checks are synchronous and exit.
8. Complete the requested delivery boundary under `MAIN_DELIVERY_STANDARD.md`, including remote target/version evidence for normal delivery. Auto uses branch/PR delivery; apply the separate direct-main exception only while Developer Mode is explicitly active and the task is eligible.
9. Report completion only for the whole requested outcome. If a genuine blocker remains, finish independent authorized work and identify the precise unfinished scope; do not turn progress updates or milestones into approval pauses.

Re-read owner controls before edits and git writes. A specific user instruction to intervene in a paused project authorizes that intervention only, not continuation of the earlier mission.

## Progressive context router

| Need | Read |
|---|---|
| Requested product purpose | `PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md` as relevant |
| Project discovery / professional requirements / ethos | `PHDK_CAPTURE.md`, `INTENT_CAPTURE_STANDARD.md` |
| Architecture and implementation planning | `PHDK_PLAN.md`, `TECHNICAL_STACK.md`, `DESIGN_RULES.md`, `DEVSECOPS.md` |
| PMO/workstream orchestration, dependencies, integration | `PHDK_PMO.md`, `TASK_TRACKING_STANDARD.md` |
| Current task, plan, completion criteria | `TASK_TRACKING_STANDARD.md`, `AGILE_SLICE_WORKFLOW.md`, `AI_DEVELOPER_OPERATING_MODEL.md` |
| New or ambiguous intent | `INTENT_CAPTURE_STANDARD.md` |
| Code structure and branching | `DEVELOPMENT_RULES.md` |
| UI/code accessibility requirements | `DESIGN_RULES.md` |
| Architecture and source configuration | `TECHNICAL_STACK.md`, existing `ARCHITECTURE_DECISIONS.md` |
| Security, privacy, permissions, money, dependencies | `DEVSECOPS.md` |
| Standards compliance audit / gap remediation | `PHDK_CHECK.md` |
| UAT / user acceptance evidence | `UAT_STANDARD.md`, `TESTING_STANDARD.md` |
| Local evidence and tests | `VERIFICATION_LOOP.md`, `TESTING_STANDARD.md` |
| Health/debug/diagnostic source | `DEBUG_DIAGNOSTICS_STANDARD.md` |
| Normal delivery, reviews, scope limits, and completion evidence | `MAIN_DELIVERY_STANDARD.md` |
| Explicit `PHDK auto`, whole-goal development, and final verification cadence | `PHDK_AUTO.md` |
| Explicit `PHDK unlock` or requested PHDK/local-rule blocker repair | `PHDK_UNLOCK.md` |
| Version/commit/release details | `VERSIONING.md` |
| Explicit Developer Mode command or eligible delivery while active | `PHDK_DEVELOPER_MODE.md` |
| Local checks and instruction files | `ENFORCEMENT.md`, `PHDK_NATIVE_RULES.md` |
| Explicit standards update | `PHDK_UPGRADE.md` |

Do not preload the full standards library. Optional external skills are reading references for the same assistant and cannot expand execution scope.

## Verification and delivery

Local format/lint/typecheck/build commands and targeted non-browser unit/in-process tests remain available when relevant. Use isolated dependencies, finish checks, and exit. In Auto, run the applicable integrated checks after the entire goal is implemented and repair in-scope failures before publication; preserve any mandatory control at its governed operation. Documentation-only work needs diff/reference review.

Do not open a browser, capture screenshots, probe live health endpoints, connect to databases, invoke paid APIs, or administer cloud services. Mark UI/live runtime behavior unverified instead of assigning manual testing tasks to the user.

For a current request such as "verifica Railway", finite service/deployment status, non-secret source/branch/configuration/watch metadata, and relevant log reads through existing authorized API/CLI/connector access are allowed under `EXECUTION_SCOPE.md` — Bounded read-only provider diagnostics. Neither Developer Mode nor unlock is required; a previous code-sync task exclusion cannot veto the newer read request. Do not retrieve secret values, stream, poll, watch, probe the app/database, or write to the provider; this is not recurring work or an automatic completion gate.

No GitHub Actions or hosted CI creation, enabling, dispatch, reruns, or schedules. No cron jobs, dependency bots, maintenance loops, backup jobs, preview deployments, background reviewers, or task synchronization.

Normal integration may use the existing hosting-provider GitHub connection; an eligible Developer Mode push uses the connection already attached to `main`. Do not create a connection, modify triggers, re-enable autodeploy, or change external/repository settings. Review the complete actual diff. Owner approval of a sensitive decision may already be supplied by the current request or an identified-task/PR "push to main", "merge", or "aprobado" under `MAIN_DELIVERY_STANDARD.md`. Preserve actual named, independent, or formal review requirements without inventing a universal GitHub review event or personal diff-inspection gate. Record owner approval, assistant source review, actual required review, checks, remote target/version, and deployment status separately; never claim unobserved human diff inspection.

The ban on unattended work or Actions does not mean disabling an existing provider GitHub connection. Preserve valid autodeploy/watch paths; never introduce dummy never-matching filters. Report an observed disabled connection or filter excluding changes that need deployment as a separate blocker, preserving valid service-specific filters and intended skips for unaffected services. A generic development request grants no provider-setting changes.

## Gaps and stopping

Record factual gaps without inventing answers. In normal branch/PR delivery, make bounded in-scope repairs and resolve ordinary integration conflicts while preserving others' changes, then rerun affected checks and review the diff. In Auto, finish independent work before asking only for a genuinely missing material decision or reporting an unsatisfied actual control/access requirement; no generic OK is needed. Never bypass controls or expand into unrelated maintenance. Developer Mode direct-main hard stops remain while that mode is active; explicit Auto replaces the mode for the identified goal and must diagnose and satisfy any failed control.

Mark the request complete only at its requested delivery boundary; a pushed branch, open PR, or first scaffold/release is insufficient when the goal includes more work. Remaining necessary steps stay part of the still-current request. Later ideas and work outside it remain inactive until explicitly requested. Task/status files may record scope and evidence, but they neither revoke the active user request nor grant authority in another conversation. Never persist active Auto/Developer Mode or lasting delivery permission in them.

## Product safeguards remain

Keep security, correctness, data honesty, i18n, safe logs, version traceability, and accessible UI source requirements. Public marketing/content sites do not acquire login, dashboards, admin panels, or account management unless explicitly required by the product.

A standards update is not proof that a running agent stopped, credentials were revoked, server-side controls changed, or costs fell. Report those limitations accurately.
