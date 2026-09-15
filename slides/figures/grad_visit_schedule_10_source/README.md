# Slide 2 schedule figure — how to remake it

Produces `../grad_visit_schedule_10.png`, the "Schedule by Visitors" plot on slide 2.

The figure is **real output from the public package**, not a mock-up. Keep it that way: if the
slide needs a different schedule, change the inputs here and rerun, rather than editing the image.

## Run it

```bash
pip install grad-visitor-scheduler
GVS_SRC=/path/to/grad-visit-scheduler/src python3 run.py
cp visitor_schedule_pooh10_4slot_rank1.png ../grad_visit_schedule_10.png
```

`GVS_SRC` should point at a checkout of
[dowlinglab/grad-visit-scheduler](https://github.com/dowlinglab/grad-visit-scheduler). The
released PyPI version is 0.5.0; the checkout carries the unreleased v0.5.1 auto-sized plotting
this figure relies on. Installing the package is still required — the package reads its own
version from the installed metadata.

## The settings that matter, and why

| Setting | Value | Why |
|---|---|---|
| Visitors | 10 Winnie-the-Pooh characters | Alex asked for "more characters" than the earlier six-visitor version, so the slide reads as a real recruitment day. Fictional visitors, real faculty. |
| Faculty | 6 CBE faculty, NSH and MCH | Real names and real buildings; the two buildings are what make the travel constraint visible. |
| Time slots | **4**, thirty minutes each, 9:00–11:00 | Requested 2026-09-14. Eight fifteen-minute slots made the blocks too narrow to read from the back of the room. |
| `movement.policy` | **`travel_time`**, NSH↔MCH lag of 1 slot | Requested 2026-09-14: enforce a free slot to change buildings. The constraint forbids being in NSH at slot *t* and MCH at *t+1*, so every building switch shows a visible gap. `policy: none` produced back-to-back cross-building meetings, which is not a schedule anyone could actually walk. |
| `min_faculty` | 2 | 4 slots × 6 faculty = 24 one-on-one meetings for 10 visitors. Requiring 3 meetings each needs 30 and is infeasible once the travel lag applies. |
| `max_group` | 1 | Keeps every meeting one-on-one so the plot stays easy to narrate. |
| `faculty_breaks` / `student_breaks` | 0 | `breaks: []` in `config.yaml` means there is no break window to enforce; a nonzero value raises "Must specify some break times!" |

## If you change the slot count again

Capacity is `slots × faculty`. Drop the slot count and `min_faculty` has to come down with it, or
the model is infeasible — `s.infeasibility_report()` (already wired into `run.py`) says which
constraint failed. Check the rendered figure afterward: the aspect ratio changes with the slot
count, and slide 2's column widths in `sections/00_open.tex` are tuned to it. Four slots gave a
roughly square figure, so the figure column is 0.50 and the timeline column 0.46; the earlier
eight-slot figure was wide and short and used 0.60 / 0.37.
