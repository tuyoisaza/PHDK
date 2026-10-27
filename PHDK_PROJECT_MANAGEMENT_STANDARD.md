## v2.62.0 — Explicit-only UAT authorization (overrides legacy automatic-stage wording)

**Binding rule:** `PHDK auto` and `PHDK auto force` MUST NOT invoke, enter, provision, seed, or run UAT Prep (45), UAT (50), or UAT Fix (60), even after milestones, deployment, Check, or a failed prior UAT. Neither FORCE nor a generic full-lifecycle instruction grants UAT authorization. These stages are **DEFERRED — OWNER OPT-IN**, not BLOCKED, FAILED, or a completion prerequisite. This rule takes precedence over any older automatic UAT transitions in this file.

Auto/Force must implement **all authorized milestones first**, perform permitted static checks and integration review, version/commit/push/PR/merge each completed value milestone, finish applicable SEO/AEO and Check/remediation without invoking acceptance tests, deploy through the existing authorized production route, verify remote main and deployment with available non-UAT evidence, and report truthful **DEVELOPMENT COMPLETE / PARTIALLY DELIVERED / BLOCKED** separately from **UAT NOT RUN**. A deployment that cannot be verified must be reported as unverified, not complete. Preserve user stories, acceptance criteria and milestone-to-story mapping as *documentation only*; no synthetic accounts, fixtures, browser journeys, runtime acceptance, or UAT spending in Auto. Do not execute local behavioral tests, Docker, or unauthorized external services.

At the end, offer `PHDK uat` as an optional **future explicit command**, without waiting for an answer as a delivery gate. Only a fresh, explicit owner invocation of `PHDK uat` authorizes UAT and its necessary Prep prerequisite, subject to normal access, safety and spending controls. Standalone `PHDK uat prep` prepares identities only when explicitly requested; it does not authorize running UAT. `PHDK uat fix` requires explicit invocation or authorization within an active explicitly initiated UAT. Prior UAT failures never reopen the completed development goal or prevent subsequent independent development.

# PHDK Project Management Standard

## Tenant-risk register input

For multi-tenant initiatives, `PHDK_TENANT_RISK_STANDARD.md` and `TENANT_RISK_ASSESSMENT.md` supply a concise risk register input: inherent/residual score and tier, evidence, risk owner, controls, cost/operability, pending material decisions and review triggers. Map approved mitigations into milestones. Assessment is not authorization to purchase, provision or migrate infrastructure; preserve `PHDK_PRODUCTION_VERIFICATION.md` limits.


## Purpose and authority

This standard defines the project-management operating model used by PHDK Plan, PMO, Auto and UAT. It adapts the owner's PMI/PMBOK 8 knowledge base into a software-delivery contract focused on value, risk, acceptance evidence and proportional governance.

It is an operational interpretation for PHDK, not a transcription of PMI publications, a certification claim, or a replacement for an organization's legal, financial, security or professional governance. Current owner instructions, `EXECUTION_SCOPE.md`, product requirements and actual repository/provider controls remain authoritative.

## Core operating principles

PHDK project management is outcome-driven:

- **System view** — consider product, technology, operations, people, dependencies and downstream effects together.
- **Value** — every milestone and workstream must trace to a user/business outcome, requirement, risk reduction or approved enabling capability.
- **Built-in quality** — acceptance criteria and evidence are defined before execution and checked continuously, not invented at the end.
- **Accountability** — identify the responsible execution owner and the authority for material decisions; an AI recommendation is not a fabricated human approval.
- **Sustainability** — consider maintainability, operating cost, resource use and long-term support proportionally to project impact.
- **Empowered execution** — workers may make routine reversible implementation choices inside their mandate while material scope/risk decisions follow the applicable governance boundary.

Tailor ceremony to size, uncertainty, criticality and regulation. A small low-risk project may keep these controls in compact existing artifacts; a large, sensitive or regulated project may require fuller records.

## Delivery approach classification

During Plan classify the current goal as:

- **Predictive** — scope and acceptance criteria are stable enough for a baseline plan.
- **Adaptive** — material uncertainty or changing requirements justify incremental milestones and explicit replanning.
- **Hybrid** — stable components use predictive planning while exploratory components use adaptive validation.

The classification is a planning aid, not a reason to stop execution. Record assumptions and change the approach when evidence warrants it.

## Seven PMO control domains

PMO continuously considers these domains and records only material status, variance, decision or risk:

1. **Governance** — mandate, decision rights, escalation, continuation criteria and material approvals.
2. **Scope** — outcomes, requirements, exclusions, acceptance criteria and unauthorized scope growth.
3. **Schedule** — milestone sequencing, dependencies, capacity constraints and committed versus estimated dates when dates actually exist.
4. **Finance** — known budget/spend constraints, metered-service exposure and material cost variance; never invent budgets or precision.
5. **Stakeholders** — users, owner/approvers, affected groups, communication and acceptance needs.
6. **Resources** — skills, worker/tool availability, shared-file ownership and bottlenecks.
7. **Risk** — threats/opportunities with cause, effect, response, owner and review trigger proportional to significance.

Every material recommendation or change should identify the affected domains when that improves the decision.

## Five operating focus areas

These are concurrent/revisitable focuses, not rigid phases:

- **Initiation** — clarify problem, objective, expected value, scope boundary and authority.
- **Planning** — define architecture, milestones, dependencies, acceptance, quality and principal risks.
- **Execution** — coordinate workstreams, resources and dependencies to produce working outcomes.
- **Monitoring and control** — compare actual progress/evidence with the approved milestone plan; evaluate material variance and changes.
- **Closure** — verify the authorized development evidence, delivery state, operational handoff/residual ownership and lessons/decisions needed before declaring the development goal complete. Record optional runtime acceptance separately as `UAT NOT RUN` until explicitly initiated.

