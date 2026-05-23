# SKILL: Disposition Workspace Builder

## Description
Builds a customized disposition workspace by asking diagnostic questions about how a firm makes hold/sell decisions and runs a sale, then assembling a folder structure, stage contracts, and config files based on the answers.

## When to Use
When a firm needs to make a hold-vs-sell call on an owned asset and, when the answer is sell, run the disposition through to close and capital return. One workspace per asset under active consideration.

## Process

### Phase 1: Diagnosis (ask before building)

Ask the following questions one at a time. Wait for each answer before proceeding.

**Question 1: What triggers an exit conversation?**
"What makes you start thinking about selling an asset — business plan complete, a loan maturity, a strong market, fund life, an unsolicited offer?"

**Question 2: How do you decide hold vs. sell?**
"What factors do you weigh, and who makes the call? Is there an investment-committee gate, and what would the committee want to see?"

**Question 3: Where do the numbers come from?**
"Where do the hold-vs-sell return scenarios and the valuation come from — Argus, your model, a broker BOV? Who produces them?"

**Question 4: Walk me through your sale process.**
"From a decision to sell through close — how do you select a broker, prepare the asset for market, run the process, and evaluate offers?"

**Question 5: What happens at close?**
"Once it closes, how does capital return to LPs, and how is the realization communicated to them? Who handles each?"

### Phase 2: Assembly

Based on the answers, build the workspace:

1. Create the folder structure: four stages (position, decision, market, close), plus _config/ and _references/. If their process is simpler, do not force four — but keep the decision as a distinct gate.
2. Write CLAUDE.md: what this is, current state, structure map, how to use. Frame it as the mirror of deal-pipeline (taking an asset out), and note the decision stage is a fork — hold exits, sell proceeds.
3. Write CONTEXT.md: the stage map with the hold/sell fork, how stages connect, the handoff to fund administration (the platform and fund-admin team) and lp-reporting at close, and the AI-vs-Platform table.
4. Write a CONTEXT.md for each stage.
5. Create config templates: asset-profile.md (carried from asset-management where possible), hold-sell-criteria.md (when the firm holds vs. sells, timing factors, the decision bar), disposition-standards.md (broker selection, package contents, approval gates, offer evaluation). Populate from their answers.
6. Set up _references/ for prior dispositions, broker track records, and comps.

### Phase 3: Orientation

After building, walk the user through:
- "Here is what I built and why each piece exists."
- "The decision stage makes the hold case *and* the sell case in good faith — selling a good asset early and holding a bad one too long are both expensive. Stage 01 surfaces both sides before the IC decides."
- "Timing is part of the decision, not an afterthought. A sell decision carries a timing thesis into the market stage."
- "The model frames the thesis; it never produces the return that justifies the decision. The delta, the net proceeds, the valuation come from your model and the brokers (Constraint 09)."
- "Close ends with capital return and a clean handoff — your fund-administration platform and fund-admin team run the distribution, lp-reporting communicates the realization. The disposition isn't done at the wire."

## Important Notes
- Do not build before completing the diagnosis. The questions are the skill.
- The decision stage is the judgment heart. Make sure the hold case is real, not a foil, and that a marginal call is presented as marginal.
- Keep the math on the platform: this workspace argues and narrates; the numbers come from the model, the brokers, and the closing statement.
- Load and name the constraints this workflow uses: 01 (AI Writing Patterns), 02 (Output Drift), 08 (Handoff), plus the universal 06 and 09.
- Always annotate files with their ICM layer (L0–L4).
