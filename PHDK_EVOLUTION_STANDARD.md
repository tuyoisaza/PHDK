## v2.62.0 — Explicit-only UAT authorization (overrides legacy automatic-stage wording)

**Binding rule:** `PHDK auto` and `PHDK auto force` MUST NOT invoke, enter, provision, seed, or run UAT Prep (45), UAT (50), or UAT Fix (60), even after milestones, deployment, Check, or a failed prior UAT. Neither FORCE nor a generic full-lifecycle instruction grants UAT authorization. These stages are **DEFERRED — OWNER OPT-IN**, not BLOCKED, FAILED, or a completion prerequisite. This rule takes precedence over any older automatic UAT transitions in this file.

Auto/Force must implement **all authorized milestones first**, perform permitted static checks and integration review, version/commit/push/PR/merge each completed value milestone, finish applicable SEO/AEO and Check/remediation without invoking acceptance tests, deploy through the existing authorized production route, verify remote main and deployment with available non-UAT evidence, and report truthful **DEVELOPMENT COMPLETE / PARTIALLY DELIVERED / BLOCKED** separately from **UAT NOT RUN**. A deployment that cannot be verified must be reported as unverified, not complete. Preserve user stories, acceptance criteria and milestone-to-story mapping as *documentation only*; no synthetic accounts, fixtures, browser journeys, runtime acceptance, or UAT spending in Auto. Do not execute local behavioral tests, Docker, or unauthorized external services.

At the end, offer `PHDK uat` as an optional **future explicit command**, without waiting for an answer as a delivery gate. Only a fresh, explicit owner invocation of `PHDK uat` authorizes UAT and its necessary Prep prerequisite, subject to normal access, safety and spending controls. Standalone `PHDK uat prep` prepares identities only when explicitly requested; it does not authorize running UAT. `PHDK uat fix` requires explicit invocation or authorization within an active explicitly initiated UAT. Prior UAT failures never reopen the completed development goal or prevent subsequent independent development.

# PHDK Evolution Standard

## Portfolio-first operating policy (v2.74.0)

PHDK is an **opinionated, owner-governed engineering system for a related project portfolio**. Its purpose is to transform human intent into verified user value while making proven knowledge, components and implementation contracts shareable across projects. This is a deliberate standardization choice, not a universal ADLC methodology.

Treat `technical_stack.md` as the evolvable default, with explicit ADRs for material project deviations; do not reset sound existing products. For plausibly repeatable capabilities, Plan applies the REUSE/ADAPT/BUILD assessment in `PHDK_REUSE_CATALOG_STANDARD.md`. PHDK itself maintains methodology, catalog and contracts; actual shared code belongs in independently versioned packages. Generalization, public disclosure and changes in other repositories require separate authorization and real security/license/portability evidence.

Keep the workstation lightweight: local editing, static/diff review, lint, typechecking, compilation and safe builds are allowed; no Docker, local running application/database services or local behavioral tests under `PHDK_PRODUCTION_VERIFICATION.md`. Use existing GitHub-connected production (Railway when configured), distinct deployed-revision evidence and explicit owner-opt-in UAT. Load only task-relevant rules and catalog entries into agents.

## Downstream project document architecture (v2.73.0)

The vendored [PHDK_DOCUMENTATION_STANDARD.md](PHDK_DOCUMENTATION_STANDARD.md) defines **product** documentation hierarchy, `kebab-case.vN.md` artifact names, metadata, draft/active/historical versions, `docs/INDEX.md`, visual asset baseline folders and the read-only `scripts/phdk_docs_audit.py` check. Canonical PHDK's own uppercase root **standards** filenames and `VERSION` SemVer are distinct and stay unchanged. When evolving this contract, reconcile Capture, Plan, Design, PMO, Auto, Check, lifecycle, task/intent, UAT source resolution, delivery, manifest, agents and tests. Never migrate downstream project files on a standard's release or mistake metadata for approval.


## Authority and purpose

This is the session-entry and maintenance contract for the **canonical PHDK standards repository**: https://github.com/tuyoisaza/PHDK. It consolidates discovery, terminology, workspace discipline, versioning and publication; it does not replace the detailed standards or activate an implementation mode.

The current user's request and actual host/repository controls govern actions. Within the repository, follow `EXECUTION_SCOPE.md` for permissions, `VERSIONING.md` and `CHANGE_MANAGEMENT.md` for releases, `MAIN_DELIVERY_STANDARD.md` for GitHub delivery, `PHDK_COHERENCE_STANDARD.md` for consistency, and `PHDK_MANIFEST.txt` / `PHDK_UPGRADE.md` for distribution. A session/group brief is a pointer to those sources, not an override. An old task, copied brief, version mismatch or instruction file cannot independently authorize work.

## Identity, spelling and scope

