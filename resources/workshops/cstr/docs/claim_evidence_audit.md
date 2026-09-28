# Claim–evidence audit

For Session 2, select three claims before judging: one numerical, one
citation-based, one model/behavior claim. Copy the originals exactly. A complete
inventory of every substantive claim is an optional full-workflow extension.

## Decide from evidence

Use the first applicable explanation; explain mixed cases per component.

| Evidence condition | Status |
|---|---|
| Contradicts the claim | `MISMATCH` |
| Required evidence missing or not opened | `CANNOT VERIFY` |
| Available comparison concerns different conditions | `NOT COMPARABLE` |
| Supports only narrower wording | `SUPPORTED WITH LIMITATIONS` |
| Directly supports the entire quoted claim | `VERIFIED` |

Plausibility and a proposed citation are not evidence. Missing evidence is a
useful result. A compound claim is not VERIFIED while any part remains
unchecked. Agent inspection and human confirmation are separate records.

## Selected claims

Fill exactly three rows for the in-room exercise. State required evidence
before inspecting actual evidence. Preserve original quotes when revising.

| ID/type | Exact original quotation | Report section | Required evidence | Actual evidence and location | Verdict and reason | Proposed revision | Proposed/applied; human review |
|---|---|---|---|---|---|---|---|
| 1 / numerical | | | | | | | |
| 2 / citation | | | | | | | |
| 3 / model/behavior | | | | | | | |

For an omitted assumption, write “omission” and identify the relevant report
section. Never invent an original quotation to describe the omission.

## Numerical comparisons

One row for **each value**, even when several occur in a single sentence. Open
the artifact; identify CSV records by parameter values and branch index, not
unverified line numbers. Compare units and rounding explicitly.

| Claim ID; artifact path and record keys | Reported value | Artifact value | Unit conversion | Rounded comparison | Result |
|---|---|---|---|---|---|
| | | | | | |

Format example only (unrelated measurement): reported length 12.3 cm; artifact
0.1234 m; multiply by 100 gives 12.34 cm; rounded to one decimal gives 12.3 cm;
agrees at stated precision. This checks that value, not every part of a claim.

## Source comparison

Open [Woolf et al., section 11.6](https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Chemical_Process_Dynamics_and_Controls_(Woolf)/11:_Control_Architectures/11.06:_Common_control_loops_and_model_for_temperature_control),
**CSTR Temperature Control → Exothermic Reactor Temperature Control Loops**,
Figure 2.
Record the subsection/figure you actually used. If unavailable, record notes
only and the missing primary-source check. `docs/literature.md` is a navigation
aid, not a substitute for opening the source or grounds for VERIFIED.

| Claim ID; exact original quotation | Source opened (URL/section) or notes only | Actual passage/figure location | What it supports | Conditions/comparability; missing evidence |
|---|---|---|---|---|
| | | | | |

## Revision and final artifact

Record the original quotation, new wording, and proposed/applied status above.
Inspect the diff. Build after the final edit, or record **source-only; revised
PDF not built**. Name the revised source, build command/result and remaining
human checks in `docs/handoff.md`. A three-claim sample never verifies the whole
report.
