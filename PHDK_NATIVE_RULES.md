<!-- PHDK-MANAGED:START -->
## PHDK managed rules

- Read `phdk-standards/AGENTS.md` before project work. Read `TASK.md` and `STATUS.md` before changing code.
- Canonical upgrade command: **`PHDK upgrade`**. When the developer gives that exact command, execute `phdk-standards/PHDK_UPGRADE.md` immediately. The command itself is approval to synchronize PHDK-managed files; do not ask for a second confirmation.
- **Mission Autopilot is default:** once `TASK.md` defines a clear goal/scope/Done When, keep working across planned slices until complete, genuinely blocked, or a true Stop-and-Ask boundary is reached. Never ask "continue?" between planned slices.
- Verified slices may be committed and pushed autonomously to the mission feature branch. Never commit directly to `main` unless Finetuning Mode is explicitly active. Never force-push; Human Diff Review is still required before merge to `main`.
- Never weaken auth, RBAC, validation, privacy, or cost controls merely to make a feature work.
- Verification is diagnostics-first: use health/deep-health, affected safe probes, browser confirmation, and Copy Diagnostics; add automated tests only for the risk triggers in `phdk-standards/TESTING_STANDARD.md`.
- Stop before destructive data operations, auth/payment/tenant architecture changes, new external services, or metered API behavior without a hard cap and kill switch.
- Preserve project memory in `TASK.md` and `STATUS.md`; do not treat chat memory as the source of truth.
<!-- PHDK-MANAGED:END -->
