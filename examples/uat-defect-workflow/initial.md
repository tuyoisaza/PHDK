# Company Co initial UAT excerpt

Fictional example. The revisions, case observations and evidence notes illustrate the reporting format. A real run links its actual deployment readback, redacted frames or traces, and fixture manifest.

## Coverage checkpoint

The coordinator assigned the Bruma handoff, Nube access check and mobile admin journey to separate workers with isolated synthetic sessions. The published source commit was `a010a010a010a010a010a010a010a010a010a010`. The example deployment readback identified the running build as `a010a010a010a010a010a010a010a010a010a010` before and after these cases.

| Case | Observed outcome on this build | Verdict |
|---|---|---|
| UAT-001 | The Bruma lead assigned repair R-01. The page displayed success, but reopening the record showed no assignee. | FAIL |
| UAT-002 | The intended Bruma member opened the inbox independently. R-01 was absent. The later step to acknowledge receipt could not run. | FAIL |
| UAT-003 | On the supported iOS browser, the platform owner switched to the fixture user. The banner covered Return to admin and the control could not be activated. | FAIL |
| UAT-004 | The Nube admin requested Bruma's R-01 by ID using the application API. The server denied access without returning the record. | PASS |

**NOT ACCEPTED.** Four cases reported, three failed and one passed. UAT-001 and UAT-002 share one defect. The mobile defect blocked its remaining steps. The independent isolation check finished on the same revision.

## Defect register

| ID | Cases | Severity | Observed build | Initial evidence | State | Fixed build | Retest build | Retest result | Retest evidence | Next action |
|---|---|---|---|---|---|---|---|---|---|---|
| DEF-001 | UAT-001, UAT-002 | P1 | a010a010a010a010a010a010a010a010a010a010 | [A-01](initial.md#a-01) | OPEN | - | - | - | - | Repair assignment persistence under authorized UAT Fix. Repeat both sides of the handoff and the isolation check. |
| DEF-002 | UAT-003 | P1 | a010a010a010a010a010a010a010a010a010a010 | [A-02](initial.md#a-02) | OPEN | - | - | - | - | Restore the visible control. Retest the original iOS route including server-confirmed return to the elevated actor. |

### A-01

Example evidence pairs the lead's saved confirmation and reopened empty assignee with the member's empty inbox for the same fixture R-01. The business handoff failed. The lead's success cue also misrepresented the saved state.

### A-02

Example pre-action frame shows the Test as banner covering the return control on iOS. The attempted action left the role unchanged. The worker stopped this journey and revoked its temporary session through the normal cleanup path.
