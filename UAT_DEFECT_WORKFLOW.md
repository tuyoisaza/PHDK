# Defects during UAT

The default is to finish the discovery pass on one deployed revision, keep a live defect register in `UAT_REPORT.md`, and retest an identifiable repair candidate. The evaluator records a defect before moving to the next case. In a bare `PHDK uat`, product repairs remain queued for `PHDK uat fix`. A request such as “PHDK uat: finish the pass, repair the findings and retest” authorizes both stages in that order. Honor more specific owner instructions. No prompt per defect is required once repair is authorized.

## Run the discovery pass

1. Pin run, deployed build, environment/configuration revision, role, case scope and synthetic fixture set. Open the report and its register before the first case. On resuming a run, reconcile existing case notes and screenshots first. Import evidenced failures and flag missing proof for recheck. Import relevant outstanding findings from the last report or stage snapshot. Preserve the initial observation and keep one writer responsible for the register.
2. On discovery, append a stable defect ID and link the evidence immediately. Record step and scenario, role/tenant, expected and actual outcome, impact, reproducible steps, observed build, evidence, severity, blocked dependents, owner and next action in the existing case/action card. Capture a rendered frame for a visual defect. Record root cause as unknown until established. Reuse the defect ID when several cases share the same evidenced problem; keep every affected case. Keep distinct defects distinct even on one screen.
3. A verified failure is FAIL. If it prevents another step or case from being exercised, mark the dependent item BLOCKED and link the defect. Missing access alone is a blocker, without an invented product defect. Continue independent roles and journeys. A workaround can expose further coverage; it does not clear the original failure. Use the existing P0–P3 severity rules and the functional/workflow UX decision. Track minor friction even when the associated case passes.
4. Stop the affected operations immediately for a leak, corruption, unintended real side effect or a lost test boundary. If the affected scope cannot be isolated, stop the entire pass, preserve minimal redacted evidence, clean up safely and report. For a non-hazardous blocker that prevents all remaining journeys, close the baseline pass early with the blocked case IDs; start an authorized repair batch or report the next repair command.

## Evidence and work can move in parallel

Use [PHDK_INTELLIGENT_EXECUTION.md](PHDK_INTELLIGENT_EXECUTION.md) only when the host supports bounded foreground workers and the split helps. One evaluator stays on the pinned build and sends defect ID, case IDs, revision, expected/actual result and evidence as soon as each finding is captured. A second worker may deduplicate, trace source, assess impact and propose the smallest repair. With explicit repair authority it may prepare a change on an isolated branch with disjoint write ownership. If shared browser state, mutable fixtures or tooling prevents isolation, one agent performs these responsibilities sequentially.

The coordinator owns the register, scope, integration, release and final verdict. A worker saying “fixed” records work done; a commit or merge still needs deployed retest evidence. Keep staged repairs off the shared test target while the discovery pass is active. If a critical repair must deploy early or autodeploy changes the site, checkpoint A, retain completed observations under A, stop/requeue in-flight cases and verify B before resuming. Apply the same rule to shared schema, feature flags, auth policy and fixture changes even when the URL is unchanged. Never combine A and B into one uninterrupted run. The evaluator may retest as soon as B is verified and its test window starts. The handoff must identify cases interrupted on A and requeued for B. Browser and data permissions, cleanup and spending limits apply equally to workers.

## One register with a visible status

Use this table in the existing report. Keep the heading and column names literal for the offline checker. Case IDs are comma-separated; put reproduction details and long text outside the table and link them by ID. Use a dash for unavailable values. Keep both a write-through record and a stage-50 snapshot so the initial FAIL can be reconstructed after retest.

```markdown
## Defect register

| ID | Cases | Severity | Observed build | Initial evidence | State | Fixed build | Retest build | Retest result | Retest evidence | Next action |
|---|---|---|---|---|---|---|---|---|---|---|
```

| State | Meaning |
|---|---|
| OPEN | Captured, triaged or awaiting repair authority. Give an owner and next action in the card. |
| IN_REPAIR | Authorized work is underway. Record source revision and delivery status in `UAT_REMEDIATION.md`. |
| AWAITING_RETEST | A repair was prepared or delivered. Enter Fixed build only after verifying the exact deployed candidate contains the repair. |
| REOPENED | The observed retest still fails. Keep the initial failure and link the latest failing evidence. |
| RETEST_BLOCKED | Confirmation cannot finish. State why, who can unblock it and which case resumes. |
| VERIFIED_RESOLVED | All affected cases passed on the selected repaired build with linked confirmation evidence. |
| OUT_OF_SCOPE | A documented scope decision moved the item outside this run. Preserve its history, rationale and owner. |

Keep one row per defect and count cases separately. The initial build and evidence stay immutable; add affected cases as discovered. Fixed build is the actual deployment selected for retest and may differ from the source commit. Retest build identifies the deployment actually exercised. Use a dash if access prevented any execution on that build. For a single case, use its retest result. For several cases, record each explicitly, for example `UAT-001=PASS, UAT-002=PASS`. Link the per-case records in `UAT_RETEST_REPORT.md`; retain every attempt there, including failed and blocked ones.

At case-batch checkpoints, at a blocker that changes coverage, and at closeout, show cases executed/planned, failed and blocked, plus defects open/in repair, awaiting retest, reopened, retest-blocked, verified closed and out of scope. Name urgent IDs, the active build and the next action. Link the register directly. Zero findings is a valid outcome. A checkpoint might read “Build B, 4/4 cases reported, 3 passed, 1 blocked. DEF-001 verified closed. DEF-002 awaits the iOS retest. Next, restore iOS access and repeat UAT-003.” Before finalizing or handing off a run, run the read-only check against the current report and the last applicable report, if present:

```sh
python phdk-standards/scripts/phdk_uat_defect_register.py UAT_REPORT.md --previous PATH_TO_PRIOR_REPORT
```

Omit `--previous` on the first pass. On the first run after upgrading, import unresolved issues from legacy action cards and link the archived evidence before applying the structured check. The checker inspects recorded dispositions. The coordinator verifies that linked evidence shows what the report claims. See the [initial report](examples/uat-defect-workflow/initial.md) and [retest report](examples/uat-defect-workflow/retest.md) for one fictional handoff.

## Close the repair and retest cycle

Batch related fixes by impact and dependency. Start with blockers that unlock the most journeys and security or integrity defects. Verify the revised candidate is deployed before using the browser. On B, replay the original failing step through its observable outcome, including functional and UX criteria. Execute formerly blocked steps and risk-based regression around shared components, affected roles, tenant boundaries and related workflows. If impact cannot be bounded, a shared access/data/navigation change affects many flows, or prior evidence cannot be attributed reliably, rerun the full affected suite. Preserve A's results as historical; identify coverage actually executed on B. If current evidence is insufficient for required acceptance, keep acceptance incomplete.

Close only after confirmation. If the same failure persists, reopen it with the new evidence. Try another repair only with a materially different diagnosis or change. Once available evidence reveals no safe new action, stop that loop with the defect open, attempts and a specific next decision or unblock step. Finish independent work first. An approved scope exception or deferred cosmetic item remains visible. An unresolved required failure, a missing proof or a worker's progress update cannot become acceptance by being moved to a later list.

This workflow applies the distinction between confirmation testing and regression testing, and the practice of retaining configuration and defect history. [ISTQB CTFL v4.0.1, §§2.2.3, 5.4–5.5](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)
