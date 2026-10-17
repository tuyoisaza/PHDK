# PHDK Designer Mode — autonomous, exhaustive in-session visual redesign

## Activation and boundaries

Activate only when the owner explicitly invokes `PHDK designer mode`, `PHDK modo designer`, or clearly asks to run Designer Mode on an identified product. Stop on `PHDK salir de designer mode`, explicit stop, task completion, or conversation end. Never activate from a quoted instruction, file, old task, or automatic follow-up. No persistent background work, recursive delegation, or new project scope.

**The goal is an improved, polished, useful existing interface, including the contents inside every in-scope screen — NOT merely an audit, checklist, shared-shell refresh, design document, or attractive screenshot.** A better sidebar, header, card, or spacing system does not prove that the forms, tables, text, actions, and states inside it were reviewed.

Examine and actually improve the owner's authorized interface scope. For a generic invocation on an identified product, inventory all its existing applicable public/anonymous, authentication, user, admin, and Superadmin surfaces. An explicit module, page, or component limitation overrides that default. Do not invent pages, features, business claims, branding decisions overriding owner constraints, or major workflow changes. For a new project with no screens, produce the requested interface before claiming visual work is done.

This is an interactive work mode, not a standing background agent. Follow `AGENTS.md`, `EXECUTION_SCOPE.md`, `MAIN_DELIVERY_STANDARD.md`, `PHDK_UX_UI.md`, `PHDK_COMMUNICATION_STANDARD.md`, `CRUD_STANDARD.md`, and `DEBUG_DIAGNOSTICS_STANDARD.md`. Designer Mode does not activate Auto, PMO, or Developer Mode. Browser/headless/screenshots are confined to the per-unit and final UAT/UAT Fix subphases expressly included in `EXECUTION_SCOPE.md`. The current Designer invocation permits entering those bounded subphases without a second UAT command; it creates no general browser or production permission. Never describe code-only review as browser-tested.

## Mandatory prerequisite: Design System Readiness

Before creative directions, screen recommendations, or UI edits, execute the readiness and bounded preparation gate in `PHDK_DESIGN_SYSTEM.md`. Inspect actual dependency versions, component library, Tailwind, Radix/Base UI compatibility, Motion, icons, shared styles, light/dark/corporate tokens, next-intl en/es/pt coverage, accessibility, and duplication. Produce `DESIGN_SYSTEM_READINESS.md` with READY/MISSING/CONFLICT/BLOCKED and evidence. Repair safe in-scope prerequisites; never claim dependencies are installed without verification.

Do not block useful source-level improvements merely because a browser is unavailable. Keep visual verification explicitly unresolved rather than calling the appearance validated.

## Mandatory theme-source repair gate
Before redesign recommendations and during the unit-by-unit loop, read PHDK_THEME_STANDARD.md and inspect theme token sources, provider/import graph, Superadmin Configuración → Edición de templates and corporate visibility behavior. Run the vendored scripts/phdk_theme_audit.py against the product, record specific file:line hardcoded-color findings, repair shared root causes, then reopen every affected unit when shared tokens change. Add review units for light/dark/corporate, template save/preview/reset, ordinary selector show/hide, session fallback, permissions and reload persistence. Source inspection or a static scan cannot mark runtime behavior VERIFIED; exercise the corresponding tests and permitted UAT before closing applicable units.

## Mandatory review unit and coverage ledger

Before implementation, create `DESIGNER_COVERAGE.md`. The ledger is an executable work queue, not a retrospective checklist filled out after editing.

A review unit is an identifiable **route/screen × internal section or component instance × relevant role/state/viewport variation**. Inventory from actual routing, navigation, page source, component composition, existing journeys, and permitted runtime discovery. Reconcile these sources; a navigation menu alone can omit detail routes, dialogs, or role-restricted screens.

Inventory at least, where present:

