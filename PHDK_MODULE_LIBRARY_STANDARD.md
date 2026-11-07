# PHDK Private Modules Library Standard

## Scope and boundary

`PHDK-Modules` is the **logical name** of a separate, private implementation library. Canonical PHDK stays the public methodology, standards and disclosure-safe reuse catalog. The owner-approved private library receives reusable product code, independently versioned by module. This standard **does not assert that any provider repository is provisioned**. A downloadable template or a PR in public PHDK is not a private repository, installed package or consumer deployment.

The current explicit owner authorization for the **library architecture** does not authorize copying any unrelated donor code, changing donor repositories, publishing a public package, granting repository access, installing background jobs or updating consumers. Verify the actual remote's private visibility and authorized identity before transferring any source. No private repository URL, private code or donor-specific metadata belongs in the public PHDK catalog by default.

## Storage architecture

The implementation library is one private Git repository containing independently versioned modules. A single private repository is permitted; separate repositories per module are optional future migrations. The library root uses:

```text
PHDK-Modules/
  MODULES_CATALOG.json
  schemas/phdk-module.schema.json
  schemas/phdk-modules-catalog.schema.json
  scripts/phdk_modules.py
  modules/<category>/<kebab-slug>/versions/<MAJOR.MINOR.PATCH>/
    module.json
    README.md
    <approved, sanitized implementation files>
  tests/test_phdk_modules.py
```

The stable identity is `<category>.<slug>`; categories: `ai`, `auth`, `data`, `infra`, `integrations`, `observability`, `security`, `ui`, `workflow`, `other`. An ID cannot be reassigned or silently renamed. A new module starts a new entry. An improvement retains its ID and adds a **new immutable version**; it never rewrites an earlier version or changes an existing consumer automatically.

`module.json` describes identity/title/summary, category, SemVer, interfaces, dependencies, runtimes/framework compatibility, security review reference, license and actual redistribution rights, owner/maintenance policy, test evidence, portability evidence and change-level/rationale. `README.md` must document purpose, integration/install/remove instructions, migrations and limits. `MODULES_CATALOG.json` is the **private** index: ID, latest version, release history, paths, digest, approval reference and contribution reference; it is not the public PHDK catalog.

## Lifecycle — discovery to private receipt

1. Run explicit `PHDK export modules` against **one authorized donor** under `PHDK_EXPORT_MODULES.md`. Discovery is read-only and provides one batch of new/extension/standard/local-only/needs-evidence candidates; it never transfers code.
2. The owner chooses specific candidates and the private destination. Confirm actual provider access, visibility, code ownership/license/redistribution rights, target branch controls and source sensitivity. If unverified, report `LIBRARY_NOT_PROVISIONED` or `NEEDS_EVIDENCE` and stop before source transfer.
3. In the authorized local context, separately generalize and sanitize only selected code; create its manifest, documentation and tests. Preserve the donor. Remove secrets, client identifiers, private fixtures and avoidable coupling. No direct private-to-public copy.
4. On a local private library checkout, use the offline **read-only** receiver proposal: `python3 scripts/phdk_modules.py --root . propose --candidate <authorized-path>`. This verifies naming, current private catalog, base version, declared SemVer change, permissions/security metadata and source-file safety limits. The resulting SHA-256 is a concurrency checkpoint, not a seal of legal or functional validity.
5. For the same currently authorized candidate, use `python3 scripts/phdk_modules.py --root . receive --candidate <authorized-path> --expected-catalog-sha256 <reported-hash> --approval-ref <actual-owner-reference> --contribution-id <stable-reference>`. This mutates the **private checkout only**, adding a new immutable version snapshot and atomically updating the private catalog. The reference flags record provenance and **do not grant approval**.
6. Run the offline `verify` validator, permitted static checks and diff/security/license review; publish only through the private library's scoped Git branch/PR under real repository access/approval controls. Read back the private remote `main` to confirm. Do not claim release or deployment for local receipt or an open PR.
7. If a separate installable package and redistributable metadata are ready, propose a **sanitized**, independently authorized catalog-only PR to public PHDK. Keep source, private coordinates, internal evidence and customer identifiers out. An implementation snapshot is not automatically `ACCEPTED_VERSIONED` or downloadable.

## Incremental version governance

- Private module versions use strict `MAJOR.MINOR.PATCH`, per module, not the canonical PHDK methodology version. A major change declares breaking compatibility, minor declares backward-compatible new capability, patch declares compatible fix. The helper checks chronology and declared class, **not actual semantic compatibility**.
- Every accepted receipt adds an immutable `versions/X.Y.Z` snapshot. Registry history retains each version and deterministic SHA-256 of file paths/content, so a later in-place edit fails `verify`. Prior revisions remain in the private repo and may be adopted/recovered explicitly.
- The receiver rejects duplicate IDs with conflicting paths, duplicate/downgraded versions, inconsistent change levels, invalid metadata, symlink/hidden-file hazards, oversized files, absent README, unreviewed security or unverified license rights. It never runs donor code, network calls, GitHub Actions, Docker or UAT.
- A private receipt does not automatically authorize package publication or consumer upgrades. A private receipt may have status `CANDIDATE` or `REVIEWED`; it is not a production claim. `ACCEPTED_VERSIONED` remains subject to observed test evidence and at least **two independent consumer implementations**, plus public PHDK's separate security/license/portability gate. Claims in a manifest are evidence pointers needing real verification.
- Existing consumers remain pinned. Plan's `REUSE | ADAPT | BUILD` still requires actual target access and compatibility review. `PHDK upgrade` syncs public methodology only; it never automatically installs, updates or fetches private modules.

## Public-private catalog separation

`PHDK_REUSE_CATALOG.json` is a disclosure-safe **public index**, controlled by `PHDK_REUSE_CATALOG_STANDARD.md`. `MODULES_CATALOG.json` is a **private** implementation registry. They use distinct schemas and authorization. A candidate private library entry can remain invisible to the public catalog until generic, safe metadata is separately approved; **do not create fictional implementation references or turn a private location into a public URL**. PHDK Plan may consult the private library only with actual current scoped access.

Public PHDK vendors **this standard**, not the private source, the private registry or its receiver. The library's source/template may be prepared locally before a private provider repository exists; record `REPOSITORY_NOT_CREATED` honestly. No automated cross-repository synchronization, scheduled scanners, GitHub Actions, public releases, external spending or private consumer adoption follow from the architecture alone.

## Verification limits

The private starter includes a standard-library offline receiver and synthetic regression cases for new contributions, SemVer increments, immutability, catalog concurrency, bad metadata, symlink and secret-path exclusions, and absent rights/security review. These checks do **not** establish real code quality, license ownership, independent consumer portability, production behavior or UAT. A private GitHub repository must be separately created and its private visibility verified before treating this library as remotely available.
