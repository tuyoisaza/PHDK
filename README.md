**Hybrid Secure (v2.63.0):** During Auto/Force, perform milestone security deltas and a consolidated `PHDK secure` gate after integration and before final Check/delivery, following [PHDK_SECURE.md](PHDK_SECURE.md). Secure is development validation only: it never initiates UAT Prep/UAT/Fix, forbidden local runtime tests, Docker, new infrastructure or paid scans. Remediate authorized vulnerabilities, preserve real security gates, record evidence and residual risk; Critical/High confirmed issues block clearance absent an explicit permitted owner risk decision.

# PHDK

**Node.js default:** New Node.js projects target the newest compatible security-patched Active LTS, with a supported Maintenance LTS fallback when no Active LTS exists or is compatible. Plan verifies and pins the runtime; Secure enforces npm supply-chain controls and deployment evidence. See [PHDK_SECURE.md](PHDK_SECURE.md).

**UAT is explicit-only (v2.62.0):** `PHDK auto` and `PHDK auto force` finish development, milestone releases, applicable non-UAT Check and delivery without running UAT Prep/UAT/Fix. They retain acceptance stories and offer `PHDK uat` only after delivery; only a fresh explicit `PHDK uat` invocation may begin acceptance and required preparation. `PHDK uat prep` alone does not initiate acceptance. The development lifecycle and optional acceptance path are shown separately below.

**Hook decisions (clarified in v2.65.2):** The [hook decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) must load before executing, blocking or asking about ambiguous build/packaging/hook commands. Distinguish static tooling from compiled-application load checks; repair only proven PHDK-owned steps within authorized scope, preserve independent controls, and propose the concrete remaining decision without requesting prohibited local-runtime exceptions.


**Project Handoff to Development Kit**\
**Version v2.68.0**

