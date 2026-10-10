# PHDK Capture Standard

## Command and purpose

Before substantive execution, run the universal preflight in `PHDK_PREFLIGHT.md`. Verify the active PHDK installation/version and inspect/use stage-relevant available skills from `SKILLS_REGISTRY.md`, unless the user explicitly disabled them.

`PHDK capture` is the requirements-discovery and intent-capture command for PHDK.

It serves two cases:

1. **Existing/advanced repository** — investigate the repository, existing product documentation, code, routes, data models, tests, configuration, intents, and historical decisions to reconstruct what the product currently appears to be, then professionalize that evidence into a coherent requirements baseline.
2. **New or empty project** — interview the owner from first principles and build the same professional requirements baseline from zero.

Capture does not implement product code. Its deliverable is a complete, professional, internally consistent requirements package that later governs `PHDK plan`, PMO, Auto, UAT, and Check.

Match `PHDK capture` case-insensitively after trimming whitespace. Reading this file, quoting the command, or installing PHDK does not invoke it.

## Core principle: evidence is not intent

For an existing repository, code and current behavior are evidence of what was built, not automatic proof of what should exist.

Capture must distinguish:

- **stated intent** — explicit problem, purpose, desired outcome, principles, constraints, and non-goals from owner/project sources;
- **implemented behavior** — what current source/configuration appears to do;
- **inferred requirement** — a professionalized requirement supported by multiple pieces of evidence but not explicitly stated;
- **legacy/accidental behavior** — implementation that may not belong to the intended product;
- **open question** — a material requirement decision that cannot be responsibly inferred.

Never rewrite the project's intent merely to match existing code. If code conflicts with stated intent, record the contradiction and ask which side is authoritative.

## Canonical requirements package

Capture creates or refreshes these canonical project artifacts.

### 1. PROJECT_INTENT.md

The durable project-level "why" and ethos.

Required sections:

- **Purpose / Ethos** — the underlying reason this product should exist and the principles it should embody.
- **Problem Statement** — the real problem or opportunity.
- **Target Users / Stakeholders** — who experiences the problem and who cares about the outcome.
- **Jobs / Desired Outcomes** — what users/stakeholders need to accomplish or change.
- **Value Proposition** — why this product is worth using/building.
- **Project Objectives** — concrete outcomes the project is trying to achieve.
- **Success Measures** — observable measures or qualitative acceptance signals; do not invent numeric targets.
- **Product Principles** — durable decision principles such as simplicity, trust, speed, human control, auditability, etc., only when supported.
- **Constraints** — hard constraints.
- **Non-Goals** — what this project intentionally will not become.
- **Risks / Tensions** — known tradeoffs that affect requirements.
- **Evidence and Provenance** — where the intent came from.
- **Open Intent Questions** — unresolved intent-level decisions.

Give durable intent statements stable IDs such as `INT-001`.

### 2. PROJECT_BRIEF.md

A concise executive synthesis of the project.

Required sections:

- one-sentence product definition;
- target users;
- problem and desired outcome;
- scope summary;
- principal workflows/capabilities;
- current stage;
- constraints/non-goals;
- known integrations/dependencies;
- definition of success;
- major open questions.

This file is summary, not the detailed source of requirements.

### 3. PRD.md

The professional Product Requirements Document.

Required sections:

1. Document status, revision, sources, and assumptions.
2. Executive summary.
3. Product intent references.
4. Stakeholders and actors.
5. Personas / Jobs-to-be-Done where evidence supports them.
6. Goals and measurable/observable outcomes.
7. Scope.
8. Non-goals / out of scope.
9. End-to-end user/business workflows.
10. Functional requirements.
11. Business rules.
12. Roles and permissions.
13. Data and content requirements.
14. Integrations and external dependencies.
15. AI/LLM requirements when applicable.
16. UX and interaction requirements.
17. Accessibility requirements.
18. Localization/i18n requirements.
19. Privacy/security/compliance requirements.
20. Reliability/performance/operability requirements.
21. Error, empty, loading, recovery, and degraded states.
22. Auditability/observability requirements.
23. Migration/backward-compatibility requirements when relevant.
24. Acceptance principles.
25. Assumptions.
26. Open questions / decisions needed.
27. Explicitly inferred requirements requiring later confirmation.

Use stable IDs:
- `FR-###` functional requirements;
- `BR-###` business rules;
- `NFR-###` non-functional requirements;
- `SEC-###` security/privacy requirements where useful;
- `DATA-###` data requirements where useful.

Every requirement must state:
- requirement statement;
- rationale / intent link;
- priority;
- source/provenance;
- acceptance signal;
- status: CONFIRMED, INFERRED, or OPEN.

Requirements must be implementation-neutral unless a technical constraint is itself a requirement.

### 4. FEATURES.md

The delivery-facing feature model.

Each feature must include:

- stable feature ID `FEAT-###`;
- name;
- intent links;
- requirement IDs satisfied;
- target actor(s);
- user/business value;
- priority P0/P1/P2 or explicit future;
- scope;
- acceptance criteria;
- dependencies;
- out-of-scope notes;
- status/evidence if reconstructing an existing repo.

