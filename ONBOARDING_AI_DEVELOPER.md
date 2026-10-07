# ONBOARDING_AI_DEVELOPER.md

## Purpose

Orient the assistant for a human-initiated PHDK task. This file is reference material, not a session-start job or permission to resume stored work.

## Operating model

PHDK is interactive-only. One assistant works on the current explicit user request, completes its necessary steps, reports evidence, and stops. There is no Mission Autopilot, delegated coding/review, subagent, agent team, or agent queue, including during the active session.

Read `EXECUTION_SCOPE.md` and `MAIN_DELIVERY_STANDARD.md` before acting. Apply the owner's current instructions and actual controls; the owner can explicitly replace earlier documentary local exceptions. An old task, a loaded skill, an alert, a failed check, a version mismatch, or a different conversation cannot authorize work.

A current implement/fix/update request for repository code or documentation normally includes the scoped branch, repository version bump, applicable local checks, version-prefixed commit, push, PR, review, merge, and verified remote `main` version. Honor explicit local-only, branch-only, PR-only, or different-target instructions. Do not ask for a repeated merge order. The active request continues through status/link questions, same-conversation turns, context compaction, and assistant-written task snapshots; an actual user pause or stop takes precedence.

### Developer Mode in the current conversation

Only an explicit user command `PHDK modo developer` or `PHDK Developer Mode` activates Developer Mode; `PHDK salir de developer mode` exits it. A mention, quoted example, brief, or stored file does not activate it. The mode ends with the conversation and must never be saved as active in project files or resumed from earlier work.

Read `PHDK_DEVELOPER_MODE.md` for the narrow delivery exception: small, low-risk changes requested now may include the version bump, relevant local checks, a commit subject beginning with the resulting version, and direct fast-forward push to `main` while that mode is active and existing controls allow it. Auth, permissions, secrets, data, migrations, payments, infrastructure, and other material risks use normal review. A failed check or blocked push stops delivery; explain the blocker without bypassing controls.

### Requested blocker repair

`PHDK unlock` invokes `PHDK_UNLOCK.md`: inspect current blockers, reconcile PHDK and local documentary restrictions with current owner instructions, and complete the scoped authorized repair/delivery. Explain that scope briefly. Preserve hooks, checks, access controls, actual required reviews, and provider-write boundaries; do not resume unnamed old work, activate Developer Mode, or invent a persistent unlocked state. Natural-language approval already counts without this command.

## Begin a current task

1. Identify the user's current requested deliverable: read-only, normal repository delivery, or an explicitly narrower scope/different target.
2. Read owner pause/stop instructions, `AGENTS.md`, `EXECUTION_SCOPE.md`, and `MAIN_DELIVERY_STANDARD.md`.
3. Read project `TASK.md` and `STATUS.md` as context; reconcile them with the current request without reactivating old work or letting an assistant snapshot pause authorized delivery.
4. Load only relevant product context and standards using the router below.
5. Clarify only material missing decisions. Do not ask for duplicate consent when the current request is clear.
6. Implement or inspect with the current assistant; do not delegate.
7. Review source and run proportionate synchronous local checks that exit.
8. Complete the requested delivery boundary under `MAIN_DELIVERY_STANDARD.md`, including remote target/version evidence for normal delivery. Apply `PHDK_DEVELOPER_MODE.md` only if explicitly active in this conversation and the requested change is eligible; respect existing protections.
9. Record completion or the precise unresolved blocker, evidence, and inactive follow-ups; report and stop only when that boundary is reached or a genuine blocker/user stop applies.

Re-read owner controls before edits and git writes. A specific user instruction to intervene in a paused project authorizes that intervention only, not continuation of the earlier mission.

## Progressive context router

