# PHDK Hook Compatibility Remediation Standard

## Intent and authority

All PHDK commands that deliver code, including Auto and Auto Force, MUST inspect the effective pre-commit/pre-push hooks and package-script command graph before executing a potentially incompatible test. PHDK Check MUST classify the same mismatch early. This applies to Husky, native Git hooks, package-manager scripts, repository-scoped validation scripts and vendor-managed instructions. Use `PHDK_PRODUCTION_VERIFICATION.md` as the runtime boundary: local lint, static format/type checks, safe static analysis and compilation/builds are allowed; local application behavior tests (`pnpm test`, Vitest, Jest, unit/in-process/integration runtime suites), Docker, local servers and databases are prohibited.

## Required discovery

1. Identify the effective Git `core.hooksPath`, installed hook directory, hook command chain, package scripts, and any mandatory local or remote checks. Inspect actual command definitions; names such as `check`, `build` or `lint` do not prove safety.
2. Determine provenance from tracked source, history, owner instructions and existing repository security/branch rules. Record `PHDK-MANAGED`, `LEGACY-PHDK`, `OWNER-OWNED`, `EXTERNAL/REQUIRED` or `UNKNOWN` with evidence; never assume an unknown hook is PHDK-owned.
3. Detect local behavioral test commands even if nested or indirectly invoked by `pre-push`, `prepare`, `build` or a wrapper. Distinguish static gates, commit/version checks, secret scans, security gates, lint/typecheck/build and genuine behavior tests.

## Authorized reconciliation

- Within an already authorized implementation/Auto goal or `PHDK check --fix`, automatically repair **proven PHDK-managed or legacy PHDK-generated** hooks and scripts that violate production-first verification. Replace the prohibited behavior-test invocation with equivalent permitted static checks, preserving the rest of the hook and every existing version/branch/commit/secret/security control. Do not remove the hook, disable it, use `--no-verify`, alter protection or change external CI/provider settings.
- For an owner-owned hook, preserve it unless the owner specifically authorized that hook change; a generic Auto/Force command is not permission to weaken an independent project control. For external/required or unknown provenance, preserve it. Record the exact conflict and required authorization, mark push/delivery BLOCKED if the actual gate prevents publication and continue independent permitted work.
- If a hook mandates a prohibited local test, NEVER execute it as an exception to satisfy the hook. A test-only gate is not automatically security-equivalent to static checks: report the lost behavioral coverage without claiming a test was run. Replacing a proven PHDK-owned legacy test command does not authorize acceptance or create a new delivery prerequisite. In Auto/Force record `UAT NOT RUN` and `DEFERRED — OWNER OPT-IN`; obtain production acceptance evidence only after explicit `PHDK uat` under `UAT_STANDARD.md` and the production-first policy. Preserve independent owner/external security and required-check controls; if an actual control prevents delivery, report that concrete conflict rather than silently relaxing it.
- Write and inspect the full proposed diff. Validate edited hooks **statically** for retained commands/structure, script references and allowed execution boundary. Execute only safe permitted checks. Do not bypass failed hooks; if required controls genuinely reject delivery, report their actual evidence and stop only that operation.
- All changes follow normal branch, version bump, reviewable PR, merge and remote-`main` verification.

## Check/Auto outputs

Check must report `HOOK_COMPATIBILITY` as COMPLIANT, AUTO-FIXABLE, BLOCKED/DECISION REQUIRED or UNVERIFIED, including path, effective commands, provenance, conflict, kept security gates, changes made and verification limits. Bare `PHDK check` remains audit-only; `PHDK check --fix`, approved Check remediation, Auto and Auto Force perform authorized fixes. Auto must inspect compatibility before push to avoid surprise approval prompts, and may repair discovered proven PHDK-generated mismatches immediately; it must not ask the owner to authorize a local runtime-test exception prohibited by policy.
