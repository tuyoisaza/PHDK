# INTENT_CAPTURE_STANDARD.md

## Purpose

`PHDK capture` is the preferred project-level discovery/reconstruction workflow and is governed by `PHDK_CAPTURE.md`. It produces `PROJECT_INTENT.md` for project-level ethos/purpose plus the professional requirements package. This standard remains the durable mechanism for later feature/bug/change-level intent files under `docs/intents/`.


This file defines when and how to capture the *why* behind a feature, bug, or body of work as a durable, human-reviewable repository artifact. Capture relevant intent while defining scope in `TASK.md` and include it in the authorized change; it does not require a separate commit or human-approval gate before implementation.

It extends `SPEC_INTERVIEW_PROMPT.md`'s one-time, project-level interview down to individual asks that a human presents during an active session, such as a stakeholder request, customer bug report, or teammate's report.

Its goal is that the reason a piece of work exists survives a context reset, a different AI tool picking up the thread, or months passing — the same way `TASK_TRACKING_STANDARD.md` makes sure the *plan* survives, and `CHANGELOG.md` makes sure the *outcome* survives.

`EXECUTION_SCOPE.md` governs which work may be performed. Intent capture never authorizes scheduled maintenance, automated alerts, dependency bots, or an agent to launch a mission. Diagnosis and repair discovered during an approved code mission stay within that mission; a new objective requires a human request.

For explicit `PHDK auto`, follow `PHDK_AUTO.md`: derive intent from the identified current goal, proceed through all its stages, and collect final verification after complete implementation. Do not start an interview, intent-approval round, or new handoff merely because a slice needs a record. Existing requirements and reversible conventional choices settle routine details; isolate only genuinely missing material decisions and continue independent authorized work.

---

## Status

Read this file when:

- a new feature or bug ask arrives that is not already covered by `PROJECT_BRIEF.md`, `PRD.md`, or `FEATURES.md`
- the person asking for the work is not the person who will implement or verify it
- a human presents an incident report that needs a code fix and the reason is not self-evident from the supplied evidence
- starting `TASK.md` for a new slice, to decide whether that slice needs an intent file behind it

---

## Core Rule

An intent file captures the problem and the desired outcome, separately from the implementation plan and code. The assistant reviews it against the current request while recording scope in `TASK.md`; a clear owner request already supplies its authorization. Do not require the owner to confirm the same intent again.

This is not a spec. It does not describe files, routes, or implementation. If it starts describing how something will be built, that content belongs in `TASK.md`'s `Slice` section instead.

---

## When to Write One

Write an intent file when:

- A new feature or bug's *why* is not already fully covered by `PROJECT_BRIEF.md` / `PRD.md` / `FEATURES.md`
- A human brings an earlier request into the current session, such as a ticket, message, or support report
- The originator of the ask is not the same person who will implement or verify it

Skip it when:

- The slice is purely mechanical execution of something already fully specified in `FEATURES.md` or `PRD.md`
- The change is a one-line trivial fix with an obvious, undisputed reason

When in doubt, write one. A short intent file costs little; a lost "why" costs a rediscovery conversation later.

---

## Format

Create the file at `docs/intents/<short-name>-intent.md`:

```md
# Intent — <short name>

## Originator
[The human requesting this work in the current session, and any earlier request or report they supplied. A bot, alert, or schedule is not an authorizing originator.]

## Problem
[What pain, gap, or risk this addresses. Not the solution — the problem.]

## Desired Outcome
[What success looks like, in terms of what a person can do, see, or no longer worry about.]

## Constraints / Non-Goals
[What this must not become, any hard constraints, and anything explicitly out of scope.]

## Open Questions
[Anything unresolved that scoping (TASK.md) will need to settle.]

## Linked Slices
[TASK.md / docs/completed-slices/ entries this intent has produced, added to as they happen.]
```

---

## Optional Capture Interview

Use a short interview only when the supplied context leaves a material goal or constraint genuinely unresolved. A short request with a clear outcome needs no interview. Use the prompts below to identify the one missing decision, not as a compulsory sequence:

1. Who is asking for this, and what prompted it right now?
2. What problem or pain does this address — what happens today without it?
3. What does success look like when this is done?
4. Is there anything this must not become, or anything explicitly out of scope?
5. Anything unresolved that needs to be settled before scoping starts?

Ask only what the current request and available evidence do not answer, one question at a time. Under Auto, finish independent authorized work before requesting a blocked decision; neither this list nor `SPEC_INTERVIEW_PROMPT.md` interrupts an already clear whole-project goal.

