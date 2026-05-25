# Thesis Format

<!--
ANNOTATION: The structure of the thesis document, plus the LP-facing market-
commentary variant. The publish stage writes against this. A defined shape keeps
theses comparable cycle to cycle and preserves the evidence/inference discipline
that makes them trustworthy. See Constraint 02 (Output Drift).

VOICE: the firm's core written voice comes from the shared firm voice file,
`_shared-config/voice-and-tone.md` (from this workspace under workspaces/<name>/,
that is ../../_shared-config/voice-and-tone.md). The publish stage reads it for
the firm voice. This file holds only the thesis REGISTER on top of that voice:
the internal-vs-LP-facing variants and the confidence vocabulary (which lives in
research-standards.md). See Constraint 05.

This is L3 reference, loaded in stage 03.
-->

## Base Format: Internal Market Thesis
[The structure of the internal thesis document. The default in the stage
contract is: The Claim and Why It Matters → The Case (evidence and inference,
kept distinct) → What Would Have to Be True / Risk Case → Downstream Actions →
Tracked Call. Adjust to how the firm consumes it. Specify length and any
standard exhibits. The non-negotiable element: evidence and inference stay
visibly separate, with confidence marked.]

## Variant: LP-Facing Market Commentary
[The same view, recast for an external audience. Describe the differences:
- Audience: LPs, not the internal investments team.
- Register: more cautious; never asserts more conviction than the internal
  thesis supports.
- Drops: the firm's specific sourcing/box actions and any non-public positioning.
- Keeps: the view and its grounding, in a form appropriate to share.
- Must align to the firm's investor voice in `_shared-config/voice-and-tone.md`
  and any compliance/forward-looking language requirements (see Constraint 05 and
  the lp-reporting workspace's constraints file).
A market commentary that says more than the internal thesis is a compliance and
credibility risk; the external register is more cautious, never less.]
