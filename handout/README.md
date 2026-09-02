# Handout

**Rescoped 2026-09-02:** printed, one sheet, front and back (~1.5 pages of actual content) — Alex can get copies made for students at that length, not longer. This is a big change from the original "denser leave-behind covering everything" concept; it's now a compact reference card plus a pointer to the repo, not a standalone document that reproduces `resources/`. Not yet built.

Given the length limit, the handout's job is to be memorable and to get someone back to this repository — not to be comprehensive. Anything not listed below stays online-only in [`resources/`](../resources/README.md) and the handout links to it rather than repeating it.

## Planned contents

**Front:**
- Title, one-line thesis, event footer (title/date optional depending on final layout)
- The lifecycle diagram — Explore → Ground → Build → Record → Write → Verify — with one short line per stage (the core teaching point from each [outline.md](../outline.md) section, not the supporting detail)
- The one callout that has to land: *"The filesystem/repository is the source of truth. The AI conversation is not."*
- The claim-audit table (Outline Section 7) as the single worked example — it's the most memorable image in the talk and earns the space

**Back:**
- A short "Monday morning" checklist (4–6 items, one line each): keep a project-instructions file, keep a research log, ground literature claims in real sources you've read, review every AI-generated diff before accepting it, run a claim-audit pass before submitting a paper
- A compact Notre Dame box: the 🟢🟡🟠🔴 data-classification tiers, "Claude = Public data only (for now)," and the `researchsecurity@nd.edu` DoD/DoW contact — see [notes/references.md](../notes/references.md)
- Links: this GitHub repo (for `resources/`, the full prompts, and the checklists), the Anthropic Team-for-Scientists application, and the Amateur Radio book repo if there's room

## Explicitly cut from the handout (now online-only in `resources/`)

Full literature-folder workflow, full repository-pattern write-ups and provenance-manifest example, the complete manuscript-audit toolkit (methods-vs-code, figure-vs-text, journal-guideline compliance), the reproducibility/handoff checklist in full, and the writing-style workflow. Each still gets built as a proper resource — see [resources/README.md](../resources/README.md) — they just don't fit on paper anymore.

## Planned layout

```
handout/
├── main.tex
├── sections/
└── README.md   this file
```
