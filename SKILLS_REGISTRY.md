# SKILLS_REGISTRY.md

## Purpose

This is a curated menu of external Agent Skills, plugins, MCP servers, and reference material that complement PHDK. None of it is required — PHDK's own standards are self-contained and take priority over anything listed here.

This file is not part of the Required Reading Order. Consult it only when the current task would genuinely benefit from one of these, and confirm with the developer before installing anything — installing a skill "just in case" is not the default.

**This applies to any AI coding tool, not only Claude Code** — the same tool list PHDK itself installs into (Claude Code, Cursor, Codex CLI, Windsurf, VS Code, OpenCode, Pi, Antigravity). Most entries below are plain Agent Skills (a folder with a `SKILL.md`) that any of those tools can read the same way they read PHDK. A few are Claude-Code-specific plugin mechanisms — those are flagged explicitly so a different tool's AI developer doesn't waste time trying to install something that only exists for Claude Code.

---

## Status

Consult this file when:

- the task involves real UI/visual polish work beyond what `DESIGN_RULES.md` specifies
- the task needs real browser verification (screenshots, form flows, login flows) as evidence for `VERIFICATION_LOOP.md`
- security-sensitive code would benefit from a second pass alongside `DEVSECOPS.md`
- a manual pattern has repeated 3+ times and proven itself — time to turn it into a reusable skill
- the task needs current framework/library docs beyond training-data knowledge
- a diff needs a second review pass before merge/release, alongside `QA_CHECKLIST.md`
- connecting an external tool or repo via MCP
- improving this project's own `CLAUDE.md`/`AGENTS.md` agent-instruction file
- the AI coding tool in use is OpenCode — see the OpenCode row below, the one recommendation PHDK makes about the tool itself

---

## How installation differs by type

Six different mechanisms show up in this table. Check which one applies — a plain `git clone` only works for one of them.

- **Portable Agent Skill** (a folder with its own `SKILL.md`, no plugin manifest) — works in **any** Agent-Skill-aware tool. Clone the source repo once, then copy just that skill's self-contained subfolder into the current tool's skill directory — same layout PHDK uses for itself (`.claude/skills/<name>`, `.cursor/skills/<name>`, `.windsurf/skills/<name>`, `.opencode/skills/<name>`, `.agents/skills/<name>` for Codex CLI/Antigravity, etc.):
  ```bash
  git clone https://github.com/<owner>/<repo>.git /tmp/<repo>
  cp -r /tmp/<repo>/<path-to-skill-folder> <tool-skill-dir>/<skill-name>
  ```
- **Claude Code Plugin Marketplace** (repo has `.claude-plugin/marketplace.json`) — the convenience path (`/plugin marketplace add <owner/repo>` then `/plugin install <skill-name>@<marketplace-name>`) is **Claude Code only**. In any other tool, most of these marketplaces still contain plain `SKILL.md` folders underneath (check for a `skills/` directory) — use the Portable Agent Skill method above on that subfolder instead.
- **Claude Code plugin (hooks/commands, no SKILL.md)** — some plugins ship as hooks or slash commands instead of a skill. These have **no portable equivalent** for other tools; treat them as Claude-Code-only and read their README for what they actually do, so the same behavior can be approximated manually elsewhere if needed.
- **MCP server** — not a skill. Connect it as a tool server through the current tool's own MCP config (Claude Code, Cursor, Windsurf, and others all support MCP) — commands and config drift, verify against the server's current README before running one.
- **OpenCode plugin** — an OpenCode-native plugin installed through its own installer, not a `SKILL.md` folder. **OpenCode only** — there is no portable equivalent, and none of the copy-a-skill-folder methods above apply. Install per the plugin's own README.
- **Reference-only** — nothing to install. Read it, borrow the pattern, or use it as a discovery index. Never treat it as an authority equal to a PHDK standard or to a vetted skill in this table.

---

## Recommended External Skills & Sources