Do not create a feature merely because a route/component/table exists.

### 5. REQUIREMENTS_TRACEABILITY.md

The traceability backbone.

At minimum maintain:

**Project Intent → Requirement → Feature → User Story → Acceptance Criterion → UAT Case**

Include:
- intent IDs;
- requirement IDs;
- feature IDs;
- user-story IDs when stories exist;
- acceptance criteria;
- linked UAT IDs after UAT is generated;
- source/provenance;
- implementation evidence when reconstructing an existing product;
- unresolved contradictions/gaps.

This is the canonical map used by `PHDK uat` and `PHDK check`.

## Relationship to feature-level intents

`docs/intents/*-intent.md` remains the durable intent mechanism for later individual features, bugs, stakeholder asks, and changes.

`PROJECT_INTENT.md` is project-level and answers "why does this product exist / what should it become?"

Feature/slice intent files answer "why are we making this particular change?"

Capture should reconcile existing intent files into the project requirements package without deleting, overwriting, or flattening their history.

## Existing repository investigation

Before asking questions, inspect as much relevant evidence as the current environment permits.

Prioritize:

1. Existing `PROJECT_INTENT.md`, `PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md`, `REQUIREMENTS_TRACEABILITY.md`.
2. `docs/intents/`, architecture decisions, task/status records, changelog, README, onboarding docs.
3. Routes/navigation and visible product areas.
4. Domain models/schemas and business entities.
5. API/service boundaries and permissions.
6. Tests and fixtures, especially acceptance/business behavior.
7. Environment/configuration names and integration adapters.
8. Admin capabilities and role models.
9. Existing AI integrations, prompt definitions, consumption tracking, imports, payments, notifications, etc.
10. Git history/current branches only when needed to understand product evolution.

Do not treat generated/vendor/build artifacts as product requirements.

Build an evidence ledger with:
- source;
- observed fact;
- confidence;
- requirement/intent implication;
- contradiction/open question if any.

## From evidence to professional requirements

For every material behavior discovered:

1. Ask what user/stakeholder outcome it appears to support.
2. Link it to an existing intent statement if possible.
3. Determine whether it is:
   - confirmed requirement;
   - plausible inferred requirement;
   - technical implementation detail;
   - legacy/accidental behavior;
   - unknown.
4. Promote only confirmed or responsibly inferred user/business needs into the PRD.
5. Keep implementation details as evidence or constraints rather than rewriting them as user requirements.
6. Record contradictions rather than smoothing them over.

Capture should simplify duplicate or contradictory requirement language into one normalized requirement while retaining provenance.

## New-project discovery

When the repository has no meaningful product evidence, begin from zero.

Capture the minimum professional discovery domains:

- purpose/ethos;
- problem/opportunity;
- target users and stakeholders;
- desired outcomes/jobs;
- value proposition;
- business/organizational objective;
- success definition;
- core workflows;
- scope and non-goals;
- roles/permissions;
- information/data handled;
- integrations;
- AI usage if any;
- monetization/payment if any;
- content/editorial requirements;
- privacy/sensitivity;
- accessibility;
- localization;
- reliability/performance expectations;
- audit/observability needs;
- constraints/deadlines only when real;
- migration/legacy context;
- open risks and assumptions.

Do not force irrelevant enterprise ceremony on a small project. The professional standard is completeness of material decisions, not maximum document length.

## Gap-driven interview

Capture must investigate first and ask second.

Do not run a fixed questionnaire when the repository or conversation already answers the question.

After the first investigation pass:

1. Draft the requirements package with known evidence.
2. Build a **Requirements Gap Register** of missing material information.
3. Rank gaps:
   - **Blocking** — cannot formulate a coherent requirement without it;
   - **Material** — affects scope, behavior, risk, or acceptance;
   - **Refinement** — useful precision but a safe assumption may be recorded.
4. Ask only unanswered Blocking/Material questions.
5. Ask one focused question at a time by default; a small tightly related batch is allowed when it reduces unnecessary round-trips.
6. After every answer, update the model and ask the next highest-value unresolved question.
7. Stop asking when remaining gaps can be recorded honestly as assumptions/open questions without making the requirements misleading.

Never ask the user to restate information already present in the repository or conversation.

## Professional question quality

Questions should seek decisions, not trivia.

Prefer:
- "Who is allowed to approve an imported dataset before it becomes official, and what should happen if approval is revoked?"

Avoid:
- "Do you want an approve button?"

Prefer:
- "What outcome tells you this project is successful six months after launch?"

Avoid:
- "What KPI should we put on the dashboard?"

Prefer:
- "Which user groups may see or change this information, and are there any cross-team boundaries?"

Avoid:
- "Should we add RBAC?"

## Confidence and provenance

Every substantive captured statement should be attributable to one of:

- OWNER CONFIRMED;
- EXISTING PROJECT DOCUMENT;
- CURRENT CODE EVIDENCE;
- TEST/BEHAVIOR EVIDENCE;
- INFERRED — HIGH/MEDIUM/LOW confidence;
- OPEN / UNKNOWN.

Do not present inferred requirements as owner-confirmed.

