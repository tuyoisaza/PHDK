# PHDK Design — visual direction before implementation

## Chosen record workspace controls (v3.1.0)

If the owner enabled a named resource under `PHDK_FLEXIBLE_DATA_WORKSPACE_STANDARD.md`, include its **selected** sortable header, combined filter, column-picker/order, view-saving, privileged custom-field manager, inline entry and recovery states in the same consolidated coded decision board and representative preview. Use existing tokens, accessibility and role-specific behavior. Do not invent a second design approval or infer optional feature authorization from an Auto Force visual selection. If declined, design ordinary CRUD without the advanced profile.


## Purpose, routing and authority

`PHDK design` establishes a visible, durable design baseline after technical/content planning and before implementing the affected interface. It is also mandatory lifecycle stage **25-design** for UI-applicable Auto and Auto Force goals. It prevents coding an arbitrary visual style and asking the owner to redesign the finished product.

Read `PHDK_PLAN.md`, `PHDK_UX_UI.md`, `PHDK_DESIGN_SYSTEM.md` and `PHDK_THEME_STANDARD.md` only as needed for the current task. `EXECUTION_SCOPE.md`, `PHDK_PRODUCTION_VERIFICATION.md`, actual host/security controls and current owner instructions remain authoritative. This standard adds no paid services, browser permission, local runtime tests, Docker, preview server, staging environment or provider writes.

The Auto/Auto Force lifecycle is **Capture → Plan → Design (25-design) → PMO/implementation → Integration → applicable SEO/AEO → Check/remediation → Delivery**. UAT Prep → UAT/Fix is a separate optional sequence initiated only by explicit `PHDK uat`. PMO may organize independent work earlier, but no UI workstream may implement an unresolved design. API-only/non-visual scope records evidence-based NOT APPLICABLE. A backend-only change to an existing UI product does not trigger a redesign.

`PHDK designer mode` remains the separate implementation/redesign mode for existing interfaces. It consumes or refreshes the Design baseline for a material new visual direction; it is not silently activated by `PHDK design`. Standalone Design produces the design package and its authorized repository delivery, not the full application. Neither quoted commands nor saved artifacts activate any mode.

## Decision policy — consolidated board; Auto Force chooses

There are **two separately traceable Design decisions in one evolution**: (A) how design alternatives are selected, and (B) how transitions/microinteractions behave. Both remain in stage 25-design and share one combined recommendation/preview and one owner sign-off; do not create an independent motion approval.

| Invocation | Required behavior |
|---|---|
| Standalone `PHDK design` | Show **all material coded visual and motion choices together** with options, tradeoffs and per-item recommendations, one coherent default bundle and its integrated preview. Owner can **approve all** or **override selected codes**. If overrides materially change the result, show a refreshed composite preview and obtain one final acceptance. |
| `PHDK auto` | Same consolidated recommendation/preview and one owner approve-all/override response. Dependent UI waits; genuinely independent authorized work continues. |
| `PHDK auto force` | Compare the full map, select a coherent visual/motion bundle with per-item rationale, record `AGENT_SELECTED_AUTO_FORCE`, and continue without a PHDK owner review pause. |

Reuse actual previously owner-approved visual and motion choices independently; agent defaults, silence or generated previews are **not** owner approval. Reopen only changed codes and their impacted preview. A known owner restriction still applies in Force, as do security, access and spend constraints.

Normal Auto pending input remains `design_choice` / `DESIGN_AWAITING_OWNER`; record the map revision, unresolved codes, recommended bundle, combined preview/limitations and **one actionable owner request** (approve all or specify overrides), rather than a sequence of cosmetic questions. The response resumes the same mandate without another implementation command. Switching to Force resolves PHDK-only visual waits with actual agent selections, never by fabricating approval or waiving real owner stops.

## Entry: use what Plan already knows

Verify the current intent, audience/roles, primary tasks, content hierarchy/navigation, solution architecture, selected frontend stack and constraints. Consume `UX_ARCHITECTURE.md`, `UX_RESEARCH_BASELINE.md`, `UX_JOURNEYS.md`, `UI_DESIGN_SYSTEM.md`, `UX_UI_DECISIONS.md`, and the implementation/milestone plan. Plan owns the initial design constraints and draft design-system baseline; Design owns the visual alternatives, selected previews and final implementation-ready specification. Do not require final visual approval to enter Design.

Inspect available brand assets, prior owner choices, existing shared components/tokens and design-system compatibility. For greenfield projects without installed packages, distinguish **PLANNED** dependencies from verified installed ones; lack of a lockfile is not a reason to install/build an application before choosing its appearance. For brownfield scope preserve working flows, accessibility, permissions, brand and documented exceptions. Reuse valid designs and review only materially affected surfaces.

In a standalone invocation with genuinely missing architecture, collect the minimum missing context or identify the required Plan work; do not silently invent product scope or activate Auto. Inside an authorized Auto goal, repair the missing upstream planning in scope.

## Consolidated decision map and combined preview

