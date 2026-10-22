# PHDK Design — visual direction before implementation

## Purpose, routing and authority

`PHDK design` establishes a visible, durable design baseline after technical/content planning and before implementing the affected interface. It is also mandatory lifecycle stage **25-design** for UI-applicable Auto and Auto Force goals. It prevents coding an arbitrary visual style and asking the owner to redesign the finished product.

Read `PHDK_PLAN.md`, `PHDK_UX_UI.md`, `PHDK_DESIGN_SYSTEM.md` and `PHDK_THEME_STANDARD.md` only as needed for the current task. `EXECUTION_SCOPE.md`, `PHDK_PRODUCTION_VERIFICATION.md`, actual host/security controls and current owner instructions remain authoritative. This standard adds no paid services, browser permission, local runtime tests, Docker, preview server, staging environment or provider writes.

The Auto/Auto Force lifecycle is **Capture → Plan → Design (25-design) → PMO/implementation → Integration → applicable SEO/AEO → Check/remediation → Delivery**. UAT Prep → UAT/Fix is a separate optional sequence initiated only by explicit `PHDK uat`. PMO may organize independent work earlier, but no UI workstream may implement an unresolved design. API-only/non-visual scope records evidence-based NOT APPLICABLE. A backend-only change to an existing UI product does not trigger a redesign.

`PHDK designer mode` remains the separate implementation/redesign mode for existing interfaces. It consumes or refreshes the Design baseline for a material new visual direction; it is not silently activated by `PHDK design`. Standalone Design produces the design package and its authorized repository delivery, not the full application. Neither quoted commands nor saved artifacts activate any mode.

## Decision policy: Auto asks; Auto Force decides

| Invocation | Required behavior |
|---|---|
| Standalone `PHDK design` | Show alternatives, ask one unresolved question at a time, wait for the answer, then request approval of the selected preview before affected UI implementation. |
| `PHDK auto` | Run the same guided choices and final visual approval. Do not infer a choice from silence, a recommendation, or generic authorization to build. Pause the dependent UI work; continue genuinely independent authorized work. |
| `PHDK auto force` | Generate/compare appropriate alternatives, choose the best supported direction, state the rationale and assumptions, record **AGENT_SELECTED_AUTO_FORCE**, and continue immediately. Do not wait for a style answer or visual sign-off. |

This mode distinction is a specific exception to ordinary Auto's generic no-interview/no-stage-approval language. The normal Auto design decision is intentional product input, not a ceremonial code-review gate. FORCE removes the PHDK-imposed design wait, not the Design stage, its deliverables, known brand decisions or actual controls. Never record agent selection as owner approval. An explicit current owner restriction such as “do not implement this interface until I approve this preview” still applies within its scope, including FORCE.

Reuse a current owner-approved baseline rather than asking the same questions again. FORCE may reuse a compatible earlier agent-selected baseline. Normal Auto must present an agent-selected-only baseline for owner choice before dependent new UI work. Record the exact baseline/assets and decision provenance. A later explicit mode switch to FORCE resolves an inherited PHDK-only design wait by making and recording the decision; a switch back to Auto requires the appropriate owner decision for still-unimplemented affected work. Never start from records alone.

For ordinary Auto awaiting input, keep the existing mandate, stage and next unanswered question in the lifecycle state. Use the existing BLOCKED stage status with reason `DESIGN_AWAITING_OWNER`, distinguish it from a technical failure, and retain completed work. Resume from the answer without repeating Capture, Preflight, prior choices or requesting a second implementation command. FORCE must not inherit that reason as a blocker unless an actual owner restriction remains.

## Entry: use what Plan already knows

Verify the current intent, audience/roles, primary tasks, content hierarchy/navigation, solution architecture, selected frontend stack and constraints. Consume `UX_ARCHITECTURE.md`, `UX_RESEARCH_BASELINE.md`, `UX_JOURNEYS.md`, `UI_DESIGN_SYSTEM.md`, `UX_UI_DECISIONS.md`, and the implementation/milestone plan. Plan owns the initial design constraints and draft design-system baseline; Design owns the visual alternatives, selected previews and final implementation-ready specification. Do not require final visual approval to enter Design.

Inspect available brand assets, prior owner choices, existing shared components/tokens and design-system compatibility. For greenfield projects without installed packages, distinguish **PLANNED** dependencies from verified installed ones; lack of a lockfile is not a reason to install/build an application before choosing its appearance. For brownfield scope preserve working flows, accessibility, permissions, brand and documented exceptions. Reuse valid designs and review only materially affected surfaces.

