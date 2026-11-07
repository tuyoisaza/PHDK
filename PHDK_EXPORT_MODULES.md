# PHDK Export Modules — Contribution and Discovery Standard

## Purpose and command

`PHDK export modules` is an explicit, **foreground, donor-repository** inventory and proposal workflow. It makes reusable code/contract candidates visible for owner choice and safe contribution. It is the reverse of Plan's REUSE/ADAPT/BUILD decision, not an automatic upstream synchronization, package publisher, approval token, or new Auto stage. It does not replace `PHDK_REUSE_CATALOG_STANDARD.md` or `PHDK_RETROSPECTIVE_STANDARD.md`.

For an installed PHDK project, run the vendored helper from the donor root:

```sh
python3 phdk-standards/scripts/phdk_export_modules.py --root .
python3 phdk-standards/scripts/phdk_export_modules.py --root . --json
```

From the canonical PHDK repository, use `python3 scripts/phdk_export_modules.py --root <authorized-local-project> --catalog PHDK_REUSE_CATALOG.json`. On Windows use `py -3`. This local helper only reads the named repository and an optionally supplied local catalog; there is no network, provider operation, source copy, creation of files, or GitHub write. If no local catalog is available, report `CATALOG_UNAVAILABLE`, not "unique". `--json` is private **donor-local** structured output suitable for an agent-generated review; no JSON output is safe to publish upstream without separate redaction and authorization.

## Inventory and attribution rules

The helper inspects direct children of `packages/`, `modules/`, `components/`, `lib/`, `src/modules/`, `src/features/`, `src/components/`, `src/lib/`, `src/utils/`, `src/hooks/` and `src/services/`. It uses only directory names, optional `phdk-module.json`, package manifest/readme/test *presence*, and optional local Git changed-file paths. It skips symlinks, private/build/generated/data directories, deeply nested trees, source contents, credentials and customer fixtures. The upper bound is 80 candidates; a missing candidate is not proof of non-reusability. An agent may perform a more focused authorized source review after this inventory (including nonconventional layouts) but must not broaden into other repositories without authority.

Optional provenance marker **inside a candidate directory**:

```json
{
  "schema_version": 1,
  "catalog_id": "starter.themes",
  "upstream_version": "1.0.0",
  "upstream_commit": "0123456789abcdef0123456789abcdef01234567",
  "upstream_head_commit": "0123456789abcdef0123456789abcdef01234567"
}
```

`catalog_id` binds a declared catalog identity when present; an unknown ID is **UNVERIFIED**, not automatically a new standard. `upstream_commit` is the commit **already present in donor-local Git history** when the module was imported. `upstream_head_commit` is an optional local Git commit for a newer upstream revision with the same comparable paths and verified ancestry. No remote fetch occurs. The read-only helper detects changed tracked paths (excluding the marker) against the original baseline and, when both commits are locally accessible and ancestral, reports a three-way **path-level** overlap between local and upstream changes. This is a review signal, not a semantic merge, proof of improvement, patch quality, compatibility or a transferable change. Missing commits, moved module paths and untracked files are **UNVERIFIED** or outside automatic comparison. Never invent provenance markers, Git SHAs, tests or version evidence.

### Qualification

Inventory scores reflect only packaging, documentation, tests present and declared provenance. `HIGH` is a review priority, **not** evidence that functionality works or should be exported. Categories:

| Category | Interpretation |
|---|---|
| `NEW_CANDIDATE` | No obvious catalog name match in available catalog; further search required |
| `SPECIFICATION_IMPLEMENTATION` | Declared match to a specification-only contract; a possible first implementation |
| `POTENTIAL_EXTENSION` | Declared match to an implemented catalog module; change/quality review still required |
| `POSSIBLE_OVERLAP` | Uncertain textual match; must not silently fork a shared module |
| `UNVERIFIED_CATALOG_REFERENCE` | Declared catalog ID not found; reconcile provenance first |
| `UNCLASSIFIED` | No local catalog available; cannot assess novelty |

For each candidate, the agent must inspect relevant actual implementation and baseline (when permitted), interfaces, dependencies, tests, versioning, security/tenant isolation, license and redistribution rights, portability, maintenance ownership, installation/removal, regressions, and donor coupling. Summarize what is observably different, which parts are improvements **supported by evidence**, trade-offs and unresolved facts. Never infer `PASS` merely from test-file presence. Keep restrictions on local runtime tests, UAT, secrets and external services intact. Existing PHDK catalog status gates remain unchanged.

## Optional private PHDK Modules receiving library (v2.90.0)

