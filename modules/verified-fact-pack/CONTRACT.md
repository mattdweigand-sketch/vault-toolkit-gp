# Verified Fact Pack Contract

## Purpose
Limit downstream work to verified facts, explicit inferences, and visible open checks.

## Inputs
- Platform-verified figures or system references.
- Source IDs from a provenance pass.
- Audience or entitlement restrictions.
- Forbidden claims.

## Process
1. Record each fact with source, owner, date, and audience restriction.
2. Separate verified facts from inferences.
3. List facts that are requested but unsupported.
4. List claims the workspace may not make.
5. Stop before client-facing output if high-stakes checks remain open.

## Outputs
- `fact_pack.md`
- `forbidden_claims.md`
- `entitlement_notes.md`
- `open_fact_checks.md`

## Done Looks Like
Every figure has a platform source or source ID. The pack distinguishes verified fact, inference, and forbidden claim. Missing facts are flagged, not invented.

## Common Failure Modes
- Treating narrative-friendly claims as verified facts.
- Omitting entitlement limits.
- Using working-model figures as final platform facts.

## Layer Annotation
L2 module contract. Fact packs are L4 outputs used as L3-like references by drafting stages.
