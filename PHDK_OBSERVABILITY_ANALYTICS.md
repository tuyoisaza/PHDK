# PHDK — Observability, Analytics & Behavioral Monitoring Standard

Status: Proposed standard. Applies to greenfield and brownfield repositories. Owner decisions are explicit; no external resource is provisioned without authorization.

## Principles
1. Distinguish **technical observability** (application/backend reliability), **product analytics** (GA4), and **behavioral analytics** (Clarity). They are separate opt-in decisions.
2. During Capture, inspect existing telemetry, monitoring, analytics, consent mechanisms, hosting, and superadmin capabilities before recommending duplication.
3. During Plan, recommend all applicable capabilities and record adoption choices: ENABLED, PLANNED, DECLINED, EXISTING, NOT_APPLICABLE, or BLOCKED_EXTERNAL. Never infer approval from running `PHDK auto`.
4. If an existing monitoring server/platform is available, ask for provider, endpoint, environment, allowed protocols, auth method, retention requirements, and who manages it. Do not request passwords in chat or commit secrets.
5. If none exists, propose a self-hosted OpenTelemetry-compatible destination first (initial recommendation: self-hosted Grafana OSS + Prometheus + Loki + Tempo with OpenTelemetry Collector or Grafana Alloy, after checking infrastructure, capacity, maintenance, TLS, backups, updates, access controls and retention; Grafana Cloud and other managed vendors are secondary alternatives, never default). Explain operating cost, privacy/data residency, retention, and maintenance. Wait for affirmative choice before account creation, vendor connection, provisioning or any billable change.
6. All configurations must be per environment; development/test telemetry must not contaminate production analytics. No service silently enabled merely because an identifier exists.
7. In applications with Superadmin, expose integrations as a standard configuration module. If none exists, document a configuration owner/flow rather than adding a full Superadmin solely for analytics.

## Discovery questions — ask one at a time if not already answered
1. Is an observability/monitoring server or SaaS already in use?
2. If yes, what provider and connectivity/protocol are available? If no, shall we use the recommended self-hosted stack, choose a managed service, or defer?
3. Should GA4 be enabled? If yes, what is the web data stream Measurement ID (`G-...`)?
4. Should Clarity be enabled? If yes, what is its Project ID?
5. Which consent/CMP, geography, data classification, retention and roles apply? Discover from the project first.

## Technical observability implementation contract
- Instrument server/API/background jobs with OpenTelemetry where supported: traces, metrics, structured logs (or log correlation), service.name, deployment.environment, version, request/correlation/trace IDs, error outcomes and endpoint latency. Avoid high-cardinality or personally identifying attributes.
- Support OTLP endpoint, exporter transport, sampling, service name, auth from server-side secret store, resource labels, timeout and graceful failure. Use collectors/agents where appropriate; do not expose privileged OTLP credentials to browsers.
- Establish availability checks, error rate, latency p95/p99, traffic/throughput, saturation/resource metrics, dependency failures, and job/queue failures appropriate to architecture. Define SLOs where useful, with responsible alert destination and escalation owner.
- Alerts must be tested with synthetic failure or safe test events. Logging-only does NOT count as monitoring. Suppress sensitive values, authorization tokens, request payloads and unnecessary PII; document retention and access policy.
- In Superadmin: show provider, environment, configured/missing status, last successful signal ingestion if verifiable, dashboard link, test connection/action implemented server-side, safe status diagnostics and redacted error details. Secrets are write-only, masked and access-controlled; changing them is audit logged.
- If declined, do not install collectors or exporters. Lightweight local diagnostic logging may remain part of baseline engineering.

## Google Analytics 4 implementation contract
- Recommend for applicable web products, never activate without owner approval and required privacy configuration.
- Superadmin: enabled toggle, Measurement ID (`G-...`), domain/environment applicability, consent/CMP status, validation status, and safe verification instructions. A measurement ID is a public identifier, NOT an admin API key.
- Install Google tag once; handle SPA route changes explicitly and prevent duplicate page_view events when enhanced measurement and manual routing overlap.
- Define and document a restrained event taxonomy aligned with PRD funnels: signup_completed, login_completed, search_performed, lead_submitted, checkout_completed or domain-relevant equivalents. No passwords, free-text inputs, emails or other PII in events.
- Implement Consent Mode v2 as applicable: analytics_storage, ad_storage, ad_user_data and ad_personalization; default to denied where required, capture user choices with a CMP and honor changes/withdrawal. Prefer blocking before consent where appropriate.
- Verification must include network/DebugView or equivalent evidence for pageviews, route transitions, chosen business events, and consent-denied behavior. Mark external validation blocked if property access is unavailable; never claim success from script presence alone.

