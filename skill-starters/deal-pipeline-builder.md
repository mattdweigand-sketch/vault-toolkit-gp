# SKILL: Deal Pipeline Workspace Builder

## Description
Builds a customized acquisition workspace for a GP deal team. Asks diagnostic questions about how the firm sources, underwrites, and approves deals, then assembles a workspace with sourcing, diligence, IC, and close stages tailored to the firm's process.

## When to Use
When you run acquisitions through a multi-stage process with a diligence period and an investment committee gate. This is for deals that take weeks to months, not for a quick screen.

## Process

### Phase 1: Diagnosis

Ask the following questions one at a time. Wait for each answer.

**Question 1: What do you acquire?**
"Describe the typical deal. Asset type (multifamily, industrial, office, a portfolio company), check size, structure (acquisition, recap, development), and hold. Be specific about what the firm is buying and why."

**Question 2: How do deals get sourced and screened?**
"How does an opportunity reach you, broker, off-market, marketed process? How do you decide whether to spend diligence dollars? Do you write a screen memo or thesis before committing, or do you dive into underwriting first?"

**Question 3: What is your IC process?**
"How does investment committee work? Is there internal underwriting review before IC? What does the committee need to see? How are conditions to close tracked after approval? How often does a deal go back for a retrade or more diligence?"

**Question 4: What kills deals?**
"Think about the deals that blew up in diligence or should never have advanced. What caused it? A thin thesis, a missed environmental issue, a financing fall-through, confirmation bias, broken assumptions? These failure modes are what the workspace is designed to catch."

**Question 5: What happens after close?**
"When a deal closes, how does it transition to asset management? Is there a handoff of the business plan and model, or does the deal team stay on it? What does asset management need on day one?"

**Question 6: What reference material do you reuse across deals?**
"Do you have underwriting standards, return hurdles, submarket comps, lender term sheets, or records from prior deals that apply across the board? List anything you pull from repeatedly."

### Phase 2: Assembly

Based on the answers:

1. Determine the stage structure. The default is four stages (sourcing, diligence, IC, close) but adjust based on their answers:
   - If they sign an LOI/PSA before diligence: add stage 01a_loi.
   - If a physical inspection or PCA is a gated step: add 02a_site-visit within diligence.
   - If they track the post-close business plan in the same workspace: add stage 05_asset-management.
   - If internal review and committee are distinct meetings: keep IC as one stage with two phases.

2. Create the folder structure. Numbered stages, _config/, _references/.

3. Write CLAUDE.md:
   - What this workspace is (their deal type and process)
   - Structure map
   - How to use (one deal = one copy of this workspace)
   - Key decisions (especially around the thesis and the IC gate, citing their failure mode answers as rationale)

4. Write CONTEXT.md routing file:
   - Stage map with decision checkpoint column
   - How stages connect, including the IC → diligence loop for conditions
   - Reference material locations

5. Write stage contracts:
   - Sourcing: screening process based on how they currently decide to commit diligence dollars. Include their failure modes as deal breakers the sourcing stage tests.
   - Diligence: their underwriting and verification process with a self-check against the thesis conditions.
   - IC: two-phase process (internal review then committee). Include their typical retrade/return frequency as a guideline.
   - Close: closing checklist and asset management handoff based on their post-close description.

6. Create config files:
   - deal-brief.md: template for capturing the original opportunity
   - deal-terms.md: template with their typical deal structure
   - investment-thesis.md: placeholder (produced by sourcing)

7. If they mentioned reusable reference material, create _references/ with placeholder files for each type. Add a note about a central reference library if they run many deals.

### Phase 3: Orientation

Walk the user through. Highlight:
- "The sourcing stage is designed to catch [their specific failure modes]. The investment thesis it produces is what the rest of the deal works from, not the broker's offering memo."
- "The IC stage has two phases. Internal review happens before committee. This catches problems when walking is still cheap."
- "The close stage includes an asset management handoff. If you skip it, asset management spends month one reverse-engineering the deal."
- "Each deal gets its own copy of this workspace. _references/ can be shared across deals. _config/ is always deal-specific and confidential."

### Recommended Constraints

Load these constraint files for a deal-pipeline workspace, and name them in the workspace CLAUDE.md so the deal team can find them. Load the one a stage needs when that stage runs, not all of them at once.

- **Constraint 06 (Layer Triage)** and **Constraint 09 (Platform Boundary)** — read first, with the team. They decide what AI does (thesis synthesis, risk narratives, drafting the IC memo), what a spreadsheet or the platform's engine does (the underwriting model, return math), and what the enterprise data foundation (Juniper Square) owns (the cap table, the system of record). The underwrite is deterministic work; AI writes about it, it does not compute it.
- **Constraint 01 (AI Writing Patterns)** — for the screen memo, IC memo, and asset management handoff. These are written deliverables that must read clean.
- **Constraint 02 (Output Drift)** — to keep each stage's output matched to what the next stage needs. The "Done Looks Like" line in each stage contract is the anchor.
- **Constraint 08 (Handoff Readiness)** — the close stage hands the deal to asset management. This constraint is the test for whether that handoff survives without the deal team in the room.
- **Constraint 07 (Scaling vs. Automating)** — only if the firm runs many deals a year. It decides what to template versus automate before they build the same workspace by hand ten times.

## Important Notes
- Sourcing is the highest-value stage in the workspace. If the firm currently underwrites before forming a thesis, explain why a tested thesis prevents their specific failure modes (using their own answers) but do not force a heavy process. Suggest a lightweight screen memo they can try.
- The investment thesis is the most important document in the workspace. It is produced in sourcing and consumed by every subsequent stage. Emphasize that spending diligence dollars without a thesis is the root cause of most deals that blow up late.
- For teams with multiple members, note where handoffs between stages matter (underwriter to IC presenter, deal team to asset manager), not just the final close handoff.
- If the firm runs many similar deals, suggest a "master workspace" template that gets copied per deal rather than rebuilt each time.
