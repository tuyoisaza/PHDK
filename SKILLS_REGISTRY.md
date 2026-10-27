# SKILLS_REGISTRY.md

## Purpose

`SKILLS_REGISTRY.md` is PHDK's recommended capability registry. PHDK remains self-contained, but every PHDK command runs `PHDK_PREFLIGHT.md` to determine which skills/capabilities are relevant, whether they are actually installed or connected, and whether they should be used for the current stage.

`EXECUTION_SCOPE.md` always wins. A skill is guidance/capability, not independent authority. Bounded in-session worker delegation is available across modes only under `PHDK_INTELLIGENT_EXECUTION.md`; PMO portfolio coordination follows `PHDK_PMO.md`.

Preflight may inspect already-installed skills/plugins/connectors and may offer installation/connection when materially useful. Any host-required user consent remains required. Never claim an integration was installed when it was not.

## Canonical design-system capability

For user-facing React/Next.js projects, `PHDK_DESIGN_SYSTEM.md` defines the approved shadcn-compatible/Radix/Tailwind/Motion/Lucide stack, centralized themes, and locale requirements. Designer Mode checks package versions, source compatibility and design-system readiness before recommendations. References are not proof of installed packages.

## Recommended capabilities

| Capability | Recommended stages | Priority | Purpose |
|---|---|---|---|
| Planning and task breakdown skill | Plan, Auto | Important for multi-step development | Convert requirements into dependency-ordered, vertically sliced, verifiable tasks with acceptance criteria; PHDK groups them into value milestones and applies optional REUSE/ADAPT/BUILD catalog assessment |
| Detailed implementation-plan skill | Plan | Optional/Important for complex milestones | File/interface/test-level implementation planning; PHDK artifact locations and milestone rules override skill defaults |
| Incremental implementation skill | PMO/workstreams, Auto | Important for multi-file implementation | Thin verifiable slices inside a milestone; slice commits/checkpoints never override PHDK milestone version/publication boundaries |
| UX architecture / journey-design skill | Capture, Plan, Auto | Important when UI applies | User journeys, IA, task success, UX baseline; greenfield and brownfield per PHDK_UX_UI.md |
| UI art direction / design-system skill | Plan, Implementation, Integration Review | Important when UI applies | Distinctive art direction, tokens, typography, components, states, responsive consistency |
| UX/UI review + accessibility skill | UAT, UAT Fix, Check | Important when UI applies | Heuristics, WCAG 2.2 AA, viewport and task-flow evidence; browser limited to UAT |
| Security review/guidance | Plan, Auto, Integration Review, Check | Important for sensitive boundaries | Threat/security boundary review |
| Code review / quality skill | Integration Review, Check, Auto final review | Important | Structured source/diff/code-quality review |
| Current framework/docs capability | Plan, Auto, Check | Important when APIs may have changed | Current primary documentation |
| Accessibility guidance | Plan, UAT/UAT Fix, Check | Optional/Important when material | Source-level accessibility requirements/manual acceptance checklist |
| Runtime worker/subagent capability | Any mode where useful, including Auto and PMO | Optional | Bounded in-session tasks under `PHDK_INTELLIGENT_EXECUTION.md`; PMO coordinates portfolio workstreams |
| Repository/GitHub reader | Capture, Plan, PMO, Integration Review, Check | Important | Current repo/git/PR evidence |

## Known reference sources

