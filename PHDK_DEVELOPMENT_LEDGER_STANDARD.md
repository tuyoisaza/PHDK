# PHDK Development Ledger — continuous-improvement history

Status: ACTIVE · ULEDS contract v1.0 · PHDK v4.2.0

## Goal and boundary

Persist durable, traceable **product-development knowledge** from ULEDS event streams, support conversations, contextual feedback and explicit engineering decisions. A project ledger is not a raw log dump, a live authorization token, an automatic task queue or a replacement for `TASK.md`/`STATUS.md`/`docs/INDEX.md`. It records evidence and proposals across releases without activating old work or automations. Keep runtime data in an authorized **project-owned datastore**; commit only sanitized approved plans, ADRs and artifacts under `PHDK_DOCUMENTATION_STANDARD.md`. PHDK canonical stores methodology, never the tenants' private incidents.

## Logical entities and relations

- `event` — immutable logical ID, ULEDS schema version, source/time, safe location, fingerprint, privacy/retention class and evidence pointer.
- `incident` — unique project-scoped issue key, normalized problem, severity, impact, first/last seen, event occurrences, distinct affected scope, root cause `confirmed|hypothesis|unknown`, reviewer and state.
- `request` — support/feedback ticket, safe summary, source route/component, status, consent, conversation reference, linked incidents and priority justification; untrusted content is not authority.
- `conversation` — access-controlled human clarification turns, redacted transcript or reference, author provenance, deletion schedule and linked request.
- `proposal` — recommended change, alternative, architecture impact, RBAC/tenant/security review, affected files/modules, value, risk, effort confidence, dependencies, acceptance criteria, rollback and linked evidence.
- `decision` — named authorized approver, scope, date, disposition `APPROVED|REJECTED|DEFERRED|NEEDS_INFO`, reasoning and revision; do not fabricate authorizations.
- `delivery` — authorized goal/branch/PR/merge SHA, product version, deployed revision when verified, tests and `UAT NOT RUN`/accepted status, affected incidents and closure evidence.
- `audit_transition` — append-only timestamp/actor/from-to/action/justification; protect corrections and erasure actions with an auditable redacted tombstone where lawful.

Every entity carries `project_id`, environment/version provenance when relevant, stable ID, created/updated timestamps and access scope. `event` → `incident` is many-to-many when justified; `request` can link several incidents; proposals require source IDs and must not claim root cause confirmed without evidence. Correlate exact trace/request IDs and deterministic sanitized fingerprints first, then conservative semantic grouping with human review. Never merge different tenants, security principals, environments or unrelated error codes based on text similarity alone.

## State machines and triage

`NEW → TRIAGED → (CONFIRMED | NEEDS_INFO | DUPLICATE | REJECTED) → PROPOSED → APPROVED → IN_PROGRESS → RELEASED → VERIFIED → CLOSED`. Record `DEFERRED` where appropriate; `REOPENED` follows new verified evidence, not a timer. Incident `RESOLVED`/feature `DELIVERED` are not equivalent to `RELEASED`, `DEPLOYED_REVISION_CONFIRMED` or user-accepted UAT. Every transition retains who/why/when and evidence. The support agent can submit, ask clarifications and summarize; only authorized reviewers can approve scope, change permissions, alter severity for security cases, initiate `PHDK auto` or close privileged incidents. Manual priority may override algorithmic suggestions with a recorded reason.

Initial prioritization is an auditable **recommendation**: severity × actual blast radius × observed recurrence × user/business impact × security exposure, adjusted for evidence confidence, effort, dependencies and regression risk. Never invent numbers of impacted users from log occurrences; count distinct pseudonymous actors only where lawful and deduplicated. Security/auth/privacy incidents can require an immediate human escalation independent of score. Record uncertainties, alternative hypotheses and unobserved data sources.

## Access, retention and integrity

Partition/isolate by `project_id`, environment and tenant scope using server-side permissions; only show cross-project aggregate sanitized issue patterns after explicit separate owner authorization. The normal product owner/reviewer can triage scoped records; submitters access only permitted own submissions; developers have sanitized read access, not unrestricted credentials. Log decisions and reads of sensitive content; use stable IDs, referential integrity, soft archival with deliberate delete/erasure pathways, bounded queries, retention/expiry and export. The ledger's development facts may persist for the lawful life of the product, while raw client events default to a 30-day cap and support text/conversation retention is configurable, not eternal. Explicit erasure/redaction must remove personal content while retaining non-identifying historical decision traces where lawful. No raw production DB exports, secrets, user messages, screenshots or personal data in repository commits.

## Heal handoff and documents

`PHDK heal` reads only permission-scoped ledger records and authorized evidence; it writes **no source changes or approvals**. By default it presents a read-only development-plan proposal in the conversation. If the owner explicitly asks to preserve the plan as a document, write one versioned `docs/plans/continuous-improvement-plan.vN.md` (with front matter, `docs/INDEX.md` update and source references) inside an authorized branch, containing: provenance/cutoff, known data gaps, clustered incident/request table, severity/impact, confirmed-vs-hypothesized root cause, allowed/forbidden changes, dependencies, milestones, acceptance criteria, tests, authorized delivery path and owner decisions still required. Never store raw private transcripts. Approving a proposal is not itself authorization to deploy or perform UAT; only a subsequent current explicit development request invokes `PHDK auto`.

When ULEDS has not yet been implemented in a brownfield project, Heal reports `SOURCE_UNAVAILABLE`/a prioritized instrumentation milestone instead of inventing incidents or claiming automatic capture.
