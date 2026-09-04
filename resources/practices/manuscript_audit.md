# Auditing a Manuscript Against Its Results

**What this is.** How to check a paper against the code, data, and results behind it — before reviewers do. This is the highest-value thing an AI assistant can do in a research project, and the one most often done badly.

**When to reach for it.** Before submission. Before a revision goes back. When you inherit a manuscript whose results you did not personally produce. When a number appears in the abstract and you cannot immediately say which file it came from.

**How to read it.** Sections are numbered and stable, so you can point an agent at one (`follow §4`). §1 determines the shape of everything else.

---

## 1. Separate three questions that people collapse into one

An audit answers three distinct questions, and confusing them is what makes audits feel like accusations:

1. **Is the arithmetic right?** Do the reported numbers follow correctly from the inputs?
2. **Is the method right?** Is the appropriate calculation being performed at all?
3. **Is the transcription right?** Does the manuscript say what the results files actually say?

They have different evidence, different remedies, and different emotional weight. A transcription error is a typo. A method question is a scientific disagreement. Reporting them as one undifferentiated list of "problems" guarantees a defensive reading.

**Structure the report in that order, and lead with the reassuring finding when you have one.** A real example of the pivot that makes the rest land:

> There is no calculation bug. This is important and worth stating plainly to reviewers. It also means the remaining questions are about *which* calculation is performed, not whether it is performed correctly.

That sentence converts the audit from an attack into a methods discussion — while conceding nothing.

## 2. Set up: pin the artifact, bound the scope, keep the subject read-only

- **Pin what you audited.** Name the exact commit, version, or file state, and record that it was left unmodified. An audit of "the code" is not reproducible; an audit of a named commit is.
- **Keep the subject read-only.** The material under audit is never modified. Work in a separate directory or repository, and put that rule in every task you dispatch.
- **Pin the manuscript too.** A manuscript that moves during an audit — sections renumbered, tables reordered — will silently invalidate your cross-references. If it must move, re-anchor deliberately and record the mapping.
- **Disambiguate near-identical result sets up front.** Most projects have several: the published run, a rerun, an exploratory variant. Write a short table saying which is which, and flag any hazard (for example, a notebook that points at a variant and must not be synced over the published one).
- **Write the scope boundary down before it becomes a recurring question.** How deep do you trace? A workable rule: if a reference value is a correlation or an equation of state, that *is* the reference — you do not reconstruct the experimental data behind it; if a source tabulates its own values, you use them as reported. Then name the one or two exceptions where you *do* go deeper. Without this, "but is something missing?" reopens every week.

## 3. State the standard of evidence — including when *not* to change something

Write the rule before the findings. A workable standard: change a reported number only when

- **(a)** it contradicts another number in the same document and arithmetic settles which is right; or
- **(b)** it contradicts the code, *and* the code is demonstrably the source of the published result; or
- **(c)** it is an outright error — a malformed reference, a failed cross-reference, a compile error.

And the converse, which matters more:

> Where the code and the manuscript disagree but it is not clear which is authoritative — typically an input-parameter table — the item is left alone and moved to the outstanding list.

**Publishing the rule for *not* changing something is what makes your changes credible.** An audit that changed everything it could would be indistinguishable from one that changed things it shouldn't have.

Declare your limitations in the same breath: what you could not install, could not run, could not obtain. An audit with no stated limits is not more thorough; it is less honest.

## 4. Trace every claim: clean-room recomputation

**Reimplement the calculation from the formula rather than calling the code under audit.** This converts "the code runs" into "the number is right," and it is the only way to catch an error that is faithfully reproduced by the pipeline every time.

The trace, hop by hop, for one claim:

```
Printed value (Table 3, row 2, "5.30 %")
  → the row in results/metrics.csv that should produce it
  → the inputs that row was computed from
  → the source those inputs came from (a file, a paper, an instrument)
```

Every hop gets named. A trace that skips a hop is a guess.

