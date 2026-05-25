# Deal Screening References

<!--
This folder holds knowledge that applies across screens, not to one deal.

What lives here:
- The pass log: every passed deal and its tagged reason. The decision stage
  writes to this. Over time it keeps screening consistent (the same kind of
  deal gets the same answer) and reveals the firm's rejection patterns.
- Prior screens of similar deals, for comparison and consistency.
- Submarket comps and recent trades the firm tracks.
- The firm's underwriting standards as they apply at the screen level.

This is L3 reference, shared across the screening queue. Keeping it separate
from _config means the standing criteria (what the firm buys, how it screens)
stay clean while the accumulating record of actual screens grows here.

The pass log is the asset that makes screening compound: a firm that can see
why it passed its last hundred deals screens its next hundred faster and more
consistently.

Starting state: empty. The pass log and the rest fill on first use. A stage
contract that names a file here treats it as optional until you populate it —
the absence is not an error, it is a workspace that has not run yet.
-->
