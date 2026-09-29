# CSTR workshops

The two sessions use one scientific case: steady-state multiplicity in a cooled, nonisothermal CSTR. The values are a teaching set, not measurements of a reactor.

## Workshop 1: inherit the notebook

Start with the small [notebook handoff zip](workshop1_activity.zip). It contains only an exploratory notebook, a parameter file, and an empty `results/` directory. Download and unzip it, open the folder in Claude, and follow the [Activity 1 guide](activities/01_notebook_to_reproducible_project.md): ask Claude to walk you through turning the folder into a clean GitHub repository. Optional paths lead on to running and auditing the notebook, extracting tested Python functions, and one of the [four analysis extensions](activities/workshop1_extensions.md). The [session guide](activities/session_guide.md) points to the in-room route.

The zip is generated from the source notebook and parameter file with `python build_workshop1_handoff.py`; rerun that builder after changing either input. The existing full starter below is separate from the inherited notebook handoff.

## Optional: evidence-linked report

The in-room Part 2 activity is now the [statistics audit](../stats_audit/README.md). This reactor-report workflow is an optional take-home that uses the same audit habits on a different artifact. Use the [instructions](activities/02_evidence_linked_report.md) and the report, literature, and evidence folders in this full starter. This project also retains a longer optional extraction workflow and utilities for notebook baseline capture. They are support material, not the initial Workshop 1 handoff.

To run this full starter in its own private copy:

```bash
cp -R /path/to/claude-for-researchers/resources/workshops/cstr ~/cstr-full-starter
cd ~/cstr-full-starter
conda env create -f environment.yml
conda activate cstr-workshop
python scripts/run_notebook.py --check
```

A Workshop 2 PDF build additionally needs a LaTeX toolchain. The source-only audit can proceed without it.

## The science and limits

The steady-state material and energy balances may have more than one solution at a given coolant temperature. One nonlinear solve from one guess establishes only one root. The notebook searches from many starting points, sweeps coolant temperature, and plots the state locus. The calculation alone does not establish dynamic stability, exact fold locations, or agreement with a real reactor. Read the notebook's assumptions, units, sign conventions, and closing limits before making claims about its figure.

Instructor solutions, reference results, tolerances, and rubrics are held in the private sibling repository. Nothing in this public starter requires access to them.
