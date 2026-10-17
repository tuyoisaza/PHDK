# PHDK Administration Console Standard

**Applies to:** every stateful portal/application with authenticated administrative operations, regardless of industry (CRM, ERP, LMS, HR, operations, commerce, etc.). A genuinely static/no-backend/no-administration product may document NOT APPLICABLE with evidence; an authenticated app may not opt out merely because its vertical differs.

## 1. Tenancy decision before architecture and UI

In Capture and on the first PHDK Preflight/Check for an existing app, discover or explicitly resolve the tenancy model in `ADMIN_ARCHITECTURE.md`:

- `single_tenant`: one organization/security domain; one application-level `admin` (or equivalent existing elevated role) owns the complete administration console. **Do not fabricate a redundant `super_admin` or tenant CRUD.** Regular users/roles are still supported.
- `multi_tenant`: multiple independent customer organizations or equivalent isolated domains; platform-wide `super_admin` owns the platform console and each tenant has `tenant_admin` or `admin` scoped solely to that tenant. No tenant admin may manage global configuration or other tenants.
- `unknown`: evidence insufficient. Recommend multi-tenant **when a plausible future SaaS/multiple-organization product justifies the isolation and operational costs**, but do not silently convert a single-tenant application or provision shared tenancy. Record tradeoffs (isolation, cost, complexity, data residency, migration) and mark DECISION REQUIRED where architecture/security changes.
- In product UX label the appropriate area **Configuración / Settings**. Its tabs depend on tenancy and active features. Apply exactly one platform administrative authority: `super_admin` for multi-tenant, `admin` for single-tenant, with equivalent abilities appropriate to the app. Tenant admins receive a deliberately narrower tenant-scoped console.

Existing names/paths may be mapped through `ADMIN_ARCHITECTURE.md`; enforce semantics and behavior instead of requiring literal identifiers. Support multi-membership only with explicitly verified active-tenant context.

## 2. Mandatory navigable configuration surface

An authenticated, server-authorized administrator must have a persistent, discoverable **Configuración** navigation entry (such as `/admin/settings`) with a usable tabbed/sectioned console, responsive layout, keyboard and screen-reader navigation, per-tab permissions, deep links, validation, save/errors/loading/empty states and accessible translations. A mocked UI or decorative toggles never count as implementation. Group related screens if tabs would become unwieldy, but preserve discoverable sections and routes.

**Core required sections for every applicable app:**

| Section | Required end-to-end capabilities |
| --- | --- |
| General & localization | Application name, native/default locale and supported translations, timezone, formats, organization preferences, safe global defaults, relevant business rules; persist and reflect changes. |
| Users & invitations | List/search/detail, create/invite, assign roles and authorized tenant membership, deactivate/reactivate, revoke sessions/invitations, documented deletion/anonymization policy, audit. Invite tokens must expire and be single-use. |
| Roles & permissions | Role/type-of-user CRUD for permitted custom roles, immutable protected system roles, permission matrix by resource/action/scope, role defaults at creation/onboarding and safe inheritance. Server-side deny-by-default enforcement; never allow self-escalation or last-platform-admin removal. |
| System & integrations | Environment-safe nonsecret settings, debug ENABLED/DISABLED (privileged, with production-safe constraints), configured integrations/provider status, validated nonsecret provider configuration, feature flags, change audit. Secrets/API keys appear as presence/last-rotation plus masked replace/rotate/revoke controls, **never reveal plaintext values**, store in a secrets manager/provider facility, never in ordinary application config tables, source, logs, browser payload or prompt definitions. |
| Security & audit | MFA/SSO policy where supported, session policy, access denials and critical events, admin/audit history with actor/tenant/time/action/result and redaction, authorization review, anomaly alerts, export subject to permissions/retention. Audit events must resist alteration. |
| Backups & recovery | Protected backup inventory/status/scope/retention, restore plan and drills, restore authorization, tested tenant-aware restore boundaries where applicable; show evidence and health. Never add a destructive one-click restore/delete without preview, approval and rollback/retention controls. |
| Operations & monitoring | Application health, relevant error/usage/traffic/cost indicators, observability integration status, actionable failure states; active connectors/configuration for applicable analytics tools as separately approved. |
| Visual templates | Shared semantic design tokens for **claro, oscuro y corporativo** through one centralized token/theme source. Enable/disable corporate theme without hard-coded page colors; preserve contrast, rollback, preview and effective selection by scope. Follow `PHDK_THEME_STANDARD.md` and `PHDK_DESIGN_SYSTEM.md`. |

