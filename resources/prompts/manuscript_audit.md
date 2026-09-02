# Prompt: audit a manuscript against its results

Four modes of the same operation — *trace an artifact back to its authoritative source and report match, mismatch, or cannot-verify.* Run whichever you need; they share the setup block.

**Companion reading:** [`../practices/manuscript_audit.md`](../practices/manuscript_audit.md). The prompts below cite it by section rather than repeating it, so give the agent access to that file.

**The rule that makes all four work:** the audit reports; it does not fix. Auto-applying a "correction" is how an audit introduces the error it was run to catch.

---

## Setup block (prepend to any mode)

```markdown
Read `practices/manuscript_audit.md` before starting.

## Ground rules

- The code and results are the SUBJECT: strictly READ-ONLY. Do not modify,
  run destructively, or commit anything in <code repo path>.
- Work in <workspace path>. Write findings there, not into the manuscript.
- **Change nothing in the manuscript.** Report only.
- Do not fabricate. Every value you report must come from a named file, with
  the path. If you cannot trace something, the answer is "cannot verify" — that
  is a real and useful result (§5), not a failure to work around.
- Record the exact commit you audited, and note whether the working tree was
  clean.
- Flag anything ambiguous rather than resolving it plausibly.

## What I am giving you

- Manuscript: <path>, at <version/commit>
- Code: <path>, at <commit>
- Results: <path>
- <Anything else: data, a prior audit, journal guidelines>
```

---

## Mode 1 — Quantitative claim audit

The core one. Run this before submission.

```markdown
Following `practices/manuscript_audit.md` §4–§5, audit every quantitative claim
in the abstract, results, and conclusions.

For each claim, produce one row:

| Claim (quoted) | Location | Reported value | Source file + row/field | Recomputed value | Status | Note |

- **Recompute independently** from the underlying data where feasible, rather
  than reading the analysis code's own output (§4). Say which you did.
- Status is one of: `VERIFIED`, `MISMATCH`, `CANNOT VERIFY`. Use exactly these.
- For `MISMATCH`, give both values and your best account of where they diverge.
- For `CANNOT VERIFY`, say what specifically is missing — the file, the config,
  the run — rather than just "unclear".
- Do not propose corrections to the manuscript. List findings.

Finish with counts per status, and the three findings you would look at first
if you had an hour.
```

---

## Mode 2 — Methods versus code

```markdown
Following `practices/manuscript_audit.md` §12, compare the Methods section
against the implementation.

Report, with file and line for every finding:

1. Assumptions present in the code but absent from Methods.
2. Parameter values that differ between the text and the code.
3. Preprocessing, filtering, or solver settings the text does not mention.
4. Equations implemented differently from how they are written.
5. Anything in Methods with no corresponding implementation.

Mark each `high` or `medium` confidence, and say what you checked to reach it —
reading the code is weaker evidence than confirming behavior in output (§4).

Close with the question that matters: could a competent reader reproduce this
method from the Methods section alone? Answer specifically — what would they
get wrong, and where would they have to guess?
```

---

## Mode 3 — Figures versus text

```markdown
Following `practices/manuscript_audit.md` §12 and
`practices/scientific_figures_tables.md` §5, audit every figure.

For each figure:

| Figure | Generating script | Input data | Config/seed | Claim the text makes about it | Does the plotted data support that claim? | Status |

- Trace provenance from committed evidence — provenance sidecars, manifests,
  scripts — not from filename similarity. If the link is not recorded, the
  status is `cannot determine`; do not infer a plausible source.
- Check the caption against the axes: units, error-bar meaning, scale.
- Flag any figure the text never refers to, and any figure reference with no
  corresponding figure.
- Flag baked-in citation numbers in figure images, which rot on renumbering.
```

---

## Mode 4 — Guideline compliance

```markdown
Check the manuscript against <the journal's author instructions / our figure
guidelines / the nomenclature file>, which is at <path>.

Report one row per violation:

| Location | Rule violated (quote it) | What is wrong | Suggested fix |

- Cite the specific rule for every finding. A violation without a quoted rule is
  an opinion.
- Report compliant-but-risky items separately from actual violations.
- Where a rule is ambiguous, say so rather than picking an interpretation.
- Change nothing.
```

---

## After the audit: applying the findings

A separate task, and a separate session. From `practices/manuscript_audit.md` §6 and §9:

```markdown
Apply only the findings I have marked APPROVED in <findings file>.

- One edit per finding, by **exact single-match replacement**. If the pattern
  matches zero times or more than once, change nothing and tell me.
- After applying, regenerate a diff against <baseline commit> and trace every
  changed line back to an approved finding. Report anything unaccounted for.
- Do not fix anything you notice along the way. New findings go on the list.

Keep two registers: edits applied, and decisions still open that only I can
close. "Decided" is not "done" — every decided item still needs a file edited.
```

---

## Notes on using these

**Run Mode 1 even when you are confident.** Its most valuable output is the `CANNOT VERIFY` rows — provenance gaps found before a reviewer finds them.

**Do not let the agent "helpfully" correct things.** Every mode says report-only for the same reason: an audit that edits is an audit you now have to audit.

**Ask for enumeration, not confirmation.** "List every claim with no traceable source" produces evidence; "is the paper consistent?" produces reassurance (§8).

**Consider a second pass with a different tool.** Cross-model review catches structural mistakes a same-model recheck reproduces. Tell the second one not to assume the first pass was exhaustive.
