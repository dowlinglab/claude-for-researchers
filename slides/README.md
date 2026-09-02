# Slides

Beamer source for the live talk. Not yet started — see [outline.md](../outline.md) for the content plan this will follow.

**Base template:** [ND Beamer Template](https://github.com/dphow/ND_Beamer_Template) (public domain). `\documentclass{beamer}`, `\usetheme{NotreDame}`; supports TikZ for diagrams and `listings` for code/file-tree display.

**Design constraints** (from [notes/seminar_design.md](../notes/seminar_design.md)):
- Little text per slide; strong visual hierarchy.
- Concrete examples over abstract claims — repository trees, before/after diffs, real prompts and outputs.
- Diagrams for workflow structure (e.g., the lifecycle arrow, the context-file pattern).
- No decorative AI/robot/brain imagery.

## Planned layout

```
slides/
├── main.tex          entry point, \usetheme{NotreDame}, includes sections
├── sections/          one .tex file per outline.md section
├── figures/           diagrams, screenshots, file-tree images
└── README.md          this file
```

Build once `outline.md` is considered stable and the ND theme files have been added here.
