# PHDK Browser Configuration Standard

## Intent and precedence

PHDK separates **external service configuration** from **application verification**. A browser is a permitted administrative transport for an identified development dependency, not an implicit test runner. Apply this standard with `EXECUTION_SCOPE.md`, current owner instructions, actual host/connector permission and security controls. The owner controls documentary PHDK restrictions, not access that the host or provider has not granted.

## Commands and scope

| Invocation (case-insensitive; trim surrounding whitespace) | Behavior |
|---|---|
| `PHDK browser on` | Enable browser-assisted **external configuration** for the presently identified authorized project/goal; do not expand the authorized provider, action or spending scope. |
| `PHDK browser allow` | Exact alias of `PHDK browser on`. |
| `PHDK browser off` | Immediately disable non-UAT browser-assisted configuration in the current scope. Preserve independent source work and already-authorized UAT rules. |

**Default:** non-UAT browser operation is OFF unless the owner explicitly requests the relevant external configuration or invokes `PHDK browser on` for a currently identified goal. A direct request such as "create/configure the accounts and integrations necessary for Xenia Charis" authorizes browser assistance for that *identified configuration task* without requiring the exact command; it is not a standing browser-on policy. `on` alone does not grant new account/provider-write authority when no configuration goal or target has been authorized. Natural-language stop/revoke instructions are equivalent to `off`; a later specific owner instruction may create a new scoped grant.

This command is a **conversation-scoped policy instruction**, not an executable browser tool or persistent service toggle. It lasts only for the active goal and conversation, ending with `off`, owner stop, goal completion or conversation end (whichever comes first). Record the grant's source, target, operations and disposition in the existing TASK/AUTO_STATE or workstream status when those records are in use, **without storing a reusable activation flag**. Do not auto-resume it from a repository, older conversation or upgraded managed block. Configuration work remains synchronous/in-session.

## What the exception permits

Only for the owner-authorized project and named/necessary external service dependencies, an already-available, host-permitted browser, browser MCP or equivalent UI automation may:

- Navigate a third-party administrator/developer console to create or configure approved project accounts, apps, workspaces, OAuth clients/redirect URIs, domain/DNS records, integrations, authorized repository/hosting settings or environment configuration.
- Complete ordinary account onboarding and copy/paste configuration values via legitimate UI, subject to the provider's terms, account ownership, role limits and required confirmation. Prefer existing authorized accounts and least privilege; avoid duplicates.
- Read back saved settings or non-sensitive provider status needed to show that the intended configuration was actually applied, recording timestamps, target, redacted change summary and evidence.

**Authority is action-specific:** merely enabling the browser is not consent to create accounts, change production configuration, alter security policies, grant broad permissions, buy subscriptions, incur charges, move data, or deploy. A current specific request to configure accounts/integrations can authorize *necessary, bounded, non-billed* setup consistent with that goal; uncertain high-impact, destructive, security-sensitive or billable actions need the owner's distinct, informed authorization. Normal existing login/MFA/CAPTCHA/connector consent remain human/provider-controlled; never evade them or ask for passwords, recovery codes, cookies or tokens to be pasted into chat. Never expose or persist secret values in task logs, screenshots, commits or reports. Use official provider UI/API where already authorized; no covert credential extraction.

## Explicit non-permissions

- **No product browser testing:** do not navigate the project's running application to validate UI, login, journeys, API behavior, accessibility, responsiveness, screenshots or acceptance. Those are `PHDK uat` / `PHDK uat fix` only. A configuration editor's own saved-state confirmation is **CONFIGURATION_VERIFIED**, never UAT PASS or deployed-product behavior evidence.
- No Playwright/Puppeteer/Cypress/Selenium browser tests, local preview servers, local app/database runtime, Docker, arbitrary live-app probes or test fixtures from this exception.
- No unlimited browsing, monitoring, background jobs, third-party automation purchases or access to unrelated accounts and projects. Do not perform user impersonation, privilege escalation, tenant boundary bypasses, unsolicited messaging, real payments or real-customer record mutation.
- `PHDK browser off` does not cancel an independently and explicitly initiated UAT phase; UAT retains its own narrowly bounded browser readiness and synthetic-data controls.

## Operating sequence and evidence

1. Confirm current owner mandate, project, provider, requested/necessary actions, and whether `on` or a task-specific equivalent is active; distinguish **browser channel availability** from permission and from authentication. If the target/action is not identifiable, ask one essential question; proceed with independent work.
2. Classify the UI operation as `EXTERNAL_CONFIG` versus `PRODUCT_UAT` or unrelated browsing **before opening a page**. Use the least-privilege existing authorized session; do not circumvent host consent or provider protections.
3. Perform the bounded authorized configuration, stopping for actual identity verification or separately required sensitive approval, not for repetitive routine browser permission prompts. Keep independent source/plan work moving.
4. Inspect only the provider's own configuration readback, capture sanitized evidence, and record `CONFIGURATION_APPLIED`, `CONFIGURATION_UNVERIFIED` or `BLOCKED` per action. Configuration readback does not mean app runtime works.
5. Close disposable sessions and avoid lingering elevated privileges. End the grant with the task/conversation or `off`; report outstanding access or external steps concretely. No background retries.

## Decision examples

| Situation | Outcome |
|---|---|
| Owner asks an agent to set up an existing OAuth client and callback URI for the current product | Browser-assisted provider configuration permitted if connected; verify provider-saved URI; product login remains UAT NOT RUN. |
| Owner says `PHDK browser on` while developing an already specified provider setup | Permit navigation for that scoped setup; no general product browsing or extra provider actions. |
| Auto tries to click through the app to see if registration works | DENIED until explicit `PHDK uat`, even with browser ON. |
| Owner says `PHDK browser off` mid-configuration | Stop browser configuration immediately; do not delete partial approved settings blindly; report saved/unsaved state. |
| Provider requires MFA, paid upgrade or owner-controlled domain transfer | Respect the external gate; never bypass, purchase or assume approval. |
