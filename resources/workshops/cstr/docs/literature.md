# Literature notes

One section per source. Written from the document in front of you, not from a
search-result snippet, an abstract, or a summary produced by a tool.

A note is useful when a reader six months from now can tell, without reopening
the paper, whether a given claim can lean on it.

## How to write one

Four things, every time:

1. **What the source says** — the equation, parameter, or finding, stated
   precisely enough to compare against your own work.
2. **Under what conditions** — the parameters, assumptions, and regime. This is
   what decides whether a comparison with your results is meaningful.
3. **Where exactly** — section, equation number, figure, table, or page. "In the
   paper somewhere" is not a location.
4. **What it cannot support** — the limits. This column is the one that makes
   the claim audit possible, and the one everybody skips.

Keep your interpretation separate from what the source states. Both belong here;
confusing them is how an inference becomes a citation.

---

## Woolf et al. (2009), *Chemical Process Dynamics and Controls*, §11.6

**Type.** Open educational resource (Engineering LibreTexts, page ID 22513),
CC BY 3.0. Not peer reviewed.

**Verified.** 2026-09-15, from the page itself.

**What it says.** For an exothermic CSTR, plots a heat-generation curve (S-shaped
in temperature, from the Arrhenius rate) against a heat-removal line (linear in
temperature). Their intersections are steady states. Where there are three, it
argues the outer two are stable and the middle one is unstable, by comparing the
*rates* of heat generation and removal on either side of each intersection: when
generation exceeds removal, the temperature rises away from the intersection.

**Under what conditions.** A generic exothermic CSTR. The page does not supply a
specific parameter set, and reports no numerical steady-state temperatures for
the system discussed.

**Where exactly.** Section 11.6, in the discussion of the heat-generation and
heat-removal curves and the labelled intersections.

**What it cannot support.**

- *Any numerical claim about our reactor.* It reports no parameter values and no
  temperatures, so "agrees with Woolf et al." cannot be a quantitative
  statement. It is not the source for $E/R$, $k_0$, or any other number.
- *A stability conclusion transferred to our computation.* Their argument is
  dynamic: it is about rates of change on either side of a steady state. Our
  computation solves the algebraic steady-state balances and produces a locus.
  The shape of that locus is not the argument they made. To claim what they
  claim, we would have to make their argument — or a Jacobian eigenvalue
  calculation — about our model. Citing them for it instead is borrowing a
  conclusion without borrowing its evidence.

**Our interpretation (not from the source).** The qualitative structure we
compute — three steady states over an interval of coolant temperature, one
outside it — is the same phenomenon this source describes. That is a qualitative
correspondence, and it is worth stating as one.

---

## [Your model source]

**Type.**
**Verified.**
**What it says.**
**Under what conditions.**
**Where exactly.**
**What it cannot support.**

---

## [Your behavior source]

**Type.**
**Verified.**
**What it says.**
**Under what conditions.**
**Where exactly.**
**What it cannot support.**

---

## Gaps

What you could not find a source for. These drive the next search rather than
getting quietly dropped.

-
