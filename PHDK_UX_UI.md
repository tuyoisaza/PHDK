# PHDK UX/UI Product Design & Quality Standard

## Applicability and authority
Mandatory for projects with a user-facing interface, whether greenfield or brownfield. Does not invent new features, override user decisions, bypass security, expand browser permissions, or require external paid services. Public, anonymous, login, application and admin surfaces are included wherever present. API-only projects record an evidence-based NOT APPLICABLE. `PHDK_PRODUCTION_VERIFICATION.md` governs local/static and deployed runtime verification.

Apply `UAT_STANDARD.md` for explicit-only acceptance. Auto/Force, Design, Designer, Integration and Check do not initiate UAT Prep/UAT/Fix or browser journeys. Runtime acceptance begins only after explicit `PHDK uat`, with Fix separately authorized under that contract. Auto/Force report development delivery independently from `UAT NOT RUN` / `DEFERRED — OWNER OPT-IN`; preserve real owner/host controls and current in-scope defects without treating missing optional acceptance as a delivery blocker.

## Pre-implementation Design stage
Apply `PHDK_DESIGN.md` after technical/content Plan and before affected UI implementation. Stage `25-design` turns Plan's draft design-system constraints into visual alternatives, representative previews, a selected style guide and a durable implementation baseline. **Auto asks and waits for the owner's visual decisions, one question at a time; Auto Force selects, records AGENT_SELECTED_AUTO_FORCE and continues without a PHDK design-approval pause.** Preserve actual owner restrictions. Reuse valid owner-approved choices; do not repeat the interview or fabricate approval. Designer Mode remains the separate interface-improvement execution mode.

## Theme editing and governance
UI design specifications must include the single-source light/dark/corporate semantic color contract, authorized platform administrator's template editor, toggle and documented propagation cases defined in PHDK_THEME_STANDARD.md. Source review covers all three themes where selectable. During explicitly initiated UAT, test corporate editability for the authorized administrator even when hidden from ordinary users, as well as fallback behavior. Report implementation and static review evidence separately from runtime persistence, access and contrast evidence; nominal palette names never establish functional acceptance.

## Design operating modes
- GREENFIELD: derive users, tasks, journeys and information architecture from Capture/Plan before designing screens. Use Design to define a product visual direction, design system and previews/specifications before affected UI coding.
- BROWNFIELD: inventory existing routes and UX patterns; inspect existing source, available screenshots, tests and feedback; establish a baseline; identify friction, inconsistent patterns and visual debt; preserve correct functionality, permissions and brand where applicable. Runtime inspection remains in scoped UAT. Prioritize incremental improvements, not indiscriminate rewrites. Baseline and target must be comparable.
- Both modes: prioritize task success, clarity, consistency and accessibility over decorative novelty. A beautiful UI is not proof of a good UX.

## Three capabilities (execute as responsibilities, not autonomous agents)
1. UX ARCHITECT (Capture/Plan): audience and real jobs to be done, top user journeys, navigation, IA, information hierarchy, cognitive load, progressive disclosure, understandable language, failure recovery, mobile behavior and interaction specification.
2. UI DESIGN DIRECTOR (Design/Implementation): deliberate art direction (not generic dashboards), harmonious type/color/spacing/layout, responsive grid, visual hierarchy, component system, consistent icons, accessible focus and contrast, meaningful microinteractions. Show alternatives, record the mode-correct decision and implement the selected baseline. Choose style based on product audience, brand and use case; do not force one style on all projects.
3. UX/UI QUALITY REVIEWER (Integration/UAT/UAT Fix/Check): inspect actual source and retained evidence during Integration/Check; only in explicitly initiated UAT or authorized Fix audit user paths and screenshots/browser interaction. Compare against the selected Design baseline and old baseline, log defects with severity and repair within the authorized scope. Retest runtime behavior only inside that explicit acceptance scope. No invented observations.

## Mandatory project deliverables
During Plan, alongside UX_ARCHITECTURE.md:
- UX_RESEARCH_BASELINE.md — evidence vs assumptions, personas/roles, primary jobs, existing-interface inventory for brownfield, current pain points and measures. No fabricated interviews or usage analytics.
- UX_JOURNEYS.md — critical tasks, entry conditions, happy/empty/loading/error/success/permission states, expected outcomes, routes, labels and completion criteria.
- UI_DESIGN_SYSTEM.md — draft brand constraints, existing/planned component mappings, accessibility and theme contracts; identify decisions to resolve in Design instead of pretending the final visual direction is approved.
- UX_UI_DECISIONS.md — known owner choices, preserved behavior, open visual choices, prioritized incremental tasks and traceability to Capture requirements.

