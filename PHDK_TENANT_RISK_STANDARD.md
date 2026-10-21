# PHDK Tenant Risk Management and Isolation Standard

**Scope:** all products with existing, planned or plausible multi-tenancy; single-tenant products record NOT APPLICABLE to cross-tenant controls while retaining ordinary security/privacy duties. This standard is consulted during Capture, Plan, Auto/implementation, UAT Prep, UAT and Check. Read with `ADMIN_CONSOLE_STANDARD.md`, `DEVSECOPS.md` and `PHDK_PRODUCTION_VERIFICATION.md`.

## 1. Outcome and decision authority

Protect each tenant as an independent security boundary across all data and execution paths. A request authenticated to tenant A must not read, infer, update, delete, export, restore or trigger actions against tenant B's information. Encryption does not substitute for authorization or separation; "military-grade" is not a technical assurance level or certification.

**Risk assessment is mandatory; architecture selection is consultative and proportional.** Do not impose a dedicated database, per-tenant KMS key or dedicated infrastructure on every project. Instead assess exposure and impact, show credible alternatives with costs, recommend a level and get the owner's decision for material architecture, provider spend, data movement or residual-risk acceptance. Maintain non-negotiable baseline protections at every level. The chosen architecture may exceed the recommendation; a weaker choice requires an explicit, recorded risk owner/exception and cannot waive essential tenant isolation or applicable law/contract.

Prefer the least complex design that demonstrably meets the risk and isolation requirement. A changing threat model or sensitivity can require escalation; never silently migrate live data, provision databases/services, change provider IAM/KMS or incur new spend.

## 2. Consultative discovery: evidence first, one question at a time

Start from existing requirements, database model, auth/tenant membership, roles, architecture, traffic/exposure, data classifications, customer contracts, applicable regulation, existing cloud protections, incident history and provider capabilities. Mark each fact `OBSERVED`, `OWNER-CONFIRMED`, `INFERRED` or `UNKNOWN`, with a source. Do not ask the owner to repeat known information. Avoid lengthy questionnaires and generic security interrogations.

Resolve only material unknowns; when needed ask **one focused question, wait for its answer, then ask the next**. Start with the highest-uncertainty exposure/sensitivity issue, e.g. "If one customer's data leaked to another customer, what kind of information would be exposed: public, internal business, personal, financial/health, or highly restricted?" Then, only as needed:
- **Exposure and actors:** private/internal, selected partners, internet-facing/self-service, APIs/webhooks, untrusted tenants and third-party integrations.
- **Blast radius:** number/size of tenants, likely cross-tenant reach, downstream AI/search/exports/backups and harmful side effects.
- **Impact:** confidentiality, integrity, availability, fraud/safety, reputational and contractual loss, recovery time.
- **Requirements:** jurisdictions/data residency, retention, contractual audit or key ownership, sector regulation, certifications actually required.
- **Constraints:** existing stack and controls, acceptable downtime, recovery objective, migration complexity, operating budget and operational expertise.

Do not request actual secrets, personal records or confidential customer content in chat. Do not invent legal obligations, claim compliance or assert zero risk. If exposure cannot be resolved, provisionally rate conservatively and identify the missing owner decision.

## 3. Explainable risk rating

Record **inherent risk** before proposed controls and **residual risk** after them:
- `likelihood` (1 rare through 5 very likely), informed by external exposure, tenant trust, attack surface, historical failures and control quality.
- `impact` (1 negligible through 5 severe), using the **highest** credible confidentiality/integrity/availability, legal, customer or systemic impact, not an average.
- `score = likelihood × impact` as a discussion aid, not a substitute for a threat model.
- **R1 Low (1–4)**, **R2 Moderate (5–9)**, **R3 High (10–16)**, **R4 Critical (17–25)** are provisional bands. Explicit legal/contractual requirements, highly sensitive data, credible systemic blast radius or severe adversarial exposure may raise the tier irrespective of arithmetic; document the override and confidence.
- Record principal threat scenarios (especially cross-tenant IDOR, tenant confusion, compromised administrator/service principal, cache/object/search/AI leaks, restore/export leakage and data-key compromise), evidence and assumptions. Never "score down" an unknown to make it convenient.

Provide owner with the recommended tier, rationale, two feasible architecture options where possible, protection/cost/operability tradeoffs, implementation dependencies, residual risks and the precise decision requested. Once approved, enter date, owner, tier, accepted alternative/exception, review trigger and controls into `TENANT_RISK_ASSESSMENT.md` and `ADMIN_ARCHITECTURE.md`. If a material decision is pending, continue safe independent tasks, mark `DECISION REQUIRED` and do not implement an irreversible tenancy migration.

