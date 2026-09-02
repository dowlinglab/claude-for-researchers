# Writing Style Guide

**What this is.** Three things in one file: how to *derive* a style guide from writing you already have (Part I), the Dowling Lab register spelled out as the worked instance and as the standard for group papers (Part II), and how to adapt it when you write elsewhere (Part III).

**When to reach for it.** Before a prose pass on a group manuscript. Before asking an assistant to draft or revise anything longer than a paragraph. And once, early, to build your own version of Part II.

**How to read it.** Part I is transferable to anyone. Part II is one group's register — useful to others as an example of the genre, binding for group papers. Sections are numbered and stable, so a prompt can cite `§7`.

---

# Part I — Making a style guide

## 1. What a style guide is for

Not to make your writing uniform, and not to make AI-assisted prose undetectable. It exists so that a revision — by a coauthor, by a new student, or by an assistant — lands in the register the paper is already written in, instead of drifting toward the flat, confident, generic voice that unanchored generation produces by default.

The test of a style guide is narrow and practical: **hand it to someone (or something) that has never read your work, and see whether the paragraph that comes back has a tonal seam.**

Two things that are *not* style but belong in the same file, because they are what a prose pass most often damages:

- integrity constraints — claims that must not be overstated (§3)
- an acceptance test — how to tell whether a paragraph passed (§4)

## 2. Deriving one from your own writing

Don't write a style guide from general principles. Derive it from documents you have already written and are willing to be judged by.

**Pick the exemplars first.** Three to six documents, named explicitly, ideally including at least one you are proud of and one written for a different audience (a proposal reads differently from a paper). Weight them: work where you were first or corresponding author reflects your voice more than work where you were in the middle of the author list.

**Commit the exemplars into the repository** alongside the guide, or record exactly where they live. A style guide that references documents nobody can find degrades into opinion within a year.

**Extract, don't invent.** Ask for what is *observably* true of the samples:

- sentence structure and typical length; where long sentences are allowed
- paragraph architecture — how paragraphs open, how many ideas each carries
- first-person usage; active versus passive
- how equations are introduced and how figures are referenced
- transition and pivot vocabulary
- hedging: how much, and expressed how
- terminology conventions, including what gets italicized or defined
- **habits you notably lack** — the constructions that never appear are as diagnostic as the ones that do

**Calibrate the confidence, and say so in the file.** Patterns in argument structure and paragraph design emerge reliably from a handful of documents. Word-level preferences, punctuation, and sentence rhythm need a much larger sample to distinguish from noise. Mark which of your rules are well-supported and which are provisional; an assistant will otherwise treat a guess and a finding as equally binding.

**Infer patterns; do not copy sentences.** The output is a description of how you write, not a bank of phrases to reuse.

## 3. Carry integrity constraints, not just voice

This is the part most style guides miss, and the part that earns the file its place.

When a verification pass establishes something — that a result is prior art, that a method estimates one quantity and not another, that a claim is narrower than it first appeared — **freeze that finding in the style guide**, because the style guide is the one document the next prose pass is guaranteed to read.

Constraints are stated as prohibitions with the reason attached:

> - **Attribute** the non-identifiability result to prior work; never present it as ours.
> - **Estimand, not truth:** describe the contribution as restoring estimability of an explicitly defined estimand; **never** "solve" or "eliminate" non-identifiability.
> - **Conservative gap register:** "has received limited explicit treatment," never "has been ignored."

Without this, a later revision quietly re-inflates a claim that a careful audit had already narrowed — and nobody notices, because the sentence reads well.

## 4. Make it checkable: the litmus test

End the guide with a single acceptance test a person or an assistant can apply to one paragraph. Something like:

> A paragraph passes if it could sit inside [named exemplar, named section] without a tonal seam: confident first-person plural, a named and cited framework, an italicized term or two on first use, a contrast pivot, and no overclaiming.

This converts the guide from aspiration into something with a pass/fail. Anything you cannot express as a test is advice, not a rule (see `working_with_ai_agents.md` §9).

## 5. Keeping it current

A style guide is a **living document** in the sense of `working_with_ai_agents.md` §3 — one of the three or four per project that must be true. Revisit it when a paper comes back with reviewer comments about clarity, when a new constraint is established by an audit, and when you notice yourself correcting the same thing twice. Two corrections of the same kind is the signal to add a rule.

---

# Part II — The Dowling Lab register

*Binding for group manuscripts. Useful to everyone else as a worked example of what Part I produces.*

This section merges two earlier derivations: one built empirically from the group manual plus a large corpus of the group's own papers, one anchored to named exemplar documents. Where they agreed, the rule is stated plainly. Confidence is **high** for argument structure, paragraph design, and terminology handling; **moderate** for individual word choice, punctuation, and sentence rhythm — treat the moderate items as defaults, not law.

**The priority order, when rules conflict:** scientific accuracy and reproducibility first, then clarity for the reader, then consistency with this guide, then style preference. A sentence that is more elegant and less precise is the wrong sentence.

## 6. Rhetorical moves

