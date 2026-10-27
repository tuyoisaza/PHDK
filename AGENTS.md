**Hybrid Secure (v2.63.0):** During Auto/Force, perform milestone security deltas and a consolidated `PHDK secure` gate after integration and before final Check/delivery, following [PHDK_SECURE.md](PHDK_SECURE.md). Secure is development validation only: it never initiates UAT Prep/UAT/Fix, forbidden local runtime tests, Docker, new infrastructure or paid scans. Remediate authorized vulnerabilities, preserve real security gates, record evidence and residual risk; Critical/High confirmed issues block clearance absent an explicit permitted owner risk decision.

## Explicit-only UAT authorization

**Binding rule:** `PHDK auto` and `PHDK auto force` MUST NOT invoke, enter, provision, seed, or run UAT Prep (45), UAT (50), or UAT Fix (60), even after milestones, deployment, Check, or a failed prior UAT. Neither FORCE nor a generic full-lifecycle instruction grants UAT authorization. These stages are **DEFERRED — OWNER OPT-IN**, not BLOCKED, FAILED, or a completion prerequisite.

Auto/Force must implement **all authorized milestones first**, perform permitted static checks and integration review, version/commit/push/PR/merge each completed value milestone, finish applicable SEO/AEO and Check/remediation without invoking acceptance tests, deploy through the existing authorized production route, verify remote main and deployment with available non-UAT evidence, and report truthful **DEVELOPMENT COMPLETE / PARTIALLY DELIVERED / BLOCKED** separately from **UAT NOT RUN**. A deployment that cannot be verified must be reported as unverified, not complete. Preserve user stories, acceptance criteria and milestone-to-story mapping as *documentation only*; no synthetic accounts, fixtures, browser journeys, runtime acceptance, or UAT spending in Auto. Do not execute local behavioral tests, Docker, or unauthorized external services.

At the end, offer `PHDK uat` as an optional **future explicit command**, without waiting for an answer as a delivery gate. Only a fresh, explicit owner invocation of `PHDK uat` authorizes UAT and its necessary Prep prerequisite, subject to normal access, safety and spending controls. Standalone `PHDK uat prep` prepares identities only when explicitly requested; it does not authorize running UAT. `PHDK uat fix` requires explicit invocation or authorization within an active explicitly initiated UAT. Prior UAT failures never reopen the completed development goal or prevent subsequent independent development.

## Canonical PHDK maintenance session gate

When the requested work changes **PHDK itself** (the canonical standards repository), read `PHDK_EVOLUTION_STANDARD.md` at session entry. Verify fresh remote `main`, `VERSION`, README and newest CHANGELOG entry; use consistent **PHDK** spelling and the defined workspace, version, coherence, manifest and versioned branch/PR delivery contract. Preserve `EXECUTION_SCOPE.md`, `VERSIONING.md`, `CHANGE_MANAGEMENT.md`, existing host controls and current user authorization. A discussion or copied brief does not activate Auto, PMO, Developer Mode or background work. In ordinary downstream-product tasks, follow applicable vendored rules without turning this maintainer guide into a new lifecycle gate.

## Phase-transition scope reconciliation

