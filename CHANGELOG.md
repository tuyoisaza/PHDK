# CHANGELOG.md

All notable changes to the PHDK standards are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## v2.13.0 — 2026-08-09

### Theme: Railway Deployment Setup

A real incident surfaced the gap this closes: PHDK stated the deployment *rules* everywhere (never deploy from local CLI, GitHub push triggers deploy, two Railway services at repo root) but never the *procedure* for connecting Railway to GitHub the first time. Without it, an agent asked to deploy improvised — and uploaded a local build as a tarball to Railway, which is exactly what "never deploy from local CLI" was meant to prevent. The rule existed; the path to follow instead didn't.

### Added

- `TECHNICAL_STACK.md` — new "First-time Railway Setup" procedure under Deployment, numbered end-to-end: commit with the version bumped per `VERSIONING.md`, push to GitHub, create the Railway project via "Deploy from GitHub repo" (explicitly not `railway up` or a tarball upload), create the two services against the same repo, set root directory/build/start commands per service, set env vars in the Railway dashboard, then verify the live deploy against `VERIFICATION_LOOP.md` Health Check Standard. After this one-time setup, every push to `main` deploys on its own.

### Changed

- `AGENTS.md`, `DEVSECOPS.md`, `DEVELOPMENT_RULES.md`, `QA_CHECKLIST.md` — every existing "never deploy from local CLI" rule and checklist item now names the actual trap (`railway up`, local build/tarball upload) instead of staying generic, and points to the new setup procedure as what to do instead.

### Canonical Decisions

- The only supported path to a live deployment is: commit (versioned) → push to GitHub → Railway's GitHub-connected pipeline. There is no CLI-based or manual-upload alternative, ever.

---

## v2.12.0 — 2026-08-09

### Theme: LSP / Code Intelligence Setup

Adds a standard for setting up and verifying real code-intelligence (Language Server Protocol) support, adapted from a general-purpose proposal down to PHDK's fixed stack — TypeScript strict mode, pnpm workspaces, Turborepo — so the language/server choice isn't a per-project decision, it's already `typescript-language-server`.

### Added

- `TECHNICAL_STACK.md` — new "LSP / Code Intelligence Setup" section: required setup (project references across `apps/*`/`packages/*`, Drizzle-generated types resolved, Next.js/NestJS type support, no duplicate `tsconfig.json`), required verification on a real symbol (diagnostics, go-to-definition across package boundaries, find-references, rename, hover, workspace symbols), and the sharpest part of the source proposal carried through as-is: a working editor LSP does not mean the AI agent has the same capability — confirm and report which one is actually available, since grep-based search misses what a real LSP catches.
- `BUILD_APP_FOUNDATION_PROMPT.md` — new Quality Gates item: full LSP setup and verification happens once, at foundation build.
- `ONBOARDING_AI_DEVELOPER.md` — new session-start step: a quick LSP smoke-check (diagnostics + go-to-definition on a real symbol), not the full verification loop every session.
- `QA_CHECKLIST.md` — new "LSP / Code Intelligence QA" section, nine checks.

### Changed

- `AGENTS.md` — `TECHNICAL_STACK.md` router description updated to mention LSP/code intelligence setup
- `README.md` — new LSP setup canonical decision row

### Canonical Decisions

- `typescript-language-server` is the canonical LSP for all PHDK projects. Full setup and verification happens once at foundation build, not every session. Whether the AI agent itself has direct LSP access or only text-search access must be confirmed and reported, never assumed.

---

## v2.11.5 — 2026-08-09

### Fixed

- `README.md` — Quick Start showed only the Claude Code `git clone` command, making PHDK look Claude-Code-only at the top of the page even though 7 other tools are supported. Replaced it with the same tool-agnostic self-installing prompt already used in "Trigger it" — the AI picks the right per-tool command itself, so Quick Start no longer favors or excludes any tool. The later "Trigger it" section now points back to Quick Start instead of duplicating the same prompt block twice on one page.

---

## v2.11.4 — 2026-08-09

### Fixed

Pre-publish audit found two real gaps in the vendoring/bootstrap flow added in v2.9.0–v2.11.3:

