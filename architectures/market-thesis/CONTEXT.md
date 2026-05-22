# Workflow: Market Thesis

## Overview
Three-stage pipeline: Research → Synthesis → Publish. Each stage has a defined contract and a clear output. Human review between stages. The research stage gates the others: no thesis is built on inputs that have not been vetted and sourced.

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_research | Gather and vet the market inputs | Data-provider exports, broker/sell-side research, economic data, news | 01_research/output/ |
| 02_synthesis | Form the thesis; evidence vs. inference | Research pack, research standards, prior thesis | 02_synthesis/output/ |
| 03_publish | Produce the thesis document; route it downstream | Synthesized thesis, thesis format | 03_publish/output/ |

## How Stages Connect
- 01 → 02: Research produces a vetted, sourced pack — the inputs ranked by quality and provenance. Synthesis reasons over the pack, not over raw research. If synthesis is re-vetting a source, research did not finish.
- 02 → 03: Synthesis produces the thesis with its evidence, inference, and risks. Publish formats it and routes it. Publish does not change the view; it presents it. If publish is re-arguing the thesis, synthesis needs to commit harder.
- 03 → deal-screening / sourcing (the point): The published thesis is meant to update the investment box and screening criteria in the deal-screening workspace and to focus sourcing. The thesis is wired to change downstream behavior, not just to be read.

## Reference Material (in _config/)
- thesis-format.md: The structure of the thesis document, plus an LP-facing market-commentary variant. Loaded in stage 03.
- research-standards.md: How sources are vetted, what counts as supported, how confidence is marked, the never-do list. Loaded in stages 01 and 02.
- source-map.md: The firm's market-data sources and their known biases and lags. Loaded in stage 01.

## Reference Material (in _references/)
- Prior theses and what they predicted (tracked calls), the firm's evidence library, and standing market context worth carrying forward.

## When to Add Stages
- **02a_challenge** between synthesis and publish: a structured red-team of the thesis — the strongest case against it — before it goes out and starts steering capital. Worth adding for theses that will materially redirect sourcing.

## AI vs. Platform: Where Each Step Lives

The temptation here is to let the model produce market statistics from memory or state a forecast as fact. The rule: data comes from named sources, the view is the firm's, the model synthesizes and drafts. See Constraint 09.

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| Market data — rents, vacancy, cap rates, transactions, economic figures | Platform / data foundation | Data providers and named research (CoStar and others) |
| Inventorying and ranking sources by provenance and bias | AI + human | You, applying the research standards (Constraint 10) |
| Synthesizing the data into a point of view, structuring the argument, drafting | AI | You, on top of vetted inputs |
| The firm's conviction — the call the thesis commits to | Human in the loop | The investments / research lead |

The trap on this workflow: a confident statistic with no source, or a forecast dressed as an observation. AI synthesizes vetted, sourced inputs into the firm's view; the data comes from named providers; the conviction is the firm's.
