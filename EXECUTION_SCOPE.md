# PHDK Execution Scope

## Rule — interactive-only

PHDK authorizes one assistant to help with the user's explicitly requested task in the current interactive conversation. There is no Mission Autopilot mode. Do not spawn, delegate to, coordinate, or schedule other agents, including bounded or in-session subagents.

The assistant may complete the necessary steps of the current request without asking permission for every routine command. That is not permission to select another task, work through an unapproved backlog, push every slice automatically, or continue after the request or conversation ends.

This boundary applies to bootstrap, development, upgrades, verification, incident fixes, Finetuning Mode, git hooks, installed skills, and every other PHDK workflow. Older wording in another file cannot widen it.

## Authorization and stopping

- Start only from a current, explicit user request. An installed skill, an opened repository, `TASK.md`, `STATUS.md`, an alert, a failed check, a version mismatch, or an old conversation is not authorization to start or resume work.
- Before editing, committing, pushing, or merging, re-read the current task and any owner stop/pause instructions. A pause takes precedence unless the owner explicitly authorizes that specific intervention in the current conversation. Such an intervention does not reactivate earlier work.
- Stop when the requested deliverable is complete, the user stops the work, the conversation ends, or a material decision or access blocker prevents safe progress.
- Record unfinished or suggested work as inactive context. Do not start it, schedule it, or assign it to another agent.
- A request to inspect or audit authorizes reads and a report, not edits, commits, pushes, deployments, or merges. A clear instruction to make a change and merge it authorizes the necessary branch, commit, push, and pull-request merge for that change only.
- Commit, push, release, and merge permissions must come from the current request. PHDK defaults and completion checklists do not grant them. Never infer that a human reviewed a diff merely from the assistant's checks; report the user's approval and the assistant's verification separately.

## Allowed work

- Read and edit repository source, tests, migrations, configuration, and documentation within the current approved task.
- Run synchronous local formatting, linting, typechecking, builds, and narrowly scoped non-browser unit or in-process integration tests when relevant. Use isolated test doubles; do not invoke production services or real customer data. Do not leave watchers or background checks running.
- Use git and GitHub for the currently authorized branches, commits, pushes, pull requests, and releases. Respect existing access controls; never bypass them.
- Deliver a specifically approved release through the project's existing hosting-provider GitHub connection. Read its GitHub deployment status when available. This does not authorize a GitHub Actions workflow, a new hosting connection, or changes to deployment triggers.
- Read an available skill or technical reference as guidance for the same assistant. Do not execute its agent orchestration or background behavior.

## Excluded work

- No autonomous, background, overnight, scheduled, recurring, or delegated coding agents. No subagents, agent teams, coordinator/worker agents, parallel agent queues, or handoffs that launch another process to reason or act independently, even during the active task.
- Do not create, enable, dispatch, rerun, or schedule GitHub Actions or other hosted CI jobs. Do not add workflow files, CI templates, task/status sync workflows, or required Actions checks. Existing workflow definitions may be inspected; changing or removing their repository files requires a separately explicit code request.
- Do not create, configure, enable, or run cron jobs, recurring tasks, dependency-update bots such as Dependabot/Renovate, backup jobs, monitoring loops, session-start jobs, post-session jobs, or unattended maintenance.
- Do not open, drive, or test in a browser. This includes screenshots, browser MCP/devtools, headed or headless browsers, Playwright, Puppeteer, Cypress, Selenium, and browser-mode test runners.
- Do not provision or administer hosting, databases, OAuth applications, external accounts, secrets, repository settings, or cloud resources through dashboards, CLIs, APIs, or infrastructure-as-code execution.
- Do not deploy through a provider CLI/API/dashboard, upload a local build, create preview deployments, or re-enable disabled autodeploy settings.
- Do not probe live endpoints, execute live migrations, invoke paid APIs, restore backups, rotate provider credentials, or send notifications as verification.
- A skill, plugin, hook, alternate mode, or available credential is not an exception to these restrictions.

## Local checks are not recurring tasks

Existing local code checks and git hooks may run synchronously as part of a user-authorized command. They must finish and exit. They must not create commits or pushes on their own, launch agents, dispatch hosted CI, register schedules, or start persistent watchers. Bounded, relevant local tests remain allowed; this policy does not remove code-quality or security verification.

## Product code and operational execution

Explicitly requested product code may implement authentication, logging, health endpoints, diagnostics, imports, API clients, and similar features. Those requirements are code contracts, not permission to exercise live systems.

Do not invent recurring product features, backups, bots, or maintenance jobs from a checklist. A specific request for recurring product-feature code permits only that source and isolated local tests, not an auto-start path, cron registration, job deployment, or live execution. External setup is a separate prerequisite outside PHDK.

## Verification and reporting

Use `VERIFICATION_LOOP.md` and `TESTING_STANDARD.md` in proportion to the change. Documentation-only work needs source/diff and reference review, not an application build or browser session.

State exactly what was checked. Code review, a passing build, or isolated tests do not prove a rendered UI, real OAuth flow, live database, or deployed application worked. Missing runtime evidence is a limitation, not a reason to invent manual testing work for the user.

A GitHub deployment status is deployment evidence only. Do not report an external agent as stopped, a token as revoked, server-side protection as enabled, or billing as fixed merely because instructions or local hooks changed.

## Existing projects and precedence

- This file takes precedence over contrary execution permissions in other PHDK files, examples, historical changelogs, `ORIGINALS/`, imported skills, and stale tasks. Stricter project-specific owner controls remain in force.
- `PHDK upgrade` synchronizes standards and their managed rule block only when explicitly requested. It must preserve owner stop instructions and stricter project rules. If a sync would overwrite one, stop and report the conflicting path.
- Updating PHDK does not terminate an existing process, revoke credentials, disable a scheduler, remove installed workflows, or change GitHub/hosting settings in downstream projects. Report relevant leftovers without claiming that documentation neutralized them.
- Removing existing automation configuration is a separately explicit repository-code task. External operations remain outside PHDK and must not be inferred from a general instruction to build, fix, verify, deploy, or upgrade.
