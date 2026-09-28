# Workshop 1: inherit a notebook, build a research project

**Case.** A former student sends you a zip file containing an exploratory notebook and a parameter file for a cooled, nonisothermal continuous stirred-tank reactor (CSTR). The notebook appears to run, but there is no repository, environment, test suite, or record of which computation produced its figure. Make the work recoverable, audit it, extract reusable Python, and answer one new question. The notebook is a teaching model, not a measured reactor.

**Time.** The 45-minute in-room block starts all four steps. Keep the numbered sequence and save a checkpoint at minute 40. A clean Conda install and full extraction can take longer; continue the same steps between sessions. A partial checkpoint must say which gate is pending. Work in a private repository of your own. An AI coding agent may draft files and run checks; you decide whether the scientific claims are justified.

## 1. Create the repository and import the handoff (0–10 min)

Download [`workshop1_notebook.zip`](https://raw.githubusercontent.com/dowlinglab/claude-for-researchers/main/resources/workshops/cstr/workshop1_notebook.zip), unzip it, and put the enclosed `cstr-project/` folder where you keep research projects. Open a terminal **inside that folder**. It contains `notebooks/cstr_exploration.ipynb`, `data/reactor_parameters.yml`, and an empty `results/` directory. The notebook writes results relative to this folder.

```bash
cd /path/to/cstr-project
git init
git branch -M main
git status --short
git add README.md notebooks data results/.gitkeep
git commit -m "Import inherited reactor notebook"
```

Create an empty **private** GitHub repository named `cstr-project`; do not initialize it with another README. Copy its URL into the next command, then push:

```bash
git remote add origin YOUR-PRIVATE-REPOSITORY-URL
git push -u origin main
git switch -c workshop1
```

**Gate 1:** `git log -1 --oneline` shows the import, `git remote -v` points to *your* private repository, and `git status --short` is empty. If authentication fails, keep working locally and record that the push is pending. Never add an environment directory, tokens, or raw private data to Git.

## 2. Build the environment, run, and audit the notebook (10–22 min)

If `conda --version` fails, install [Miniconda for your operating system](https://docs.anaconda.com/miniconda/) and reopen the terminal. Ask your agent to inspect imports and draft an `environment.yml` with Python, NumPy, SciPy, pandas, matplotlib, JupyterLab, pytest, and any other packages actually needed. Compare its list with the notebook yourself. A working starting point is the [full starter's environment file](../environment.yml); remove its editable package install (`pip: - -e .`) because your new repository does not have a package yet. Add that install after Step 3.

```bash
conda env create -f environment.yml
conda activate cstr-workshop
python -c "import numpy, scipy, pandas, matplotlib; print('imports OK')"
jupyter lab
```

Start Jupyter from the project root. In the notebook, select the `cstr-workshop` kernel, **Restart Kernel and Run All Cells**, and confirm that the CSV and figure appear in `results/`. If Jupyter cannot see the kernel, use `conda run -n cstr-workshop jupyter lab` from the same directory. Record `python --version` and `conda list --export > results/conda-list.txt`.

If you use VS Code, open the **`cstr-project/` folder** as your workspace, not just the `.ipynb` file. Before running all cells, run `from pathlib import Path; print(Path.cwd()); print(Path('results').is_dir())` in a scratch cell. The working directory must be `cstr-project/` and the second value must be `True`. If either check is wrong, launch `jupyter lab` from a terminal in `cstr-project/` as shown above. If you see `OSError: Cannot save file into a non-existent directory: 'results'`, correct the working directory and rerun from a fresh kernel; the inline plot alone does not mean the CSV and PNG were saved.

**Audit before editing:** Read the opening equations, assumptions, units, and final limits. Compare every parameter typed in the notebook with `data/reactor_parameters.yml`. Check the sign of the exothermic heat term, absolute temperatures, solver convergence flag and residual norm, distinct-root tolerance, initial-guess range, coolant sweep spacing, and that a branch index is a rank at one condition rather than a continuous identity. Inspect a nominal row and a sweep row in the CSV. Look at the figure for false line connections. Record each check as **checked**, **question**, or **not yet checked**, with its source location. A rerun checks repeatability; it does not prove physical validity, root completeness, or stability.

Preserve the original source and results before the refactor. Commit a short `docs/audit.md`, `environment.yml`, and the unchanged notebook; commit the generated CSV, PNG, and environment list as baseline evidence. A notebook with new output cells is fine, but do not alter its equations or solver settings before this commit. Record the commit hash with `git rev-parse HEAD`.

**Gate 2:** a fresh kernel runs all cells, the scientific audit has named evidence and open questions, and the baseline commit precedes any refactor. If the notebook fails, preserve the error and fix the environment first.

## 3. Move the computation into tested Python modules (22–35 min)

Ask your agent to extract **one bounded function at a time** into `src/cstr_workshop/`: parameter loading and validation, kinetics and residuals (`model.py`); initial guesses and distinct steady-state solves (`solve.py`); parameter sweeps (`sweep.py`); figure creation (`plotting.py`). Keep the notebook as a readable exploration that **imports** the extracted functions after you have compared outputs. Add a minimal `pyproject.toml` so `python -m pip install -e .` installs the project in the active environment. Ask for NumPy-style docstrings: summary, Parameters with units, Returns, and Raises where relevant. Avoid a vague “document everything” prompt; inspect one signature and docstring yourself.

Write meaningful `pytest` tests before trusting the extraction. At minimum, test the parameter file loads, reaction rate increases with positive absolute temperature, residuals are small at every accepted state, concentration and conversion stay in physical bounds, distinct states are sorted and deduplicated, the sweep has one row per state, and an extracted nominal/sweep result agrees with the saved notebook CSV within a stated numerical tolerance. Also test a deliberately invalid parameter. Compare numeric values, not PNG bytes. Run:

```bash
python -m pip install -e .
python -m pytest -q
git diff --check
git status --short
```

**Gate 3:** tests pass and the extracted computation matches the saved baseline. Save the code, tests, and comparison in a new commit. If agreement fails, inspect the difference; never replace the pre-refactor baseline to make the test pass.

## 4. Extend the analysis in one direction (35–40 min; continue later)

Choose **one** question below. Keep the nominal parameters and original figure as controls. Give the agent a bounded task: state what varies, what stays fixed, the output table/figure, a test, and what claim it must *not* make. Put the new result under `results/extensions/` and record the command and environment. The [extension guide](workshop1_extensions.md) gives starting ranges, checks, and interpretation limits.

1. **Coolant resolution:** refine the grid near the change from one to three steady states. Report a *bracket* for each transition; do not claim an exact fold from a grid alone.
2. **Heat-transfer sensitivity:** vary `UA` while holding other parameters fixed. Show how the number of steady states at a fixed coolant temperature changes; label units and use the same root checks.
3. **Feed-temperature sensitivity:** vary `Tf` while holding other parameters fixed. Compare the temperature and conversion of all distinct states, not only the first solver root.
4. **Solver robustness:** widen and densify the initial-guess grid. Compare root sets and residuals. Agreement across grids strengthens the numerical check but does not prove that every root was found.

**Gate 4:** a script reruns your extension, a test or comparison checks it against the unchanged control, and a short note states what the result supports and what remains uncertain. Save the work even if incomplete.

## Stop, hand off, and regroup

At minute 40, run `git status --short` and save the actual state. In `docs/handoff.md`, record the baseline commit, completed gates, commands and working directory, checks you performed personally, pending questions, and the next exact command. Commit drafts with **human review pending** where needed. At regroup, show one audit finding, one comparison, and the extension you chose. Can a partner resume from your files with the chat closed?

**If stuck:** after five minutes, ask for help or pair with another participant. Record whose machine ran the computation. Continue from your own last verified gate instead of skipping evidence to reach Step 4.