## 4. Baseline controls — required for every multi-tenant tier

1. **Verified context, least privilege and deny-by-default.** Derive tenant scope from authenticated server-validated identity and active membership, not user-supplied tenant IDs, JWT edits, headers or UI state. Enforce authorization on each resource/action/record and all APIs (including admin, GraphQL, background, internal and integration paths). Tenant administrators cannot gain platform-wide roles. A platform superadmin is not an unconditional default reader of tenant content; exceptional access is purpose-bound, time-limited, least-privilege and audited.
2. **Data-layer defense in depth.** Every tenant-owned table/record is scoped and operations fail closed. On PostgreSQL shared tables, prefer enforced RLS with non-bypassing request roles, transaction-scoped tenant context and documented policies. Never run tenant request paths as superuser, owner or `BYPASSRLS`; address `FORCE ROW LEVEL SECURITY` where relevant. If another data store or proven isolation boundary is used, document equivalent independent enforcement and tenant-negative evidence. An untested `WHERE tenant_id = ...` convention alone is not sufficient proof.
3. **All surfaces.** Partition cache keys/session namespaces, search/vector indexes and retrieval results, object-storage paths/permissions/signed URLs, jobs/queues/notifications, analytics, exports, logs, AI prompts/tools/memory and backups. Explicitly authorize cross-tenant platform analytics and return only data authorized for that purpose; default-deny cross-tenant joins. Restrict service-to-service identities and propagation of tenant context.
4. **Transport, storage and secrets.** Use supported TLS for connections carrying tenant data; encrypt sensitive persistent data and backups at rest with provider-supported encryption, verifying real configuration rather than assuming it. Keep keys and credentials outside source, logs, user-visible configuration and prompts in an approved KMS/secret manager with scoped access and rotation/revocation procedures. Do not use homemade cryptography. Store passwords with a suitable password-hashing function (e.g. Argon2id), not reversible encryption.
5. **Operations.** Minimize sensitive data, redact telemetry, protect audit integrity, enforce retention/deletion policy, make exports/restores and cleanup tenant-aware, record access denials, and have an incident containment/recovery process. Backups must be encrypted and restore boundaries verified. No unscoped production delete or restore.
6. **Verification.** Provide positive/negative role tests and cross-tenant read/write/list/detail/search/cache/file/export/AI/job cases relevant to the product, including stale or switched membership, suspended users and direct object-ID attempts. Treat leakage, bypassed authorization and plaintext secret exposure as Critical/High acceptance blockers. Record real evidence; code inspection and unexecuted tests remain UNVERIFIED.

## 5. Recommended architecture by assessed risk (not rigid infrastructure mandates)

| Tier | Default recommendation | Escalate when warranted |
| --- | --- | --- |
| **R1 Low** | Shared database/schema with demonstrably enforced tenant scope (e.g. PostgreSQL RLS), shared infrastructure, baseline encryption and tenant-aware services. | Add stronger partitioning if privilege boundaries or restore/export scope cannot be demonstrated. |
| **R2 Moderate** | Baseline + hardened policy tests, robust tenant-aware storage/cache/jobs, enhanced audit and incident controls; shared DB with RLS may remain suitable, or schema/database separation if recovery, contractual or blast-radius needs warrant it. | Per-tenant database or separate service identities if tenant isolation risk cannot be managed in the shared model. |
| **R3 High** | **Recommend** tenant-dedicated database and scoped database credentials, stronger workload/storage segmentation, isolated backup/restore, managed KMS and per-tenant data keys/key boundaries where feasible and justified. Consider approved application/field encryption for high-value secrets or particularly sensitive fields. | Require stronger separation if regulated handling, active adversarial customers, targeted compromise or incident impact demands it. |
| **R4 Critical** | **Recommend** dedicated tenant infrastructure/security domains, database, workload/network controls, scoped IAM, separate managed key boundaries, strict privileged access, recovery/incident drills and independent security assurance aligned with the real threat model. | Contractual/legal controls and qualified external review may be necessary. No "military-grade"/certification claim without independent evidence. |

Shared vs dedicated options must distinguish **logical isolation, administrative privilege isolation, cryptographic isolation and infrastructure isolation**. A separate database without separate credentials/access is not a complete isolation guarantee. Separate encryption keys reduce some blast-radius risks but do not fix an application authorization bug that decrypts for the wrong tenant. Select the narrowest sufficient combination of defenses, verify provider capabilities and quantify cost/operations before authorizing changes.

