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

Rewritten 2026-09-02 against the current 10-slide list — the previous version predated the thesis/scoping restoration and the resources/meta slides entirely, and only ever numbered 7 items.

| # | Slide | Visual | Type | Status |
|---|---|---|---|---|
| 1 | Title | ND wordmark | C | ✅ have (`figures/nd_logo.png`) |
| 2 | The claim | none | — | text only, framing slide, deliberately spare |
| 3 | The teaser (grad-visit-scheduler) | none yet — text only for the tease; save the visual payoff for Act II's full return | — | by design |
| 4 | Borrowed structure | TAL logo + act-strip | C + B | ✅ have (`figures/tal_logo.png`) + built |
| 5 | Today | act-strip only | B | built |
| 6 | The landscape | vendor table | text | no image needed |
| 7 | ND data classification | the 🟢🟡🟠🔴 table | text/B | **candidate real screenshot**: the actual `ai.nd.edu/ai-in-action/approved-ai-tools/` page, cropped to the tier legend + the Claude row. Proves the "Public data only" finding isn't a paraphrase. Needs the in-app browser (fetch tool can't reach this domain — see `notes/references.md`). Re-verify current before capturing; the page changes. |
| 8 | Check before you start | none | — | text only |
| 9 | What you get today | a real `ls resources/` or a cropped repo-tree screenshot of GitHub's own file browser on this repo, once it's pushed | C | **needs the repo pushed to GitHub first** — can't screenshot a page that doesn't exist yet. Built with a typeset tree in the meantime |
| 10 | This talk was built the same way | none | — | text only, a numbered list — moved here from the Epilogue 2026-09-02 |

## Act I — Understand

Rewritten 2026-09-02 against the current 8-slide list in `storyboard.md` — the previous version of this table predated even the original 6-slide lock and no longer matched it (a numbered "graduating-student case" and "correct in place" slide that no longer exist as such, no rows at all for the two slides restored from `02_context.tex`). Alex's priority stated the same day: every slide's example should be concrete and front-and-center, since the use cases are both what holds the room's attention and the source of the visuals — no slide here should rest on an abstract statement with "none" as its visual.

| # | Slide | Visual | Type | Status |
|---|---|---|---|---|
| 1 | Open on the failure | the real commit message | A | **verified real**: `dowlinglab/emcal` commit `31184f4`. Exact quoted text confirmed present. Candidate upgrade from typeset (current) to a real screenshot of the GitHub commit page — the chrome proves it's public and dated, which matters for a slide whose point is "this really happened, and you can go check." |
| 2 | State the shift | the same commit, referenced again, not a fresh generic diagram | A | reuses slide 1's artifact rather than illustrating "conversation vs. repository" in the abstract — keeps the real example doing the work across two slides instead of one |
| 3 | What git and GitHub actually give you | a real screenshot of the `emcal` repo landing page | C | **ready to capture now**: public repo, no confidentiality concern — already listed under "what needs capturing" below. Shows what a commit/repository/GitHub host actually look like, anchored to the same failure |
| 4 | Three kinds of context | the membrane-transport project's own persistent/authoritative/task context, named concretely (its conventions; its actual model and data; this run's question) | A | text-artifact, illustrative — Type 1, so generic, no project name; this is the fix for the version of this slide that stated the taxonomy with no example at all |
| 5 | One file, read at the start of every session | that same project's actual `CLAUDE.md`, shown in full via `lstlisting` (built in `02_act1_understand.tex`) | A | text-artifact, illustrative, generic — continues slide 4's example rather than switching projects |
| 6 | Parallel A, idea-first: cross two literatures | a real annotation-schema excerpt, plus a small generic TikZ diagram: two literature streams (icons or labeled boxes) converging on one idea | A + B | text-artifact, generalized (no project name) — matches how `literature_review.md` already handles it; the diagram gives the slide something to look at beyond the excerpt, without naming the proposal |
| 7 | Parallel A, corpus-first: the corpus becomes someone's starting point | the getting-started report's actual section list, plus a small generic TikZ diagram: a folder of PDFs -> a report icon | A + B | text-artifact only for the content — the underlying project is private; show the *structure*, never the content. The diagram is process, not content, so it carries no confidentiality risk |
| 8 | Parallel B, closing: a departed collaborator's notebook → git | a generic TikZ workflow diagram: local notebook (no backup) -> `git init` -> GitHub, three boxes with an arrow each | B | added 2026-09-02, replacing "none" — Alex's note: an anonymized slide should still get a constructed procedure diagram, not go visual-less by default. Diagrams are process, not content, so the name-protection rule doesn't block them |

