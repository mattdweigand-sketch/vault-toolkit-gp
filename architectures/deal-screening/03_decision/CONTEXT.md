# Stage 03: Decision

## Purpose
Record the go/no-go on the screened opportunity. On a pursue, produce the handoff brief that seeds a deal-pipeline workspace. On a pass, log the decision and its reason. This is the gate between the funnel and a committed diligence effort.

## Inputs
- **02_screen/output/screen-[deal-name]-[date].md**: The screen assessment and recommendation.
- **_references/**: The pass log and prior decisions, for consistency and the audit trail.

## Process
1. Read the screen assessment. The recommendation is an input to the decision, not the decision — the deal team makes the call.
2. Record the decision: pursue, pass, or hold (revisit on a trigger or date).
3. On **pursue**: produce the handoff brief. This is the bridge to deal-pipeline — it carries the snapshot, the screen rationale, the fit assessment, and the open questions forward so deal-pipeline's sourcing stage starts from the screen's work, not a blank page.
4. On **pass**: log the pass with its reason, tied to the screen rationale. Add it to the pass record in _references so the same deal type gets a consistent answer and the firm can see its rejection patterns over time.
5. On **hold**: note the trigger or date that would bring it back, so it does not silently disappear.
6. Record the decision in output.

## Output
Write to: 03_decision/output/decision-[deal-name]-[date].md

For a pursue:
```
# Decision: PURSUE — [Deal Name]
Screen reference: [filename]
Decided by: [name], on [date]

## Why Pursue
[The decision rationale, building on the screen.]

## Handoff Brief (seeds deal-pipeline sourcing)
[The snapshot summary, the fit assessment, the screen rationale, the open
 questions, and the rough economics — packaged as the starting point for a
 new deal-pipeline workspace. Copy this into that workspace's _config to
 begin sourcing.]
```

For a pass / hold:
```
# Decision: PASS (or HOLD) — [Deal Name]
Screen reference: [filename]
Decided by: [name], on [date]

## Reason
[Why, tied to the screen rationale. For a hold: the trigger or date to revisit.]

## Logged
[Confirm added to the pass record in _references.]
```

## Done Looks Like
A recorded decision. On a pursue, a handoff brief that a deal-pipeline workspace can start from directly. On a pass, a logged reason that keeps screening consistent and auditable.

## Common Failure Modes
- **Treating the recommendation as the decision.** The screen recommends; the team decides. Recording a decision means a person owns it.
- **A pursue with no handoff.** If "pursue" does not produce the brief that seeds deal-pipeline, the screen's work is lost and sourcing restarts from the OM. The handoff is the point.
- **An unlogged pass.** A pass that is not recorded breaks consistency and the audit trail, and erases the pattern data that makes the firm a sharper screener over time.

## Layer Annotation
L2 stage contract. The screen assessment is L4 (this deal). The pass log in _references/ is L3 reference this stage writes back to, so the firm's screening record compounds.
