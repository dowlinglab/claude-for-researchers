# Slides

Two Beamer decks for *Claude for Research: Beyond the Chatbot*, sharing all slide
sources. Part 1 (September 28) has **34 slides**; Part 2 (October 12) has **42**.
Part 1's lecture frames keep their numbers (1–27), and it appends activity
frames, a regroup, and a recap. Part 2 opens with the Part 1 recap (frame 2), a bridge frame (3), and five Git and
GitHub recap frames (4–8), so its later lecture frames moved by six: the
original frames 27–54 are now frames 9–36. Tablet annotations made
for the earlier Part 2 numbering no longer line up.

Each 105-minute session uses **35 minutes presentation, 10 Q&A, 45 hands-on,
and 15 regroup**. Part 1's activity starts from a notebook handoff: students use
Claude as a tutor to turn the folder into a clean GitHub repository, with
optional paths that continue into a reproducible project. Part 2 recaps Git and
GitHub with figures, then runs a statistics audit: participants check a
colleague's analysis against open references and judge the audit. The public
decks contain participant-facing activity and regroup frames; private instructor
builds add answer reveals from the private repository.

## Build and verify

From this directory:

```bash
make
```

The outputs are `part1_slides.pdf` and `part2_slides.pdf`. `make part1` or `make part2` builds
one session. There is no combined deck. `make notes`
builds `part1_slides_notes.pdf` and `part2_slides_notes.pdf`, instructor copies with each
frame's speaker notes beside it. The notes mark where to stop talking and let
participants work. See [`pacing_notes.md`](pacing_notes.md) for possible cuts.
`make watch MAIN=part1` watches the first part. The shared entry point uses a
part selector, and `\part` records each session without adding divider frames.

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
| `storyboard.md` | Two-part mapping of the original 54 slides plus session opening/closing frames |
| `check_layout.py` | Flags slides that are top-empty and bottom-crowded; run it after layout changes |
| `image_plan.md` | Final inventory of image and native visual assets |
| `pacing_notes.md` | Where the lecture is long relative to hands-on time, and possible cuts |
| `style_guide.md` | Typography, color, density, logo, and verification rules |

The deck uses the [Dowling Lab ND Beamer Template](https://github.com/dowlinglab/ND_Beamer_Template).

## Source-comment decision

After the September 11, 2026 final audit, the detailed editorial and historical comments were removed from `main.tex` and `sections/*.tex`. The comments were valuable during refinement but made the final source harder to scan. Their full rationale remains available in Git history through commit `2c55c74`; future durable decisions should be recorded concisely in the relevant Markdown file and commit message.
