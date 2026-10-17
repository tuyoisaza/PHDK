# PHDK CRUD and Resource Administration Standard

## Normative requirement
Every application with persisted, manageable business entities MUST inventory its resources and evaluate Create, Read (list and detail), Update and Delete individually for each role and exposure surface. Administrative interfaces, especially Superadmin, default to complete authorized management capability, not read-only tables with inaccessible records. A CRUD gap must be fixed or have a documented, evidence-backed exception. CRUD is a capability audit, NOT a command to expose unsafe operations to every role.

## Scope and classification
Inspect database models, APIs, routes, menus, tables, public catalogs, dashboards, admin and superadmin screens, integrations and existing access policy. Include entities already listed without detail navigation, entities manageable only by API, and public listings that imply a legitimate user workflow. Do not invent CRUD for computed dashboards, audit logs, third-party read-only mirrors, immutable financial/legal events, append-only records, security-sensitive resources or content explicitly not owned by the application. Document read-only/append-only/soft-delete alternatives, rationale and authority.

## Mandatory capability matrix
Maintain `CRUD_MATRIX.md` for applicable projects, with one row PER resource × role × surface and columns: resource, owner/source, route/list entry, C, R-list, R-detail, U, D, authorized vs forbidden, field/record scope, API/backend enforcement, UI affordance, deletion policy, evidence, exception rationale and status. Status: PASS, GAP, BLOCKED, NOT APPLICABLE, DECISION NEEDED. Identify bulk actions and export separately if relevant; never silently conflate list with detail or archive with hard delete.
Default recommendations:
- Superadmin: full authorized C/R/U/D for first-party mutable resources, including a functional record-detail view; record restrictions for secrets, audit integrity, legal retention, irreversible transactions and tenant isolation.
- Admin/operator: only actions within explicit domain responsibility, tenant and record ownership; deny by default elsewhere.
- Authenticated end user: own/authorized records and product-specific workflows only.
- Anonymous/public: usually read-only public fields; suggest create/update/delete only when an explicit public workflow (submission, self-service, community content) is justified, with abuse protection and moderation.
Do not expose secret credentials, protected personal information or system internals merely because a role can list an entity.

## Configuración and tenant-scoped administration CRUD

Apply `ADMIN_CONSOLE_STANDARD.md` for every app with administrator-managed state. Treat users, invitations, custom roles, permission templates, tenant/membership records (multi-tenant), managed nonsecret settings, provider connection metadata, themes and prompt/agent definitions (AI only) as explicit managed resources. Add their C/R-list/R-detail/U/D or justified limited-action rows to `CRUD_MATRIX.md` and `ADMIN_CAPABILITY_MATRIX.md`. Immutable built-in roles, external secret values, historical audit records, backups and irreversible tenant deletion require action-specific protected controls; never fabricate dangerous generic delete or read-secret operations. Require server-side role/record/tenant scope and authorization-negative tests. Platform super_admin exists only in multi-tenant; in single-tenant use the corresponding elevated admin.

## Behavioral acceptance requirements
For each authorized operation, ensure end-to-end implementation: discoverable navigation; list/search/filter/pagination as suitable; opening an individual record; usable create/edit form with defaults and validation; clear save/error/loading/empty states; deletion or archive with confirmation, impact explanation and recovery where feasible; consistent data refresh; API endpoint and persistent storage; audit event for consequential administrative mutations. Access checks MUST run on the server for resource and record/tenant scope; hidden buttons are not authorization. Use least privilege, CSRF protection where applicable, anti-enumeration defenses, safe error handling, concurrency protection where applicable, and hard/soft delete/retention decisions. Forbidden operations must fail at the API too.

## Lifecycle enforcement and evidence
- Capture: inventory user roles, managed resources and intended operations; classify genuine uncertainty without inventing requirements.
- Plan: produce the capability matrix, role/permission contract, exception decisions, implementation tasks and traceability. A listed admin resource without an accessible detail action is a GAP unless the exception is justified.
- Implementation/Integration: implement each approved operation end-to-end; reconcile UI, API, backend policies and persistence. Document migration/backfill risks and irreversible actions.
- UAT/UAT Fix: test each allowed C/R-detail/U/D and each forbidden operation, including role isolation, tenancy, empty/error states, update persistence, delete/recovery, denied API calls and regressions. Use real browser evidence when available under UAT rules, otherwise BLOCKED/MANUAL rather than PASS.
- Check: compare current code, routes, policies and tests to `CRUD_MATRIX.md`; fail applicable incomplete admin management flows and missing record-detail routes; issue prioritized remediation. Exceptions must be justified and testable.
- Auto: include gaps in scope accounting and downstream handoff; no DONE if committed CRUD deliverables or relevant PRs remain unfinished.
Snapshot `CRUD_MATRIX.md` with Plan and UAT/Check handoffs when applicable.

## Minimum regression cases
1. Superadmin opens a listed record and views details; allowed edits persist after reload.
2. Authorized creation appears in list and detail; validations and failed writes are visible.
3. Authorized delete/archive has confirmation and coherent post-action state; restricted deletions stay disabled/denied.
4. Admin from tenant A cannot read/update/delete tenant B via direct URLs or API IDs.
5. Public anonymous user sees only approved fields and cannot mutate via direct API.
6. Read-only or immutable resource has documented exception and server-side denial; not an invented delete button.
7. UI lists and API operations return appropriate loading, empty, invalid, conflict and permission-denied states.

## Exit criteria
PASS requires coverage for every applicable resource-role-surface combination, functional Read-detail wherever relevant, backend authorization tests and explicit justified exceptions. Missing evidence is BLOCKED, not assumed complete. Avoid universal hard-delete mandates and avoid generating permissions solely from UI appearance.
