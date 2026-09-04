# Vendored ND Beamer theme

Source: [github.com/dowlinglab/ND_Beamer_Template](https://github.com/dowlinglab/ND_Beamer_Template) (the Dowling Lab's own fork of [dphow/ND_Beamer_Template](https://github.com/dphow/ND_Beamer_Template), public domain). Retrieved 2026-09-03.

Vendored rather than referenced so this repository builds after a clone, with no hunting for dependencies — which is the same argument the seminar makes about pinning anything else a result depends on.

| File | Purpose |
|---|---|
| `beamerthemeNotreDame.sty` | The theme; declares the options below |
| `logos/` | Official Notre Dame academic marks and monogram, vector PDFs, in the colors and shapes the theme's own options select between |

This deck previously vendored the unforked upstream theme (`dphow/ND_Beamer_Template`), which used its own `[white, nologo]` boolean options, a `beamercolorthemeNotreDame*.sty` pair for palette selection, and Notre Dame logos not committed to that repo at all (`../figures/nd_logo.png`, a raster PNG, filled in locally). The fork replaces all of that: every visual element is its own `key=value` option (see below), real vector marks ship with the theme itself, and the previously-required manual gold correction (see "History" below) is now correct in the theme by default.

## Theme options

See the fork's own [README](https://github.com/dowlinglab/ND_Beamer_Template/blob/master/README.md) for the full, current list. This deck uses:

```latex
\usetheme[cornerlogo=blue, textcolor=blue, titlelayout=leftrule]{NotreDame}
```

- `cornerlogo=blue` — the small mark, bottom-left, on every frame after the title slide (replaces this deck's own former hand-rolled `\ndcornerlogo`).
- `textcolor=blue` — body text defaults to ND Blue rather than black (replaces `\setbeamercolor{normal text}{fg=NDBlue}`).
- `titlelayout=leftrule` — the left-aligned title-page style this deck's title slide was built around by hand before the fork existed; promoted into the theme itself, so this deck's title slide is now `\titlepage`, not bespoke code (see `../main.tex`).

## Local modifications

**None.** The `.sty` file and `logos/` are unmodified from the fork. Everything specific to this deck lives in `../main.tex`, so the vendored files can be re-pulled from upstream without losing anything.

## History: the gold correction

The original vendored theme defined `NDGold` as RGB (174, 143, 64) = `#AE8F40` — not the University's Dome Gold — so this deck overrode it locally in `main.tex`. The fork corrects `NDGold` to `#C99700` (PMS 117) directly, so **that override no longer exists in `main.tex`** as of the 2026-09-03 migration. The measurements below still hold; they're just enforced by the theme now, not a per-deck patch.

| Foreground | On white | On ND Blue |
|---|---|---|
| ND Blue `#0C2340` | 15.79 | — |
| Dome Gold `#C99700` | **2.65** ✗ | 5.95 ✓ |
| Irish Green `#00843D` | 4.81 ✓ | 3.28 ✗ |
| White | — | 15.79 |

**Dome Gold never carries text on white.** It is used for rules, fills, and the active lifecycle stage only.
