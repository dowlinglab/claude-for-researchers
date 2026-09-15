# Build plan: two AI-assisted research workshops using a CSTR

**Status:** approved design; implementation pending.

**Audience:** chemical engineering graduate students, postdocs, and faculty with
mixed experience in Python, Git, LaTeX, and coding agents.

**Format:** two workshops, 1.75 hours each. Both workshops use the same project
so that repository setup, computation, literature, writing, and auditing form one
continuous workflow.

## 1. Learning arc

### Workshop 1: notebook to reproducible project

Participants establish an agent-ready private repository, reproduce a supplied
nonisothermal CSTR notebook, record a numerical baseline, extract reusable Python
functions, add a reproduction script and regression tests, and review the work
through Git.

The central lesson is to capture evidence before restructuring code. The
activity is complete only when the refactored project reproduces the recorded
scientific result.

### Workshop 2: evidence to an audited report

Participants curate a small literature corpus, compare the implemented model and
computed behavior with those sources, draft a short LaTeX report, inventory its
claims, and audit each claim against either a source or a computational artifact.

The central lesson is that an agent can accelerate scientific writing without
becoming the authority for the science. A useful audit may return `CANNOT
VERIFY`, `NOT COMPARABLE`, or a narrower claim.

## 2. Repository architecture

### Public repository: `claude-for-researchers`

This repository is the source for student-facing material. Add the completed
case study under `resources/workshops/cstr/`:

```text
resources/workshops/cstr/
├── README.md
├── environment.yml
├── pyproject.toml
├── AGENTS.md.example
├── CLAUDE.md.example
├── activities/
│   ├── 01_notebook_to_reproducible_project.md
│   └── 02_evidence_linked_report.md
├── notebooks/
│   └── cstr_exploration.ipynb
├── data/
│   └── reactor_parameters.yml
├── literature/
│   ├── README.md
│   ├── source_manifest.csv
│   └── pdfs/.gitignore
├── src/cstr_workshop/__init__.py
├── scripts/
├── tests/
├── results/README.md
├── report/
│   ├── report.tex
│   ├── ref.bib
│   └── figures/.gitkeep
└── docs/
    ├── literature.md
    ├── claim_evidence_audit.md
    └── handoff.md
```

Students copy this starter into a new private repository. A later implementation
may also publish it as a dedicated GitHub template, but this repository remains
the canonical source for the seminar and workshop instructions.

### Private repository: `claude-for-researchers-private`

The sibling private repository is the instructor-only source:

```text
activity_answers/
├── STARTER_VERSION.md
├── 01_notebook_to_reproducible_project/
│   ├── expected_outcomes.md
│   ├── rubric.md
│   └── common_agent_failures.md
└── 02_evidence_linked_report/
    ├── reference_report.tex
    ├── claim_evidence_audit.md
    ├── rubric.md
    └── common_agent_failures.md
reference_implementation/
reference_results/
mutation_tests/
scripts/
```

`STARTER_VERSION.md` must record the public repository commit and release tag
that the answers solve. The private repository may use an `activity_answers/`
folder because the entire repository is access-controlled. The public repository
must never contain the answers, even temporarily or on a hidden branch.

## 3. Scientific case

Use a jacketed, nonisothermal continuous stirred-tank reactor with the
irreversible reaction

```text
A -> B
```

and first-order Arrhenius kinetics. At steady state, the model should include a
material balance and an energy balance with feed enthalpy, heat of reaction, and
heat exchange with coolant. Choose a parameter set that gives a useful nonlinear
response and, over part of the sweep, multiple steady states.

The example should support these questions:

- Does the code implement the stated balances, units, and sign conventions?
- Can the nominal result and parameter sweep be reproduced outside the notebook?
- Does the computation find distinct roots rather than returning the same root
  from several initial guesses?
- Does an S-shaped steady-state curve alone establish dynamic stability?
- Are comparisons with literature numerical, qualitative, or not comparable
  because the sources use different parameters or assumptions?

Use NumPy, SciPy, pandas, matplotlib, PyYAML, pytest, Jupyter, and a minimal LaTeX
toolchain. Avoid requiring Pyomo or a commercial solver in the core activity. An
optional Pyomo extension can be added after the main workshops work reliably.

## 4. Build the starter notebook

The notebook must execute successfully before students edit it. It should be
scientifically sound but structurally typical of exploratory work.

### Required notebook sections

1. State the reactor problem, assumptions, equations, and units.
2. Define nominal parameters in cells, initially using global variables.
3. Implement the Arrhenius rate and steady-state residuals.
4. Solve one nominal condition and report concentration, conversion,
   temperature, and residual norm.
5. Sweep one operating parameter, using multiple initial guesses and a stated
   tolerance to identify distinct roots.
6. Plot reactor temperature or conversion against the swept parameter.
7. Give a short, cautious initial interpretation that can be revisited during
   the literature and claim audit.

