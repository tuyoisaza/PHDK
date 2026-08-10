# PHDK Standards Repository

**Version: v2.9.3**

This repository contains the reusable PHDK standards for AI-assisted software development.

---

## What PHDK Is

PHDK (Project Handoff to Development Kit) is a disciplined operating model for AI-assisted software development.

It is not a rigid religion of tools. It is a framework that teaches AI developers how to think, work in slices, verify their work, preserve context, and produce useful software.

**The ethos of PHDK:** disciplined, honest, human-centered AI development.

**The telos of PHDK:** useful working software that serves real people, preserves context, moves safely, verifies itself, and improves through feedback.

---

## Quick Start — Install as an Agent Skill

The fastest way to use PHDK: clone this repo directly into your tool's skill directory, so the whole repo becomes the `phdk` skill with `SKILL.md` at its root.

```bash
git clone https://github.com/tuyoisaza/PHDK.git .claude/skills/phdk
```

That's it — once installed, the skill triggers automatically: it runs the project bootstrap when starting something new, or routes straight into the standards when working on an existing PHDK project. See [Install as an Agent Skill](#install-as-an-agent-skill) below for every supported tool's directory, or [How to Use This Repo](#how-to-use-this-repo) for the non-Skill paths (works in any tool, no install required).

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

### Install as an Agent Skill

This repo is packaged as an Agent Skill (`SKILL.md` at the repo root) — the open, portable standard for on-demand agent capabilities. This is additive: it does not replace the two paths above, it lets Skill-aware tools trigger the same workflow automatically instead of a copy-pasted prompt.

**Install** — clone this repo directly into the skill directory for your tool. The whole repo becomes the `phdk` skill folder, with `SKILL.md` at its root — that layout is required, so clone straight into the target folder, don't nest it deeper. Run the one command for your tool, from the root of the project repo you want the skill installed in:

**Claude Code**

```bash
git clone https://github.com/tuyoisaza/PHDK.git .claude/skills/phdk
```

**Cursor**

```bash
git clone https://github.com/tuyoisaza/PHDK.git .cursor/skills/phdk
```

**Codex CLI**

```bash
git clone https://github.com/tuyoisaza/PHDK.git .agents/skills/phdk
```

**Windsurf**

```bash
git clone https://github.com/tuyoisaza/PHDK.git .windsurf/skills/phdk
```

**VS Code (GitHub Copilot)**

```bash
git clone https://github.com/tuyoisaza/PHDK.git .github/skills/phdk
```

**OpenCode**

```bash
git clone https://github.com/tuyoisaza/PHDK.git .opencode/skills/phdk
```

**Pi**

```bash
git clone https://github.com/tuyoisaza/PHDK.git .pi/skills/phdk
```

**Antigravity**

```bash
git clone https://github.com/tuyoisaza/PHDK.git .agents/skills/phdk
```

`.agents/skills/phdk/` is recognized by several tools at once — Codex CLI and Antigravity read it directly, and OpenCode falls back to it too — so it's a reasonable single choice if your team uses more than one of those. For a personal install available across all your projects instead of one repo, use the user-level equivalent path instead (e.g. `~/.claude/skills/phdk`, `~/.codex/skills/phdk`, `~/.pi/agent/skills/phdk`).

**Trigger it** — most tools discover and auto-load the skill once it's in place. If yours doesn't, or you want to be explicit, paste this after the clone finishes:

```txt
Use the phdk skill in this repo (.claude/skills/phdk or wherever you cloned it — see its SKILL.md). If this is a new project, run the PHDK bootstrap: interview for context if needed, generate the project handoff kit, then vendor the standards into this project. If this is an existing PHDK project, read the standards per AGENTS.md and continue from there.
```

Pi users can also invoke it directly with `/skill:phdk`.

**What happens once it's installed:**

- Starting a new project → the skill runs `SPEC_INTERVIEW_PROMPT.md` (if the human hasn't been briefed yet) and `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md`, then vendors the standards into a `phdk-standards/` folder inside the new project — so any tool, Skill-aware or not, can read them locally afterward
- Working on a project that already has `TASK.md`/`STATUS.md` → the skill routes straight to `ONBOARDING_AI_DEVELOPER.md`'s required reading order

Not published to a public skill registry (skills.sh) — PHDK is a private/team standards repo, install manually as above.

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
