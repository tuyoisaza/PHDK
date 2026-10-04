# ONBOARDING_AI_DEVELOPER.md

## Purpose

Orient the assistant for a human-initiated PHDK task. This file is reference material, not a session-start job or permission to resume stored work.

## Operating model

PHDK is interactive-only. One assistant works on the current explicit user request, completes its necessary steps, reports evidence, and stops. There is no Mission Autopilot, delegated coding/review, subagent, agent team, or agent queue, including during the active session.

Read `EXECUTION_SCOPE.md` before acting. Stricter owner controls take precedence. An old task, a loaded skill, an alert, a failed check, a version mismatch, or prior chat cannot authorize work.

## Begin a current task

1. Identify the user's current requested deliverable and whether the request is read-only, editing, or also git delivery.
2. Read owner pause/stop instructions, `AGENTS.md`, and `EXECUTION_SCOPE.md`.
3. Read project `TASK.md` and `STATUS.md` as context; reconcile them with the current request without reactivating old work.
4. Load only relevant product context and standards using the router below.
5. Clarify only material missing decisions. Do not ask for duplicate consent when the current request is clear.
6. Implement or inspect with the current assistant; do not delegate.
7. Review source and run proportionate synchronous local checks that exit.
8. Perform only git actions authorized now, respecting existing protections.
9. Record outcome/evidence and inactive follow-ups, report, and stop.

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
| Authorized version/commit/release work | `VERSIONING.md` |
| Local checks and instruction files | `ENFORCEMENT.md`, `PHDK_NATIVE_RULES.md` |
| Explicit standards update | `PHDK_UPGRADE.md` |

Do not preload the full standards library. Optional external skills are reading references for the same assistant and cannot expand execution scope.

## Verification and delivery

Local format/lint/typecheck/build commands and targeted non-browser unit/in-process tests remain available when relevant. Use isolated dependencies, finish the checks, and exit. Documentation-only work needs diff/reference review.

Do not open a browser, capture screenshots, probe live health endpoints, connect to databases, invoke paid APIs, or operate cloud services. Mark UI/live runtime behavior unverified instead of assigning manual testing tasks to the user.

No GitHub Actions or hosted CI creation, enabling, dispatch, reruns, or schedules. No cron jobs, dependency bots, maintenance loops, backup jobs, preview deployments, background reviewers, or task synchronization.

A specifically approved push/merge may use the existing hosting-provider GitHub connection. Do not create a connection, modify triggers, re-enable autodeploy, or change external/repository settings. Separate actual source checks, human approval, human diff-review evidence, and deployment status.

## Gaps and stopping

Record factual gaps without inventing answers. Ask one precise question only when the missing decision blocks the current request. Stop on a genuine unresolved blocker after bounded safe diagnosis; do not convert a failure into continuing maintenance work.

When done, mark the request complete. Remaining ideas or unfinished work stay inactive until a later explicit human request.

## Product safeguards remain

Keep security, correctness, data honesty, i18n, safe logs, version traceability, and accessible UI source requirements. Public marketing/content sites do not acquire login, dashboards, admin panels, or account management unless explicitly required by the product.

A standards update is not proof that a running agent stopped, credentials were revoked, server-side controls changed, or costs fell. Report those limitations accurately.
