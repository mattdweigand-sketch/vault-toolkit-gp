# Workflow: Deal Pipeline

## Overview
Four-stage acquisition pipeline: Sourcing → Diligence → IC → Close. Each stage has a decision checkpoint. The sourcing stage is non-negotiable. Skipping it is the single most common cause of money lost in diligence on a deal that never had a thesis.

## Stage Map

| Stage | Purpose | Key Inputs | Output Location | Decision Checkpoint |
|---|---|---|---|---|
| 01_sourcing | Screen the opportunity, set the thesis | Offering memo, market data, deal terms | 01_sourcing/output/ | Go / no-go on spending diligence dollars |
| 02_diligence | Underwrite and verify | Investment thesis, third-party reports, data room | 02_diligence/output/ | Findings either confirm or break the thesis |
| 03_ic | Internal review then committee | Underwriting, DD findings, risk register | 03_ic/output/ | Committee approves, declines, or sends back |
| 04_close | Close and transition | Approved IC memo, final terms | 04_close/output/ | Deal funds and transitions to asset management |

## How Stages Connect
- 01 → 02: Sourcing produces an investment thesis and a screen memo. Diligence works from the thesis, not from the broker's offering memo. The offering memo is what the seller wants you to believe. The thesis is what you need to prove. These are often different.
- 02 → 03: Diligence produces the underwriting and a risk register. IC evaluates it first internally (against underwriting standards and the thesis), then at committee. The committee either approves for close or sends it back with specific conditions.
- 03 → 04: IC produces an approved memo. Close executes the transaction and packages the handoff to asset management.
- 03 → 02 (loop): If IC raises conditions (a price retrade, a missing report, an unresolved risk), they go back to diligence as a scoped work item, not as a vague "look into it." The IC stage should produce specific, actionable conditions.

## Reference Material
- _config/deal-brief.md: The original opportunity (offering memo, teaser, broker email). Kept for reference but not used as the working specification after sourcing is complete.
- _config/deal-terms.md: LOI/PSA terms, price, structure, timeline, key dates.
- _config/investment-thesis.md: Produced in sourcing. The working specification for the deal.
- _references/: Underwriting standards, market comps, prior deal records from similar assets.

## When to Add Stages
- **01a_loi** before diligence: If the process requires a signed LOI or PSA before diligence dollars are committed.
- **02a_site-visit** within diligence: If the asset requires a physical inspection or property condition assessment as a gated step before full underwriting.
- **05_asset-management** after close: If the team wants the post-close business plan tracked in the same workspace rather than handed off entirely.

## AI vs. Platform: Where Each Step Lives

Before you point AI at this workflow, decide what AI does, what a deterministic tool does, and what your enterprise platform must own. The rule: rely on your platform for the data and the record, use AI for the language and the judgment. See Constraint 09.

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| Deal and document data, security masters, the system of record | Platform / data foundation | Enterprise platform (fund admin and the software underneath it) |
| Return math, model outputs, basis and yield calculations | Deterministic | Spreadsheet or the platform's calculation engine |
| Synthesizing diligence findings, drafting the IC memo, surfacing risks across documents, market research, first-draft thesis | AI | You, on top of governed data |
| The go/no-go and the IC approval | Human in the loop | Deal team and committee |

The trap on this workflow: letting AI read a stale or fragmented data room and treating its underwrite as authoritative. AI can summarize and surface. The figures it underwrites from must trace to a governed source.
