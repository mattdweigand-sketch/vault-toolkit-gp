# SKILL: Deal Screening Workspace Builder

## Description
Builds a customized top-of-funnel screening workspace by asking diagnostic questions about how a firm sees and triages deal flow, then assembling a folder structure, stage contracts, and config files based on the answers.

## When to Use
When a firm sees far more opportunities than it pursues and wants to apply its investment criteria consistently and fast — reaching a defensible pursue/pass on each, and handing pursued deals cleanly to a full diligence process.

## Process

### Phase 1: Diagnosis (ask before building)

Ask the following questions one at a time. Wait for each answer before proceeding.

**Question 1: What deal flow do you see, and from where?**
"Roughly how many opportunities cross your desk, and through what channels — brokers, off-market, relationships, listing platforms? Where does the volume come from?"

**Question 2: What is your investment box?**
"What do you actually buy — asset types, markets, deal size, strategy, return profile? Just as important: what is an automatic no, regardless of price?"

**Question 3: How does a deal get screened today?**
"Walk me through what happens when an opportunity arrives. Who looks at it, what do they check, how long does it take, and what does a 'no' look like?"

**Question 4: What rough economics do you run at the screen stage?**
"Before committing to diligence, what quick numbers do you run, and on what assumptions? Where do market cap rates and financing assumptions come from?"

**Question 5: What happens to a pursue, and to a pass?**
"When you decide to pursue, where does it go and what does the next team need? When you pass, is the reason recorded anywhere?"

### Phase 2: Assembly

Based on the answers, build the workspace:

1. Create the folder structure. The default is three stages (capture, screen, decision), matched to their described process. Add _config/ for the box and criteria, and _references/ for the pass log and comps.
2. Write CLAUDE.md as the entry point: what this workspace is, current state, the structure map, and how to use it. Emphasize "kill fast" and that pursued deals hand off to the deal-pipeline workspace.
3. Write CONTEXT.md as the routing file: the stage map, how stages connect, the pursue→deal-pipeline handoff and pass→_references log, and the AI-vs-Platform table.
4. Write a CONTEXT.md for each stage from their process description.
5. Create config templates: investment-box.md, screening-criteria.md (deal-breakers + weighing rules + a pass-reason taxonomy), economics-assumptions.md (rough, dated). Populate from their answers.
6. Set up _references/ with the pass log structure.

### Phase 3: Orientation

After building, walk the user through:
- "Here is what I built and why each piece exists."
- "The point is speed: spend the least effort to reach a defensible pass, so attention goes to the deals that fit. Screen against the box in _config, not the broker's pitch."
- "The rough economics is a filter, not an underwrite. The real model lives in deal-pipeline. Never let a screen number masquerade as an underwrite (Constraint 09)."
- "Every pass is logged with a reason. That keeps screening consistent and, over time, shows you your own rejection patterns."
- "The first thing to populate is the investment box — a sharp box is what makes screening fast."

## Important Notes
- Do not build before completing the diagnosis. The questions are the skill.
- Keep it lean. The most common mistake is over-building a process whose entire value is speed. If they have fewer than three real steps, do not force three stages.
- Load and name the constraints this workflow uses: 02 (Output Drift) so screens are comparable, 10 (Source Provenance) for opportunities that arrive with a fuller data set, and the universal 06 and 09.
- Always annotate files with their ICM layer (L0–L4) so the user understands the architecture, not just the files.