- **First-person plural, present tense, declarative.** "We investigate…", "We reformulate…", "We show…", "We argue…". Confident, not hedged.
- **Motivate broad to narrow.** Paradigm → the specific class of problem → the gap → *this work* → the objective. Each step one or two sentences; the funnel should be visible.
- **Use contrast pivots to set up gaps and contributions.** *Yet*, *In contrast*, *Instead*, *Unlike direct calibration, which …, we …*, *Consequently*, *Overall*. These carry the argument's turns; a section with no pivots is usually a section with no argument.
- **Name and cite frameworks rather than gesturing at them.** "The Kennedy–O'Hagan formulation [ref]" rather than "prior work."
- **Close sections with what was established**, not with a restatement of what the section would cover.

## 7. Sentences and paragraphs

- **One idea per sentence.** Moderate length. Active voice by default.
- **Topic sentence first; one point per paragraph.** If a paragraph has two points, it is two paragraphs.
- **Vary the rhythm.** A long qualified sentence followed by a short flat one reads as human; uniform mid-length sentences read as generated.
- **Build the argument before polishing the sentences.** This is the register's governing rule, and it is why Part I §1 exists.
- **Past tense** for what was done, **present tense** for what results show, future tense only in future-work.

## 8. Terminology and definitions

- **Italicize key terms on first use** — *hybrid*, *grey-box*, *black-box*, *aleatoric*, *epistemic*, *estimand*, *discrepancy*.
- **Define in crisp contrasting pairs**, in the sentence that introduces them:

  > *Aleatoric* (statistical) uncertainty corresponds to random phenomena, such as measurement noise. *In contrast*, *epistemic* uncertainty corresponds to systematic bias or model inadequacy.

- **Define statistics and optimization vocabulary for a chemical-engineering audience.** The reader is technically strong and may not share your subfield's shorthand. One clause is usually enough; omitting it loses the reader silently.
- **One symbol, one meaning**, across the manuscript and the supplement (`technical_writing.md` §3).

## 9. Drift signals

These are the tells that a paragraph has left the register — most often after a generation or revision pass:

- generic throat-clearing openings ("In recent years, machine learning has revolutionized…")
- passive, agentless hedging ("it could be argued that…")
- overclaimed novelty — "we solve", "for the first time", "always", "never"
- undefined jargon on first use
- long multi-clause sentences stacking three ideas
- uniform paragraph length and three-item lists everywhere
- asserted significance in place of demonstrated significance
- losing the chemical-engineering reader by importing a subfield's vocabulary unglossed

## 10. The litmus test for this register

> A paragraph passes if it could sit inside the group's established prose without a tonal seam: confident first-person plural, a named and cited framework, an italicized term or two on first use, a *Yet / In contrast / Unlike* pivot, one idea per sentence, and no overclaiming.

Apply it to one paragraph at a time. A paragraph that fails usually fails on exactly one axis, and naming which one is more useful than rewriting it.

---

# Part III — Adapting this

## 11. Writing outside the group

Part II is one group's register, shaped by a subfield and a set of venues. Do not port it wholesale into a different context — a first-person-plural declarative voice that reads as confident in a process-systems paper can read as overclaiming in a statistics venue, and italicized-term conventions vary by publisher.

When you move on, or write for a different audience:

1. Keep Part I. The method transfers completely.
2. Rebuild Part II from *your* exemplars, using §2. Six of your own documents is enough to start.
3. Keep the integrity constraints (§3) — those belong to the science, not to the venue.
4. Rewrite the litmus test to name your own reference documents.

A style guide you derived yourself is worth more than a better one you inherited, because you can tell when it is wrong.

---

## Checklist

**Building a guide**

- [ ] Three to six exemplar documents named explicitly, weighted by authorship role
- [ ] Exemplars committed to the repo or their location recorded
- [ ] Rules extracted from what the samples do, not from general principles
- [ ] Confidence marked: which rules are well-supported, which are provisional
- [ ] Integrity constraints from any verification work are frozen in the file
- [ ] A one-paragraph litmus test that gives a pass/fail

**Using one on a manuscript**

- [ ] The assistant was given the guide, not asked to "improve the writing"
- [ ] The revision was checked against the drift signals (§9)
- [ ] Integrity constraints survived the pass — no claim got quietly re-inflated
- [ ] Caveats that weaken the argument are still present

## Using this file with an AI assistant

**As standing project context:**

> Follow `practices/writing_style_guide.md` Part II for all prose in this repository. The constraints in §3 and the drift signals in §9 are not stylistic preferences — do not violate them, and do not remove a caveat to improve flow.

**As a bounded prose pass:**

> Read `practices/writing_style_guide.md` Part II. Revise `sections/introduction.tex` into this register. Do not change any quantitative claim, citation, or caveat — if the register would require weakening or strengthening a claim, stop and flag it instead. After revising, apply the §10 litmus test to each paragraph and report pass/fail with the axis that failed.

**To derive your own (Part I):**

> Read `practices/writing_style_guide.md` Part I. I will give you six documents I wrote. Analyze them for sentence structure, paragraph architecture, first-person usage, voice, transition vocabulary, hedging, terminology handling, and constructions I notably avoid. Weight first-author work most heavily. Produce a style guide in the shape of Part II, and **mark each rule high or moderate confidence** based on how consistently the samples support it. Infer patterns; do not reuse my sentences.
