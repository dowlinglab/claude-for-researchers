# Slides

Current Beamer draft for *Claude for Research: Beyond the Chatbot*. The presentation has 55 slides and is designed for a 40-minute talk followed by discussion.

## Build and verify

From this directory:

```bash
make
```

The compiled presentation is `main.pdf`. From the repository root, run the documentation check with:

```bash
python3 resources/scripts/check_docs.py
```

## Structure

| Path | Purpose |
|---|---|
| `main.tex` | Theme configuration, shared macros, title slide, and section includes |
| `sections/` | Slide content organized by the talk's five-part structure |
| `figures/` | Images used by the deck |
| `theme/` | Vendored Notre Dame Beamer theme and logos |
| `storyboard.md` | Current 55-slide sequence and narrative through-line |
| `image_plan.md` | Final inventory of image and native visual assets |
| `style_guide.md` | Typography, color, density, logo, and verification rules |

The deck uses the [Dowling Lab ND Beamer Template](https://github.com/dowlinglab/ND_Beamer_Template).

## Source-comment decision

After the September 11, 2026 final audit, the detailed editorial and historical comments were removed from `main.tex` and `sections/*.tex`. The comments were valuable during refinement but made the final source harder to scan. Their full rationale remains available in Git history through commit `2c55c74`; future durable decisions should be recorded concisely in the relevant Markdown file and commit message.
