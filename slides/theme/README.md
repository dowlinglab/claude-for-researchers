# Vendored ND Beamer theme

Source: [github.com/dowlinglab/ND_Beamer_Template](https://github.com/dowlinglab/ND_Beamer_Template), the Dowling Lab's fork of [dphow/ND_Beamer_Template](https://github.com/dphow/ND_Beamer_Template) (public domain). Retrieved 2026-09-03.

Vendored rather than referenced so the repository builds after a clone, with no hunting for dependencies. That is the same argument the seminar makes about pinning anything else a result depends on.

| File | Purpose |
|---|---|
| `beamerthemeNotreDame.sty` | The theme; declares the options below |
| `logos/` | Official Notre Dame academic marks and monogram, as vector PDFs, in the colors and shapes the theme's options select between |

The `.sty` file and `logos/` are unmodified from the fork. Everything specific to these decks lives in `../main.tex`, so the vendored files can be re-pulled from upstream without losing anything.

## Theme options

See the fork's own [README](https://github.com/dowlinglab/ND_Beamer_Template/blob/master/README.md) for the full, current list. The decks use:

```latex
\usetheme[cornerlogo=fullcolor, titlepagelogo=fullcolor, textcolor=blue, titlelayout=leftrule, monogram=none]{NotreDame}
```

- `cornerlogo=fullcolor` puts the small mark bottom-left on every frame after the title slide. `main.tex` sets its size and margin.
- `titlepagelogo=fullcolor` sets the mark on the title page.
- `textcolor=blue` makes body text ND Blue rather than black.
- `titlelayout=leftrule` selects the left-aligned title-page style.

## Build

`../.latexmkrc` puts `theme/` on `TEXINPUTS`, because the theme loads its color theme by name and that search covers the TeX path. `main.tex` also sets `\input@path` and `\graphicspath` so a plain `pdflatex` run finds the theme too.

Several passes are needed because of TikZ `remember picture, overlay` (the corner logo, the title-page logo, and the bottom note): positions are written on one pass and read on the next. `latexmk` handles this by rerunning until stable.

## Color contrast

The theme defines `NDGold` as Dome Gold `#C99700` (PMS 117). WCAG contrast ratios:

| Foreground | On white | On ND Blue |
|---|---|---|
| ND Blue `#0C2340` | 15.79 | n/a |
| Dome Gold `#C99700` | **2.65** (fails) | 5.95 |
| Irish Green `#00843D` | 4.81 | 3.28 (fails) |
| White | n/a | 15.79 |

**Dome Gold never carries text on white.** It is used for rules, outlines, and fills only.
