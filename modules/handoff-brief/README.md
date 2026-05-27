# Handoff Brief

Moves output from one workspace to another without making the downstream workspace re-derive it.

Use this when diligence feeds IC, a backtest feeds future underwriting, portfolio intervention feeds hold/sell/refi, or LP issue prep feeds a memory loop. Do not use it to copy a whole upstream workspace.

Implements constraint 08, with support from 10 and 09.

Used by all architectures that feed another workflow.