---

## File Location and Lifecycle

- Intent files live in `docs/intents/`, one file per intent.
- An intent file is created once and never overwritten. It can span multiple slices and `TASK.md` cycles over time; it is a permanent record. Keep `TASK.md` focused on the whole current goal until that goal closes, including all Auto stages, rather than replacing it at each internal checkpoint.
- Never delete an intent file. If the work it describes is abandoned, add a line under `Open Questions` noting that and why, rather than removing the file.
- As slices that implement an intent close, add a pointer to each closed slice's archived `TASK.md` (per `TASK_TRACKING_STANDARD.md`) under the intent's `Linked Slices` section.

---

## Review Step

Intent capture must preserve the originator's meaning, but it is not a mandatory approval pause. If the current user is the originator and their request already clearly states the problem, desired outcome, and relevant constraints, write the intent file from that request and continue into mission scoping without asking them to confirm their own words again.

If the human's request relies on an external source or delegated report and contains a material ambiguity that could change the mission, isolate that decision, complete independent authorized work, and ask the current user only what still blocks progress. Their clear authorization is sufficient; do not contact third parties or require a separate originator approval. External evidence and captured intent do not authorize work beyond the approved mission or `EXECUTION_SCOPE.md`.

---

## Relationship to Existing Files

- **`PROJECT_BRIEF.md` / `PRD.md` / `FEATURES.md`** — the project-level equivalent, captured once at project inception via `SPEC_INTERVIEW_PROMPT.md` and `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md`. An intent file is not a replacement for these — it is the missing middle layer for asks that arrive *after* project inception and are not already covered by them.
- **`TASK.md`** — reads the reviewed intent file's `Problem` and `Desired Outcome` when defining the slice's user-visible outcome (`AGILE_SLICE_WORKFLOW.md` Step 1) and references it via the `Intent:` field in `TASK.md`'s `Slice` header (`TASK_TRACKING_STANDARD.md`).
- **`STATUS.md`** — does not track intents directly; intents are tracked via the `Linked Slices` section inside each intent file itself, plus the normal `TASK.md`/`STATUS.md` slice lifecycle.

PHDK deliberately does not add a separate `spec.md` artifact on top of this. `PROJECT_BRIEF.md`/`PRD.md`/`FEATURES.md` plus `TASK.md`'s `Slice` header already cover requirements and design scope; a third layer would be exactly the kind of ceremony `AGILE_SLICE_WORKFLOW.md` warns against for small slices.

---

## Anti-Patterns

- Writing an intent file that describes implementation details instead of the problem and desired outcome
- Asking the current originator to reconfirm an intent that already faithfully captures their explicit request
- Pausing Auto for an intent interview, checkpoint commit, or stage approval when the whole current goal is already clear
- Acting on a materially ambiguous externally-originated intent without resolving the ambiguity
- Treating a trivial, undisputed one-line fix as requiring an intent file
- Overwriting or deleting an intent file instead of updating its `Linked Slices` and `Open Questions`
- Skipping intent capture for an ask that arrived from outside the current session just because writing the file feels like overhead
- Starting work from a scheduled check, automated alert, dependency bot, or agent-generated objective without a human request in the active session
- Treating a saved intent as a future execution trigger or permission to create automation

---

## Verification

- [ ] An intent file exists for any feature/bug not already covered by `PROJECT_BRIEF.md`/`PRD.md`/`FEATURES.md`
- [ ] The intent reflects the human's request in the active session, and any material ambiguity was resolved before acting on it
- [ ] `TASK.md`'s `Slice` header references the intent file via its `Intent:` field, or explicitly states none applies
- [ ] The intent file describes the problem and desired outcome, not implementation
- [ ] Closed slices that implemented the intent are linked back under its `Linked Slices` section
- [ ] No intent file was deleted or overwritten


## Relationship to UAT and user stories

`PHDK uat` must treat project intent as the upstream source for user stories and acceptance cases. The required traceability chain is:

**Project Intent → User Story → Requirement / Acceptance Criterion → UAT Case → Evidence**

User stories are not generated from implementation inventory. A route, component, endpoint, schema field, or existing code path does not justify a story unless its user value can be traced to the project's problem, desired outcome, objective, or constraint.

When a proposed story cannot be traced to an existing project-level intent or a current scoped intent, mark it `OUT OF INTENT` and exclude it from acceptance counts. If it appears necessary, surface it as a product-scope decision instead of silently expanding the product.

The UAT report must state which intent sources were used and identify any uncovered intent, uncovered story, or out-of-intent behavior.
