# Printed session handouts

Print **one two-page handout per participant per meeting**: US letter, actual
size (100%), double-sided, flip on the long edge. Each front is the part's
summary and save/handoff reference; each back is a numbered 45-minute activity.
The core instructions, prompts, checkpoints, and help route are printed. Participants do not need to navigate to the online session guide
to follow the normal route. The guide remains available for troubleshooting.

```bash
make -C handout           # part1.pdf and part2.pdf, exactly two pages each
make -C handout combined  # main.pdf, optional four-page packet of both handouts
```

Distribute `part1.pdf` for September 28 and `part2.pdf` for October 12. The old
`main.pdf` filename now means the combined packet, not a single two-page sheet.
All PDFs are generated and Git-ignored. `preamble.tex` contains shared formatting
and shared macros; `part1_front.tex`, `part1_back.tex`,
`part2_front.tex`, and `part2_back.tex` contain the editable content.

## Physical use

- Part 1 page 1: a concise lecture recap occupies the upper half; the lower
  half begins Activity 1 with the goal, a starter prompt, the mental model, and
  a vocabulary box. Page 2 has questions to ask Claude, conceptual checkpoints,
  troubleshooting prompts, and reflection. There is no command sequence.
- Part 2 page 1 is the audit summary, claim statuses, how to judge an audit, a
  Git and GitHub recap box, and reference links. Page 2 is the audit workflow,
  the optional Step 0, and a findings log. Both handouts are two pages on
  US letter paper, double-sided with a long-edge flip.
- A participant may reach only an early gate during the 45-minute block,
  particularly if installing Conda. Record the completed gate and next command;
  finish the same assignment between sessions.

After changes, rebuild and inspect both rendered pages for line wrapping, footer
clearance, and print legibility. No numerical answers or instructor reveals belong
in public handouts.
