---
name: phdk
description: Use when starting a new project that should follow PHDK standards, generating a PHDK project handoff kit, or when an existing project's AGENTS.md says it follows PHDK and the standards need to be applied. Covers project bootstrap (interview, generate handoff kit, vendor standards into the project) and ongoing development (read standards in the required order, work in verified slices, follow DevSecOps/cost/backup rules).
---

# PHDK

This skill packages the PHDK (Project Handoff to Development Kit) standards and workflow. It does not restate any standard — it routes to the file that already defines it. Read `README.md` in this repo for the full picture; this file only decides which existing PHDK workflow applies right now.

## Step 1 — Determine project state

Check the current project repo for `TASK.md` and `STATUS.md`.

- **Neither exists → this is a new project.** Go to "New Project" below.
- **Both exist → this is an ongoing PHDK project.** Go to "Ongoing Project" below.

## New Project

1. If the human has not been briefed on the project yet (no clear product brief in the conversation), run `SPEC_INTERVIEW_PROMPT.md` first.
2. Run `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md` to generate the kit (`PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md`, `NAVTREE.md`, `PUBLIC_CONTENT.md`, `PRIVATE_CONTENT.md` if login, `TASK.md`, `ARCHITECTURE_DECISIONS.md`, `STATUS.md`, `README.md`), following that file's own generation workflow and question flow exactly — including the backup policy question.
3. **Vendor the standards into the project repo.** Copy this skill's own standards files into a `phdk-standards/` folder inside the target project repo:
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

   This makes the project self-contained: any tool working on it afterward — Skill-aware or not, with or without access to this repo — can read the standards locally instead of depending on a live fetch.
4. Point the generated `TASK.md` and any onboarding note at `phdk-standards/AGENTS.md` as the required entry point, per `ONBOARDING_AI_DEVELOPER.md`'s reading order.

## Ongoing Project

1. Read `phdk-standards/AGENTS.md` if vendored (or this skill's own `AGENTS.md` if not) — it is the router into the rest of the standards.
2. Follow `ONBOARDING_AI_DEVELOPER.md`'s required reading order before touching code.
3. Work per `AI_DEVELOPER_OPERATING_MODEL.md`: small verified working slices, evidence before marking anything complete, stop-and-ask on the conditions listed in `DEVSECOPS.md` and `AI_DEVELOPER_OPERATING_MODEL.md`.
4. Read `TASK.md` and `STATUS.md` in the project repo for current scope and state.

## Never

- Never regenerate an existing project's kit files through the "New Project" path — that path is for bootstrap only.
- Never skip vendoring when bootstrapping a new project, even if the current tool can read this repo directly — the next tool or session might not be able to.
- Never restate a standard inline instead of pointing to its file — this skill stays a router, same as `AGENTS.md`.
