# Image plan

Every visual in the deck, planned before more slides get drafted. Companion to [`storyboard.md`](storyboard.md) — same slide numbering.

## Three kinds of visual, and how each gets made

**A. Typeset text-artifacts** (`lstlisting`, `tabular`, TikZ boxes) — commit messages, file trees, code, macros. **No image file.** Typeset directly, styled with the deck's existing `\lstset{style=plain}`. Crisper than a screenshot at projector resolution, and the pattern is already established (`02_act1_understand.tex`'s commit-message slide).

**B. Constructed diagrams** (TikZ) — the act strip, workflow arrows, the claim-tracing table. Built in LaTeX, not an image file. Same reasoning as A: vector, scales, matches the palette exactly.

**C. Real images** — photos, logos, and screenshots where the *fact that something really happened* is the point, not just the words. This is the category that needs planning, below.

## The rule that decides category C: screenshot only when the chrome is the proof

A screenshot earns its place when the browser/GitHub/PyPI frame around the content is doing work — proving a package is really published, a commit is really public and dated, a page really says what you claim. Otherwise it's clutter competing with a cleaner typeset version of the same text. Every row below states which case it is.

## The confidentiality boundary

**Public repos → real screenshots are fair game and preferred** (grad-visit-scheduler, emcal, bits_for_gaps, radio-extra-book — all public under `dowlinglab`/`adowling2`). **Private or unpublished work → illustrative reconstruction only**, same rule as the practice files: synthetic numbers, no project names, nothing that could deanonymize or expose pre-publication content. This hits Act III hardest — the claim-audit table, the empty-nomenclature example, and the eleven-wrong-items status report all come from unpublished audits and manuscripts. None of those get real screenshots. Flagged per-row below.