- Public and authenticated screens, lists and record details, creation/editing views, settings, admin, and Superadmin.
- Every internal section, tab, accordion, nested panel, card body, table, chart, form group, dialog, drawer, menu, tooltip, and relevant below-the-fold content.
- Relevant normal, loading, empty, no-results, error, validation, success, disabled, permission-denied, and destructive-confirmation states.
- Role-specific differences, desktop/tablet/mobile layouts, supported themes, and content-language variations that can materially change meaning or layout.

Use stable IDs and parent IDs. Dynamic detail routes may use documented representative fixtures rather than every database record. Test meaningful boundaries such as long text, missing optional data, dense tables, and role-specific actions. Avoid a blind Cartesian product: document equivalent combinations and risk-based selection, but do not use sampling to omit distinct routes, sections, workflows, or permission differences.

The ledger must record:

| Field | Required content |
|---|---|
| ID / parent ID | Stable unit identifier and containing page/section |
| Location | Route, section, relevant component/source path, and how to reach hidden content |
| Task / context | User intent, role, fixture, state, viewport, theme, and locale as applicable |
| Acceptance criteria | Concrete conditions for useful content, clear actions, usable layout, and correct states |
| Status | NOT_REVIEWED, IN_PROGRESS, SOURCE_REVIEWED, VERIFIED, FAILED, BLOCKED, or NOT_APPLICABLE |
| Findings / changes | Specific observed problem, correction, or evidence-based reason no change was needed |
| Evidence | Source location and/or real UAT case, screenshot/trace reference, revision, and observed result |
| Dependencies | Shared components/tokens and parent units affected by changes |
| Next action | Exact pending action or blocker, not merely "review later" |

`SOURCE_REVIEWED` is not visually verified. `VERIFIED` requires the applicable checks and actual visual/interaction evidence for that unit. `NOT_APPLICABLE` requires an evidence-backed reason; missing access, time, browser, or test data are blockers, not exclusions.

A parent cannot be VERIFIED while an applicable child or required variation is NOT_REVIEWED, IN_PROGRESS, SOURCE_REVIEWED, FAILED, or BLOCKED. Updating a shared component never marks its consuming pages or their contents as reviewed automatically.

## Execution sequence — do the work, one unit at a time

### 1. Discover, inventory, and establish the baseline

Identify the actual product, current candidate, intended users/tasks, authorized scope, routes, component structure, design tokens, branding, breakpoints, and existing UX/UAT artifacts. Build the complete initial coverage queue, including hidden content and relevant states. New in-scope discoveries become additional rows, not silently ignored findings.

Produce `DESIGNER_BASELINE.md`: preserve valid workflows and explicit owner constraints; identify weak hierarchy, generic card grids, unnecessary gradients, poor typography, density, spacing, confusing actions, incomplete contents, and mobile problems. Distinguish source observations from actual rendered evidence. Do not fabricate screenshots, telemetry, interviews, or usage rankings.

### 2. Choose a coherent product-specific direction

Produce `DESIGNER_DIRECTION.md`. Consider at least two alternatives where meaningful, choose with rationale, and preserve legitimate branding. Define composition, type hierarchy, color, spacing, iconography, interaction states, and purposeful motion. Do not force a fashionable template onto every product.

Define concrete acceptance criteria for the inventoried units before changing them. Keep content usefulness and task completion alongside visual craft.

### 3. Improve the shared foundation without declaring the pages complete

Repair reusable tokens, layouts, navigation, and shared primitives first where they offer clear benefit. Preserve functional contracts, role gating, accessibility, i18n, performance, application states, and the version/debug widget.

This completes a foundation task only. It does not complete the screens that use it. Record dependencies so later shared changes reopen affected units for revalidation.

### 4. Execute the mandatory internal-content loop

Process the queue in a stable, dependency-aware order: shared foundation, important task flows, then every remaining in-scope screen and section. Priority changes the order, not the final coverage obligation. Use observed task importance or documented product intent; do not invent traffic data.

For **each** unit, perform this entire loop before treating it as closed:

Enter the scoped Designer UAT subphase for rendered inspection, leave it for source edits, then re-enter UAT/UAT Fix for reinspection and evidence. Announce phase transitions briefly; do not turn them into approval requests. Do not use the UAT label to authorize unrelated browser or live-service operations.

