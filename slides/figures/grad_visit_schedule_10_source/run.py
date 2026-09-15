import sys, pathlib
sys.path.insert(0, str(pathlib.Path("../gvs/src").resolve()))
from grad_visit_scheduler import scheduler_from_configs, Solver

s = scheduler_from_configs("faculty.yaml", "config.yaml", "visitors.csv", solver=Solver.HIGHS)
sol = s.schedule_visitors(group_penalty=0.2, min_visitors=0, max_visitors=8,
                          min_faculty=3, max_group=1, faculty_breaks=0,
                          student_breaks=0, tee=False, run_name="pooh10")
if sol is None:
    print(s.infeasibility_report())
else:
    sol.plot_visitor_schedule(save_files=True, show_solution_rank=False)
    print("OK")
