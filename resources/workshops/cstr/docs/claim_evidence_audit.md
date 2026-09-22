# Claim–evidence audit

Every substantive claim in the report, and what actually backs it.

A claim is substantive if a reader could act on it, disagree with it, or cite
it. "The reactor is modeled as perfectly mixed" is a claim. "Figure 1 shows the
results" is not.

## Statuses

| Status | Use it when |
|---|---|
| `VERIFIED` | The stated evidence exists, says what the claim says, and is comparable |
| `SUPPORTED WITH LIMITATIONS` | The evidence supports a narrower version of the claim |
| `MISMATCH` | The evidence contradicts the claim, or the number does not match the artifact |
| `CANNOT VERIFY` | The required evidence does not exist, or was not produced |
| `NOT COMPARABLE` | The source addresses a different system, parameters, or assumptions |

`CANNOT VERIFY` and `NOT COMPARABLE` are results, not failures. A claim that
cannot be checked should be narrowed or removed — not upgraded because it feels
true.

## How to run the audit

1. **Inventory first, judge second.** List every claim with its location before
   assessing any of them. Judging as you read means you stop finding claims.
2. **State the required evidence before looking at the actual evidence.** "A
   value in `results/steady_states.csv` at $T_c = 300$" is required evidence.
   Deciding what would satisfy you *after* seeing what you have is how a claim
   gets graded against itself.
3. **Check numbers against the artifact, not against memory.** Open the file.
   Rounding a value differently in two places is a real inconsistency.
4. **For literature claims, check comparability before agreement.** Different
   parameters do not make results contradictory, and they do not make them
   agree either.
5. **Write the revision.** An audit that finds a problem and does not say what
   the sentence should become has not finished.

## A note on agents

An agent is genuinely good at the inventory step and at checking a number
against a CSV. It is not the authority on whether a comparison is meaningful,
and it will produce a confident, well-formatted audit table whether or not it
checked anything. Ask it for the evidence and the location, then look.

The failure to watch for: an agent asked to "verify the claims" tends to mark
things `VERIFIED` because the claim is plausible and the prose is consistent.
Plausibility is not evidence.

## Table

| Claim | Location | Required evidence | Actual evidence | Status | Revision |
|---|---|---|---|---|---|
| | | | | | |
