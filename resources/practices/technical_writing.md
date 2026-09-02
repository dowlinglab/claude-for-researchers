# Technical Writing for Research Papers

**What this is.** How to draft, revise, and prepare a manuscript — and how to use an AI assistant on it without ending up with prose that is fluent, confident, and not yours.

**When to reach for it.** When you start an outline, when you get comments back, and before anything goes to coauthors. Pair it with `writing_style_guide.md` (voice), `scientific_figures_tables.md` (figures and tables), and `manuscript_audit.md` (checking claims against results).

**How to read it.** Sections are numbered and stable, so you can point an agent at one (`follow §3`).

---

## 1. Structure before sentences

Fix the argument before polishing the language. An AI assistant will happily produce beautiful paragraphs defending a structure that doesn't work, and fluent prose disguises a broken argument better than clumsy prose does.

Work in this order:

1. **The claim.** One sentence: what is true that wasn't known before?
2. **The evidence.** Which results establish it, and what would falsify it?
3. **The outline.** Section by section, and — critically — **which figure or table carries each point.** If a subsection has no artifact, either it isn't a subsection or the artifact is missing.
4. **Then the prose.**

An outline that names its figures is the single most useful planning artifact, because it exposes both gaps (a claim with no evidence) and clutter (a figure supporting nothing).

## 2. A manuscript is a set of files, not a blob

Split the source: `main.tex`, `sections/*.tex`, `bibliography.bib`, `figures/`. This matters more with an AI assistant than without one:

- A model asked to "improve the paper" will rewrite it. A model asked to check notation in `sections/methods.tex` does a bounded, reviewable thing.
- Diffs stay readable, so you can actually see what changed.
- Sections can be worked on independently without merge pain.

Keep the manuscript in version control even when drafting in a synced editor. If you use a collaborative editor, decide which side is authoritative and write it down — the common failure is edits made in both places on the same day.

## 3. Notation, equations, and prose conventions

These are the mechanical rules worth enforcing, because they are checkable and they are where careless drafts leak.

**Notation**

- Every symbol is defined in words at first use.
- The definition appears in the *same sentence* as the symbol, not two sentences later.
- One symbol means one thing throughout, including the supplement.
- Every acronym is defined once, at first use, and not redefined.

**Equations**

- Equations are punctuated as part of the sentence that contains them — commas and periods included.
- A sentence never begins with a mathematical symbol. *"The constant $\alpha$ sets the…"*, not *"$\alpha$ is a constant that…"*
- Every equation that is referenced is numbered; equations never referenced usually don't need numbers.
- Each equation is introduced before it appears, not explained afterward.

**Prose**

- Each paragraph begins with a topic sentence that states the point.
- Each paragraph makes **one** point.
- Past tense for what was done; present tense for what the results show; future tense only in future-work.
- Active voice by default. Passive is a choice, not a register.

**Bibliography**

- Every cited key resolves, and resolves to the work you meant.
- Every entry has the fields the venue requires — and a DOI where one exists.
- No preprint or conference self-citation where the journal version exists.

## 4. Citations: never cite what you haven't read

The chain is: **AI suggestion → locate the source → read it → cite it.** There is no shortcut, and this is the single most likely way to embarrass yourself with an AI-assisted manuscript.

Concrete practices:

- **Treat every model-suggested reference as a lead, not a citation.** Keep suspect ones in a marked block — *"UNVERIFIED — do not cite until a real source is obtained"* — with the reason. Plausible-but-nonexistent references are a well-documented failure mode and they look exactly like real ones.
- **Verify DOIs mechanically** (`resources/scripts/doi_checker/`). A DOI that resolves to a *different* paper is worse than a missing one and is invisible on the page.
- **Keep literature notes as a claim audit, not a summary.** For each source record: the question it asks, the evidence it actually provides, and — the useful part — **what it can and cannot support in your manuscript.** For example: *"This paper proposes, rather than demonstrates, real-time control; the introduction must not cite it as evidence of completed feedback control."*
- **Track what you couldn't obtain.** Sources you requested and never got go in an explicit list with DOIs and the reason. A named gap is honest; a citation to an unread paper is not.

## 5. Edit against a standard, not against taste

"Make this better" produces drift. "Check this against that file and report violations with the rule cited" produces a reviewable list.

So write the standards down as files and point the assistant at them:

- a voice/style guide (`writing_style_guide.md`)
- figure guidelines (`scientific_figures_tables.md`)
- a nomenclature file for notation
- the target journal's author instructions, saved into the repo

Then the task becomes checkable: *"Review every figure against the figure guidelines. Report each violation with the specific rule it breaks."* This is the same move as §5 of `manuscript_audit.md`, applied to writing, and it is the difference between an assistant that edits and an assistant that reviews.

## 6. Recognizing AI drift in prose

The goal is **not** to make AI-assisted writing undetectable. It is to keep your technical voice and your actual claims intact. Watch for these tells — they are what unanchored generation produces by default:

- **Asserted significance.** "This represents a significant advance." Say what changed and by how much; let the reader conclude.
- **Throat-clearing openings.** "In recent years, machine learning has revolutionized…"
- **Overclaimed novelty.** "For the first time," "we solve," "always," "never." Prefer the conservative register: "has received limited explicit treatment," not "has been ignored."
- **Formulaic transitions and excessive symmetry.** Every paragraph the same length, every list three items long, every section ending with a summary sentence.
- **Agentless hedging.** "It could be argued that…" — by whom, on what basis?
- **Vague quantities.** "Substantially improves," "approximately doubles," where a number exists.
- **Homogeneous rhythm.** Real technical prose varies: a long qualified sentence, then a short flat one.
- **Undefined jargon on first use**, particularly statistical terms in an engineering paper.

