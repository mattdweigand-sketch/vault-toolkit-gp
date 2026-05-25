# The GP Operating Toolkit

For private equity and commercial real estate GPs who want to build with AI instead of just use it. It turns your firm's recurring deal, investor, and fund work into controlled AI workflows — without rebuilding the systems of record that already hold your data, and without the data-risk of pointing a model at everything at once.

**Who this is for:** the COO, Head of IR, CFO or controller, acquisitions lead, asset-management lead, and the AI or technology lead at a GP firm — anyone who owns a recurring workflow and wants AI to help run it without handing over the firm's records or its judgment.

**What this is not:** not a replacement for your fund-accounting or fund-administration platform, your investor-management system, your deal pipeline, or your CRM; not a data warehouse; not a compliance approval system; not a prompt library; and not a way to skip human review.

## What This Is

This is not a prompt library. There are no copy-paste templates here.

This is a set of tools organized around problems your firm has already encountered. Each one follows the same structure: the principle that solves the problem (most of which predate AI by decades), the existing tools or skills that handle it, and the deeper architectural thinking that makes the fix permanent instead of temporary.

Every constraint file includes tuning questions. These are not decorative. They exist because a constraint that does not fit your specific workflow will either be ignored or will make your output worse. Answer them before you use the file. The constraint adapts to your firm, not the other way around.

## How to Use This

**To set up: open this folder with an AI agent, point it at `CLAUDE.md`, and say "Run setup."** That
one instruction works in any tool. In Claude Code `CLAUDE.md` loads automatically, so "Run setup" is
all you need; in other tools, make sure the agent has read `CLAUDE.md` first. `CLAUDE.md` is a thin
bootstrap that hands the agent to `SETUP.md`, the setup engine — it orients to your firm once, then
builds your first workspace.

**The repository becomes your operating system.** After the first setup, `SETUP.md` rewrites
`CLAUDE.md` into your firm's operating-system map — it names what is built and how to add more. You
keep building forever: say "add a workflow," "build a &lt;workflow&gt;," or "Run setup" again to stand
up a new workflow type or another instance of one you already run. An optional, reversible
**finalize** step moves the toolkit (`SETUP.md`, `architectures/`, `constraints/`, `skill-starters/`)
into `_kit/`, so the repo root reads purely as your operating system while every building capability
stays intact. Everything below is optional background.

**If you are setting this up with an AI agent:** Clone or download this repository to your working directory, then point your agent at `CLAUDE.md` at the root. That file is the agent's map. It runs the onboarding sequence, routes you to the right builder, names the constraints to load, and finishes with a working, populated workspace. Start there and the rest of this section is optional reading.

**If you work in Claude Code, Cowork, Cursor, or VS Code:** Drop the constraint files into your workspace. Reference them from your CLAUDE.md or CONTEXT.md. Load them selectively based on the stage of work you are in. Do not load all of them at once.

**If you work in Claude Projects:** Add the relevant constraint files as knowledge sources. Use one or two at a time, matched to the task. The whole point of separation of concerns is that each piece of context has a job.

**If you work in Claude Desktop, ChatGPT, Copilot, or any other chat interface:** Copy the constraint content into your conversation when you need it. These are portable. The principles work regardless of which model or tool you are using.

**If you are non-technical:** Start with constraint 06 (Layer Triage). It will help you figure out which problems at your firm actually need AI and which ones need a spreadsheet or your fund administrator. If you are weighing what to build versus what to source from a platform, read constraint 09 (Platform Boundary) next. Then move to whichever constraint matches your most frequent frustration.

## What Is in Here

### /constraints (10 files)
Problem-organized reference files. Each one addresses a specific frustration GPs hit when working with AI on deal, investor, and fund work. Each one has three layers: traditional solutions that predate AI, existing skills and tools that handle part of the problem, and the architectural principle that makes the fix stick. Each one has tuning questions that customize the constraint to your firm. Constraint 06 (Layer Triage) and Constraint 09 (Platform Boundary) together answer the question most GPs get wrong: where to apply AI for real value, and where to rely on an enterprise data foundation instead of building it yourself.