Three techniques that repeatedly find real errors:

- **The dual ruler.** When the reference standard is itself a judgment call — which database, which convention, which subset — compute the metric against *both* candidates and report both side by side. Divergence between the two becomes an automatic flag for items worth checking a third time.
- **Confirm in the output, not only in the source.** Reading the code tells you what it intends; the output tells you what happened. Where a bound could apply to two quantities, find the run where it binds and see which one moved.
- **Check physical plausibility alongside numerical residuals.** Some errors are invisible to a residual test and obvious to a domain expert — a density that is impossible for that material, a rate constant off by an order of magnitude. Ask "is this physically sensible?" as a separate question from "does this reproduce?"

## 5. Report status, not prose: vocabularies where "cannot verify" is a result

Give every item a status from a short, fixed, machine-readable vocabulary, with a **distinct token for "could not verify"** — separate from "verified" and from "discrepant."

Examples of usable vocabularies:

- `MATCH` / `MATCH (both blank)` / `MATCH (alternate source)` / `MISMATCH`
- `VERIFIED` / `UNRELIABLE — needs [specific tool]` / `ANOMALY`
- `OK` / `APPROX` / `UNRELIABLE`

Two things follow from this that prose hedging cannot give you:

- **The distribution becomes a summary statistic.** "54 of 84 exact matches, 23 both-blank, 6 alternate-source, 1 unexplained" is a far stronger claim than "the tables are mostly consistent."
- **Unverifiable items get named rather than dropped.** A value that cannot be checked without a tool you don't have is a finding. So is a figure region too dense to digitize — leave it empty and say why, rather than fabricating points into it.

**"Cannot verify" is a successful result.** It is a provenance gap discovered for free, before a reviewer finds it. The rule that makes this work: **never fill a provenance gap by guessing.**

## 6. "Decided" is not "done": keep two registers

Audits generate two different kinds of item, and merging them loses work:

- **Edits** — numbered, with location, severity, and status. Something concrete must change in a file.
- **Decision points** — numbered, with your recommendation and the question. Only the authors can close these, and **"the audit takes no position" is a legitimate entry.**

Track a status per item, and keep `decided` distinct from `closed`:

> A decision is not a change: every *decided* item still needs someone to edit a file.

That distinction is where audits quietly fail. A long conversation resolves twenty questions, everyone feels finished, and nothing has been applied.

## 7. Determine status from evidence, not memory

Do not report which items are applied from recollection — yours or an agent's. Test for it.

The mechanism is simple: for each correction, record a **text signature** — either the old text that must now be *absent*, or the new text that must be *present* — and write a script that checks the current file. Then the status list is generated, not remembered.

> Run it rather than trusting any status statement, including this one.

This exists because status reported from memory has been confidently, specifically wrong. The lesson generalizes past audits:

> The remedy is not to be more careful but to stop deriving status from recollection at all.

## 8. Check the rendered artifact, not the build log

A document build can succeed, emit no warnings, produce a plausible page count, and still be wrong. Real instances, all with a zero exit code:

- a generated nomenclature table that rendered empty, so the section the main text points readers to was blank in every version reviewers saw
- a bibliography that silently failed to resolve
- overfull lines suppressed by a preamble setting

**The countermeasure that works, every time, is reading the rendered output** — not the log, not the exit status, not the page count. Note that two of those failures made the page count *more* plausible, being shorter.

Two habits follow:

- **A request to enumerate is worth more than a request to confirm.** "Is the bibliography fine?" invites a yes. "List every citation marker that renders as a question mark, with its page number" produces evidence. Ask for enumeration whenever the answer matters.
- **Ask what a *different* build system will do before you hand the work over.** A locally correct build does not travel. The cheapest way to find that out is to ask before submission, not after.

Where a check can be automated, automate it — geometric detection of overfull lines from the rendered PDF, a test that every referenced figure file exists, a check that no cross-reference renders unresolved.

