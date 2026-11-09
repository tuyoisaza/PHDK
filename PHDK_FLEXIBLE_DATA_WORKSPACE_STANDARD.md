# PHDK Flexible Data Workspace Standard

## Contract, applicability and ownership

**OPTIONAL PER RESOURCE.** PHDK Data Workspace is a capability profile for advanced tabular record workflows, not a mandatory CRUD replacement, new lifecycle stage, automatic installation, permission, general-purpose database abstraction or an already released package. `CRUD_STANDARD.md` and `TABULAR_DATA_EXCHANGE_STANDARD.md` remain normative regardless of whether this optional profile is chosen. This specification is vendored with PHDK; implementation code belongs in a separately versioned package, never implicitly inside canonical PHDK.

When Capture/Plan discovers a significant record-management workflow (large collections, routine multirow entry, ad hoc reporting, spreadsheet dependence or frequently changing metadata), **recommend** Data Workspace if its value justifies integration and maintenance. Name the relevant resources, roles, benefits, estimated complexity, core behavior, optional capabilities and baseline-CRUD alternative. Ask a single scope-specific question alongside existing setup/Design decisions: **Enable for recommended resources, choose a subset, or decline?** Do not ask sequentially per feature, assume silence is consent, or reopen a previously approved unchanged selection.

Record the owner decision and selected capabilities in the existing Plan/Design/resource matrix, not a new document or gate. Permissible dispositions:
- `NOT_APPLICABLE`: no relevant resource, no recommendation.
- `RECOMMENDED_PENDING_OWNER`: one consolidated proposal awaiting actual interactive choice; independent work continues.
- `OWNER_ENABLED`: named resource and selected extensions approved by owner.
- `OWNER_DECLINED`: baseline CRUD and independently eligible exchange remain.
- `EXISTING_APPROVED`: reuse evidence of a prior selection for unchanged scope.
- `NOT_SELECTED_AUTO_FORCE`: with no explicit owner opt-in, Auto Force retains baseline CRUD. Force may select UI design for *already enabled* features, not authorize new optional scope.

No installation, migration, provider write, UAT, real-data operation, new infrastructure or spending is authorized by this standard, catalog visibility or an agent's recommendation.

## Reusable architecture

Separate (1) framework-neutral typed grid/query state, (2) optional React/Next.js presentation using consuming-project design tokens, (3) typed API adapters, (4) consuming application's server-side policy/tenant/field authorization and business validation, and (5) independently selectable feature extensions. Review REUSE/ADAPT/BUILD, supported dependency versions, licenses and maintenance before constructing a package. TanStack Table plus existing accessible shadcn/Radix components is a possible fit, **not a mandatory dependency**. Never embed an InmotionTitan/Titanic table, SQL schema, route, financial rule, UI theme, customer data or Railway configuration in the generic module.

**Core for an enabled resource:** discoverable table and record detail/navigation, reliable page or cursor pagination, click/keyboard sort on appropriate headers with clear direction and deterministic tie-breaker, search, typed combinable per-field filters, hide/show/reorder columns, responsive empty/loading/error states, and optional saved personal/shared views. Keep query and UI state coherent across pages; bound server queries, use stable record IDs, cancellation, deterministic sorting and accessible header controls. Server-side filtering, sorting and pagination are preferred for large data. Virtualization is conditional on observed need. Hiding a column is a display preference and NEVER an authorization boundary.

**Independent extensions, OFF unless selected for that resource:** keyboard-first inline/multirow edit and paste; bulk actions; tabular import/template/XLSX/CSV export; notes and review flags; undo/recovery/history; custom field definition and value editing. Existing mandatory import/template/export requirements under `TABULAR_DATA_EXCHANGE_STANDARD.md` are never made optional by declining this profile. Disabled optional features are not missing-CRUD Check failures.

## Custom fields — privileged metadata, not schema mutation

Only roles with server-enforced `fields.manage` (or a separately mapped equivalent) can create, rename, deactivate or change field *definitions*. The right to edit normal record values (`records.update`) does not include definition management. Define authorization per tenant, resource, field, role and operation; distinguish permission to define a field from separately permitted read/write/export/import of its values.

