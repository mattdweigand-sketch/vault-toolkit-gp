# Stage 01: Intake

## Purpose
Receive an inbound inquiry, determine what it actually is, classify it by type and sensitivity, confirm which investor and fund it concerns, assign priority, and produce a classified ticket the resolve stage can act on without re-reading the original.

## Inputs
- **The inquiry**: LP email, portal message, call note, or a forward from a partner. Paste or reference it here.
- **_config/investor-context.md**: To identify the investor, the entities involved, and any standing sensitivities or preferences.
- **_config/response-standards.md**: To apply the right priority and to recognize what is IR's to answer versus what must be referred.

## Process
1. Read the inquiry in full. Identify the actual question, which is not always the stated one. "Can you confirm my balance?" may really be "I am reconciling for my own audit and need it by Friday."
2. Identify the investor, the entity, the fund, and the requester. Confirm against investor-context.md. If you cannot identify the requester or their authority to receive the information, flag it — do not assume.
3. Classify the inquiry by type:
   - **Informational** — a question answerable from governed data or the FAQ bank (balance, performance, distribution history, fund facts).
   - **Document request** — a re-send or copy of a statement, K-1, notice, or agreement.
   - **Action request** — the LP wants something done (update contact details, explore a commitment increase, change distribution instructions).
   - **Sensitive** — anything touching redemption, a complaint, a side-letter interpretation, legal/compliance, or a figure dispute. These are flagged for escalation now, not answered later.
4. Assign priority based on the requester, the stated deadline, and the sensitivity.
5. Note what resolving it will require: which platform data, which team if escalation is needed, any authentication step.
6. Produce the classified ticket.

## Output
Write to: 01_intake/output/inquiry-[investor]-[date].md

Format:
```
# Inquiry Ticket: [Short Description]

Investor / Entity: [Name]
Requester: [Name, role, authorized: yes / no / unconfirmed]
Fund: [Name]
Date received: [Date]
Type: [Informational / Document request / Action request / Sensitive]
Priority: [High / Medium / Low]

## What Was Asked
[The inquiry in their words. Direct quote or close paraphrase.]

## What It Actually Requires
[Your read of the real need, and what answering it takes:
 which platform data, which document, which team.]

## Sensitivity / Escalation
[None, or: what makes this sensitive and who it must route to
 (IR principal, compliance, counsel). If sensitive, the resolve
 stage acknowledges and hands off — it does not answer.]

## Notes
[Standing investor sensitivities, prior related inquiries, deadline.]
```

## Done Looks Like
A ticket the resolve stage can act on without re-reading the original message or asking "is this one I can answer?" The type and sensitivity are decided here, on purpose, before any drafting.

## Common Failure Modes
- **Answering in the inbox.** The fastest way to mishandle a sensitive inquiry is to dash off a reply before classifying it. Classify first. The redemption signal that reads like a routine question is exactly the one this stage exists to catch.
- **Skipping requester verification.** Releasing account information to someone whose authority is unconfirmed is a control failure. If you cannot confirm the requester, say so in the ticket.
- **Taking the stated question literally.** Read for the real need. The misread question produces a technically-correct, actually-useless answer.

## Layer Annotation
L2 stage contract. The inquiry is L4 (this run). Investor context and response standards from _config/ are L3 (stable reference).
