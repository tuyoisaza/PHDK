# PHDK Continuous Improvement — in-product support and contextual feedback

Status: ACTIVE · ULEDS contract v1.0 · PHDK v4.2.0

## Mandatory always-visible entry point

For every interactive PHDK application, extend the existing single shared version/debug-actions component defined in `DEBUG_DIAGNOSTICS_STANDARD.md`. In the **top-left branding area immediately beneath the app name**, render exactly:

```text
vX.Y.Z  [clipboard]  [trash]  [🤖]
```

Preserve version text (12px, `vMAJOR.MINOR.PATCH`, no SHA/date), icon-only square controls (28 x 28px), glyph sizing (approximately 14px), 4px gap, one row, keyboard focus and effective 44 x 44px target where feasible. Order is **version → copy diagnostic logs → clear permitted cache → robot emoji**. The robot is the user-requested **literal 🤖 emoji**, not a third copy/cache status check, navigation redirect or decorative icon. Accessible name/tooltip: `Agente de soporte y mejora continua` (localized equivalent); keyboard Enter/Space opens it, with visible focus. All four elements must remain visible on public home, login, authenticated pages and admin even when debug mode is OFF; show exactly one shared instance in a region. Never hide the robot merely because AI provider or debug mode is disabled. The support panel itself applies permission and privacy rules.

Do not move, resize or duplicate the existing clipboard/trash pair. Copy/clear success checkmarks continue independently and are shown only after actual operations succeed; the robot remains a separate control. Explicit user choice overrides the older "exactly TWO buttons / no third control" contract throughout the debug standard. Source/unit tests assert four-element order, no visible helper labels, public/debug-OFF visibility, accessibility and absence of console-data leakage.

## Integration with existing diagnostics and ledger (v4.2.1)

The new 🤖 belongs to the same shared version/clipboard/trash UI component; do not duplicate it or change the 28px visible controls. Use the existing bounded, sanitized frontend diagnostics buffer to attach **references and correlation IDs only** when the user explicitly sends a ticket—never automatically upload copied console dumps, DOM fields or customer payloads. Clear Cache may reset local diagnostics/session state, but must not delete persisted `PHDK_ULEDS_STANDARD.md` events or `PHDK_DEVELOPMENT_LEDGER_STANDARD.md` decisions/tickets. A support chat ticket is a real, server-verified product-side write; this is distinct from the read-only developer `PHDK_HEAL_STANDARD.md` command. Route privileged debugging to separate authenticated admin surfaces; keep the robot's basic safe report intake working without paid LLM infrastructure.

## What robot click does

Open an accessible first-party **Continuous Improvement Support** drawer/panel anchored to the current route. The panel offers (a) `Reportar problema`, (b) `Proponer mejora`, (c) `Comentar elemento de la pantalla`, and (d) existing owned-ticket status if the user is authorized. All flows work without a paid LLM: a short, guided clarification flow plus a ticket receipt is the baseline. An actual AI assistant can be connected only after separate provider/spending/security approval; when enabled it asks **one missing question at a time**, captures clarifications, summarizes the request and requests user confirmation before submitting. It never runs code, changes roles/permissions, performs privileged queries or starts `PHDK auto`/Heal.

Contextual selection: a conscious user-triggered, cancellable "select element" mode temporarily suspends dialog, highlights eligible elements and allows pointer/keyboard selection. Prefer stable `data-phdk-component-id`/route/feature IDs (e.g. `customers.export.button`) added at design/implementation; fall back to a safe screen-level anchor. Retain logical component ID, safe route, product version, environment and pseudonymous session correlation—not raw element text, HTML, input values, screenshots or unfiltered CSS selectors. Never allow picking password, payment, health, private message, hidden/admin-sensitive or cross-tenant data areas. Restore normal focus and interaction on submit/cancel/error.

## Intake and persistence contract

Treat every user message as untrusted external content. Server validates identity/anonymous policy, writes an audit-ready `phdk.support.request` or `phdk.feedback.contextual` ULEDS event, creates/links a ticket/conversation, and returns a real persisted reference before claiming "Enviado". The UI may display a local queued/retry state but not a false receipt; provide useful fallback when unavailable. Constrain text length, message count, attachments, rate limit, abuse filtering, IP/cross-origin behavior, tenant scope and retention; mask inadvertent credentials and provide clear privacy notices/consent when required. Public unauthenticated support is allowed only through deliberately narrowed server endpoints, anti-abuse controls and public-safe status; it never reveals internal logs, roadmap, private tickets, tenant info or admin actions. Avoid storing full chat transcripts in the Development Ledger—only scoped references and minimized summaries.

The support assistant may explain publicly documented behavior or clarify a report; it must not promise a delivery date, imply automatic resolution, expose other users' requests, change an authorization rule on request, execute provider actions or treat user-supplied text as development instructions. Security requests that attempt to circumvent RBAC (e.g. "let me delete all tenants") are rejected/escalated as a security/authorization decision, not implemented as feature requests. Genuine vulnerability reports have protected private routing.

## Administration and governance

Existing admin/superadmin settings may configure categories, copy, support hours, language, assignment, role-based visibility of ticket histories, approved AI-provider integration, consent/retention, quotas and escalation. **The always-visible robot launcher and basic safe reporting remain mandatory**; disabling a paid chat model must leave a functioning non-AI reporting path. An authenticated submitter sees only their own appropriately scoped tickets, tenant admin only authorized tenant records and platform superadmin only permitted global metadata; support staff roles are explicit, least privilege, audited and not implicitly cross-tenant. A public visitor may submit and receive an opaque reference, not an unrestricted ticket lookup endpoint.

Mark support tickets `NEW` and hand them to the registry/Development Ledger triage. No chat entry directly alters code or provider configuration; promotion to `PROPOSED`/approval belongs to the authorized owner. A user request is *evidence of demand*, not product-owner authorization.

## Required tests and evidence

Hermetic component/unit/contract tests cover shared four-element widget, 28px/14px/12px/4px visual contract, accessible open/close/focus/keyboard, anonymous/login/debug-OFF, safe contextual anchor and cancel, submitted ticket receipt only after verified storage, validation/masking, anti-abuse, RBAC/tenant negative cases, no AI-provider fallback, non-blocking ingestion failure and no user-message-to-execution path. Browser/runtime acceptance is optional **explicit UAT only**. No extra polling process, unattended support agent or automatic deployment is created merely by this standard.
