# The GP Operating Toolkit

For private equity and commercial real estate GPs who want to build with AI instead of just use it. It turns your firm's recurring deal, investor, and fund work into controlled AI workflows, without rebuilding the systems of record that already hold your data, and without the data-risk of pointing a model at everything at once.

**Who this is for:** anyone at a GP firm who runs the same work on a cycle (quarterly LP letters, deal screening, investor questions, fund reporting) and wants AI to speed it up without giving it free run of the firm's data or final say over decisions. In practice that means the COO, Head of IR, CFO or controller, acquisitions or asset-management lead, or whoever owns AI and technology.

**What this is not:** a replacement for your fund-accounting or fund-administration platform, your investor-management system, your deal pipeline, or your CRM; a data warehouse; a compliance approval system; a prompt library; or a way to skip human review.

## What this is

A setup guide for putting AI to work at a GP firm in ways that are actually useful, compliant, and secure.

Most firms land at one of two extremes: avoiding AI because they cannot control it, or pointing it at everything and trusting output they cannot verify. This guide is the path between them. It helps your team stand up AI workflows for the recurring work you already do, like drafting LP letters, screening deals, fielding investor questions, and building IC memos. It adds the controls that keep the model on your firm's voice and rules, keep your systems of record (not the model) as the source of truth, and keep it out of decisions it should not make.

It works in three parts: reference files that show where AI genuinely helps and where it does not (constraints), example workspaces you can copy and study (architectures), and skills that interview you and assemble a starting workspace from your answers (skill-starters). Together they take you from "we should use AI" to a working, governed setup.

There are no copy-paste templates here. The value is the structure underneath: knowing which work belongs to AI and which belongs to your platform, database, or established software, and setting it up so the result holds up to an LP or an auditor.

## The principle behind all of this

Every repeatable workflow has steps. Every step has a scope of information it actually needs. The job is to match those two things so each step runs with signal instead of noise.

Whatever your environment supports for separating information is your implementation layer. Folders, tabs, knowledge sources, your data room, SharePoint libraries. The medium changes. The logic does not.

The question is always the same: does this piece of information belong at this step, or am I just carrying it because I do not know where else to put it?

## Most work is not an AI task

Roughly 60% of what people throw at AI is better handled by traditional software, databases, or an established process. Another 30% suits rule-based automation or a prebuilt routine. Only about 10% genuinely needs the judgment a language model brings.

So if you are reaching for Claude to recalculate a waterfall your fund-accounting platform already owns, you are spending tokens on something deterministic. The constraint files tell you when that is the case.

## How to use this

### Before you start (if you have never used an AI agent)

You need an AI coding assistant to run this. It does the work; this repository is its instruction
manual. If you have never set one up, do these four things once, in order:

