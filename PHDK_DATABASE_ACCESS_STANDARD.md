# PHDK Scoped Live Database Diagnostics Standard (v4.1.0)

## Purpose and trigger

This is a **procedure, not a PHDK command, test profile, or lifecycle stage**. When the owner's **current authorized development, incident, investigation, or data-focused task** genuinely needs existing live database state (schema, migration ledger, counts, configuration records, a specific scoped fact), an agent may perform **bounded read-only diagnostics** without first invoking `PHDK uat` or asking for redundant permission. Inspect available source, migrations and provider non-secret metadata first; connect only when that evidence cannot answer the task. General code work, automatic Preflight/Check, a past permission, an alert, and an Auto session alone do not justify opportunistic live database browsing. If the environment or actual data scope is material and unclear, ask one targeted question. Honor more restrictive current owner/host/security rules.

This exception applies to **data inspection only**. It does not initiate UAT Prep, UAT, UAT Fix, acceptance/API/browser testing, migration execution, seeding, runtime health probing, product writes, backup/restore, provider administration, account/role creation or recurring access. Even a developer's request to "configure the DB" must be separated into permitted reads and independently authorized writes. `PHDK auto force` never expands this boundary.

## Before connecting — authorization, target and privileges

1. Record the concrete question and minimum evidence needed, repository, provider, project, **environment** (production/staging/development), database/service, affected tenant if any, and relevant release/schema revision. Never guess which environment a URL or variable targets.
2. Verify the current task's owner authorization and the active agent's legitimate provider/database access. A tool's installation, a URL, or possession of a password is **not** authorization. Production reads require an identified relevant production target and appropriate data rights; ambiguous target, protected categories or cross-tenant exploration require specific owner clarification/approval.
3. **Prefer an existing scoped read-only database role** with only the required schema/table privileges and tenant controls. Read-only transactions are defense in depth, **not** substitutes for database authorization, RLS, or field-level access. **Practical constrained fallback:** if an existing owner-authorized Railway/Postgres connection exposes only a privileged role, an agent may inspect **schema, migration metadata and narrowly targeted aggregate counts only** under a deliberately read-only transaction, after confirming the specific target, task authorization and data/tenant scope. Tag the session `ELEVATED_DIAGNOSTIC`, use an explicit approved tenant predicate for tenant data, never inspect sensitive/user rows, never call application functions, and disclose this elevated-credential risk. This is **not** equivalent to least privilege and grants no admin action. If secure session restrictions, tenant authorization or sensitivity cannot be established, stop and request a safer preconfigured read-only identity rather than treating admin credentials as unrestricted access.
4. Use an existing approved secret delivery mechanism (provider session/CLI injection, secured local environment, or connected authorized credential tool). Read only values essential to connect when genuinely available and permitted. Never request passwords in chat, print `DATABASE_URL`, place credentials in shell arguments, logs, tool transcripts, screenshots or repository files, or create new secrets/accounts as a diagnostic workaround.

## Connection order — choose the least invasive working transport

1. **Existing private authorized connection or ephemeral tunnel** to the identified DB from an already-approved execution context, if actually supported by the available tools. No new hosted worker, persistent service or SSH key is implied.
2. **Railway/PostgreSQL baseline:** where Railway CLI and a legitimate project session are available, prefer Railway's documented `railway connect postgres --tunnel-only` capability and explicitly select/verify the target environment and service. Run a supported short-lived foreground connection/client, avoiding new public exposure. A `railway run` environment variable does not itself make a Railway private hostname reachable from the local machine. Re-check the current provider documentation and actual CLI support rather than guessing flags.
3. A **pre-existing, authorized, TLS-verified external endpoint** may be used with the same read-only role if the private/tunnel path is unavailable and current owner policies permit it. Verify endpoint identity and TLS; do not disable certificate verification or accept an unknown/self-signed certificate blindly. An owner-authorized certificate/CA pin may be used where necessary.
4. Creating a **new public TCP proxy**, firewall exception, database user, SSH key, deployment, paid connector or any provider-setting write is **not part of this read-only permission**. A temporary Railway TCP proxy is an exceptional separately and **explicitly** authorized external-configuration operation for the named service/environment/port; examine deployment/availability impact, preserve its original state, minimize duration and verify removal. A cleanup promise does not authorize creating it. Never delete or reconfigure someone else's pre-existing access.

