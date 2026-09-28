# Slides

Two Beamer decks for *Claude for Research: Beyond the Chatbot*, sharing all slide
sources. Part 1 (September 28) has **32 slides**; Part 2 (October 12) has **36**.
The original lecture sections retain their frame numbers: Part 1 frames 1–27,
Part 2 frames 1–31. Each now appends four activity frames and a regroup discussion
frame. Existing tablet annotations therefore retain their part-specific numbers.

Each 105-minute session uses **35 minutes presentation, 10 Q&A, 45 hands-on,
and 15 regroup**. The appended slides support the activity/regroup blocks;
they do not enlarge the 35-minute lecture. Part 1 saves and checks a baseline.
Part 2 checks three claims and revises one; extraction is optional afterward.
Both activities follow the numbered instructions in the corresponding
[two-page printed handout](../handout/README.md). Setup is pre-work.
See the [storyboard](storyboard.md) for the frame mapping.

The public decks contain participant-facing regroup questions. Private instructor
builds reuse these sources and add answer reveals from the private repository;
public builds do not read private files. The empty regroup hooks in `main.tex`
allow this without copying instructor content into public sources.

## Build and verify

From this directory:

```bash
make
```

The outputs are `part1.pdf` and `part2.pdf`. `make part1` or `make part2` builds
one session. `make combined` builds `main.pdf` with both parts (68 slides).
`make watch MAIN=part1` watches the first part. The shared entry point uses a
part selector, and `\part` records each session without adding divider frames.

After layout changes, run from the repository root:

```bash
python3 slides/check_layout.py --pdf slides/part1.pdf
python3 slides/check_layout.py --pdf slides/part2.pdf
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
| `part1.tex`, `part2.tex` | Small entry points selecting one session |
| `sections/` | Slide content organized by the talk's five-part structure |
| `figures/` | Images used by the deck |
| `theme/` | Vendored Notre Dame Beamer theme and logos |
| `storyboard.md` | Two-part mapping of the original 54 slides plus session opening/closing frames |
| `check_layout.py` | Flags slides that are top-empty and bottom-crowded; run it after layout changes |
| `image_plan.md` | Final inventory of image and native visual assets |
| `style_guide.md` | Typography, color, density, logo, and verification rules |

The deck uses the [Dowling Lab ND Beamer Template](https://github.com/dowlinglab/ND_Beamer_Template).

## Source-comment decision

After the September 11, 2026 final audit, the detailed editorial and historical comments were removed from `main.tex` and `sections/*.tex`. The comments were valuable during refinement but made the final source harder to scan. Their full rationale remains available in Git history through commit `2c55c74`; future durable decisions should be recorded concisely in the relevant Markdown file and commit message.
