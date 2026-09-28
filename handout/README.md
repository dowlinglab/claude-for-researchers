# Printed session handouts

Print **one two-page handout per participant per meeting**: US letter, actual
size (100%), double-sided, flip on the long edge. Each front is the part's
summary and save/handoff reference; each back is a numbered 45-minute activity.
The core instructions, prompts, commands, stopping checklist, and help route
are printed. Participants do not need to navigate to the online session guide
to follow the normal route. The guide remains available for troubleshooting.

```bash
make -C handout           # part1.pdf and part2.pdf, exactly two pages each
make -C handout combined  # main.pdf, optional four-page packet of both handouts
```

Distribute `part1.pdf` for September 28 and `part2.pdf` for October 12. The old
`main.pdf` filename now means the combined packet, not a single two-page sheet.
All PDFs are generated and Git-ignored. `preamble.tex` contains shared formatting
and checkpoint instructions; `part1_front.tex`, `part1_back.tex`,
`part2_front.tex`, and `part2_back.tex` contain the editable content.

## Physical use

- Part 1 front: project memory, the baseline cycle, reactor context, file map,
  and evidence/handoff saving commands. Back: inspect, capture, restart, save.
- Part 2 front: the audit cycle, verdict definitions, evidence/source directions,
  and saving commands. Back: open evidence, select three claims, check, revise, save.
- Both backs have visible time checkpoints, a five-minute help rule, a minute-40
  stopping rule, and writing space for a next action or question.
- Keep human confirmation separate from agent work. A draft or partial checkpoint
  is a valid saved state; completing the exercise does not validate the model.

The existing Notre Dame navy/gold and 11-point body text are retained. After
changes, rebuild, confirm the separate PDFs still have two pages, and render
all four pages to inspect line wrapping, footer clearance, and print legibility.
No numerical answers or instructor reveals belong in these handouts.