### /architectures (11 annotated workspaces)
Real folder structures you can copy, explore, and study, each modeled on a GP workflow and built on one of four structural shapes (gated pipeline, operations queue, document production, learning loop). Ten span the GP lifecycle:
- **deal-screening**: triaging inbound deal flow against the investment box — capture, screen, decide. Feeds deal-pipeline.
- **deal-pipeline**: an acquisition from sourcing through diligence, investment committee, and close.
- **asset-management**: portfolio monitoring — business-plan-vs-actual reviews and a watchlist; hosts JV/co-GP and special-servicing report variants.
- **disposition**: the exit — hold/sell decision through marketing and close to capital return.
- **lp-reporting**: investor communications from data through drafting through distribution.
- **lp-inquiries**: inbound LP questions between formal events — intake, resolve, respond.
- **deal-win-loss-learning**: a learning loop that captures why the firm wins or loses competitive acquisitions and accumulates bid and sourcing intelligence to sharpen the next bid.
- **underwriting-backtest**: a learning loop that captures why realized deals beat or missed their original underwriting and accumulates that variance to calibrate future models.
- **ic-memo-intelligence**: a learning loop that captures what the investment committee decides and why — its standing conditions, revealed risk appetite, and precedent — and accumulates that decision memory so the next memo pre-empts the committee's conditions and cites precedent instead of relitigating it.
- **market-thesis**: building the firm's defensible market/sector view to focus screening and sourcing.

The eleventh sits off the lifecycle, because it applies anywhere on it:
- **one-off-deliverable**: one serious deliverable from a messy, unvetted source set — an IC memo, a hold/sell case, a diligence brief, a one-time letter. Inventory the sources, review, then draft. The non-recurring cousin of the document-production workflows; reach for it when the deliverable matters but maps to no recurring cycle.

Every file is annotated with what layer it sits on, why it exists, and what would change if your workflow were different. The layer named here is the file's ICM context layer (L0–L4), which says when the file loads; see Constraint 03 (Context Hygiene) for the full model. Each one also carries an "AI vs. Platform" decision map showing which steps belong to AI, which to a deterministic tool, and which to your enterprise data foundation. These are reference pieces, not templates. Study them, then build your own. The examples name commercial-real-estate systems of record (Argus, Yardi, MRI, RealPage); a PE deal team should read those as placeholders for its own deal model and portfolio or fund-accounting systems.

Five architectures ship with a fully worked `_example/` so you can see finished output, not just the empty shape:
- **lp-reporting/_example**: a complete quarterly-letter cycle for a fictional fund — verified data pack, draft, and final letter. The draft-to-final diff shows the compliance pass adding the disclosure footer, and every figure traces to the data pack.
- **deal-win-loss-learning/_example**: a populated learning-loop store — three resolved bids (one won on certainty, two lost where the broker cited price) plus the rolled-up `patterns.md`. This is the one to read to understand the loop shape, where the deliverable is the accumulating store rather than any single record, and to see the stated-vs-assessed-reason defense catch broker spin in action.
- **underwriting-backtest/_example**: a populated learning-loop store — three realized deals that each "beat" their underwriting, where the rolled-up `patterns.md` shows the beat was dominated by exit-cap compression the firm did not create while its multifamily lease-up assumptions ran optimistic every time. Read it to see the skill-vs-luck defense keep a market tailwind from being banked as underwriting edge.
- **ic-memo-intelligence/_example**: a populated learning-loop store — three IC decisions (two approvals-with-conditions and a decline) whose rolled-up `patterns.md` reveals the committee's hard ~65% leverage ceiling, an emerging DSCR-stress condition, and a recurring lease-up concern. Read it to see how decision memory compounds and the stated-vs-inferred-rationale defense keep a tidy rationale the committee never gave from becoming false precedent.
- **one-off-deliverable/_example**: a hold/sell case built from a deliberately messy source set — two model versions that disagree on the exit cap, a stale appraisal, a broker's value, and a rent roll the model references but nobody included. Read the inventory and the conflict log to see the provenance pass surface the disagreement instead of blending it, then the memo cite every figure to its source and flag what the pile does not support.

