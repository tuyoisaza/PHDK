# PHDK Standards Repository

**Version: v2.33.0**

PHDK (Project Handoff to Development Kit) is a reusable set of standards for human-directed, AI-assisted software development. It covers project intent, code organization, security, local verification, versioning, and durable repository context.

## Execution model — interactive-only

One assistant works on the user's explicit request in the current conversation. There is no Mission Autopilot mode, delegated-agent allowance, or automatic next mission.

- No subagents, agent teams, autonomous reviewers, or delegated code tasks, even within the active session.
- No unattended, overnight, background, scheduled, or recurring work; no cron jobs, dependency bots, backup jobs, maintenance loops, or task-sync workflows.
- No creation, enabling, dispatch, rerun, or scheduling of GitHub Actions or hosted CI. PHDK contains no Actions workflows and does not require them.
- No browser/headless testing, screenshots, live endpoint/database probes, paid verification calls, or external administration.
- Relevant local formatting, linting, typechecking, builds, and isolated non-browser tests remain allowed. They run synchronously for the current request and exit; they are not background tasks.
- A current implementation/fix/update request includes scoped versioned branch/PR delivery through verified remote `main`, without a repeated merge order. Honor a narrower requested outcome and existing controls. Audits remain read-only; explicitly active Developer Mode supplies only its separate eligible direct-main exception.
- A requested diagnosis may retrieve bounded existing logs through an authorized provider API/CLI/connector. No browser, continuous monitoring, application probes, or provider writes are permitted by that exception.

The authoritative rules are in `EXECUTION_SCOPE.md`. They override contrary wording in older documents, examples, and external skills. Stricter owner controls remain in effect.

**Finish the requested deliverable, report, and stop.** Old task files, alerts, failures, version mismatches, installed skills, and prior conversations never start work by themselves.

## What changed in v2.33.0

Normal development now finishes with the requested change and consistent version verified on remote `main`, unless the user specified a narrower outcome. The same current request includes its branch, version, checks, commit, push, PR, required review, and merge. Ordinary changes use assistant diff review; human review remains mandatory for high-risk changes and stricter repository requirements.

Task records no longer create a second authorization barrier: status/link questions, context compaction, or an assistant-written inactive flag cannot cancel an unfinished request in the same conversation. Real owner stops remain binding. Integration includes routine in-scope conflict/version reconciliation and avoids redundant post-merge bumps or pushes.

Existing GitHub-connected provider autodeploy remains allowed. PHDK must not disable it or install dummy never-matching watch filters to enforce its limits on autonomous work. Observed deployment blockers/statuses are reported separately from integration in `main`; valid service-specific filters and intended skips for unaffected services are normal. Provider configuration writes remain outside a generic development request.

`AGENTS.md` and `SKILL.md` are instruction files, not runnable agents. Loading them does not start a task. Existing local code-check hooks are not schedules and may not launch agents or generate pushes.

## Complete the requested delivery

Follow [MAIN_DELIVERY_STANDARD.md](MAIN_DELIVERY_STANDARD.md). For a normal implementation request, use the scoped feature/fix branch, applicable local checks, repository version standard, version-prefixed commits, PR, required review, and merge. Resolve clear integration conflicts while preserving other contributors' work, recheck the result, and verify the remote target and version before calling delivery complete.

A pushed branch or open PR is an intermediate state for a request targeting `main`. Report a real unmet check, material conflict, required review, or access restriction as blocked delivery. A request limited to local work, a branch, or a PR retains that limit. A GitHub PR merge already updates remote `main`; it does not require a second bump or push just to finish.

Preserve the same task's authorization across turns in the active conversation. Compare task/status snapshots with the actual user request and current git/PR state. Do not mistake an old unchecked delivery box for evidence that a merge is still pending or restart old work from a saved record.

## PHDK Developer Mode

Activate explicitly with either command:

```txt
PHDK modo developer
PHDK Developer Mode
```

The assistant briefly explains the permissions. While the conversation remains active, small requested translations, copy, documentation, and simple visual changes may use the existing repository version standard, applicable local checks, a version-prefixed commit, and a fast-forward push directly to `main` when its controls permit it. The push may trigger the deployment already connected to `main`.

Authentication, authorization, secrets, data/migrations, payments, infrastructure, permission-policy changes, and other high-risk work retain normal review. A failed applicable check, rejected/non-fast-forward push, or unsatisfied control stops the direct-main flow. No bypasses, force-pushes, persistent flags, settings changes, provider deployment commands, or autonomous next tasks.

Exit with:

```txt
PHDK salir de developer mode
```

The mode also ends when the user stops the work or the active conversation ends. Documentation, quoted commands, installation, and previous task records never activate or restore it. Full procedure: [PHDK_DEVELOPER_MODE.md](PHDK_DEVELOPER_MODE.md).

## Requested log diagnosis

For an explicit current log or incident diagnosis, use an existing authorized API/CLI/connector to read existing logs for the identified project, service, environment, and deployment. Bound the time window, result count, and timeout; redact sensitive data and report the evidence's limits. Do not follow a live stream, poll, create traffic, change settings, deploy, or grant new access.