Use Plan, brand assets, known choices and real product journeys first. Ask **one essential clarifying question** only when a material unknown prevents sound options. Do **not** conduct the prior serial one-question-per-choice visual interview. Present a single scannable map of **all relevant decisions** (for example 8, 12, 14 or 17; no fixed quota). Each row gives a **stable code** (e.g. `A3`, `B2`, `C4`), title, affected component/role, 2–4 distinct options when useful, concise tradeoff and **one recommended option**. Mark inherited owner-approved choices as approved/locked rather than recasting them as AI defaults.

Provide a complete recommended combination (`A3 · B2 · C4 · …`) and show **what accepting all recommendations looks like together**: representative screens with the same task content, responsive/empty/error states and a short annotated before→action→after transition storyboard. Identify incompatible choices before recommending a combination. Owner can say **“approve all”** or override chosen codes (e.g. “A2 and C1; rest recommended”). Preserve all unchanged decisions; recalculate the affected composite preview and seek final acceptance only when the result materially changed. If the owner approves the initially shown coherent preview, that is the single needed sign-off.

Keep the four existing visual responsibility groups (not extra lifecycle stages):
1. **Visual identity**: brand tone, typography, image/icon language.
2. **Composition**: navigation, shell, information hierarchy and density.
3. **Graphic system**: semantic palette/themes, type scale, spacing, radii, buttons, table/card states.
4. **Experience in context**: representative screens, primary journey, responsive and feedback states.

**Separate motion/interaction decision domain:** intensity (minimal/static, **discreet functional** default, expressive if justified), menu switch, button feedback, tab content, accordion expand/collapse, modal open/close, view/route continuity, focus and reduced-motion alternative as material to the product. The normative **Motion interaction contract** is in `PHDK_DESIGN_SYSTEM.md`. Do not infer motion approval from the visual style or add mandatory animation choices to a static product.

Record actual owner/Force provenance for every selected visual and motion code. A recommendation, partial answer or image does not establish owner approval. Reference sources and accessibility constraints honestly; do not invent visited sites, screenshots, interviews or AI-generated-text percentages.

## Preview before affected UI coding

Show actual accessible preview artifacts using currently available, authorized design/image/artifact capabilities. Prefer a small representative set: typically three screens covering the main entry, the primary task or data-heavy screen, and settings/admin when applicable. A simple one-page product needs proportionate coverage, not invented dashboards/admin pages. Include at least one narrow/mobile composition and relevant empty/loading/error/permission states, plus a short storyboard of the critical flow **and relevant motion** (trigger, exit/enter or expand/collapse, focus/result, proposed timing and reduced-motion fallback). Static frames do not prove animation works. These may be panels within the same boards; do not demand dozens of mockups.

Use real product labels and representative synthetic content rather than meaningless filler. Present comparison boards/images in **16:9 HD (1920×1080 or higher equivalent)** unless the owner specifies otherwise; show mobile portrait layouts inside those boards without stretching them or claiming the board is a mobile viewport. Preserve editable source when available and map the selected UI to real shared component/token names. Generated images are concepts, not evidence that the application renders or works.

Creating or inspecting a static design artifact is not browser UAT. Public references may be read through existing permitted read-only capabilities; this does not authorize interactive browsing, screenshots of a running application, executing prototype scripts, application probes, local servers, new deployments or paid generation services. App/browser verification still occurs only in the authorized UAT/UAT Fix phases on the permitted deployed target.

An HTML/SVG/specification file whose rendered result was not viewed is not a shown or visually verified preview. When visual tooling is unavailable, record the exact limitation and preserve editable specifications plus the next verification action. Interactive Design/Auto must disclose it and obtain an explicit informed owner choice to proceed from the available specification, recorded as `OWNER_ACCEPTED_SPEC_ONLY`; do not manufacture image approval. FORCE chooses from the best available evidence, records `AGENT_SELECTED_AUTO_FORCE` with `visual_evidence: UNVERIFIED`, and continues permitted implementation. Tool absence must not create a disguised human gate in FORCE or a fabricated visual PASS.

## Durable, compact design package

**Versioned location rule:** Apply [PHDK_DOCUMENTATION_STANDARD.md](PHDK_DOCUMENTATION_STANDARD.md). New/revised style guides live at `docs/plans/ui-design-system.vN.md`, new decision records at `docs/decisions/ux-ui-decisions.vN.md`, and retained visual assets at `docs/images/<topic>/vN/`. Read the active baseline from `docs/INDEX.md`; a newer draft is not automatic approval. The legacy `UI_DESIGN_SYSTEM.md`, `UX_UI_DECISIONS.md` and `docs/design/` paths below remain accepted for existing projects; do not migrate them on a passive upgrade or create a parallel design truth. Design selection/provenance and stage-25 handoff requirements remain unchanged.


Reuse existing canonical artifacts; do not introduce a parallel set of truth documents:

