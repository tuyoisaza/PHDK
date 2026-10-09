# PHDK Standards Repository

**Version: v2.36.1**

PHDK (Project Handoff to Development Kit) is a reusable set of standards for human-directed, AI-assisted software development. It covers project intent, code organization, security, local verification, versioning, and durable repository context.

## Execution model — interactive-only

One assistant works on the user's explicit request in the current conversation. Explicit `PHDK auto` enables continuous development through the entire agreed goal and final integrated verification. There is no legacy Mission Autopilot, delegated-agent allowance, or automatic next mission.

- No subagents, agent teams, autonomous reviewers, or delegated code tasks, even within the active session.
- No unattended, overnight, background, scheduled, or recurring work; no cron jobs, dependency bots, backup jobs, maintenance loops, or task-sync workflows.
- No creation, enabling, dispatch, rerun, or scheduling of GitHub Actions or hosted CI. PHDK contains no Actions workflows and does not require them.
- No browser/headless testing, screenshots, live endpoint/database probes, paid verification calls, or external administration.
- Relevant local formatting, linting, typechecking, builds, and isolated non-browser tests remain allowed. They run synchronously for the current request and exit; they are not background tasks.
- A current implementation/fix/update request includes scoped versioned branch/PR delivery through verified remote `main`, without a repeated merge order. Honor a narrower requested outcome and existing controls. Audits remain read-only; explicitly active Developer Mode supplies only its separate eligible direct-main exception.
- A requested provider check/diagnosis may retrieve bounded existing status, deployment/source/branch/non-secret configuration metadata, and logs through an authorized API/CLI/connector. No browser, continuous monitoring, application probes, secret values, or provider writes are permitted.

The authoritative execution rules are in `EXECUTION_SCOPE.md`. Current owner instructions govern documentary policy; applicable real owner/security/access controls remain in effect. Older files, templates, task snapshots, and external skills cannot veto a current scoped owner instruction or waive an enforced control.

**Finish the requested deliverable, report, and stop.** Old task files, alerts, failures, version mismatches, installed skills, and prior conversations never start work by themselves.

## What changed in v2.36.1

UAT user stories are now intent-first. Every story must trace to the project's current intent, and acceptance uses the chain **Project Intent → User Story → Requirement / Acceptance Criterion → UAT Case → Evidence**.

Stories generated only from implementation details are invalid. Untraceable stories are marked `OUT OF INTENT` and excluded from acceptance counts. UAT cannot conclude ACCEPTED unless the intent-alignment gate passes and all applicable stories are covered.

## What changed in v2.36.0

`PHDK uat` adds autonomous, traceable user acceptance testing for the identified current candidate. It derives use/acceptance cases from roles, requirements, acceptance criteria, current code, and existing test evidence; writes `UAT_CASES.md`; executes every permitted acceptance check it can; and writes `UAT_REPORT.md` with PASS/FAIL/BLOCKED/MANUAL evidence and a final acceptance conclusion.

UAT never converts code inspection into a behavioral PASS. Browser/headless execution, screenshots, live application probes, destructive/live data operations, paid calls, hosted CI dispatch, provider writes, recurring monitoring, and background work remain excluded. Cases that require unavailable or excluded evidence are reported honestly as BLOCKED or MANUAL.

Under an active `PHDK auto` goal, applicable UAT is part of the final whole-goal acceptance boundary. In-scope failures are repaired and the affected cases rerun before final delivery. Standalone `PHDK uat` validates and reports the current candidate without silently expanding into unrelated product development.

## What changed in v2.35.0

`PHDK auto` carries the entire identified development goal through implementation, final integrated verification, in-scope repairs, and normal versioned branch/PR delivery. It does not stop for another human OK after a plan, feature, scaffold, stage, or release candidate. A whole-project request is not silently reduced to an MVP or first release.

Auto writes needed test coverage during implementation and runs planned tests against the completed candidate. Checklists become final coverage, not per-stage acceptance gates. Necessary diagnostic checks and actual mandatory hooks remain applicable when they govern an operation; the complete verification still precedes publication. Source/QA/onboarding/bootstrap instructions now follow this same cadence.

Current scoped owner approval remains sufficient without another PHDK-only human sign-off. Actual repository/security/access controls remain effective. Auto's continuous development is limited to the current goal and active conversation, with no background jobs, browser tests, live probes, provider writes, or persistent authorization flags.

Task records no longer create a second authorization barrier: status/link questions, context compaction, or an assistant-written inactive flag cannot cancel an unfinished request in the same conversation. Real owner stops remain binding. Integration includes routine in-scope conflict/version reconciliation and avoids redundant post-merge bumps or pushes.

Existing GitHub-connected provider autodeploy remains allowed. PHDK must not disable it or install dummy never-matching watch filters to enforce its limits on autonomous work. Observed deployment blockers/statuses are reported separately from integration in `main`; valid service-specific filters and intended skips for unaffected services are normal. Provider configuration writes remain outside a generic development request.

`AGENTS.md` and `SKILL.md` are instruction files, not runnable agents. Loading them does not start a task. Existing local code-check hooks are not schedules and may not launch agents or generate pushes.

