# Validated Memory Store Contract

## Purpose
Capture repeated judgment in a comparable, validated store that future workflows can read.

## Inputs
- Event or outcome record.
- Canonical questions.
- Controlled taxonomy.
- Store schema.
- Human validation owner.

## Process
1. Analyze the event against the same canonical questions used by prior records.
2. Propose causal claims with confidence labels.
3. Require human validation before capture.
4. Write append-only records.
5. Update patterns only when evidence supports, extends, or contradicts them.
6. Flag lessons that should flow to other workflows.

## Outputs
- `_store/records/[record].md`
- `_store/patterns.md`
- Capture log.
- Cross-workflow flags.

## Done Looks Like
The store contains comparable records, validated causal claims, controlled tags, and pattern updates that future workflows can use.

## Common Failure Modes
- Capturing unvalidated model judgment.
- Overwriting history.
- Protecting an existing pattern from contradictory evidence.
- Promoting a single anecdote into policy.

## Layer Annotation
L2 module contract. `_store/` is a persistent L3/L4 hybrid: written by runs, read as future reference.