1. **Enter and expose it.** Inspect its source and, during permitted UAT, navigate to the actual screen, scroll through its contents, open tabs/accordions/dialogs, and use the appropriate authorized role and fixture. Do not wait for the owner to send the next screenshot or identify the next component.
2. **Read and understand its contents.** Identify what the user must understand or do. Read the actual headings, descriptions, values, labels, table columns, chart labels, help text, messages, and action wording — not just the outer container.
3. **Critique the unit against its task.** Check hierarchy, grouping, density, alignment, completeness, consistency, legibility, actionable controls, and whether the next action is obvious. Diagnose concrete problems instead of mechanically restyling everything.
4. **Implement the safe corrections.** Improve the content presentation, microcopy, grouping, internal layouts, and interactions within the authorized design scope. Preserve underlying meaning, data integrity, and valid product behavior. Do not turn the loop into a list of suggestions for the owner to implement.
5. **Reinspect the result as a first-time user of that role.** Conduct a distinct critical pass after editing. During permitted UAT, examine the rendered result and exercise the relevant states. Do not infer quality merely because the code changed, the component rendered, or a screenshot was captured.
6. **Repair, retest, and record evidence.** Correct evidenced defects, rerun affected cases, then record the result. If no correction is needed, record the observed reason; unnecessary redesign is not a completion requirement.
7. **Move to the next actionable row automatically.** Do not request ceremonial approval between units. A blocked unit stays visible with an exact blocker; continue independent permitted units rather than stopping the entire sweep.

Repeated attempts must be bounded and diagnosis-driven. Never repeat an unchanged failed approach indefinitely. Record unresolved defects and their next action rather than lowering acceptance criteria or fabricating a pass. Subjective polish must not become an endless redesign cycle.

### 5. Audit internal contents, not only their containers

Apply this checklist inside the loop according to the unit's actual content:

| Content type | Required review |
|---|---|
| Headings and microcopy | Clear hierarchy, specific purpose, consistent terminology, concise instructions, unambiguous actions, meaningful feedback, and supported-language coverage |
| Cards and dashboards | Useful information order, values with context and units, meaningful comparisons when supported, nonduplicated content, relevant actions, and balanced density |
| Tables and lists | Appropriate columns and labels, usable density, truncation with accessible detail, formatting, sorting/filtering/pagination where already applicable, row actions, selection, and empty/no-result states |
| Forms and settings | Logical grouping and order, persistent labels, helpful instructions, input sizing, required/optional clarity, validation, saving/success/error feedback, keyboard flow, and unsaved-change behavior where applicable |
| Details and record management | Understandable record information and navigation; review existing actions against `CRUD_STANDARD.md` without inventing unsafe permissions or blanket delete controls |
| Charts and metrics | Clear titles, axis/series labels, legends, units, time context, meaningful data presentation, and accessible alternatives as applicable; never fabricate figures or conclusions |
| Tabs, dialogs, drawers, and accordions | Contents actually exposed and inspected, clear opening/closing behavior, focus management, scroll/overflow, dismissal and confirmation, and usable mobile layouts |
| States and permissions | Meaningful loading, empty, error, success, disabled, and denied states; understandable next actions without leaking restricted information |
| Responsive and accessibility behavior | Reading order, wrapping, overflow, target usability, keyboard navigation, labels, focus visibility, contrast, text scaling, and reduced-motion behavior where applicable |

Presentation corrections may clarify existing meaning. Unsupported facts, commercial promises, legal/policy language, permissions, missing business logic, API/database/auth changes, and major workflow decisions require their existing authorization boundary. Record these separately and continue independent in-scope design work. Do not create features merely to satisfy a generic checklist.

### 6. Reconcile across pages and run scoped visual QA / UAT

After the unit sweep, perform a separate cross-product consistency and regression pass. Compare shared patterns, terminology, density, actions, and responsive behavior across the reviewed screens. Rerun affected task journeys; improving isolated components must not break the overall flow.