During Design, refine those same files rather than duplicating them:
- UI_DESIGN_SYSTEM.md — selected visual style guide: tokens, typography, color/contrast, spacing, breakpoints, layout, icons, component variants, focus/hover/disabled/errors, motion and responsive rules, mapped to the actual or explicitly planned shared component/token source.
- UX_UI_DECISIONS.md — references/anti-references, alternatives, tradeoffs, actual owner approval or agent selection, baseline revision, existing preview asset paths and design-to-task mapping under PHDK_DESIGN.md.
- docs/design/ — retained permitted references, concepts, representative selected previews and editable sources when available. Disclose unavailable visual tooling; specification-only decisions never become visual verification.

During explicitly initiated UAT only:
- UX_UI_AUDIT_REPORT.md — candidate/revision and selected Design baseline, tested devices and viewports, route and workflow coverage, browser/screenshot links where allowed, heuristic/a11y findings, before/after evidence for brownfield, fidelity deviations, severity/owner/fix, verified/pass/fail/blocked/manual status and unresolved risks.
- UX_UI_REMEDIATION_REPORT.md — fixes, affected components, regression/retest evidence, remaining blockers (create when issues exist).

Archive snapshots for executed/reused stages in the run's 20-plan/ and **25-design/** HANDOFFs. Create 50-uat/ and 60-uat-fix/ evidence only when their explicitly authorized stages execute; Auto records their deferred disposition without fabricating runtime reports or executed handoffs. Design is a distinct pre-implementation stage; runtime UX/UI acceptance remains part of explicit UAT. For non-visual scope record applicability in the relevant executed stages. Do not rewrite historical completed runs to invent a Design approval.

## Audit rubric (evaluate, do not assert scores without evidence)
Assess the following 12 dimensions with finding IDs and evidence. During source/design review label results as static evidence and retain unverified runtime criteria. During explicitly initiated acceptance use PASS / FAIL / BLOCKED / MANUAL / NOT APPLICABLE according to actual observations; Auto's deferred UAT is not a failed or blocked acceptance run.
1. Audience and key task match: primary actions discoverable and complete.
2. Information architecture and navigation: where am I, where can I go, how do I return?
3. Visual hierarchy and readability: titles, actionable elements, type scales and density.
4. Consistency and design system: selected Design baseline fidelity, tokens, reuse and state parity across screens.
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
- Plan cannot exit for UI-applicable projects without UX baseline, user journeys, draft design-system constraints and decisions tied to planned work. It hands off to Design, not directly to unresolved UI implementation.
- Design follows the one-question-at-a-time Auto/standalone policy and autonomous FORCE selection in PHDK_DESIGN.md. Static design artifacts are not app screenshots or browser UAT; no local server, Docker, runtime tests or new staging is authorized.
- Integration reviews actual components, route/state and viewport rules against the selected baseline, without claiming browser verification outside UAT.
- During explicitly initiated UAT or authorized UAT Fix, browser/headless and screenshots stay within the existing scoped UAT exception and PHDK_PRODUCTION_VERIFICATION.md, including run-owned synthetic data and verified cleanup. Use real available browsers, otherwise mark browser-dependent cases BLOCKED or MANUAL in that authorized run. Do not mislabel source inspection as observed use.
- Apply current in-scope findings to implementation and rerun affected permitted static checks. Rerun UAT cases only within explicitly authorized acceptance; historical UAT findings alone do not reopen that scope or completed development. Avoid changing correct features solely to match stylistic preference. Brownfield change must preserve documented functionality, security and information. Material direction changes reopen only affected Design choices under the current mode.
- Check verifies actual decision provenance, artifact/evidence quality, selected-baseline traceability, current confirmed P0/P1 defects and handoffs for stages actually executed. Deferred UAT has no required runtime report or browser evidence. A file's existence or an attractive generated image is not a runtime PASS, and unverified acceptance remains separate from development delivery.
- Existing DEBUG_DIAGNOSTICS_STANDARD.md placement, icons and behavior remain mandatory and may not be redesigned contrary to that standard.

## Recommended references
Nielsen Norman Group usability heuristics: https://www.nngroup.com/articles/ten-usability-heuristics/
W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/
Anthropic frontend-design skill: https://github.com/anthropics/skills/tree/main/skills/frontend-design
UI UX Pro Max: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

These are references, not automatically installed dependencies.