### Deliberate structural weaknesses

The starter may mix model, solver, sweep, plotting, and file handling in the
notebook. It may repeat calculations, assume output directories exist, print
results instead of saving a manifest, and embed tolerances in cells. It should
not contain a secret numerical defect merely to trick participants. Workshop 1
needs a trustworthy baseline.

### Reference outputs held privately

The instructor repository should contain:

- nominal concentration, conversion, temperature, and residual norm;
- the expected range and count of roots at selected sweep conditions;
- reference CSV and figure;
- explicit floating-point tolerances that work on supported platforms;
- expected runtime on an ordinary laptop;
- a perturbed implementation showing that the tests fail meaningfully.

Do not require exact image equality or unnecessarily precise floating-point
matches.

## 5. Workshop 1 activity specification

### Outcomes

By the end, a participant should have a private, versioned repository containing
a runnable environment, verified baseline, reusable model functions, a
reproduction script, regression tests, and a handoff document.

### Schedule

| Time | Work |
|---:|---|
| 10 min | Instructor framing and finished-workflow demonstration |
| 20 min | Create the private repository, environment, branch, and agent instructions |
| 15 min | Execute the notebook and capture baseline artifacts |
| 30 min | Extract model, solver, sweep, and plotting functions |
| 15 min | Add a reproduction script and numerical tests |
| 10 min | Review the diff or pull request and update the handoff |
| 5 min | Debrief and preparation for Workshop 2 |

### Student steps and gates

1. Create a private repository from the starter, clone it, and create a feature
   branch.
2. Build the documented environment and run the untouched notebook end to end.
3. Ask the agent to inspect the repository and draft `AGENTS.md` or `CLAUDE.md`.
   Review and shorten generic instructions before committing them.
4. Create baseline artifacts such as `baseline.json`, `steady_states.csv`, and a
   deterministic figure. Record parameters, software versions, residual norm,
   sweep definition, and creation command.
5. Extract reusable functions for kinetics, residuals, nonlinear solution,
   distinct-root detection, parameter sweeps, and plotting.
6. Create one documented command that regenerates the results without executing
   the notebook.
7. Add tests for the nominal residual, physical bounds, reference values,
   duplicate-root handling, and invalid inputs.
8. Review the actual diff, rerun the gates, commit a coherent change, and update
   `docs/handoff.md` with the verified Git state and resume point.

The activity instructions must give exact setup, execution, test, and cleanup
commands. Each command should be tested from a clean clone.

### Minimum completion and extensions

The minimum completion is a running environment, captured baseline, one
extracted model function, one passing numerical regression test, and a handoff.
Extensions may include full modularization, a command-line interface, stability
analysis, continuation methods, or a Pyomo implementation.

## 6. Literature preparation between workshops

Provide one legally redistributable or openly accessible anchor source. Ask each
participant to locate two more sources:

- one source for the governing equations, assumptions, or parameter values;
- one source for multiple steady states, ignition/extinction, thermal runaway,
  stability, or a related reactor application.

Suggested search phrases may include `nonisothermal CSTR multiple steady
states`, `CSTR ignition extinction diagram`, `exothermic CSTR thermal runaway`,
and `continuous stirred tank reactor bifurcation`.

Participants should store downloaded PDFs locally under the Git-ignored
`literature/pdfs/` directory unless redistribution rights clearly permit
committing them. They should version-control the source manifest, verified
BibTeX, and their own literature notes.

The source manifest should record the local filename, title, authors, year, DOI,
URL, source type, and verification status. Each literature note should state the
relevant equation or finding, its conditions, its exact location in the source,
and what the source cannot support.

## 7. Workshop 2 activity specification

### Outcomes

By the end, a participant should have a small verified literature corpus, a
two-page evidence-linked LaTeX report, a claim inventory, an audit table, a
revision visible in a diff, and a final handoff.

### Schedule

| Time | Work |
|---:|---|
| 10 min | Reconnect the computational baseline to the writing task |
| 15 min | Verify metadata and process the small literature corpus |
| 10 min | Compare equations, assumptions, and behavior with the sources |
| 20 min | Draft the short LaTeX report |
| 25 min | Inventory and audit every substantive claim |
| 15 min | Revise, compile, inspect the diff, and rerun computational gates |
| 10 min | Debrief and final handoff |

### Literature and comparison steps

1. Verify each source from the document itself and update `source_manifest.csv`,
   `ref.bib`, and `docs/literature.md`.
2. Audit the implemented balances, assumptions, units, and signs against the
   model source.
3. Compare the computed steady-state behavior with the behavior source.
4. Label the comparison as numerical, qualitative, not comparable, or
   insufficiently specified. Different parameters are not automatically a
   contradiction.
5. Record gaps that should drive the next literature search.

### Report specification

