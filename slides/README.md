# Slides

Beamer source for the live talk, in progress. The slide-level content plan is [storyboard.md](storyboard.md) (supersedes `outline.md`'s section list); visual sourcing per slide is [image_plan.md](image_plan.md); typography/color/density/logo rules are [style_guide.md](style_guide.md), extracted from Alex's own real PowerPoint talks. `sections/00_open.tex`, `01_ecosystem.tex`, `02_context.tex` predate all three and are due for a rewrite — see `storyboard.md`'s status line.

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