### /skill-starters (11 diagnostic skills)
Skills that ask before they build. Each one opens with diagnostic questions about your specific workflow, then assembles a workspace skeleton based on your answers. The decomposition logic is built in. Your answers provide the specifics. One per architecture: deal-screening-builder, deal-pipeline-builder, asset-management-builder, disposition-builder, lp-reporting-builder, lp-inquiries-builder, deal-win-loss-learning-builder, underwriting-backtest-builder, ic-memo-intelligence-builder, market-thesis-builder, one-off-deliverable-builder.

## The Principle Behind All of This

Every repeatable workflow has steps. Every step has a scope of information it actually needs. The job is to match those two things so each step runs with signal instead of noise.

Whatever your environment supports for separating information is your implementation layer. Folders, tabs, knowledge sources, your data room, SharePoint libraries. The medium changes. The logic does not.

The question is always the same: does this piece of information belong at this step, or am I just carrying it because I do not know where else to put it?

## Glossary

A few terms used throughout the toolkit, in plain language:

- **ICM (Interpreted Context Methodology)** — the discipline of organizing a workspace's files into layers (L0–L4) so each step loads only what it needs. The "Note on Two Kinds of 'Layer'" below explains the layers.
- **Stage contract** — the `CONTEXT.md` inside a numbered stage folder. It states what that stage loads, what it produces, and what "done" looks like. It is the instruction sheet for one step of the workflow.
- **Deterministic** — a task with one correct answer that does not require judgment (calculating a waterfall, summing a rent roll). Deterministic work belongs in a spreadsheet or the platform, not in a language model.
- **Waterfall** — here, the *fund waterfall*: the rules governing how returns are split between the GP and its LPs. It is deterministic math, owned by the fund-accounting platform.
- **VLOOKUP** — a spreadsheet function that looks up a value in a table by matching a key. Used as shorthand for "ordinary spreadsheet work," the kind of task that does not need AI.
- **MCP server** — a connector that lets Claude read from an outside system (a database, a drive, a CRM) through a defined interface, without custom code. "MCP" is the Model Context Protocol that standardizes those connectors.
- **n8n / Zapier / Make** — workflow-automation platforms that run rule-based "if this, then that" steps. They are the 30% rule-based layer, between traditional software and a language model.

## A Note on Two Kinds of "Layer"

This toolkit uses the word *layer* in two unrelated ways. Keep them separate:

- **Context layers (L0–L4)** describe *when* a file loads — the always-on map, routing, the stage contract, reference material, the working files. Constraint 03 (Context Hygiene) defines them.
- **Solution layers (60/30/10)** describe *what kind of tool* should solve a problem — traditional software, a rule-based system, or a language model.

(A third, local use also appears: the "Layer 1/2/3" *section headings* inside each constraint file label that file's three-part structure — traditional solutions, existing tools, the architectural fix — and have nothing to do with the two kinds above.)

The rest of this section is about the second kind.

Roughly 60% of the problems people throw at AI are better solved by traditional tools, databases, or established processes. Another 30% are handled well by rule-based systems, existing skills, or automation workflows. Only about 10% genuinely benefit from the probabilistic reasoning that a language model provides.

If you find yourself reaching for Claude to recalculate a waterfall that a spreadsheet handles, you are spending tokens on something deterministic. The constraint files will tell you when that is the case.

---

Built by Matt Weigand. Released under the [MIT License](LICENSE) — clone, customize, and use it freely.