The LaTeX template should request a research question, model and assumptions,
computational method, principal result and figure, comparison with literature,
limitations, and reproducibility statement. Keep the target near two pages plus
references.

Every numerical claim should trace to a result artifact. Every figure should
name its generating script. Every literature claim should cite a source the
participant actually inspected.

### Claim audit

The audit table should include:

```text
Claim | Location | Required evidence | Actual evidence | Status | Revision
```

Allowed statuses are `VERIFIED`, `SUPPORTED WITH LIMITATIONS`, `MISMATCH`,
`CANNOT VERIFY`, and `NOT COMPARABLE`.

The activity should explicitly test tempting overclaims, especially that the
middle branch is dynamically unstable merely because an S-shaped steady-state
curve exists, or that results match a paper exactly when parameters differ.

### Fallback audit document

Provide `report/audit_fallback.tex` for participants who do not finish their own
draft. State that it contains several evidence problems without revealing their
locations. Seed five reviewable issues:

1. an unsupported stability claim;
2. an exact-agreement claim despite different parameters;
3. a numerical value inconsistent with the stored result;
4. a model assumption used in code but omitted from the report;
5. a citation that does not support the associated statement.

The private repository holds the annotated answer and reasoning.

## 8. Student-facing instruction design

Each activity file should contain:

- learning objectives and estimated time;
- a short scientific setup;
- prerequisites and exact environment commands;
- numbered phases with an artifact and a gate after each phase;
- copyable prompts that tell the agent to inspect before editing;
- explicit read/write boundaries;
- a minimum stopping point and optional extensions;
- common failure symptoms without giving away the solution;
- final verification commands;
- a handoff template.

The instructions should tell participants what evidence must exist, but allow
more than one reasonable module organization or report narrative.

## 9. Instructor answers and rubrics

Keep all answers in `claude-for-researchers-private/activity_answers/`. The
answers should define scientific invariants and acceptable outcomes rather than
requiring an exact source tree or identical prose.

Workshop 1 rubric categories:

- environment and untouched notebook reproduce;
- baseline exists before refactoring;
- model and scripts reproduce the baseline within tolerance;
- tests detect scientifically meaningful changes;
- Git history and handoff are reviewable.

Workshop 2 rubric categories:

- source identities and metadata are verified;
- literature notes distinguish evidence from interpretation;
- report claims trace to sources or generated artifacts;
- audit finds the seeded fallback issues;
- revisions narrow unsupported claims without inventing evidence;
- compiled output and handoff are complete.

## 10. Validate that the activities are answerable

Run four independent passes before release.

### Reference pass

Complete both activities from a fresh copy using only the student instructions.
Record actual time, unstated assumptions, missing dependencies, ambiguous
expected results, and every command that fails.

### Clean-agent pass

Start fresh Claude and Codex sessions with access only to the public starter.
Confirm that each can reproduce the notebook, preserve the baseline while
refactoring, create the required artifacts, avoid invented citations, identify
the fallback report's seeded problems, and leave a usable handoff. Different
valid code structures are acceptable.

### Novice-user pass

Ask someone with modest Python and Git experience to attempt the activities.
Focus on authentication, environment activation, LaTeX installation, branches,
generated-file locations, and the meaning of a claim audit.

### Mutation pass

Introduce one fault at a time and confirm that a test or audit catches it:

- reverse the heat-release sign;
- treat Celsius as Kelvin;
- change a parameter silently;
- use only one nonlinear-solver initial guess;
- alter a reported rounded value;
- claim stability without stability evidence;
- compare results with a source using incompatible conditions.

The workflow is not validated merely because its own reference implementation
passes. It should fail for meaningful scientific defects.

## 11. Implementation phases and commit gates

1. **Scaffold:** create the public starter and private instructor directories.
   Gate: links resolve and no answer files appear in the public tree.
2. **Scientific kernel:** establish equations, parameters, nominal solution, and
   sweep. Gate: private reference tests pass and results are physically
   reasonable.
3. **Starter notebook:** create the executable exploratory notebook. Gate: clean
   execution reproduces the private reference results.
4. **Workshop 1:** write instructions, reference implementation, rubric, and
   mutations. Gate: clean-agent and reference passes succeed.
5. **Literature packet:** select the open anchor source and create empty corpus
   templates. Gate: source rights and metadata are documented; no restricted PDF
   is committed.
6. **Workshop 2:** write the LaTeX template, fallback report, audit instructions,
   answers, and rubric. Gate: the fallback audit has exactly the intended
   evidence problems and compiles.
7. **Clean-room release audit:** run both workshops from a fresh public copy with
   no access to the private repository. Gate: all documented commands work,
   timings are plausible, and public Git history contains no answers.
8. **Release:** tag matching public and private states and record the public
   commit in the private `STARTER_VERSION.md`. Prepare commits in both
   repositories, but do not push without explicit approval.

