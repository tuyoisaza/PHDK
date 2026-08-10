# PHDK Standards Repository

**Version: v2.9.0**

This repository contains the reusable PHDK standards for AI-assisted software development.

---

## What PHDK Is

PHDK (Project Handoff to Development Kit) is a disciplined operating model for AI-assisted software development.

It is not a rigid religion of tools. It is a framework that teaches AI developers how to think, work in slices, verify their work, preserve context, and produce useful software.

**The ethos of PHDK:** disciplined, honest, human-centered AI development.

**The telos of PHDK:** useful working software that serves real people, preserves context, moves safely, verifies itself, and improves through feedback.

---

## How to Use This Repo

### For a new project

1. Generate a project-specific PHDK kit using `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md`
2. The generated kit references this standards repo
3. Give your AI coder the kit and tell it to fetch the latest standards from this repo before starting

### For a new AI coder session

Tell the AI coder:

```txt
Read the PHDK standards from https://github.com/tuyoisaza/PHDK in this order:
1. ONBOARDING_AI_DEVELOPER.md
2. AI_DEVELOPER_OPERATING_MODEL.md
3. AGENTS.md
4. DEVELOPMENT_RULES.md
5. DESIGN_RULES.md
6. TECHNICAL_STACK.md
7. DEVSECOPS.md
8. VERSIONING.md
9. VERIFICATION_LOOP.md
10. DEBUG_DIAGNOSTICS_STANDARD.md
Then read TASK.md and STATUS.md from the project repo.
```

### As an Agent Skill

This repo is also packaged as an Agent Skill (`SKILL.md` at the repo root) — the open, portable standard for on-demand agent capabilities, supported by Claude Code, Cursor, Codex CLI, Windsurf, and VS Code. This is additive, not a replacement for the two paths above.

To install: copy or clone this repo into the tool's skills directory (for Claude Code, `.claude/skills/phdk/`). Once installed, the skill triggers automatically when starting a new PHDK project or working on one that already follows PHDK, and it handles vendoring the standards into the project repo so later sessions — in any tool, Skill-aware or not — can read them locally.

Not published to a public skill registry (skills.sh) — PHDK is a private/team standards repo, install manually.

---

## Included Files

### Onboarding and Operating Model

| File | Purpose |
|------|---------|
| `ONBOARDING_AI_DEVELOPER.md` | Required reading order and session start procedure |
| `AI_DEVELOPER_OPERATING_MODEL.md` | Core doctrine: ethos, slices, autonomy, verification, feedback loop |
| `SPEC_INTERVIEW_PROMPT.md` | Optional pre-brief interview tool for new projects |
| `SKILL.md` | Agent Skill packaging — routes to bootstrap or ongoing-project workflow |

### Development Standards

| File | Purpose |
|------|---------|
| `AGENTS.md` | Agent rules, completion checklist, things never to do |
| `DEVELOPMENT_RULES.md` | Branching, commits, file rules, feature structure |
| `DESIGN_RULES.md` | UI, UX, accessibility, theming, responsive rules |
| `TECHNICAL_STACK.md` | Canonical stack, auth standard, deployment |
| `DEVSECOPS.md` | Security, auth, secrets, logging, dependency safety |
| `VERSIONING.md` | Version format, branches, commits, changelog, release |

### Workflow Standards

| File | Purpose |
|------|---------|
| `AGILE_SLICE_WORKFLOW.md` | Working slice model, lifecycle, sizing, backlog |
| `VERIFICATION_LOOP.md` | What counts as proof, health checks, deep health |
| `DEBUG_DIAGNOSTICS_STANDARD.md` | Copy diagnostics spec, debug mode, auth diagnostics |
| `QA_CHECKLIST.md` | Quality gates for every merge and release |

### Bootstrap

| File | Purpose |
|------|---------|
| `BUILD_APP_FOUNDATION_PROMPT.md` | Prompt to build the initial app foundation |
| `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md` | Prompt to generate a project-specific PHDK kit |

### Project Continuity

| File | Purpose |
|------|---------|
| `CHANGELOG.md` | Standards version history |

---

## Canonical Decisions

These decisions are set at the standards level and apply to all PHDK projects by default:

| Decision | Standard |
|----------|---------|
| Auth | Custom Google OAuth 2.0 — no paid auth vendor by default |
| ORM | Drizzle with PostgreSQL only — no SQLite in any environment |
| Monorepo | pnpm + Turborepo |
| Frontend | Next.js App Router |
| Backend | NestJS + Fastify |
| Deployment | Railway — two services, repo root |
| Working model | Small user-visible verified slices |
| Verification | Evidence required before every slice is marked complete |
| Cost safety | Every metered/paid external API requires a hard usage cap, timeout, retry limit, and kill switch before it ships |
| AI/LLM | Provider and model are config-driven; admin-manageable prompt, output schema, and live pricing; guardrails against prompt injection |
| Data backup | Every project must have an explicit database backup policy, asked during kit generation, recorded in `ARCHITECTURE_DECISIONS.md` — code backup is always GitHub, separately |

Overrides require an entry in `ARCHITECTURE_DECISIONS.md` in the project repo.

---

## v2.5.0 Direction

This version adds the AI Developer Operating Model.

The model teaches AI coders to:

- interview for human context before generating specs
- work autonomously inside approved slices
- avoid waterfall implementation patterns
- verify through evidence, not claims
- use health and deep-health checks as verification tools
- produce useful debug diagnostics that reduce back-and-forth
- preserve continuity through `TASK.md` and `STATUS.md`
- use custom Google OAuth 2.0 instead of paid auth vendors

---

## Changelog

See `CHANGELOG.md` for the full version history.
