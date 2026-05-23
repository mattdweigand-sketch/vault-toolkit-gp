# SKILL: Market Thesis Workspace Builder

## Description
Builds a customized market-thesis workspace by asking diagnostic questions about how a firm forms its view on markets and sectors, then assembling a folder structure, stage contracts, and config files based on the answers.

## When to Use
When an investments or research lead wants the firm's acquisition focus driven by an articulated, defensible point of view — where to look and why now — that sharpens screening and sourcing, rather than reacting to whatever deals appear.

## Process

### Phase 1: Diagnosis (ask before building)

Ask the following questions one at a time. Wait for each answer before proceeding.

**Question 1: What do you form a view on, and how often?**
"Which markets, sectors, or strategies do you build a thesis on, and on what cadence — quarterly, when the market moves, ahead of a fund?"

**Question 2: What are your data sources?**
"Where does your market data come from — CoStar, broker research, economic data? Which sources have known biases or lags you already account for?"

**Question 3: How is a thesis used today?**
"Once you have a view, what does it actually change? Does it steer screening and sourcing, or does it mostly get written and filed?"

**Question 4: How do you separate what you know from what you believe?**
"When you make a market call, how do you distinguish the data you can point to from the interpretation you're making on top of it?"

**Question 5: Do you publish externally, and do you track your calls?**
"Do you produce LP-facing market commentary as well? And do you ever look back at whether a past thesis held up?"

### Phase 2: Assembly

Based on the answers, build the workspace:

1. Create the folder structure: three stages (research, synthesis, publish), plus _config/ and _references/.
2. Write CLAUDE.md: what this is, current state, structure map, how to use. Emphasize that a thesis is a claim, not a data dump, and that it is wired to update the deal-screening box and focus sourcing.
3. Write CONTEXT.md: the stage map, how stages connect, the downstream routing to deal-screening and sourcing, and the AI-vs-Platform table (data comes from named sources; the model synthesizes; the conviction is the firm's).
4. Write a CONTEXT.md for each stage.
5. Create config templates: thesis-format.md (internal thesis plus an LP-facing commentary variant), research-standards.md (source vetting, supported-vs-inference bar, confidence levels, never-do list), source-map.md (sources with their biases and lags). Populate from their answers.
6. Set up _references/ for prior theses and their tracked calls.

### Phase 3: Orientation

After building, walk the user through:
- "Here is what I built and why each piece exists."
- "A thesis commits to a view. If the document recites figures and concludes nothing, it is research, not a thesis."
- "Evidence and inference stay visibly separate, with confidence marked — a forecast presented as a fact is the cardinal market error (Constraints 01 and 02)."
- "Data comes from named sources, never from the model's memory of the market (Constraint 09). The research stage vets provenance before any synthesis (Constraint 10)."
- "The thesis points the machine: the publish stage names the specific changes to the screening box and the sourcing focus. A thesis that changes no downstream behavior was a writing exercise."
- "Prior theses and their calls live in _references so you can see which views held — that keeps the firm honest about its own forecasting."

## Important Notes
- Do not build before completing the diagnosis. The questions are the skill.
- The discipline here is provenance and the evidence/inference split, not volume. A short, sourced, committed thesis beats a long, hedged market report.
- An LP-facing variant must never assert more conviction than the internal thesis supports — flag this as a compliance and credibility risk.
- Load and name the constraints this workflow uses: 01 (AI Writing Patterns), 02 (Output Drift), 10 (Source Provenance), plus the universal 06 and 09.
- Always annotate files with their ICM layer (L0–L4).