| Name | URL | Type | PHDK use |
|---|---|---|---|
| Front-end Design | https://github.com/anthropics/skills/tree/main/skills/frontend-design | Portable Agent Skill | UI polish, visual hierarchy, layout, accessibility — complements `DESIGN_RULES.md`. See the "Front-end Design — compare before choosing" section below before defaulting to this one. |
| Webapp Testing / Playwright | https://github.com/anthropics/skills/tree/main/skills/webapp-testing | Portable Agent Skill | Browser testing, UI verification, screenshots, login/form flows — real evidence for `VERIFICATION_LOOP.md` |
| Security Guidance | https://github.com/anthropics/claude-code/tree/main/plugins/security-guidance | Claude Code plugin (hooks, no SKILL.md) | Anthropic's actual dedicated security plugin — but it's hook-based and Claude Code only, not a portable skill. In another tool, use it as a reading reference for what to check (auth, secrets, permissions, unsafe data exposure) alongside `DEVSECOPS.md`, not as something to install. |
| Skill Creator | https://github.com/anthropics/skills/tree/main/skills/skill-creator | Portable Agent Skill | Use once a manual pattern has repeated and proven itself — turn it into a reusable skill |
| Superpowers | https://github.com/obra/superpowers | Claude Code Plugin Marketplace (many portable skills inside `skills/`) | Workflow discipline, planning, debugging, finishing branches — pairs with `AGILE_SLICE_WORKFLOW.md`, does not replace it. Claude Code: `/plugin marketplace add obra/superpowers`. Any other tool: copy the specific skill folder you want from its `skills/` directory (e.g. `systematic-debugging`, `writing-plans`, `verification-before-completion`). |
| Context7 | https://github.com/upstash/context7 | MCP server | Fetch current docs for frameworks/libraries/APIs instead of relying on training-data knowledge, which goes stale. Works from any MCP-capable tool. Connect per the repo's own README — its exact command has changed before, verify current syntax. |
| Addy Osmani Agent Skills | https://github.com/addyosmani/agent-skills | Claude Code Plugin Marketplace (many portable skills inside `skills/`) | Code review, quality review, production-engineering patterns. Claude Code: `/plugin marketplace add addyosmani/agent-skills`. Any other tool: copy the specific skill folder from `skills/` (23 available — see repo). |
| Code Review Skill | https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md | Portable Agent Skill (part of the entry above) | Review a diff before merge/release — a second pass alongside `QA_CHECKLIST.md` |
| Oh My OpenCode Slim | https://github.com/alvinunreal/oh-my-opencode-slim | OpenCode plugin (OpenCode only) | **When the tool in use is OpenCode, PHDK recommends running this on top of it.** A slimmed, token-efficient multi-agent suite (Orchestrator, Explorer, Oracle, Council, Librarian, Designer, Fixer) that gives OpenCode the delegated-subagent workflow PHDK's slice model assumes. MIT, ~8.6k★. Install: `npx oh-my-opencode-slim@latest install` (or `bunx`). On OpenCode v2, pin an exact version rather than `@latest` — the plugin is moving fast. Not applicable to any other tool. |
| MCP Servers | https://github.com/modelcontextprotocol/servers | Reference / MCP catalog | Index of official MCP servers — GitHub, filesystem, and other tool connectors. Browse it and add only the specific server the task needs, per that server's own instructions. |
| TypeScript MCP SDK | https://github.com/modelcontextprotocol/typescript-sdk | Reference (SDK, not a skill) | Only relevant when actually building or integrating a custom TypeScript MCP server/client — install per the SDK's own docs. |
| Claude Code Best Practice | https://github.com/shanraisshan/claude-code-best-practice | Reference-only | Ideas for `CLAUDE.md`/agent-instruction management. Compare against PHDK's own `AGENTS.md`/`INANUTSHELL.md` before adopting anything — read only, nothing to install. |
| VoltAgent Awesome Agent Skills | https://github.com/VoltAgent/awesome-agent-skills | Discovery index | A large curated list for finding additional skills. Explicitly not a default authority — anything pulled from it still needs the same scrutiny (verify the URL, identify the type, confirm before installing) as every row in this table. |
| Andrej Karpathy-style CLAUDE.md | https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md | Reference-only | Simplicity, surgical changes, goal-driven execution — a second `CLAUDE.md` style to compare against PHDK's own agent files, not a replacement for them. Read only. |

