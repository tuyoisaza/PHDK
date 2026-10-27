# PHDK Starter Capability Profile

## Status

**Composition target only.** This document specifies interoperable capability boundaries for future reusable packages. It does not ship an implementation, grant download/install authority, or claim runtime verification.

Matching entries in `PHDK_REUSE_CATALOG.json` are `SPECIFICATION_ONLY` with `implementation: null`.

## Composition principles

A future starter should be assembled from independently versioned capabilities with explicit contracts. Consumers may reuse, adapt or build each capability separately; adoption of one must not force the entire stack.

Cross-cutting requirements:

- server-side authorization and tenant isolation remain authoritative;
- secrets and sensitive settings use protected storage, never client-only controls;
- audit-relevant administrative changes are attributable;
- public UI configuration uses centralized tokens/contracts rather than duplicated per-page state;
- locale/theme/prompt settings have clear ownership and deterministic fallback;
- migrations and removal paths are explicit;
- synthetic UAT tooling is opt-in and isolated from normal production identity flows.

## 1. Administration, organizations, multitenancy and roles

Target contracts:
- platform `super_admin` only when a real multi-tenant product requires it;
- tenant/organization administrators scoped to their organization;
- organization lifecycle and membership;
- server-enforced roles/permissions and negative authorization behavior;
- tenant-scoped data access with explicit isolation strategy;
- audit trail for privileged changes;
- integration with `ADMIN_CONSOLE_STANDARD.md` and `PHDK_TENANT_RISK_STANDARD.md`.

A UI-only role selector or client-side route guard is not this capability.

## 2. Synthetic identities and UAT tooling

Target contracts:
- uniquely run-owned synthetic identities and records;
- explicit role/tenant matrix;
- legitimate application/provider-issued sessions;
- expiry, cleanup and revocation evidence;
- negative-permission cases;
- audited test-as-role only when the product supports it safely.

Synthetic identities are usable only under explicit `PHDK uat prep` / `PHDK uat` authorization. They must not enable real-user impersonation, forged tokens, production authentication bypass or persistent hidden test accounts.

## 3. AI prompt administration

Target contracts:
- privileged prompt registry;
- immutable or traceable prompt versions;
- draft/publish/rollback semantics where applicable;
- model/workflow binding;
- audit history and change attribution;
- protected secrets/credentials separated from prompt text;
- compatibility with `AI_ADMIN_STANDARD.md`.

A hard-coded prompt file without administrative/audit contracts is not this capability.

## 4. Theme system

Target contracts:
- centralized semantic design tokens;
- light, dark and corporate theme variants;
- contrast/accessibility constraints;
- persisted user/organization preference with deterministic fallback;
- shared component consumption rather than duplicated local palettes;
- compatibility with `PHDK_THEME_STANDARD.md` and the selected product Design baseline.

A static visual preview or CSS fragment does not establish a reusable theme package.

## 5. Internationalization and language selection

Target contracts:
- message catalog and locale fallback;
- deterministic locale resolution;
- user/organization language preference and selector;
- server/client formatting agreement for dates/numbers where applicable;
- missing-key behavior and extraction/update policy;
- accessibility-compatible language metadata.

Internationalization adapters are stack-dependent; a reusable core must declare supported frameworks and extension points rather than pretending one adapter fits every product.

## Acceptance path for future packages

1. keep the specification stable enough to evaluate;
2. implement in a separate versioned package/repository;
3. register as `CANDIDATE`;
4. complete contract/security/license/evidence review;
5. register as `REVIEWED`;
6. prove integration in one consumer and portability in a second independent consumer;
7. record observed passing tests for the proposed version;
8. only then promote to `ACCEPTED_VERSIONED`.

PHDK does not automatically extract donors, mutate donor repositories, or upgrade consumers.
