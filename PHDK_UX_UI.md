# PHDK UX/UI Product Design & Quality Standard

## Applicability and authority
Mandatory for projects with a user-facing interface, whether greenfield or brownfield. Does not invent new features, override user decisions, bypass security, expand browser permissions, or require external paid services. Public, anonymous, login, application and admin surfaces are included wherever present. API-only projects record an evidence-based NOT APPLICABLE.

## Design operating modes
- GREENFIELD: derive users, tasks, journeys and information architecture from Capture before designing screens. Define a product visual direction, design system and prototypes/specifications before coding.
- BROWNFIELD: inventory existing routes and UX patterns; inspect existing app, screenshots, tests and feedback; establish a baseline; identify friction, inconsistent patterns and visual debt; preserve correct functionality, permissions and brand where applicable. Prioritize incremental improvements, not indiscriminate rewrites. Baseline and target must be comparable.
- Both modes: prioritize task success, clarity, consistency and accessibility over decorative novelty. A beautiful UI is not proof of a good UX.

## Three capabilities (execute as responsibilities, not autonomous agents)
1. UX ARCHITECT (Capture/Plan): audience and real jobs to be done, top user journeys, navigation, IA, information hierarchy, cognitive load, progressive disclosure, understandable language, failure recovery, mobile behavior and interaction specification.
2. UI DESIGN DIRECTOR (Plan/Implementation): deliberate art direction (not generic dashboards), harmonious type/color/spacing/layout, responsive grid, visual hierarchy, component system, consistent icons, accessible focus and contrast, meaningful microinteractions. Choose style based on product audience, brand and use case; do not force one style on all projects.
3. UX/UI QUALITY REVIEWER (Integration/UAT/UAT Fix/Check): audit actual user paths and screenshots/browser interaction where permitted, compare against plan and old baseline, log defects with severity, repair in scope and retest. No invented observations.

## Mandatory project deliverables
During Plan, alongside UX_ARCHITECTURE.md:
- UX_RESEARCH_BASELINE.md — evidence vs assumptions, personas/roles, primary jobs, existing-interface inventory for brownfield, current pain points and measures. No fabricated interviews or usage analytics.
- UX_JOURNEYS.md — critical tasks, entry conditions, happy/empty/loading/error/success/permission states, expected outcomes, routes, labels and completion criteria.
- UI_DESIGN_SYSTEM.md — brand direction, tokens, typography, color/contrast, spacing, breakpoints, layout, icons, component variants, focus/hover/disabled/errors and responsive rules. Include implementation mappings to existing components.
- UX_UI_DECISIONS.md — alternative designs considered, tradeoffs, approved/preserved behavior, screenshots/mockups or testable specs, prioritized incremental redesign tasks and traceability to Capture requirements.

During UAT:
- UX_UI_AUDIT_REPORT.md — candidate/revision, tested devices and viewports, route and workflow coverage, browser/screenshot links where allowed, heuristic/a11y findings, before/after evidence for brownfield, severity/owner/fix, verified/pass/fail/blocked/manual status and unresolved risks.
- UX_UI_REMEDIATION_REPORT.md — fixes, affected components, regression/retest evidence, remaining blockers (create when issues exist).

Archive snapshots in the run's 20-plan/ and 50-uat/ (and 60-uat-fix/ when relevant) HANDOFFs. No new independent stage is required: the quality gate is part of existing UAT. For API-only projects record applicability verdict in Plan and UAT handoffs.

## Audit rubric (evaluate, do not assert scores without evidence)
Assess 12 dimensions with PASS / FAIL / BLOCKED / MANUAL / NOT APPLICABLE, finding IDs and evidence:
1. Audience and key task match: primary actions discoverable and complete.
2. Information architecture and navigation: where am I, where can I go, how do I return?
3. Visual hierarchy and readability: titles, actionable elements, type scales and density.
4. Consistency and design system: tokens, reuse and state parity across screens.
5. Feedback and visibility of system state: saving, progress, success, delays, retry.
6. Prevent mistakes and recover: validation, confirmation for destructive actions, undo where possible.
7. Accessibility: keyboard and focus, semantic labels, contrast, zoom/reflow, target sizing; target WCAG 2.2 AA when applicable and distinguish automated from manual checks.
8. Responsive/mobile: phone/tablet/desktop, content reflow and usable touch interaction.
9. Forms and microcopy: understandable labels, defaults, concise errors and clear next step.
10. Empty/error/loading/auth states: no dead ends or misleading promises.
11. Trust and user control: transparent permissions, predictable behaviors, no dark patterns.
12. Perceived craft: distinctive, cohesive, appropriately restrained aesthetic and useful microinteractions.

Severity: P0 = critical blocked primary workflow/security/access; P1 = major usability/accessibility failure; P2 = moderate friction/inconsistency; P3 = minor polish. P0/P1 verified failures block UX acceptance; P2/P3 become prioritized tracked debt unless explicit product acceptance requires them. No subjective numeric score is an automatic pass.

## Execution and boundaries
- Preflight checks installed UX/frontend design, accessibility and UX review capabilities; source links alone are not installed tools. Use core rubric regardless of optional skill availability.
- Capture asks for essential user context only if missing after repository discovery; label assumptions.
- Plan cannot exit for UI-applicable projects without UX baseline, user journeys, design system and decisions tied to planned work.
- Integration reviews actual components, route/state and viewport consistency, without claiming browser verification outside UAT.
- During UAT/UAT Fix, browser/headless and screenshots only within the existing scoped UAT exception and allowed environments. Use real available browsers, otherwise mark browser-dependent checks BLOCKED or MANUAL. Do not mislabel source inspection as observed use.
- Apply findings to implementation and re-run affected UAT cases; avoid changing correct features solely to match stylistic preference. Brownfield change must preserve documented functionality, security and information.
- Check verifies artifact existence, evidence quality, traceability, unresolved P0/P1 and historical handoffs.
- Existing DEBUG_DIAGNOSTICS_STANDARD.md placement, icons and behavior remain mandatory and may not be redesigned contrary to that standard.

## Recommended references
Nielsen Norman Group usability heuristics: https://www.nngroup.com/articles/ten-usability-heuristics/
W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/
Anthropic frontend-design skill: https://github.com/anthropics/skills/tree/main/skills/frontend-design
UI UX Pro Max: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

These are references, not automatically installed dependencies.
