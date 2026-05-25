# Firm Profile (shared)

<!--
THE FIRM, CAPTURED ONCE. Run Setup's firm orientation fills this in before any workspace is built,
and every builder reads it instead of re-asking the same questions. It is the firm-level context
that is true regardless of which workflow you are running. Refine it any time the firm changes.

This file is L3 reference. (Run Setup tells a first-time setup from a returning one by whether
`_shared-config/setup-progress.md` exists — that file is written at the end of the first setup.)
-->

## Firm
- **Name:** [Firm name]
- **What we invest in:** [Asset classes, strategy, geography — e.g., value-add multifamily and
  light-industrial in Sun Belt secondary markets]
- **Vehicles:** [Current fund(s)/vehicles, vintage, size, target returns — high level]

## Systems of Record (the platform boundary)
[The authoritative systems AI must NARRATE but never compute or override. Name each and what it owns.
This is the single most important section for keeping AI in its lane (Constraint 09). Examples:]
- **Fund administration / investor management:** [platform] — capital accounts, the waterfall,
  distributions, the investor register. Authoritative for all LP-facing figures.
- **Property / fund accounting:** [platform] — operating actuals, rent rolls, NOI.
- **Underwriting model:** [Excel / Argus] — return math. The model computes; AI writes about it.
- **CRM / pipeline:** [platform] — deal and relationship tracking.

## Team and Roles
[Who owns what, so workspaces route handoffs and sign-offs correctly. Examples:]
- [Name] — [Managing Partner / chairs IC / final win-loss call]
- [Name] — [Acquisitions lead / owns the investment thesis]
- [Name] — [Asset Management lead / business-plan-vs-actuals, dispositions]
- [Name] — [Investor Relations lead / LP letters, capital accounts, LP inquiries]

## Voice
The firm's written voice lives in `_shared-config/voice-and-tone.md` (this folder). Run Setup seeds
it here; it is fully populated the first time a writing workspace is built.
