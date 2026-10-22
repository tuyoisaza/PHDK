# UAT Browser Readiness and Cost Guard

## Mandatory scoped UAT entry gate

Execute at **every entry** into explicit `PHDK uat`, explicit `PHDK uat fix`, or a retest authorized within an active explicitly initiated UAT run. Auto, Auto Force, PMO and Designer Mode alone do not activate acceptance or this browser gate. Execute **only inside those UAT phases**, not during Prep, generic development, Plan, Check, provider diagnosis or Delivery. Follow `UAT_STANDARD.md`, `PHDK_PRODUCTION_VERIFICATION.md`, `EXECUTION_SCOPE.md` and the host's higher-priority access controls.

**Permission is not connectivity.** At UAT entry announce: **Navegador UAT: permiso de fase ACTIVO; acceso real PENDIENTE DE VERIFICAR.** The PHDK rule already authorizes a connected/available browser for actual user acceptance testing in that bounded phase; no extra PHDK owner approval is needed. It does not install, connect, authenticate, or grant a browser tool and cannot override host consent or explicit owner restrictions.

### Entry sequence

1. **Discover, do not assume.** Inspect the current runtime/tool inventory for an already-connected browser, permitted browser MCP/Computer Use, or an existing local Playwright/Cypress/browser runner. Registry entries, available code libraries, and old screenshots do not prove real access. Prefer an existing suitable channel with **no new service purchase**; do not repeatedly install tools or provision infrastructure.
2. **Verify actual access in UAT only.** Use an already authorized tool to perform a harmless navigation to the permitted candidate's public/login page. Record a real response, sanitized screenshot/trace, or actual tool error with timestamp, target, stage and revision. Do not declare `AVAILABLE_VERIFIED` without that evidence. If a host connection or consent is needed, explain the **one specific user action** to connect it; never claim to have obtained access while pending.
3. **Check target and safe identities.** Verify that the existing deployed production revision and target match current Integration/deployment evidence, and that role-based actions use only authorized uniquely run-owned synthetic identities and data. A URL alone does not establish either permission or isolation. Prove exact ownership, allowed operations, tenant limits, expiry and cleanup before writes. Real users/data, payments and destructive actions remain excluded. A browser grant does not authorize provider configuration writes, purchases, credential exposure or MFA bypass.
4. **Proceed or isolate.** Run browser-dependent stories when the tool and safe target are actually available. If not, mark each unexecuted browser case `BLOCKED`/`MANUAL`, **never PASS**, and continue independently permitted source review and non-browser/API acceptance on the same authorized deployed candidate. Do not run local unit/in-process tests or request new spend as a browser workaround. Auto development remains independent of this optional UAT run. Retry a blocked case only after the relevant access change; close browser sessions and verify synthetic cleanup after UAT.
5. **Report and resume.** If a genuine connection, role login or environment blocker remains, give one minimal non-secret owner action, exact resume cue and affected case IDs. On return, re-verify access, retest those cases and update the existing UAT evidence without restarting already completed cases.

### Strict no-unplanned-spend rule

**UAT never implies approval for new spending.** Never fabricate a budget ceiling, demand blanket cost authorization, buy credits, call a paid API, subscribe to a browser farm, provision billed testing services, enable metered external tools, dispatch GitHub Actions or deploy new infrastructure to replace missing browser access. Do not propose a spending cap as if it grants browser permission. Existing product hosting/connected tools may incur ordinary costs: do not claim a $0 total or cost savings without billing evidence. If use of an already-connected metered service would cause *new* charges outside existing authorization, do not use it. Ask for explicit authorization only for an independently necessary **actual product** paid dependency with grounded price/scope, mark that case `DECISION REQUIRED`, and continue unrelated UAT. Unavailable browser access is a **capability blocker**, not a financial approval gate.

### Required evidence

Create/update a **Browser Readiness** section of `UAT_ACCESS_REPORT.md` and mirror its summary in `UAT_REPORT.md` for each scoped entry/re-entry, recording:

- stage, run, candidate revision, exact URL/environment and timestamp;
- permission `ACTIVE_UAT_EXCEPTION` separately from runtime capability `AVAILABLE_VERIFIED`, `UNAVAILABLE`, `HOST_CONNECTION_REQUIRED` or `NOT_NEEDED`;
- selected channel, real harmless operation evidence or redacted error; no invented screenshots;
- target type, synthetic/test data safety, role access and case IDs affected;
- spend disposition `NO_NEW_SPEND`, `PAID_DEPENDENCY_EXCLUDED`, or `EXISTING_AUTHORIZED_SERVICE` (billing remains UNVERIFIED unless inspected);
- executed cases, BLOCKED/MANUAL cases, independent work performed, specific one-step owner action and exact retest cue.

After verification say **Navegador UAT: permiso de fase ACTIVO; acceso real VERIFICADO / NO DISPONIBLE / REQUIERE CONEXIÓN.** Never call UAT ACCEPTED with outstanding required browser evidence. The next-action contract of `UAT_JOURNEY_STANDARD.md` applies. This rule does not authorize browser use in any other phase or bypass host connection requirements.


## Production-first verification override (v2.58.0)

**Mandatory:** Apply [PHDK_PRODUCTION_VERIFICATION.md](PHDK_PRODUCTION_VERIFICATION.md). Owner-authorized production-only UAT supersedes earlier local unit/in-process/runtime testing, staging-only identity, and blanket production-test prohibitions. Local operations are limited to static analysis, lint, typecheck and safe builds; Docker, local runtime tests and separate staging/databases are prohibited. UAT must use existing versioned production deployment and existing database, strictly scoped run-owned synthetic identities/records, audit, automated cleanup and verified revocation on success, failure and interruption. Never touch real data or bypass existing security hooks; a conflicting gate is BLOCKED.
