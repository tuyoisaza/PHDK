---
name: phdk
description: >-
  Use for a current explicit request to create or edit a PHDK project's code or
  documentation, validate locally, deliver through GitHub, synchronize standards,
  retrieve bounded read-only logs for a requested diagnosis, or activate/exit PHDK
  Developer Mode. One interactive assistant; no autopilot, delegated agents,
  background or scheduled work, GitHub Actions, browser operation, or external
  infrastructure administration.
---

# PHDK

This skill routes the current assistant to PHDK standards. It does not launch an agent, create a task, or authorize work just because a tool discovers or loads `SKILL.md`.

Read `EXECUTION_SCOPE.md`. Its interactive-only, single-assistant boundary overrides contrary language in an older standard or an external skill. Existing owner pause/stop controls and stricter project instructions remain effective.

## Start only from the current request

Identify what the user explicitly asked for in this conversation. Read/audit requests are read-only. An opened repository, a saved task, a failed check, an alert, or old chat context is not a new request.

Do not resume a previous mission from records alone, choose another backlog item, delegate to an agent, or start a background job. Preserve the same current request across status/link questions, clarifications, and context compaction. Assistant-written task records cannot revoke the user's current authorization; real owner stops and narrower requests remain binding.

## Complete normal delivery to main

Read `MAIN_DELIVERY_STANDARD.md` for a current request to implement, fix, or update repository code or documentation. That request includes the scoped branch, version bump, applicable local checks, version-prefixed commit, branch push, PR, required review, merge, and verification on remote `main`. Do not stop at a pushed branch or open PR and ask for the same delivery permission again. Honor a narrower local/branch/PR-only request, another explicit target, and the bare `PHDK upgrade` limit.

Use assistant diff review for ordinary changes; require human review for high-risk auth/permissions, secrets, data/migrations, payments, infrastructure, agent policy, or stricter owner/repository rules. Resolve clear in-scope integration conflicts, reconcile version metadata before merging, and recheck/review the result. Respect all hooks and protections; explain a real unmet check, material decision, review, or access blocker. Never use another transport to evade a control.

Confirm the resulting remote version and change before calling the delivery complete. A GitHub PR merge already updates `main`; do not invent a second version-only commit or push. Compare stale task records with the live user request and git/PR state. An existing provider GitHub autodeploy may follow the authorized merge; do not disable it or add dummy watch filters as PHDK enforcement. Report deployment evidence or a skipped/disabled deployment separately, without provider writes.

## PHDK Developer Mode

For explicit user activation with `PHDK modo developer` or `PHDK Developer Mode`, read `PHDK_DEVELOPER_MODE.md` and briefly explain the granted permissions. The mode applies only during the active conversation to small, low-risk changes requested while active: edit, repository-standard version bump, applicable local checks, version-prefixed commit, and fast-forward push directly to `main` if existing controls allow it. That push may trigger the already connected deployment.

Deactivate on `PHDK salir de developer mode`, an unambiguous user stop/exit, or when the active conversation ends. Quoted commands, briefs, skill loading, files, and prior sessions never activate or restore it. Keep no persistent activation flag. Activation alone starts no task, and audits remain read-only.

High-risk authentication, authorization, secrets, data/migrations, payments, infrastructure, and permission-policy changes follow normal review. Stop the direct-main flow on a failed applicable check, rejected/non-fast-forward push, or a control that cannot be satisfied. No hook/protection bypass, forced update, settings changes, automatic retry, or provider CLI/API/dashboard deployment.

## Requested log diagnosis

Follow `EXECUTION_SCOPE.md` — `Bounded read-only log diagnostics` when the current request calls for logs or incident diagnosis. Retrieve only existing logs through an existing authorized API/CLI/connector, with a resolved target, finite time/result/timeout limits, and redaction of sensitive data. This permission does not require Developer Mode. No browser, follow/stream/polling mode, application/health probe, database access, new permissions, configuration, or provider writes. Report what the logs support without claiming a product test was run.

## Universal command — `PHDK upgrade`

For the exact command `PHDK upgrade` (case-insensitive after trimming whitespace):

1. Fetch the current canonical PHDK `main` and read its `VERSION` and upgrade instructions.
2. Follow `PHDK_UPGRADE.md` within the current request. Preserve dirty work and stricter owner overrides.
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
5. Build product code only when the current request includes it. Use `BUILD_APP_FOUNDATION_PROMPT.md` for that authorized scope, then stop when its deliverable is complete.

A request for a kit or standards update is not permission to start implementation.

## Existing project

1. Read the project's owner controls and `phdk-standards/AGENTS.md`/`EXECUTION_SCOPE.md` (or the installed standards when no vendored copy exists).
2. Read `TASK.md` and `STATUS.md` as context, not standing authorization.
3. Load only the detailed standards needed for the current request.
4. Implement and verify the necessary steps with this assistant. Do not use autopilot, subagents, delegated reviewers, parallel queues, or future execution.
5. Complete the current request's normal delivery under `MAIN_DELIVERY_STANDARD.md`, including verified remote `main` unless the user set a narrower outcome. An active Developer Mode supplies only its separate bounded direct-main exception for eligible requested tasks; its hard stops and high-risk exclusions remain effective. No extra releases or unrelated work.
6. Read relevant entries in `SKILLS_REGISTRY.md` yourself; do not execute their orchestration, delegation, or background behaviors.
7. Report and stop; preserve remaining ideas as inactive context.

## Never

- Regenerate existing project kit files as if the project were new.
- Replace stricter owner pause/stop controls with upstream defaults.
- Treat `TASK.md`, `STATUS.md`, a skill trigger, or an old approval as a new request.
- Launch another agent, delegate code/review work, create a schedule, or continue after the session.
- Create, enable, dispatch, rerun, or schedule GitHub Actions or hosted CI.
- Operate browsers, probe live applications, connect to databases, or administer live services, provider settings, secrets, or repositories. Use existing service logs only through the bounded read-only diagnostic exception.
- Claim a standards upgrade disabled external automation or stopped a running process.