| Need | Read |
|---|---|
| Requested product purpose | `PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md` as relevant |
| Current task, plan, completion criteria | `TASK_TRACKING_STANDARD.md`, `AGILE_SLICE_WORKFLOW.md`, `AI_DEVELOPER_OPERATING_MODEL.md` |
| New or ambiguous intent | `INTENT_CAPTURE_STANDARD.md` |
| Code structure and branching | `DEVELOPMENT_RULES.md` |
| UI/code accessibility requirements | `DESIGN_RULES.md` |
| Architecture and source configuration | `TECHNICAL_STACK.md`, existing `ARCHITECTURE_DECISIONS.md` |
| Security, privacy, permissions, money, dependencies | `DEVSECOPS.md` |
| Local evidence and tests | `VERIFICATION_LOOP.md`, `TESTING_STANDARD.md` |
| Health/debug/diagnostic source | `DEBUG_DIAGNOSTICS_STANDARD.md` |
| Normal delivery, reviews, scope limits, and completion evidence | `MAIN_DELIVERY_STANDARD.md` |
| Explicit `PHDK unlock` or requested PHDK/local-rule blocker repair | `PHDK_UNLOCK.md` |
| Version/commit/release details | `VERSIONING.md` |
| Explicit Developer Mode command or eligible delivery while active | `PHDK_DEVELOPER_MODE.md` |
| Local checks and instruction files | `ENFORCEMENT.md`, `PHDK_NATIVE_RULES.md` |
| Explicit standards update | `PHDK_UPGRADE.md` |

Do not preload the full standards library. Optional external skills are reading references for the same assistant and cannot expand execution scope.

## Verification and delivery

Local format/lint/typecheck/build commands and targeted non-browser unit/in-process tests remain available when relevant. Use isolated dependencies, finish the checks, and exit. Documentation-only work needs diff/reference review.

Do not open a browser, capture screenshots, probe live health endpoints, connect to databases, invoke paid APIs, or administer cloud services. Mark UI/live runtime behavior unverified instead of assigning manual testing tasks to the user.

For a current request such as "verifica Railway", finite service/deployment status, non-secret source/branch/configuration/watch metadata, and relevant log reads through existing authorized API/CLI/connector access are allowed under `EXECUTION_SCOPE.md` — Bounded read-only provider diagnostics. Neither Developer Mode nor unlock is required; a previous code-sync task exclusion cannot veto the newer read request. Do not retrieve secret values, stream, poll, watch, probe the app/database, or write to the provider; this is not recurring work or an automatic completion gate.

No GitHub Actions or hosted CI creation, enabling, dispatch, reruns, or schedules. No cron jobs, dependency bots, maintenance loops, backup jobs, preview deployments, background reviewers, or task synchronization.

Normal integration may use the existing hosting-provider GitHub connection; an eligible Developer Mode push uses the connection already attached to `main`. Do not create a connection, modify triggers, re-enable autodeploy, or change external/repository settings. Review the complete actual diff. Owner approval of a sensitive decision may already be supplied by the current request or an identified-task/PR "push to main", "merge", or "aprobado" under `MAIN_DELIVERY_STANDARD.md`. Preserve actual named, independent, or formal review requirements without inventing a universal GitHub review event or personal diff-inspection gate. Record owner approval, assistant source review, actual required review, checks, remote target/version, and deployment status separately; never claim unobserved human diff inspection.

No autonomous work or Actions does not mean disabling an existing provider GitHub connection. Preserve valid autodeploy/watch paths; never introduce dummy never-matching filters. Report an observed disabled connection or filter excluding changes that need deployment as a separate blocker, preserving valid service-specific filters and intended skips for unaffected services. A generic development request grants no provider-setting changes.

## Gaps and stopping

Record factual gaps without inventing answers. In normal branch/PR delivery, make bounded in-scope repairs and resolve ordinary integration conflicts while preserving others' changes, then rerun affected checks and review the diff. Ask one precise question only for a material missing decision or unresolved check, review, or access blocker; never bypass controls or expand into unrelated maintenance. Developer Mode direct-main hard stops remain unchanged, with no automatic repair, retry, or fallback.

Mark the request complete only at its requested delivery boundary; a pushed branch or open PR is insufficient for normal delivery. Remaining necessary steps stay part of the still-current request. Later ideas and work outside it remain inactive until explicitly requested. Task/status files may record scope and evidence, but they neither revoke the active user request nor grant authority in another conversation. Never persist active Developer Mode or lasting delivery permission in them.

## Product safeguards remain

Keep security, correctness, data honesty, i18n, safe logs, version traceability, and accessible UI source requirements. Public marketing/content sites do not acquire login, dashboards, admin panels, or account management unless explicitly required by the product.

A standards update is not proof that a running agent stopped, credentials were revoked, server-side controls changed, or costs fell. Report those limitations accurately.