## 9. Apply changes safely

- **Propose, don't write, for anything a false positive would corrupt.** Bibliographies especially: a DOI that resolves to the wrong paper is worse than a missing one and looks identical on the page. Have the tool report candidates; apply them by hand after checking title, authors, year, and venue.
- **Edit by exact single-match replacement, aborting on any other count.** If the pattern matches zero times or twice, nothing is written and you look at it. This guard catches stale patterns and near-duplicates that a fuzzy replace would silently mangle.
- **Verify after applying.** Regenerate a diff against the pinned baseline and trace *every* flagged change back to a recorded entry. Unexplained changes are the point of the exercise; this is also how you find an edit applied to the main text but not the supplement.
- **Regenerate, don't retype.** Any table that appears in both a results file and the manuscript should be generated from the results file by a script that only formats and holds no state. One hand-transcription error is enough to justify this permanently.
- **Make figures independent of the bibliography.** Reference numbers baked into figure images rot the moment citations are renumbered. Label series A–E and map them in the caption — the option that cannot rot again.

## 10. Audit the audit

Your instruments have bugs too, and an audit that hides its own errors is not worth much.

- **Hold audit scripts to the standard you are applying to the subject.** They are new code written quickly under time pressure — exactly the risk profile you are auditing for.
- **Run a second, independent pass on anything high-stakes**, ideally with a different tool or model. Cross-model triangulation catches structural mistakes a same-model recheck will reproduce. A real instance: a first pass's reference values, produced by one tool, were independently re-derived by a second audit and found reliable for most quantities but systematically biased for one — a bias invisible from re-running the same tool twice, and named as a risk before it was resolved rather than smoothed over.
- **A correct detection is not the same as a correct conclusion.** The sharper failure mode isn't always a missed bug — it can be a right answer, correctly flagged, then explained away in the write-up. One real audit's own comparison script correctly detected a systematic data error; a subsequent editorial pass misclassified that correct signal as an "explained non-issue." The tool was right; the sentence written about the tool's output was wrong. Check whether a flagged anomaly survived into prose as a finding, or got argued away under pressure to reach a clean verdict.
- **Retract in writing, in place.** When a finding collapses, write the retraction where the claim was, with the mechanism: *"This subsection corrects a wrong conclusion this report previously stated."* Do not silently edit it away.
- **Keep a self-correction section.** A running list of the audit's own errors, each generalized into a named failure mode, is the single most useful artifact for the next audit — and it makes the rest of the document more credible, not less.
- **Distinguish a tool bug from a scientific finding before you believe either.** A striking result that rests on a broken tool is not a result. Verify the instrument, then re-derive; the finding may well survive, and it will survive on trustworthy inputs.

## 11. Hand it back so someone else can check it

An audit nobody can verify is just an assertion with more pages. Write a short guide that lets an author independently re-check the work:

- **One worked end-to-end example**, all the way from a printed value to the raw inputs, with the arithmetic spelled out so it can be redone by hand or in a spreadsheet.
- **A single named source of truth** — for example, "these tables are generated by one script from one data file; the script only formats and holds no hidden state."
- **A discrepancy-log template** for what they find. And say what a short log means: *if the log comes back nearly empty, that is itself a strong validation result.*

**Frame findings for fairness, not for blame.** Where a correction cuts both ways, say so first. A reference error that inflated one method's performance while deflating a competitor's is a fairness fix, not an indictment — and reporting it that way is both more accurate and far more likely to be acted on.

**Ask where a wrong number came from, not just whether it's wrong.** A transcription slip and a value silently overwritten by an earlier, unrelated AI suggestion during data entry look identical once discovered, but they call for different fixes and different scrutiny going forward. As more of a lab's own data entry becomes AI-assisted, "was this number's origin itself an unreviewed AI output" is worth asking as its own question, separate from "is this number right."

## 12. The same move, in four variants