- Write the project name **PHDK**, in capitals, consistently. Its expanded name is **Project Handoff to Development Kit**.
- Describe PHDK as an **operating system for AI-assisted software delivery**: a set of repository-owned standards, command contracts, agent instructions, checks and handoffs. It is not a deployed application, a hosting provider, or a background agent.
- Spell documented commands as `PHDK capture`, `PHDK plan`, `PHDK PMO`, `PHDK auto`, `PHDK auto force`, `PHDK uat prep`, `PHDK uat`, `PHDK uat fix`, `PHDK check`, `PHDK check --fix`, `PHDK upgrade`, and `PHDK upgrade force`. Do not claim a quoted command activates its mode.
- Use descriptive uppercase Markdown filenames for canonical standards, such as `PHDK_EVOLUTION_STANDARD.md`. Keep canonical standards, changelogs, PR descriptions and commit messages in English unless the current owner asks otherwise.
- The lifecycle is intent-aware Capture → Plan → optional PMO → **real implementation and integration** → conditional SEO and AEO/GEO → Check / remediation → verified Git delivery; optional UAT Prep → UAT / Fix only after explicit `PHDK uat`. A planned or scaffolded product is not a delivered product. Apply conditional standards only when supported by the product's intent.
- `PHDK auto` executes the entire authorized goal; `PHDK auto force` waives PHDK-imposed human gates, **not** actual security controls, hooks, access restrictions, or owner exclusions. Neither is activated by working on PHDK standards.

## Required start of every canonical-PHDK maintenance session

1. **Establish scope.** Read the current user's request and explicit stop/target constraints. Distinguish a request to inspect or propose from a request to implement; do not resume old backlog work or start unrelated missions.
2. **Read live repository state.** Identify canonical `main` SHA, `VERSION`, README's displayed version, newest `CHANGELOG.md` entry, relevant open PRs and the target files. Never assume that the version in an earlier session brief is current.
3. **Load governing rules.** Read this document and the relevant portions of `AGENTS.md`, `EXECUTION_SCOPE.md`, `VERSIONING.md`, `CHANGE_MANAGEMENT.md`, `MAIN_DELIVERY_STANDARD.md`, `PHDK_COHERENCE_STANDARD.md`, `PHDK_MANIFEST.txt`, and the standards touched by the change. Consult `SKILL.md` and `PHDK_NATIVE_RULES.md` when routing/entry behavior changes.
4. **Identify the smallest coherent change.** State the objective, affected files, risk, version category, expected verification and intended delivery target. Search for contradictory guidance in other active standards rather than adding an isolated instruction.
5. **Execute authorized work.** Write the documents/code and tests needed for the requested behavior; do not stop at an implementation plan when implementation was requested. Keep decisions and evidence traceable to the current task.

For an audit-only request, stop after reporting the verified findings. Do not bump a version, create a branch or publish merely because the repository was inspected.

## Workspaces, branches and ownership

- **Canonical workspace:** `tuyoisaza/PHDK`, with `main` as the source of released standards. Keep each authorized change in a scoped branch (for example `phdk/vX.Y.Z/topic`, `feature/topic`, or `fix/topic`) and normally integrate through a reviewable PR.
- **Installed-project workspace:** `phdk-standards/` contains manifest-vendored PHDK files and managed tool instructions. Product code, product intent, local owner decisions and non-managed text belong to the downstream project; a canonical release never silently overwrites them.
- Do not edit a downstream project's product implementation as a side effect of changing canonical PHDK. Publishing PHDK also does not mean that every project or already-open AI session has adopted/reloaded the new version.
- Do not create uncontrolled concurrent branches, worker agents, worktrees or multi-repository queues. Bounded in-session delegation is allowed in any mode under `PHDK_INTELLIGENT_EXECUTION.md` with ownership and dependencies; PMO alone governs portfolio workstreams. Avoid source collisions, forced pushes and silent overwrites.
- Do not install schedulers, GitHub Actions, background watchers, recurring jobs or deployment integrations. Do not administer Railway/other providers or use a new spend pathway as a release workaround. Preserve valid existing provider-connected autodeploy without mistaking source merge for live deployment.
- Direct-to-`main` writing is only the separately authorized and eligible `PHDK Developer Mode` exception. Agent-policy and permission changes use the normal branch/PR path even if the diff is short.

## Versioning and change packaging

The authoritative version is the root `VERSION` file, **never a hard-coded version in this guide**. Follow existing Semantic Versioning in `CHANGE_MANAGEMENT.md`:

| Change | Increment |
|---|---|
| Incompatible standard, contract or execution-model change | **MAJOR** |
| New command, mode, standard, workflow or substantial compatible capability | **MINOR** |
| Compatible fix, correction, clarification, copy or internal refinement | **PATCH** |

