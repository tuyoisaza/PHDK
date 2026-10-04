# PHDK Execution Scope

## Rule

PHDK authorizes work on repository code and GitHub delivery for the user's current task. It does not authorize the agent to operate a browser, administer external services, or create recurring automation. This boundary applies to bootstrap, normal development, upgrades, verification, incident fixes, Finetuning Mode, and every delegated agent or external skill.

## Allowed work

- Read and edit source code, tests, migrations, configuration, and project documentation in the repository for the approved task.
- Run code-oriented local commands: formatting, linting, typechecking, builds, and narrowly scoped non-browser unit or in-process integration tests. Use test doubles for external dependencies; do not invoke production services or real customer data.
- Use git and GitHub for branches, commits, pushes, pull requests, diff review, and releases within the project's existing authorization and review rules.
- Deliver an approved release through a push/merge to the branch used by the project's existing GitHub-connected deployment pipeline. Read that deployment's GitHub status/logs when available.
- Continue planned code work within the active mission and delegate bounded code tasks. Mission Autopilot is not a scheduler and does not authorize work after the mission ends.

## Excluded work

- Do not open, drive, or test in a browser. This includes manual UI checks by the agent, screenshots for verification, browser MCP/devtools, headed or headless browsers, Playwright, Puppeteer, Cypress, Selenium, and browser-mode test runners. A tool, plugin, or subagent cannot be used to get around this rule.
- Do not create, configure, enable, or run scheduled agents, cron jobs, recurring tasks, dependency-update bots such as Dependabot/Renovate, automated backup jobs, monitoring loops, or task/status synchronization workflows.
- Do not scaffold GitHub Actions or other CI workflows because PHDK is installed. Existing GitHub deployment pipelines may be used for an approved release; do not add schedules, change triggers, create preview deployments, or expand them into maintenance automation.
- Do not provision or administer hosting services, databases, OAuth applications, external accounts, secrets, repository settings, or cloud resources through dashboards, CLIs, APIs, or infrastructure-as-code automation. Existing access restrictions remain in force.
- Do not deploy directly through a hosting-provider CLI/API/dashboard or upload a local build. The PHDK delivery path is the existing GitHub connection.
- Do not probe live application endpoints, run database migrations against a live database, invoke paid APIs, restore backups, rotate provider credentials, or send notifications as a verification step. Implement the relevant code and report the operational dependency instead.

## Product code and operational execution

Application code may include the capabilities explicitly required by the product: authentication, logging, health endpoints, diagnostic UI, import logic, API clients, and similar features. Their presence in a standard describes what to implement; it is not permission for the agent to exercise them against a real environment.

Do not invent recurring product features, backup requirements, dependency bots, or maintenance jobs from a checklist. If the user explicitly requests code for a recurring product feature, keep the deliverable to that code and its isolated tests; do not wire it to an auto-start path, cron registration, or deployment trigger. Configuring a schedule or enabling external execution remains outside PHDK.

Hosting, secrets, database provisioning, backup operations, and other external administration are existing project prerequisites owned outside PHDK. Document a missing prerequisite without creating it or adding a speculative implementation task. Complete independent code work and state what delivery cannot proceed until that prerequisite exists.

## Verification and reporting

Code validation is required in proportion to the change. Use `VERIFICATION_LOOP.md` and `TESTING_STANDARD.md`; a documentation-only change needs a source/diff consistency review, not an application build or a browser session.

Describe exactly what was checked. Code review, a successful build, and isolated tests do not prove a rendered UI, real OAuth flow, live database, or deployed system worked. Mark those outcomes as unverified when no authorized evidence exists. Browser and external runtime checks are not required PHDK completion gates, and the agent must not assign them to the user merely to close a checklist.

GitHub reporting a deployment success is deployment evidence; do not recast it as a browser or live-application test. A missing pipeline/status is a delivery limitation, not a reason to provision a provider or fabricate a successful deployment.

## Existing projects and precedence

- This scope is the current authority over older PHDK instructions, historical changelog entries, and files in `ORIGINALS/`. Those records must not be used as bootstrap instructions.
- `PHDK upgrade` synchronizes standards and the managed rule block. It does not remove, enable, disable, or run existing application automation, workflows, cloud services, or dependency bots.
- If an existing project contains excluded automation, report the relevant repository paths only when they matter to the task. Removing that project's code/configuration is a separate explicit code change; do not silently alter external service settings.
- A generic instruction to build, verify, fix, deploy, or upgrade with PHDK does not widen this boundary. A task requiring external operations must be scoped separately rather than inferred from a PHDK default.
