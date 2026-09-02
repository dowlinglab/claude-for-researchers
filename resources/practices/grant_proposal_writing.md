# Grant Proposal Writing with AI Assistance

**What this is.** How to draft, revise, and verify a grant proposal with an AI assistant's help — a document with its own constraints that a paper doesn't have: a strict page limit, a sponsor's exact required questions, a submission deadline that doesn't move, and often several collaborators editing at once.

**When to reach for it.** Drafting a new proposal, revising against reviewer or program-officer feedback, or preparing a proposal for a program you've submitted to before.

**Companion resources.** [`../practices/literature_review.md`](literature_review.md) for grounding the proposal's claims before you write; [`../practices/technical_writing.md`](technical_writing.md) for the prose conventions that apply here too; [`../scripts/latexdiff_check.sh`](../scripts/latexdiff_check.sh) automates §5 below.

**How to read it.** Sections are numbered and stable, so a prompt can cite one (`follow §4`).

---

## 1. Ground it before you draft it

A proposal's central claims — that a gap exists, that a combination of methods is new — are exactly the claims `literature_review.md` §2 and §7 are built to test. Do this before drafting, not while polishing: a proposal built on a novelty claim that collapses under one more literature pass is a much bigger problem the week before a deadline than the week you started.

## 2. Draft against the sponsor's actual questions, then restore its exact wording

Many programs use a fixed, numbered form: specific questions, specific page limits per section. Draft tersely against each question first — get the content right without carrying the sponsor's full boilerplate through every revision. Then, in a dedicated pass before submission, **restore the sponsor's exact official wording** above your answer, rather than paraphrasing what it asked. This is a compliance move as much as a readability one: a paraphrased question can drift from what the sponsor is actually evaluating; the sponsor's own words cannot.

## 3. Track open decisions inline, visibly, while drafting

Not everything is settled when drafting starts — a budget line, a collaborator's role, an experimental detail. Mark these inline with something visually distinct (a colored macro, a bracketed flag) rather than leaving a mental note or a separate list:

```latex
\newcommand{\draft}[1]{\textcolor{gray}{\textit{#1}}}
```

Strip the markers once every decision is resolved — their disappearance from the document is itself a checkable definition of "ready to submit."

## 4. Let AI review for compliance, inline, not in a separate document

Ask an assistant to check a draft against the funding call's actual requirements — required statements, page limits, whether a task reads as in-scope — and have it write findings **directly into the document**, visible in the compiled draft, next to the text they concern:

```latex
\newcommand{\foacomment}[1]{\textcolor{blue}{\textbf{[Compliance note:} #1\textbf{]}}}
```

This is the same principle as `manuscript_audit.md` §5, applied before a result exists rather than after: findings are visible where they matter, and each one is either resolved (fix the text, remove the comment) or explicitly deferred — but never lost in a chat transcript that won't exist by the time you need to remember what was flagged. The loop is: flag → fix → remove. Every comment that survives to the next commit is a finding that hasn't been addressed yet, which makes "any comments left?" a real pre-submission check rather than a question you have to reconstruct from memory.

## 5. Verify every revision with a word-level diff before committing

An AI-assisted line-edit pass can quietly change what a sentence claims — "more than double" softened to "substantially increase," a number tightened, a hedge added or removed — in ways a normal re-read misses because the sentence still reads fine. Before committing a revision:

1. Extract the last committed version of the file.
2. Run `latexdiff` against your current working copy.
3. Compile the diff to PDF and **read the colored, word-level changes**, not just the final text.
4. Only then commit.

[`../scripts/latexdiff_check.sh`](../scripts/latexdiff_check.sh) does steps 1–3 in one command. Do this after *any* substantial AI-assisted edit, not only at the end — it is cheap, and it is the check that catches a proposal accidentally naming the funding program inside its own narrative, or a claim quietly inflated past what the evidence supports.

## 6. Separate "expand" from "compress"