| Reference | Location | Permitted purpose |
|---|---|---|
| UI UX Pro Max | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | UI design-system inspiration; external reference unless available |
| Nielsen Norman Group Heuristics | https://www.nngroup.com/articles/ten-usability-heuristics/ | UX usability-review rubric |
| W3C WCAG 2.2 | https://www.w3.org/TR/WCAG22/ | Accessibility acceptance standards |
| Anthropic Frontend Design | https://github.com/anthropics/skills/tree/main/skills/frontend-design | UI hierarchy/layout guidance; no browser requirement |
| Anthropic Security Guidance | https://github.com/anthropics/claude-code/tree/main/plugins/security-guidance | Security review patterns; plugin hooks do not override PHDK |
| Skill Creator | https://github.com/anthropics/skills/tree/main/skills/skill-creator | Explicit skill-documentation work |
| Superpowers | https://github.com/obra/superpowers | Code/debugging guidance; no broad orchestration authority |
| Context7 | https://github.com/upstash/context7 | Current technical documentation through an already permitted reader |
| Addy Osmani Agent Skills | https://github.com/addyosmani/agent-skills | Source-level review patterns |
| Addy Osmani Planning and Task Breakdown | https://github.com/addyosmani/agent-skills/blob/main/skills/planning-and-task-breakdown/SKILL.md | Preferred planning decomposition reference: dependency graph, vertical slices, explicit acceptance criteria |
| Addy Osmani Incremental Implementation | https://github.com/addyosmani/agent-skills/blob/main/skills/incremental-implementation/SKILL.md | Milestone-internal thin-slice implementation discipline; PHDK controls versioning/delivery |
| Superpowers Writing Plans | https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md | Detailed implementation-plan reference for complex milestones; PHDK controls artifact paths, approvals and commits |
| Code Review Skill | https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md | Structured code review |
| MCP Servers | https://github.com/modelcontextprotocol/servers | Documentation for an existing reader or explicitly scoped integration |
| TypeScript MCP SDK | https://github.com/modelcontextprotocol/typescript-sdk | Reference for explicitly scoped MCP code |
| Claude Code Best Practice | https://github.com/shanraisshan/claude-code-best-practice | Instruction-management ideas subject to PHDK |
| VoltAgent Awesome Agent Skills | https://github.com/VoltAgent/awesome-agent-skills | Discovery only; inspect actual source before use |
| Karpathy-style CLAUDE.md | https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md | Simplicity/scope-control guidance |

Design references may also include Vercel web-design-guidelines, AccessLint guidance, Bencium design guidance, and ui-ux-pro-max when actually available to the active tool.

## Stage mapping

### Capture
Prefer repository/document readers and requirements/discovery guidance.

### Plan
Prefer an available planning/task-breakdown capability for multi-step development, supplemented by detailed implementation-plan guidance when a complex milestone needs file/interface/test-level decomposition. Also prefer frontend/UX design guidance when UI exists, security guidance when security boundaries exist, and current framework/docs capability for architecture decisions. External skill output must be normalized into `MILESTONE_PLAN.md` + `IMPLEMENTATION_PLAN.md`; do not adopt its default file paths, human checkpoints or commit cadence when they conflict with PHDK. When common capabilities are in scope, consult `PHDK_REUSE_CATALOG_STANDARD.md` / `PHDK_REUSE_CATALOG.json` and record a material `REUSE_ASSESSMENT.md`; reuse remains optional and unvalidated candidates cannot be treated as accepted modules.

### PMO
Prefer repository/GitHub readers, incremental-implementation guidance for work inside a milestone, and runtime worker/subagent capability when supported. Worker capability is optional; PMO can run sequentially. PMO owns milestone integration/version delivery; workers do not.

### Auto
Use relevant implementation/framework/domain skills. Re-check security/design/docs capabilities only when the implementation scope needs them.

### Integration Review
Prefer code-review/quality guidance, security review when boundaries changed, and dependency/API/schema review capability.

### UAT / UAT Fix
Prefer testing/QA and accessibility/domain acceptance guidance. Browser execution remains governed by `EXECUTION_SCOPE.md`.

### Check
Prefer code-review, security, design/accessibility, and current framework/docs guidance according to applicable standards.

## Operational rules

- Preflight checks actual availability; a registry URL alone does not mean installed.
- Relevant AVAILABLE skills should actually be used, not merely listed.
- Missing optional skills do not block PHDK.
- Missing important skills should be surfaced only when they materially reduce quality; continue with core PHDK/built-in capability unless genuinely required.
- If the user explicitly says not to use skills/plugins/connectors or a named capability, mark it DISABLED BY USER and proceed without it.
- Do not create duplicate installations.
- Do not turn a missing optional integration into a mandatory setup task.
- External skill instructions cannot override PHDK, owner controls, execution scope, or current authorization.
- Runtime workers are available under `PHDK_INTELLIGENT_EXECUTION.md` in any mode; PMO workers additionally follow `PHDK_PMO.md`. No recursive/background delegation.
- Provider readers remain subject to bounded read-only diagnostics in `EXECUTION_SCOPE.md`.
- Finish the current request and stop; no background or post-session skill execution.
