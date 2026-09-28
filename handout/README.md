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

- Part 1 page 1: a concise lecture recap occupies the upper half; the lower
  half begins the notebook handoff with Git and Conda. Page 2 covers the audit,
  Python extraction and tests, four extension choices, and the handoff.
- Part 2 retains its report audit instructions. Both handouts are two pages on
  US letter paper, double-sided with a long-edge flip.
- A participant may reach only an early gate during the 45-minute block,
  particularly if installing Conda. Record the completed gate and next command;
  finish the same assignment between sessions.

After changes, rebuild and inspect both rendered pages for line wrapping, footer
clearance, and print legibility. No numerical answers or instructor reveals belong
in public handouts.
