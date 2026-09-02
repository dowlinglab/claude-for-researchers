# Vendored ND Beamer theme

Source: [github.com/dphow/ND_Beamer_Template](https://github.com/dphow/ND_Beamer_Template), released into the **public domain**. Retrieved 2026-09-02.

Vendored rather than referenced so this repository builds after a clone, with no hunting for dependencies — which is the same argument the seminar makes about pinning anything else a result depends on.

| File | Purpose |
|---|---|
| `beamerthemeNotreDame.sty` | The theme; declares the options below |
| `beamercolorthemeNotreDame.sty` | Default palette (white text on **black**) |
| `beamercolorthemeNotreDameWhite.sty` | White palette — the one this deck uses |

## Theme options

`nav`, `white`, `nologo`, `compactlogo`, `sections`, `noslidenumbers`, `fullFooter`.

This deck uses `[white, nologo]`. See the comment block at the top of `../main.tex` for why.

## Local modifications

**None.** The `.sty` files are unmodified. Everything specific to this deck — including the gold correction below — lives in `../main.tex`, so the vendored files can be re-pulled from upstream without losing anything.

## One correction applied in `main.tex`, not here

The theme defines `NDGold` as RGB (174, 143, 64) = `#AE8F40`. That is **not** the University's Dome Gold. `main.tex` overrides it:

| | Theme | Official |
|---|---|---|
| ND Blue | `#0C2340` | `#0C2340` ✓ |
| Gold | `#AE8F40` | `#C99700` (PMS 117) |

The blue matches exactly, which is good corroboration for the rest. Verified 2026-09-02 against Notre Dame branding sources; `onmessage.nd.edu` could not be read directly by any tool available at the time, so **confirm in a browser before the talk**.

Contrast, measured (WCAG needs 4.5:1 for body text):

| Foreground | On white | On ND Blue |
|---|---|---|
| ND Blue `#0C2340` | 15.79 | — |
| Dome Gold `#C99700` | **2.65** ✗ | 5.95 ✓ |
| Irish Green `#00843D` | 4.81 ✓ | 3.28 ✗ |
| White | — | 15.79 |

**Dome Gold never carries text on white.** It is used for rules, fills, and the active lifecycle stage only.