1. **Get an AI agent.** Install [Claude Code](https://claude.com/claude-code), or open
   [claude.ai/code](https://claude.ai/code) in your browser. (Cowork, Cursor, and VS Code with an AI
   extension also work.) If your firm already has one, use that.
2. **Download this repository.** On its web page, click the green **Code** button, then
   **Download ZIP**. Save it somewhere you can find (your Desktop is fine) and unzip it. (If you
   know Git, you can clone it instead. Same result.)
3. **Open the unzipped folder in your AI agent.** In Claude Code, that means pointing it at this
   folder. You do not need to open any individual file.
4. **Type:** `Run setup` and answer the questions it asks about your firm.

The agent reads its own instructions from here, walks you through a short set of questions about
your firm, and builds your first workspace. You do not need to read or edit any file yourself.
Everything below this box is background you can skip.

---

**Already have an AI agent?** Skip the download steps above. Open this folder in your agent and say
"Run setup." (In Claude Code that is all you need; in other tools, make sure the agent has read
`CLAUDE.md` first.) Setup asks a few questions about your firm and builds your first workspace. Later,
say "add a workflow" whenever you want to build another.

**Just want the reference material?** You do not have to run setup. The constraint files are portable:
open whichever one matches the problem you are hitting and work from it, a couple at a time rather than
all at once. They work in any tool: a Claude Code, Cursor, or VS Code workspace; as knowledge sources
in Claude Projects; or pasted into ChatGPT, Copilot, or any chat.

**Not technical?** Start by reading constraint 06 (Layer Triage): it sorts which problems at your firm
actually need AI versus your platform, database, or fund administrator. If you are deciding what to build
versus buy, read constraint 09 (Platform Boundary) next. Then go to whichever constraint matches your
most frequent frustration.

### The last step: finalize

Once you have built the workflows you need, finalize the repo. Say "finalize" (or "make this our
operating system") and the agent moves the toolkit itself (`SETUP.md`, `architectures/`,
`constraints/`, `skill-starters/`) into a `_kit/` folder, leaving only your firm's workspaces and
operating-system map at the root. The repo stops reading like a kit you are setting up and starts
reading like the system you run your firm on.

You keep building exactly as before: "add a workflow" still works, it just pulls from `_kit/`. And
it is fully reversible: finalize writes a `_kit/RESTORE.md` that puts everything back. Treat this as
the step that turns the toolkit into your operating system, not an afterthought.

## What is in here

### /constraints (10 files)
The constraints are the principles for getting real work out of AI instead of plausible-looking output. Each of the ten takes one way AI predictably breaks down (writing in a flat, generic voice, losing track of your instructions in a long chat, or trusting a document it should not) and tells you why it happens and how to keep it reliable. Each ends with a few questions that tailor the fix to how your firm works.

These are foundational principles of AI and computer science. They hold for anyone working with a language model.

If you read only two, read constraint 06 (Layer Triage) and constraint 09 (Platform Boundary). The first tells you which problems at your firm are even worth pointing AI at. The second tells you what to build yourself and what to leave to your platform. Those are the two calls most firms get wrong.

### /architectures (11 annotated workspaces)
Real folder structures you can copy, explore, and study, each modeled on a GP workflow. Every one is built on one of four structural shapes:
- **Gated decision pipeline**: advance one item through sequential go/no-go stages toward a terminal decision (deal-screening, deal-pipeline, disposition).
- **Recurring operations queue**: intake, process, deliver, repeated for each request that arrives (lp-inquiries).
- **Recurring document production**: verified data, then a drafted narrative, then distribution, on a cycle (lp-reporting, asset-management, market-thesis).
- **Learning loop**: capture an outcome, analyze why, write it to a store, then read it back next time so a repeated activity compounds (deal-win-loss-learning, underwriting-backtest, ic-memo-intelligence).

Ten of the eleven span the GP lifecycle:
- **deal-screening**: triaging inbound deal flow against the investment box: capture, screen, decide. Feeds deal-pipeline.
- **deal-pipeline**: an acquisition from sourcing through diligence, investment committee, and close.
- **asset-management**: portfolio monitoring: business-plan-vs-actual reviews and a watchlist; hosts JV/co-GP and special-servicing report variants.
- **disposition**: the exit: hold/sell decision through marketing and close to capital return.
- **lp-reporting**: investor communications from data through drafting through distribution.
- **lp-inquiries**: inbound LP questions between formal events: intake, resolve, respond.
- **deal-win-loss-learning**: why the firm wins or loses competitive bids, accumulated as bid and sourcing intelligence to sharpen the next one.
- **underwriting-backtest**: why realized deals beat or missed their original underwriting, accumulated to calibrate future models.
- **ic-memo-intelligence**: what the investment committee decides and why (standing conditions, revealed risk appetite, precedent), so the next memo pre-empts the committee's conditions and cites precedent instead of relitigating it.
- **market-thesis**: building the firm's defensible market/sector view to focus screening and sourcing.

The eleventh sits off the lifecycle, because it applies anywhere on it:
- **one-off-deliverable**: one serious deliverable from a messy, unvetted source set: an IC memo, a hold/sell case, a diligence brief, a one-time letter. Inventory the sources, review, then draft. The non-recurring cousin of the document-production workflows; reach for it when the deliverable matters but maps to no recurring cycle.

**If your workflow is not one of the eleven, you are not stuck.** The eleven are not a fixed catalog; they are instances of the four shapes above, and most GP work is a variant of one. Classify your work by shape first, then copy the nearest architecture and run its builder: the decomposition carries over, only the specifics change. If it fits no shape at all, the setup engine builds a fresh workspace from scratch, using constraints 06 (Layer Triage), 03 (Context Hygiene), 08 (Handoff Readiness), and 09 (Platform Boundary) as the recipe. Either way you do not do this by hand: say "add a workflow" or "build a &lt;workflow&gt;," and setup classifies the work and assembles it with you.

Each architecture also marks, step by step, what is the AI's job, what a deterministic tool or automation should handle, and what belongs to your platform of record where the data lives. The examples use real-estate software names (Argus, Yardi, MRI, RealPage) as stand-ins; a PE firm should read those as its own deal model and fund-accounting systems.

Five architectures ship with a fully worked `_example/` so you can see finished output, not just the empty shape:
- **lp-reporting/_example**: a full quarterly-letter cycle for a fictional fund: data pack, draft, final letter. The draft-to-final diff shows the compliance pass adding the disclosure footer, and every figure traces back to the data pack.
- **deal-win-loss-learning/_example**: three resolved bids (one won on certainty, two lost to a broker citing price) plus the rolled-up `patterns.md`. Read this one to understand the loop shape, where the deliverable is the accumulating store rather than any single record, and to watch the stated-vs-assessed-reason check catch broker spin.
- **underwriting-backtest/_example**: three realized deals that each "beat" their underwriting, where `patterns.md` shows the beat came from exit-cap compression the firm did not create, while its multifamily lease-up assumptions ran optimistic every time. The skill-vs-luck check keeps a market tailwind from being banked as underwriting edge.
- **ic-memo-intelligence/_example**: three IC decisions (two approvals-with-conditions, one decline) whose `patterns.md` reveals the committee's hard ~65% leverage ceiling, an emerging DSCR-stress condition, and a recurring lease-up concern. The stated-vs-inferred-rationale check keeps a rationale the committee never gave from becoming false precedent.
- **one-off-deliverable/_example**: a hold/sell case from a deliberately messy source set: two models that disagree on the exit cap, a stale appraisal, a broker's value, and a rent roll the model cites but nobody included. The inventory and conflict log show the provenance pass surfacing the disagreement instead of blending it; the memo then cites every figure to its source and flags what the pile does not support.

### /skill-starters (11 diagnostic skills)
Skills that ask before they build. Each opens with diagnostic questions about your workflow, then assembles a workspace skeleton from your answers: the decomposition logic is built in, your answers supply the specifics. One per architecture: deal-screening-builder, deal-pipeline-builder, asset-management-builder, disposition-builder, lp-reporting-builder, lp-inquiries-builder, deal-win-loss-learning-builder, underwriting-backtest-builder, ic-memo-intelligence-builder, market-thesis-builder, one-off-deliverable-builder.

## Glossary

A few terms used throughout the toolkit, in plain language:

- **ICM (Interpreted Context Methodology)**: the discipline of organizing a workspace's files into layers (L0–L4) so each step loads only what it needs. Constraint 03 (Context Hygiene) defines the layers.
- **Stage contract**: the `CONTEXT.md` inside a numbered stage folder. It states what that stage loads, what it produces, and what "done" looks like. It is the instruction sheet for one step of the workflow.
- **Deterministic**: a task with one correct answer that does not require judgment (calculating a waterfall, summing a rent roll). Deterministic work belongs in your platform, database, or established software, not in a language model.
- **MCP server**: a connector that lets Claude read from an outside system (a database, a drive, a CRM) through a defined interface, without custom code. "MCP" is the Model Context Protocol that standardizes those connectors.
- **n8n / Zapier / Make**: workflow-automation platforms that run rule-based "if this, then that" steps. They are the 30% rule-based tier, between traditional software and a language model.

---

Built by Matt Weigand. Released under the [MIT License](LICENSE). Clone, customize, and use it freely.
