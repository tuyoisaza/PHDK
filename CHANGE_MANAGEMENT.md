# PHDK Change Management

## Purpose

This file keeps release/change-management material out of the product README.

Use the README to understand what PHDK is, why it exists, its operating lifecycle and commands.

Use this document and `CHANGELOG.md` to understand how PHDK evolves.

## Sources of truth

- `VERSION` — current published PHDK version.
- `CHANGELOG.md` — detailed technical release history.
- GitHub pull requests — reviewable source changes and merge evidence.
- `PHDK_MANIFEST.txt` — standards distributed into downstream projects.
- `PHDK_UPGRADE.md` — downstream synchronization contract.

## Versioning

PHDK uses semantic versioning.

- **MAJOR** — incompatible standards or execution-model changes.
- **MINOR** — new commands, modes, standards, workflows or substantial capabilities.
- **PATCH** — corrections, clarifications and compatible behavior improvements.

## Release workflow

A PHDK standards release should:

1. start from current canonical `main`;
2. update the relevant standards coherently;
3. reconcile all routing/native copies that could contradict the new behavior;
4. update `VERSION`;
5. update `CHANGELOG.md`;
6. verify manifest mappings, references and version markers;
7. review the complete outgoing diff;
8. publish through the repository's normal branch/PR flow;
9. verify the resulting version/content on remote `main`.

## Downstream adoption

Publishing PHDK does not automatically mutate downstream repositories.

Existing projects receive the new standards only when explicitly synchronized, normally with:

```text
PHDK upgrade
```

When the local PHDK-owned surface intentionally needs to be replaced with canonical upstream despite local edits:

```text
PHDK upgrade force
```

Force applies only to PHDK-owned files/managed blocks and does not authorize product-code changes.

## Migration principle

New PHDK versions should preserve project-specific intent and owner controls unless the owner explicitly asks to replace them.

Standards upgrades must distinguish:

- PHDK-owned canonical content;
- project-specific requirements and decisions;
- owner instructions;
- generated task/status evidence;
- product code and configuration.

A standards release is not evidence that every downstream project has adopted it.

## Recent capability milestones

For exact release details, see `CHANGELOG.md`.

High-level milestones include:

- **v2.44.3** — Auto lifecycle visibility: mandatory stage board at startup, stage-transition updates, and final lifecycle closure.
- **v2.44.2** — generic Auto now falls into PMO portfolio discovery when multiple parallel fronts exist instead of demanding one arbitrary task.
- **v2.44** — universal PHDK command preflight, version/install validation, and operational recommended-skills usage.
- **v2.43** — `PHDK plan` solution architecture/convergence planning and full-lifecycle `PHDK auto` orchestration.
- **v2.42** — PMO multi-workstream orchestration and bounded in-session workers.
- **v2.41** — actionable UAT repair and incomplete-acceptance guidance.
- **v2.40** — `PHDK upgrade force`.
- **v2.39** — professional project Capture and project-level intent.
- **v2.38** — conditional AI admin / Prompts / consumption standards.
- **v2.37** — repository compliance auditing with `PHDK check`.
- **v2.36** — intent-aligned UAT and autonomous UAT reporting.
- **v2.35** — continuous whole-goal execution with `PHDK auto`.
- **v2.34** — documentary blocker reconciliation with `PHDK unlock`.
- **v2.33** — complete normal delivery-to-main semantics.
- **v2.32** — Developer Mode and bounded provider diagnostics.

## Reader guidance

If you want to:

- **understand PHDK** → read `README.md`;
- **see exactly what changed** → read `CHANGELOG.md`;
- **understand release/adoption policy** → read this file;
- **upgrade a project** → read `PHDK_UPGRADE.md`.
