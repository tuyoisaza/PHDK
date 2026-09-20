<!-- PHDK-MANAGED:START -->
## PHDK managed rules

- Read `phdk-standards/AGENTS.md` before project work. Read `TASK.md` and `STATUS.md` before changing code.
- Canonical upgrade command: **`PHDK upgrade`**. When the developer gives that exact command, execute `phdk-standards/PHDK_UPGRADE.md` immediately. The command itself is approval to synchronize PHDK-managed files; do not ask for a second confirmation.
- Never commit directly to `main` unless Finetuning Mode is explicitly active. Never force-push.
- Never weaken auth, RBAC, validation, privacy, or cost controls merely to make a feature work.
- Verification is diagnostics-first: use health/deep-health, affected safe probes, browser confirmation, and Copy Diagnostics; add automated tests only for the risk triggers in `phdk-standards/TESTING_STANDARD.md`.
- Stop before destructive data operations, auth/payment/tenant architecture changes, new external services, or metered API behavior without a hard cap and kill switch.
- Preserve project memory in `TASK.md` and `STATUS.md`; do not treat chat memory as the source of truth.
<!-- PHDK-MANAGED:END -->
