# Remaining follow-up items

The September 11 practice-feedback implementation is recorded in [the feedback map](practice_feedback_2026-09-11.md). The current deck has 54 slides and six research tasks; the September 14 annotated read-through revisions are logged in [seminar_notes.md](seminar_notes.md).

**The event changed on September 21, 2026** from a single 1-hour talk (October 15, Carey Auditorium) to a two-part hands-on series: September 28 and October 12, 2026, 3:30–5:15 PM, McCourtney Hall B01. Items 1, 2, 6, and the new items 7–9 are all consequences of that change.

1. **Rehearse timing after the restructuring.** The 40-minute target no longer applies directly — see item 7; the storyboard gives a provisional act-level allocation. No live timed rehearsal was performed during editing. The September 14 pass cut the hooks slide but added two Act I slides (the inherited-project problem statement and the plan-review-launch sequence), so Act I is now the segment most likely to run long.
2. **Recheck time-sensitive claims before September 28.** Haiku 4.5 was confirmed current on September 14; recheck the whole model table before Part 1, and again before Part 2 on October 12. Product names, model availability and limits, Notre Dame approvals, and sponsor restrictions may change. Use [references](references.md). Antigravity's ND-plan exclusion was confirmed by Alex's September 11 account check and is recorded in references.md, but the slide that stated it was cut on September 14, so nothing in the deck depends on it now.
3. **Remove DRAFT when Alex requests it.** Retained on the title slide.
4. **Build the separate handout if desired.** The [plan](../handout/README.md) is updated to the current talk arc; no handout source has been created.
5. **Capture the desktop app screenshot for slide 12.** Slides 13 and 14 now use official Claude
   Code documentation screenshots, but **the documentation has no image of the desktop app**, so
   slide 12 still holds a placeholder. It has to come from Alex's own setup: the Code tab with the
   sidebar showing several sessions and one conversation open, since "supervise several tasks at
   once" is the slide's claim. Two constraints learned from the first attempt: crop the sidebar's
   project names out or rename them, because this repository is public and the sidebar showed
   private project titles; and keep the visible text to roughly 8-15 lines, since the image is
   9 cm wide on the slide.
6. **Re-time the talk.** The deck is 54 slides against a 40-minute target rehearsed at 52, and the
   weight has moved into Act I, which now runs 13 slides against an 8-minute budget. The three
   workspace slides (12-14) are the obvious candidates to re-merge if rehearsal runs long.
7. **Split the deck across the two parts.** The budget is settled — 55 presentation minutes total, about 28 in Part 1 and 27 in Part 2, with a 30-minute activity and a group recap in each (decision of 2026-09-21). That is *more* time than the 40 minutes the 54-slide deck was rehearsed against, so this is a split, not a cut. What remains is choosing the cut point and writing the two new opening/closing slides each part needs. Provisional: Prologue + Act I → Part 1 (setting up a project); Acts II–III + Epilogue → Part 2 (advanced features), dividing near slide 21.
8. **~~Recover the workshop starter~~ — resolved 2026-09-22.** Alex recovered it from his office desktop and pushed both repositories; the starter, `cstr_two_workshop_plan.md`, and the stub package are on `main` through commits `a948f58`, `da18fb1`, `e5225d5`, and `04279b1`. A Copilot-assisted merge, `09f15b3`, joined that line to the rescheduling work. A source-level review found nothing lost — CLAUDE.md rule 13 was edited rather than dropped, and the stubs are genuine stubs — but **the merged state has not been verified at runtime**, because the `cstr-workshop` conda environment does not exist on this machine. Running the five release checks against it is the first task in the Codex handoff.
9. **Send the announcement and state the prerequisites.** Participants need to create Claude and GitHub accounts, install the tools, and run `conda env create` *before* Part 1 — the environment build is the largest and most variable setup step and needs no instruction (private D8/D10). The announcement should also say the two parts are designed to be taken together.
