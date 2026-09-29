# Inherited reactor notebook

A former student left this notebook and a parameter file. Your job is to make a project another researcher can run, inspect, test, and extend. Start in the folder containing this README; the notebook writes to `results/` relative to that folder. In VS Code, open this whole `cstr-project/` folder as the workspace before running the notebook. In a notebook cell, run `from pathlib import Path; print(Path.cwd()); print(Path('results').is_dir())`; it should show this folder and `True`. If it does not, launch `jupyter lab` from a terminal in `cstr-project/`.

Read `notebooks/cstr_exploration.ipynb` before editing it. It describes a teaching model of a cooled, nonisothermal CSTR. The values in `data/reactor_parameters.yml` are a second copy of the parameters, useful for an audit; the notebook currently types them in directly. No environment, package, or tests are supplied in this handoff.

Follow the [Activity 1 guide](https://github.com/dowlinglab/claude-for-researchers/blob/main/resources/workshops/cstr/activities/01_notebook_to_reproducible_project.md). Keep the notebook and this parameter file as the original evidence until you have recorded and checked a baseline.
