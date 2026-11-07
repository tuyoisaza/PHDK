# Company Co UAT Fix retest excerpt

Fictional continuation of the [initial run](initial.md). The observations below illustrate a mixed retest outcome.

## Coverage checkpoint

For this example the owner authorized UAT Fix for both defects. The coordinator closed the first test window and published the repairs in source commit `b020b020b020b020b020b020b020b020b020b020`. A separate deployment readback identified `b020b020b020b020b020b020b020b020b020b020` as the running build before workers resumed. Each replay used fresh run-owned fixtures and sessions.

| Case | Observed outcome on the repaired build | Verdict |
|---|---|---|
| UAT-001 | The Bruma lead assigned R-02. The confirmation named the recipient. Reopening R-02 showed the same person. | PASS |
| UAT-002 | The member found R-02 in the inbox and acknowledged it. The lead reopened the record and saw the acknowledgment. | PASS |
| UAT-003 | The required iOS browser was unavailable. The original mobile return path still needs confirmation. | BLOCKED |
| UAT-004 | Because assignment handling changed, the Nube admin repeated the direct lookup for Bruma's R-02. The API denied it and returned no record. | PASS |

**ACCEPTANCE INCOMPLETE.** Three cases passed on the repaired build and one remains blocked. The original three failures stay in the initial run.

## Defect register

| ID | Cases | Severity | Observed build | Initial evidence | State | Fixed build | Retest build | Retest result | Retest evidence | Next action |
|---|---|---|---|---|---|---|---|---|---|---|
| DEF-001 | UAT-001, UAT-002 | P1 | a010a010a010a010a010a010a010a010a010a010 | [A-01](initial.md#a-01) | VERIFIED_RESOLVED | b020b020b020b020b020b020b020b020b020b020 | b020b020b020b020b020b020b020b020b020b020 | UAT-001=PASS, UAT-002=PASS | [B-01](#b-01) | Closed for this build. |
| DEF-002 | UAT-003 | P1 | a010a010a010a010a010a010a010a010a010a010 | [A-02](initial.md#a-02) | RETEST_BLOCKED | b020b020b020b020b020b020b020b020b020b020 | - | UAT-003=BLOCKED | [B-02](#b-02) | Restore access to the supported iOS browser, confirm the deployed revision, then rerun UAT-003. |

### B-01

Example before-action frame shows the recipient picker. After saving, the reopened record and receiving inbox both identify R-02 and the same member. A separate role session confirms the persisted acknowledgment. UAT-004 supplies the associated permission regression.

### B-02

Example readiness record identifies the repaired deployment and the disconnected iOS browser. The desktop worker could continue the other cases. The mobile interaction remains unobserved on this build.