In a standalone invocation with genuinely missing architecture, collect the minimum missing context or identify the required Plan work; do not silently invent product scope or activate Auto. Inside an authorized Auto goal, repair the missing upstream planning in scope.

## Guided design session

Do not send a long questionnaire. Use existing answers first. Present one unresolved decision at a time with visual examples, concise tradeoffs and a recommendation grounded in the product. Default to four clearly distinct alternatives when meaningful; constrained brands may need fewer, with a reason. An owner may select a combination or reject the set. Never force every project into the same four aesthetic labels.

First recover references already supplied. When necessary in interactive Design/Auto, ask for a preferred site, screenshot, brand guide or example to avoid; an owner without references receives agent-proposed examples, not a homework assignment. Record what to borrow (for example hierarchy or density), what not to copy, source/provenance and actual access limitations. Do not fabricate visited sites, screenshots, interviews, licensing rights or an AI-authorship percentage. Do not publish confidential reference assets into a public repository.

The four decision groups are:

1. **Visual identity.** Tone, audience fit, brand personality, typography and image/icon language. Show comparable style tiles or moodboards, not just words such as “modern” or “premium”.
2. **Composition.** Navigation pattern, content hierarchy, page shell and information density. Use the same representative content/task for alternatives so the choice reflects design rather than different features.
3. **Graphic system.** Semantic palette, type scale, spacing, radii, elevation, buttons, fields, tables/cards and focus/disabled/error states. Show light/dark/corporate as coordinated presets, not three unrelated layouts.
4. **Experience in context.** Apply the selected direction to representative screens and the primary user journey, including responsive behavior, feedback and purposeful reduced-motion-aware interaction rules.

In FORCE perform these responsibilities without turning them into questions. Prefer an existing approved brand and familiar usable patterns over speculative novelty; choose safe reversible defaults when routine detail is missing. Explain a material tradeoff briefly and continue. New sensitive scope, spending and genuine user restrictions are not routine visual decisions.

## Preview before affected UI coding

Show actual accessible preview artifacts using currently available, authorized design/image/artifact capabilities. Prefer a small representative set: typically three screens covering the main entry, the primary task or data-heavy screen, and settings/admin when applicable. A simple one-page product needs proportionate coverage, not invented dashboards/admin pages. Include at least one narrow/mobile composition and relevant empty/loading/error/permission states, plus a short storyboard of the critical flow. These may be panels within the same boards; do not demand dozens of mockups.

Use real product labels and representative synthetic content rather than meaningless filler. Present comparison boards/images in **16:9 HD (1920×1080 or higher equivalent)** unless the owner specifies otherwise; show mobile portrait layouts inside those boards without stretching them or claiming the board is a mobile viewport. Preserve editable source when available and map the selected UI to real shared component/token names. Generated images are concepts, not evidence that the application renders or works.

Creating or inspecting a static design artifact is not browser UAT. Public references may be read through existing permitted read-only capabilities; this does not authorize interactive browsing, screenshots of a running application, executing prototype scripts, application probes, local servers, new deployments or paid generation services. App/browser verification still occurs only in the authorized UAT/UAT Fix phases on the permitted deployed target.

An HTML/SVG/specification file whose rendered result was not viewed is not a shown or visually verified preview. When visual tooling is unavailable, record the exact limitation and preserve editable specifications plus the next verification action. Interactive Design/Auto must disclose it and obtain an explicit informed owner choice to proceed from the available specification, recorded as `OWNER_ACCEPTED_SPEC_ONLY`; do not manufacture image approval. FORCE chooses from the best available evidence, records `AGENT_SELECTED_AUTO_FORCE` with `visual_evidence: UNVERIFIED`, and continues permitted implementation. Tool absence must not create a disguised human gate in FORCE or a fabricated visual PASS.

## Durable, compact design package

Reuse existing canonical artifacts; do not introduce a parallel set of truth documents:

- **`UI_DESIGN_SYSTEM.md`**: the visual style guide, selected direction, tokens, typography, layout/density/breakpoints, component catalog/states, three-theme semantics, icons, accessibility, motion and implementation mappings. Link to the existing single canonical CSS palette source; never add a competing palette file just for Design.
- **`UX_UI_DECISIONS.md`**: references/anti-references, alternatives, selections, rationale, assumptions, actual approval or agent-selection evidence, asset paths/revision, affected requirements and design-to-task mapping. Include the design gate record below.
- **`docs/design/`**: actual retained reference metadata/permitted assets, concept boards and selected previews/editable sources. Use `references/`, `concepts/` and `previews/` where useful, not empty folders/checklists. A small index in the existing decisions file is sufficient.
- **`docs/phdk/lifecycle/<run-id>/25-design/HANDOFF.md`**: in a lifecycle run, snapshot the relevant style guide, decisions and selected assets or immutable commit-addressed artifact references. Never rely only on a mutable external design link.