**Phase transitions:** [Phase-transition reconciliation](MAIN_DELIVERY_STANDARD.md#phase-transition-reconciliation) keeps temporary plan limits from becoming permanent prohibitions. Plan records the verified PHDK baseline and restriction provenance; a later scoped owner authorization reconciles existing task/plan/status and worker context without duplicate approval. Technical access, spending and explicit UAT remain separate controls; updating documents does not resolve an executor denial.

**Historical architecture audit:** [Intelligent development architecture audit](docs/audits/intelligent-development-architecture-2026-10-18.md) publishes the v2.56.0 assessment, estimates and migration/benchmark proposals, with an addendum identifying later policy changes. It is an optional historical report, not a current instruction or proof of performance gains.

**Optional Company Co documents:** [Quality-management importer corpus](https://github.com/tuyoisaza/PHDK/tree/main/docs/fixtures/companyco/iso9001-2025) provides 35 fictional documents covering 17 processes, editable Word and PDF versions, a consolidated dossier, OCR/version variants and expected extraction cases. This Spanish-language 2025 scenario is sample data for an explicitly requested import exercise; it is not a PHDK execution standard, certification claim or automatic UAT trigger. The corpus is available separately from the vendored standards.

PHDK is an operating system for AI-assisted software delivery. It turns a repository, an idea or an unfinished product into a structured process where AI can understand intent, define a visible design, coordinate work, implement, validate, repair and deliver without losing human control.

**New pre-implementation Design:** [`PHDK_DESIGN.md`](PHDK_DESIGN.md) introduces `PHDK design` and applicable lifecycle stage **25-design**, after technical/content Plan and before affected UI implementation. **Auto asks one visual question at a time and waits for your selection; Auto Force chooses, records its rationale and continues.** References, visual alternatives, representative previews and the selected style guide are retained in the repository. Agent selection is never reported as owner approval.

**Production-first verification (v2.58.0):** [PHDK_PRODUCTION_VERIFICATION.md](PHDK_PRODUCTION_VERIFICATION.md) governs all modes: local static checks/builds only; no local behavioral tests, Docker, extra staging/databases or preview servers. Runtime UAT uses the existing versioned production deployment/database, uniquely run-owned synthetic fixtures and verified cleanup. Static design concepts do not create a browser/runtime exception.

**Risk-based multi-tenant security (v2.59.0):** [PHDK_TENANT_RISK_STANDARD.md](PHDK_TENANT_RISK_STANDARD.md) requires consultative exposure/impact assessment before choosing tenant security architecture. Ask unresolved material questions one at a time; baseline isolation and sensitive-data protection remain mandatory. Per-tenant databases, field encryption, managed keys and dedicated infrastructure scale with assessed and owner-approved risk. No infrastructure changes or local behavioral tests are implied.

**Intelligent execution:** [PHDK_INTELLIGENT_EXECUTION.md](PHDK_INTELLIGENT_EXECUTION.md) permits bounded in-session delegation in any host-supported mode, keeps PMO for portfolio governance and loads context progressively by stage/task/specialist. Worker handoffs do not replace primary-agent integration and delivery. After Design, workers consume the relevant selected-baseline slice rather than every rejected concept.

**Milestone delivery:** [PHDK_PROJECT_MANAGEMENT_STANDARD.md](PHDK_PROJECT_MANAGEMENT_STANDARD.md) makes `MILESTONE_PLAN.md` the value roadmap. Auto/Force verify, version and merge each completed value milestone to verified main before continuing; final UAT maps milestones to user-value stories. Merely ending Plan, Design or another lifecycle stage does not trigger a release.

**Maintaining PHDK itself:** [PHDK_EVOLUTION_STANDARD.md](PHDK_EVOLUTION_STANDARD.md) governs fresh repository context, naming, workspace ownership, SemVer, release coherence and verified publication. Reading this guide does not activate Auto or authorize unattended changes.

**Continuity and communication:** [PHDK_AUTO_CONTINUITY.md](PHDK_AUTO_CONTINUITY.md) preserves the scoped mandate through compaction and actual delivery repair/retry. [PHDK_COMMUNICATION_STANDARD.md](PHDK_COMMUNICATION_STANDARD.md) requires concise evidence-based mode/version/progress/git/next-action reporting and avoids repetitive optional promotions. Neither creates background execution.

---

## The problem PHDK solves

Software delivery breaks down when requirements live only in chat, agents stop at plans/scaffolds, interfaces are designed only after implementation, parallel work lacks ownership, tests miss product intent, or nobody can show what shipped and what remains blocked.

PHDK makes the work **traceable, repeatable, governable and aligned with the product's actual intent**. Each stage leaves durable evidence, not only a conversational claim.

# Development lifecycle and optional acceptance

For applicable UI work:

```text
PHDK capture
    ↓
PHDK plan — technical stack, architecture and content/navigation structure
    ↓
PHDK design — references, visual choices, previews and selected style guide
    ↓
PHDK PMO / implementation — selected workstreams and real product development
    ↓
Integration Review — coherent candidate and actual owner/host controls
    ↓
SEO → AEO/GEO, when relevant
    ↓
PHDK secure (hybrid gate) → PHDK check → authorized remediation
    ↓
Verified delivery
```

After delivery, only a fresh explicit `PHDK uat` starts the optional acceptance path: necessary UAT Prep → UAT → explicitly authorized UAT Fix/retest. Standalone `PHDK uat prep` prepares identities without starting acceptance.

For a single focused workstream:

```text
Capture → Plan → Design → implementation/integration → applicable SEO/AEO → Check → delivery; optional explicit `PHDK uat` → UAT Prep/UAT/Fix
```

Or run `PHDK auto` for the complete authorized goal. Every invocation revalidates intent/requirements against actual code before reusing prior work, builds missing implementation and completes partial products. UI-independent work can proceed while normal Auto awaits a design choice; dependent UI cannot. Non-visual scopes record Design NOT APPLICABLE rather than inventing screens.

| Stage or mode | Purpose |
|---|---|
| **Capture** | Define intent, users, requirements, constraints and success criteria. |
| **Plan** | Define/reconstruct technical and content architecture plus executable value milestones. |
| **Design** | Select a visible product-specific direction and implementation-ready style guide before affected UI coding. |
| **PMO** | Coordinate confirmed workstreams, dependencies, ownership, workers and integration. |
| **Auto** | Execute the whole authorized lifecycle; ask unresolved Design choices. |
| **Auto Force** | Execute the same lifecycle; decide routine visual choices and remove PHDK-only human-review waits. |
| **Designer Mode** | Implement improvements/redesigns to an existing authorized interface. |
| **UX/UI quality** | Preserve usable journeys, accessible states, consistency and selected-design fidelity. |
| **UAT Prep** | Explicit preparation, standalone or necessary within an explicit UAT request; no automatic Auto stage. |
| **UAT / UAT Fix** | Explicit acceptance of the deployed candidate; repairs/retests require their own command or authorization within active explicit UAT. |
| **SEO / AEO-GEO** | Improve applicable public discoverability and factual answer clarity without invented ranking promises. |
| **CRUD governance** | Enforce justified resource × role × surface operations and authorization evidence. |
| **Secure** | Hybrid milestone security checks and consolidated pre-delivery audit/remediation. |\n| **Check** | Audit applicable standards and produce a scoped remediation backlog. |

# Before every command: PHDK Preflight

[PHDK_PREFLIGHT.md](PHDK_PREFLIGHT.md) verifies installation, canonical versus installed version, manifest/managed instruction integrity, relevant capabilities and actual tool availability. A registry URL is not proof a skill is installed. Use relevant available capabilities unless disabled by the owner; missing optional capabilities do not automatically block work.

When PHDK-owned standards are clean and stale, Preflight conservatively synchronizes from canonical main. It never silently overwrites dirty PHDK files or downstream owner content. Inside Auto, reuse Preflight and refresh only newly relevant capabilities instead of loading every standard at every stage. See [SKILLS_REGISTRY.md](SKILLS_REGISTRY.md).

# Lifecycle deliverables and historical handoffs

Current state is `PHDK_LIFECYCLE_STATUS.md`. Each full run records material stage evidence under:

```text
docs/phdk/lifecycle/<run-id>/
  00-preflight/
  10-capture/
  20-plan/
  25-design/
  30-pmo/
  40-integration/
  45-uat-prep/
  50-uat/
  60-uat-fix/
  65-seo/
  67-aeo-geo/
  70-check/
  80-remediation/
  90-delivery/
```

Each executed/reused stage has `HANDOFF.md` and material snapshots. Later stages validate required inputs and reopen only materially invalidated upstream decisions. Historic completed runs are not rewritten to invent retrospective Design approval. Full contract: [PHDK_LIFECYCLE.md](PHDK_LIFECYCLE.md).

| Stage | Canonical outputs |
|---|---|
| Preflight | `PHDK_PREFLIGHT_REPORT.md` |
| Capture | `PROJECT_INTENT.md`, `PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md`, `REQUIREMENTS_TRACEABILITY.md` |
| Plan | Solution/repository/UX architecture, UX baseline/journeys, draft `UI_DESIGN_SYSTEM.md` / `UX_UI_DECISIONS.md`, `MILESTONE_PLAN.md`, `IMPLEMENTATION_PLAN.md`, ADRs and TASK integration |
| Design | Refined **same** design-system/decisions files, actual assets in `docs/design/`, mode-correct decision provenance and affected plan/task updates |
| PMO | `PMO.md`, `PMO_WORKSTREAMS.md`, `PMO_DEPENDENCIES.md`, `PMO_STATUS.md` |
| Integration | `INTEGRATION_REPORT.md` |
| UAT Prep | `UAT_AUTH_PLAN.md`, `UAT_ROLE_MATRIX.md`, `UAT_FIXTURE_MANIFEST.md`, `UAT_PREP_REPORT.md` |
| UAT | `UAT_CASES.md`, `UAT_REPORT.md`, applicable `UX_UI_AUDIT_REPORT.md` |
| UAT Fix | `UAT_REMEDIATION.md`, retest/updated acceptance evidence and applicable UX/UI remediation |
| SEO | `SEO_AUDIT_REPORT.md`, `SEO_CHECKLIST.md`, `SEO_REMEDIATION_REPORT.md` or justified N/A |
| AEO/GEO | `AEO_GEO_AUDIT_REPORT.md`, `AEO_GEO_CHECKLIST.md`, `AEO_GEO_REMEDIATION_REPORT.md` or justified N/A |
| Check / remediation | `PHDK_CHECK_REPORT.md`, `PHDK_REMEDIATION_REPORT.md` when applicable |
| Delivery | `DELIVERY_REPORT.md` and completion/remote-target evidence |

# Core commands

## `PHDK capture`

Turn an idea or existing repository into a professional product baseline. Capture investigates docs, code/routes, domain models/APIs, tests, configuration, intents, ADRs, current task/status and relevant history before asking what remains unknown.

It separates stated intent, implemented behavior, inferred requirements, legacy/accidental behavior and open decisions. It creates the five Capture artifacts listed above, explicitly says whether material questions remain, and identifies the stored results for review. Capture alone does not implement the product.

## `PHDK plan`

Turn requirements into architecture and executable delivery work.

- **Greenfield:** define a target architecture appropriate to the requirements.
- **Brownfield:** reconstruct current architecture, preserve sound decisions and define incremental convergence; do not reset a working project to defaults.

Plan covers solution/repository topology, web/API boundaries, data ownership, integrations, auth/security, applicable AI, observability/verification, conceptual UX/content architecture and dependency ordering. It produces:

```text
SOLUTION_ARCHITECTURE.md
REPOSITORY_ARCHITECTURE.md
UX_ARCHITECTURE.md
MILESTONE_PLAN.md
IMPLEMENTATION_PLAN.md
ARCHITECTURE_DECISIONS.md   # when applicable
TASK.md
```

UI projects also retain the UX baseline/journeys and draft design-system constraints. **Plan does not pretend final visual choices are approved: it hands those inputs to Design.** Design later adjusts only affected tasks and decisions. See [PHDK_PLAN.md](PHDK_PLAN.md).

Value milestones map requirements, workstreams, dependencies, risks, acceptance evidence and expected SemVer impact. In Auto/Force, a completed value milestone is technically verified within permitted scope, versioned, committed with the version prefix, merged through the normal PR route and remotely verified; execution then continues from main. Final UAT maps milestones to user stories and cases.

## `PHDK design`

Define how the product should look and feel **before implementing its interface**.

```text
PHDK design
```

The stage consumes the planned tech stack, content/navigation structure, audience, primary tasks and existing brand decisions. It recovers references already provided and offers visual examples/recommendations when the owner has none. It does not assign reference-hunting homework or ask for information already known.

Four guided decision groups:

| Decision | What PHDK presents |
|---|---|
| **Identity** | Product-appropriate visual directions, typography and image/icon language. |
| **Composition** | Navigation, hierarchy, layout and density using comparable content. |
| **Graphic system** | Semantic palettes, type/spacing scale, shared components and relevant states. |
| **Experience** | Representative screens and the critical flow, including responsive composition and feedback. |

Default to four meaningful alternatives where useful, not four mandatory aesthetic labels for every product. Constrained brands may need fewer. Present one unresolved question at a time with a recommendation and tradeoffs; the owner can combine or reject options.

| Invocation | Who chooses? |
|---|---|
| Standalone `PHDK design` | The owner, through guided questions and selected-preview approval. |
| `PHDK auto` | The owner. Auto waits for the unresolved visual answer before dependent UI coding. |
| `PHDK auto force` | The agent. It chooses, records `AGENT_SELECTED_AUTO_FORCE` and continues without a PHDK visual-approval wait. |

Actual explicit owner restrictions, security and spending boundaries remain in all modes. FORCE never fabricates owner approval. Existing valid owner-approved baselines are reused instead of repeating the interview. Switching from Auto to Force resolves a PHDK-only design wait by making the choice, not skipping the design work.

Preview coverage is proportional: typically entry, primary task/data-heavy screen and settings/admin **only where applicable**, with a narrow/mobile composition, critical states and a short flow storyboard. Comparison boards default to **16:9 HD (1920×1080 or higher equivalent)**; mobile layouts are shown inside them without distortion. A one-page site does not acquire a fake dashboard to satisfy the template.

The durable package reuses existing truth documents:

```text
UI_DESIGN_SYSTEM.md       # selected visual style guide and implementation mappings
UX_UI_DECISIONS.md        # references, alternatives, choices, rationale and provenance
docs/design/
  references/            # metadata and permitted retained assets
  concepts/
  previews/              # selected artifacts and editable sources where available
docs/phdk/lifecycle/<run-id>/25-design/HANDOFF.md
```

The style guide maps to the **single canonical shared token/component source**, including light/dark/corporate semantics. It does not introduce a second palette or per-page hardcoded colors. Selected assets must be retained or immutably referenced, not only linked to a mutable external preview.

Static design concepts are not browser testing or proof the application works. Unrendered HTML/SVG is not a shown preview. When visual tooling is unavailable, Auto discloses the limitation and needs an informed `OWNER_ACCEPTED_SPEC_ONLY` choice; FORCE selects from available evidence, records visual evidence UNVERIFIED and continues permitted work. No local server, Docker, extra environment, paid workaround or new browser exception is required.

UAT later compares the actual deployed UI to the selected baseline; Check evaluates provenance, real artifacts, component/token usage and current evidence. Material design changes reopen only affected choices; routine fidelity repairs do not restart the interview. Full contract: [PHDK_DESIGN.md](PHDK_DESIGN.md).

## `PHDK designer mode`

This separate explicit mode inspects an existing interface, chooses a product-specific direction, **implements** improvements and performs permitted static checks. Rendered acceptance requires a separate explicit `PHDK uat`. It is not completed by delivering only a style guide or attractive screenshot.

Use [PHDK_DESIGNER_MODE.md](PHDK_DESIGNER_MODE.md) and actual design-system readiness. Preserve valid selected Design decisions, functionality, permissions, diagnostic controls and brand. Parent Auto/Force mode controls material new visual choices when present; standalone Designer retains its explicit autonomous redesign scope.

## `PHDK PMO`

Coordinate multiple active fronts. PMO reads requirements, plans, code, branches/PRs and acceptance/audit evidence, then presents a candidate portfolio for one confirmation/add/remove/reprioritize decision.

It manages dependencies, ownership, shared files/collision risks, workstream status, branches/worktrees, integration readiness and blockers. Its four canonical artifacts are in the deliverables table. Dependent UI work consumes the selected Design baseline; independent work may continue during an ordinary Auto design wait.

Any host-supported PHDK mode may delegate bounded in-session tasks under `PHDK_INTELLIGENT_EXECUTION.md`. PMO governs portfolio workstreams. Workers receive one confirmed scope, use bounded Auto semantics, cannot recursively delegate/select new work and cannot finalize shared global integration independently. The primary orchestrator owns the combined result. Without worker support, coordinate sequentially and say so.

## `PHDK auto`

Execute one complete authorized goal. **Auto now includes stack maintenance by default:** every new Auto/Force run performs a fresh Stack Security Review at Preflight and automatically applies compatible repository-owned security maintenance such as supported same-major Node.js security patches and compatible dependency security fixes. No separate `PHDK upgrade force` or remediation sentence is required. Major migrations, provider/infrastructure changes, spending, secret/account operations and explicit owner exclusions remain separate boundaries.


```text
PHDK auto
```

Auto rereads intent and requirements against actual code every invocation, reuses only current/coherent artifacts, builds absent code and completes partial implementation without discarding valid work. A scaffold or documentation is not a completed app; unavailable repository access remains UNVERIFIED.

**Plan → Design → implementation is one active goal.** Auto asks unresolved visual choices and waits for your answer; after the applicable Design decision, it continues without another development command or ceremonial approval. It does not silently reduce complete scope to an MVP. A design wait blocks dependent UI, not genuinely independent authorized tasks.

The Auto sequence includes Capture, Plan, Design, PMO/implementation, Integration, applicable SEO/AEO, Check/remediation and delivery. UAT Prep/UAT/Fix are separate optional stages triggered only by explicit `PHDK uat`. A status board shows development progress and marks UAT Prep/UAT/UAT Fix DEFERRED — OWNER OPT-IN, with UAT NOT RUN separate from completion. Generic Auto with several coherent active fronts uses PMO portfolio confirmation instead of forcing one arbitrary task.

## `PHDK auto force`

Use the same lifecycle with autonomous routine visual decisions and no PHDK-only human-review stops:

```text
PHDK auto force
```

FORCE still explores and records Design; it does not wait for style selection or final visual approval. It records agent selection and rationale, never a fictional owner sign-off. PHDK-only review gates are `NON_BLOCKING_BY_MODE` from entry without preventive reviewer/protection investigations. Actual owner/host/security restrictions remain.

FORCE reviews source/diff, performs permitted checks, pushes the scoped branch, opens/updates the PR, merges and reads back main. Actual hook/tool/GitHub failures trigger report → diagnosis → scoped repair → revalidation → retry; unchanged rejected writes, force-pushes, disabled hooks, alternate credentials/transports and provider-setting evasion are prohibited.

Both variants retain mandate provenance, scope/target/restrictions, progress and next action in `docs/phdk/lifecycle/<run-id>/AUTO_STATE.json`. The file is factual context, not cross-session authority. The advisor distinguishes `design_choice`: normal Auto waits with `DESIGN_AWAITING_OWNER`; FORCE returns a selection action before dependent UI. Independent tasks keep moving. Missing/malformed state is repaired internally. See [PHDK_AUTO_CONTINUITY.md](PHDK_AUTO_CONTINUITY.md) and [scripts/phdk_auto_gate.py](scripts/phdk_auto_gate.py).

Updating, installing or discussing PHDK never activates Auto. Neither mode executes in the background or continues after the active conversation ends.

## `PHDK uat prep`

Explicit `PHDK uat prep`, or necessary Prep within an explicitly initiated `PHDK uat`, follows [PHDK_UAT_PREP.md](PHDK_UAT_PREP.md) to implement missing safe Company Co synthetic identities, repeatable seeders, legitimate role sessions, authorized Test as, fixture ownership and cleanup. It produces auth/role/fixture/prep evidence, not merely a list of fictional users.

The production-first verification policy governs actual runtime checks. Prep does not grant browser access, authentication bypasses, human password/bearer collection, provider writes, local tests or new environments. If it changes code, reconcile/deliver the new candidate before acceptance. Stage 50 separately verifies browser availability.

## `PHDK uat`

Only a fresh explicit owner invocation starts acceptance and its necessary Prep. Auto/Force completion, deployment, Check and prior UAT failures do not start it. Acceptance follows:

```text
Project intent → user story → requirement/acceptance criterion → UAT case → evidence
```

Create `UAT_CASES.md` and `UAT_REPORT.md`. Results are PASS, FAIL, BLOCKED, MANUAL or NOT APPLICABLE; final conclusion is ACCEPTED, NOT ACCEPTED or ACCEPTANCE INCOMPLETE. Applicable UI cases compare actual rendered behavior with the selected Design baseline. Neither code inspection, owner visual approval nor generated mockups become behavioral PASS.

Read [JWT_STANDARD.md](JWT_STANDARD.md), [UAT_JOURNEY_STANDARD.md](UAT_JOURNEY_STANDARD.md) and [USE_COMPANY_CO_INFO_FOR_DEMOS.md](USE_COMPANY_CO_INFO_FOR_DEMOS.md) when authenticated journeys/fixtures apply. Use legitimate role-specific sessions, safe synthetic records, negative tenant/role boundaries and auditable elevated switching. JWT is conditional on actual application authentication, not mandatory for OAuth/cookie apps. Never request secrets in chat or fabricate privileged access. No automatic bulk email to `@tujuisasa.com`.

[UAT_BROWSER_READINESS_STANDARD.md](UAT_BROWSER_READINESS_STANDARD.md) separately verifies phase permission and actual connected browser, with no invented paid workaround. Keep unavailable cases blocked and independent cases moving. Revoke sessions and verify synthetic cleanup on success, failure or interruption.

## `PHDK uat fix`

Explicit `PHDK uat fix`, or repair authorization within an active explicitly initiated UAT, turns unresolved acceptance into defects and an executable repair plan. For each FAIL/BLOCKED/MANUAL case, identify cause, impact, actor, location, ordered action, closure evidence and retest command. Repair in-scope source/auth/fixture gaps and rerun only permitted deployed cases. Do not create local/in-process harness execution contrary to the governing policy.

Real external account, provider, secret, host-control or browser limitations get exact owner actions rather than a bare BLOCKED label. Material design direction changes follow the current mode's affected-choice policy; fidelity fixes do not require a fresh full interview.

## SEO and AEO/GEO — after Integration, before Check

[PHDK_SEO.md](PHDK_SEO.md) audits and applies safe public-site corrections; [PHDK_AEO_GEO.md](PHDK_AEO_GEO.md) improves factual answers, entity clarity and source credibility. Both retain reports/handoffs and permitted static verification evidence. Auto does not require UAT reports or runtime regressions; a later explicit UAT validates affected behavior. Private-only scope records justified N/A. Neither grants extra production/browser/provider access or promises rankings/AI citations.

## `PHDK check`

Audit applicability and actual implementation/evidence. Findings include COMPLIANT, GAP, PARTIAL, NOT APPLICABLE, UNKNOWN / DECISION NEEDED and UNVERIFIED. Remediation is AUTO-FIXABLE, FIXABLE WITH VALIDATION, DECISION REQUIRED or EXTERNAL / MANUAL.

The first bare Check is read-only except its report, followed by one question about executing enumerated fixable gaps. A yes authorizes that backlog only. `PHDK check --fix` explicitly includes safe in-scope remediation; active Auto also repairs its applicable authorized gaps. Sensitive tenancy/permissions, live destructive effects and external credentials are not silently authorized.

For UI scope, inspect Design provenance, retained previews or disclosed limitations, stage25 handoff, shared tokens/components and actual fidelity evidence. A valid FORCE agent choice is not missing owner approval; a file's mere existence is not compliance.

# Cross-cutting product standards

## Universal administration console

[ADMIN_CONSOLE_STANDARD.md](ADMIN_CONSOLE_STANDARD.md) requires real protected Configuración / Settings for applicable administered portals. Establish single tenant (elevated admin) versus multi-tenant (platform super_admin plus tenant admins), without silent migration. Implement actual users/invitations/roles/permissions, applicable tenant lifecycle, locale, safe debug/integrations/secret status, backups/audit/security/observability, templates and auditable role testing. Require UI + API + persistence + negative-permission evidence, not placeholder tabs.

For AI products, Prompts describes agent purpose, callsite, approved DB/API inputs, versioned prompts, JSON output schema and destination/next-agent workflow graph. Applicable roles and security boundaries remain server-enforced.

## Automation and cost hygiene

[PHDK_AUTOMATION_HYGIENE.md](PHDK_AUTOMATION_HYGIENE.md) applies to every Check: identify leftover PHDK Actions, agents, schedules, watcher/reload loops, cron/restart storms and CI waits. Compare source with read-only GitHub/Railway state, preserve valid checks/autodeploy and label unavailable remote evidence UNVERIFIED. The vendored static collector cannot prove workflows inactive; provider reconfiguration is not an automatic fix.

## Canonical design system and themes

[PHDK_DESIGN_SYSTEM.md](PHDK_DESIGN_SYSTEM.md) defines applicable shared shadcn-compatible/Radix components, Tailwind semantic tokens, Motion, Lucide and en/es/pt conventions. Preserve project exceptions and actual installed compatibility. Designer Mode checks readiness before implementation; greenfield Design may specify compatible planned dependencies without claiming installation.

[PHDK_THEME_STANDARD.md](PHDK_THEME_STANDARD.md) requires one canonical light/dark/corporate semantic palette source and no hardcoded per-screen colors. The applicable platform administrator edits persisted presets in Configuración → Edición de templates, with corporate visibility/fallback controls and server-side permissions. [scripts/phdk_theme_audit.py](scripts/phdk_theme_audit.py) gives static signals, not runtime persistence/propagation/accessibility proof.

## Verified completion

[PHDK_COMPLETION_GATE.md](PHDK_COMPLETION_GATE.md) requires remote SHA/version and honest machine-readable evidence after main delivery. PR state, scope and commitments remain independently audited. Open PRs or locally generated files are not published completion.

# Standards activate only when relevant

Intent and requirements determine applicability. Do not add RBAC to a role-free product, AI infrastructure without AI, migrations without schema changes, PMO overhead for one simple task or a Design interview for non-visual scope. A standard's existence is not authorization for new features.

# AI-native project support

Actual AI integrations require centralized provider access (`packages/ai` or equivalent), configurable provider/model, prompt-injection defenses, structured output validation, token/cost observability and attribution, rate/cost safeguards, timeouts/retry limits and kill switches.

Applicable privileged administration includes Prompts with an agent/prompt list, editable Name, Personality prompt, Execution prompt and Output JSON schema, stable identity, revisions and audit history. Consumption evidence attributes provider/model, feature/workflow, agent/prompt revision, tokens/cost, latency and errors. Projects without AI do not receive these requirements. No unapproved paid verification follows from these standards.

# Human control and safety boundaries

Autonomy operates inside explicit human direction. Owners define intent, portfolio, material product/security choices, actual formal approvals and external actions. Normal Auto asks visual choices; FORCE delegates those routine choices to the agent without fabricating owner approval. Real retained owner restrictions, security/access controls, hooks and spending boundaries remain effective.

No unattended/overnight execution, recurring agents, Actions/hosted CI activation, local runtime tests, Docker, preview servers/new staging/databases, secret inspection, real-data test mutations or provider administration. Browser/headless application verification is only scoped UAT/UAT Fix on the existing permitted deployment. Static design artifact creation is distinct, and never proves behavior. See [EXECUTION_SCOPE.md](EXECUTION_SCOPE.md) and [PHDK_PRODUCTION_VERIFICATION.md](PHDK_PRODUCTION_VERIFICATION.md).

## Stack review on upgrade

Every `PHDK upgrade` / `PHDK upgrade force` includes the bounded read-only [Stack Security Review](PHDK_SECURE.md#stack-security-review), even when standards are already current. Preflight runs it once when adopting a new version. It checks runtimes, resolved dependencies/frameworks, images and data engines against current official advisories/support schedules, separating source, build and deployed evidence.

Report **STANDARDS_SYNC**, **STACK_REVIEW_COVERAGE** and **STACK_SECURITY_STATUS** independently. Vendoring can succeed with security findings or unverified runtime evidence; it does not patch the application. Existing supported Node majors receive patch recommendations first; EOL/major migrations require compatibility work. Reuse current evidence at unchanged stages; no scheduler, new infrastructure, package installation or UAT is introduced.

## Central downstream repository status

[PHDK_REPOSITORY_STATUS.md](PHDK_REPOSITORY_STATUS.md) defines a lightweight registry for PHDK repositories owned by `tuyoisaza`. When a foreground PHDK session is operating on `tuyoisaza/<repo>` and already has write access to canonical `tuyoisaza/PHDK`, it refreshes:

```text
docs/repos/<repo>/status.md
```

The snapshot records the downstream PHDK version, observed repository SHA, evidence-backed runtime/framework/package-manager/data-engine/image versions and the independent Stack Security Review result. This lets maintainers identify repositories behind the current PHDK release or current stack-security recommendations. Missing canonical write access is reported without blocking the downstream task or requesting credentials. No background agent, crawler, Action, webhook or scheduler is introduced.

# Keep PHDK synchronized

```text
PHDK upgrade
```

Conservatively synchronizes standards, preserving dirty PHDK files and reporting conflicts, then reviews the actual project stack even when no standards changed.

```text
PHDK upgrade force
```

Performs the forced standards synchronization and Stack Security Review, then **immediately continues as `PHDK auto force` in the same session**. If there is an active authorized development goal, it continues it; otherwise it runs bounded repository maintenance: reconcile against current PHDK and recorded product intent, remediate compatible security/standards gaps, Check/remediate and deliver without inventing new features. The upgrade phase still replaces only manifest-owned `phdk-standards/` files and exact `PHDK-MANAGED` blocks. The chained Auto Force preserves all normal exclusions for UAT, major/material decisions, provider/infrastructure writes, spending, secrets and real controls.

# Other operational commands

`PHDK unlock` reconciles documentary blockers while preserving actual protections, access, security and controls. `PHDK Developer Mode` is a separate explicitly activated, temporary direct-main exception for eligible small low-risk tasks. Neither silently starts another mission.

# How to start

For explicit stages on a UI project:

```text
PHDK capture
PHDK plan
PHDK design
PHDK PMO
```

Then implement and continue applicable acceptance/audit/delivery. Or use `PHDK auto` for the complete goal with guided visual choices; use `PHDK auto force` to let the agent choose and continue.

The lifecycle board includes Preflight, Capture, Plan, **Design**, PMO/Workstreams, Integration, UAT Prep/UAT/Fix, SEO/AEO, Check/Remediation and Delivery. Development statuses are PENDING, RUNNING, REUSED, COMPLETED, BLOCKED and NOT APPLICABLE. In Auto, UAT Prep/UAT/UAT Fix instead remain DEFERRED — OWNER OPT-IN, with UAT NOT RUN; their absence does not block delivery. A normal Auto design wait is explicitly `DESIGN_AWAITING_OWNER`; answering resumes the active goal.

For an existing project, use `PHDK upgrade`, then Capture/Plan to reconstruct intent and architecture. Design reuses valid choices and changes only affected scope; no automatic wholesale redesign. `PHDK auto` performs this reconciliation within an authorized complete goal. For unclear standards drift, use `PHDK check` first.

# The PHDK philosophy

Intent before implementation; visible design before dependent UI coding; requirements and decisions that survive chat sessions; complete authorized work rather than ceremonial continuation prompts; parallel ownership/integration discipline; acceptance tied to user needs; actionable blockers; proportionate standards; autonomy with accountability; evidence for every completion claim; and a repository that preserves the project's durable memory.

# Documentation map

| Need | Read |
|---|---|
| Maintainer sessions/evolution | [PHDK_EVOLUTION_STANDARD.md](PHDK_EVOLUTION_STANDARD.md) |
| Execution boundaries | [EXECUTION_SCOPE.md](EXECUTION_SCOPE.md) |
| Production-first verification | [PHDK_PRODUCTION_VERIFICATION.md](PHDK_PRODUCTION_VERIFICATION.md) |
| Preflight | [PHDK_PREFLIGHT.md](PHDK_PREFLIGHT.md) |
| Lifecycle/historical handoffs | [PHDK_LIFECYCLE.md](PHDK_LIFECYCLE.md) |
| Capabilities/progressive execution | [SKILLS_REGISTRY.md](SKILLS_REGISTRY.md), [PHDK_INTELLIGENT_EXECUTION.md](PHDK_INTELLIGENT_EXECUTION.md) |
| Requirements capture | [PHDK_CAPTURE.md](PHDK_CAPTURE.md) |
| Architecture/planning | [PHDK_PLAN.md](PHDK_PLAN.md) |
| Visual style guide/previews/choices | [PHDK_DESIGN.md](PHDK_DESIGN.md) |
| Existing-interface implementation/redesign | [PHDK_DESIGNER_MODE.md](PHDK_DESIGNER_MODE.md) |
| Milestones | [PHDK_PROJECT_MANAGEMENT_STANDARD.md](PHDK_PROJECT_MANAGEMENT_STANDARD.md) |
| Workstream coordination | [PHDK_PMO.md](PHDK_PMO.md) |
| Whole-goal development | [PHDK_AUTO.md](PHDK_AUTO.md) |
| FORCE, design choice continuity, repair/retry | [PHDK_AUTO_CONTINUITY.md](PHDK_AUTO_CONTINUITY.md) |
| UAT preparation | [PHDK_UAT_PREP.md](PHDK_UAT_PREP.md) |
| UAT/repair | [UAT_STANDARD.md](UAT_STANDARD.md) |
| Compliance | [PHDK_CHECK.md](PHDK_CHECK.md) |
| Main delivery | [MAIN_DELIVERY_STANDARD.md](MAIN_DELIVERY_STANDARD.md) |
| AI administration | [AI_ADMIN_STANDARD.md](AI_ADMIN_STANDARD.md) |
| Testing rules | [TESTING_STANDARD.md](TESTING_STANDARD.md) |
| Security/tenant risk | [DEVSECOPS.md](DEVSECOPS.md), [PHDK_TENANT_RISK_STANDARD.md](PHDK_TENANT_RISK_STANDARD.md) |
| Versioning | [VERSIONING.md](VERSIONING.md) |
| Upgrade | [PHDK_UPGRADE.md](PHDK_UPGRADE.md) |
| Repository status registry | [PHDK_REPOSITORY_STATUS.md](PHDK_REPOSITORY_STATUS.md) |
| Changes/releases | [CHANGE_MANAGEMENT.md](CHANGE_MANAGEMENT.md) |
| Technical release history | [CHANGELOG.md](CHANGELOG.md) |

# Installation

Vendor the exact `PHDK_MANIFEST.txt` mappings under `phdk-standards/` and add the appropriate managed block to the active coding tool's native instructions, preserving owner content.

| Tool | Project-local skill location |
|---|---|
| Claude Code | `.claude/skills/phdk` |
| Cursor | `.cursor/skills/phdk` |
| Codex CLI / Antigravity | `.agents/skills/phdk` |
| Windsurf | `.windsurf/skills/phdk` |
| VS Code / GitHub Copilot | `.github/skills/phdk` |
| OpenCode | `.opencode/skills/phdk` |
| Pi | `.pi/skills/phdk` |

Use the tool actually in use. No background updater, scheduler or CI agent is required.

# Project status

PHDK is actively evolving. This README describes what it is and how to use it, not a substitute for release history. See [CHANGE_MANAGEMENT.md](CHANGE_MANAGEMENT.md) and [CHANGELOG.md](CHANGELOG.md) for release notes and historical changes.
