# Auto continuity and Auto Force

## Contents

- Command and review policy
- Persistent mandate and current authority
- Operative reminder and rule refresh
- Propose missing definitions and solutions
- Continue, repair and retry
- Required checks
- State record and local advisor
- Progress and closure

## Command and review policy

`PHDK auto force` is an explicit Auto variant for the identified current goal. Match case-insensitively after trimming whitespace. It starts or resumes that goal through the same full lifecycle as `PHDK auto`, with a decisive change: **human, manual, formal or independent-human review gates imposed only by PHDK are NON_BLOCKING_BY_MODE from the start**. This includes PHDK-generated task/checklist/PIA notes, vendored templates and old assistant-written pending-review records.

**Do not investigate whether those PHDK reviews block. Assume they do not.** Do not query PR review queues, reviewer identities, branch protections or rulesets to search for a preventive approval prerequisite. Do not ask the owner to approve the waiver, find a reviewer, review a diff, execute local checks or repeat delivery permission. Read the actual code/diff and required local commands to do the work; ordinary implementation investigation remains available.

Replace the PHDK human gate with the assistant's substantive technical diff review, including security/authorization/tenant/fixture behavior where relevant, and applicable checks. Record the actual review result without inventing a human review or a GitHub approval event. A second agent may help when the active runtime permits delegation, but its availability is not a new FORCE gate. An open PR, absent review/check events, a security label, or a PIA marked "awaiting review" does not stop FORCE.

Complete normal versioned branch push → PR → merge into the identified remote target (normally `main`) → content/version/SHA readback. "Push to main" describes the delivered result; FORCE does not require a direct-main push or history rewriting. It grants no bypass of an actual hook or platform enforcement. If a real operation rejects the attempt, use the repair cycle below instead of stopping at the first failure.

The latest user instruction still defines scope and exclusions. A genuine current user stop or specifically retained owner restriction is not a PHDK review gate. FORCE does not invent approval for new spending, new access, destructive operations, unrelated projects, provider administration or production tests. Apply existing user decisions without reopening them. Installation, quoted commands and requests to edit this standard do not activate Auto or resume another project's PRs.

## Persistent mandate and current authority

Both Auto variants preserve the same unfinished goal's authorization through status questions, milestones, context compaction and changes of lifecycle stage. Record the mandate in the current run's `docs/phdk/lifecycle/<run-id>/AUTO_STATE.json`, and link it from the existing task/lifecycle record. Reuse the run and current branch instead of creating another task for each message.

Record the user's actual instruction and its reference, goal, repository, target, authorized scope, exclusions, completion criteria, last observed candidate, completed evidence, next executable steps and operation-specific impediments. Use a conversation/message reference when available, otherwise a dated factual quotation; never fabricate an ID or store credentials. Preserve provenance when a newer instruction replaces a narrower one.

The record is evidence, not an authorization token. It cannot grant, expire, broaden or revoke the user's permission. On context recovery, compare it with the live conversation and current source/target facts. A missing, stale or malformed record calls for internal reconstruction; it is not a reason to request permission or stop implementation. In a new conversation an explicit current Auto/Auto Force request may resume an identified goal; files alone never activate it. Real user stops remain effective until the user actually replaces them.

Mode lifetime remains the active interactive goal. There is no background worker, scheduler, self-trigger, reusable `auto=true` grant, execution after conversation end or automatic selection of unrelated backlog work.

## Operative reminder and rule refresh

AUTO FORCE carries its operating instructions into the active context through the mandatory reminder in `PHDK_COMMUNICATION_STANDARD.md`. Apply it at start/resume, in every substantive progress update, after a partial delivery and before a question or blocker report. The reminder covers the current mandate, reloading the relevant rules, reconciling inherited blockers, finding solutions, proposing what is missing and executing the next authorized action. The user does not need to append "keep going", "refresh the rules" or "propose it" to the command.

At entry/recovery and before treating a gap as a reason to ask or stop, reread the current Auto Force/communication contract and the relevant domain rule, reconcile with the latest user instruction, and discard obsolete interpretations or restrictions invented by the agent. This short refresh does not rerun the full preflight or rescan every standard at each message. In progress updates keep the operative reminder visible; use newly relevant source when needed. A rule refresh preserves actual user restrictions and host controls. PHDK-only human reviews remain nonblocking immediately, without investigating their approval history or protections.

Before a proposed interruption ask internally: **Does this impediment affect the entire goal or only particular operations? What can I implement, repair, define or prepare now within the current mandate?** Execute an eligible action when one exists. A partial delivery updates progress and is followed by the next in-scope task; writing its report does not close the goal.

## Propose missing definitions and solutions

