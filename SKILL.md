---
name: phdk
description: Use when starting a new project that should follow PHDK standards, generating a PHDK project handoff kit, working on an existing project whose AGENTS.md says it follows PHDK, or when the developer asks to update/sync/upgrade a project's vendored PHDK standards. Covers project bootstrap (interview, generate handoff kit, vendor standards into the project), ongoing development (read standards in the required order, work in verified slices, follow DevSecOps/cost/backup rules), and updating an already-vendored phdk-standards/ folder to the latest version.
---

# PHDK

This skill packages the PHDK (Project Handoff to Development Kit) standards and workflow. It does not restate any standard — it routes to the file that already defines it. Read `README.md` in this repo for the full picture; this file only decides which existing PHDK workflow applies right now.

## Step 0 — Keep this skill current

This skill's own directory is a git clone of the PHDK standards repo. Before doing anything else, update it: run `git pull` inside this skill's directory (the folder this `SKILL.md` lives in). Then read `VERSION` to confirm what version you're on.

If the pull fails because of local modifications in this directory, stop and tell the developer instead of forcing it or discarding changes — this directory should only ever contain PHDK's own files, so unexpected local changes are worth a question, not a silent overwrite.

## Step 1 — Determine project state

Check the current project repo for `TASK.md` and `STATUS.md`.

- **Neither exists → this is a new project.** Go to "New Project" below.
- **Both exist → this is an ongoing PHDK project.** Go to "Ongoing Project" below.

## New Project

1. If the human has not been briefed on the project yet (no clear product brief in the conversation), run `SPEC_INTERVIEW_PROMPT.md` first.
2. Run `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md` to generate the kit (`PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md`, `NAVTREE.md`, `PUBLIC_CONTENT.md`, `PRIVATE_CONTENT.md` if login, `TASK.md`, `ARCHITECTURE_DECISIONS.md`, `STATUS.md`, `README.md`), following that file's own generation workflow and question flow exactly — including the backup policy question.
3. **Vendor the standards into the project repo.** Copy this skill's own standards files into a `phdk-standards/` folder inside the target project repo:
   - `VERSION`
   - `ONBOARDING_AI_DEVELOPER.md`
   - `AGENTS.md`
   - `DEVELOPMENT_RULES.md`
   - `DESIGN_RULES.md`
   - `TECHNICAL_STACK.md`
   - `DEVSECOPS.md`
   - `VERSIONING.md`
   - `VERIFICATION_LOOP.md`
   - `DEBUG_DIAGNOSTICS_STANDARD.md`
   - `AI_DEVELOPER_OPERATING_MODEL.md`
   - `AGILE_SLICE_WORKFLOW.md`
   - `QA_CHECKLIST.md`

   This is the full set referenced from `AGENTS.md`'s own required reading order plus the QA gate it points to — anything less would leave a dangling reference once the project is on its own. This makes the project self-contained: any tool working on it afterward — Skill-aware or not, with or without access to this repo — can read the standards locally instead of depending on a live fetch. `VERSION` is what makes the update check below possible — without it, nobody can tell what's vendored.
4. Point the generated `TASK.md` and any onboarding note at `phdk-standards/AGENTS.md` as the required entry point, per `ONBOARDING_AI_DEVELOPER.md`'s reading order.
5. Tell the developer the kit is generated and vendored, and offer to run `BUILD_APP_FOUNDATION_PROMPT.md` next as the first build step. Wait for confirmation before running it — it scaffolds the actual codebase, that's a bigger action than generating docs.

## Ongoing Project

1. Read `phdk-standards/AGENTS.md` if vendored (or this skill's own `AGENTS.md` if not) — it is the router into the rest of the standards.
2. Follow `ONBOARDING_AI_DEVELOPER.md`'s required reading order before touching code.
3. Work per `AI_DEVELOPER_OPERATING_MODEL.md`: small verified working slices, evidence before marking anything complete, stop-and-ask on the conditions listed in `DEVSECOPS.md` and `AI_DEVELOPER_OPERATING_MODEL.md`.
4. Read `TASK.md` and `STATUS.md` in the project repo for current scope and state.
5. If the developer asks to update, sync, or upgrade the project's PHDK standards, go to "Updating Vendored Standards" below. Otherwise, don't check on your own initiative — this is an explicit action, not something to do silently mid-task.

## Updating Vendored Standards

For a project that already has a vendored `phdk-standards/` folder, this refreshes it from this skill's own (Step-0-updated) copy.

1. Compare `phdk-standards/VERSION` in the project against this skill's own `VERSION`. If the project has no `phdk-standards/VERSION` file, treat it as older than everything and say so.
2. If they match, tell the developer the vendored standards are already current and stop — there is nothing to do.
3. If they differ, tell the developer the vendored copy's version, the current version, and ask before proceeding — this changes files the project has committed, it is not silent maintenance.
4. On confirmation, overwrite every file in `phdk-standards/` with this skill's current copy (the same file list as the New Project vendoring step above), so `phdk-standards/VERSION` ends up matching this skill's own.
5. Note the update in the project's `STATUS.md` (old version → new version), same as any other state change. Commit it through the project's normal branch and commit rules — this is not exempt from `DEVELOPMENT_RULES.md`, and it is not on its own grounds for Finetuning Mode.
6. If the developer had modified any file inside `phdk-standards/` directly, flag that before overwriting — those are meant to be a clean mirror of this repo, so local edits there are themselves worth a question.

## Never

- Never regenerate an existing project's kit files through the "New Project" path — that path is for bootstrap only.
- Never skip vendoring when bootstrapping a new project, even if the current tool can read this repo directly — the next tool or session might not be able to.
- Never update `phdk-standards/` in an existing project without telling the developer what version it's moving from and to, and getting confirmation first.
- Never restate a standard inline instead of pointing to its file — this skill stays a router, same as `AGENTS.md`.
