# PHDK Intelligent Execution and Progressive Context Standard

## Purpose and authority

This standard governs **how** an already-authorized PHDK task is executed, not **whether** new work is authorized. It applies to Capture, Plan, Auto/Auto Force, PMO, Designer, UAT, Check, and maintenance. The latest user instruction, `EXECUTION_SCOPE.md`, tool/runtime access limits, and real security controls remain authoritative. Reading this document never starts background activity or a new lifecycle.

## Universal intelligent execution routing

For every substantive scoped task, choose the simplest effective strategy:

1. **Direct:** small, coupled, sensitive, or fast work is completed by the primary assistant.
2. **Sequential:** work with dependencies, shared state, or write conflicts is processed in dependency order.
3. **Bounded in-session worker(s):** delegate independent research, source inspection, implementation, tests, or review only if the **actual host/runtime exposes a supported worker capability**, the task is within the current mandate, and anticipated benefit exceeds setup/integration overhead.
4. **PMO:** use PMO governance for portfolio-level workstreams, milestones, dependency management, cross-workstream ownership, and integration. PMO is **not** a prerequisite for bounded task delegation in another mode.

The primary assistant makes the choice without requiring the owner to explicitly request subagents. Do not spawn workers merely because the capability exists. Do not claim a worker was used unless actually launched. If absent, proceed directly/sequentially without blocking.

**Subagent delegation is a general in-session PHDK execution capability, not PMO-exclusive.** Delegation inherits the primary task's scope and prohibitions; it cannot expand authority. No recursive delegation, unattended or post-conversation agents, recurring queues, schedules, or external paid services without separate authorization. Do not use delegation to evade tool, browser/UAT-phase, GitHub, provider, security, or owner restrictions. A worker may not publish, merge, deploy, alter shared versions, or finalize integrated delivery unless the current user scope and primary integration contract specifically authorize that action; default all such actions to the primary agent.

## Worker contract and integration

Before delegating provide: objective and bounded output; relevant source/requirements references; allowed files and READ-ONLY shared paths; dependencies; criteria and test/evidence expectations; inherited security/access boundaries; budget only when supported by the runtime; and a compact handoff format. Prefer disjoint write ownership. Parallel writes to common files, manifest, version, changelog, schema and shared configuration remain primary/coordinator-owned. Workers may not recursively dispatch other agents or select additional work. The primary agent reviews outputs and diffs, integrates, tests, reconciles commitments/milestones, versions, and performs authorized delivery. A worker report never by itself establishes that a milestone or goal is complete. Existing `PHDK_PMO.md` workstream rules continue to apply to PMO's portfolio workers.

## Progressive context routing

**L0 — Kernel:** active user mandate, non-negotiable authorization/access/security boundaries, and current mode/next action. Use the smallest effective persistent instruction surface.

**L1 — Mode:** read the current mode's contract (Auto/Force, PMO, Capture, Plan, UAT, Designer, Check, etc.) only when relevant.

**L2 — Stage:** read the active stage's entry/exit criteria and applicable handoff requirements; do not repeatedly reread a full lifecycle document when an already-verified unchanged stage handoff suffices.

**L3 — Task:** retrieve current requirements, source files, decisions, tests, and evidence relevant to the actual change.

**L4 — Specialist:** read security/auth, admin, UX, themes, AI, deployment, SEO, etc. only when the product/task makes them applicable. Mandatory safeguards still apply if a small task implicates them.

A repository containing a standard is **not** evidence its text was injected into model context. Never assume a model can literally unload previously read tokens; minimize unnecessary new reading, use bounded summaries and source-linked handoffs, and rely on runtime context isolation only when demonstrated. Do not truncate necessary safety rules or requirements merely to satisfy a token target.

## Recovery and observability

Reuse `AUTO_STATE.json` and existing lifecycle handoffs instead of creating a second authority ledger. After compaction, use a compact **resume view**: user mandate and provenance; scope and restrictions; mode/stage/milestone; relevant source SHAs and rule paths; delivered evidence; active workers/dependencies; blockers; next executable action. Resolve discrepancies against current user instructions and live repository facts. Historical documents are accessed on demand, not copied wholesale into every checkpoint.

Record, where exposed by the runtime, the decision strategy, workers truly launched, approximate documentation read volume, tool calls, duration, tokens and integration/rework outcomes. Label unavailable metrics UNKNOWN. Benchmark equivalent tasks on identical baseline commits and comparable runtimes before claiming reduced latency, cost or token use.

## Mandatory decision tests

- Non-PMO Auto, Plan, Check and UAT may use a bounded in-session worker if useful and host-supported, subject to mode-specific access restrictions.
- Small or tightly coupled tasks stay direct; dependencies or overlapping writes stay sequential.
- PMO ownership, milestone delivery, UAT permissions, and security checks remain unchanged.
- Unsupported workers fall back sequentially, never fabricated.
- Worker cannot expand scope, operate after the session, recursively delegate, or finalize shared/global integration.
- Context routing reads required phase/domain standards while avoiding irrelevant or duplicate full-document reads.