## Microsoft Clarity implementation contract
- Recommend on applicable user-facing web applications, independent of GA4. Superadmin: enabled toggle, Project ID, environment scope, consent status and test/verification indicator.
- Install exactly once via official supported integration. Verify recordings/events/heatmaps in the real Clarity project when authorized; script installation alone is not proof of data arrival.
- Enable appropriate masking, avoid session recording of highly sensitive workflows and data by design, prevent PII in custom tags/identify calls. Do not capture passwords, tokens, payment details, health records, private messages or admin secrets.
- Synchronize consent state with the site's CMP; respect denial and withdrawal, including Microsoft Clarity consent signals and cookie behavior as required by visitor jurisdictions. Do not assume GA4 consent automatically configures Clarity without verifying integration.
- Define optional custom events for UX funnels only after approving an event taxonomy.

## Common Superadmin information architecture
Settings → Integrations → Monitoring & Analytics
- **Observability:** Enabled; Existing / Self-hosted / Managed provider; OTLP endpoint; connection test; health/alerts/dashboard; server-side masked credential management.
- **Google Analytics:** Enabled; Measurement ID; consent state; verify installation; visit dashboard.
- **Microsoft Clarity:** Enabled; Project ID; consent state; verify installation; visit dashboard.
- All have independent saving, environment scoping, role restrictions, audit history and explicit clear/disconnect. Never expose private tokens in API responses, browser bundles or verbose/copy-all debug logs.

## Lifecycle enforcement
- **Preflight/Capture:** inventory existing integrations and identify consent/security constraints. Record adoption questions, owner responses and inventory in `MONITORING_DECISIONS.md`.
- **Plan:** describe architecture, costs, retention, dashboards and tasks in `OBSERVABILITY_ANALYTICS_PLAN.md`; trace requirements to acceptance cases.
- **Implementation:** add adapters and Superadmin fields only for approved integrations, automated tests and config documentation; no vendor lock-in to a single telemetry backend.
- **UAT:** browser-based test consenting and declining, route transitions, tracking isolation, access controls, masking, duplicated events, exporter outages, connectivity, and alert paths. Evidence in `MONITORING_UAT_REPORT.md`.
- **Check:** report individual states for each integration; fail an approved integration that is unverified, misconfigured or leaking private data. A deliberately declined capability is a recorded decision, not a compliance failure.
- **Delivery:** attach `MONITORING_HANDOFF.md` with provider/owner, endpoints (not secrets), operational dashboard links, test evidence, alerts, consent design, retention, open blockers and cost exposure.
- Historical stage handoffs must snapshot these documents under the active `docs/phdk/lifecycle/<run-id>/` folder and verify predecessor outputs before advancing.
- No disabled or externally blocked capability should prevent unrelated safe lifecycle work; never mislabel unverified tracking as PASS.

## Acceptance checklist
- [ ] Inventory and all three owner decisions recorded independently.
- [ ] Existing monitoring platform reused or proposed provider explicitly accepted.
- [ ] Service instrumentation produces correlated telemetry; real ingestion verified.
- [ ] At least one actionable alert is exercised and owner/route documented.
- [ ] Superadmin controls exist where the product has Superadmin; secret handling audited.
- [ ] GA4 pageviews and non-PII business events verified, without duplication.
- [ ] Clarity session/event visibility and sensitive-field masking verified.
- [ ] Consent deny/accept/withdraw tested for both vendors where applicable.
- [ ] Production and development telemetry segregated.
- [ ] Evidence artifacts, blockers and user decisions are carried into Check and Delivery.

## Default provider decision (owner approved 2026-10-12)
- Prefer reuse of an already deployed compatible observability stack.
- Otherwise recommend **self-hosted Grafana OSS + Prometheus + Loki + Tempo**, instrumented through OpenTelemetry Collector or Grafana Alloy, as the first option.
- Evaluate CPU/RAM/storage, expected telemetry volume, retention, TLS, access, backups, alert routing, ongoing operations, and estimated infrastructure costs before offering deployment.
- If self-hosting is unsuitable, offer managed alternatives such as Grafana Cloud; require explicit acceptance before provisioning.
- Never install or expose a telemetry endpoint until hosting destination and operational ownership are authorized.

## Primary references (reviewed 2026-10-12)
- https://opentelemetry.io/docs/collector/deploy/agent/
- https://grafana.com/products/cloud/
- https://developers.google.com/tag-platform/security/guides/consent
- https://support.google.com/analytics/answer/10000067
- https://learn.microsoft.com/en-us/clarity/setup-and-installation/consent-management
- https://learn.microsoft.com/en-us/clarity/setup-and-installation/cookie-consent
- https://clarity.microsoft.com/blog/npm-integration/