After the owner selects a named candidate, a verified private implementation library may hold independently versioned, immutable snapshots under `modules/<category>/<slug>/versions/<SemVer>`, governed by [PHDK_MODULE_LIBRARY_STANDARD.md](PHDK_MODULE_LIBRARY_STANDARD.md). That separate **private** `MODULES_CATALOG.json` tracks module identity, versions and integrity; PHDK's public `PHDK_REUSE_CATALOG.json` remains sanitized and never contains private source or coordinates. `PHDK export modules` by itself **does not perform private receipt, create a repository or publish a package**. If the private repository is not accessible/provisioned, report the blocker and preserve the proposal.

## Decision and contribution workflow

1. **Discover** from the current authorized donor only; locate relevant retrospective findings (`docs/decisions/phdk-process-review.vN.md`) and any `REUSE_ASSESSMENT.md`. Neither opens a canonical task or publishes anything by itself.
2. **Compare and qualify** against the currently installed catalog and, when authorized, fresh canonical PHDK `main` and the relevant **actual** package version. Distinguish code changes from standard/policy changes. For any proposed "improvement", record local baseline, upstream version, observed delta and counter-evidence. Do not declare a three-way merge from incompatible/missing local Git ancestry.
3. **Present a batched decision** with IDs, classification (`NEW | EXTEND | STANDARD | LOCAL_ONLY | NEEDS_EVIDENCE`), recommendation, measured benefits (or `UNKNOWN`), risks, package target, required sanitization, test gaps, licensing and actual reuse rationale. Ask the owner **which particular candidates** to contribute, where and with what permitted visibility. An explicit answer identifying those candidates and target is the approval for that contribution only, subject to actual rights/access controls.
4. **Prepare separately** only the approved candidates: extract/rewrite generic code and tests to a separately versioned package/repository for implementation; remove donor/client details, secrets, credentials, tenant data, proprietary fixtures, branding and unlicensed code. Use synthetic examples. Preserve the donor implementation unchanged. For a standard or contract improvement, propose only generic policy/schema/checker changes to canonical PHDK. A catalog metadata entry belongs in PHDK; **product implementation does not**.
5. **Validate before publishing:** verify target visibility and redistribution rights, perform allowed static checks, review diff and actual test/portability evidence; status begins `CANDIDATE` if separately versioned implementation exists, not `ACCEPTED_VERSIONED`. Acceptance still requires observed tests and two independent consumers per `PHDK_REUSE_CATALOG_STANDARD.md`. `SPECIFICATION_ONLY` persists until implementation exists.
6. **Deliver through PRs**: create a scoped branch/PR in the authorized implementation package repo if applicable, plus a separate scoped PHDK standards/catalog PR under `PHDK_EVOLUTION_STANDARD.md`; reconcile `VERSION`, README, CHANGELOG, manifest, instructions and verification. Merge only as authorized and actually permitted; independently read back remote `main`. A PR draft/open is not published. Never auto-upgrade consumers or assume downstream adoption.
7. **Return a donor handoff** listing approved/rejected/deferred candidates, exact package/catalog versions and links, tests run/not run, rights restrictions, publication status and how a future `PHDK upgrade` or explicit package adoption could use it. No background queues, GitHub Actions, ongoing crawling or silent cross-project changes.

## Explicit guardrails

- **Export requires two independent boundaries:** owner choice of specific candidates plus separate verified authority/licensing for public or cross-repository publication. Merely running `PHDK export modules`, `PHDK auto`, `PHDK check` or an installed PHDK rule never grants export rights. An explicit current request to implement *this PHDK command* does **not** authorize publication of any unrelated donor code.
- Do not include private repository names, internal paths, source snapshots, embeddings, customer names, private URLs or donor-specific diffs in a public catalog or PHDK PR. Perform classification/rewrite inside the authorized environment; run secret/PII/license review before any PR. If rights or review evidence is unavailable, record `NEEDS_EVIDENCE` and withhold code.
- No source binary, installer, package coordinates or consumer dependency is added to PHDK merely because a project has a clever implementation. Do not overwrite an accepted module with a local variant; version and review changes, migrations and backwards compatibility.
- Treat proposals as local documents governed by `PHDK_DOCUMENTATION_STANDARD.md`. An authorized owner-local report may be written into `docs/decisions/<topic>.vN.md` and indexed; the helper itself is read-only. Catalog updates use the existing schema/checker and acceptance gates. Check `PHDK_AUTO_CONTINUITY.md` for bounded sessions if the later contribution is an explicit Auto task.

## Verification and limits

`tests/test_phdk_export_modules.py` covers safe inventory, local-only output, absent catalog, marker parsing, version uncertainty, local Git baselines, three-way path overlap, and symlink/path exclusions with synthetic temporary repositories. These tests verify the helper's logic, not a real exported module, package acceptance or deployed behavior. The helper cannot attest that a code fragment is useful, secure, original or legally shareable; these remain review decisions.
