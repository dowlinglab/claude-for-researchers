# Prompt: review a grant proposal draft

Three modes for the stages of preparing a proposal — compliance review, restoring the sponsor's exact wording, and expanding or compressing a section to fit a limit. Run whichever you need; they share the setup block.

**Companion reading:** [`../practices/grant_proposal_writing.md`](../practices/grant_proposal_writing.md). The prompts below cite it by section rather than repeating it, so give the agent access to that file.

**The rule that makes all three work:** a review reports findings; it does not silently resolve them. Auto-fixing a compliance gap or a page-limit overage is how a review introduces the mistake it was run to catch.

---

## Setup block (prepend to any mode)

```markdown
Read `practices/grant_proposal_writing.md` before starting.

## Ground rules

- Do not submit, email, or otherwise transmit anything. This is a local,
  read/write editing session only.
- Change nothing outside the sections I name.
- Do not fabricate a requirement, a page limit, or a piece of guidance you
  have not actually read in the funding call. If you cannot find where a
  requirement is stated, say so rather than guessing.
- Flag anything ambiguous rather than resolving it plausibly.

## What I am giving you

- Draft: <path>, current as of <date/commit>
- Funding call / program guidelines: <path>
- <Anything else: a prior proposal to this program, reviewer feedback, a
  budget justification>
```

---

## Mode 1 — Compliance review against the funding call

```markdown
Following `practices/grant_proposal_writing.md` §4, check <path> against
every requirement stated in the funding call: required statements, page
limits per section, in-scope task language, formatting rules.

For each finding, insert it directly into the document, next to the text it
concerns:

\newcommand{\foacomment}[1]{\textcolor{blue}{\textbf{[Compliance note:} #1\textbf{]}}}

- Do not fix anything yourself — flag it for me to resolve.
- Cite the specific requirement for every finding (quote it or give its
  section number in the call). A finding without a cited requirement is an
  opinion.
- List anything you could not check because the requirement is ambiguous or
  the call doesn't address it.
- Report compliant-but-risky items (technically meets the letter, likely to
  draw a reviewer's attention anyway) separately from actual violations.

Finish with a count of open `\foacomment{}` markers and where they are.
```

---

## Mode 2 — Restore the sponsor's exact wording

```markdown
Following `practices/grant_proposal_writing.md` §2, find every place in
<path> where a sponsor-form question or required heading has been
paraphrased rather than quoted exactly from <funding call path>.

For each one, report:

| Location | Current (paraphrased) text | Sponsor's exact wording | Confidence |

- Quote the sponsor's wording verbatim, with the page/section of the call it
  comes from.
- Flag, separately, any place the draft answers a question the sponsor did
  not ask, or is missing a required heading entirely.
- Do not edit the document — report only. I will apply the approved
  corrections myself, or ask you to in a separate pass.
```

---

## Mode 3 — Expand, then compress (as two separate calls)

```markdown
Call 1: This section is a placeholder or thin draft. Using <project
description path> and <literature notes path>, draft full content for it —
substance over length, we'll trim to fit next. Preserve every specific
number and claim from the source material exactly; do not round, soften, or
generalize a figure while expanding around it.
```

```markdown
Call 2 (separate turn, after I've reviewed Call 1's output): This section is
now <Y> words; the limit is <X>. Trim it to fit without cutting any of the
required content items listed in <path>. Preserve the specific numbers and
claims exactly. Flag anything you think should be cut for me to decide,
rather than removing it yourself.
```

---

## After the review: applying the findings

A separate task, and ideally a separate session. From
`practices/grant_proposal_writing.md` §3 and §5:

```markdown
Apply only the findings I have marked APPROVED in <findings list, or the
in-document \foacomment{} markers I have left in place>.

- One edit per finding, by **exact single-match replacement**. If the
  pattern matches zero times or more than once, change nothing and tell me.
- Remove the \foacomment{} (or \draft{}) marker only for findings you just
  resolved — leave every other marker exactly as it was.
- After applying, run `../scripts/latexdiff_check.sh` and report the diff
  before I decide whether to commit (§5). Do not commit yourself.
```

---

## Notes on using these

**Run Mode 1 even against a program you've submitted to before.** Guidelines change between cycles more often than anyone remembers to check.

**Do not let the agent "helpfully" resolve a flagged item.** Every mode says report-only for the same reason: a compliance pass that edits is a compliance pass you now have to re-check.

**Keep Mode 3's two calls in separate turns, not one prompt.** Asking for both expansion and a page limit in the same instruction reliably produces a draft that either stayed thin or is still over length — see `grant_proposal_writing.md` §6 for why.

**Before submission, confirm zero markers remain** — no `\foacomment{}`, no `\draft{}`. Their disappearance is the checkable definition of "ready," not a memory of having addressed them.
