---
name: phdk
description: >-
  Use for a current explicit request to create or edit a PHDK project's code or
  documentation, validate locally, deliver through GitHub, synchronize standards,
  complete a whole development goal with PHDK auto, run autonomous acceptance validation with PHDK uat, audit and close standards gaps with PHDK check, repair PHDK blockers with
  PHDK unlock, retrieve bounded read-only provider
  status/configuration metadata or logs, or activate/exit PHDK Developer Mode.
  One interactive assistant; no unattended work or delegated agents,
  background or scheduled work, GitHub Actions, browser operation, or external
  infrastructure administration.
---

# PHDK

This skill routes the current assistant to PHDK standards. It does not launch an agent, create a task, or authorize work just because a tool discovers or loads `SKILL.md`.

Read the current user request and `EXECUTION_SCOPE.md`. Its interactive-only, single-assistant boundary overrides contrary language in an older standard or external skill. Honor current owner controls within their scope; the owner can explicitly replace older documentary exceptions. A file cannot veto that current instruction or remove actual access/security controls.

## Start only from the current request

Identify what the user explicitly asked for in this conversation. Read/audit requests are read-only. An opened repository, a saved task, a failed check, an alert, or old chat context is not a new request.

Do not resume a previous mission from records alone, choose another backlog item, delegate to an agent, or start a background job. Preserve the same current request across status/link questions, clarifications, and context compaction. Assistant-written task records cannot revoke the user's current authorization; real owner stops and narrower requests remain binding.

## Complete normal delivery to main

Read `MAIN_DELIVERY_STANDARD.md` for a current request to implement, fix, or update repository code or documentation. That request includes the scoped branch, version bump, applicable local checks, version-prefixed commit, branch push, PR, required review, merge, and verification on remote `main`. Do not stop at a pushed branch or open PR and ask for the same delivery permission again. Honor a narrower local/branch/PR-only request, another explicit target, and the bare `PHDK upgrade` limit.

Review the complete diff and apply the approval rules in `MAIN_DELIVERY_STANDARD.md`. Sensitive behavior/policy decisions need owner approval; a well-defined current request or "push to main", "merge", or "aprobado" for the identified change may already supply it in the conversation. Do not invent a GitHub review event or proof-of-opening-the-diff requirement. Preserve formal/named/independent reviews actually required by current owner instructions, hooks, or server rules, and never invent human inspection. Resolve clear in-scope conflicts, reconcile versions, and recheck. Respect hooks/protections; explain an actual unmet control or decision without changing transports to evade it.

Confirm the resulting remote version and change before calling the delivery complete. A GitHub PR merge already updates `main`; do not invent a second version-only commit or push. Compare stale task records with the live user request and git/PR state. An existing provider GitHub autodeploy may follow the authorized merge; do not disable it or add dummy watch filters as PHDK enforcement. Report deployment evidence or a skipped/disabled deployment separately, without provider writes.

## PHDK check

For explicit `PHDK check`, follow `PHDK_CHECK.md`. First perform a read-only applicability/compliance audit across the repository's active PHDK standards and implementation, create or refresh `PHDK_CHECK_REPORT.md`, present the prioritized gaps, and ask once whether the user wants the AUTO-FIXABLE and FIXABLE WITH VALIDATION items executed. Do not begin remediation before that answer.

If the user answers yes to that report in the same conversation, treat the listed fixable gap IDs as the authorized remediation scope. Implement them autonomously under normal PHDK controls, run applicable checks/UAT, deliver when requested by the remediation flow, rerun `PHDK check`, and report residual gaps. Do not auto-fix DECISION REQUIRED or EXTERNAL / MANUAL items.

## PHDK uat

For explicit `PHDK uat`, follow `UAT_STANDARD.md`. Identify the project's current intent first, derive user stories that explicitly align to that intent, then derive traceable acceptance cases for the current candidate and create/update `UAT_CASES.md`, execute all permitted acceptance evidence autonomously, and create/update `UAT_REPORT.md`. Do not ask for approval between cases. Never pass an unexecuted behavioral case by inspection; use BLOCKED or MANUAL when the required evidence is unavailable or excluded.

Standalone UAT validates and reports the candidate. Under active `PHDK auto`, repair in-scope UAT failures and rerun affected cases before final delivery.

## PHDK auto

For explicit `PHDK auto`, follow `PHDK_AUTO.md`. Use the identified current goal, including every agreed feature/stage, and begin without another OK or a mandatory interview when its scope is clear. Develop the whole candidate, run final integrated verification, repair in-scope failures, and finish normal versioned branch/PR delivery. Keep communicating without ending at milestones; do not create a release or optional full test cycle per stage. Actual mandatory hooks and necessary diagnostic checks remain applicable.

Auto replaces Developer Mode for that goal; it grants no direct-main bypass, background execution, new mission, or persistent flag. Exit on `PHDK salir de auto`, a clear stop, whole-goal completion, or conversation end. Source files, examples, installation, and a request to implement this command never activate it. The command's specific cadence takes precedence over generic interview, slice, and handoff approval templates.

## PHDK unlock

For the current command `PHDK unlock`, read `PHDK_UNLOCK.md`. Explain briefly that it audits PHDK-related blockers and repairs documentary restrictions in this repository according to the owner's current instructions, while preserving real checks, reviews, hooks, protections, access, security, and provider-write boundaries.

Inspect all relevant existing active native instruction files, copied PHDK sources and in-repository skills, task records, actual hooks/toolchain, and current GitHub evidence. Reconcile the authorized local exceptions and stale task boundaries, then finish the scoped normal versioned branch/PR delivery. Do not stop after fixing only one wrapper while another active copy retains the blocker.

