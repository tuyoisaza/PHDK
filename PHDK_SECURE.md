# PHDK Secure Standard — v2.63.0

## Contract
`PHDK secure` is an explicit standalone security audit-and-authorized-remediation command. In `PHDK auto` and `PHDK auto force`, Secure is mandatory **development work**, not UAT or UAT Prep. Hybrid operation means lightweight security checks at each completed value milestone and a consolidated security gate after integration and before final Check/delivery. Security findings may require reopening implementation. Never interpret Secure as permission for UAT, penetration testing, paid scanning, external provider mutations, local behavioral tests, Docker, new environments or bypassing controls.

## Milestone checks
For each completed value milestone inspect changed source/configuration and relevant threat boundaries: secrets, dependencies, authentication/session management, server-side authorization and least privilege, tenant isolation across data/storage/jobs/exports/AI, encryption and TLS configuration, input validation and injection, SSRF/XSS/CSRF, rate limiting, logging/PII, backup exposure, supply chain and GitHub/Railway configuration. Run permitted static checks only, preserve existing independent security gates, and document applicability and evidence. Do not claim behavioral assurance from source inspection.

## Consolidated gate
After integration, assess OWASP Top 10 and relevant ASVS controls using a risk-based threat model; reconcile with `PHDK_TENANT_RISK_STANDARD.md`, `PHDK_PRODUCTION_VERIFICATION.md`, current owner decisions and actual hosting architecture. Record each finding with severity, affected asset/tenant boundary, reproducible static evidence, remediation, verification status and residual risk. Fix authorized source/config defects, repeat permitted static checks, and document unverified runtime controls for later explicitly authorized UAT. No fabricated passing tests or acceptance evidence.

## Release decisions
Critical/High confirmed security vulnerabilities block Secure clearance and final delivery until fixed or subject to an explicit, documented owner risk decision consistent with non-waivable host/security controls. An owner waiver cannot bypass technical enforcement or assert a vulnerability is resolved. Unknown/unverified is not PASS: classify its risk and report limits; absent UAT is not itself a Secure failure. Medium/Low findings require documented prioritization and ownership. Do not request routine approval in Auto Force; sensitive architecture, spending and risk acceptance still require owner authority.

## Outputs
At each milestone, record a concise security delta in the milestone handoff. For the consolidated gate, create `docs/phdk/lifecycle/<run-id>/68-secure/HANDOFF.md` and `SECURITY_REPORT.md` with scope, controls matrix, findings, remediation commits, static verification, residual risk, release decision and explicit `RUNTIME SECURITY VALIDATION NOT RUN` where applicable. Record stage in lifecycle status. Standalone Secure audits current state and fixes only within the owner's authorization; read-only invocation must not mutate code.

## Precedence and integration
Secure runs after implementation/integration, before final Check and delivery; it never enters stages 45/50/60. This standard supplements existing tenant, production-verification, Check, delivery, Auto and milestone rules. Existing owner/host controls take precedence. Load this file only at the relevant security stage or milestone rather than in every context.