If no safe authorized path exists, stop with `DIAGNOSTIC_BLOCKED` and a concrete access gap. Do not fall back to raw data export, speculative scripts, broad credential extraction, SSH improvisation, public exposure or unauthorized alternative tools.

## Query discipline — PostgreSQL default

- Prefer `information_schema`, limited `pg_catalog`, migration metadata and aggregate counts. Query actual rows only when necessary to answer the specific request, with an appropriate tenant/business predicate, a narrow column projection and a finite row limit (**default 50 rows maximum**). Never do `SELECT *`, full-table dumps, sensitive profile discovery, cross-tenant enumeration or open-ended paging.
- Use a **read-only DB role** and a **read-only transaction**, with short statement/lock/idle timeouts. Example for a known safe query; parameters and target-specific filtering must be supplied securely:

```sql
BEGIN READ ONLY;
SET LOCAL statement_timeout = '5000ms';
SET LOCAL lock_timeout = '1000ms';
SET LOCAL idle_in_transaction_session_timeout = '30000ms';
SELECT COUNT(*) FROM app_table WHERE tenant_id = $1;
ROLLBACK;
```

- Keep a finite diagnostic budget (normally **at most 10 narrowly scoped statements**, with no loops, polling or costly full scans). Never execute DDL, DML, `CALL`, arbitrary SQL functions with side effects, `EXPLAIN ANALYZE`, `COPY`, migrations, seeds, `pg_sleep`, locks or changes to grants/roles/configuration. **A SQL `SELECT` is not automatically safe**: inspect functions/views/query plans and privileges where risk exists. Read-only transaction does not prevent every external side effect of an unsafe function.
- Minimize personal/regulated/secret data; default to column names, counts, redacted examples or presence indicators. No unrestricted PII, tokens, authentication materials, credentials, payroll/payment details or customer exports. If those are essential, seek a specifically authorized privacy-safe route rather than expanding the read.
- For another SQL/database engine, use its **equivalent** scoped credentials, transaction isolation, read-only enforcement and time/row budgets; do not blindly run PostgreSQL syntax.

## Closeout and evidence

Always roll back the diagnostic transaction, close the client and foreground tunnel, and verify that no temporary privilege/network exposure was left behind. If a separately authorized temporary provider change was made, verify restoration against the captured original state; failure is `ACCESS_CLEANUP_BLOCKED` with the real risk and exact remediation owner. Do not assume successful cleanup from an exit code alone.

Report `DIAGNOSTIC_READ_COMPLETE`, `DIAGNOSTIC_READ_PARTIAL`, `DIAGNOSTIC_BLOCKED`, or `ACCESS_CLEANUP_BLOCKED` with the target (no secrets), task purpose, scope, connection class, privilege level, bounded query count, timestamps, sanitized findings and verified cleanup. Distinguish observed database state from source assumptions and deployment/application/UAT success. Preserve no dumps or result sets by default; redact retained task evidence.

## Integration and authority

- `EXECUTION_SCOPE.md` authorizes this narrow **non-UAT read-only diagnostic**; `technical_stack.md` supplies the PostgreSQL/Railway baseline. This standard is manifest-vendored to downstream projects and routed by active AGENTS/SKILL/native instructions.
- `PHDK_TEST_AUTOMATION_STANDARD.md` **local profile stays hermetic/offline**. This exceptional read-only investigation is not a local test-runner check and cannot be smuggled into a hook, background script or `PHDK test` profile. Real acceptance tests and test-owned synthetic mutations still require explicit UAT under `PHDK_PRODUCTION_VERIFICATION.md`.
- Current owner/host rules, least privilege, privacy, provider-write authority, production security and explicit UAT boundaries prevail. Merely upgrading PHDK does not connect to a database, access credentials, modify a provider or grant additional external permissions.
