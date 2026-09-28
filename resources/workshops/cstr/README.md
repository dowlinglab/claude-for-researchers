# CSTR workshops

The two sessions use one scientific case: steady-state multiplicity in a cooled, nonisothermal CSTR. The values are a teaching set, not measurements of a reactor.

## Workshop 1: inherit the notebook

Start with the small [notebook handoff zip](workshop1_notebook.zip). It contains only an exploratory notebook, a parameter file, and an empty `results/` directory. Download and unzip it, then follow the [four-step assignment](activities/01_notebook_to_reproducible_project.md): create your own private Git repository; set up Conda, run and audit the notebook; extract and test Python functions with NumPy-style docstrings; and complete one of the [four analysis extensions](activities/workshop1_extensions.md). The [session guide](activities/session_guide.md) points to the in-room route. Save a truthful checkpoint at minute 40 and continue unfinished gates between sessions.

The zip is generated from the source notebook and parameter file with `python build_workshop1_handoff.py`; rerun that builder after changing either input. The existing full starter below is separate from the inherited notebook handoff.

## Workshop 2: evidence-linked report

Use the [Activity 2 instructions](activities/02_evidence_linked_report.md) and the report, literature, and evidence folders in this full starter. This project also retains a longer optional extraction workflow and utilities for notebook baseline capture. They are support material, not the initial Workshop 1 handoff.

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
