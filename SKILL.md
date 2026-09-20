---
name: phdk
description: Use when starting a new project that should follow PHDK standards, generating a PHDK project handoff kit, working on an existing project whose AGENTS.md says it follows PHDK, or when the developer says `PHDK upgrade` or otherwise asks to update/sync PHDK. Covers project bootstrap, progressive context loading, verified slices, DevSecOps/cost/backup rules, and synchronizing an already-vendored phdk-standards/ folder to the latest canonical version.
---

# PHDK

This skill packages the PHDK (Project Handoff to Development Kit) standards and workflow. It does not restate any standard — it routes to the file that already defines it. Read `README.md` in this repo for the full picture; this file only decides which existing PHDK workflow applies right now.

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
2. Run `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md` to generate the kit (`PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md`, `NAVTREE.md`, `PUBLIC_CONTENT.md`, `PRIVATE_CONTENT.md` if login, `TASK.md`, `ARCHITECTURE_DECISIONS.md`, `STATUS.md`, `README.md`), following that file's own generation workflow and question flow exactly — including the backup policy question.
3. **Vendor the standards into the project repo.** Read the current `PHDK_MANIFEST.txt` and copy each mapped upstream source into its destination under `phdk-standards/`. Do not maintain a second handwritten file list here — the manifest is the source of truth.

   Vendoring keeps the project self-contained without loading every standard into context. It also installs `PHDK_UPGRADE.md`, `PHDK_MANIFEST.txt`, and `PHDK_NATIVE_RULES.md`, so future upgrades are tool-agnostic.
4. Point the generated `TASK.md` and any onboarding note at `phdk-standards/AGENTS.md` as the required entry point, per `ONBOARDING_AI_DEVELOPER.md`'s reading order.
5. Generate the current tool's native always-loaded rule file per `ENFORCEMENT.md` Tier 2 and include the exact managed block from `phdk-standards/PHDK_NATIVE_RULES.md`. Preserve its `PHDK-MANAGED` markers so `PHDK upgrade` can refresh only that block later without overwriting project-specific instructions.
6. Tell the developer the kit is generated and vendored, and offer to run `BUILD_APP_FOUNDATION_PROMPT.md` next as the first build step — this is also where `ENFORCEMENT.md` Tier 1 (git hooks, local verification gates, branch protection) gets scaffolded. GitHub Actions are not created by default. Wait for confirmation before running it — it scaffolds the actual codebase, that's a bigger action than generating docs.

## Ongoing Project

1. Read `phdk-standards/AGENTS.md` if vendored (or this skill's own `AGENTS.md` if not) — it is the router into the rest of the standards.
2. Read `TASK.md` and `STATUS.md` in the project repo for current scope and state.
3. Follow `AGENTS.md`'s progressive standards router and load only what the current task needs. Use `ONBOARDING_AI_DEVELOPER.md` for orientation, not as a mandatory full-stack preload.
4. Work per the task-relevant PHDK standards: small verified working slices, evidence before marking anything complete, and stop-and-ask at the documented boundaries.
5. If the developer says `PHDK upgrade`, execute `PHDK_UPGRADE.md` immediately. For any other explicit request to update/sync/upgrade PHDK, route to the same file; only the exact canonical command waives the extra confirmation step.
6. If the current task would genuinely benefit from an external skill (heavy UI work, browser-testing evidence, a second security or code-review pass), consult this skill's own `SKILLS_REGISTRY.md` — optional, situational, never installed without asking first.

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