---

## Front-end Design — compare before choosing

"A design skill" isn't one thing — researched five candidates so the developer can pick deliberately instead of defaulting to the first result. None of these are installed automatically; present this table and let the developer choose.

| Skill | URL | Maintainer / trust signal | Best for | Portable? |
|---|---|---|---|---|
| **Anthropic Frontend Design** | https://github.com/anthropics/skills/tree/main/skills/frontend-design | Anthropic, official (171k★ repo) | Distinctive, production-grade visual aesthetics — deliberately breaks the generic "AI-app look" (typography, color, layout choices) | Yes |
| **Vercel Web Design Guidelines** | https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines | Vercel Labs, official (30k★ repo, listed on skills.sh) | Automated quality gates — 100+ accessibility/UX checks against established standards | Yes |
| **AccessLint** | https://github.com/accesslint/claude-marketplace | AccessLint, a dedicated accessibility-tool vendor (88★) | WCAG 2.1 auditing specifically — contrast checking, refactoring, an MCP server for color analysis | Claude Code plugin marketplace; check inside `plugins/` for a portable `SKILL.md` before assuming it works elsewhere |
| **Bencium UX Designer** | https://github.com/bencium/bencium-claude-code-design-skill | Independent design studio (400★) | UX fundamentals — "simplicity through reduction," motion specs, accessibility reference docs | Unverified — inspect the repo's actual structure before trusting it |
| **UI/UX Pro Max** | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | NextLevelBuilder (⚠️ 120k★ — unusually high for the repo's visibility/profile; verify the star count and read the actual `SKILL.md` content before trusting it) | Claims a searchable design database: 50+ styles, 97 color palettes, persistent design system with overrides | Unverified |

**Working recommendation, not a mandate:** default to **Anthropic Frontend Design** — official, most-scrutinized, purely aesthetic direction, so it doesn't fight with `DESIGN_RULES.md`'s structural rules (brand requirements, app shell layout, token ownership). If a project needs accessibility rigor specifically, pair it with **Vercel Web Design Guidelines** rather than replacing it. Hold off on UI/UX Pro Max until someone has actually read its `SKILL.md` content — a star count that disproportionate to a repo's visibility is a reason to look closer, not a reason to trust it more.

---

## Rules

- The OpenCode recommendation is about the *tool*, not the project: it changes how the AI developer is run, never what PHDK requires. `AGILE_SLICE_WORKFLOW.md`, `VERSIONING.md`, and `DEVSECOPS.md` apply identically with or without it — an orchestrator delegating to subagents does not relax branch, commit, version, or verification rules for any agent in the chain.
- None of these override a PHDK standard. If a skill's guidance conflicts with `DEVELOPMENT_RULES.md`, `DEVSECOPS.md`, or any other PHDK file, PHDK wins — same precedence rule as `INANUTSHELL.md` has against the full standards.
- Installing something from this table is a judgment call for the current task, not a default step in bootstrap. Ask before installing.
- Before recommending a skill, identify which of the six install types above it is, and whether it's portable to the current tool or Claude-Code-only. Don't hand a developer on Cursor or Windsurf a `/plugin marketplace add` command that only works in Claude Code.
- Before adding a new row to this table: verify the URL actually resolves, and treat an unusually high star count relative to a repo's visibility as a reason for closer scrutiny, not automatic trust.
- A discovery index (VoltAgent, or anything similarly generic) is never cited as an authority on its own — only entries actually vetted and listed by name above are "PHDK-recommended."