Every audit in this document is one operation — *trace an artifact back to its authoritative source and report match, mismatch, or cannot-verify.* Four common applications:

- **Quantitative claim audit.** Every number in the prose → the results file that should support it → verified, discrepant, or unverifiable.
- **Methods-versus-code.** Does the paper describe what the code actually does? Look for assumptions present in code and absent from the methods, parameter values that differ, preprocessing or solver settings omitted, and equations implemented differently from how they are written.
- **Figure-versus-text.** For each figure: which script produced it, from which data, and does the plotted content support what the caption and text claim about it? Check units and axis labels against the underlying values. A real instance: a figure's axis label claimed one quantity; the code that generated it computed a related but different one. The plotted data was correct throughout — only the label and the prose built on it were wrong. Distinguish "the figure is wrong" from "the figure is mislabeled": the fix and the blast radius are not the same.
- **Guideline compliance.** Check the manuscript against a named standard — journal instructions, a figure guideline, a nomenclature file — and report each violation *with the specific rule cited*. This is the easiest audit to automate and the easiest to skip.

---

## Checklist

**Setup**

- [ ] The audited artifact is pinned by commit or version, and left unmodified
- [ ] The workspace is separate from the subject
- [ ] The scope boundary is written down, including how deep to trace
- [ ] Near-identical result sets are disambiguated in a table

**Method**

- [ ] The standard of evidence is stated, including when *not* to change something
- [ ] Limitations are declared — what could not be run or obtained
- [ ] Claims are traced hop by hop, with every hop named
- [ ] Key metrics were recomputed independently, not read from the subject's own output
- [ ] Every item carries a status, with a distinct token for "cannot verify"

**Reporting and follow-through**

- [ ] Arithmetic, method, and transcription findings are reported separately
- [ ] Edits and author-decision items are in separate registers
- [ ] Item status is generated from evidence, not recalled
- [ ] The rendered output was inspected, not just the build log
- [ ] Applied edits were verified against a regenerated diff
- [ ] The audit's own errors are recorded and generalized

## Anti-patterns

- **The undifferentiated problem list.** Typos and methodological objections in one column, guaranteeing a defensive reading.
- **Silent correction.** Changing a number without recording the rule it broke and the evidence that settled it.
- **Filling a gap by guessing.** The one thing an audit must never do.
- **Hedging instead of status.** "Broadly consistent" where a vocabulary and a count belong.
- **Status from memory.** Reliably wrong, specifically wrong, and easy to eliminate.
- **Trusting the exit code.** A clean build that renders an empty table.
- **Auto-applying reference fixes.** A confidently wrong DOI is worse than a missing one.
- **The audit that exempts itself.** New code, written fast, checking everything but itself.

## Using this file with an AI assistant

**As a scoped audit task:**

> Read `practices/manuscript_audit.md`. Audit `manuscript.tex` against the results in `results/` following §3–§5. The code repository is READ-ONLY — do not modify it. For every quantitative claim in the abstract, results, and conclusions, produce a row: claim | location | the results file that should support it | recomputed value | status (`VERIFIED` / `MISMATCH` / `CANNOT VERIFY`) | note. Recompute independently from the data rather than calling the analysis code. Do not change any file. Where a claim cannot be traced, say so — do not infer a plausible source.

**As a methods-versus-code check:**

> Following `practices/manuscript_audit.md` §12, compare the Methods section against the implementation. Report: assumptions present in the code but absent from Methods; parameter values that differ between the two; preprocessing or solver settings not described; equations implemented differently from how they are written. Cite file and line for every finding, and mark each `high` / `medium` confidence. Change nothing.

**As a rendered-output check:**

> Following §8, build the document and inspect the *rendered* PDF, not the log. Enumerate: every unresolved cross-reference or citation marker, with page number; every generated table or list that renders empty; every figure reference whose target file is missing. Report a count for each category even if zero. Do not fix anything yet.