Two structural safeguards matter more than any of the individual tells:

- **Protect the inconvenient results.** The default drift of AI-assisted revision is toward a cleaner, more one-sided story than your evidence supports. State explicitly, in the task: *the honest caveats must survive; do not sand them into a "our method wins" narrative.*
- **Carry integrity constraints in the style file itself**, so a later prose pass cannot quietly undo a verified finding. See `writing_style_guide.md` §4.

## 7. Capture review comments as a work list before acting

Comments arrive as annotated PDFs, email, or margin ink. Convert them to a numbered, trackable list *before* editing anything:

| # | Comment (verbatim) | Where it lands | Planned edit | Status |
|---|---|---|---|---|

- **Quote comments verbatim.** Paraphrasing a reviewer loses the thing you need most.
- **Mark what you couldn't read** with an explicit `[?]` and collect those into a "clarifications needed" list, rather than guessing at intent. An assistant transcribing handwritten notes must surface ambiguity, not resolve it.
- **Answer the ambiguous ones yourself, in the file.** Your answers then become durable context that survives the session.
- **Then execute in batches**, and close with a status table: done / done differently / partial / deferred, with a reason for anything not done.
- **Re-key comments against content, not numbering**, if the manuscript was restructured in between. A reply keyed to a stale item number silently assigns a decision to the wrong item.

The same structure works for editorial-office letters: reproduce the letter verbatim, add a status row per item, and record the judgment calls with their rationale.

## 8. Submission readiness, in graded gates

"Done" is not one threshold. Three, in order, each with a different standard:

1. **Ready for internal review.** The argument is complete and the numbers are traceable. Prose may be rough.
2. **Ready for coauthors.** Every figure final, every claim supported, notation consistent, references resolving. A coauthor's time is expensive; don't spend it on things a checklist would catch.
3. **Ready to submit.** Journal formatting satisfied, supplement complete and cross-referenced, data/code availability statement written, disclosures in place.

Two things that belong at gate 3 and are routinely missed:

- **A code and data availability statement that actually points somewhere** — a repository URL, a commit hash or tag, ideally an archival DOI. "Available upon request" is not a provenance link, and a public repository that isn't named in the paper cannot be found from it.
- **Publisher mechanics**, which are more fiddly than they look — some submission systems will not accept subfolders in a LaTeX upload, and a locally correct build does not always survive the publisher's compiler. Check before, not after.

## 9. Choosing a journal

AI can build the comparison; it cannot make the call. Give it the abstract, a one-paragraph contribution statement, the candidate journals' scope statements, and two or three representative papers from each, and ask for a table: scope fit, audience, methodological fit, novelty expectations, typical paper length and style, and likely reviewer objections. Treat the output as a structured argument to react to, not a recommendation to follow.

## 10. Disclose AI assistance

- **Check the venue's policy, and record the check** — which policy, which date, what it requires. Policies are changing faster than manuscripts move.
- **Describe what the tools actually did**, including what they did not do. If an assistant refactored the numerical methods or audited the results, that is a methods-section fact. A statement describing that as language polishing would be false.
- **Rewriting text into your own voice does not reduce the disclosure obligation.**
- Keep the disclosure numbered and cross-referenced like any other section so it survives renumbering.

---

## Checklist

**Before drafting**

- [ ] The claim is one sentence, and the evidence for it is named
- [ ] The outline names the figure or table carrying each point
- [ ] The manuscript is split into files under version control

**Before coauthors see it**

- [ ] Every symbol defined in words, in the sentence that introduces it
- [ ] Every acronym defined once; notation consistent with the supplement
- [ ] Equations punctuated as sentences; no sentence starts with a symbol
- [ ] One point per paragraph, topic sentence first
- [ ] Every citation traced to a source you have actually read
- [ ] DOIs verified mechanically; unverifiable references flagged, not cited
- [ ] Honest caveats still present after the last revision pass

**Before submission**

- [ ] Checked against the journal's author instructions, with violations listed
- [ ] Code and data availability statement names a repository and a commit or DOI
- [ ] AI disclosure written to the venue's current policy, and the policy check recorded
- [ ] Rendered PDF inspected — not the build log (`manuscript_audit.md` §8)

## Anti-patterns

- **Polishing before the argument is settled.** Fluent prose defending a broken structure.
- **"Improve this section."** Unbounded, unreviewable, and how voice gets lost.
- **Citing from a summary.** Including a summary you generated yourself.
- **Trusting a reference because it resolves.** It may resolve to the wrong paper.
- **Sanding off the caveats.** The most common quiet damage of an AI revision pass.
- **Paraphrasing reviewer comments** into a to-do list, losing the actual objection.
- **"Available upon request."** A non-answer that a reviewer will read as a non-answer.

## Using this file with an AI assistant

**As standing project context:**

> Follow `practices/technical_writing.md` for all manuscript work in this repository, especially §3 (notation and prose conventions) and §6 (avoiding AI drift). Honest caveats must survive every revision pass.

**As a bounded editing task:**

> Read `practices/technical_writing.md` §3. Check `sections/methods.tex` against it and report violations as a table: location | rule broken | suggested fix. Do not edit the file. Do not change any quantitative claim — if a number looks wrong, flag it for a separate audit rather than correcting it.

**As a drift check on your own recent revisions:**

> Read `practices/technical_writing.md` §6. Review the last revision's diff for AI-drift signals: asserted significance without numbers, overclaimed novelty, formulaic transitions, agentless hedging, vague quantities, and removed caveats. Quote each instance with its location. Pay particular attention to anything that made a result sound stronger than the previous version did.
