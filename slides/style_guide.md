# Slide style guide

The rule set the Beamer decks (`main.tex`, `sections/*.tex`) follow. It was derived from two delivered talks by the same speaker, a 26-slide teaching talk and a 51-slide faculty seminar. The teaching talk's register is the model, because this audience listens to a spoken narrative rather than reading equations. History lives in Git.

## Rules

1. **One title size.** The theme's `frametitle` template enforces it everywhere except the cover slide, which has its own typographic treatment.
2. **Two body sizes.** `\large` for the slide's one argument (the `\slidepoint` callout); `\small` for everything that supports it. Do not use `\Large`, ad hoc `\normalsize`, or `\footnotesize` for running prose. `\scriptsize` and `\tiny` are for diagram micro-labels and code only.
3. **Logo bottom-left,** drawn automatically by the theme. Section files never add it. Check any new content-heavy or fully centered frame visually, because the logo collides easily with a bottom line of body text.
4. **Colors.** Official Notre Dame colors only, defined once (`NDBlue` `#0C2340`, Dome Gold `#C99700`, Irish Green `#00843D`; contrast ratios in [`theme/README.md`](theme/README.md)), plus the Okabe-Ito colors for data and status marks. Text is `NDBlue` or black, and never `Muted` gray on body prose, captions, or asides, because gray reads as too low-contrast. `NDGold` and `IrishGreen` are accents (rules, bullets, outlines). `Muted` is for non-text elements meant to look inactive and for code comments.
5. **No closing takeaway bar.** It mostly repeated the frame title in different words. State the slide's point in the title, and treat the body (table, list, quote) as evidence for a claim already made.
6. **Text density.** About 20 to 25 words of prose per narrative slide, not counting titles and diagram labels. A slide that needs more is doing two jobs: split it, or make it a labeled backup slide if the extra material is reference.
7. **Grouping boxes are for parallel content.** Use colored-outline panels for genuinely parallel, comparable things, never as a lone accent stripe. Use the shared `nd box` and `nd highlight` TikZ styles: white interior, gold outline at 0.8 pt, 2 pt rounded corners, ND Blue text, and a green outline for the highlighted item, such as the active act on a divider.
8. **Center vertically; do not pin content to the top.** Wrap frame content in `\vfill ... \vfill`. For side-by-side content, use `\begin{columns}[c]`. Use `[t]` only for text columns that are meant to start on the same line. When a slide looks top-heavy or lopsided, check alignment and `\vfill` placement before touching content or proportions.
9. **Every visual element earns its space.** Before adding a diagram, icon, or repeated motif, ask what it changes about what the audience understands. If it repeats what the title or a table already says, cut it. The act strip belongs on the `\stagedivider` transition slides, where one stage lights up, and not as a second copy beside an outline that shows the same thing.
10. **Look at the rendered slide.** A frame can compile cleanly and still show lopsided whitespace, a collision with the corner logo, or an element with no job. Render with `pdftoppm` and look at each frame you touched. `check_layout.py` flags top-empty and bottom-crowded frames but does not replace looking.
11. **Fix a corner-logo collision with a fixed floor,** not a larger `\vfill` weight. On a dense frame the trailing `\vfill` is already near zero, so changing its weight does nothing. End the frame with `\vspace{1.8cm plus 1fill}`, which clears the logo at its current size. If the frame still collides, reduce content height (a smaller code font, a shorter image, tighter spacing, fewer words). Recompute the floor if the logo size changes: its height is about its width times 0.4125.
12. **Bold a few key words in a `\slidepoint`, never the whole sentence.** `\slidepoint` sets the callout color and size but does not bold its argument. Each call site wraps its own one or two key words in `\textbf{}`: usually a contrasting verb or noun pair, or the one concrete outcome in an otherwise plain sentence. The same habit applies to a long necessary quote: bold a handful of phrases so it can be skimmed, rather than paraphrasing it shorter.

## Conventions

- **Anonymous examples.** Non-public examples stay generic so that no student or collaborator is identifiable, so slides carry no photo-credit headshots.
- **Annotate equations in place** (colored terms connected to plain-language labels) if an equation ever needs term-by-term explanation, rather than adding a separate legend.
- After any content, layout, or corner-logo change, rebuild and inspect every affected frame.
