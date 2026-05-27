# Response Posture Contract

## Purpose
Choose the right response posture before sensitive external-facing output ships.

## Inputs
- Likely questions.
- Audience context.
- Response standards.
- Escalation rules.
- Compliance boundaries.

## Process
1. Assign each issue a posture: answer directly, answer with caveat, hold, escalate, or route to platform.
2. Name the owner for every escalation.
3. Write approved language boundaries.
4. List what cannot be said yet.
5. Stop client-facing output while required confirmations remain open.

## Outputs
- `response_posture.md`
- `approved_language_boundaries.md`
- `escalation_log.md`

## Done Looks Like
The team knows what can be answered, what must be caveated, what must be escalated, and what belongs in the platform.

## Common Failure Modes
- Answering a platform-record question in narrative.
- Treating legal/compliance review as optional.
- Giving confident language before source facts are cleared.

## Layer Annotation
L2 module contract. Posture outputs are L4 artifacts and client-facing gates.