Do not persist an unlocked flag, activate Developer Mode, resume old missions, merge unrelated PRs, weaken controls, or alter provider settings. Natural-language approval and bounded diagnosis requests already count without this command; quoted examples do not invoke it.

## PHDK Developer Mode

For explicit user activation with `PHDK modo developer` or `PHDK Developer Mode`, read `PHDK_DEVELOPER_MODE.md` and briefly explain the granted permissions. The mode applies only during the active conversation to small, low-risk changes requested while active: edit, repository-standard version bump, applicable local checks, version-prefixed commit, and fast-forward push directly to `main` if existing controls allow it. That push may trigger the already connected deployment.

Deactivate on `PHDK salir de developer mode`, an unambiguous user stop/exit, or when the active conversation ends. Quoted commands, briefs, skill loading, files, and prior sessions never activate or restore it. Keep no persistent activation flag. Activation alone starts no task, and audits remain read-only.

High-risk authentication, authorization, secrets, data/migrations, payments, infrastructure, and permission-policy changes follow normal review. Stop the direct-main flow on a failed applicable check, rejected/non-fast-forward push, or a control that cannot be satisfied. No hook/protection bypass, forced update, settings changes, automatic retry, or provider CLI/API/dashboard deployment.

## Requested provider diagnostics

Follow `EXECUTION_SCOPE.md` — `Bounded read-only provider diagnostics` for a current request such as "verifica Railway", a deployment/version check, or log/incident diagnosis. Read only relevant existing service/deployment/status/source/branch/non-secret configuration/watch metadata and logs through an authorized API/CLI/connector, with a resolved target, finite bounds, and redaction. No second authorization phrase, Developer Mode, or unlock is needed; an older task-specific exclusion does not cancel the newer read request. No browser, streams/polling, app probes, database access, secret values, new permissions, settings writes, or deployment. Report provider evidence separately from product-test or recovery claims.

## Universal command — `PHDK upgrade`

For the exact command `PHDK upgrade` (case-insensitive after trimming whitespace):

1. Fetch the current canonical PHDK `main` and read its `VERSION` and upgrade instructions.
2. Follow `PHDK_UPGRADE.md` within the current request. Preserve dirty work and genuine owner overrides in a bare sync; apply any explicit current request to remove/reconcile local PHDK exceptions through `PHDK_UNLOCK.md`.
3. Synchronize the manifest-controlled standards and the current tool's managed rule block.
4. Verify the source copy, report, and stop. Do not continue into product work or schedule a later upgrade.

The exact command authorizes the sync, not a push/merge, deployment, workflow run, or external administration. A current instruction that also explicitly requests git delivery supplies that additional permission.

## Skill updates

Update an installed skill clone only when the current request explicitly includes installation, update, or synchronization. Use a safe fast-forward and never discard local modifications. Re-read the updated `SKILL.md`, `EXECUTION_SCOPE.md`, and `VERSION` before proceeding.

Do not register auto-update hooks, scheduled refreshes, background pulls, or session-start jobs. Skill availability or a newer version is not authorization to mutate the project.

## New project

1. If the current request is for a new project and its purpose is unclear, use `SPEC_INTERVIEW_PROMPT.md` to clarify the necessary decision.
2. Generate the requested kit through `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md`, without adding bots, schedules, backup jobs, CI, external provisioning, or delegated agents.
3. When the request includes PHDK installation, read `PHDK_MANIFEST.txt` and vendor exactly its mappings under `phdk-standards/`.
4. Include the exact `PHDK_NATIVE_RULES.md` managed block in the current tool's instruction file per `ENFORCEMENT.md`. Preserve existing owner instructions and the managed markers; do not generate files for unused tools.
5. Build product code only when the current request includes it. Use `BUILD_APP_FOUNDATION_PROMPT.md` for that authorized scope. In Auto, a foundation is one part of the whole goal; continue the remaining agreed development and final verification/delivery under `PHDK_AUTO.md` rather than stopping at the scaffold.

A request for a kit or standards update is not permission to start implementation.

## Existing project

1. Read the project's owner controls and `phdk-standards/AGENTS.md`/`EXECUTION_SCOPE.md` (or the installed standards when no vendored copy exists).
2. Read `TASK.md` and `STATUS.md` as context, not standing authorization.
3. Load only the detailed standards needed for the current request.
4. Implement and verify the necessary steps with this assistant. Explicit Auto follows `PHDK_AUTO.md` through all agreed development and final integrated verification. Do not use unattended execution, subagents, delegated reviewers, parallel queues, or future execution.
5. Complete the current request's normal delivery under `MAIN_DELIVERY_STANDARD.md`, including verified remote `main` unless the user set a narrower outcome. An active Developer Mode supplies only its separate bounded direct-main exception for eligible requested tasks; its hard stops and high-risk exclusions remain effective. No extra releases or unrelated work.
6. Read relevant entries in `SKILLS_REGISTRY.md` yourself; do not execute their orchestration, delegation, or background behaviors.
7. Report and stop when the whole requested goal and delivery are complete, not at an Auto stage; preserve unrelated ideas as inactive context.

## Never

- Regenerate existing project kit files as if the project were new.
- Replace a genuine current owner restriction with upstream defaults without the owner's scoped instruction; remove actual checks, access rights, or security controls as documentary cleanup.
- Treat `TASK.md`, `STATUS.md`, a skill trigger, or an old approval as a new request.
- Launch another agent, delegate code/review work, create a schedule, or continue after the session.
- Create, enable, dispatch, rerun, or schedule GitHub Actions or hosted CI.
- Operate browsers, probe live applications, connect to databases, or administer live services, provider settings, secrets, or repositories. Requested existing provider metadata/log reads use only the bounded read-only diagnostic rule.
- Claim a standards upgrade disabled external automation or stopped a running process.