This permission is available with or without Developer Mode. It does not turn log evidence into an executed application test. Details: [EXECUTION_SCOPE.md — Bounded read-only log diagnostics](EXECUTION_SCOPE.md#bounded-read-only-log-diagnostics).

## Getting started

For a new project, explicitly request the desired brief/kit and, separately or in the same request, the implementation you want. PHDK does not infer a product-build mission from a documentation-only request.

The assistant reads `AGENTS.md`, `EXECUTION_SCOPE.md`, and the current project's `TASK.md`/`STATUS.md`, then loads only the task-relevant standards. If the product goal is unclear, use `SPEC_INTERVIEW_PROMPT.md`; generate a kit with `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md`. Use the foundation prompt only for an explicitly requested build.

## Install as a skill

Installation is a user-requested file operation, not a background service. For the tool currently in use, clone PHDK directly into that tool's skill folder so `SKILL.md` is at its root. Keep the installed copy clean and update it only when requested; do not add schedules or startup/update jobs.

Existing installation locations documented by PHDK:

| Tool | Project-local folder |
|---|---|
| Claude Code | `.claude/skills/phdk` |
| Cursor | `.cursor/skills/phdk` |
| Codex CLI / Antigravity | `.agents/skills/phdk` |
| Windsurf | `.windsurf/skills/phdk` |
| VS Code / GitHub Copilot | `.github/skills/phdk` |
| OpenCode | `.opencode/skills/phdk` |
| Pi | `.pi/skills/phdk` |

Example for a currently authorized Claude Code installation:

```sh
git clone https://github.com/tuyoisaza/PHDK.git .claude/skills/phdk
```

Use the corresponding folder for the tool in use. Do not install multiple tools or delegation plugins speculatively. Tool discovery may load the instructions, but execution still requires the current human request.

## Universal upgrade command

```txt
PHDK upgrade
```

The command fetches canonical `main`, reads `VERSION`, synchronizes the `PHDK_MANIFEST.txt` mappings into `phdk-standards/`, refreshes the current tool's marked `PHDK_NATIVE_RULES.md` block, verifies the copy, reports, and stops.

The exact command authorizes synchronization now without duplicate confirmation. It does not authorize git delivery, product changes, automation changes, or a future session. Preserve dirty files and stricter owner controls; stop if they would be overwritten. Full procedure: `PHDK_UPGRADE.md`.

An upstream standards update does not update every existing project automatically. It also does not terminate an external process, revoke credentials, disable installed jobs, or change hosting/GitHub settings. Existing projects need their own explicitly requested standards sync; removing old automation is a separate scoped operation.

## Included standards

`PHDK_MANIFEST.txt` is the authoritative mapping of source filenames to their vendored names. Some root filenames are lowercase and become uppercase inside `phdk-standards/`.

| Area | Source files |
|---|---|
| Execution and routing | `AGENTS.md`, `EXECUTION_SCOPE.md`, `MAIN_DELIVERY_STANDARD.md`, `PHDK_DEVELOPER_MODE.md`, `PHDK_NATIVE_RULES.md`, `SKILL.md` |
| Current-request workflow | `AI_DEVELOPER_OPERATING_MODEL.md`, `AGILE_SLICE_WORKFLOW.md`, `TASK_TRACKING_STANDARD.md` |
| Intent and onboarding | `INTENT_CAPTURE_STANDARD.md`, `ONBOARDING_AI_DEVELOPER.md`, `SPEC_INTERVIEW_PROMPT.md` |
| Code and local enforcement | `DEVELOPMENT_RULES.md`, `ENFORCEMENT.md`, `INANUTSHELL.md` |
| Architecture and design | `technical_stack.md`, `design_rules.md` |
| Security and diagnostics | `DEVSECOPS.md`, `DEBUG_DIAGNOSTICS_STANDARD.md` |
| Verification | `VERIFICATION_LOOP.md`, `TESTING_STANDARD.md`, `qa_checklist.md` |
| Versioning and upgrades | `VERSIONING.md`, `PHDK_UPGRADE.md`, `PHDK_MANIFEST.txt`, `VERSION` |
| Bootstrap | `build_app_foundation_prompt.md`, `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md` |
| Optional reading references | `SKILLS_REGISTRY.md` |
| History | `CHANGELOG.md`, `ORIGINALS/` |

## Product-code defaults

The execution change does not remove PHDK's implementation standards. Defaults remain pnpm/Turborepo, Next.js, NestJS/Fastify, Drizzle/PostgreSQL, custom Google OAuth, server-side authorization, i18n, safe diagnostics, structured logs, traceable version metadata, real-data states, and bounded cost controls.

Product-specific choices belong in `ARCHITECTURE_DECISIONS.md`. They describe source requirements, not permission to provision infrastructure, operate a browser, run live migrations, or launch agents.

## Delivery and verification

An explicitly approved push/merge, including an eligible Developer Mode push, may use the project's existing hosting-provider GitHub connection. This is not permission to add or run a GitHub Actions workflow, create a deployment connection, alter triggers, re-enable autodeploy, or deploy through Railway/provider CLI/API/dashboard.

Use feature/fix branches by default and respect existing repository review/access controls. Only the explicitly active, low-risk Developer Mode flow permits direct-main delivery; high-risk changes retain normal review. Keep actual source verification, user authorization, human diff review, and deployment status distinct. Never claim a human review or production health check that did not happen.

Instructions and local hooks do not enforce every external action. A standards commit is not evidence that a running agent stopped, a token was revoked, server-side branch protection was enabled, or costs fell.

## History

See `CHANGELOG.md` for the current release and its preserved historical archive. Historical autonomy instructions are not current operating rules.
