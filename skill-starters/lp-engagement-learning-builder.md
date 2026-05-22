# SKILL: LP Engagement Learning Workspace Builder

## Description
Builds a customized learning-loop workspace by asking diagnostic questions about how a firm could capture and learn from why LPs commit or pass, then assembling a folder structure, stage contracts, config files, and a store based on the answers.

## When to Use
When a firm wants its fundraising to compound — to systematically learn why LPs commit or decline and turn that into intelligence that sharpens the next raise — rather than restarting the learning every fund. This is a learning loop, not a CRM; it explains *why* and remembers.

## Process

### Phase 1: Diagnosis (ask before building)

Ask the following questions one at a time. Wait for each answer before proceeding.

**Question 1: Do you debrief why an LP committed or passed today?**
"When an engagement resolves, do you capture why — formally, informally, or not at all? If you do, what happens to it?"

**Question 2: Where does the engagement record live?**
"Where is the history of an LP engagement — touchpoints, meetings, materials, the outcome? Is it in your CRM, and how complete is it?"

**Question 3: What would you want to know about every engagement?**
"If you could answer the same set of questions about every LP that commits or passes, what would those questions be? This becomes the canonical debrief set that makes records comparable."

**Question 4: How do you segment LPs?**
"How would you categorize LPs so patterns can aggregate — type (pension, endowment, family office, etc.), check size, how they were sourced?"

**Question 5: Who validates the why, and who reads the patterns?**
"Who would confirm the causal read before it becomes institutional memory? And who would read the accumulated patterns, and when — before a raise, before prepping a prospect?"

### Phase 2: Assembly

Based on the answers, build the workspace:

1. Create the folder structure: three stages (signal, analysis, capture), plus _config/ and a _store/ folder with records/ and patterns.md. The _store/ is the deliverable — make it visible.
2. Write CLAUDE.md: what this is, the learning-loop shape and how it differs from a linear pipeline (the output feeds back into the store), current state, structure map, how to use.
3. Write CONTEXT.md: the stage map, how the loop closes (capture writes the store; signal and analysis read it back), how the store feeds other workspaces, and the AI-vs-Platform table (the CRM owns what happened; the model proposes the why; a human validates it).
4. Write a CONTEXT.md for each stage.
5. Create config templates: debrief-questions.md (the canonical set — the most important file), segment-taxonomy.md (controlled tags for aggregation), store-schema.md (record shape, patterns structure, privacy handling). Populate from their answers.
6. Set up _store/ with the README and an empty records/ folder.

### Phase 3: Orientation

After building, walk the user through:
- "Here is what I built and why each piece exists."
- "This is a loop, not a pipeline. The deliverable is the store, not any single write-up. Resist perfecting one record; invest in making records comparable so the corpus reveals patterns."
- "Comparability is the whole game — every analysis answers the same canonical questions in the same shape (Constraint 04). Changing the questions breaks comparability with prior records."
- "A human validates the why before it is captured. A confident, wrong 'why' in the store poisons future decisions."
- "Read patterns.md before a raise or a prospect prep — and feed it to your capital-raising work. That is the loop paying off."

## Important Notes
- Do not build before completing the diagnosis. The questions are the skill.
- The canonical debrief questions are the highest-value config. Spend the most time here; a loose or shifting question set makes the store un-aggregatable.
- This is sensitive intelligence about named LPs. Address access and handling in store-schema.md.
- It does not replace the CRM — it rides on it. The record of what happened is the platform's; this workspace adds the why and the memory.
- Load and name the constraints this workflow uses: 04 (Session Consistency) — the load-bearing one, 03 (Context Hygiene), 08 (Handoff), plus the universal 06 and 09.
- Always annotate files with their ICM layer (L0–L4); note that _store/ is an L3/L4 hybrid — the signature of the learning-loop shape.