Store stable field IDs and versioned metadata (label, bounded type, validation rules, default, requiredness, sensitivity, read/write visibility, filter/sort/export eligibility, audit owner, deactivation and migration policy). Limit types deliberately, e.g. text, decimal, date, boolean and controlled enum. Use a vetted metadata/value or extension-storage model. **Never automatically ALTER business tables** when a user creates a field. Reject executable formulas, unsafe or overlarge metadata, arbitrary references, and hidden-field access through direct APIs. Domain-critical financial or workflow semantics require domain change review; no user-created field automatically becomes a billable value or permission flag.

## Integrity, recoverability and permissions

Server policy authoritatively restricts each field, row, tenant, sort/filter operator, import/export, saved-view share, custom definition, update and batch action. Column hiding does not protect secret data. Denied fields cannot be recovered via exports, filters, saved-view payloads, counts or API probes. Use allowlisted parameterized filters, query/row limits, CSRF protection as applicable, tenant-safe caching and audit trails. For imports/exports follow `TABULAR_DATA_EXCHANGE_STANDARD.md` including spreadsheet injection defenses.

Financial amounts remain typed numeric values. Unstructured circumstances such as "paid half, rest Friday" belong in typed payment state, note or flagged exception, **never** coerced into invalid monetary values. Failed inline edits preserve draft input and return actionable cell errors without falsely reporting persistence. Concurrency conflicts and bulk partial failures remain visible. Soft-delete/undo/recovery is subject to domain retention, immutability and audit requirements; a toast-only 10-second undo is not an adequate universal recovery policy. Explicitly exclude unsafe destructive actions.

## Design, implementation, evidence and private-library gates

- **Capture/Plan:** inventory relevant jobs-to-be-done and eligible resources; recommend profile with actual costs and alternatives, get explicit owner selection, record chosen feature set and server-side permission matrix, and assess REUSE/ADAPT/BUILD. Public catalog status is `SPECIFICATION_ONLY` until a real accepted package exists.
- **Design:** put chosen workspace behaviors in the EXISTING consolidated coded visual/motion choice board and integrated preview; show accessible sort/filter/column-picker/custom-field-management/error states and role-based differences. No new approval stage.
- **Implementation:** integrate only enabled resources/features, preserve existing UI and CRUD where suitable, use service adapters, package install instructions, stable exports/API, versioning, test fixtures, migration/backout instructions, and backend authorization. Do not claim portability from one consumer.
- **Check:** assess only owner-selected advanced features, field-level authorization and relevant implementation evidence. Decline/NOT_APPLICABLE is not a defect; baseline CRUD and eligible exchange requirements still apply. Static evidence cannot prove runtime UX.
- **Explicit UAT only:** if separately invoked and authorized, verify actual keyboard/click sorting, combined filters over multiple pages, columns, saved views, field-definition permission denials by UI AND API, tenant isolation, invalid edits, recovery, and imported/exported scope on a pinned deployed build. Otherwise state **UAT NOT RUN**.
- **Reuse:** an InmotionTitan-built version would be a donor *candidate*. Private `PHDK-Modules` receipt, source extraction, versioned package release, licensing, security and two-consumer portability gates require separately authorized acts under `PHDK_MODULE_LIBRARY_STANDARD.md` and `PHDK_REUSE_CATALOG_STANDARD.md`. This standard causes no downstream consumer updates.

## Acceptance examples only for enabled resources

1. Sort an allowed numeric/date column by header; combine text and range filters, navigate more than one page, maintain deterministic results and tenant-scoped totals.
2. Hide/reorder permitted columns and save a view. Neither hidden sensitive fields nor forbidden columns appear in network payloads, exports or saved view references.
3. An authorized `fields.manage` role creates a typed field, uses it in permitted form/grid views and persists its values. An unauthorized role cannot mutate definitions even by direct API.
4. Invalid row edits retain user drafts, report the precise error and do not corrupt authoritative numeric values; concurrent writes detect conflicts.
5. Recoverable changes follow domain rules and audit. Immutable resources cannot be altered or incorrectly "undone".
6. When profile is declined, original CRUD and eligible import/template/export continue to work with no extra package.

Measure actual task completion, error rates, recoverability and spreadsheet reliance in an authorized pilot. No unmeasured performance or AI-generated text percentage is an acceptance claim.