- `SKILL.md` — `ONBOARDING_AI_DEVELOPER.md` and `QA_CHECKLIST.md` were missing from the vendored file list, even though both are referenced from files that *are* vendored (`ONBOARDING_AI_DEVELOPER.md` is item 1 of `AGENTS.md`'s own required reading order; `QA_CHECKLIST.md` is the QA gate pointed to from `DEVSECOPS.md`, `TECHNICAL_STACK.md`, and `DEVELOPMENT_RULES.md`). A bootstrapped project had dangling references to files it didn't actually have. Both added to the vendored set.
- `SKILL.md` New Project flow and `README.md` "For a new project" — neither ever ran or mentioned `BUILD_APP_FOUNDATION_PROMPT.md`, the standard's own "first build prompt after the kit is generated." The kit was generated and vendored, but the actual foundation build step was silently skipped. Both now include it as an explicit next step (offered, with confirmation before running, since it scaffolds real code).

---

## v2.11.3 — 2026-08-09

### Added

- `SKILL.md` — new "Updating Vendored Standards" workflow: for a project that already has a vendored `phdk-standards/` folder, compares `phdk-standards/VERSION` against this skill's own (kept current by Step 0), tells the developer what's changing, and only overwrites `phdk-standards/` after explicit confirmation — never silently, never on its own initiative mid-task. Notes the update in the project's `STATUS.md` and goes through the project's normal branch/commit rules like any other change.
- `QA_CHECKLIST.md` — Documentation QA now checks that a vendored `phdk-standards/VERSION` matches the current PHDK standards version, or that the gap is flagged.

### Fixed

- `SKILL.md` — `VERSION` was missing from the vendored file list added in v2.9.0, which meant a bootstrapped project had no way to know which PHDK standards version it was carrying. Added, and it's what makes the update check above possible.

### Changed

- `SKILL.md` frontmatter `description` — now also triggers on "update/sync/upgrade the project's vendored PHDK standards"
- `README.md` — "What happens once it's installed" now documents the update-vendored-standards case

---

## v2.11.2 — 2026-08-09

### Changed

- `SKILL.md` — new "Step 0 — Keep this skill current": before doing anything else, `git pull` inside the skill's own directory so the standards are always current, reading `VERSION` to confirm. If the pull fails due to local modifications, stop and ask rather than force or discard.
- `README.md` — the "Trigger it" prompt now doubles as the update command: paste it again anytime and it installs fresh if missing, or pulls latest if already installed, before using the skill.

---

## v2.11.1 — 2026-08-09

### Changed

- `README.md` — the "Trigger it" copy-paste prompt now also tells the AI to install the skill itself, if it isn't already, using whichever per-tool command from "Install as an Agent Skill" matches the tool it's running in. One prompt now covers both the manual-clone-then-trigger flow and the fully self-installing flow, instead of assuming the `git clone` step already happened.

---

## v2.11.0 — 2026-08-09

### Theme: Indirect Prompt Injection

Adds Indirect Prompt Injection as its own named threat category for any LLM-powered feature — distinct from the direct-injection guardrails already in place (v2.7.0) and distinct from classical injection (SQL/command injection). Also closes a gap: command injection was never explicitly named alongside SQL injection in the Security QA checklist.

### Added

- `DEVSECOPS.md` — new "Indirect Prompt Injection" subsection under LLM Integration Safety: defines the category (payload hidden in externally-fetched content — scraped pages, CMS fields like a WordPress `post_content`, uploaded files, third-party API responses — that the model, not a deterministic parser, may interpret as instructions instead of data), maps it to OWASP Top 10 for LLM Applications (LLM01 indirect subtype, LLM08 Excessive Agency) and MITRE ATLAS (AML.T0051), and requires: external content always treated as data, action-triggering scoped to the authenticated user's own request, per-resource/per-tenant credential scoping (no single broadly-scoped key across sites/tenants — the "confused deputy" failure mode), a confirmation gate before destructive actions, structural delimiting of external content in prompts, and logging/flagging of unrequested action-like model output. Added to Applies To, Core Rules, Stop-and-Ask Conditions, and Verification.
- `QA_CHECKLIST.md` — "Command injection risk reviewed" added to Security (classical injection was missing this alongside SQL injection); five new indirect-injection checks added to AI / LLM Configuration QA

### Changed

- `TECHNICAL_STACK.md` — AI / LLM Integration section cross-references the new indirect-injection guardrails
- `README.md` — new Prompt injection canonical decision row

### Canonical Decisions

- Any LLM feature requires both direct and indirect prompt injection guardrails — not interchangeable, both required, alongside (not instead of) classical SQL/command injection protection

---

## v2.10.0 — 2026-08-09

### Theme: Finetuning Mode

Adds one narrow, explicit exception to "never commit directly to `main`": a pre-production, verbally-activated iteration mode for the window after core development is functionally complete but before the project has real users.

### Added

- `DEVELOPMENT_RULES.md` — new "Finetuning Mode" section: applies only pre-production (refuses to activate if the project already has live production traffic — recommend a sandbox instead), activated verbally per-conversation only (never persisted in `TASK.md`/`STATUS.md`, never assumed, never carried into a new conversation), and while active relaxes exactly one thing — for each requested change, make it, run tests, and only on a pass commit and push directly to `main`. Every other standard (DevSecOps, cost safety, backup policy, stop-and-ask conditions, versioning) still applies in full.

### Changed

- `AGENTS.md`, `DEVSECOPS.md`, `AI_DEVELOPER_OPERATING_MODEL.md`, `VERSIONING.md` — every existing "never commit/push directly to `main`" rule and stop-and-ask condition now cross-references Finetuning Mode as the one standing, explicitly-scoped exception
- `README.md` — new Finetuning Mode canonical decision row

### Canonical Decisions

- Direct push to `main` stays forbidden by default. Finetuning Mode is the only exception, and it is scoped tightly: pre-production only, activated verbally for the current conversation only, and every other safety rule still applies

---

## v2.9.3 — 2026-08-09

### Added

- `README.md` — install commands for three more Skill-aware tools: OpenCode (`.opencode/skills/phdk`), Pi (`.pi/skills/phdk`), and Antigravity (`.agents/skills/phdk`, shared with Codex CLI) — verified against each tool's actual skill-discovery paths before publishing
- `README.md` — a "Trigger it" copy-paste prompt to paste after cloning, for tools that don't auto-discover the skill or when the user wants to invoke it explicitly; notes Pi's `/skill:phdk` explicit-invocation syntax

### Changed

- `ONBOARDING_AI_DEVELOPER.md` — Skill-aware tool list updated to include OpenCode, Pi, and Antigravity

---

## v2.9.2 — 2026-08-09

### Changed

- `README.md` — replaced the per-tool directory table with a standalone, one-line copy-paste `git clone` command for each tool (Claude Code, Cursor, Codex CLI, Windsurf, VS Code/Copilot), so each install command has its own GitHub copy button instead of requiring manual path substitution.

---

## v2.9.1 — 2026-08-09

### Changed

- `README.md` — turned the GitHub front page into a proper landing page for the Agent Skill install path: a "Quick Start" block right under the intro with a one-line clone command, and an expanded "Install as an Agent Skill" section with a verified per-tool skill-directory table (Claude Code, Cursor, Codex CLI, Windsurf, VS Code/Copilot) plus the cross-tool `.agents/skills/` option and the user-level global install path.

---

## v2.9.0 — 2026-08-09

### Theme: Agent Skill Packaging

Packages PHDK as an Agent Skill — the open, portable standard for on-demand agent capabilities (Claude Code, Cursor, Codex CLI, Windsurf, VS Code) — as an additional, additive distribution path alongside the existing `AGENTS.md` router and copy-paste prompt paths.

### Added

- `SKILL.md` — new repo-root skill entry point. A thin router (same philosophy as the `AGENTS.md` rebuild in v2.7.1): branches on whether the target repo has `TASK.md`/`STATUS.md` yet. New projects run `SPEC_INTERVIEW_PROMPT.md` (if needed) then `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md`, then vendor the standards files into a `phdk-standards/` folder in the new project repo. Ongoing projects follow `ONBOARDING_AI_DEVELOPER.md`'s required reading order. No standard is restated inline.

### Changed

- `README.md` — new "As an Agent Skill" subsection under How to Use This Repo, plus `SKILL.md` added to the Included Files table
- `ONBOARDING_AI_DEVELOPER.md` — note that `SKILL.md` is an alternate entry point in Skill-aware tools

### Notes

Not published to a public skill registry (skills.sh) — PHDK is a private/team standards repo, install manually by copying this repo into the tool's skills directory. This also resolves the "not every IDE can read our GitHub repo" gap raised earlier: the skill's own bootstrap action vendors the standards into the new project, so any tool can read them locally afterward regardless of Skill or GitHub-fetch support.

---

## v2.8.0 — 2026-08-08

### Theme: Data Backup Policy

Adds a mandatory standard: every project must have an explicit backup policy for its live application data (the database), decided during kit generation and recorded as an architecture decision. This is separate from code backup — GitHub is always the code backup and was never in question.

### Added

- `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md` — new Question 3 (renumbering brand → Question 4, corrections → Question 5) that always asks for the database backup policy and offers two simple recommended defaults: a weekly Monday full SQL export emailed to the developer, or a weekly SQL dump committed to a dated git backup branch in the private repo. New "Backup Policy Rule" branching section records the answer in `ARCHITECTURE_DECISIONS.md`, including the case where the developer explicitly says no policy yet.
- `TECHNICAL_STACK.md` — new "Data Backup Policy" subsection under Database: the two recommended defaults, retention, and restore-verification requirements
- `DEVSECOPS.md` — new "Data Backup and Recovery Safety" section: encryption/password-protection for emailed dumps containing sensitive data, private-repo-only rule and retention for git backup branches, and "never assume a policy exists" rule; added to Applies To, Stop-and-Ask Conditions, and Verification
- `QA_CHECKLIST.md` — new backup checks under Database: policy recorded, job runs and is monitored, sensitive dumps protected, backup branches private-only, restore tested at least once

### Canonical Decisions

- Every project has an explicit, recorded data backup policy for its database before it is considered production-ready — "no policy" must be an explicit dated decision, never a default by omission

---

## v2.7.2 — 2026-08-08

### Fixed

- `DEBUG_DIAGNOSTICS_STANDARD.md` and `QA_CHECKLIST.md` — the standard listed the copy diagnostics and clear cache buttons but never specified their placement. Both now explicitly require the clear cache button to sit immediately next to the copy diagnostics button, everywhere the pair is specified (Required UI Controls, Debug Mode Behavior, version badge component, QA checks).

---

## v2.7.1 — 2026-08-08

### Theme: AGENTS.md as Cross-Tool Router

`AGENTS.md` is now an open, Linux Foundation-governed specification read natively by 30+ AI coding tools (Claude Code, Cursor, Windsurf, GitHub Copilot, Codex, Gemini CLI, Aider, Devin, Amazon Q). This release restructures PHDK's own `AGENTS.md` to match how the spec is meant to be used: a short entry point that routes agents to the rest of the standards, not a second copy of them.

### Changed

- `AGENTS.md` — trimmed from ~290 to ~180 lines. Sections that fully duplicated content already specified in `TECHNICAL_STACK.md` (Monorepo Structure, AI/LLM Feature Requirements), `DEVSECOPS.md` (Authentication Standard), `VERSIONING.md` (Version Requirements), and `DEVELOPMENT_RULES.md` (Code Organization Rules) were replaced with one-line pointers to the authoritative file. Required Reading Order, Core Agent Rules, Public-Only Project Rule, Required Product Baseline/Roles/Routes, Agent Completion Checklist, and Things Agents Must Never Do stay inline since they are not duplicated elsewhere.

### Notes

Duplicated content across files was also the root cause of several of the v2.5.0 consistency bugs fixed in v2.5.1 (a rule stated in one file and contradicted in another because both carried their own copy). Routing instead of duplicating removes that failure mode going forward.

This does not change any project-facing tool or file distribution mechanism (vendoring standards into generated project repos, optional SKILL.md packaging) — that remains open for a future release.

---

## v2.7.0 — 2026-08-08

### Theme: AI/LLM Admin Manageability and Guardrails

Adds a mandatory standard for any feature that calls an LLM: the prompt, expected output, provider, model, and live per-model pricing must be admin-manageable from `/admin/ai`, and every integration must guard against prompt injection and validate output before use.

### Added

- `TECHNICAL_STACK.md` — new "AI / LLM Integration — packages/ai" section: config-driven provider/model, admin-manageable prompt and output schema, injection guardrails, output validation, audit logging, and a "refresh model pricing" admin action
- `AGENTS.md` — new "AI/LLM Feature Requirements" section and `/admin/ai` conditional route
- `DEVSECOPS.md` — new "LLM Integration Safety" section: guardrails, output validation, audit logging, pricing visibility, and rules against unbounded pricing-refresh calls; added to Applies To, Core Rules, Stop-and-Ask Conditions, and Verification
- `QA_CHECKLIST.md` — new "AI / LLM Configuration QA" section

### Canonical Decisions

- Every LLM-powered feature requires: config-driven provider/model selection, an admin-manageable prompt and output schema, prompt-injection guardrails, output validation, audit logging on config changes, and a live per-model pricing lookup in the admin panel

---

## v2.6.0 — 2026-08-08

### Theme: Cost and Consumption Safety

Adds a mandatory safeguard standard for any integration billed by usage (AI/image/video generation, LLM calls, SMS, email sending, and other metered APIs), so a runaway loop or retry storm cannot burn unbounded money before anyone notices.

### Added

- `DEVSECOPS.md` — new "Cost and Consumption Safety" section: required hard usage caps, request timeouts, max retry/loop limits, idempotency guards, kill switches, per-user quotas, spend logging and alerting; added to Applies To, Core Rules, Stop-and-Ask Conditions, and Verification
- `DEBUG_DIAGNOSTICS_STANDARD.md` — new "Metered API / Cost Diagnostics Requirements" section and QA items, so a runaway metered call is visible in the diagnostics report

### Changed

- `AGENTS.md` — added metered/paid API rule to "Things Agents Must Never Do"
- `AI_DEVELOPER_OPERATING_MODEL.md` — added metered/paid API rule to Stop-and-Ask Conditions
- `QA_CHECKLIST.md` — added "Cost and Consumption Safety" QA section
- `README.md` — added Cost safety canonical decision

### Canonical Decisions

- Every metered/paid external API requires a hard usage cap, timeout, retry limit, and kill switch before it ships — no exceptions, no "add it later"

---

## v2.5.1 — 2026-08-07

### Theme: Post-Update Consistency Review

### Changed

- **Database standard reverted to PostgreSQL-only.** v2.5.0 introduced SQLite for local development; this was reverted. All environments, including local development, use PostgreSQL — no SQLite anywhere. Updated `TECHNICAL_STACK.md`, `DEVELOPMENT_RULES.md`, `README.md`.
- `BUILD_APP_FOUNDATION_PROMPT.md` — fixed leftover `WORKOS_API_KEY`/`CLERK_SECRET_KEY` env var example, replaced with the Google OAuth 2.0 env vars used everywhere else in the standard.
- `QA_CHECKLIST.md` — fixed the auth checklist item that still named WorkOS/Clerk as the approved default provider; now references custom Google OAuth 2.0.
- `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md` — fixed version header mismatch (was still v1.5 while CHANGELOG recorded it as bumped to v1.6); filled in the standards repo URL placeholder with `https://github.com/tuyoisaza/PHDK`.
- `README.md` — filled in the standards repo URL placeholder in the "new AI coder session" instructions.

### Notes

This release corrects internal inconsistencies introduced by the v2.5.0 update package that were not caught before merge: a canonical decision that contradicted its own QA gate, stale env var examples from the pre-Google-OAuth auth standard, and unfilled repo URL placeholders.

---

## v2.5.0 — 2026-08-06

### Theme: AI Developer Operating Model

This version upgrades PHDK from a standards repo for AI coding to an AI developer operating system.

### Added

- `AI_DEVELOPER_OPERATING_MODEL.md` — core doctrine for AI developers: ethos, telos, rule levels, autonomous work model, working slice doctrine, stop-and-ask conditions, feedback loop, and final report format
- `SPEC_INTERVIEW_PROMPT.md` — optional pre-brief interview prompt that guides the AI to interview for human context before generating a PHDK kit
- `AGILE_SLICE_WORKFLOW.md` — working slice model to replace waterfall-style AI development; defines slice lifecycle, sizing rules, backlog management, and anti-patterns
- `VERIFICATION_LOOP.md` — defines what counts as proof; required evidence types, health check standard, deep health check standard, verification by slice type, and honest reporting rules
- `DEBUG_DIAGNOSTICS_STANDARD.md` — complete copy diagnostics report specification, debug mode behavior, auth diagnostics requirements, UI controls, and QA checklist
- `DEVSECOPS.md` — security and operational safety baseline covering auth, authorization, sessions, logging, dependencies, environment variables, deployment, and stop-and-ask conditions
- `VERSIONING.md` — version, branch, commit, changelog, release, and visible build metadata standards
- `ONBOARDING_AI_DEVELOPER.md` — required reading order, standards file definitions, session start procedure, rule levels, and what AI developers must never do

### Changed

- `AGENTS.md` — added AI Developer Operating Model section, added autonomous work rules, added public-only project clarification, updated required reading list
- `TECHNICAL_STACK.md` — replaced WorkOS and Clerk with custom Google OAuth 2.0 auth standard, added Google OAuth credential setup instructions, updated environment variables
- `BUILD_APP_FOUNDATION_PROMPT.md` — added new standards files to required reading, updated auth to custom Google OAuth 2.0, added slice completion rule, added diagnostics requirement, updated first task instruction
- `QA_CHECKLIST.md` — added AI Developer Operating Model QA, Working Slice QA, Verification Loop QA, Google OAuth 2.0 QA, Debug Diagnostics QA, Deep Health QA sections
- `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md` — updated TASK.md template with working slice section, updated first generated task, updated auth references, added new standards files to reference list, updated to v1.6
- `DEVELOPMENT_RULES.md` — removed WorkOS and Clerk references, updated auth standard
- `README.md` — added v2.5 direction, updated included files list, updated canonical decisions

### Removed

- All references to WorkOS as a default auth provider
- All references to Clerk as a default auth provider
- `BOOTSTRAP_MONOREPO_PROMPT.md` — replaced by `BUILD_APP_FOUNDATION_PROMPT.md` in v2.0

### Canonical Decisions

- Auth: custom Google OAuth 2.0 by default; no paid auth vendor by default
- Working slice model replaces waterfall-style development
- Verification evidence required before every slice is marked complete
- Deep health check standard added as verification requirement

---

## v2.0.0 — 2026-05-07

### Theme: Foundation Prompt and Standards Consolidation

### Added

- `BUILD_APP_FOUNDATION_PROMPT.md` — replaced `BOOTSTRAP_MONOREPO_PROMPT.md` with a project-mode-aware foundation prompt supporting public, authenticated, hybrid, and unclear modes

### Changed

- All references to `BOOTSTRAP_MONOREPO_PROMPT.md` updated to `BUILD_APP_FOUNDATION_PROMPT.md`
- `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md` updated to v1.5 with hard mode switch, project name confirmation, canvas mode awareness, and correction loop

### Removed

- `BOOTSTRAP_MONOREPO_PROMPT.md` — replaced by `BUILD_APP_FOUNDATION_PROMPT.md`

---

## v1.0.0 — Initial Release

### Added

- `AGENTS.md`
- `DEVELOPMENT_RULES.md`
- `DESIGN_RULES.md`
- `TECHNICAL_STACK.md`
- `QA_CHECKLIST.md`
- `BOOTSTRAP_MONOREPO_PROMPT.md`
- `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md`
- `README.md`
