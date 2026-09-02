# Prompt: process a folder of literature PDFs

For the folder of downloaded papers named `1-s2.0-S0009250923004... .pdf` and `Downloaded (3).pdf` that everyone accumulates.

Turns it into: consistent filenames, a notes file organized by paper, and BibTeX entries — with **uncertain metadata flagged rather than guessed**, which is the entire difference between this being useful and being a liability.

**Companion reading:** [`../practices/technical_writing.md`](../practices/technical_writing.md) §4, on why literature notes should record what a source *can and cannot support* rather than summarizing it.

**Pair it with** [`../scripts/doi_checker/`](../scripts/doi_checker/) once you have BibTeX — this prompt extracts metadata, that script verifies it against Crossref.

---

## The prompt

```markdown
# Task: organize a literature folder

Folder: <absolute path to the PDFs>
Output: <where literature.md and references.bib should go>

## Ground rules

- **Never fabricate metadata.** Not a DOI, not a year, not a journal, not a page
  range. If you cannot read it from the PDF itself, mark it `UNCERTAIN` and say
  what you could not determine. A wrong DOI is worse than a missing one and
  looks identical on the page.
- Read the PDF content. Do not infer the citation from the filename, and do not
  rely on your own recollection of a paper you recognize.
- **Do not rename or move anything until I approve the plan** (Phase 2).
- Never delete a file, including apparent duplicates.
- Work in three phases and stop after each of the first two.

## Phase 1 — Inventory (read-only)

For every PDF, extract from the document itself:

- first author surname, all authors, year, title
- venue (journal / conference / preprint server), volume, pages
- DOI, if printed in the document
- document type: journal article, preprint, thesis, report, standard, book chapter
- a confidence marker: `confirmed` (read off the document) or
  `UNCERTAIN — <what is missing or unclear>`

Report as a table, plus:

- **Probable duplicates**, grouped, with what distinguishes them (preprint vs.
  published version, v1 vs. v2, two scans of the same paper). Do not delete
  anything — say which you would keep and why.
- **Unreadable or scanned files** that would need OCR.
- **Files that are not papers** (slides, supplementary data, a manual).

Then stop.

## Phase 2 — Propose a naming scheme and the file map

Propose a filename convention and apply it to every file as a proposal:

    FirstAuthor_Year_ShortTitle.pdf     e.g. Kennedy_2001_BayesianCalibration.pdf

- ASCII only; no spaces; strip diacritics; three or four words of title maximum.
- Say how you would disambiguate same-author-same-year collisions.
- Present as a table: current name → proposed name → confidence.
- Flag every file where the proposed name rests on `UNCERTAIN` metadata; those
  should not be renamed until the metadata is confirmed.

Then stop for approval.

## Phase 3 — Execute, after approval

1. Rename approved files with `git mv` (or `mv` if not under version control).
   Leave `UNCERTAIN` files untouched and list them.
2. Write `literature.md`, one section per paper:

   ```
   ## Kennedy_2001_BayesianCalibration
   **Citation.** <full citation>
   **DOI.** <doi, or "not printed in document">
   **Question.** <what the paper is trying to answer, one or two sentences>
   **Approach.** <method, briefly>
   **Main evidence.** <what it actually demonstrates, as opposed to proposes>
   **Can support.** <claims this paper could legitimately be cited for>
   **Cannot support.** <claims it could NOT be cited for, especially ones it
   might look like it supports — e.g. "proposes rather than demonstrates X;
   do not cite as evidence of a working implementation">
   **Status.** confirmed | UNCERTAIN — <what is unresolved>
   ```

3. Write `references.bib` with entries for confirmed papers only. Put
   `UNCERTAIN` ones in a clearly separated block at the end, commented out,
   with a note on what is missing.
4. Write a short `README` in the folder recording the naming convention, the
   date, and the list of files left unrenamed and why.

## Report back

- Counts: total files, confirmed, uncertain, duplicates, non-papers.
- Everything left unrenamed, and what would resolve each case.
- Any paper whose DOI you could not find in the document — I will check those
  against Crossref separately.
```

---

## Notes on using it

**The "Cannot support" field is the point.** A summary tells you what a paper says; this tells you what you may cite it for. It is the field that prevents the most common citation error — citing a paper that *proposes* something as though it *demonstrated* it. It is also the field an agent will skip unless you ask for it explicitly.

**Expect a meaningful fraction to come back `UNCERTAIN`,** especially preprints, older scans, and conference papers. That is the tool working. A run where everything is confidently confirmed is a run to be suspicious of.

**Then verify the DOIs mechanically:**

```bash
python resources/scripts/doi_checker/check_dois.py references.bib \
    --mailto you@example.edu
```

**Where to keep the PDFs** is a separate decision from where the notes live. Notes and BibTeX are small and text — they belong in the manuscript repository, under version control. A few hundred megabytes of PDFs usually do not, particularly if that repository syncs with a collaborative editor. Reference managers, shared storage, and a git-ignored local folder are all defensible; what matters is that the choice is written down so a collaborator can find them.