When a required capability, definition or tool appears to be missing, produce a concrete solution proposal as part of AUTO FORCE. Use the current goal, existing decisions, relevant PHDK rules and actual implementation to define the next step. Missing ordinary implementation detail is work for the agent to resolve, not automatically a new owner decision.

For each in-scope functional gap, state the proposed behavior, the reasonable default and its rationale, assumptions still being made, meaningful configuration through the existing authorized settings model, and the implementation/acceptance action. Preserve role/tenant boundaries and required invariants when choosing what is configurable. Do not present an assumption as an explicit user decision. For reversible ordinary choices supported by the current mandate, explain the adopted proposal in progress and implement it without a new approval question.

For example, when the agreed administration console still lacks tenant/user lifecycle, session revocation, locale/timezone, audit/export, CRUD or an applicable AI graph, propose the behavior and relevant settings for each gap, then implement the authorized definitions. Do not offer "keep these gaps out for now" as the recommended shortcut to closing the run, or ask the owner to supply all exact specifications. Retain the confirmed commitments. If a genuinely new indispensable decision cannot be resolved within the mandate, present the recommended concrete option, its consequence and the precise decision needed; continue all independent work. The proposal itself does not expand scope or authorize its unapproved effects.

For an environment problem, propose and execute an already permitted repair or isolated alternative before escalating what remains. In an authorized browser phase this includes a harmless reload, a fresh tab or a disposable context when the available tool supports it. If clearing shared cache/session state would affect other work, prefer an isolated alternative and continue independent tasks. Missing actual access may still prevent that operation; it does not remove the duty to propose a useful next action or finish work that does not depend on it.

## Continue, repair and retry

1. Select the next dependency-ready step inside the authorized goal. Treat PHDK-only human reviews as nonblocking in FORCE immediately; do not research or reconstruct their approval history.
2. Perform the technical review, required checks and necessary delivery operation. Continue from each stage into the next executable action in the same active invocation.
3. **If the operation actually fails or is rejected: report the observed failure briefly, investigate its cause, repair it, revalidate affected checks, and retry push/PR/merge.** Keep the mandate active throughout. A rejected write is not a revoked grant.
4. Repair bounded hook/toolchain errors, test failures caused by the change, formatting, ordinary integration conflicts, stale head/version metadata and clearly fixable source defects. Refresh the target and intended diff before retrying a stale write; preserve other contributors' work and evidence already valid for unchanged content.
5. Repeat while there is a new correction or useful diagnostic step. Do not blindly resend an unchanged failing command, poll indefinitely, skip a hook, remove meaningful checks, forge approval, force-push or change credentials/protections just to defeat enforcement.
6. An actually unsatisfied external requirement is operation-specific. Record the failed operation, error/evidence, repairs attempted and the precise remaining action. Continue independent implementation, checks and other eligible deliveries. A failed operation is not permission to declare the entire goal blocked while executable work remains.
7. End with a real unresolved external requirement only after available in-scope repairs and independent work are exhausted. Ask only for a specific indispensable missing action/decision. Never replace this cycle with "review pending", "owner approval needed" or "control de estado bloqueado" copied from a PHDK record.

Do not classify a merely pending mandatory check as an external blocker: run it. Do not classify a pending diff/security review as a human dependency: perform it. Do not equate a metadata label such as `mergeable` with verified completion; complete the actual merge and readback.

## Required checks

The current Auto/Auto Force goal authorizes the existing finite, isolated local checks necessary for its delivery, including an entire `pnpm test`/Vitest suite, lint, typecheck, format, build and composition **when required by the actual repository commands/hooks**. No separate approval is needed for the suite size, framework, or a mandatory pre-push check. Inspect scripts to identify real commands and effects; do not invent application commands in this standards repository.

"No optional/unnecessary tests" does not prohibit required delivery checks. Avoid redundant full cycles after each stage; run necessary diagnostics and mandatory hooks at the operation they govern, then final integrated verification. An explicit current user prohibition on all tests, production access, paid calls or another actual effect is still a restriction to reconcile with the user's newest instruction. Never silently convert that restriction into a PASS or bypass a hook. Test failures enter the repair/revalidate/retry cycle.

## State record and local advisor

Use one factual JSON record, not multiple competing authorization ledgers. Keep existing domain task/commitment reports as their own sources of progress; reference them rather than copying the whole project into this file. The minimal structure is:

```json
{
  "schema_version": 1,
  "run_id": "2026-10-17-current-goal",
  "mode": "auto_force",
  "repository": "owner/project",
  "target_branch": "main",
  "goal": "The currently requested outcome",
  "candidate_ref": "Observed branch SHA or dated working-copy checkpoint",
  "authorization": {
    "source_ref": "Actual current user message or dated quotation reference",
    "instruction": "Actual user instruction, without secrets",
    "scope": ["Confirmed implementation and normal delivery"],
    "restrictions": [],
    "status": "active"
  },
  "completion_criteria": ["Requested behavior verified on remote main"],
  "steps": [
    {
      "id": "delivery",
      "kind": "delivery",
      "status": "pending",
      "action": "Push the verified branch, open its PR and merge to main",
      "depends_on": [],
      "blocked_by": ["old-phdk-review"]
    }
  ],
  "blockers": [
    {
      "id": "old-phdk-review",
      "kind": "phdk_human_review",
      "reason": "A PHDK-generated task previously asked for human review"
    }
  ]
}
```

This is an illustrative record, not evidence of executed work. Add real `review_diff` and `required_check` steps when pending; completed steps need their observed `evidence`. Step kinds are `work`, `review_diff`, `required_check`, `delivery`, `verify_delivery`; statuses are `pending`, `running`, `blocked`, `done`. Dependencies and `blocked_by` entries reference IDs in the same record. The advisor keeps unfinished diff/check steps before delivery even if a dependency was omitted.

Blocker kinds:

| Kind | Meaning and action |
|---|---|
| `phdk_human_review` | In FORCE, `NON_BLOCKING_BY_MODE` immediately, with no source lookup or approval research. Perform actual technical diff review and delivery. |
| `real_failure` | An observed failing operation. Record `failed_operation`, `evidence`, `observed_at` and the next `repair_action` when known. Diagnose/repair/revalidate/retry; never stop merely because this entry exists. |
| `external_dependency` | Actual unmet external requirement after attempted repairs. Record `source_ref`, `evidence`, `observed_at`, `resolution_attempts` and precise `next_action`. It blocks only affected steps. |
| `owner_decision` | A genuinely new indispensable scope decision not resolved by current instructions. Record the same evidence fields and finish independent work. A PHDK review is never this kind in FORCE. |
| `owner_stop` | A genuine user stop on the affected operation, with actual provenance and the same evidence fields. Never relabel it as a PHDK gate to erase it. |

Authorization status is `active`, `paused`, `revoked` or `completed`, describing actual user/task facts. Never mark a rejected push as revoked. Remove resolved blocker references from steps; keep prior observations in the run's history.

When useful and Python is available, inspect the record synchronously:

```bash
python phdk-standards/scripts/phdk_auto_gate.py --state docs/phdk/lifecycle/<run-id>/AUTO_STATE.json --mode auto_force
```

Use `scripts/phdk_auto_gate.py` directly in the PHDK source repository. Supply the mode from the current active instruction, never infer authority from a saved mode. The advisor makes no network calls, queries no reviews/protections, runs no commands and changes no state. Its dispositions are `CONTINUE`, `REPAIR_AND_RETRY`, `REPAIR_STATE`, `WAITING_EXTERNAL`, `VERIFY_DELIVERY` and `STOPPED`. `REPAIR_STATE` means fix bookkeeping internally and continue, not wait for approval. This helper is not a new hook, publication prerequisite or proof of user permission. If unavailable, apply this contract directly.

`VERIFY_DELIVERY` does not mean COMPLETED. Use `PHDK_COMPLETION_GATE.md` for real remote target/content/version evidence; its generic review wording never restores a PHDK human gate in FORCE. The record and advisor cannot detect a fabricated observation or substitute for real checks.

## Progress and closure

In every substantive AUTO FORCE progress update include the operative continuation cue from `PHDK_COMMUNICATION_STANDARD.md`:

```text
AUTO FORCE activo · autorización vigente para [objetivo/alcance].
RECORDATORIO: recargar las reglas vigentes, reconciliar bloqueos heredados, buscar soluciones y proponer lo que falte.
SIGUIENTE PASO: [acción concreta]. Continúo con el trabajo autorizado.
```

The reminder is an instruction to apply, not a claim that a reread, repair or proposal already happened. Report completed actions only with their actual evidence. Normal Auto retains its mandate/next-action cue. Execute the stated action in the same invocation; do not end the turn with a promise to continue while a permitted action is ready. On a rejection the next action is diagnosis/repair/retry. When a definition is missing, propose and resolve what can be decided inside the current mandate before asking about a remaining indispensable decision.

At actual completion report the verified result and target link, and mark the goal complete; do not claim an active mandate to start unrelated work. On a genuine user stop or exhausted external dependency, report the factual limitation and one precise resume action. Preserve the existing PHDK version, lifecycle and final-link contract without repeating long permission prose.