Minimum design gate record in `UX_UI_DECISIONS.md`:

```text
Design baseline: <stable ID and revision>
Scope: <requirements, routes, roles and critical flow>
Mode: DESIGN | AUTO | AUTO_FORCE
Decision: PENDING | OWNER_APPROVED | OWNER_ACCEPTED_SPEC_ONLY | AGENT_SELECTED_AUTO_FORCE | REUSED | NOT_APPLICABLE
Decision evidence: <actual owner message/date OR agent rationale; never a fabricated approval>
Reused authority: <original decision type/evidence when REUSED>
Selected assets: <existing paths and immutable revision, or explicit unavailable status>
Visual evidence: SHOWN | UNVERIFIED
Token/component source: <existing or planned canonical paths; distinguish the two>
Remaining limitations: <specific items, owner-accepted limitation where relevant>
Next action: <one answer needed OR authorized implementation action>
```

Do not fabricate message IDs, artifact paths or a future commit SHA. Record the actual revision when available. Store assets before relying on them for handoff; normal versioned repository delivery follows existing milestone/standalone scope, not a forced version bump simply because stage 25 ended. Source implementation later must match the selected baseline rather than invent a new style page by page.

## Exit, implementation and change control

Design is ready for dependent UI work only when applicability/inputs, the four relevant decision groups, representative preview/specification coverage, one authoritative token/component mapping and decision provenance are recorded. Interactive Design/Auto requires the owner's applicable decision; FORCE requires an explicit agent selection, not a pending owner review. Visual limitations remain explicit and are carried to UAT. A decision to proceed is not proof of accessibility, interaction behavior or appearance in the running product.

Refresh `IMPLEMENTATION_PLAN.md`, `MILESTONE_PLAN.md` and requirement/task links for material design consequences. Do not re-run the entire technical plan for a cosmetic decision. If design exposes a genuine architecture/feature/scope change, reopen only affected upstream decisions under existing authority and then reconcile downstream work.

PMO/workers receive the selected baseline, component/token source and their relevant screen/state slice, not every rejected moodboard or the whole design history. Shared components are implemented first where appropriate. New patterns extend the shared system; screens do not hardcode new palettes. Preserve centrally managed light/dark/corporate themes and the applicable authorized template editor.

A material direction, navigation or component-system change reopens affected Design decisions and invalidates affected visual evidence. In Auto ask about the changed choice only; in FORCE choose and record the revised baseline and continue. Routine fidelity fixes to an already selected design do not trigger another style interview. Existing brownfield products are not automatically redesigned merely because PHDK was upgraded.

## Integration, UAT and Check

Integration compares source/components/tokens against the selected baseline and records deviations without claiming a browser inspection. UAT compares the actual permitted deployed candidate with the selected previews and verifies representative journeys, states, responsive behavior, accessibility and theme parity. Functional success alone is not visual fidelity, and visual approval alone is not functional acceptance. Log and repair in-scope deviations under the existing UX/UI severity and UAT Fix rules.

`PHDK check` verifies applicability, decision provenance/mode, actual retained previews or disclosed limitations, stage 25 handoff when applicable, plan/task mappings, central theme/component consumption and current visual/runtime evidence. A file's mere existence is not PASS. Preserve bare Check's read-only boundary; authorized Auto/check-fix remediation repairs only in-scope gaps. Missing or stale evidence is GAP/UNVERIFIED as appropriate, never invented approval or runtime verification.

## Compatibility and progressive loading

Older Plan artifacts remain valid inputs: enrich/reuse them rather than renaming them or discarding owner decisions. Historic completed runs remain immutable; add stage 25 to new/current affected runs, not retrospective fictional approvals. Keep the four decisions inside this stage, not four extra lifecycle stages or release milestones.

Load this standard at Design entry, affected UI implementation handoff and applicable Check/UAT comparison. Retain a compact baseline pointer after the stage and reload detailed assets only for the current task. `PHDK_INTELLIGENT_EXECUTION.md` governs bounded in-session delegation; primary-agent ownership and all existing security/delivery boundaries remain unchanged.