### Encryption escalation decision

Always protect tenant traffic and sensitive stored data/backups. For data requiring extra protection (e.g. high-impact personal/medical/financial fields, tenant-controlled secrets, contractual key segregation), assess authenticated field-level encryption (such as a supported AEAD implementation using AES-256-GCM), envelope encryption with KMS-managed key-encryption keys, key per tenant, separation of duties, key rotation/revocation and recoverability. These are **conditional** controls—not universal directives to encrypt every column or buy KMS. Account for search/indexing, accessibility, backup restore, key loss, audit and performance. Never implement encryption merely as a UI toggle; never store a key next to its protected data or expose plaintext in logs/AI prompts. Do not use reversible encryption for passwords.

## 6. Lifecycle contract and decision gates

- **Capture:** detect single/multi/unknown; inspect exposure and sensitivity, interview only unresolved material risks one question at a time, and produce/update the provisional `TENANT_RISK_ASSESSMENT.md` for applicable multi-tenant plans, with explicit unknowns, owner decisions and requirements links. For a true single-tenant project, record N/A with evidence.
- **Plan:** record threat model, inherent/residual tier, options and cost tradeoff, chosen/awaiting decision, key and isolation design, data residency, migrations, recovery, acceptance criteria and implementation workstreams in `ADMIN_ARCHITECTURE.md` / `MILESTONE_PLAN.md`. Materially different live architecture must not be silently chosen by Auto/Force.
- **Implementation/Integration:** implement the agreed baseline and tier-specific controls in actual product code/config without creating unapproved services, databases, KMS resources, credentials, provider writes or new spend. Preserve existing sound controls and record deviations/risks.
- **UAT Prep/UAT:** prepare only permitted synthetic tenants/personas/records, following the current overriding `PHDK_PRODUCTION_VERIFICATION.md` (no local behavioral or in-process testing, Docker, new staging/databases). Test tenant boundaries only against authorized deployed production with uniquely owned synthetic records, scoped negative requests and automatic audited cleanup; **never probe or mutate real tenants' records**. No new infrastructure for a test. Unavailable safe test evidence is BLOCKED/UNVERIFIED, not PASS.
- **Check:** compare observed backend enforcement/configuration, assessment approval and evidence against the agreed tier and baseline; report GAP, Critical/High, DECISION REQUIRED or UNVERIFIED rather than demanding an unjustified high-cost tier. `PHDK check` remains read-only; approved `check --fix` may repair authorized code gaps but not make new provider/architecture/security acceptance decisions.
- **Review triggers:** new personal/sensitive data category, internet exposure, new API/AI integration, tenant-count/blast-radius growth, security incident, jurisdiction/contract change, provider/key design change or material architecture migration. Reassess after such changes; do not schedule background monitoring without owner authorization.

## 7. Required assessment record — `TENANT_RISK_ASSESSMENT.md`

Keep it compact and updated in the existing project's repository; do not put actual sensitive data in it:

| Field | Required content |
| --- | --- |
| Product/revision/owner/date | Scoped product; decision owner and review date |
| Tenancy and data | Source-backed model, sensitivity categories and tenant classes |
| Exposure and threat scenarios | Audience, attack paths, blast radius and assumptions |
| Evidence/confidence | Observed/confirmed/inferred/unknown with source links |
| Inherent risk | Likelihood 1–5, impact 1–5, score, tier and overrides |
| Options and recommendation | At least one viable option (prefer two), benefits, residual risks, cost and operational impacts |
| Approved control profile | Isolation, RLS/equivalent, identity, storage/search/AI, TLS/at-rest/field crypto, key management, backups, audit and remediation work |
| Residual risk and decision | Re-estimated likelihood/impact/tier, decision/exception, owner and approval state |
| Verification and next review | Evidence paths, tests/UNVERIFIED, unresolved blockers, explicit review trigger |

Avoid claiming the score is a NIST-certified method or that any architecture makes cross-tenant compromise impossible. For legal/regulated environments seek qualified interpretation of the specific applicable requirements.

## References

- OWASP Multi-Tenant Security: https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html
- OWASP Cryptographic Storage: https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html
- OWASP Key Management: https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html
- PostgreSQL Row-Level Security: https://www.postgresql.org/docs/current/ddl-rowsecurity.html
- NIST Cybersecurity Framework 2.0 (risk governance context; not a source for PHDK's invented score bands): https://www.nist.gov/cyberframework
