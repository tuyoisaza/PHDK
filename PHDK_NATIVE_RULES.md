<!-- PHDK-MANAGED:START -->
## PHDK managed rules

- Read `phdk-standards/AGENTS.md` and `phdk-standards/EXECUTION_SCOPE.md` before project work. Read `TASK.md` and `STATUS.md` before changing code.
- PHDK acts only on repository code/docs, local code validation, git/GitHub, and approved deployment through an existing GitHub-connected pipeline. Do not provision or administer external services, databases, secrets, OAuth accounts, or repository settings.
- Never open, drive, or test in a browser, including headless runners, screenshots, browser MCP/devtools, Playwright/Puppeteer/Cypress/Selenium, or delegated browser work.
- Never create scheduled agents, recurring tasks, cron jobs, Dependabot/Renovate, backup jobs, maintenance workflows, or preview deployments. Do not scaffold CI workflows or alter the existing deployment pipeline's triggers.
- Canonical upgrade command: **`PHDK upgrade`**. When the developer gives that exact command, execute `phdk-standards/PHDK_UPGRADE.md` immediately. The command itself is approval to synchronize PHDK-managed files; do not ask for a second confirmation.
- **Mission Autopilot applies to the active code task:** once `TASK.md` defines a clear goal/scope/Done When, keep working across planned slices within the execution boundary until complete or blocked. Never ask "continue?" between planned slices or schedule work after the mission ends.
- Verified slices may be committed and pushed autonomously to the mission feature branch. Never commit directly to `main` unless Finetuning Mode is explicitly active. Never force-push; Human Diff Review is still required before merge to `main`.
- Never weaken auth, RBAC, validation, privacy, or cost controls merely to make a feature work.
- Verify source/diffs and use appropriate local format/lint/typecheck/build commands plus risk-triggered non-browser unit/in-process tests. Do not probe live endpoints, databases, or metered APIs. Report visual/live-runtime results as unverified when evidence is absent; they are not mandatory PHDK gates.
- Stop before out-of-scope repository changes or auth/payment/tenant architecture changes. External administration and live data operations remain outside PHDK; product API code still requires hard caps and kill switches.
- Preserve project memory in `TASK.md` and `STATUS.md`; do not treat chat memory as the source of truth.
<!-- PHDK-MANAGED:END -->
