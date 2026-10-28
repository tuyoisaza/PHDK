# PHDK Documentation, Nomenclature and Traceability Standard

## Purpose and authority

This is the canonical **downstream product-documentation** convention for PHDK. It is vendored as \`phdk-standards/PHDK_DOCUMENTATION_STANDARD.md\` and applies when Capture, Plan, Design, PMO, Auto/Auto Force, Check, or an authorized development task creates or materially revises project knowledge. It does not relocate PHDK's own standards, override \`EXECUTION_SCOPE.md\`, activate dormant work, or invent owner approval.

**Principle:** stable categories, versioned durable content, one active execution record, traceable decisions, and low-overhead automatic maintenance *within the current authorized foreground work*. Documentation describes intent and evidence; it never substitutes for implemented software, a passed test, a deployed revision, or acceptance.

## Canonical downstream hierarchy

\`\`\`text
<project>/
  README.md                   # entry point and docs/INDEX.md link
  AGENTS.md                   # agent instructions, not mutable project state
  TASK.md                     # one current authorized goal / next action
  STATUS.md                   # optional factual project summary, not a second task queue
  docs/
    INDEX.md                  # generated active-document locator
    intents/                  # project ethos and later feature/change intent
    briefs/                   # project/product/requirements and scope briefs
    decisions/                # permanent ADRs and product/design decisions
    plans/                    # solution, repository, UX, milestones, delivery/deploy plans
    images/                   # design references, mockups and other retained visual assets
    evidence/                 # non-UAT proof, Check references, validation snapshots
    phdk/lifecycle/           # existing immutable PHDK stage run handoffs, unchanged
\`\`\`

Create only folders needed by actual work. Do not generate empty category folders, redundant \`status/\`, \`tasks/\`, or a second planning ledger. Existing specialized directories such as \`docs/fixtures/\`, \`docs/design/\`, \`docs/audits/\` and \`docs/repos/\` are not deleted or reorganized by PHDK installation.

### Canonical location of existing PHDK logical artifacts

| Existing logical name (may be a legacy root filename) | New/updated versioned file |
|---|---|
| \`PROJECT_INTENT.md\` | \`docs/intents/project-intent.v0.md\` |
| Feature/change intent | \`docs/intents/<topic>-intent.v0.md\` |
| \`PROJECT_BRIEF.md\` | \`docs/briefs/project-brief.v0.md\` |
| \`PRD.md\` / \`FEATURES.md\` | \`docs/briefs/prd.v0.md\` / \`docs/briefs/features.v0.md\` |
| \`REQUIREMENTS_TRACEABILITY.md\` | \`docs/plans/requirements-traceability.v0.md\` |
| \`SOLUTION_ARCHITECTURE.md\`, \`REPOSITORY_ARCHITECTURE.md\`, \`UX_ARCHITECTURE.md\` | \`docs/plans/<logical-name>.v0.md\` |
| \`MILESTONE_PLAN.md\` / \`IMPLEMENTATION_PLAN.md\` | \`docs/plans/milestone-plan.v0.md\` / \`docs/plans/implementation-plan.v0.md\` |
| \`ARCHITECTURE_DECISIONS.md\` / ADRs | \`docs/decisions/architecture-decisions.v0.md\`, \`docs/decisions/adr-0001-<topic>.v0.md\` |
| \`UI_DESIGN_SYSTEM.md\` / \`UX_UI_DECISIONS.md\` | \`docs/plans/ui-design-system.v0.md\` / \`docs/decisions/ux-ui-decisions.v0.md\` |
| Design concepts or screenshots | \`docs/images/<topic>/v0/<asset-name>.<ext>\` |

\`v0\` is the *initial draft*, not a claim of approval. For material baselines, the next owner-approved or otherwise legitimately selected revision is \`v1\`. Other named project records (\`TASK.md\`, \`STATUS.md\`, \`PHDK_CHECK_REPORT.md\`, \`PMO_STATUS.md\`, \`PHDK_LIFECYCLE_STATUS.md\`) remain where their governing operational contracts place them. They are current-state controls, not historical document baselines. Historical PHDK handoffs remain under \`docs/phdk/lifecycle/\` with their existing names.

## Filenames, versions and metadata

- Category folders remain **unversioned**. Durable Markdown files use lowercase \`kebab-case.vN.md\` where \`N\` is a nonnegative integer, for example \`project-intent.v0.md\`, \`deployment-plan.v1.md\` or \`adr-0003-auth-strategy.v2.md\`. Do not put spaces, dates or \`latest\` in versioned names.
- Versions are **per document identity**, not per folder and not the project's/PHDK's SemVer. Use \`v0\` for the first draft, \`v1\` for its first established baseline, and \`v2\` for a materially new baseline. Subsequent small copy/metadata corrections use Git history without a new document version.
- A material change to intent, scope, accepted architecture, interfaces or delivery assumptions creates a new versioned file. Do not silently rewrite the substantive body of an earlier baseline. Status metadata and supersession pointers may be corrected with Git history.
- Each versioned Markdown file begins with plain YAML-style scalar front matter as below. \`created_at\` and \`updated_at\` are explicit ISO dates; filesystem creation timestamps are unreliable after cloning. Do not invent historical dates or authorization; use \`unknown\` for unavailable provenance and record the limitation in the body.
- \`status\`: \`draft\`, \`active\`, \`superseded\`, \`archived\`. An \`active\` document is the operative baseline, **not** proof of human approval. \`authority\` records \`owner-approved\`, \`owner-request\`, \`agent-selected\`, \`inherited\`, or \`unknown\`; Auto Force must not use \`owner-approved\` for agent choices.
- \`doc_id\` is stable across versions of the same logical document (e.g. \`project-intent\` or \`ADR-0003\`). A decision keeps its ADR ID permanently; a replacement decision normally gets a new ADR ID and links to the superseded ID rather than rewriting its conclusion.

\`\`\`md
---
doc_id: project-intent
version: v0
status: draft
created_at: 2026-10-28
updated_at: 2026-10-28
authority: owner-request
---

# Project intent
...
## Traceability
- Source: <owner brief or verified repo location>
- Related decisions: <ADR IDs and links, if relevant>
- Related plans/milestones: <IDs and links, if relevant>
\`\`\`

Do not use the example dates or provenance as defaults for real documents. Preserve stable requirement, story, milestone and decision IDs when splitting or revising documents.

## Image and evidence versioning

Visual binaries and editable sources use \`docs/images/<topic>/vN/\` with descriptive lowercase asset names and a nearby versioned design specification/decision linking to them. Retain actual originals where permitted, not just dead external links. An asset folder's \`vN\` is a **visual baseline revision**, not necessarily the associated Markdown file's revision or project SemVer. Do not create AI images, previews, browser journeys or screenshots simply to fill a folder.

Verification evidence can use \`docs/evidence/<milestone-or-topic>/vN/\` when it is a stable documentary snapshot, and must include the observed Git SHA/revision, scope, date, method, result and explicit \`NOT RUN\`/\`UNVERIFIED\` limitations. Existing PHDK lifecycle snapshots and UAT's explicit-only artifacts remain authoritative at their original paths; use links rather than cloning an evidence ledger.

## Active-document index and traceability

\`docs/INDEX.md\` is a **generated locator**, not an approval register or a duplicate requirements source. For each logical document list its category/ID, active baseline, draft revision(s), and historical links. If no active baseline exists, identify the newest draft as provisional. A newer draft must never displace an older active baseline by filename order alone.

When the current authorized task creates or changes versioned docs, refresh \`docs/INDEX.md\` in the *same scoped change* and verify that it matches metadata. Use the vendored standard-library helper:

\`\`\`sh
python phdk-standards/scripts/phdk_docs_audit.py --root . --check
python phdk-standards/scripts/phdk_docs_audit.py --root . --sync-index  # write; only in authorized work
python phdk-standards/scripts/phdk_docs_audit.py --root . --check --changed docs/plans/deployment-plan.v1.md
\`\`\`

Use \`scripts/phdk_docs_audit.py\` when operating on the canonical PHDK source repo itself. It performs a **static documentation check only**. A bare \`PHDK check\` must not use \`--sync-index\` or silently rename/migrate files. Generated output must not overwrite an independently owner-maintained \`docs/INDEX.md\` that lacks the helper's signature.

Maintain **Intent → Brief/Requirement → Decision → Plan/Milestone → TASK/Implementation → Evidence** with stable IDs and links, using only relevant parts of this chain for the current task. Mark \`PLANNED\`, \`IMPLEMENTED\`, \`PUBLISHED\`, \`DEPLOYED\`, \`ACCEPTED\`, \`NOT RUN\`, \`UNVERIFIED\` separately as the existing lifecycle requires; the index is not a status dashboard.

## Stage duties and non-negotiable constraints

| Stage | Documentation duty |
|---|---|
| Capture | Reuse current root legacy or indexed baseline, then create/update versioned intent and brief/requirements; preserve provenance and map requirement IDs. |
| Plan | Resolve current active intent/brief/decisions; create/revise versioned technical, UX, delivery plans; link milestone and implementation IDs; keep root \`TASK.md\` actionable. |
| Design | Link visual decision/provenance to retained \`docs/images/<topic>/vN/\` assets; do not invent approval or demand screenshots outside permitted modes. |
| PMO | Workstreams consume current indexed baselines and report milestone/decision deltas; they must not fork a competing set of project plans. |
| Auto / Auto Force | At entry load \`docs/INDEX.md\` and root TASK, verify/reconcile required upstream docs; update affected docs and index at each material milestone and before Check/delivery. Do not regenerate the whole library or interrupt implementation for document ceremony. |
| Check | Audit location, filename, metadata, duplicate active baselines, index currency, ID links and stale decision/plan references with read-only checks; classify new violations as actionable gaps and legacy debt proportionately. |
| UAT (explicit only) | Read the intent/acceptance baseline and retain authorized acceptance evidence at the existing UAT/lifecycle locations; documentation does not grant UAT authorization. |
| Delivery | Verify the committed index, current TASK/milestone references and truthful evidence agree with actual Git/PR/deployment state. |

### Adoption in existing (brownfield) projects

1. Inspect existing root and \`docs/\` records before proposing changes. **Do not bulk-move, rename or delete** owner artifacts on install/Upgrade, or manufacture missing v0 history.
2. A verified existing \`PROJECT_INTENT.md\` or \`IMPLEMENTATION_PLAN.md\` remains an **accepted legacy canonical input** until its owning task materially revises it; the new versioned path supersedes it only after links and ownership have been reconciled. Avoid simultaneously editing two competing copies.
3. When in-scope migration is authorized, preserve original Git history and a pointer/redirect or updated references for legacy consumers. Record the legacy-to-new path mapping in the new index or task; never declare a migration complete until in-repo references and applicable tooling are updated.
4. For untouched legacy files, report \`LEGACY_COMPATIBLE\` or low-priority technical debt; do not block delivery or generate dozens of empty documents. Newly created or materially revised project documents must follow this standard.
5. Keep documentation proportional. Read indexed *relevant* baselines and supporting excerpts, not the entire repository at every substep. Mandatory full-intent reconciliation in Auto still applies.

## Acceptance criteria

- Stable, descriptive folders; versioned durable Markdown documents and versioned design asset baselines only as needed.
- One unambiguous active revision per \`doc_id\`/category; draft vs active vs historical clearly distinguished; decision supersession explicit.
- Valid front matter, observed provenance, and a current generated \`docs/INDEX.md\`.
- \`TASK.md\` is the current execution contract; plans, STATUS and historical snapshots are not parallel authorizations.
- The current milestone's intent, decisions, implementation, evidence and delivery state are reconcilable by paths/IDs without reconstructing chat history.
- No hidden changes to owner content, invented approvals, unnecessary document proliferation, local runtime tests, background jobs or UAT activation.