AI is good at turning a thin placeholder section into real content, and bad at hitting a page or word limit in the same pass — it will tend to overshoot. Treat these as two deliberate steps: ask for expansion first, review what it produced, then run a dedicated trimming pass against the actual limit. Expecting one prompt to do both reliably produces a draft that's either still thin or still over length.

## 7. Reuse across cycles: separate the form from the content

For a recurring program, split a **blank, project-agnostic template** — the sponsor's form structure, with placeholder macros — from this cycle's actual content file. At the start of a new cycle, bring forward last cycle's finished materials alongside the new call's blank form: the prior proposal is both a content precedent and a check that nothing about the form has changed. This turns "write a new proposal" into "fill in a template," which is a meaningfully smaller task than it sounds and compounds in value with every cycle it survives.

## 8. Coordinate tools carefully when more than one is editing

A proposal often moves through a collaborative editor (which auto-commits), a local AI-assisted editing session, and direct edits from coauthors — sometimes all in the same day. Two failure modes to guard against explicitly, since they will otherwise happen by luck rather than by design:

- **Pull before invoking a tool locally**, so an agent isn't editing a version a coauthor has already superseded.
- **Don't edit the same section in two places at once.** If a coauthor is live-editing in a shared editor, don't simultaneously run an AI-assisted pass over the same section locally — the sync step afterward is where conflicts hide.

## 9. Disclose

- **Check the program's AI-use policy before you rely on any of this** — coverage varies widely by sponsor and is not always written down. When a program has no stated policy, default to disclosing anyway; that default protects you more than it costs you.
- **Name the tool in the commit**, consistently — an attribution that appears for one drafting session and then stops makes the record misleading about how much AI assistance the document actually received.
- **Consider a human-plus-AI authorship line on the document itself** ("Prepared by [name], with AI assistance") for anything that will be read outside of git — a git trailer is invisible to anyone who only ever sees the PDF.

## 10. Working with an AI assistant

**Compliance review against the funding call:**

> Read the funding call at `<path>`. Check `main.tex` against every requirement it states — required statements, page limits per section, in-scope task language. Insert findings using `\foacomment{}` directly above the text each one concerns. Do not fix anything yourself; flag it for me to resolve. List anything you could not check because the requirement is ambiguous.

**Expand, then compress (§6), as two separate calls:**

> This section is a placeholder. Using the project description in `<path>` and the literature notes in `<path>`, draft full content for it — aim for substance over length; we'll trim next.
>
> *(after review, in a separate turn)* This section is now Y words; the limit is X. Trim it to fit without cutting any of the required content items listed in `<path>`. Preserve the specific numbers and claims exactly — flag anything you think should be cut rather than removing it yourself.

**Pre-commit verification (§5):**

> Run `../scripts/latexdiff_check.sh main.tex` and show me the compiled diff before I decide whether to commit.

---

## Checklist

**Before drafting**

- [ ] Central novelty/gap claims checked against literature (`literature_review.md` §2, §7)
- [ ] The sponsor's actual required questions and page limits are at hand, not paraphrased from memory

**While drafting**

- [ ] Open decisions marked inline and visibly, not tracked separately
- [ ] Compliance review run against the funding call, findings inline, each one resolved or explicitly deferred
- [ ] Expansion and compression run as separate, deliberate passes

**Before every commit**

- [ ] `latexdiff` run against the last committed version and the diff actually read
- [ ] The sponsor's exact wording restored above each answer
- [ ] All inline decision/compliance markers resolved and removed

**Before submission**

- [ ] AI-use policy for this specific program checked
- [ ] Tool use disclosed, consistently, wherever the program or convention requires it
- [ ] If this is a recurring program: template split out for next cycle

## Anti-patterns

- **Paraphrasing the sponsor's question** instead of restoring its exact wording before submission.
- **A compliance comment that survives to submission** because it was flagged once and never revisited.
- **Trusting a re-read to catch AI-introduced drift.** A word-level diff catches what a re-read doesn't.
- **Expecting one prompt to both expand and fit the page limit.**
- **Two tools editing the same section at once**, discovered only when the merge doesn't look right.
- **Inconsistent AI attribution** — present for one session, silently absent for the rest.