## PHDK auto

Activate for the current identified development goal:

```txt
PHDK auto
```

If the goal is already clear in the conversation, the assistant starts immediately. It implements every agreed stage, communicates progress without asking for an OK, then verifies the complete integrated candidate, fixes in-scope failures, and finishes the authorized versioned branch/PR delivery to `main`. The assistant performs the applicable local checks; final human acceptance is not a PHDK prerequisite unless actually requested as one.

Exit with `PHDK salir de auto`, a clear stop, whole-goal completion, or conversation end. Auto replaces Developer Mode for that goal and uses normal branch/PR delivery; it does not inherit direct-main permissions. A real unavailable control/decision/access can block an operation, while independent authorized work continues. No files or examples activate the mode. Full contract: [PHDK_AUTO.md](PHDK_AUTO.md).

## PHDK uat

Run autonomous user acceptance testing for the identified current candidate:

```txt
PHDK uat
```

The assistant first identifies the project's current intent, derives user stories aligned to that intent, then creates or refreshes `UAT_CASES.md`. Each case follows the traceability chain `Project Intent → User Story → Requirement / Acceptance Criterion → UAT Case → Evidence`, then executes every feasible acceptance check through permitted repository-local channels and writes `UAT_REPORT.md`.

The report distinguishes PASS, FAIL, BLOCKED, MANUAL, and NOT APPLICABLE; records the tested revision/version, evidence, defects and coverage gaps; and concludes ACCEPTED, NOT ACCEPTED, or ACCEPTANCE INCOMPLETE. It does not claim browser, production, or human acceptance evidence that did not occur. Full contract: [UAT_STANDARD.md](UAT_STANDARD.md).

## PHDK unlock

Use this command in the current project's conversation:

```txt
PHDK unlock
```

The assistant identifies each blocker's source and actual enforcement, reconciles the requested documentary rules across existing native files and copied PHDK sources, makes bounded in-scope repairs, and finishes the currently authorized delivery to `main`. With no identified current product task, it only repairs the PHDK rules; it does not choose old work or merge every open PR.

Actual failed checks, unavailable access, required formal reviews, and material unresolved decisions remain explicit blockers. The command does not disable them, change provider settings, activate Developer Mode, or create a permanent unlocked state. Clear natural-language approvals and read requests already work without the command. Full procedure: [PHDK_UNLOCK.md](PHDK_UNLOCK.md).

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

## Requested provider diagnostics

For a current request to check Railway or another provider, inspect deployment/version information, or diagnose a specified incident, use an existing authorized API/CLI/connector. Read only relevant existing service/deployment/status/source/branch/non-secret configuration/watch metadata and logs for the identified target. Set finite query bounds, redact sensitive data, and report the evidence's limits. Do not stream, poll, create application traffic, read secret values, change settings, deploy, or grant new access.

The request itself supplies this read authorization, independently of Developer Mode or unlock; a previous task-specific exclusion does not cancel it. Provider evidence is separate from an executed application test or confirmed recovery. Details: [EXECUTION_SCOPE.md — Bounded read-only provider diagnostics](EXECUTION_SCOPE.md#bounded-read-only-provider-diagnostics).

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

The exact command authorizes synchronization now without duplicate confirmation. It does not authorize git delivery, product changes, automation changes, or a future session. Preserve dirty files and genuine owner controls in a bare sync. A current request to remove/reconcile local PHDK exceptions supplies that documentary scope under `PHDK_UNLOCK.md`; a current request to publish supplies its delivery scope. Full procedure: `PHDK_UPGRADE.md`.

An upstream standards update does not update every existing project automatically. It also does not terminate an external process, revoke credentials, disable installed jobs, or change hosting/GitHub settings. Existing projects need their own explicitly requested standards sync; removing old automation is a separate scoped operation.

## Included standards

`PHDK_MANIFEST.txt` is the authoritative mapping of source filenames to their vendored names. Some root filenames are lowercase and become uppercase inside `phdk-standards/`.

| Area | Source files |
|---|---|
| Execution and routing | `AGENTS.md`, `EXECUTION_SCOPE.md`, `MAIN_DELIVERY_STANDARD.md`, `PHDK_AUTO.md`, `UAT_STANDARD.md`, `PHDK_UNLOCK.md`, `PHDK_DEVELOPER_MODE.md`, `PHDK_NATIVE_RULES.md`, `SKILL.md` |
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

Use feature/fix branches by default and respect existing review/access controls. Only explicitly active, low-risk Developer Mode permits its direct-main flow; high-risk changes use normal delivery and the approval rules in `MAIN_DELIVERY_STANDARD.md`. Keep assistant source review, owner approval, any actual formal review, and deployment evidence distinct. Never claim human source inspection or a production health check that did not happen.

Instructions and local hooks do not enforce every external action. A standards commit is not evidence that a running agent stopped, a token was revoked, server-side branch protection was enabled, or costs fell.

## History

See `CHANGELOG.md` for the current release and its preserved historical archive. Historical autonomy instructions are not current operating rules.