A repository reconstruction may produce a complete professional draft while still containing INFERRED items. Surface those clearly.

## Completion gate

Capture is complete when:

- `PROJECT_INTENT.md` is coherent and captures ethos, problem, outcomes, constraints, and non-goals;
- `PROJECT_BRIEF.md` accurately summarizes the product;
- `PRD.md` contains all material requirement domains applicable to the project;
- `FEATURES.md` maps the delivery surface without inventing scope;
- `REQUIREMENTS_TRACEABILITY.md` links intent to requirements/features and has no unexplained orphan P0 requirement;
- every Blocking requirements gap is resolved;
- every remaining Material gap is either answered or explicitly documented as OPEN with impact;
- contradictions between intent/docs/code are resolved or explicitly listed;
- inferred requirements are labeled;
- the owner has a clear list of any remaining decisions.

Capture must not declare requirements "complete" merely because every template section has text.

## User-facing interaction contract

At the beginning of `PHDK capture`, explain briefly what Capture is doing: it will investigate existing evidence, formulate the professional requirements baseline, identify missing material information, and ask only the questions that are actually needed.

After the first investigation/draft pass, explicitly state one of these two conditions:

- **No questions needed:** say clearly that the available repository/conversation evidence is sufficient and that there are no Blocking/Material questions to ask.
- **Questions needed:** say clearly that material information is still missing, then ask the highest-value question(s) under the gap-driven interview rules.

Do not leave the user guessing whether Capture is still analyzing or waiting for information.

When the last required question has been answered—or immediately when no questions are needed—finish the canonical artifacts and give an explicit completion message. The completion message must say, in substance:

> Todo lo que levanté y formulé quedó capturado en estos archivos para que puedas revisarlos.

Then list each produced/updated artifact with a one-line description and, when the environment supports it, a direct file/repository link:

- `PROJECT_INTENT.md` — intent, ethos, purpose, outcomes, constraints and non-goals.
- `PROJECT_BRIEF.md` — executive project summary.
- `PRD.md` — professional detailed requirements.
- `FEATURES.md` — prioritized delivery feature model and acceptance criteria.
- `REQUIREMENTS_TRACEABILITY.md` — intent-to-requirement/feature/story/UAT traceability.

Also state whether any INFERRED or OPEN items remain. Never imply that requirements are owner-confirmed when they are inferred.

## Interaction and stopping behavior

`PHDK capture` is an interactive requirements command. It may span multiple turns because its purpose is to obtain missing human information.

Unlike `PHDK auto`, it is allowed and expected to ask questions when material requirements are unknown.

During the interview:
- do not ask for approval after every document/section;
- ask only requirement questions;
- continuously update the canonical artifacts when repository editing is available;
- do not start product implementation.

When all Blocking gaps are resolved and the professional requirements baseline is complete, explicitly state that there are no further required questions, then present:
- captured intent/ethos;
- scope/non-goals;
- actors;
- primary workflows;
- requirements/features counts;
- confirmed vs inferred vs open items;
- remaining material decisions;
- artifact paths/links, introduced with a clear statement that everything captured/formulated is stored there for owner review.

Then stop unless the user's current request also explicitly included the next step such as kit generation, `PHDK PMO`, `PHDK auto`, UAT, check, or git delivery.

## Git and delivery boundary

The command itself authorizes creation/update of the Capture requirements artifacts in the current repository. It does not by itself authorize product-code implementation, provider changes, or deployment.

If the user's request is simply `PHDK capture`, complete the documentation capture and stop after the requirements package is ready. Follow the repository's current documentation delivery rules only when the user explicitly requested git delivery or when the current parent task already includes it.

## Relationship to other PHDK commands

- **Capture → Plan:** Capture defines what the product must achieve; Plan converts that into solution/repository/UX architecture and an executable implementation plan.
- **Capture → PMO:** PMO consumes Capture plus Plan to detect and coordinate workstreams.
- **Capture → Auto:** Capture defines the professional product baseline; Auto implements an already-authorized single goal/workstream from that baseline.
- **Capture → UAT:** UAT derives user stories and acceptance cases from `PROJECT_INTENT.md`, PRD/FEATURES, and traceability.
- **Capture → Check:** Check uses Capture artifacts as the strongest project-specific applicability source when deciding which PHDK standards apply.
- **Capture vs SPEC Interview:** `SPEC_INTERVIEW_PROMPT.md` is a legacy/narrow interview reference. `PHDK capture` is the preferred command for full professional discovery/reconstruction.
- **Capture vs Handoff:** Capture defines what the product should be. The handoff/kit translates those requirements into the broader PHDK project documentation needed for implementation.
- **Capture vs feature intent:** Capture owns project-level intent; `INTENT_CAPTURE_STANDARD.md` continues to own later feature/change intents.

## Existing project preservation

When Capture runs on an advanced repository:

- do not delete working product behavior;
- do not rewrite architecture merely to match a preferred template;
- do not erase historical intents;
- do not overwrite confirmed requirements with inference;
- do not classify undocumented code as automatically wrong;
- do not silently bless existing behavior as required.

Capture documents the product truth and its uncertainties; subsequent Auto/Check work decides what code should change.
