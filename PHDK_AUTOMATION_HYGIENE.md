# PHDK Automation Hygiene and Cost Guard

## Mandatory applicability

Every `PHDK check` (including the final Check inside `PHDK auto` and `PHDK check --fix`) must audit whether PHDK-originated automation, agents, reloaders, scheduled work, or deployment triggers persist in the project. This gate applies to every GitHub-backed project; Railway-specific checks apply only where Railway is connected. Do not label this NOT APPLICABLE because `.github/workflows/` is absent: remote state must still be evaluated where access exists.

**Baseline:** PHDK executes only during an explicitly authorized interactive conversation. PHDK itself never requires persistent GitHub Actions, scheduled update agents, background workers, hosted CI, bot PRs, polling, deploy-loop scripts, Railway cron jobs, or recurring reloads. An existing product-owned feature or owner-required security check is not presumed PHDK-owned. Normal GitHub-connected Railway autodeploy is allowed and must be preserved unless the owner expressly changes it.

## Required inspection — two independent evidence planes

1. **Repository inspection (read-only):** inventory `.github/workflows/*`, Dependabot/Renovate configuration, `.github/agents/*`, other bot/agent instructions that launch work, `package.json` start/deploy/worker scripts, startup commands, cron/scheduler definitions, Docker/Procfile files, `railway.json`, `railway.toml`, Railway environment overrides, watch paths, restart policy, and any script that polls, hot-reloads, re-runs workflows, auto-commits, auto-pushes, or redeploys. Inspect actual executable wiring, not just filenames. The vendored `scripts/phdk_automation_audit.py` is an optional fast **static evidence collector**, not the full gate: run it from the product root when available.
2. **Live metadata inspection (read-only, permitted connection only):** inspect GitHub's workflow inventory including state (`active`, `disabled_*`), recent runs/failures/cancellations, scheduled events, checks and required branch/ruleset protections; identify installed bot/app or webhook activity only when authorized metadata endpoints are available. For Railway projects inspect each connected service/environment's GitHub deployment branch, autodeploy setting, Wait for CI, watch paths, cron schedule, restart policy/max retries, pending/skipped/failed deployments, repeated restarts, and available usage/cost trends. Do not retrieve secrets, execute workflows, re-run jobs, trigger deploys, change provider settings or claim to have inspected a UI without evidence.

**Critical distinction:** a checked-in workflow file does not prove GitHub has enabled it. Conversely, missing workflow source does not prove no active or orphaned remote configuration exists. A Railway `watchPatterns` filter, healthcheck, or normal bounded `ON_FAILURE` restart is not intrinsically a gap. `Wait for CI` may leave deployments waiting on a stalled GitHub Actions check; establish actual check-suite linkage before recommending a change. Preserve valid product CI, branch protections and deployment dependencies.

## Risk classification and decisions

| Finding | Required disposition |
| --- | --- |
| Proven PHDK-created scheduled/recurring workflow, agent, bot or source-driven redeploy loop without a current authorized use | GAP, High (Critical for material costs or blocked delivery); AUTO-FIXABLE / FIXABLE WITH VALIDATION for safe repository code removal |
| Active GitHub Actions job repeatedly failing/queued, Railway Wait for CI waiting on a nonfunctional required check, or Railway cron/restart storm | GAP/PARTIAL, High; distinguish safe source repair from EXTERNAL / MANUAL provider remediation |
| Existing CI/security workflow, intended product scheduler, healthy autodeploy or bounded restarts | COMPLIANT only with requirement/owner rationale plus actual configuration evidence |
| Unknown workflow provenance or consequences of disabling it | UNKNOWN / DECISION NEEDED; never delete because its name looks suspicious |
| Unable to inspect GitHub Actions or Railway remote state | UNVERIFIED, not COMPLIANT; provide exact access/evidence required without guessing |
| No GitHub/Railway integration or schedule by established architecture | NOT APPLICABLE for that provider only, with evidence |

## Required Check report section: Automation and Cost Hygiene

Record: repository/commit + access limitations; each automation's file/path and provider identifier, trigger, schedule, current enabled state, last runs/status, PHDK/product/unknown owner, purpose, GitHub check or Railway deployment dependency, potential cost/blocker, recommended action, exact validation, and compliance status. Include counts of active/disabled/unknown workflows, active recurring triggers, suspected crash/redeploy loops, and unverified provider surfaces. Provide links to GitHub workflows/runs and Railway service/deployment where available. Never invent monetary savings without actual billing evidence.

At final Check, require explicit evidence that **no unauthorized PHDK-originated automation remains active**, that intended GitHub-to-Railway delivery is still wired correctly, and that there is no unexplained Wait-for-CI/cron/restart loop creating repeated builds or charges. If evidence is unavailable, keep the overall Check **ALIGNMENT INCOMPLETE** and identify the owner/provider action.

## Remediation and authorization

- Bare `PHDK check` is read-only except for its authorized report. It must never disable workflows, cancel runs, uninstall apps, alter GitHub rules, change Railway settings or delete source.
- `PHDK check --fix`, an approved Check remediation, or in-scope `PHDK auto` may remove clearly obsolete, PHDK-owned **repository source/configuration** only after mapping dependencies and preserving required CI/autodeploy. Run relevant local checks and rerun the audit; record before/after evidence. Do not weaken real security gates or treat an unapproved provider write as authorized by a source fix.
- External provider settings, disabling active workflows/bots/webhooks, changing Railway Wait for CI/restart/cron/autodeploy, and billing controls stay **EXTERNAL / MANUAL** or require separately supported authorization and capability under `EXECUTION_SCOPE.md`. Report exact provider location, intended setting, expected effect and validation; never pretend these actions were executed.
- If a stale PHDK artifact is the *only* blocker but its removal would impact a required check or live service, choose DECISION REQUIRED and preserve it until the dependency is resolved.

## Deterministic static collector

Run `python3 phdk-standards/scripts/phdk_automation_audit.py --root . --format json` (adjust path for direct source use). The collector uses only Python's standard library, performs no network/provider writes, emits findings with paths and lines, and always marks the remote plane UNVERIFIED. It deliberately distinguishes `REVIEW_REMOTE` from high-risk source signals; neither a clean scan nor absence of `.github` proves live-provider compliance.

References: `PHDK_CHECK.md`, `PHDK_AUTO.md`, `EXECUTION_SCOPE.md`, `DEVSECOPS.md`, `MAIN_DELIVERY_STANDARD.md`.
