# The GP Operating Toolkit

For private equity and commercial real estate GPs who want to build with AI instead of just use it. It helps your firm put AI where it belongs: investment judgment, portfolio intervention, investor communication, source control, and firm memory. It does not rebuild the systems of record that already hold your data.

**Who this is for:** anyone at a GP firm who runs high-judgment recurring work (IC prep, diligence, portfolio intervention, LP issue prep, market thesis, or firm learning loops) and wants AI to speed it up without giving it free run of the firm's data or final say over decisions. In practice that means the COO, Head of IR, CFO or controller, acquisitions or portfolio lead, or whoever owns AI and technology.

**What this is not:** a replacement for your fund-accounting or fund-administration platform, your investor-management system, your deal pipeline, or your CRM; a data warehouse; a compliance approval system; a prompt library; or a way to skip human review.

## What this is

A setup guide for putting AI to work at a GP firm in ways that are actually useful, compliant, and secure.

Most firms land at one of two extremes: avoiding AI because they cannot control it, or pointing it at everything and trusting output they cannot verify. This guide is the path between them. It helps your team stand up AI workflows for the judgment layer above the platforms you already use: pressure-testing an IC memo, mapping diligence evidence, explaining portfolio variance, preparing LP narratives, and capturing what the firm learns. It keeps your systems of record, not the model, as the source of truth.

It works in three parts: reference files that show where AI genuinely helps and where it does not (constraints), example workspaces you can copy and study (architectures), and skills that interview you and assemble a starting workspace from your answers (skill-starters). Together they take you from "we should use AI" to a working, governed setup.

There are no copy-paste templates here. The value is the structure underneath: knowing which work belongs to AI and which belongs to your platform, database, or established software, and setting it up so the result holds up to an LP or an auditor.

## The principle behind all of this

Every repeatable workflow has steps. Every step has a scope of information it actually needs. The job is to match those two things so each step runs with signal instead of noise.

Whatever your environment supports for separating information is your implementation layer. Folders, tabs, knowledge sources, your data room, SharePoint libraries. The medium changes. The logic does not.

The question is always the same: does this piece of information belong at this step, or am I just carrying it because I do not know where else to put it?

## How the layers stay separate

The toolkit keeps methodology, firm context, and live workflow context in different places:

- `_shared-config/` is firm-level truth: the firm profile, voice, setup progress, and reusable learnings.
- `workspaces/` is workflow-level operating context: the live deal, fund, reporting cycle, inquiry queue, or learning loop.
- `architectures/`, `constraints/`, and `skill-starters/` are toolkit methodology: the reusable templates, principles, and builders.
- After finalize, methodology moves to `_kit/`; firm context and live workspaces stay visible at the root.

## Most work is not an AI task

Roughly 60% of what people throw at AI is better handled by traditional software, databases, or an established process. Another 30% suits rule-based automation or a prebuilt routine. Only about 10% genuinely needs the judgment a language model brings.

So if you are reaching for Claude to recalculate a waterfall your fund-accounting platform already owns, you are spending tokens on something deterministic. The constraint files tell you when that is the case.

For a GP, this filter matters because strong platforms already exist. Juniper Square and similar systems own fund administration, investor records, data rooms, investor reporting, capital activity, portals, entitlements, and audit trails. Dealpath, DealCloud, and other investment platforms own pipeline state, relationship history, deal workflows, and execution tracking. Chronograph, iLevel-style tools, Canoe, and portfolio-monitoring platforms own collection, extraction, structured portfolio data, dashboards, and valuation workflows.

The toolkit should not compete with those systems. If a platform can own the record, workflow state, entitlement, calculation, or audit trail, leave it there. Use this toolkit for the judgment layer above the platform: source interpretation, decision framing, narrative, exception handling, and institutional memory.

The highest-leverage GP uses of AI are therefore:

- **Investment judgment:** deal thesis, diligence evidence, IC pressure testing, bid strategy, market thesis.
- **Portfolio intervention:** variance attribution, watchlist diagnosis, action planning, hold / sell / refinance framing.
- **Investor communication:** LP narratives, issue prep, likely questions, response framing around platform-verified data.
- **Source control:** data-room maps, authority ranking, conflict logs, source-backed deliverables.
- **Firm memory:** underwriting backtests, IC precedent, win/loss learning, LP objection learning, post-mortems.

The rule is simple: platform for the record, deterministic tools for the math, rules for routing, AI for judgment, and humans for approval.

## Your data

The toolkit is plain files on your machine. It has no server or database of its own and uploads nothing on its own. Setup scopes each step to just the files it needs, so the model is never pointed at everything at once.

Two caveats. Whatever AI tool you use sends the context it reads to that tool's model provider, so apply your firm's policy on what may go to which model, and use an enterprise or zero-retention plan if your data calls for it. And your systems of record stay the source of truth: you connect them, the workflows read from them, and nothing writes back or goes to an LP without a human in the loop.

## How to use this

### Before you start (if you have never used an AI agent)

**What you need:** an AI coding assistant backed by a capable model (a Claude plan, or Cursor, Copilot, Codex, or the Gemini CLI with their own model), and this repo. No server, no database, no Git required. The toolkit is free; you pay only for the AI tool you use. If you do not have an agent yet, set one up once:

1. **Get an AI agent.** Install [Claude Code](https://claude.com/claude-code) or open [claude.ai/code](https://claude.ai/code). (Cowork, Cursor, or VS Code with an AI extension also work.) If your firm already has one, use that.
2. **Download this repo.** Click the green **Code** button, then **Download ZIP**, and unzip it. (Know Git? Clone it instead.)
3. **Open the folder in your agent** and say `Run setup`.

Setup asks a few questions about your firm and builds your first workspace; later, say `add a workflow` to build another. You never open or edit a file yourself.

**Any agentic tool works:** Claude Code, Cursor, Codex, Copilot (agent mode), or the Gemini CLI. Anything that can read this repo and act on it qualifies. Claude Code loads `CLAUDE.md`, which imports `AGENTS.md`; in other tools, tell the agent to read `AGENTS.md` first. A plain browser chat (ChatGPT, Gemini) cannot run setup, but can still use the reference material below.

Everything below is background you can skip.

---

**Just want the reference material?** You do not need setup. The constraint files are portable: open whichever matches your problem, a couple at a time, not all at once. They work anywhere: a Claude Code, Cursor, or VS Code workspace; as knowledge sources in Claude Projects; or pasted into ChatGPT, Copilot, or any chat.

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

At the root are the toolkit folders, shared firm config, plus three files that run the toolkit and that you rarely edit: `AGENTS.md` (the canonical agent instructions), `CLAUDE.md` (the Claude Code wrapper), and `SETUP.md` (the engine that builds and adds workflows). Workflows you build land in `workspaces/`.

```
AGENTS.md        canonical agent instructions
CLAUDE.md        Claude Code wrapper that imports AGENTS.md
SETUP.md         the engine that builds and adds workflows
_shared-config/  firm profile, voice, setup progress, and learnings
constraints/     the principles (10 files)
architectures/   core and variant workflow architectures
skill-starters/  the builders setup runs
workspaces/      the workflows you build
```

### [/constraints](constraints/) (10 files)
The constraints are the principles for getting real work out of AI instead of plausible-looking output. Each of the ten takes one way AI predictably breaks down (writing in a flat, generic voice, losing track of your instructions in a long chat, or trusting a document it should not) and tells you why it happens and how to keep it reliable. Each ends with a few questions that tailor the fix to how your firm works.

These are foundational principles of AI and computer science. They hold for anyone working with a language model.

If you read only two, read [constraint 06 (Layer Triage)](constraints/06-layer-triage.md) and [constraint 09 (Platform Boundary)](constraints/09-platform-boundary.md). The first tells you which problems at your firm are even worth pointing AI at. The second tells you what to build yourself and what to leave to your platform. Those are the two calls most firms get wrong.

### [/architectures](architectures/) (core and variant workflows)
Real folder structures, one per GP workflow, that you copy and adapt. The current examples cover the lifecycle, but the design principle is narrower: architectures should capture the high-judgment 10% that platforms do not already own.

Each architecture should map to one of five shapes. A **gated decision pipeline** moves one item through go/no-go stages to a decision. A **recurring operations queue** runs intake, process, deliver, per request. **Recurring document production** turns verified data into a drafted, distributed document on a cycle. A **learning loop** captures an outcome, analyzes it, and reads it back so the work compounds. **Source provenance** inspects and ranks a source set before anyone relies on it.

The highest-value architecture candidates are IC pressure testing, diligence evidence mapping, underwriting backtests, portfolio intervention, hold / sell / refinance decisions, market thesis to investment-box updates, LP narrative and issue prep, and firm memory loops. Workflows like DDQ execution, investor records, capital activity, pipeline tracking, dashboards, data extraction, and fund calculations belong in the platforms built for them. The toolkit can support the judgment around those workflows, but should not rebuild them.

Not one of the listed workflows? Say "add a workflow" and setup classifies yours by shape and builds from the nearest; if it fits no shape, it builds from scratch using constraints 03, 06, 08, and 09. Each architecture also maps, step by step, what is the AI's job, what a tool or automation handles, and what belongs to your platform of record. The software names (Argus, Yardi, MRI, RealPage) are real-estate stand-ins; a PE firm reads its own deal model and fund-accounting systems.

The active `underwriting-backtest` architecture ships with a fully worked `_example/` so you see finished output, not the empty shape. Older worked examples are preserved under `architectures/_variants/` for reference and migration.

### [/skill-starters](skill-starters/) (diagnostic skills)
Skills that ask before they build. Each opens with diagnostic questions about your workflow, then assembles a workspace skeleton from your answers: the decomposition logic is built in, your answers supply the specifics. Core builders are `ic-pressure-test`, `diligence-evidence-map`, `portfolio-intervention`, `hold-sell-refi`, `market-thesis-to-investment-box`, `lp-narrative-and-issue-prep`, `underwriting-backtest`, and `firm-memory-loop`. Older lifecycle examples are archived under `_variants/` for reference, not primary routing.

---

Built by Matt Weigand. Released under the [MIT License](LICENSE). Clone, customize, and use it freely.
