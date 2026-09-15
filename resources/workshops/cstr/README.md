# CSTR workshop starter

Starter project for two 1.75-hour hands-on workshops built around one scientific
case: steady-state multiplicity in a jacketed nonisothermal CSTR.

1. **[Activity 1](activities/01_notebook_to_reproducible_project.md)** — turn an
   exploratory notebook into a reproducible project, without losing the result.
2. **[Activity 2](activities/02_evidence_linked_report.md)** — turn computational
   artifacts and a small literature corpus into a report whose every claim traces
   to evidence.

Copy this directory into a **new private GitHub repository** of your own and
work there. The instructions assume you did.

## Quick start

```bash
cp -R path/to/cstr ~/cstr-project && cd ~/cstr-project
conda env create -f environment.yml
conda activate cstr-workshop

python -c "import cstr_workshop; print('ok')"
pytest tests
python scripts/run_notebook.py --check
```

All three should succeed before Activity 1 begins. Activity 2 additionally needs
a LaTeX toolchain:

```bash
latexmk -v
cd report && latexmk -pdf report.tex && latexmk -C && cd ..
```

## The scientific case

A jacketed CSTR runs the irreversible exothermic reaction `A -> B` with
first-order Arrhenius kinetics. At steady state a material balance and an energy
balance hold simultaneously:

```
0 = q (C_Af - C_A) - V k(T) C_A
0 = q rho Cp (T_f - T) + (-dH_rxn) V k(T) C_A - UA (T - T_c)
```

Heat generation rises exponentially with temperature; heat removal rises
linearly. The two can therefore balance at more than one temperature for the
same operating condition — so a single solver call from a single starting point
returns *a* steady state and tells you nothing about how many exist.

That is the scientific hook, and it is also the methodological one. Most of what
both workshops teach is a response to the same problem: a computed result that
looks completely convincing and is incomplete.

All temperatures are absolute (K). The parameters are a teaching set, not a
measured reactor — see [`data/reactor_parameters.yml`](data/reactor_parameters.yml).

## Layout

```
cstr/
├── activities/          the two activity instruction files
├── notebooks/           cstr_exploration.ipynb -- the starting point
├── data/                reactor_parameters.yml
├── src/cstr_workshop/   empty at the start; you fill it in Activity 1
├── scripts/             run_notebook.py; you add reproduce.py
├── tests/               environment smoke test; you add regression tests
├── results/             generated artifacts (git-ignored by default)
├── literature/          source manifest, notes rules, git-ignored pdfs/
├── report/              report.tex, ref.bib, audit_fallback.tex
├── docs/                literature notes, claim audit, handoff templates
├── environment.yml      the environment
├── pyproject.toml       packaging
└── AGENTS.md.example    example agent instructions (CLAUDE.md.example is identical)
```

The notebook is deliberately typical exploratory work: globals, repeated code,
tolerances written inline, paths relative to the working directory, and no
manifest recording what produced what. It is not, however, wrong — there is no
hidden numerical defect. Activity 1 depends on the baseline it produces being
trustworthy.

## What you need

| | |
|---|---|
| **Both activities** | Git, a GitHub account, conda or mamba, an AI coding agent you can run against a local directory |
| **Activity 2 also** | A LaTeX toolchain (`latexmk`, `pdflatex`, `bibtex`) — TeX Live, MacTeX/BasicTeX, or MiKTeX |

Python, the scientific stack, and Jupyter all come from `environment.yml`.

## For instructors

Solutions, reference results, tolerances, rubrics, and mutation tests are **not**
in this repository. They are in the private instructor repository,
`claude-for-researchers-private`. This is an access boundary, not a convention:
an activity is only demonstrably answerable if it can be completed from this
tree alone.

Design rationale and the build plan are in `resources/workshops/cstr_two_workshop_plan.md`
in the `claude-for-researchers` repository — one directory above this starter.
It is referenced by path rather than by link because you are expected to copy
this directory on its own, which would break a relative link pointing outside it.