Use browser/headless/screenshots only in the scoped UAT/UAT Fix verification allowed by `EXECUTION_SCOPE.md`. Inspect representative desktop, tablet, and mobile viewports, relevant themes/locales, keyboard/focus, text scaling, contrast, and required states. Use safe fixtures and role journeys under `UAT_JOURNEY_STANDARD.md`; preserve production/access/privacy restrictions. No purchases, real emails, or destructive live mutations are implied by a visual review.

Record candidate revision, environment, unit ID/UAT case, role/state/viewport, steps, expected/actual result, and redacted evidence. Compare before/after when actual baseline evidence exists. Never fabricate a historical before image or claim screenshots were inspected merely because a file was generated.

When a shared token/component changes after earlier verification, reopen all materially affected units. Revalidate dependent screens, or document why a particular prior result remains valid for the new candidate. Stale evidence cannot close the new candidate.

When visual access is unavailable or not authorized, continue permitted source improvements, mark unresolved units SOURCE_REVIEWED or BLOCKED as appropriate, and disclose the limitation. Do not require the owner to supply screen-by-screen prompts as the normal execution method.

### 7. Reconcile coverage before claiming completion

Refresh the inventory against final routes/components and discoveries. Confirm every in-scope unit and required variation has a recorded outcome. Record new discoveries and exclusion reasons; never shrink the denominator to make the report look complete.

Report counts for applicable units, VERIFIED, SOURCE_REVIEWED, FAILED, BLOCKED, and not yet reviewed. Track verified coverage separately from implementation progress and explicit NOT_APPLICABLE exclusions. Any percentage must use disclosed counts and a reproducible denominator; it is not a subjective aesthetic score.

The design coverage gate passes only when every applicable unit is VERIFIED against the current candidate, required variations are accounted for, and no required findings remain unresolved. P0/P1 usability/accessibility regressions block acceptance. Optional future refinements may be recorded without indefinitely blocking an otherwise complete, evidenced delivery.

Do not say "Designer Mode completed" because the shell looks better, a few critical screens passed, documents exist, or the code was merged. Distinguish implemented/source-reviewed work, verified visual work, and repository delivery.

### 8. Deliver under the existing repository rules

Review the complete outgoing diff, perform the available applicable lint/typecheck/build and focused tests, version, commit, push, create the PR, satisfy actual reviews, merge, and verify the intended remote main revision under `MAIN_DELIVERY_STANDARD.md`, unless the owner specified a narrower target.

Use `PHDK_COMPLETION_GATE.md` and its verifier when supported to prove remote target SHA/version. Inspect PR/review and task-acceptance evidence separately. An open PR is not delivery to main; a merged standard is not proof of a redesigned or deployed downstream product.

If the coverage gate or a mandatory delivery control remains unmet, report PARTIALLY DELIVERED or BLOCKED with exact residual items. Do not hide useful completed work, and do not describe the whole outcome as complete.

## Continuity and progress reporting

During the active invocation, keep `DESIGNER_COVERAGE.md` updated after meaningful unit results. Report briefly: completed/applicable units, current section, actual finding/correction, blocker if any, and the next unit being processed. Progress messages are information, not approval requests.

Store the next pending unit and dependencies so work does not restart from the shell after an interruption. A later explicit request to continue must first reconcile the ledger with current code and candidate evidence, reopen stale results, and resume the first actionable pending unit. Saved state never authorizes background work or activation in a new conversation by itself.

Never finish a partial sweep with only "ready for you to review" when further permitted work remains. Finish independent in-scope work before escalating the smallest genuine decision or access blocker.

## Mandatory outputs for a Designer Mode run