**Capture constraint, found 2026-09-02:** the in-app browser used for autonomous verification passes can view and read pages but has no way to save a screenshot to disk — only "Claude in Chrome" (the user's real, logged-in browser) can, and connecting that needs the user to click "Connect," which an unattended session can't do. So every "TODO: capture a real screenshot" note in this file is a task for a live session with Alex present, not something a background pass can finish on its own. What a background pass *can* do, and already has: read these same pages to verify the facts on the slide against them (see `notes/seminar_notes.md`/commit history 2026-09-02 for two real corrections this caught) — verification and image capture are different capabilities, don't conflate them when reading "not yet captured" below.

---

## Prologue — Tinker

**Revised 2026-09-03** against the current 10-slide list: the teaser is now two hook slides with real visual plans (was one, text-only); the claim moved from item 2 to item 4; data classification and the two-checks list moved out entirely (now Epilogue items 2-3); a new archetypes slide (item 9) needs no image; the resources slide (item 8) is now a typeset filename list per Alex's explicit request, not a candidate screenshot.

| # | Slide | Visual | Type | Status |
|---|---|---|---|---|
| 1 | Title | ND wordmark | C | ✅ have (`figures/nd_logo.png`) |
| 2 | Before Codex: ten hours, a notebook, then patches | a visit-day-schedule grid | B (synthetic) | **built, deliberately synthetic, not a real screenshot** — a real generated schedule carries visiting students' and faculty's actual names/times, which is exactly the personal data the Epilogue's classification slide says not to publish. Illustrative by design, not a placeholder waiting on capture |
| 3 | One weekend with Codex, and I kept going | version-timeline TikZ (real dates/versions) | B (real data) | built — moved here from Act II 2026-09-03 (see that section's note); **candidate upgrade to real screenshots**: PyPI page, GitHub tag list, commit graph — see "what needs capturing" below |
| 4 | The claim | none | — | text only, framing slide, deliberately spare — moved here from item 2 |
| 5 | Borrowed structure | TAL logo + act-strip | C + B | ✅ have (`figures/tal_logo.png`) + built; act list is now single-line entries, not a two-line table |
| 6 | One year of practices, not a tool tutorial | act-strip only | B | built |
| 7 | Don't become loyal to a model | vendor table | text | no image needed |
| 8 | Everything today is on GitHub | typeset filename list (all 9+3+3+3 files) + repo link | text | **resolved 2026-09-03**: was a candidate for a real GitHub repo-tree screenshot; Alex asked instead for the actual filenames typeset directly, which fills the space better and needs no capture |
| 9 | Six kinds of task, all year, most of them familiar | none | — | text only, new 2026-09-03 — previews the six-types table above, no new visual needed |
| 10 | This talk was built the same way | none | — | text only, a numbered list |

Moved to the Epilogue, 2026-09-03: "ND data classification" and "Check before you start" — see that section below.

## Act I — Understand

**Revised 2026-09-03**: the old opening slide ("Open on the failure," the real `emcal` commit) is cut entirely — too in-the-weeds for its cost, per Alex, with more room going to visual examples elsewhere. Everything below is renumbered down by one; row 2 ("What git and GitHub give you") now introduces the `emcal` commit fresh rather than referencing a preceding slide. A `\stagedivider` transition slide opens the act (text only, act-strip + question, no row needed here).

| # | Slide | Visual | Type | Status |
|---|---|---|---|---|
| 1 | State the shift | a conversation vs. a repository, in the abstract | — | text only |
| 2 | What git and GitHub actually give you | a real screenshot of the `emcal` repo landing page | C | **ready to capture now**: public repo, no confidentiality concern — already listed under "what needs capturing" below. Anchored to the same real commit (`31184f4`), introduced fresh on this slide since the old lead-in slide is gone |
| 3 | Three kinds of context | the membrane-transport project's own persistent/authoritative/task context, named concretely (its conventions; its actual model and data; this run's question) | A | text-artifact, illustrative — Type 1, so generic, no project name |
| 4 | One file, read at the start of every session | that same project's actual `CLAUDE.md`, shown in full via `lstlisting` (built in `02_act1_understand.tex`) | A | text-artifact, illustrative, generic — continues row 3's example rather than switching projects |
| 5 | Parallel A, idea-first: cross two literatures | a real annotation-schema excerpt, plus a small generic TikZ diagram: two literature streams (icons or labeled boxes) converging on one idea | A + B | text-artifact, generalized (no project name) — matches how `literature_review.md` already handles it; the diagram gives the slide something to look at beyond the excerpt, without naming the proposal |
| 6 | Parallel A, corpus-first: the corpus becomes someone's starting point | the getting-started report's actual section list, plus a small generic TikZ diagram: a folder of PDFs -> a report icon | A + B | text-artifact only for the content — the underlying project is private; show the *structure*, never the content. The diagram is process, not content, so it carries no confidentiality risk |
| 7 | Parallel B, closing: a departed collaborator's notebook → git | a generic TikZ workflow diagram: local notebook (no backup) -> `git init` -> GitHub, three boxes with an arrow each | B | a constructed procedure diagram, not visual-less by default. Diagrams are process, not content, so the name-protection rule doesn't block them |

## Act II — Build

**Revised 2026-09-03**: the old two-slide opener (the version-timeline "resolved" slide + the group-impact slide) collapsed into one — the full grad-visit-scheduler story, and its real-image plan, moved to the Prologue hook (see that section above), which now tells it with more room. This act's opener is a one-line callback into new material only. A `\stagedivider` transition slide opens the act (text only, no row needed).

| # | Slide | Visual | Type | Status |
|---|---|---|---|---|
| 1 | As promised — and why it mattered | none | — | text only, deliberately spare — the point is the causal claim, not an artifact; the version-timeline diagram this slide used to show moved to the Prologue |
| 2 | Prototype → promote | a generic before/after file tree | A | text-artifact, illustrative (no real repo needed — the point is the pattern) |
| 3 | Run it, pin it, baseline it | none | — | text only |
| 4 | Freeze the science, move the code | none, or a two-column "old code / new code, science untouched" diagram | B | optional TikZ, not required |
| 5 | Regression harness enabled a reversal | none | — | generic by design (private project) |
| 6 | Not just a hobby-adjacent tool | **real screenshots of emcal and bits_for_gaps** — both public | C | see below |
| 7 | Review the diff | a generic, illustrative diff excerpt | A | text-artifact — corrected 2026-09-02: originally claimed to reuse the real emcal `31184f4` diff, but that commit's actual diff (a JSON fixture + Python test harness) doesn't support this illustration. Relabeled as illustrative rather than forced to fit |
| 8 | Proposal compliance review, inline | the `\foacomment{}` macro + one illustrative flagged comment | A | text-artifact, illustrative (real proposal content stays out) |
| 9 | Verify before you commit | **a real `latexdiff` output** | C | ✅ can generate now — the script produces exactly this, tested this session; use a synthetic example like the one already used to test the script, not real proposal text |

**Slide II.6, "not just a hobby tool":**
- emcal: screenshot of the GitHub repo page (shows the `Ind. Eng. Chem. Res.` paper link, the README's scope statement)
- bits_for_gaps: screenshot of the PyPI page or the ReadTheDocs landing page (shows the DOI, the "improvements over paper" link)
- Both public, capturable now.

## Act III — Challenge

Rewritten 2026-09-02 against the current 7-slide list (5 regular + a 2-part capstone) — the previous version predated the capstone entirely and only covered 6 slides under different numbers.

| # | Slide | Visual | Type | Status |
|---|---|---|---|---|
| 1 | Merging three questions reads as an attack | none | — | text/columns only |
| 2 | Trace every number to its file | **the claim-tracing table**, using `\good`/`\bad`/`\unknown` | B | **illustrative, built in tabular with synthetic numbers** — this is the outline's existing example (17% cost reduction / "approximately doubles") plus one added mismatch row, already de-identified. Do not source real numbers from any unpublished audit. First real use of the `\good`/`\bad`/`\unknown` macros anywhere in the deck |
| 3 | "Cannot verify" is a result | reuses the same `\unknown{}` mark from slide 2 | — | text only, deliberately spare |
| 4 | A clean build hid a silent failure | none — three short columns | — | text only; the three instances (nomenclature table, `.gitignore`, `CLAUDE.md`) are all either unpublished or already covered visually elsewhere (the course's own `.gitignore` incident doesn't need re-illustrating) |
| 5 | Status report wrong on eleven items | none | — | text only; the specific number stays but no document is shown |
| 6 | Capstone, part 1 | a real screenshot of `ndcbe.github.io/optimization` and, if available, a coursepack page showing the corrected sign | C | **not yet captured** — public, Alex's own course, no confidentiality concern. Typeset fallback ships in the meantime (see `04_act3_challenge.tex`'s TODO) |
| 7 | Capstone, part 2 | none | — | text only, closes the act |

**Act III is deliberately the most image-light act** for slides 1-5. Its evidence is the least reproducible visually without exposing unpublished work, so it leans on typeset tables rather than screenshots — that's a feature of the confidentiality boundary working as intended, not a gap to fill. The capstone (6-7) is the exception: a named, public example, so a real screenshot is both possible and worth capturing.

## Epilogue — Trust

**Revised 2026-09-03**: two IT-policy slides moved in from the Prologue (rows 2-3 below) — Alex's suggestion that they read as "Trust" material. The summary matrix (now row 4) still carries the 7th row ("Creating this talk") from the meta-slide living in the Prologue. A `\stagedivider` transition slide opens the Epilogue (text only, no row needed).

| # | Slide | Visual | Type | Status |
|---|---|---|---|---|
| 1 | Back to the question | none | — | text only, deliberately spare |
| 2 | ND data classification | the 🟢🟡🟠🔴 table | text/B | moved here from the Prologue 2026-09-03. **candidate real screenshot**: the actual `ai.nd.edu/ai-in-action/approved-ai-tools/` page, cropped to the tier legend + the Claude row. Proves the "Public data only" finding isn't a paraphrase. Needs the in-app browser (fetch tool can't reach this domain — see `notes/references.md`). Re-verify current before capturing; the page changes |
| 3 | Check before you start | none | — | text only. Moved here from the Prologue 2026-09-03 |
| 4 | A handful of projects, recurring | the summary matrix (types × acts, `\good{}` marks, 7 rows) | B | built, typeset tabular — no image file needed |
| 5 | You own every claim | none | — | text only |
| 6 | Curiosity is a feature, not a consolation prize | ✅ have, in use | C | `figures/boot_dryer_octopus.jpeg` (the spoken anchor); kitchen organizer/telescope shelf and `radio-extra-book` are a link-only mention on the same slide, no image shown |
| 7 | One thing to change Monday morning | none | — | text only |

