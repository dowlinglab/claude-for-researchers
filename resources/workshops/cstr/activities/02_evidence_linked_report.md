# Activity 2 — From evidence to an audited report

**Time:** 1 hour 45 minutes
**You need:** your repository from Activity 1, a LaTeX toolchain, and an AI
agent. Before the session, find two literature sources (see
[Between the workshops](#between-the-workshops)).

## Objectives

By the end you will have:

- a small literature corpus whose metadata you verified yourself;
- notes that separate what each source says from what you infer;
- a two-page LaTeX report in which every number traces to a file and every
  citation traces to a document you opened;
- a claim inventory and an audit of every substantive claim;
- a revision, visible in a diff, that narrows the claims the audit could not
  support;
- an updated handoff.

The lesson underneath: **an agent can accelerate scientific writing without
becoming the authority for the science.** A useful audit often returns
`CANNOT VERIFY` or `NOT COMPARABLE`. Those are results.

## LaTeX prerequisite

Check before the session starts:

```bash
latexmk -v && pdflatex --version | head -1 && bibtex --version | head -1
```

If any of these is missing, install TeX Live (Linux), MacTeX or BasicTeX
(macOS), or MiKTeX (Windows). Then confirm the supplied template builds:

```bash
cd report
latexmk -pdf report.tex
latexmk -C
```

Overleaf works too, but the audit is much easier locally where the agent can
read `results/` and the `.tex` in the same tree.

---

## Between the workshops

Find **two** sources and download them to `literature/pdfs/` (git-ignored):

- **one for the model** — governing equations, assumptions, sign conventions, or
  parameter values;
- **one for the behavior** — multiple steady states, ignition and extinction,
  thermal runaway, stability, or an application where this matters.

Search phrases: `nonisothermal CSTR multiple steady states`, `CSTR ignition
extinction diagram`, `exothermic CSTR thermal runaway`, `continuous stirred tank
reactor bifurcation`.

A verified anchor source is already supplied — see
[`../literature/README.md`](../literature/README.md). Read it before the
session; you will compare your results against it.

**Do not commit PDFs.** See the licence discussion in that README.

**If you cannot get a source at all** — paywalled, no institutional access, or
it simply does not exist in reachable form — that is a normal outcome, not a
failure of the exercise. Record the row in `source_manifest.csv` with
`verified: no` and a note saying the document could not be obtained, and say so
again wherever you would otherwise have cited it. What you must not do is fill
the gap: no citation from an abstract you skimmed, no DOI you did not see in the
document, and no entry supplied by a tool. A corpus of one verified source with
an honest statement of its limits is worth more than three you cannot vouch
for.

---

## Phase 1 — Reconnect (10 min)

```bash
cd ~/cstr-project
conda activate cstr-workshop
git switch -c workshop2
pytest tests
python scripts/reproduce.py
```

> **Gate 1.** The tests pass and `results/` is current. You are about to write
> claims about these numbers; they should be numbers you just regenerated, not
> numbers you remember.

Open `results/baseline.json` and `results/steady_states.csv` and look at them
again. Specifically: the three nominal steady-state temperatures and
conversions, and the range of coolant temperature over which there are three.

---

## Phase 2 — Verify and process the corpus (15 min)

### Verify metadata from the documents

For each of your two sources, open the PDF and check the title, authors, year,
and DOI **against the document itself**. Not against a search result, not
against a citation in another paper, not against what an agent told you.

> **Prompt.** Here is the citation metadata I have for two sources: [paste].
> The PDFs are at `literature/pdfs/[names]`. Read each PDF and tell me where the
> metadata disagrees with the document. Report only what you can see in the
> file. If a DOI does not appear in the document, say so rather than supplying
> one.

That last sentence matters. Asked for a DOI it cannot find, an agent will
frequently produce a well-formed one that belongs to a different paper.

Fill in `literature/source_manifest.csv`. `verified: no` is an acceptable value
and much better than a wrong `yes`.

### Notes

Write up each source in [`../docs/literature.md`](../docs/literature.md),
following the four-part structure there: what it says, under what conditions,
where exactly, and what it cannot support. The worked entry for the anchor
source shows the level of detail.

Keep the source's statements separate from your interpretation. Confusing them
is how an inference quietly becomes a citation.

> **Gate 2.** `source_manifest.csv` has a row per source with an honest
> `verified` value, `ref.bib` has entries only for sources you opened, and
> `docs/literature.md` has notes for each — including a "what it cannot support"
> line that is not empty.

---

## Phase 3 — Compare model and behavior (10 min)

Two comparisons, in this order.

**Model.** Audit your implemented balances against your model source: the terms
present, the assumptions, the units, the signs. Pay attention to assumptions
your *code* makes that your source does not, and vice versa. Constant coolant
temperature is one worth checking.

**Behavior.** Compare your computed steady-state structure with your behavior
source and with the anchor source.

Then label each comparison, and write the label down:

| Label | Means |
|---|---|
| numerical | Same quantity, comparable conditions, values agree within a stated tolerance |
| qualitative | Same phenomenon, different conditions or parameters |
| not comparable | Different system, assumptions, or parameters |
| insufficiently specified | The source does not report what you would need |

**Different parameters are not a contradiction.** They are also not agreement.
If your source used a different `UA` or a different reaction, a numerical
comparison is not available to you at any confidence level — and no amount of
careful phrasing creates one.

Record in `docs/literature.md` what you could not find a source for. That is the
next literature search, not a gap to paper over.

> **Gate 3.** Every comparison carries one of the four labels, in writing.

---

## Phase 4 — Draft the report (20 min)

Work from [`../report/report.tex`](../report/report.tex). Target two pages plus
references. Sections: research question, model and assumptions, computational
method, principal result and figure, comparison with literature, limitations,
reproducibility.

```bash
cp results/steady_state_locus.png report/figures/
```

> **Prompt.** Draft `report/report.tex` from the existing template using
> `results/baseline.json`, `results/steady_states.csv`, and
> `docs/literature.md`. Rules: every numerical value must come from one of those
> result files, and annotate each with the file it came from; state the
> assumptions my code actually makes, taken from the docstrings in
> `src/cstr_workshop/`; cite only entries already in `report/ref.bib`; label
> each literature comparison as numerical, qualitative, not comparable, or
> insufficiently specified. Where you are unsure whether the evidence supports a
> statement, write the weaker statement.

Three habits to hold onto while drafting:

1. **Round consistently.** Decide on a precision and use it everywhere. The same
   temperature appearing as 385.13 K in one section and 385 K in another is
   survivable; 385.13 K and 387 K is a finding.
2. **Name the generating command under every figure.**
3. **Write the limitations section before you think you are finished.** It is
   much harder to add honestly afterwards.

Compile:

```bash
cd report && latexmk -pdf report.tex && cd ..
```

> **Gate 4.** `report/report.pdf` builds with no undefined references or
> citations, and is roughly two pages plus references.

**Short on time?** Use [`../report/audit_fallback.tex`](../report/audit_fallback.tex)
instead and go straight to Phase 5. It is a complete draft of this report,
written to contain several evidence problems. It is otherwise a competent piece
of writing, which is the point — these are the mistakes that survive a careful
read.

```bash
cd report && latexmk -pdf audit_fallback.tex && cd ..
```

---

## Phase 5 — Inventory and audit every claim (25 min)

This is the core of the activity. Budget the full 25 minutes.

### Inventory first

List every substantive claim with its location. Do not assess any of them yet.

> **Prompt.** Read `report/report.tex` (or `report/audit_fallback.tex`). List
> every substantive claim with its section and a short quotation. A claim is
> substantive if a reader could act on it, disagree with it, or cite it.
> Include claims about what the model assumes, about numerical values, about
> agreement with literature, and about reactor behavior. Do not assess them yet
> — inventory only.

Expect somewhere between ten and twenty-five. If you get five, it did not read
the model section.

### Then audit

For each claim, fill in the table in
[`../docs/claim_evidence_audit.md`](../docs/claim_evidence_audit.md):

```
Claim | Location | Required evidence | Actual evidence | Status | Revision
```

Statuses: `VERIFIED`, `SUPPORTED WITH LIMITATIONS`, `MISMATCH`,
`CANNOT VERIFY`, `NOT COMPARABLE`.

**Write the required evidence before you look at the actual evidence.** Deciding
what would satisfy you after seeing what you have is grading a claim against
itself.

> **Prompt.** For each claim in the inventory, state what evidence would be
> required to support it — a specific value in a specific file, a specific
> statement in a specific source, or a computation that would have to exist.
> Then check whether that evidence is present in `results/`,
> `docs/literature.md`, or `src/`. Quote the actual value or statement you
> found, with its location. Assign a status and propose a revision for anything
> that is not VERIFIED.
>
> Rules: do not mark a claim VERIFIED because it is plausible. If a number
> differs from the artifact at the precision stated, that is a MISMATCH however
> small. If a source used different parameters, the comparison is NOT COMPARABLE
> — not a weaker form of agreement. If the required computation was never
> performed, the status is CANNOT VERIFY regardless of how standard the result
> is in the field.

### Then check the agent's work

Do not skip this. Pick four or five claims — including at least one marked
`VERIFIED` — and check them yourself against the file. An agent asked to
"verify the claims" will produce a confident, well-formatted table whether or
not it opened anything.

### Claims that are worth the attention

Two overclaims are extremely easy to make here and worth hunting deliberately:

- **Stability from an S-shaped curve.** A locus of steady states of the
  *algebraic* balances says nothing about the *dynamic* behavior. The middle
  branch of such a curve is commonly unstable in systems like this — but
  "commonly, in systems like this" is not evidence about this system. If the
  dynamic model was never written down and no Jacobian eigenvalue was ever
  computed, the required evidence does not exist. That is `CANNOT VERIFY`, and
  citing a source that made the dynamic argument for a *different* system does
  not fix it.
- **Exact agreement with a paper that used different parameters.** If the
  parameters differ, the numbers cannot agree exactly except by coincidence, and
  "exact agreement" is a claim about numbers.

Also check, mechanically:

- every reported number against `results/steady_states.csv` and
  `results/baseline.json`, at the precision stated;
- every assumption the *code* makes against the assumptions listed in the
  report — an assumption the code makes and the report omits is an error, not a
  stylistic choice. The code's assumptions are in the docstrings in
  `src/cstr_workshop/` if you completed Workshop 1; on the fallback path
  `src/cstr_workshop/` is still empty, so read the assumption list in the first
  markdown cell of `notebooks/cstr_exploration.ipynb` instead;
- every citation against what the cited source actually says, not against what
  the sentence needs it to say.

> **Gate 5.** Every claim in the inventory has a row with a status and, where
> not `VERIFIED`, a concrete proposed revision. At least one status is something
> other than `VERIFIED`. If every claim came back `VERIFIED`, the audit did not
> happen — go back and check three of them by hand.

---

## Phase 6 — Revise, compile, review (15 min)

Apply the revisions. Narrow the claims the audit could not support.

**Narrow, do not delete, and do not invent.** The honest version of an
unsupported stability claim is not silence — it is a sentence saying what was
computed and what would be required to say more. That sentence is more useful to
a reader than the overclaim was.

```bash
# your own draft
cd report && latexmk -pdf report.tex && cd ..
# or, if you audited the fallback
cd report && latexmk -pdf audit_fallback.tex && cd ..
git diff
```

Read the diff of the `.tex`. The revision *is* the deliverable — it is the
visible record that the audit changed something.

Rerun the computational gates, because the report now makes claims about them:

```bash
pytest tests
python scripts/reproduce.py
```

```bash
git add -A
git commit -m "Draft report and narrow claims the evidence audit could not support"
```

> **Gate 6.** The report compiles, the diff shows revisions traceable to audit
> rows, and the tests still pass.

---

## Phase 7 — Handoff (10 min)

Update [`../docs/handoff.md`](../docs/handoff.md): branch, commit, which gates
you ran and when, decisions and their reasons, open questions, and the known
limitations carried forward from the audit.

> **Gate 7.** Working tree clean; `docs/handoff.md` records the actual commit
> hash and only gates you actually ran.

---

## Minimum completion

1. Two sources verified from the documents, with honest manifest rows.
2. Notes for each, including what it cannot support.
3. A compiling report — yours or the fallback.
4. An audit of at least ten claims, with at least one status other than
   `VERIFIED`.
5. One revision visible in a diff.
6. An updated handoff.

## Extensions

- Compute the dynamic Jacobian and eigenvalues, then revisit the stability claim
  with actual evidence. This is the most satisfying extension.
- Add a sensitivity table over `UA` or `Tf` and audit the resulting claims.
- Write a reviewer-style response to your own report.
- Audit a real preprint in your field the same way, on a two-page excerpt.
- Turn the audit into a repeatable check script for numerical claims.

## Common problems

**`latexmk` not found.** The TeX installation is missing or not on `PATH`. On
macOS with BasicTeX you may also need `tlmgr install latexmk`.

**Undefined citations after compiling.** Run `latexmk` twice; it runs BibTeX
between passes. If they persist, a key in the `.tex` does not match the `.bib` —
or BibTeX hit a syntax error and skipped entries silently. Read the `.blg` file.

**Your agent produced a DOI you cannot find.** Treat it as fabricated until the
document proves otherwise. This is the most damaging thing an agent does in this
workflow.

**Every claim came back `VERIFIED`.** The audit did not happen. Check three by
hand.

**The audit disagrees with itself between runs.** Ask for the evidence and the
location rather than the verdict. A verdict without a location is not checkable
and is not worth much.

**You cannot tell whether a comparison is `NOT COMPARABLE` or `qualitative`.**
Ask whether the source reports the *same quantity under comparable conditions*.
If not, it is qualitative at best. If the phenomenon differs too, not comparable.

## Final verification

```bash
conda activate cstr-workshop
pytest tests
python scripts/reproduce.py       # or scripts/run_notebook.py on the fallback path
cd report && latexmk -pdf report.tex && cd ..          # your own draft
# cd report && latexmk -pdf audit_fallback.tex && cd .. # or the fallback
git status                        # expect a clean tree
git log --oneline main..HEAD
```

Your repository now contains the result, the evidence for it, the record of what
the evidence did not support, and enough context to resume cold. That is the
whole workflow.
