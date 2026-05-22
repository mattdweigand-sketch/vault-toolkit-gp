# SKILL: Asset Management Workspace Builder

## Description
Builds a customized portfolio-monitoring workspace by asking diagnostic questions about how a firm tracks owned assets against their business plans, then assembling a folder structure, stage contracts, and config files based on the answers.

## When to Use
When an asset-management or portfolio team reviews owned assets on a recurring cycle and wants a consistent business-plan-vs-actual review — with a watchlist — that feeds the investment committee and downstream LP reporting.

## Process

### Phase 1: Diagnosis (ask before building)

Ask the following questions one at a time. Wait for each answer before proceeding.

**Question 1: What do you monitor, and on what cycle?**
"Which assets or portfolio segments do you review, and how often — monthly, quarterly? What does a review cover?"

**Question 2: Where does the operating data come from?**
"Where do actuals live — Yardi, MRI, RealPage, asset reports from operators? Who pulls and reconciles them?"

**Question 3: What do you measure against?**
"What is the baseline — the underwriting or business-plan targets you grade actuals against? Where do those targets live today, and how often are they revised?"

**Question 4: What puts an asset on the watchlist?**
"What variance or condition makes an asset worth flagging — how far behind plan, a covenant concern, a valuation risk? What thresholds do you use, even informally?"

**Question 5: Who consumes the review, and in what forms?**
"Who reads it — the IC, the partners? Do you also produce JV/co-GP partner reports or distressed-asset memos from the same analysis?"

### Phase 2: Assembly

Based on the answers, build the workspace:

1. Create the folder structure: three stages (data, review, report), plus _config/ and _prompts/.
2. Write CLAUDE.md: what this is, current state, structure map, how to use. Note that the data stage gates the others and that this workspace can host JV/co-GP and watchlist variants.
3. Write CONTEXT.md: the stage map, how stages connect, and the AI-vs-Platform table (property systems own actuals; the model owns the variance narrative; returns and marks come from Argus/your model and valuation process).
4. Write a CONTEXT.md for each stage.
5. Create config templates: business-plan-targets.md (the measuring stick, synced from acquisition/deal-pipeline), review-standards.md (variance thresholds + watchlist criteria + never-do list), reporting-format.md (base internal review plus the JV/co-GP and watchlist variants if they produce them). Populate from their answers.
6. Set up _prompts/ for the recurring analysis fragments.

### Phase 3: Orientation

After building, walk the user through:
- "Here is what I built and why each piece exists."
- "The data stage gates everything — no analysis until actuals tie to source. The business plan in _config is your measuring stick; without it, variance analysis is meaningless."
- "The review stage's job is variance *with attribution* — not 'NOI missed by 6%' but why, and whether it is timing or structural."
- "The model never recomputes a return or sets a mark. Those come from your model and valuation process (Constraint 09)."
- "If you produce JV/co-GP or watchlist reports, those are format variants in reporting-format.md, not separate workspaces — same figures and analysis, different framing."

## Important Notes
- Do not build before completing the diagnosis. The questions are the skill.
- The business-plan targets are the highest-value config. A review with no baseline to measure against is just a restatement of the data.
- Keep figures out of the model's hands: it narrates and flags; the platform and the model own the numbers.
- Load and name the constraints this workflow uses: 02 (Output Drift), 04 (Session Consistency), 08 (Handoff), 10 (Source Provenance) for unvetted asset reports, plus the universal 06 and 09.
- Always annotate files with their ICM layer (L0–L4).