**Multi-tenant-only platform sections:** Tenants (create/list/detail/edit, activate/suspend/archive, safe deprovisioning and controlled deletion); each tenant's admins, users/memberships, allowed features/entitlements, quotas/limits, subscription/status if applicable, default locale/theme, default role permissions, tenant-specific integration policy, data retention and tenant-scoped backup/export where justified. A new tenant starts from an explicit versioned least-privilege template, not uncontrolled copying of platform super-admin privileges. Tenant admin console shows only its own tenant's permitted sections.

**Conditional sections:** `Prompts`, AI consumption and models are mandatory **if and only if** the project uses actual AI workflows under `AI_ADMIN_STANDARD.md`; payments/billing, notifications, webhooks, domains, analytics/Clarity, compliance or data residency appear when genuinely applicable. Do not create empty fake modules merely to satisfy a menu inventory.

## 3. Safe administrator role / user-profile switching

On multi-tenant apps a `super_admin` may enter an explicit, limited **Ver como / Test as** session for an existing authorized synthetic test user (or specially designed server-enforced scoped test identity) with a selected tenant and role, including public/newly registered, member, admin and relevant custom roles. On single-tenant apps the application `admin` has the equivalent allowed role-test facility. Requirements:

- Authenticated elevated actor, step-up MFA for sensitive cases when applicable; server-created short-lived scoped session; actor, target, tenant, reason, start/end/expiry audit, unmistakable banner and **Return to admin** control.
- The effective session **reduces** privilege to the selected role; it is never a client-only role flag, forged JWT claim, direct tenant-ID selector or permission bypass. Sensitive writes and side effects must be explicitly blocked or isolated to demo fixtures. Do not impersonate a real user without consent/authorization.
- Switching must not reveal secrets or disable MFA. Explicitly test server/API denies while switched, tenant boundaries, stale memberships, expiry and return flow. Any change made as a test user remains attributable to the originating administrator.

Follow `UAT_JOURNEY_STANDARD.md` and the optional Company Co fixture for safe test personas.

## 4. Isolation, access policy and data lifecycle

- Authorize every operation server-side at resource/action/record/tenant scope. Tenant context comes from verified identity + current membership, not caller-controlled `tenant_id`. Apply isolation consistently to queries, RLS or equivalent database boundary, storage/blobs, cache keys, search, jobs/queues, exports, backups, prompts and telemetry. Deny cross-tenant access and test IDOR/privilege escalation.
- RBAC is the baseline; supplement with ABAC/relationship rules where record ownership, department and tenant context demand it. Version permission templates and prohibit custom roles granting platform-global capabilities. Minimize PII and logging retention.
- Destructive actions (tenant deletion, restores, mass account removals) require impact preview, backup/retention awareness, strong confirmation, appropriate dual authorization where policy requires it, audit, retry/rollback strategy and **separate explicit permission for live production data**. Prefer suspend/archive with safe retention over irreversible hard delete.
- Secrets are never part of a generalized settings CRUD API. Protect secret mutation with dedicated authorization and logging of metadata only. Use least-privilege provider/service identities and revocation/rotation.
- The same API enforcement applies when navigation, tab or button is hidden. Unauthorized requests fail closed.

## 5. Canonical prompt/agent registry and execution graph (AI only)

Extend `AI_ADMIN_STANDARD.md`: a Prompts entry is a **catalog of executable workflows**, not merely editable text. For each agent/prompt show:

1. Stable ID, friendly name, purpose/business outcome, owning feature, page/route/action where invoked, enabled status, owner and revision.
2. Declared inputs with **names, types, required/optional, source** (approved database table/view/field or API/event/user input), transformations, scope and sensitivity; inspect mapping metadata without exposing actual confidential records.
3. Separate versioned personality/system layer and execution/task instructions with template variables; provider/model, safe parameters, fallback, guardrails and tool/data access allowlist.
4. Expected output JSON Schema (parse and schema validation **before use**), examples/test fixtures with redacted data, error/timeout/retry path, validation failure policy.
5. Next hop(s): return to product/UI, persist to authorized destination, enqueue permitted job, or feed the **named following agent**. Show input/output field mappings, DAG/graph edges, conditions, termination, cycle/recursion guard and cost/time budget. No unbounded autonomous execution.
6. Execution history with trace ID, actor/tenant (when applicable), agent ID+revision, provider/model, latency, tokens/cost, validation status, destination, errors and redacted payload visibility; manual test with synthetic inputs, publish/rollback revision and regression tests.