## Act II — Build

Renumbered 2026-09-02: slide 1 expanded and a new slide 2 inserted (Jeff Kantor's credit, the group-wide impact), shifting everything after down by one.

| # | Slide | Visual | Type | Status |
|---|---|---|---|---|
| 1 | The hook, in full | **this slide carries the most real-image weight in the deck** — see below | C | planned in detail below |
| 2 | This changed how the whole group works | none | — | text only, deliberately spare — the point is the causal claim, not an artifact |
| 3 | Prototype → promote | a generic before/after file tree | A | text-artifact, illustrative (no real repo needed — the point is the pattern) |
| 4 | Run it, pin it, baseline it | none | — | text only |
| 5 | Freeze the science, move the code | none, or a two-column "old code / new code, science untouched" diagram | B | optional TikZ, not required |
| 6 | Regression harness enabled a reversal | none | — | generic by design (private project) |
| 7 | Not just a hobby-adjacent tool | **real screenshots of emcal and bits_for_gaps** — both public | C | see below |
| 8 | Review the diff | a generic, illustrative diff excerpt | A | text-artifact — corrected 2026-09-02: originally claimed to reuse the real emcal `31184f4` diff, but that commit's actual diff (a JSON fixture + Python test harness) doesn't support this illustration. Relabeled as illustrative rather than forced to fit |
| 9 | Proposal compliance review, inline | the `\foacomment{}` macro + one illustrative flagged comment | A | text-artifact, illustrative (real proposal content stays out) |
| 10 | Verify before you commit | **a real `latexdiff` output** | C | ✅ can generate now — the script produces exactly this, tested this session; use a synthetic example like the one already used to test the script, not real proposal text |

**Slide II.1, "The hook, in full" — the real-image plan:**
- A screenshot of the **PyPI page** for `grad-visitor-scheduler` (proves it's really published)
- A screenshot of the **GitHub tag list** (`v0.1.1` → `v0.5.0`) or the releases page (proves the real dates/versions)
- Optionally, the **GitHub commit graph** around Feb 12 showing the dense single-day cluster (visually makes the "20-minute live demo" claim concrete)
- All three: public repo, no confidentiality concern, capturable now via the in-app browser.

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

Updated 2026-09-02 to match the current 5-slide list built in `05_epilogue.tex` — the summary matrix now carries a 7th row ("Creating this talk") instead of a dedicated meta-slide, which moved to the Prologue (item 10 there) on Alex's second thought.

| # | Slide | Visual | Type | Status |
|---|---|---|---|---|
| 1 | Back to the question | none | — | text only, deliberately spare |
| 2 | A handful of projects, recurring | the summary matrix (types × acts, `\good{}` marks, now 7 rows) | B | built, typeset tabular — no image file needed |
| 3 | You own every claim | none | — | text only |
| 4 | Curiosity is a feature, not a consolation prize | ✅ have, in use | C | `figures/boot_dryer_octopus.jpeg` (the spoken anchor); kitchen organizer/telescope shelf and `radio-extra-book` are a link-only mention on the same slide, no image shown |
| 5 | One thing to change Monday morning | none | — | text only |

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

Act I §4, §5, §7 (renumbered 2026-09-02 — the membrane-transport context/`CLAUDE.md` pair and the corpus-first parallel); Act II §9 (renumbered same day); Act III §2, §4, §6 — all touch unpublished or private work. Text-artifacts and TikZ only, generalized, no project names — same discipline already applied throughout `resources/practices/`.

## Open question

**Should I go capture the six "ready now" screenshots today**, or hold until the corresponding sections are actually being drafted? Capturing now risks a page changing before the talk (the ND policy page especially); capturing at draft-time means fewer round trips but interrupts drafting flow. My default would be to capture the six now, save them into `slides/figures/` with a note recording the URL and capture date (same provenance discipline as the TAL logo), and re-verify anything policy-related closer to September 17.
