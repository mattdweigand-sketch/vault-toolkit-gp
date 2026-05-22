# Market Thesis Workspace

## What This Is
A workspace for building the firm's defensible point of view on a market, sector, or strategy — and keeping it current. It turns scattered market data and research into a clear, sourced thesis: where the firm should be looking, why now, and what would have to be true. Built for an investments or research lead at a commercial real estate GP who wants the firm's acquisition focus driven by an articulated view rather than by whatever deals happen to cross the desk.

The thesis is not an end in itself. Its job is to point the rest of the machine: it sharpens the investment box and screening criteria in the deal-screening workspace and focuses sourcing. A firm with a written thesis screens faster and buys with more conviction.

## Current State
- This is a reference architecture. No active thesis.
- To use: copy the folder, populate _config with your thesis format, research standards, and source map, then run the cycle per market or sector you cover.

## Structure
```
market-thesis/
  CLAUDE.md              # You are here.
  CONTEXT.md             # Workflow routing.
  01_research/
    CONTEXT.md           # Stage contract: gather and vet the market inputs.
    output/              # Sourced research pack. Input for 02_synthesis.
  02_synthesis/
    CONTEXT.md           # Stage contract: form the thesis, evidence vs. inference.
    output/              # The thesis with its support and risks.
  03_publish/
    CONTEXT.md           # Stage contract: produce the thesis document; route it.
    output/              # Published thesis (internal; optional LP-facing variant).
  _config/               # Thesis format, research standards, source map.
  _references/           # Prior theses, the evidence library, tracked calls.
```

## How to Use
1. Read CONTEXT.md for the full workflow.
2. Populate _config/ with your thesis format, your research standards (how sources are vetted, how confidence is marked), and your source map.
3. Start in 01_research. Gather and vet the market inputs for the market/sector in question. Provenance matters — research arrives at varying quality.
4. Move to 02_synthesis. Form the thesis, keeping evidence and inference distinct and marking confidence.
5. Move to 03_publish. Produce the thesis document and route it — to deal-screening to update the box, to sourcing to focus the hunt, and optionally as LP-facing market commentary.
6. Re-run on a cycle or when the market moves. Compare against the prior thesis in _references.

## Key Decisions
- **A thesis is a claim, not a data dump.** The output is a defensible point of view — where to play and why — not a market report that recites figures and concludes nothing. If the document does not commit to a view, it is research, not a thesis.
- **Evidence and inference are kept separate.** The strongest market mistakes come from a forecast presented as a fact. The synthesis stage marks what is observed (sourced data) versus what is the firm's read (inference), with confidence levels, so a reader can see where the conviction rests. See Constraints 01 and 02.
- **Data comes from sources, never from the model.** Rents, vacancy, cap rates, transaction volumes, economic figures — these come from the firm's data providers and named research, not from the model's memory of the market. The model synthesizes; it does not recall a statistic. See Constraint 09.
- **Provenance is a first-class step.** Research arrives from many sources of uneven quality — broker research has a seller's lean, data providers lag, headlines mislead. The research stage inventories and ranks sources before any synthesis, so the thesis rests on vetted inputs. See Constraint 10.
- **The thesis points the machine.** A published thesis is wired to act: it updates the investment box and screening criteria in deal-screening and focuses sourcing. A thesis that changes no downstream behavior was a writing exercise.
- **Track the calls.** Prior theses live in _references with what they predicted, so the firm can see which views played out. This is not a learning loop, but it keeps the firm honest about its own forecasting.

## Constraints That Apply
Built against the GP Operating Toolkit. Most relevant: **01 (AI Writing)** so the thesis reads as a sharp view and not generic market-report prose, **02 (Output Drift)**, **10 (Source Provenance)** for the research inputs, and the universal **06 (Layer Triage)** and **09 (Platform Boundary)**.

## Layer Annotations
- CLAUDE.md: L0 (always loaded, orientation)
- CONTEXT.md: L1 (workflow routing)
- Stage CONTEXT.md files: L2 (stage contracts)
- _config/ files: L3 (reference: format, standards, source map)
- _references/ files: L3 (prior theses, evidence library, tracked calls)
- Research inputs and stage outputs: L4 (working artifacts, this thesis)