Manage edges and source definitions as structured, referentially validated records or an equivalent typed registry. Do not allow arbitrary SQL, arbitrary credentials, arbitrary agent tool permissions, or unreviewed cross-tenant data flow through an admin form. Runtime must enforce the **published** version, approved input scopes, output-schema validation, transaction/idempotency rules and tenant boundary. Reject unsafe graph edits and route secret-bearing configuration to a proper secret manager.

## 6. Artifacts, implementation and acceptance

Required project evidence for every applicable app:

- `ADMIN_ARCHITECTURE.md`: selected tenancy, trust boundaries, UI/routes, roles and inheritance, exact backend authorization mechanisms, tenant isolation and approved exceptions.
- `ADMIN_CAPABILITY_MATRIX.md`: each required/conditional section, admin authority, tenant_admin/user/public visibility, create/list/detail/update/delete and action-level scope, backend API/DB location, existing implementation path, test file, PASS/GAP/UNVERIFIED/N/A.
- `ADMIN_SETTINGS_REGISTRY.md` or typed runtime configuration registry: setting key, classification (secret/nonsecret), owner, scope, default, validation, storage backend, permission, audit, propagation/rollback policy.
- When AI applies, `AI_WORKFLOW_CATALOG.md` or structured registry documenting agent IDs, input sources, outputs, graph edges and runtime callsites; no actual secrets, personal data or confidential prompts in public evidence.
- Updated `CRUD_MATRIX.md` and UAT role/case evidence; never replace these with self-attested checkboxes.

Before scaffolding, **inspect the existing stack, auth, database, roles, routes, settings, prompts and admin screens**; extend existing primitives idempotently instead of installing a duplicate second admin panel. Build missing actual UI/API/schema/security/tests by workstream, adapting to product architecture. Do not create a fake fully-working scaffold or mark PASS based on generated files alone. Report unknown external credentials, real backup provider or infrastructure as EXTERNAL/BLOCKED, without inventing readiness.

### Check/Auto repair protocol

- `PHDK check` audits all sections and source/behavior evidence and reports categorized gaps; it does **not** mutate product implementation during the audit. Missing admin UI, protected endpoints, tenant model, locale/config, safe user simulation, settings/agent registry, audit or tests count as GAP when applicable.
- `PHDK check --fix` (also `PHDK check fix` / a plain Check followed by explicit `sí, ejecuta los gaps`) is a **single explicitly authorized audit-and-remediation run**: audit → freeze enumerated fixable gaps → implement stack-specific missing parts → validate → rerun Check → versioned branch/PR/merge and verify remote main per normal delivery contract. Do not auto-decide tenant conversions, production data migrations, new secrets, destructive live changes or new security policy where user intent is unresolved.
- Under an authorized `PHDK auto` goal, approved applicable gaps are fixed in scope without repeated ceremonial user sign-off. Missing implementation is never repaired by adding only this Markdown standard to the downstream project.
- UAT must verify navigable screens and real backend effects, both permitted and forbidden requests, cross-tenant isolation, prompt schema errors/edges, role-test session lifecycle and restore safeguards. No browser PASS without permitted execution evidence.
- Block closure for Critical/High authorization, isolation, privilege escalation, secret leak, unsafe restore/deletion and invalid output-to-action paths. Other applicable missing functionalities remain GAP or BLOCKED; no false ALIGNED.

## 7. External baseline and design rationale

- OWASP Multi-Tenant Security & Authorization Cheat Sheets: tenant-scoped identity, deny by default, isolated database/cache/storage/queues, per-resource authorization.
- OWASP Secrets Management & Logging Cheat Sheets: masked metadata-only secrets operations, scoped access, protected audit trails.
- PostgreSQL Row Security Policies: RLS can help isolation but requires attention to owner/bypass policies and is not universally portable.
- OpenFeature evaluation context: use verified subject/tenant context to evaluate feature flags.
- OWASP AI Agent and MCP Security guidance: scoped agents, tool allowlists and explicit boundaries.

References:
- https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html
- https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
- https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
- https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
- https://www.postgresql.org/docs/current/ddl-rowsecurity.html
- https://openfeature.dev/specification/sections/evaluation-context/
- https://owasp.github.io/DevSecOpsGuideline/2-Process/2-2-Develop/2-2-5-AI-Agent-and-MCP-Security/
