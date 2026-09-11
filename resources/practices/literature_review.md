# Literature Review with AI Assistance

**What this is.** How to use an AI assistant to explore a new research direction, process a collection of papers, and hand a corpus of literature to someone else — without citing a paper you haven't read or trusting a summary you haven't checked.

**When to reach for it.** Starting a new project and want to know what's already been tried. Have a research idea and want to pressure-test it against an adjacent field. Inherited or collected a folder of PDFs and need to make sense of it, for yourself or for someone taking the project over.

**Companion resources.** [`../prompts/literature_workflow.md`](../prompts/literature_workflow.md) operationalizes §3–§5 below as a ready-to-run prompt. [`../scripts/doi_checker/`](../scripts/doi_checker/) verifies the bibliography this produces.

**How to read it.** Sections are numbered and stable, so a prompt can cite one (`follow §5`).

---

## 1. Two starting points

**Idea-first.** You have a research direction and want to know what's already known, and whether it's actually novel. Brainstorming, terminology discovery, and search-strategy generation are all legitimate uses here — but nothing found this way is a citation until you've located, read, and verified the source. The chain is always: **AI suggestion → locate the source → read it → cite it.**

**Corpus-first.** You already have a folder of papers — collected over a project, inherited from someone, or gathered for a proposal — and need to turn it into something usable: an annotated bibliography, a synthesis, or an onboarding document for whoever works on this next.

Both converge on the same discipline below; they differ mainly in whether the corpus exists yet when you start.

## 2. Cross literatures deliberately to pressure-test an idea

The most productive idea-first move is not "find papers about my topic." It's **bringing in a second, adjacent literature specifically to test or extend the first.** Research a mechanistic method, then separately survey how AI agents are being used in that subfield; research a modeling approach, then survey the sensor-design literature it could inform. The second search is deliberate, not incidental, and its purpose is to answer a specific question: does this combination already exist, and where does it push back on the original idea?

Do this as two visibly separate passes — first field, then the crossing field — so each can be evaluated on its own before you claim the combination is new.

### Search, read, and search again

Start with a chatbot to develop terminology, synonyms, and search strings. Use Google Scholar and disciplinary databases to locate review papers, primary studies, citation trails, and competing terminology. After each processed batch, ask the agent to recommend specific missing sources and explain which gap each would address. Verify those recommendations and download the papers you can identify and use under the applicable license. Repeat; do not let the first search define the entire corpus.

## 3. Batch ingestion, with a checkpoint per batch

Process literature in small topical batches rather than one large dump: collect PDFs for one sub-topic, synthesize them, and only then consider that batch done. Each batch should leave behind a checkpoint — a note, a section, a commit — before the next one starts. This keeps each step reviewable and makes it obvious which topics have actually been processed versus merely collected.

Keep large PDF collections outside Git throughout the workflow. Track processing status in `literature.md` (collected, processed, verified), with the filename and source location for every entry. A checkpoint should commit the updated text artifacts; it need not commit the PDFs.

## 4. One fixed annotation schema, applied to every paper

Give every paper the same fields, and make at least one of them force a judgment call rather than a summary. Two schemas that work, depending on purpose:

**For a general literature review:** year and type, central contribution, main method, key takeaway, **relevance to this project.**

**For an onboarding synthesis:** **contribution** (what the paper actually did or found) and **project relevance** (how it changes a decision, an input, or an assumption for *this* project — including what does *not* transfer: different scale, different region, different cost year, different feed chemistry).

The rule that makes either schema worth using:

> Do not copy the abstract as the review. Interpret how the evidence changes a project decision or input requirement.

A summary restates the paper. A relevance judgment is what makes the review useful to someone who hasn't read it.

## 5. Verify in two passes

Read and summarize first. Then run a **second, dedicated pass** that checks every quantitative claim in the summary against the source PDF before it goes into anything you'd call a critical review. Two things this catches that a single pass misses:

- **Abstracts overstate results.** Check the number against the paper's actual reported figures and case study, not the headline claim — a real example: an abstract claiming "millions of variables" whose reported case study used roughly 150,000. Note the correct figure and flag the abstract's inflation explicitly, so it isn't repeated downstream.
- **Automated collection introduces noise.** A keyword search will return acronym collisions, near-duplicate versions, and the occasional wrong paper entirely. Keep a short housekeeping list of what was excluded and why, rather than silently dropping items.

## 6. Correct in place; never silently delete

When a later batch overturns an earlier synthesis — and it will, the more literature you add — record the correction where the original claim was, dated, with what changed and why:

> This section was written before a later batch of papers. That claim is not correct: [cite what changed it].

Strike through the superseded claim rather than deleting it. The record of *why* you changed your mind is as valuable as the corrected conclusion — and it is the difference between a synthesis someone can trust and one that might be quietly wrong in a way nobody can check.

## 7. Frame novelty honestly

Once claims are verified, sort them explicitly rather than asserting novelty in the aggregate:

- **Genuinely novel** — nothing in the surveyed literature does this.
- **Novel in combination** — each piece exists; the combination doesn't.
- **Where the literature pushes back** — evidence that complicates or contradicts the idea as originally framed.

This produces a proposal or introduction section that survives review, because it has already located and named the places a reviewer would push back.

## 8. Curate a "start here" path, after the full survey

