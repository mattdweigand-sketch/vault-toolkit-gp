# Stage 03: Publish

## Purpose
Produce the thesis document in the firm's format and route it so it changes downstream behavior. This stage presents the view; it does not change it. The output drives the deal-screening box and sourcing focus, and optionally becomes LP-facing market commentary.

## Inputs
- **02_synthesis/output/thesis-[market-or-sector]-[date].md**: The synthesized thesis with evidence, inference, and risk.
- **_shared-config/voice-and-tone.md**: The firm's core written voice. Read it so the published thesis sounds like the firm. (From this workspace under `workspaces/<name>/`, that is `../../_shared-config/voice-and-tone.md`.)
- **_config/thesis-format.md**: The document structure and the thesis register (internal vs. LP-facing variant) layered on the firm voice, including the LP-facing commentary variant.
- **_config/research-standards.md**: The firm's confidence vocabulary (how conviction is marked) — preserve it in the document.
- **_references/**: Where the published thesis and its tracked call are filed.

## Process
1. Read the synthesized thesis. Confirm it commits to a view and carries its support.
2. Select the format from thesis-format.md: the internal thesis document, or the LP-facing market-commentary variant (a different audience and a more cautious register — never a stronger claim than the internal view supports).
3. Write the document in the firm's voice (`_shared-config/voice-and-tone.md`) at the chosen register. Lead with the claim and the "so what." Preserve the evidence/inference distinction and the confidence markers, in the firm's confidence vocabulary — do not smooth them away for a cleaner read; that distinction is the thesis's integrity.
4. Translate the thesis into downstream actions:
   - For **deal-screening**: the specific changes to the investment box and screening criteria (which markets/asset types move up or down, which become deal-breakers).
   - For **sourcing**: where to focus the hunt and what to prioritize.
5. File the thesis and its tracked call in _references — what it predicts and the indicators to watch — so the firm can later see whether the view held.
6. Record the publication and its routing in output.

## Output
Write to: 03_publish/output/thesis-published-[market-or-sector]-[date].md (and the LP variant if produced)

Format (internal):
```
# Market Thesis: [Market / Sector] — [Date]
Synthesis reference: 02_synthesis/output/thesis-[...]-[date].md

## The Claim and Why It Matters
[The view and the "so what" for the firm, up front.]

## The Case
[Evidence and inference, distinction preserved, confidence marked.]

## What Would Have to Be True / Risk Case
[Carried from synthesis.]

## Downstream Actions
[Deal-screening: specific box and criteria changes.
 Sourcing: where to focus.]

## Tracked Call
[What this thesis predicts and the indicators to watch. Filed to _references.]
```

## Done Looks Like
A thesis document that commits to a view, preserves its evidence/inference integrity, and names the specific downstream changes — to the screening box and to sourcing — that it should drive. Its call is tracked for later honesty.

## Common Failure Modes
- **Polishing away the confidence markers.** A cleaner-reading thesis that has dropped the inference labels and confidence levels has lost the thing that made it trustworthy. Keep them (Constraint 02).
- **An LP-facing variant that overclaims.** The external commentary must never assert more conviction than the internal thesis supports. Same view, more cautious register.
- **No downstream actions.** A thesis filed without translating into screening and sourcing changes steers nothing. The "Downstream Actions" section is the point of publishing.

## Layer Annotation
L2 stage contract. The synthesized thesis is L4 (this cycle). The thesis format from _config/ is L3. The published thesis and tracked call are filed to _references/ (L3) so prior views and their outcomes accumulate.
