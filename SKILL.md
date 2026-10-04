---
name: phdk
description: Use for a current explicit request to create or edit a PHDK project's repository code/documentation, validate it locally, perform authorized GitHub delivery, or synchronize PHDK standards. Interactive-only: one assistant, no autopilot, delegated agents, background tasks, scheduled work, GitHub Actions, browser operation, or external infrastructure administration.
---

# PHDK

This skill routes the current assistant to PHDK standards. It does not launch an agent, create a task, or authorize work just because a tool discovers or loads `SKILL.md`.

Read `EXECUTION_SCOPE.md`. Its interactive-only, single-assistant boundary overrides contrary language in an older standard or an external skill. Existing owner pause/stop controls and stricter project instructions remain effective.

## Start only from the current request

Identify what the user explicitly asked for in this conversation. Read/audit requests are read-only. An opened repository, a saved task, a failed check, an alert, or old chat context is not a new request.

Do not resume a previous mission, choose another backlog item, delegate to an agent, or start a background job. Complete only the necessary steps of the requested deliverable and stop.

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
5. Commit, push, create a PR, or merge only as authorized now. A clear request to implement and merge includes the required git/PR steps without duplicate confirmation.
6. Read relevant entries in `SKILLS_REGISTRY.md` yourself; do not execute their orchestration, delegation, or background behaviors.
7. Report and stop; preserve remaining ideas as inactive context.

## Never

- Regenerate existing project kit files as if the project were new.
- Replace stricter owner pause/stop controls with upstream defaults.
- Treat `TASK.md`, `STATUS.md`, a skill trigger, or an old approval as a new request.
- Launch another agent, delegate code/review work, create a schedule, or continue after the session.
- Create, enable, dispatch, rerun, or schedule GitHub Actions or hosted CI.
- Operate browsers, live services, databases, provider settings, secrets, or repository administration.
- Claim a standards upgrade disabled external automation or stopped a running process.