A corpus of 100+ papers is not itself useful to a new reader. After the full survey, produce a short curated subset — ten to twenty papers — with explicit **reading habits** for anything else in the area:

> When reading a new paper in this space, record: the objective and decision variables (not the algorithm used to solve them); the cost in function evaluations (not wall-clock time, which won't transfer); whether identifiability is addressed at all.

Habits like these transfer to papers not yet read. A curated list without them just defers the work.

## 9. The getting-started report

The corpus-first workflow's main deliverable, when the audience is a person rather than yourself:

1. **Executive synthesis** — what the whole corpus implies, in a few sentences plus the cross-cutting constraints it surfaces.
2. **Implications organized by the project's actual workstreams** — not generic topic headings.
3. **Per-paper entries** in the fixed schema from §4.
4. **A required-data checklist** — what the incoming researcher needs to go collect, derived from what the literature says matters.
5. **Recommended additions** — papers not yet collected, each with a DOI and a one-line reason, explicitly tiered by priority.
6. **A review-limitations section**, stated plainly: this is a project-oriented synthesis, not a systematic review; before any value is used as a model parameter, trace it to the paper's methods, convert it to a common basis, and assign it an uncertainty range.

State up front that the document exists to bring someone up to speed. That framing is usually obvious to the author and invisible to the reader unless it's written down.

## 10. Verify the tool didn't invent anything

Three checks that catch fabrication, all cheap:

- **Does the stated corpus size match the file count?** If the synthesis says "56 papers," count the PDFs. A mismatch means something was double-counted, dropped, or never actually read.
- **Spot-check one paper's extracted metadata against its citation.** Title, venue, and DOI should match exactly.
- **Treat "recommended additions" as leads, not facts**, until each DOI has been checked against Crossref (`../scripts/doi_checker/`) and, ideally, the paper itself located.

## 11. Where the PDFs live is a separate decision from where the notes live

Notes, summaries, and BibTeX are small, text, and belong under version control. A large PDF collection often does not — particularly in a repository that syncs with a collaborative editor. Whichever you choose (reference manager, shared drive, a git-ignored local folder), write the policy down: a filename convention, where the files actually are, and a note field in the bibliography recording which file backs which entry, so the citation can always be traced to its source.

For a large project, a Google Drive folder can hold the PDFs while the writing repo tracks `ref.bib`, `literature.md`, and a mapping from citation keys to PDF filenames/locations. Record the access arrangements so collaborators can retrieve the same sources. Follow the roughly 10 MB individual-file convention and Overleaf synchronization guidance in [`latex_overleaf_workflow.md`](latex_overleaf_workflow.md) §1.

### Turn the corpus into a report or proposal

Build an outline that pairs each proposed claim with source PDFs and page/equation locations. Draft one section at a time against that map. Verify quotations, numerical values, qualifications, and conflicting evidence in the actual papers before polishing. Use sponsor instructions for a proposal and the journal's author instructions for a manuscript; the literature corpus supplies evidence, not the formatting rules. Review the compiled PDF and a tracked-changes version before accepting revisions.

## 12. Working with an AI assistant

**Idea-first exploration:**

> I have a research idea: [describe it]. Based on the literature you can find, identify what's already been tried, and separately survey [adjacent field] for work that could extend or challenge this idea. For every claim, show what evidence in a real, locatable paper supports it — I will verify each one before using it. Do not present anything as a citation until I've confirmed the source exists and says what you say it says.

**Processing a collected corpus (§3–§9):**

> Read `practices/literature_review.md` §3–§9. Process the PDFs in `literature/` in topical batches. For each paper: [schema from §4]. Do not copy the abstract — interpret how the evidence changes a project decision. After each batch, update a running synthesis organized by project workstream. Flag anything that overturns an earlier synthesis with a dated correction rather than rewriting silently. Close with a required-data checklist, tiered recommended additions with DOIs, and a stated review-limitations section.

**Auditing an existing review for fabrication (§10):**

> Audit `literature_review.md` against the PDFs in `literature/`. Confirm the stated corpus size matches the file count. Spot-check five entries' titles, venues, and DOIs against the actual PDFs. For every "recommended addition," verify the DOI resolves to the claimed paper. Report any mismatch, and report the count you couldn't verify as a real finding, not a gap to fill by guessing.

---

## Checklist

- [ ] Every claim traces to a source you (or the assistant, verifiably) actually read
- [ ] Literature was processed in checkpointed batches, not one dump
- [ ] Every paper uses the same annotation schema, with a relevance judgment, not a summary
- [ ] Quantitative claims were checked against the paper's reported results, not its abstract
- [ ] A corrected claim is struck through in place, dated, not deleted
- [ ] Novelty claims are sorted into novel / novel-in-combination / where-literature-pushes-back
- [ ] Corpus size, spot-checked metadata, and any recommended DOIs have been verified
- [ ] The PDF-storage policy is written down somewhere a collaborator can find it

## Anti-patterns

- **Citing a paper because an AI said it exists.** The single most damaging failure mode in this file.
- **Copying the abstract as the review.** A restatement, not a judgment.
- **One verification pass.** Reading and checking are different activities; conflating them is how an inflated abstract claim survives into a proposal.
- **Deleting a superseded claim** instead of correcting it in place.
- **Asserting novelty without naming where the literature pushes back.**
- **A curated reading list with no reading habits** — it doesn't transfer to the next paper.
- **Trusting a recommended DOI without checking it.**