Before planning, load the verified applicable PHDK baseline under `PHDK_PLAN.md`; derive the brief, plan and task boundaries from it and the actual current request. Before publication or a later owner scope change, apply [phase-transition reconciliation](MAIN_DELIVERY_STANDARD.md#phase-transition-reconciliation). Classify restrictions by provenance and lifetime in the existing task record, preserve superseded history, and refresh affected workers. Separate owner authorization, technical permissions, costs and explicit UAT opt-in. A file update cannot grant access or defeat an executor denial, and a technical denial does not justify asking for an already-granted general approval again.

## Build and hook decision routing

When a build, packaging check or Git hook has ambiguous effects or conflicts with local verification policy, load and apply the [decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) **before executing the command, declaring BLOCKED, or requesting user input**. Inspect the actual command chain and provenance; run permitted static steps and repair only proven PHDK-managed or legacy PHDK-generated steps within the authorized task. Preserve independent owner/external/unknown controls and prepare a concrete gate-change proposal if authorization is missing. Never request a prohibited local-runtime exception or initiate UAT to satisfy the gate.

## Optional reusable-capability planning and milestone evidence

During Plan and applicable Auto work, load `PHDK_REUSE_CATALOG_STANDARD.md` when a common capability could plausibly be reused. Compare REUSE, ADAPT and BUILD; only `ACCEPTED_VERSIONED` is eligible for REUSE, and catalog presence never overrides current compatibility, security, license or maintenance evidence. Record material decisions in `REUSE_ASSESSMENT.md`; do not delay product delivery to generalize a donor prematurely. PHDK remains methodology/contracts/catalog while reusable implementations live in separately versioned packages and require a second consumer before accepted portability.

Treat agile slices as milestone-internal work. A slice does not trigger version/publication, but a coherent completed authorized milestone should not be held until the whole product is finished. Milestone evidence must distinguish IMPLEMENTED, PUBLISHED, DEPLOYED and ACCEPTED plus simulated/mocked and NOT RUN/UNVERIFIED behavior.

## Mandatory pre-implementation Design gate

For explicit `PHDK design` and applicable Auto stage **25-design**, load `PHDK_DESIGN.md` after technical/content Plan and before affected UI implementation. **Auto asks one unresolved visual question at a time, shows alternatives/previews and waits for the owner's selection and preview approval. Auto Force compares, selects, records `AGENT_SELECTED_AUTO_FORCE` with rationale and continues without a PHDK visual-approval pause.** This is the specific product-input exception to normal Auto's generic no-interview/no-stage-approval language. FORCE performs Design rather than skipping it; never invent owner approval. Reuse current owner-approved choices, preserve actual owner restrictions and brand/security decisions, and do not force a redesign for non-visual scope.

Refine existing `UI_DESIGN_SYSTEM.md` and `UX_UI_DECISIONS.md`, retain permitted reference/concept/preview assets in `docs/design/`, map shared tokens/components, update affected plan/milestone tasks and snapshot `25-design/HANDOFF.md`. Keep one canonical CSS palette source. Static concepts are not browser/runtime evidence; no local preview server, Docker, extra staging or paid-tool permission is added. Missing visual tooling follows the disclosed specification-only choice in `PHDK_DESIGN.md`: normal Auto obtains an informed owner decision, FORCE selects with visual evidence UNVERIFIED and continues. Designer Mode remains separate interface-improvement execution.

Record ordinary pending visual input as `design_choice` under `PHDK_AUTO_CONTINUITY.md`, with stage reason `DESIGN_AWAITING_OWNER`, the exact unanswered question and active mandate. Continue genuinely independent authorized work, not dependent UI. The answer resumes the same goal without another development command; an explicit switch to FORCE resolves the ordinary wait through agent selection. A real owner stop is never relabeled to waive it. Later workers receive the compact selected baseline and relevant screen/component slice, not every rejected concept.

## Mandatory consultative tenant risk management

For actual/proposed multi-tenant products load `PHDK_TENANT_RISK_STANDARD.md` at applicable Capture/Plan/Auto/UAT/Check stages. Inspect existing facts first; assess exposure, sensitivity and impact, ask one material unknown at a time, and record `TENANT_RISK_ASSESSMENT.md` with inherent/residual tier and owner decision. Enforce baseline cross-tenant isolation and sensitive-data protection, but choose shared RLS, dedicated tenant database, field encryption and independent KMS keys proportionately to actual risk, cost and regulation. Never silently provision/migrate or accept material residual risk. `PHDK_PRODUCTION_VERIFICATION.md` remains authoritative for local and production test boundaries.

## Mandatory unified administration console gate

For every administered product apply vendored `ADMIN_CONSOLE_STANDARD.md` in Capture, Plan, Auto, UAT and Check. Determine single vs multi tenancy (recommended only where justified): multi has protected platform super_admin + tenant admins; single has full-scope admin without fictitious super_admin. Demand a real Configuración console and authorized backend for users, roles, tenant lifecycle when applicable, native locale, system/debug/integrations with protected secrets, backups, audit, centrally tokenized themes and conditional Prompts/agent workflow graph. Require auditable safe Test-as-role, explicit negative authorization tests and actual permitted UI/API/persistence evidence. Bare `PHDK check` audits and requests remediation approval; `PHDK check --fix` authorizes audit and immediately fixable gaps with delivery, not unapproved tenancy conversion, credentials or live destructive changes. See `PHDK_CHECK.md`.

## Mandatory Auto continuity and Auto Force routing

`PHDK auto` and explicit `PHDK auto force` follow `PHDK_AUTO_CONTINUITY.md` with `PHDK_AUTO.md`. Keep the current user mandate, scope, target, restrictions and next executable action in `docs/phdk/lifecycle/<run-id>/AUTO_STATE.json`; reload with current user instructions after compaction and before a terminal response. This is evidence of an active conversation's authorization, not persistent permission or a trigger to resume old work. Missing/malformed state requires internal reconstruction, never another approval or a paperwork-only stop.

In AUTO FORCE, human reviews/sign-offs imposed only by PHDK are `NON_BLOCKING_BY_MODE` from entry. Do not investigate whether they block, search for reviewers, or query review/protection configuration as a precondition. Perform assistant diff review and applicable permitted checks, then normal branch push → PR → merge → remote-main verification. Existing controls remain binding; apply the [hook decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) before marking an unresolved verification conflict BLOCKED. Never bypass a control. Never invent human review or treat an unexecuted test as passed. FORCE chooses ordinary visual directions before implementation rather than waiting for owner selection.

At AUTO FORCE start/resume, every progress update, after partial delivery and before any question/blocker, apply the short rule refresh and mandatory reminder in `PHDK_AUTO_CONTINUITY.md` and `PHDK_COMMUNICATION_STANDARD.md`. Reconcile inherited blockers and discard obsolete assistant interpretations; preserve real user exclusions and host controls. State the canonical reminder, find a concrete solution and execute the next authorized action. For missing routine definitions, propose behavior, reasonable defaults and configurable options within agreed scope, then implement; do not ask the owner to design everything or recommend leaving accepted gaps out. An indispensable new sensitive/scope decision gets a concrete recommendation, not a blank request.

On an actual tool/hook/GitHub rejection, report it, diagnose the cause, repair within scope, revalidate and retry the affected push/PR/merge; retain the mandate and continue independent work. Never use force-push, bypass flags, disabled controls, alternate credentials/transports or provider settings to evade rejection. A real remaining control/access/scope obstacle blocks only the affected action. End Auto progress with the truthful mandate/next-action capsule and execute eligible work in the same turn. Normal Auto's unanswered Design choice is legitimate product input: preserve the mandate and ask that one question rather than falsely claiming dependent UI work continues. Editing these standards activates neither mode.

## Mandatory delivery-autonomy and personality bootstrap

On each explicit PHDK entry, use vendored `PHDK_COMMUNICATION_STANDARD.md` as the canonical response/personality contract and check the active tool-native managed entrypoint. Do not infer a different already-open session has reloaded after an update. For scoped implementation deliverables, continue normal versioned branch/PR/merge and remote verification without universal human sign-off; keep actual independent/server reviews, safety decisions, hooks and current owner restrictions. Never confuse source merge, GitHub release and verified production deployment. See `MAIN_DELIVERY_STANDARD.md`.

## Mandatory PHDK communication personality

For every substantive PHDK-facing update, lifecycle handoff and closure, apply vendored `PHDK_COMMUNICATION_STANDARD.md`. Present PHDK version (or unverified), active mode/stage, objective, verifiable results and pending commitments, git/main/deploy state, and a copy-paste-ready `SIGUIENTE PASO`. In Auto/AUTO FORCE include actual mandate status and next action; continue eligible work rather than yield for ceremonial approval. Distinguish actual normal Auto Design input from a permission-to-continue question. Own the outcome end to end within existing permissions. Suppress repeat optional promotional messages after one relevant mention, but preserve mandatory notices and real consent/review/safety controls. A subagent's task is not integrated delivery. End every terminal PHDK response with a verified artifact/product/PR/commit URL and what it shows, or explicitly state the link is unverified/unavailable.

## Mandatory synthetic UAT authentication and JWT boundary

For explicitly authorized authenticated UAT/UAT Fix, read vendored `JWT_STANDARD.md`, `UAT_JOURNEY_STANDARD.md`, `UAT_BROWSER_READINESS_STANDARD.md` and governing `PHDK_PRODUCTION_VERIFICATION.md`. Discover actual auth provider and tenant/role model; provision run-owned Company Co identities and legitimate scoped sessions without human passwords/bearer secrets. JWT means JSON Web Token, not UAT; do not require it for cookie/OAuth apps. Never forge credentials or expose an authentication backdoor. Verify elevated access, audited Test as, direct-login roles, negative permissions and tenant boundaries only on the permitted deployed candidate; record redacted evidence, expiry/revocation and cleanup or a precise BLOCKED gap.

## Mandatory UAT Prep synthetic account implementation

Standalone `PHDK uat prep` and necessary Prep within an explicitly initiated `PHDK uat` follow vendored `PHDK_UAT_PREP.md` and the production-first verification policy: implement missing idempotent run-owned Company Co identities, legitimate authentication, role/tenant contexts, audit-safe Test as and cleanup, then write role/fixture/auth/prep evidence. Reconcile and deliver an Integration candidate changed by Prep before runtime acceptance. Browser/headless work belongs only to subsequent scoped UAT/UAT Fix; no local runtime tests, Docker, new environment or human passwords/tokens.

## Mandatory Company Co synthetic UAT fixture

During explicitly authorized PHDK UAT/UAT Fix, read vendored `USE_COMPANY_CO_INFO_FOR_DEMOS.md` and `UAT_JOURNEY_STANDARD.md`. Prefer Company Co for reproducible role journeys; adapt to the real model, provision safe synthetic identities, verify roles and applicable elevated switching, and record evidence. Emails at `@tujuisasa.com` require expressly authorized controlled delivery, never unattended bulk sends.

## Mandatory browser readiness gate

At explicitly authorized UAT and UAT Fix entry follow `UAT_BROWSER_READINESS_STANDARD.md`. Confirm phase exception and actual connected browser separately with scoped evidence. Record cost disposition; never improvise a budget or paid API/service to fix unavailable access, and run independent permitted cases while connection is blocked.

## Mandatory UAT journey and next-action gate

Apply `UAT_JOURNEY_STANDARD.md` for explicit `PHDK uat`, `PHDK uat fix` and authorized retests within that active UAT scope. Auto and Designer do not themselves activate acceptance. Require role inventory, access verification, safe synthetic identities, audited elevated profile switching, intent-traceable stories by persona, executable user journeys, and UX/CRUD and permission evidence. Product repair/retest requires explicit `PHDK uat fix` or repair authorization within the active explicitly initiated UAT; bare UAT prepares readiness, validates and reports. Every user-facing stage or blocker response ends with concise `SIGUIENTE PASO`: completed work, exact PHDK action or single required owner action, and precise resume cue. Continue autonomously where permitted; never request MFA secrets in chat or claim tests against an unverified deployment.

# AGENTS.md

## Purpose and execution boundary

This is the entry point for an assistant working on a PHDK repository. It is an instruction document, not an executable agent, scheduler, or permission to start work.

Read the current user request and `EXECUTION_SCOPE.md`, then the project's `TASK.md`/`STATUS.md`. Scope is interactive-only. Normally one assistant completes the deliverable; `PHDK auto` makes development continuous under `PHDK_AUTO.md`, with the explicit Design decision policy. Bounded in-session subagent delegation follows `PHDK_INTELLIGENT_EXECUTION.md` in any supported mode. PMO alone governs portfolio-level orchestration. No background/post-conversation agents.

Current owner pause/stop instructions remain effective within scope. Re-read them before edits and git writes and compare with the latest instruction. The owner can replace an older documentary exception; a file cannot veto that request. A specific intervention does not restart unrelated earlier work. Old tasks, alerts, failed checks, version mismatches, and skill installation never authorize work.

Complete necessary steps of the current deliverable, including authorized delivery, then report and stop. In Auto use `PHDK_AUTO_CONTINUITY.md` before a terminal response to continue eligible actions and reconstruct missing records internally. Do not choose another backlog task. Status/link questions and assistant task summaries do not cancel the unfinished active request; preserve real owner stops and leave unrelated/post-conversation work inactive.

## Git and automation boundary

`PHDK check` and Auto's final Check apply `PHDK_AUTOMATION_HYGIENE.md`: source scan plus read-only GitHub workflow active/runs/check state and Railway deploy/Wait for CI/cron/restart evidence where connected. Distinguish legacy PHDK schedules/agents from justified CI and normal GitHub→Railway autodeploy. No blanket disabling/provider writes; incomplete remote access is UNVERIFIED.

- A current implementation/fix/update request includes scoped branch, version, permitted checks, version-prefixed commit, push, PR, required review, merge, and verified remote `main` under `MAIN_DELIVERY_STANDARD.md`. Do not ask again for delivery steps. Honor narrower read/audit/plan/local/branch/PR-only requests, explicit targets and bare `PHDK upgrade` limits.
- Normal delivery requires assistant diff review and applicable checks. Sensitive behavior/policy decisions need owner approval; a well-defined current request or clear "push to main", "merge", or "aprobado" for the identified change may supply it. Do not invent a GitHub review event or human-diff-opening requirement. Preserve formal/named/independent reviews actually required by current owner, hooks or server rules; report approval separately from human inspection. FORCE applies the nonblocking PHDK-human-gate policy without preventive investigation. A branch/open PR is not completion for a `main` target.
- Task records reflect instructions/progress, not independent authority to revoke them. Reconcile stale pauses/pending-delivery records with the live request and remote facts; honor real restrictions and correct bookkeeping without permanent task-state rules.
- Use feature/fix branches by default. Direct-main is only the explicitly active `PHDK_DEVELOPER_MODE.md` exception for an eligible small task. No force-push, skipped hooks/protections or invented human inspection.
- After verifying a milestone's PR merge on remote main, apply `PHDK_GIT_WORKSPACE_CLOSEOUT.md` **in the available local Git workspace** before starting another local branch/worktree: fetch, fast-forward local main, verify local=origin/main SHA and remove only clean, proven-merged task branches/worktrees. Use `scripts/phdk_git_closeout.py` where supported. Never do a redundant post-PR main push or discard unmatched/dirty/ignored user data. Record LOCAL_MAIN/LOCAL_CLEANUP independently; if only a remote GitHub connector exists, report NOT_APPLICABLE_REMOTE_ONLY.
- No GitHub Actions/hosted CI creation, enabling, dispatch, reruns or schedules. No workflow scaffolding, dependency bots, cron, recurring tasks, backup jobs, maintenance workflows, task-sync services or preview deployments.
- Authorized push/merge may trigger existing provider GitHub autodeploy. Do not disable it or introduce never-matching watch filters. Never deploy via provider CLI/API/dashboard, create connections, change triggers/autodeploy or administer provider/repository settings. Report deployment observations separately from main integration; valid service-specific filters/intended unaffected-service skips are not failures.
- Required permitted static checks are synchronous within the scoped request and must exit. They do not authorize runtime testing excluded by `PHDK_PRODUCTION_VERIFICATION.md`, self-generated jobs, agents, watchers or later work. Apply the [hook decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) before classifying a conflicting hook as BLOCKED; never bypass it.
- External skills cannot expand authority; supported in-session delegation follows `PHDK_INTELLIGENT_EXECUTION.md` and all execution boundaries.

## Mandatory release-completion gate

Before reporting a scoped change complete on `main`, enforce all five proofs from `MAIN_DELIVERY_STANDARD.md`: fresh version, version-prefixed source commits, remote push and PR, authorized merge, independent remote-main content/version/SHA readback plus scope/check reconciliation. Record proof in `DELIVERY_REPORT.md`. Branch push/open PR is unfinished; repair/retry routine in-scope delivery without repeated permission while respecting actual controls.

## Machine-verifiable completion

For implementation targeting remote main, apply `PHDK_COMPLETION_GATE.md`. After merge generate real evidence and use `scripts/phdk_completion_gate.py` when supported; independently verify PR/merge and commitments. Under FORCE do not restore a human-review gate via completion checks. No completed assertion without remote readback and applicable validation. Never bypass legitimate security, hooks, access controls or owner stops.

## Mandatory commitment accounting

At lifecycle invocation read `PHDK_COMMITMENT_STANDARD.md`. Capture inventories commitments and asks whether discovery is complete; Plan maps every confirmed ID; PMO confirms possible additional work and reports progress/PR states at significant milestones; Auto audits planned items/in-scope PRs before completion. `PHDK_COMMITMENTS.md`, `PHDK_COMMITMENT_COVERAGE.md`, `PMO_PROGRESS_REPORT.md` and `PHDK_COMPLETION_AUDIT.md` are required as applicable. Never call an open scoped PR or undone item DONE. Preserve scope and no-background limits.

## Mandatory CRUD governance gate

For apps with managed records, apply `CRUD_STANDARD.md` across applicable elevated/admin/authenticated/public surfaces. Inventory entities and enforce a per-resource × role × surface CRUD matrix. Require actionable admin details and server-side permission evidence; accept documented immutable/read-only exceptions rather than unsafe delete controls. Capture, Plan, UAT and Check reconcile `CRUD_MATRIX.md` with evidence/handoffs.

## Mandatory debug widget gate

For applicable app-style products follow `DEBUG_DIAGNOSTICS_STANDARD.md`: one reusable always-visible version → clipboard → trash icon-only row on public home, login, app and admin, including anonymous visitors and debug OFF. Only `vX.Y.Z` visible, no SHA/date; 28×28px visible buttons, 14px icons, 12px version text, 4px gap, no helper/success text; successful copy and cache clearing individually show a temporary green check and revert. Copy verbose sanitized diagnostics; clear only permitted caches/session state. Auto inspects implementation/test source, repairs in-scope omissions and reconciles Check. No visual/runtime claim without permitted evidence.

## Mandatory UX/UI product-design gate

For user-facing scope follow `PHDK_UX_UI.md` and `PHDK_DESIGN.md`: derive UX journeys and draft constraints in Plan, select the mode-correct visual baseline in Design before affected UI coding, then audit/remediate evidenced UX/UI and baseline-fidelity issues in UAT. Apply P0/P1 blockers and preserve correct brownfield workflows. Concepts/owner approval are not runtime proof; browser evidence remains scoped to UAT/UAT Fix.

## Design system source of truth

For applicable React/Next.js work follow `PHDK_DESIGN_SYSTEM.md`: shared shadcn-compatible components, Radix composite primitives, centralized Tailwind semantic tokens, Motion presets, Lucide icons and coherent light/dark/corporate palettes. Use documented en/es/pt defaults and project exceptions. No page-specific duplicated widgets/themes. Verify installed versions before changing dependencies; greenfield Design may specify planned compatible dependencies without pretending they are installed or requiring application construction before visual selection. Preserve behavior.

## Mandatory theme token and template editor gate

For UI products read `PHDK_THEME_STANDARD.md` with `PHDK_DESIGN_SYSTEM.md`. Require one semantic CSS palette, light/dark/corporate parity, applicable authorized platform-admin Configuración → Edición de templates, persisted edits and corporate visibility. Design maps the selected style to that source; Designer detects/repairs hardcoded values; Check records file:line findings and functional evidence. The static theme audit is not runtime compliance. Preserve permissions/tenancy and audit/remediation separation.

## Designer Mode command

On explicit `PHDK designer mode` or `PHDK modo designer`, run `PHDK_DESIGN_SYSTEM.md` readiness, produce `DESIGN_SYSTEM_READINESS.md`, then follow `PHDK_DESIGNER_MODE.md`: inspect existing UI, establish baseline, choose a product-specific direction, implement improvements and run permitted static checks; verify rendered behavior only after explicit `PHDK uat`. Deliver code, not just review; preserve functionality, debug widget and normal delivery controls. Consume valid selected Design decisions; material changes under a parent Auto/Force goal follow that parent's choice policy. Standalone Designer keeps its explicit autonomous redesign scope; it is not activated by `PHDK design`, and a Design package alone does not complete Designer Mode.

## Designer Mode delivery gate

Never report Designer Mode COMPLETE for local-only edits, formatting-only validation or an undelivered branch. Follow its closure proof, repair safe permitted pnpm/hook problems before marking BLOCKED, preserve hooks and independently verify merged remote target.

## SEO and AEO/GEO lifecycle gates

After Integration before Check, execute `PHDK_SEO.md` then `PHDK_AEO_GEO.md` for applicable public discoverability. Preserve separate handoffs, reports, verified source fixes and explicit N/A for private-only routes. UAT is deferred in Auto; execute acceptance regressions only within a separately explicit UAT scope. Neither broadens browser/production authority or permits fabricated rankings/citations.

## PHDK commands

Before commands follow `PHDK_PREFLIGHT.md` and `PHDK_LIFECYCLE.md`: verify installation/version/manifest/managed rules and actual relevant capabilities from `SKILLS_REGISTRY.md`. Use available relevant capabilities unless disabled; registry text is not installation evidence. Inside Auto reuse Preflight and refresh only newly relevant capabilities. At transitions verify inputs and retain canonical outputs/historical snapshots.

On explicit `PHDK plan`, follow `PHDK_PLAN.md` and `PHDK_PROJECT_MANAGEMENT_STANDARD.md`: consume Capture, inspect current architecture, define target/convergence and executable tasks grouped into value milestones with `MILESTONE_PLAN.md`. Supply draft UI constraints and content/technical architecture to Design; do not pretend final visuals are already approved. Preserve valid brownfield architecture.

On explicit `PHDK design`, follow the Design gate above and `PHDK_DESIGN.md`. Resolve identity, composition, graphic system and contextual experience with references, meaningful alternatives and previews. Standalone/Auto asks one choice at a time; Force chooses/rationalizes/records and continues. The output is a durable design package, not automatically the complete app.

On explicit `PHDK PMO`, follow `PHDK_PMO.md` and project-management standard: execute the milestone roadmap and coordinate confirmed workstreams, dependencies, seven-domain material controls/risks. Require the selected Design baseline for dependent UI work and give workers relevant slices. Bounded delegation follows `PHDK_INTELLIGENT_EXECUTION.md`; PMO alone governs portfolio orchestration and workers cannot delegate. Under Auto/Force, integrate/version-deliver each completed value milestone to verified main, then final cross-milestone integration before Check/delivery. A later explicit UAT uses the delivered candidate. Merely ending Design is not a release boundary.

On explicit `PHDK capture`, investigate repo/conversation first, reconstruct or elicit intent/ethos/requirements and canonical package, then ask only missing material information under `PHDK_CAPTURE.md`. State whether questions are needed; when resolved, list/link artifacts. Capture may span turns but does not initiate product implementation.

On explicit `PHDK check`, follow `PHDK_CHECK.md`: audit applicable standards and actual evidence, produce a prioritized report, ask once before executing AUTO-FIXABLE/FIXABLE WITH VALIDATION gaps. Audit is read-only except its report. Include Design decision provenance, actual assets/limitations, stage25 handoff, task/component mappings and fidelity evidence under `PHDK_DESIGN.md`. Valid FORCE agent selection is not missing human approval. Explicit `check --fix` and active Auto retain their defined remediation authorization.

On explicit `PHDK uat prep`, implement safe run-owned synthetic accounts, provisioning and legitimate sessions under `PHDK_UAT_PREP.md` and production-first policy. Deliver via normal versioned PR/merge and verify only permitted deployed role/tenant behavior. Do not activate UAT/browser. Necessary Prep may precede acceptance within an explicitly initiated UAT; Auto/Force never start it.

On explicit `PHDK uat fix`, read report/cases, convert FAILs to defects and BLOCKED/MANUAL to concrete action plans, repair in-scope failures, rerun affected permitted deployed checks and update evidence without per-defect approvals. When no automatic fix remains, give who/what/where/how/when/evidence/next-command guidance. Preserve actual decisions/access/provider boundaries.

On explicit `PHDK uat`, run necessary Prep under that same authorization, identify intent, derive aligned stories/stable cases and `UAT_CASES.md`, execute permitted evidence without per-case approvals, and produce `UAT_REPORT.md`. Compare actual UI to selected Design baseline where applicable. Browser/headless only in scoped UAT/UAT Fix on the existing versioned production candidate under `PHDK_PRODUCTION_VERIFICATION.md`, with run-owned synthetic fixtures and verified cleanup. Real-data/destructive/provider operations remain excluded. Unexecuted behavioral cases are BLOCKED/MANUAL, never PASS.

On explicit `PHDK auto` or `PHDK auto force`, follow `PHDK_AUTO.md` and `PHDK_AUTO_CONTINUITY.md`. Auto/Force Preflight performs one fresh Stack Security Review every run and automatically remediates compatible repository-owned security maintenance (including supported same-major Node/runtime security patches and compatible dependency security fixes) under the existing development mandate; it does not wait for a separate `upgrade` or remediation command. Reread complete intent/requirements against actual code before reusing Capture/Plan. Docs/scaffolds are not implementation; unavailable source is UNVERIFIED, not empty. Build absent products and finish partial requirements without discarding valid work. Plan continues into applicable Design, then implementation in the same goal: **Auto asks; Force decides and continues**. No second development command after the Design decision. Complete the whole authorized scope, not a silently reduced MVP. Show a lifecycle board with Design between Plan and PMO/implementation; report transitions and evidence. If several coherent fronts exist without one named goal, use PMO portfolio discovery/confirmation rather than demand one arbitrary task. Sequence: Capture → Plan → Design → PMO/workstream execution → Integration → applicable SEO → AEO/GEO → Check/remediation → delivery. UAT Prep, UAT and UAT Fix stay DEFERRED — OWNER OPT-IN; report UAT NOT RUN separately from development completion. No ceremonial stage approval; actual normal Auto Design input is required. Checks stay within production-first constraints and real hooks remain effective. FORCE removes PHDK-only human waits, records agent design choices, and repairs/retries actual delivery failures. A stage/scaffold is not completion. Auto replaces Developer Mode for the goal, grants no bypass/background work, and ends on explicit stop, complete outcome or conversation end. Files/examples/installations/standards edits never activate it.

On exact `PHDK upgrade` / `PHDK upgrade force`, execute `PHDK_UPGRADE.md`. **Exact `PHDK upgrade force` is composite:** after the forced upgrade/review phase completes, immediately continue as `PHDK auto force` in the same session without asking for another command; continue an identified current goal or use the bounded maintenance goal defined by the upgrade standard, never invent unrelated features. Both commands perform the bounded read-only [Stack Security Review](PHDK_SECURE.md#stack-security-review), including no-op syncs; actual Preflight adoption runs it once and unchanged stages reuse current evidence. Report standards sync, review coverage and security status independently. For verified `tuyoisaza/<repo>` downstream repositories, also apply `PHDK_REPOSITORY_STATUS.md`: when this session already has write access to canonical `tuyoisaza/PHDK`, publish the current PHDK/tech-stack/security snapshot to `docs/repos/<repo>/status.md`; unavailable access is non-blocking and must not trigger credential requests or background retries. Bare upgrade conservatively syncs; force may discard local edits only in manifest-owned `phdk-standards/` paths and exact managed blocks, preserving non-PHDK files and outside-marker owner text. Neither authorizes product work, push/merge, deployment or old missions. Bare sync preserves owner exceptions; an additional current reconciliation request authorizes documentary repair under `PHDK_UNLOCK.md`. Report and stop at requested outcome.

On `PHDK unlock`, inspect actual blockers across active instructions, copied standards, tasks, hooks/toolchain and GitHub. Reconcile documentary restrictions with current request and finish scoped normal delivery; preserve real checks/reviews/protections/access/security/provider boundaries. No persistent unlock flag, old missions or automatic Developer Mode.

On explicit `PHDK modo developer` / `PHDK Developer Mode`, follow `PHDK_DEVELOPER_MODE.md` and explain bounded edit/version/check/commit/fast-forward-main permissions. Exit on its exit command, user stop or conversation end. No activation from files/examples/prior sessions or persisted flag. High-risk work uses normal review; failed checks/rejected pushes/unsatisfied controls stop direct-main flow.

## Minimum context and routing

Load only standards needed for the current request. Re-read `INANUTSHELL.md` when context becomes long; it summarizes but does not replace detailed rules. `ENFORCEMENT.md` describes local controls, not authority for agents/cloud automation. `PHDK_INTELLIGENT_EXECUTION.md` governs progressive loading.

| Current task | Relevant standards |
|---|---|
| Discovery, ethos, requirements | `PHDK_CAPTURE.md`, `INTENT_CAPTURE_STANDARD.md`, `SPEC_INTERVIEW_PROMPT.md` |
| Solution/repository/UX architecture and planning | `PHDK_PLAN.md`, `technical_stack.md`, `design_rules.md`, `DEVSECOPS.md` |
| Pre-implementation visual direction, references, style guide, previews | `PHDK_DESIGN.md`, `PHDK_UX_UI.md`, selected project design artifacts; component/theme standards only as needed |
| Planning, scope, task state | `AI_DEVELOPER_OPERATING_MODEL.md`, `AGILE_SLICE_WORKFLOW.md`, `TASK_TRACKING_STANDARD.md`; intent standard when needed |
| Branching, organization, dependencies | `DEVELOPMENT_RULES.md` |
| UI/accessibility/responsive implementation | `DESIGN_RULES.md`, `PHDK_UX_UI.md`, selected Design baseline/component slice |
| Stack, architecture, data, deployment source | `TECHNICAL_STACK.md` |
| AI providers/prompts/admin/consumption | `AI_ADMIN_STANDARD.md`, `TECHNICAL_STACK.md`, `DEVSECOPS.md` |
| Auth, secrets, security/privacy/cost | `DEVSECOPS.md`; tenant risk standard when applicable |
| Versions/commits/changelog | `VERSIONING.md` |
| Remote-main delivery/conflicts/evidence | `MAIN_DELIVERY_STANDARD.md` |
| Lifecycle inputs/outputs/handoffs | `PHDK_LIFECYCLE.md` |
| Portfolio/workstreams/delegation/integration | `PHDK_PMO.md`, `PHDK_INTELLIGENT_EXECUTION.md` |
| Whole-goal Auto, mode-specific Design, continuity | `PHDK_AUTO.md`, `PHDK_AUTO_CONTINUITY.md` |
| FORCE human-gate policy, recovery/retry | `PHDK_AUTO_CONTINUITY.md` |
| Documentary blockers/reconciliation | `PHDK_UNLOCK.md` |
| Developer Mode/eligible direct-main work | `PHDK_DEVELOPER_MODE.md` |
| Standards audit/remediation | `PHDK_CHECK.md` and affected standards, including Design when relevant |
| UAT/cases/reports | `UAT_STANDARD.md`, `PHDK_PRODUCTION_VERIFICATION.md`, `TESTING_STANDARD.md` |
| Static verification and runtime boundaries | `PHDK_PRODUCTION_VERIFICATION.md`, `VERIFICATION_LOOP.md`, `TESTING_STANDARD.md` |
| Diagnostics/provider metadata/log reads | `DEBUG_DIAGNOSTICS_STANDARD.md`, `EXECUTION_SCOPE.md` bounded diagnostics |
| Build/packaging ambiguity and hook conflicts | [Hook decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure), `PHDK_PRODUCTION_VERIFICATION.md`, `ENFORCEMENT.md` |

Read `ONBOARDING_AI_DEVELOPER.md` for orientation when needed. Do not preload every standard or make missing context an autonomous discovery mission.

## Core implementation rules

- Work only on current requested code/documentation scope. Do not upgrade dependencies, replace architecture or add infrastructure merely because a checklist mentions it.
- No fake dashboards, KPIs, metrics or demo data presented as real.
- User-facing features need real routes and meaningful empty/loading/error/success states.
- Enforce RBAC/validation server-side; hidden controls are not authorization.
- Use configured i18n for user-facing strings.
- Use structured redacted logs at important boundaries.
- Keep source files below 600 lines, preferably below 300; business logic out of pages, features organized by responsibility.
- Author reviewed migrations for schema changes; execution follows actual authorization and production-first safety, never an implicit real-data mutation.
- Never weaken auth/validation/privacy/cost controls to pass a check.
- Destructive repository changes and material auth/payment/tenant changes need explicit task scope.
- Implement the selected Design baseline through shared components/tokens. Material direction changes reopen affected choices under the current mode; routine fidelity corrections do not require another style interview.

## Product and architecture defaults

Public marketing/content sites do not acquire login, dashboards, user management or private app flows unless requirements call for them.

The standard monorepo is `apps/web` (Next.js), `apps/api` (NestJS + Fastify), optional `apps/mobile`, and shared `packages/*`. Existing web/API builds target repository root; this describes source configuration, not Railway administration permission.

Authentication defaults to custom Google OAuth 2.0. Managed auth exceptions need a documented decision. For owner-supplied OAuth variables follow `TECHNICAL_STACK.md` — **Required Railway Variables handoff**: name service/environment, exact consumed `KEY=value` blocks, real public callback/origin and safe placeholders; request secret entry in the provider, never chat. Role architecture follows applicable administration/tenancy standards, enforced server-side.

App-style products implement specified navigation, version display, real authentication, authorized administration, debug/diagnostic contracts, safe logging and i18n. Required routes come from product and relevant standards, not invented app features for public-only sites.

Explicitly required LLM features use `packages/ai`, provider-agnostic configuration, schema validation, injection defenses, measured usage, caps, timeouts, retry limits and kill switches. A standard's mention is not permission for paid verification.

## Verification and completion

Review actual source/diff and run only permitted synchronous static/format/lint/typecheck/safe-build checks. `PHDK_PRODUCTION_VERIFICATION.md` excludes local behavioral/in-process tests, Docker, servers and extra staging/databases; actual runtime acceptance is scoped to the existing deployed candidate and safely owned synthetic data with verified cleanup. Actual mandatory controls remain effective; resolve verification conflicts through the [hook decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) before reporting unresolved gates BLOCKED. Never bypass a control. Documentation-only changes need source/diff/reference and policy-scenario review. Static source analysis is not behavioral proof.

No browser/headless/application screenshots outside scoped UAT/UAT Fix. Static Design artifact authoring/viewing with available permitted tools adds no browser/app execution permission. No unauthorized live probes, real-data use or paid verification. A current request such as "verifica Railway" authorizes bounded reads of existing provider deployment/source/branch/non-secret metadata and logs through authorized connectors under `EXECUTION_SCOPE.md`; no second authorization phrase or unlock needed. No streams/polling, secrets, settings writes, new access or deployment. Provider observations do not prove UI behavior/recovery.

Before completion confirm outcome, applicable checks, owner controls and target. For main delivery verify remote content/version/SHA rather than stale checkboxes or a redundant post-merge bump. Report deployment separately. Do not claim external agents were stopped, credentials revoked, billing corrected or server protection enabled because docs/hooks changed. Record proposed follow-ups as inactive context; after the authorized outcome/delivery, stop.

## Widget functionality gate

At Auto entry inspect source and create `DEBUG_WIDGET_READINESS.md` before trusting visual controls. Widget top-left below product name; clipboard copies real sanitized events/errors/routes/version; trash clears only supported origin-scoped caches/storage/app cookies and server logout/session where needed. Animated checkmarks without awaited successful effects are FAIL. Preserve public-safe reporting and accurately report unsupported browser controls.

## Production-first verification override (v2.58.0)

**Mandatory:** Apply [PHDK_PRODUCTION_VERIFICATION.md](PHDK_PRODUCTION_VERIFICATION.md). Production-only UAT supersedes earlier local unit/in-process/runtime tests, staging-only identity and blanket production-test prohibitions. Local operations are static analysis/lint/typecheck/safe builds; Docker, local runtime tests and separate staging/databases are prohibited. UAT uses the existing versioned production deployment/database, run-owned synthetic identities/records, audit, automatic cleanup and verified revocation on success/failure/interruption. Never touch real data or bypass hooks; apply the [hook decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) before reporting an unresolved verification gate BLOCKED. Design creates no new execution exception.


## Hook compatibility (v2.61.0)

Apply the [hook decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) before executing an ambiguous build/packaging/hook command, declaring its conflict BLOCKED, or asking the owner. Inspect the command chain and provenance, automatically repair only proven PHDK-owned incompatibilities within authorized remediation, and preserve independent security/version/branch/commit gates. Owner-owned, external and unknown controls retain their authorization boundary; prepare a concrete proposal for any unresolved gate. Never request a prohibited local-runtime exception, execute excluded tests, use --no-verify or start UAT to satisfy a hook.