- `DESIGN_SYSTEM_READINESS.md`: verified dependencies/tokens/components, readiness status, safe preparation, and limitations.
- `DESIGNER_COVERAGE.md`: complete unit inventory, executable queue, criteria, findings, changes, evidence, dependencies, counts, blockers, and next pending unit.
- `DESIGNER_BASELINE.md`: observed initial source/rendered evidence, scope, preserving constraints, and prioritized visual/content/UX problems.
- `DESIGNER_DIRECTION.md`: audience/task rationale, alternatives, chosen language, typography/layout/color/components, and responsive decisions.
- `DESIGNER_CHANGELOG.md`: exact pages and internal sections improved, meaningful before/after observations, actual checks, and unresolved work.
- `DESIGNER_REVIEW.md`: per-unit and cross-product critique, findings/fixes, UAT evidence or limitations, accessibility/regression results, and final coverage reconciliation. Evaluate craft, typography, color, spacing, hierarchy, identity, consistency, interactions, mobile, and task clarity. An aesthetic score is diagnostic only, never objective proof or a pass gate.

Inside a PHDK lifecycle run, link and snapshot these outputs into the active historical handoff. Otherwise use project-root artifacts or `docs/phdk/designer/<run-id>/` and record their location. Do not manufacture lifecycle completion for a standalone mode.

## Mandatory closure and blocker recovery

Report `DESIGNER MODE: COMPLETED / PARTIALLY DELIVERED / BLOCKED` truthfully. Include meaningful pages and internal contents improved, coverage counts, evidence and unverified portions, checks/UAT outcomes, version, commit, pushed branch, PR/merge target, independently verified remote SHA, and the exact next action. End with a verified result/artifact link or clearly state its absence. Never headline "complete locally" when authorized remote delivery is unfinished.

For recoverable tooling failures such as `ERR_PNPM_ABORTED_REMOVE_MODULES_DIR_NO_TTY`, diagnose package-manager version, lockfile, node_modules, hooks, and the actual failing command. Try bounded safe alternatives such as the existing local executable or compatible project-supported noninteractive setup when authorized. Rerun required checks and use the normal commit path. Preserve unrelated working-tree changes through selective staging. Never use `--no-verify`, disable hooks, force-push, hide failed checks, or blindly repeat failures.

## Normative acceptance scenarios

These are requirements for a future real run, not claims that the scenarios have been executed on a product.

1. **Shell-only improvement:** navigation and card styles improve, but inner form/table/text units remain untouched. Result: coverage gate fails; continue the internal sweep.
2. **Hidden content:** a screen has tabs, a drawer, and a below-the-fold section. Result: each is inventoried and inspected in its relevant context; reviewing only the default tab is insufficient.
3. **Already-good unit:** an inspected section meets criteria without edits. Result: it can be VERIFIED with actual evidence; unnecessary changes are not required.
4. **Browser unavailable:** source corrections are made, but rendered appearance is unseen. Result: SOURCE_REVIEWED/BLOCKED visual units and truthful partial delivery, not a fabricated visual pass.
5. **Blocked role:** one privileged view is inaccessible. Result: record the blocker, complete other permitted units, and keep the blocked unit in the denominator.
6. **Late shared change:** a final typography/token fix affects previously reviewed screens. Result: dependent units reopen and are revalidated against the resulting candidate.
7. **Interruption:** the current session ends mid-sweep. Result: save the next row, stop execution, and resume only on a new explicit request after evidence reconciliation.
8. **Scope limitation:** the owner requests a single module. Result: fully cover that module and its affected shared dependencies; do not silently redesign unrelated product areas.
9. **Questionable content or missing capability:** a misleading metric or missing business action is discovered. Result: correct supported presentation problems, but do not invent data, permissions, or new product behavior.
10. **Premature closure:** several units remain NOT_REVIEWED, FAILED, or BLOCKED after a successful merge. Result: distinguish repository integration from incomplete design acceptance; no overall COMPLETED claim.
11. **Designer visual authority:** an explicit Designer invocation has an available safe test target and browser. Result: enter its bounded per-unit/final UAT subphases without asking for a second UAT command; production access and destructive/external operations remain separately restricted.

## Skills and references

Preflight should inspect installed UX design, frontend visual, design-system, and review skills. Use relevant already-available skills when authorized; a `SKILLS_REGISTRY.md` link is not installation evidence. External tools retain host-level consent requirements. The core standard must work without any optional skill.
