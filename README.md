# PHDK Standards Complete Package v2

Generated: 2026-05-07 15:10

This ZIP contains the full PHDK standards set.

## Included files

- `AGENTS.md`
- `BUILD_APP_FOUNDATION_PROMPT.md`
- `DESIGN_RULES.md`
- `DEVELOPMENT_RULES.md`
- `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md`
- `QA_CHECKLIST.md`
- `TECHNICAL_STACK.md`

## Update applied

`BUILD_APP_FOUNDATION_PROMPT.md` is the active app foundation prompt.

References were updated in:

- `AGENTS.md`
- `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md`
- `QA_CHECKLIST.md`
- `TECHNICAL_STACK.md` where relevant language appeared
- `DEVELOPMENT_RULES.md`

## Verification

Legacy bootstrap filename references: none found

## Recommended repo use

Put these files in your reusable PHDK standards repository.

The generated project-specific PHDK kit should reference this standards repo and instruct AI coders to fetch the latest versions before coding.


## v2 Fix Applied

Generated: 2026-05-07 15:21

`QA_CHECKLIST.md` now explicitly references `BUILD_APP_FOUNDATION_PROMPT.md` in the monorepo foundation guidance so agents know where the standard repository structure came from.