---

## What's already in hand

`figures/nd_logo.png`, `figures/tal_logo.png` (+ source `.svg`), `figures/boot_dryer_octopus.jpeg`, `figures/kitchen_organizer_telescope_shelf.jpeg`. Also usable: `resources/scripts/figure_style/example.png` (the corrected-legend demo) as a small aside anywhere the deck wants to show "even a generated figure needs a check" — not currently slotted, a candidate for Act II's figures-adjacent content if that gets its own beat.

## What needs capturing (public, ready now)

All via the in-app browser, no confidentiality concern:

1. `pypi.org/project/grad-visitor-scheduler` — package page
2. `github.com/dowlinglab/grad-visit-scheduler/tags` — version history
3. `github.com/dowlinglab/emcal/commit/31184f4` — the verified real commit
4. `github.com/dowlinglab/emcal` — repo landing page
5. `github.com/dowlinglab/bits_for_gaps` and/or its ReadTheDocs page
6. `ai.nd.edu/ai-in-action/approved-ai-tools/` — the data-classification table (re-verify current before capturing)

## What needs building (no external source, just work)

- A synthetic `latexdiff` output for Act II §10 — reuse the same fixture already used to test `latexdiff_check.sh`
- A synthetic empty-nomenclature reconstruction for Act III §4
- A generic before/after file tree for Act II §3 (no real repo needed)

## What must stay illustrative (confidentiality)

Act I §3, §4, §6 (renumbered 2026-09-03 — the membrane-transport context/`CLAUDE.md` pair and the corpus-first parallel); Act II §8 (renumbered same day); Act III §2, §4, §6 — all touch unpublished or private work. Text-artifacts and TikZ only, generalized, no project names — same discipline already applied throughout `resources/practices/`. Also the Prologue's schedule-grid mockup (item 2) — not confidentiality-driven in the same sense (grad-visit-scheduler is public), but the same rule in spirit: a real generated schedule would carry real people's names and times, so it stays synthetic by design, not just until a screenshot pass runs.

## Open question

**Should I go capture the six "ready now" screenshots today**, or hold until the corresponding sections are actually being drafted? Capturing now risks a page changing before the talk (the ND policy page especially); capturing at draft-time means fewer round trips but interrupts drafting flow. My default would be to capture the six now, save them into `slides/figures/` with a note recording the URL and capture date (same provenance discipline as the TAL logo), and re-verify anything policy-related closer to September 17.
