# SKILL: Deal Win/Loss Learning Workspace Builder

## Description
Builds a customized learning-loop workspace by asking diagnostic questions about how a firm could capture and learn from why it wins or loses competitive acquisitions, then assembling a folder structure, stage contracts, config files, and a store based on the answers.

## When to Use
When a firm wants its bidding to compound — to systematically learn why it wins or loses competitive processes and turn that into bid and sourcing intelligence — rather than relearning the same lessons one deal at a time. More deals won means more capital deployed, bigger funds, and a better track record. This is a learning loop, not a deal pipeline or CRM; it explains *why* a competitive outcome happened and remembers.

## Process

### Phase 1: Diagnosis (ask before building)

Ask the following questions one at a time. Wait for each answer before proceeding.

**Question 1: How do you learn you won or lost?**
"What competitive processes do you bid in, and how do you typically learn you won or lost — a broker debrief, public record, the grapevine? This establishes the trigger and the resolution signal."

**Question 2: Where does the bid record and the clearing price live?**
"Where is the record of what we bid — our screen, underwrite, LOI — and where does the winning/clearing price come from? Your deal system, broker relationships, public data? This is the governed source; the model must never invent it."

**Question 3: What actually decides your wins and losses?**
"What dimensions decide your competitive outcomes — price, certainty/speed of close, structure, financing, relationship? This seeds both the canonical question bank and the decisive-dimension tag."

**Question 4: Which brokers and intermediaries do you transact with repeatedly?**
"Who are the brokers and intermediaries you deal with again and again? This becomes a controlled list — which intermediaries you win through, and whose debrief feedback proves reliable, are two of the highest-value patterns this store surfaces."

**Question 5: Who owns the 'why we lost' call, and how skeptical are you of broker feedback?**
"Who internally owns the final read on why we won or lost — the deal lead, head of acquisitions? And how much do you trust a broker's stated reason? This sets the human-validation gate and how hard the workspace pushes on stated-vs-assessed reasons."

**Question 6: What would you change if you knew exactly why you win and lose?**
"If, across 50 processes, you knew exactly why you win and lose, what would you change — which processes you chase, how you bid, which relationships you build? This defines the payoff and who consumes the store."

### Phase 2: Assembly

Based on the answers, build the workspace:

1. Create the folder structure: three stages (signal, analysis, capture), plus _config/ and a _store/ folder with records/ and patterns.md. The _store/ is the deliverable — make it visible.
2. Write CLAUDE.md: what this is, the learning-loop shape and how it differs from a linear pipeline (the output feeds back into the store), current state, structure map, how to use. Call out the broker-spin guardrail in Key Decisions.
3. Write CONTEXT.md: the stage map, how the loop closes (capture writes the store; signal and analysis read it back), how the store feeds deal-pipeline sourcing and bid strategy, and the AI-vs-Platform table (the deal system and market data own what happened; the model proposes the why and keeps stated vs. assessed distinct; a human validates it).
4. Write a CONTEXT.md for each stage.
5. Create config templates: win-loss-questions.md (the canonical set — the most important file, with the stated-vs-assessed question load-bearing), deal-taxonomy.md (controlled tags including the controlled broker list), store-schema.md (record shape with our-bid-vs-clearing-price and gap, patterns structure, privacy handling). Populate from their answers.
6. Set up _store/ with the README and an empty records/ folder.

### Phase 3: Orientation

After building, walk the user through:
- "Here is what I built and why each piece exists."
- "This is a loop, not a pipeline. The deliverable is the store, not any single write-up. Resist perfecting one record; invest in making records comparable so the corpus reveals patterns."
- "Comparability is the whole game — every analysis answers the same canonical questions in the same shape and uses the same taxonomy tags (Constraint 04). Changing the questions breaks comparability with prior records."
- "Broker 'why you lost' feedback is often a polite fiction. The stated-vs-assessed question and the human validation gate are the defenses against capturing broker spin as fact and poisoning the store."
- "A human — the deal lead / head of acquisitions — validates the why before it is captured. A confident, wrong 'why' in the store skews future bids."
- "Read patterns.md before the next bid or before chasing a process — and feed it to your deal-pipeline sourcing and bid strategy. That is the loop paying off."

## Important Notes
- Do not build before completing the diagnosis. The questions are the skill.
- The canonical win/loss questions are the highest-value config. Spend the most time here; a loose or shifting question set makes the store un-aggregatable. The stated-vs-assessed reason question is load-bearing — do not drop it.
- The broker/intermediary list is a controlled list on purpose. Two of the most valuable patterns (which intermediaries we win through, whose feedback proves reliable) require a stable broker vocabulary.
- This is sensitive competitive intelligence — our bid behavior, our gap to clearing, our read on named broker relationships. Address access and handling in store-schema.md.
- It does not replace the deal pipeline or CRM — it rides on them. The record of what happened is the platform's; this workspace adds the why and the memory. The loop is triggered by deal-pipeline outcomes and pays back into sourcing and bid strategy.
- Load and name the constraints this workflow uses: 04 (Session Consistency) — the load-bearing one, 03 (Context Hygiene), 08 (Handoff), plus the universal 06 and 09.
- Always annotate files with their ICM layer (L0–L4); note that _store/ is an L3/L4 hybrid — the signature of the learning-loop shape.