- **`UI_DESIGN_SYSTEM.md`**: the visual style guide, selected direction, tokens, typography, layout/density/breakpoints, component catalog/states, three-theme semantics, icons, accessibility, motion and implementation mappings. Link to the existing single canonical CSS palette source; never add a competing palette file just for Design.
- **`UX_UI_DECISIONS.md`**: consolidated coded decision map, recommended/selected bundle, independently attributable visual and motion choices, owner overrides, alternatives, rationale, actual owner/agent selection evidence, preview paths/revision and design-to-task mapping. Include the design gate record below.
- **`docs/design/`**: actual retained reference metadata/permitted assets, concept boards and selected previews/editable sources. Use `references/`, `concepts/` and `previews/` where useful, not empty folders/checklists. A small index in the existing decisions file is sufficient.
- **`docs/phdk/lifecycle/<run-id>/25-design/HANDOFF.md`**: in a lifecycle run, snapshot the relevant style guide, decisions and selected assets or immutable commit-addressed artifact references. Never rely only on a mutable external design link.

Minimum design gate record in `UX_UI_DECISIONS.md`:

```text
Design baseline: <stable ID and revision>
Decision map: <stable revision, all applicable coded alternatives and recommended bundle>
Selected bundle: <accepted or agent-selected codes, overrides and reused approved choices>
Motion choice: <separately attributable motion codes/preset/reduced-motion policy, or N/A>
Scope: <requirements, routes, roles and critical flow>
Mode: DESIGN | AUTO | AUTO_FORCE
Decision: PENDING | OWNER_APPROVED | OWNER_ACCEPTED_SPEC_ONLY | AGENT_SELECTED_AUTO_FORCE | REUSED | NOT_APPLICABLE
Decision evidence: <actual owner message/date OR agent rationale; never a fabricated approval>
Reused authority: <original decision type/evidence when REUSED>
Selected assets: <existing paths and immutable revision, or explicit unavailable status>
Composite preview: <integrated screens and interaction storyboard, or explicit limitation>
Visual evidence: SHOWN | UNVERIFIED
Token/component source: <existing or planned canonical paths; distinguish the two>
Remaining limitations: <specific items, owner-accepted limitation where relevant>
Next action: <one answer needed OR authorized implementation action>
```

Do not fabricate message IDs, artifact paths or a future commit SHA. Record the actual revision when available. Store assets before relying on them for handoff; normal versioned repository delivery follows existing milestone/standalone scope, not a forced version bump simply because stage 25 ended. Source implementation later must match the selected baseline rather than invent a new style page by page.

## Exit, implementation and change control

Design is ready for dependent UI work only when applicability/inputs, four visual groups **and separately material motion choices** are covered in a coded decision map, coherent combined preview/specification, shared token/component/motion mapping and actual decision provenance are recorded. Interactive Design/Auto requires the owner's applicable decision; FORCE requires an explicit agent selection, not a pending owner review. Visual limitations remain explicit and are carried to UAT. A decision to proceed is not proof of accessibility, interaction behavior or appearance in the running product.

Refresh `IMPLEMENTATION_PLAN.md`, `MILESTONE_PLAN.md` and requirement/task links for material design consequences. Do not re-run the entire technical plan for a cosmetic decision. If design exposes a genuine architecture/feature/scope change, reopen only affected upstream decisions under existing authority and then reconcile downstream work.

PMO/workers receive the selected baseline, component/token source and their relevant screen/state slice, not every rejected moodboard or the whole design history. Shared components are implemented first where appropriate. New patterns extend the shared system; screens do not hardcode new palettes. Preserve centrally managed light/dark/corporate themes and the applicable authorized template editor.

A material direction, navigation or component-system change reopens affected Design decisions and invalidates affected visual evidence. In Auto ask about the changed choice only; in FORCE choose and record the revised baseline and continue. Routine fidelity fixes to an already selected design do not trigger another style interview. Existing brownfield products are not automatically redesigned merely because PHDK was upgraded.

## Integration, UAT and Check

Integration compares source/components/tokens plus applicable motion/focus/reduced-motion mappings against the selected baseline without claiming a browser inspection. UAT compares the actual permitted deployed candidate with the selected previews and verifies representative journeys, states, responsive behavior, accessibility and theme parity. Functional success alone is not visual fidelity, and visual approval alone is not functional acceptance. Log and repair in-scope deviations under the existing UX/UI severity and UAT Fix rules.

`PHDK check` verifies applicability, decision provenance/mode, actual retained previews or disclosed limitations, stage 25 handoff when applicable, plan/task mappings, central theme/component consumption and current visual/runtime evidence. A file's mere existence is not PASS. Preserve bare Check's read-only boundary; authorized Auto/check-fix remediation repairs only in-scope gaps. Missing or stale evidence is GAP/UNVERIFIED as appropriate, never invented approval or runtime verification.

## Compatibility and progressive loading

Older Plan artifacts remain valid inputs: enrich/reuse them rather than renaming them or discarding owner decisions. Historic completed runs remain immutable; add stage 25 to new/current affected runs, not retrospective fictional approvals. Keep the four decisions inside this stage, not four extra lifecycle stages or release milestones.

Load this standard at Design entry, affected UI implementation handoff and applicable Check/UAT comparison. Retain a compact baseline pointer after the stage and reload detailed assets only for the current task. `PHDK_INTELLIGENT_EXECUTION.md` governs bounded in-session delegation; primary-agent ownership and all existing security/delivery boundaries remain unchanged.