## Milestone contract

A **milestone is a coherent, independently valuable and verifiable product increment**, not a lifecycle stage, arbitrary time box, worker checkpoint or folder boundary. Plan must create `MILESTONE_PLAN.md` and map each in-scope requirement/workstream to one or more milestone IDs such as `MS-001`.

Each milestone records:

- ID and value/outcome;
- **user capability** gained and representative **user journey** that becomes possible;
- linked intent, commitments and requirements;
- included workstreams/tasks, in-scope behavior and explicit exclusions;
- dependencies and ordering;
- affected actors/surfaces;
- material domain impacts and risks;
- acceptance criteria and required permitted technical evidence;
- evidence ledger: what is observed working, what is simulated/mocked/fixture-only, and what is `NOT RUN` / `UNVERIFIED`;
- delivery target and the current authorization/restriction reference that applies to publication;
- expected SemVer impact (`patch`, `minor`, `major`) as a planning expectation, not a pre-reserved version number;
- UAT intent: documented user goal(s) for optional acceptance after explicit `PHDK uat`; planning this coverage does not authorize execution;
- next milestone (or terminal goal) and dependency handoff;
- distinct state/evidence for **IMPLEMENTED**, **PUBLISHED** to the requested source target, **DEPLOYED**, and **ACCEPTED**; none implies the next;
- after delivery, actual version/commit/PR/main SHA evidence.

Milestones should be vertically sliced when practical: a user-observable path or complete enabling capability that leaves the product coherent. A mock, page shell, isolated API, database table or internal slice is not a milestone unless it independently satisfies the declared capability and evidence contract. Do not create a milestone solely because a PHDK stage ended.

## Milestone completion and publication gate

Inside an authorized `PHDK auto` / `PHDK auto force` goal, when a milestone's implementation and relevant permitted non-UAT verification are complete:

1. reconcile all included workstreams, dependencies, acceptance criteria and material risks;
2. run applicable milestone-level source/static/typecheck/safe-build/security checks; do not run behavioral tests, synthetic provisioning or UAT;
3. refresh remote `main` and resolve routine integration drift;
4. determine the actual next version from current `main` and the delivered behavior;
5. update version/changelog metadata;
6. create the required version-prefixed source commit(s);
7. push the scoped branch, open/update its PR, satisfy applicable controls, merge to `main`, and independently verify the resulting main SHA/version;
8. record the delivery evidence in `MILESTONE_PLAN.md` / PMO status;
9. execute the post-merge [PHDK_GIT_WORKSPACE_CLOSEOUT.md](PHDK_GIT_WORKSPACE_CLOSEOUT.md) local main fast-forward/SHA and targeted worktree/branch cleanup when a local checkout exists, recording retained dirty/divergent state without deleting it; then continue the next milestone only from synchronized local `main` (remote-only agents record NOT_APPLICABLE_REMOTE_ONLY).

A milestone publication is an incremental delivery checkpoint, **not final product acceptance**. Record source publication separately from deployment and acceptance, and never convert a simulated screen/mock or unexecuted criterion into working evidence. Do not run the full non-UAT Check/SEO/AEO lifecycle or declare the whole goal complete after every milestone unless that milestone is the entire authorized goal. UAT Prep/UAT/Fix remain deferred even at the final milestone; only explicit UAT authorization permits acceptance. PHDK lifecycle stages and milestone-internal slices do not trigger version bumps merely by ending.

If milestone publication is blocked by a real control, complete independent work that does not depend on it, preserve the exact blocker and do not fabricate delivery.

## PMO execution of the Plan

PMO executes the milestone roadmap rather than replacing it with unrelated workstreams.

For each active milestone PMO:

- resolves READY/BLOCKED workstreams from dependencies;
- maintains ownership and collision control;
- monitors material variance across the seven domains;
- evaluates change impact on value, scope, schedule, finance, resources, quality and risk when relevant;
- keeps assumptions distinct from verified facts;
- updates risks/issues and concrete response/owner;
- integrates workstream results into the milestone candidate;
- applies the milestone completion/publication gate;
- advances to the next milestone without requiring ceremonial approval.

A scope change that materially alters commitments, cost, date or risk follows current owner/governance rules. Routine implementation detail inside the authorized outcome does not become a new approval gate.

## AI-specific project controls

When AI supports project management, distinguish source facts, assumptions, estimates and recommendations. Critical decisions remain attributable to an authorized human when the governing organization requires that decision.

When AI is part of the product, also evaluate as applicable:

- strategic value and non-AI alternatives;
- model/system failure, hallucination, bias, security and dependency risk;
- governance, permitted tools and auditability;
- people/adoption/training impact;
- privacy, fairness, transparency, IP and acceptable use;
- stakeholder expectations and feedback;
- iterative measurement/optimization;
- data provenance, quality, permission and representativeness;
- reliability/monitoring/correction or withdrawal procedures.

These controls supplement `DEVSECOPS.md`, `AI_ADMIN_STANDARD.md` and product-specific requirements; they do not invent a compliance claim.

## Evidence and decision discipline

When information is insufficient, mark assumptions/unknowns explicitly rather than inventing dates, budgets, probabilities, owners or approvals. Ask only the highest-priority indispensable question after independent work is exhausted.

When a deliverable or milestone is declared development-complete, verify its implementation and required permitted non-UAT criteria and record evidence. Keep the documented behavioral acceptance criteria and deferred execution status separate; no static check establishes runtime acceptance. PHDK may prepare analysis and recommendations but must never simulate a human signature, formal acceptance or regulated approval that did not occur.
