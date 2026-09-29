# Slides

Two Beamer decks for *Claude (or Codex) for Research: Beyond the Chatbot*, sharing
all slide sources. Part 1 appends activity frames, a regroup, and a recap to the
lecture. Part 2 opens with the Part 1 recap and a Git and GitHub recap before the
rest of the lecture. [`storyboard.md`](storyboard.md) maps the frame numbers, which
change whenever frames are added or cut.

Each 105-minute session uses **35 minutes presentation, 10 Q&A, 45 hands-on,
and 15 regroup**. Part 1's activity starts from a notebook handoff: students use
Claude as a tutor to turn the folder into a clean GitHub repository, with
optional paths that continue into a reproducible project. Part 2 recaps Git and
GitHub with figures, then runs a statistics audit: participants check a
teammate's analysis against open references and judge the audit. The public
decks contain participant-facing activity and regroup frames; private instructor
builds add answer reveals from the private repository.

## Build and verify

From this directory:

```bash
make
```

The outputs are `part1_slides.pdf` and `part2_slides.pdf`. `make part1` or `make part2` builds
one session. There is no combined deck. `make runsheets` builds
`run_sheets/part1_run_sheet.pdf` and `run_sheets/part2_run_sheet.pdf`, one-page
facilitator sheets: where to stop talking, the live demo, what to watch for during
the work block, the regroup plan, and possible cuts. They are for printing and are
not part of the release.
`make watch` rebuilds Part 1 on every save; `make watch MAIN=part2_slides` watches Part 2.
Each entry file sets `\seminarpart` before including `main.tex`, and `\part` records
each session without adding divider frames.

After layout changes, run from the repository root:

```bash
python3 slides/check_layout.py --pdf slides/part1_slides.pdf
python3 slides/check_layout.py --pdf slides/part2_slides.pdf
```

Render and inspect each touched frame with `pdftoppm`; the checker is a heuristic,
not a substitute for looking at the PDF. Run the documentation check with:

```bash
python3 resources/scripts/check_docs.py
```

## Structure

| Path | Purpose |
|---|---|
| `main.tex` | Shared theme, macros, session titles, and conditional section includes |
| `part1_slides.tex`, `part2_slides.tex` | Small entry points selecting one session |
| `sections/` | Slide content organized by the talk's five-part structure |
| `figures/` | Images used by the deck. `figures/git_recap/` holds the TikZ sources for the Git and GitHub recap |
| `theme/` | Vendored Notre Dame Beamer theme and logos |
| `storyboard.md` | Frame-by-frame map of each session |
| `check_layout.py` | Flags slides that are top-empty and bottom-crowded; run it after layout changes |
| `image_plan.md` | Inventory of image and native visual assets |
| `run_sheets/` | LaTeX sources for the two facilitator run sheets |
| `style_guide.md` | Typography, color, density, logo, and verification rules |

The deck uses the [Dowling Lab ND Beamer Template](https://github.com/dowlinglab/ND_Beamer_Template).

The slide sources are released under the BSD 3-Clause license. The Notre Dame logos and the screenshots and images from other sources are not, so read [`NOTICE.md`](../NOTICE.md) before reusing the slides or figures.