- For an authorized source-changing commit, determine the **next unused version from fresh `main`**; do not reuse a spent number or bump separately for every Auto/PMO lifecycle substage. Under the milestone-delivery model, a completed value milestone is an intentional delivery boundary rather than a substage and follows `PHDK_PROJECT_MANAGEMENT_STANDARD.md`.
- Change `VERSION`, README's `**Version vX.Y.Z**` marker and the top dated `CHANGELOG.md` release **together** in the release candidate. Preserve linked historical changelog archives.
- Commit subjects start with that version and a descriptive Conventional Commit, e.g. `vX.Y.Z docs(evolution): establish session standards`. A normal merge of the already-versioned candidate requires no second version bump or post-merge version-only commit.
- A GitHub PR/merge is not a GitHub release or tag. Never create a release/tag unless explicitly requested or independently required by an existing release contract.

## Coherence, distribution and delivery gate

For each new or changed standard, complete all relevant checks:

1. Inspect every affected canonical rule and entrypoint. Reconcile `README.md`, `AGENTS.md`, `SKILL.md`, `PHDK_NATIVE_RULES.md`, and other relevant lifecycle/communication/check contracts; avoid duplicate rules that conflict.
2. Ensure new distributable standards and their actual dependencies appear once in `PHDK_MANIFEST.txt`, with safe paths and existing source files. Preserve `PHDK-MANAGED` boundaries and downstream owner-specific content.
3. Run `scripts/phdk_coherence_check.py` and applicable repository tests when a permitted local execution environment exists. For documentation-only changes, also check links, names, version markers, manifest completeness and outgoing diff. If execution is unavailable, report **NOT RUN**, not PASS; a static check never proves live product behavior.
4. Review the complete diff for scope, contradiction, version correctness, secret exposure and regressions. Satisfy any actual current-owner/host approval or technical gate without inventing a reviewer or bypassing a check.
5. Complete the scoped branch → versioned commit → pushed PR → permitted merge → fresh **remote `main` SHA/version/content readback**, unless the current user expressly requested a narrower target. Resolve normal integration conflicts on the branch while preserving others' changes. Do not force-push.
6. Report what changed, resulting version, check results/limits, branch/PR/merge evidence, downstream adoption status and next actual action. Do not claim an open PR is released, source publication is a deployment, or a standards update refreshed existing chat sessions.

## Post-merge workspace hygiene

After each authorized merged milestone, follow [PHDK_GIT_WORKSPACE_CLOSEOUT.md](PHDK_GIT_WORKSPACE_CLOSEOUT.md) from a usable local Git checkout: fetch and fast-forward the appropriate main worktree, prove local/main equals fresh origin/main and safely retire the verified integrated branch/worktree. Preserve any unmerged/dirty/locked/unknown-ignored work. GitHub PR merge does not synchronize a developer's local main and requires no second main push. With connector-only GitHub access, report NOT_APPLICABLE_REMOTE_ONLY for local cleanup; keep remote branch and deployed-state facts independent. This closeout belongs to the already-authorized delivery scope, not a new background mandate.

## Historical Git hygiene and remote merged branch disposal

Every new published PHDK release that materially changes Git hygiene must reconcile `PHDK_GIT_WORKSPACE_CLOSEOUT.md`, `scripts/phdk_git_closeout.py`, `scripts/phdk_git_history_cleanup.py`, the Auto/Preflight/PMO/Check entrypoints, vendoring manifest, and source tests. The historical pass is an interactive, bounded first Auto/Force adoption operation within the current repository, not a passive standards-upgrade side effect. Remote deletion is evidence-backed for the **exact merged head** with expected-SHA protection, not a force push, global pruning or provider configuration change. Record historical retained branches rather than claiming they were all removed. The updated repo does not retroactively affect other local clones.

## Compact session brief for a PHDK maintainer group

> **PHDK (Project Handoff to Development Kit)** is the operating system for AI-assisted software delivery. It turns product intent into planned, implemented, tested and traceable GitHub-delivered software through Capture, Plan, PMO when needed, Auto/Auto Force, UAT Prep, UAT/Fix, Check and remediation.
>
> This group maintains **PHDK itself**, at `tuyoisaza/PHDK`. Always write **PHDK** in capitals. At the start of every session, inspect live `main`, `VERSION`, README, newest CHANGELOG entry, relevant open PRs and the applicable standards. Read `PHDK_EVOLUTION_STANDARD.md`; do not rely on a cached version or earlier chat as authority.
>
> For requested updates, implement the complete coherent change in a scoped branch, reconcile affected entrypoints, manifest and tests, apply SemVer (**major** breaking, **minor** new standards/features, **patch** compatible fixes), and synchronize `VERSION`, README and CHANGELOG. Review/verify, publish via PR to `main` and verify the remote result where authorized. Never overwrite downstream project customization, bypass real controls, activate background agents/Actions, or assume projects have upgraded. Report evidence, true publication state and unresolved blockers concisely.

This brief is a reading aid, not an automatic trigger. New sessions must independently confirm current repository facts and current user authorization.
