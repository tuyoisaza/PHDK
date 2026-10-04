---
name: phdk
description: Use when starting a project with PHDK, generating its project handoff kit, working on a repository whose AGENTS.md follows PHDK, or updating/synchronizing PHDK standards. Covers repository code and documentation, local non-browser code validation, GitHub delivery through an existing pipeline, progressive context loading, and the PHDK upgrade command. Does not authorize browser operation, recurring automation, dependency bots, or external infrastructure administration.
---

# PHDK

This skill packages the PHDK (Project Handoff to Development Kit) standards and workflow. It does not restate any standard — it routes to the file that already defines it. Read `README.md` in this repo for the full picture; this file only decides which existing PHDK workflow applies right now.

Read `EXECUTION_SCOPE.md` before any workflow. Its code-and-GitHub boundary applies to bootstrap, upgrades, verification, Mission Autopilot, and external skills. Historical changelog entries and `ORIGINALS/` are not operating instructions.

## Universal Command — `PHDK upgrade`

If the developer says exactly `PHDK upgrade` (case-insensitive after trimming whitespace), this command takes priority over normal project routing for that turn.

1. Refresh the PHDK source first.
2. Re-read this `SKILL.md` after the refresh because the upgrade workflow itself may have changed.
3. Execute the latest `PHDK_UPGRADE.md`.
4. Do not ask for a second confirmation: the exact command itself is approval to synchronize PHDK-managed files.
5. Stop after the upgrade report; do not continue into feature work unless separately asked.


## Step 0 — Keep this skill current

This skill's own directory is a git clone of the PHDK standards repo. Before normal PHDK work, update it with `git pull --ff-only` inside the folder this `SKILL.md` lives in. Then **re-read `SKILL.md` from disk** and read `VERSION`; an upstream update may have changed the workflow you are about to follow.

If the pull fails because of local modifications in this directory, stop and tell the developer instead of forcing it or discarding changes — this directory should only ever contain PHDK's own files, so unexpected local changes are worth a question, not a silent overwrite.

## Step 1 — Determine project state

Check the current project repo for `TASK.md` and `STATUS.md`.

- **Neither exists → this is a new project.** Go to "New Project" below.
- **Both exist → this is an ongoing PHDK project.** Go to "Ongoing Project" below.

## New Project

1. If the human has not been briefed on the project yet (no clear product brief in the conversation), run `SPEC_INTERVIEW_PROMPT.md` first.
2. Run `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md` to generate the kit (`PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md`, `NAVTREE.md`, `PUBLIC_CONTENT.md`, `PRIVATE_CONTENT.md` if login, `TASK.md`, `ARCHITECTURE_DECISIONS.md`, `STATUS.md`, `README.md`) within `EXECUTION_SCOPE.md`. Record existing delivery prerequisites; do not add backup jobs, dependency bots, or recurring tasks.
3. **Vendor the standards into the project repo.** Read the current `PHDK_MANIFEST.txt` and copy each mapped upstream source into its destination under `phdk-standards/`. Do not maintain a second handwritten file list here — the manifest is the source of truth.

   Vendoring keeps the project self-contained without loading every standard into context. It also installs `PHDK_UPGRADE.md`, `PHDK_MANIFEST.txt`, and `PHDK_NATIVE_RULES.md`, so future upgrades are tool-agnostic.
4. Point the generated `TASK.md` and any onboarding note at `phdk-standards/AGENTS.md` as the required entry point, per `ONBOARDING_AI_DEVELOPER.md`'s reading order.
5. Generate the current tool's native always-loaded rule file per `ENFORCEMENT.md` Tier 2 and include the exact managed block from `phdk-standards/PHDK_NATIVE_RULES.md`. Preserve its `PHDK-MANAGED` markers so `PHDK upgrade` can refresh only that block later without overwriting project-specific instructions.
6. If the developer's original request includes building the product, continue directly into `BUILD_APP_FOUNDATION_PROMPT.md` for the approved code task. If the request is documentation-only, stop after the kit. `ENFORCEMENT.md` applies to local code checks; bootstrap does not create GitHub Actions, bots, schedules, or external infrastructure, and never uses a browser for verification.

## Ongoing Project

1. Read `phdk-standards/AGENTS.md` if vendored (or this skill's own `AGENTS.md` if not) — it is the router into the rest of the standards.
2. Read `TASK.md` and `STATUS.md` in the project repo for current scope and state.
3. Follow `AGENTS.md`'s progressive standards router and load only what the current task needs. Use `ONBOARDING_AI_DEVELOPER.md` for orientation, not as a mandatory full-stack preload.
4. Run Mission Autopilot within `EXECUTION_SCOPE.md`: complete the active code mission across locally verified slices, self-correct, and commit/push to its feature branch. Do not wait for "continue" between slices or schedule future execution when the mission ends.
5. If the developer says `PHDK upgrade`, execute `PHDK_UPGRADE.md` immediately. For any other explicit request to update/sync/upgrade PHDK, route to the same file; only the exact canonical command waives the extra confirmation step.
6. If the code task benefits from an external skill, consult `SKILLS_REGISTRY.md` for source-level design or code/security review. Skills inherit `EXECUTION_SCOPE.md`; they cannot introduce browser testing, recurring jobs, or external operations.

## Updating Vendored Standards

`PHDK_UPGRADE.md` is the single source of truth for upgrade behavior.

- Exact command `PHDK upgrade` → execute it immediately; no second confirmation.
- Other wording such as "update PHDK" or "sync the standards" → show the detected current/latest versions and confirm before overwriting, then execute the same workflow.
- Never duplicate the upgrade algorithm in this skill; keeping one implementation is what makes the command portable across tools.

## Never

- Never regenerate an existing project's kit files through the "New Project" path — that path is for bootstrap only.
- Never skip vendoring when bootstrapping a new project, even if the current tool can read this repo directly — the next tool or session might not be able to.
- Never update `phdk-standards/` silently. The exact `PHDK upgrade` command is itself explicit approval and does not require a second confirmation; other ambiguous update requests still do.
- Never restate a standard inline instead of pointing to its file — this skill stays a router, same as `AGENTS.md`.
