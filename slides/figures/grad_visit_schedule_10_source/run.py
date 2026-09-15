"""Regenerate the slide 2 visitor schedule.

Needs the `grad-visitor-scheduler` package. Install it for the metadata, and set
GVS_SRC to a checkout of https://github.com/dowlinglab/grad-visit-scheduler to
pick up the unreleased auto-sized plotting used for this figure:

    pip install grad-visitor-scheduler
    GVS_SRC=/path/to/grad-visit-scheduler/src python3 run.py

Copy the resulting PNG over ../grad_visit_schedule_10.png.
"""

import os
import pathlib
import sys

src = os.environ.get("GVS_SRC")
if src:
    sys.path.insert(0, str(pathlib.Path(src).resolve()))

from grad_visit_scheduler import Solver, scheduler_from_configs  # noqa: E402

s = scheduler_from_configs("faculty.yaml", "config.yaml", "visitors.csv", solver=Solver.HIGHS)

# max_group=1 keeps every meeting one-on-one. The four 30-minute slots and the
# NSH/MCH travel lag in config.yaml make 3 meetings per visitor infeasible, so
# min_faculty is 2.
sol = s.schedule_visitors(
    group_penalty=0.2,
    min_visitors=0,
    max_visitors=6,
    min_faculty=2,
    max_group=1,
    faculty_breaks=0,
    student_breaks=0,
    tee=False,
    run_name="pooh10_4slot",
)

if sol is None:
    print(s.infeasibility_report())
else:
    sol.plot_visitor_schedule(save_files=True, show_solution_rank=False)
    print("OK")
