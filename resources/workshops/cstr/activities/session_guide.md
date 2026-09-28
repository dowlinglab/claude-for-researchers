# Your route through the two sessions

**Start here for both meetings.** This page is the complete in-room route. The
longer activity files are optional full workflows, not extra requirements today.
Each meeting has **35 minutes presentation, 10 Q&A, 45 hands-on, 15 regroup**.
Work in your own private copy of the starter. Before Session 1, create/activate
the environment in the starter README and run its setup checks. For Session 2,
open the anchor source below; LaTeX is optional for the core exercise.

Ask for help after five minutes stuck on a tool. Pair with someone whose setup
works if necessary, and record who ran the commands. At minute 40, save your
handoff even if unfinished. A partial checkpoint with honest missing checks is
useful. An agent can inspect evidence; it cannot claim that you reviewed it.

## Session 1 — Save evidence someone else can check

Today: complete three boxes — **instructions, saved baseline, restart check** —
and leave a short handoff. Stop there; package extraction is an extension.
A baseline is a saved record of what the original computation produced, kept so
that later changes can be compared against it.

### 1. Project instructions (about 10 minutes)

> **Prompt.** Inspect this project without changing it. Draft a short AGENTS.md
> (or CLAUDE.md for my tool) with the model's purpose, important files, commands,
> units, and rules for preserving evidence. Point to a notebook cell or parameter
> file for each project-specific statement. Do not implement the module stubs.

Open one named source and check one statement yourself. Remove generic advice.
Record agent inspection and human confirmation separately in the handoff. Save
and commit the instructions file you chose:

```bash
git add AGENTS.md  # use CLAUDE.md instead if that is your chosen file
git commit -m "Record project instructions and source checks"
```

### 2. Save the unchanged notebook's evidence (about 15 minutes)

**Unchanged** means no edits to notebook code, equations, parameters, or solver
settings. Execution counts and outputs may change; the helper preserves an
executed copy without editing your source notebook.

From the project root:

```bash
python scripts/baseline.py capture
```

If setup already produced a CSV or figure, inspect and move those existing files
to a separate archive directory first; capture refuses to overwrite any of its
four output files. The source guard also refuses changed notebook code or YAML.

This runs the notebook and saves `results/baseline.json`, `steady_states.csv`,
`steady_state_locus.png`, and `baseline.executed.ipynb`. It records the live
values, settings, software versions, source provenance, and command. It does not
fill the module stubs or ask the agent to reimplement the solver.

If no baseline exists and the source is still the untouched starter, capture
your first baseline now. If one exists, preserve it: capture refuses to replace
it. If you edited the model before the first capture, record that blocker; do
not call a new result a pre-change baseline. Use Session 2's audit route later.

Open the JSON and executed notebook/CSV. Check **one nominal record and one
sweep record**, locating CSV records by coolant temperature and branch index.
Check their units and the model assumptions in the notebook's introductory and
closing text. Inspect parameters against the YAML and notebook; inspect solver
settings, sweep definition and software/provenance fields. List each item as
checked or pending in the handoff. Printed values and CSV values may have
fewer digits than the live values: compare at the displayed precision rather
than inventing digits. Captured metadata is evidence to inspect, not automatic
human approval.

### 3. Restart, compare, and preserve (about 15 minutes)

Close the notebook. Reopen the project using files, without relying on the chat.
Run a fresh kernel and compare separate evidence with the saved baseline:

```bash
python scripts/baseline.py compare
```

If `results/recheck/` already exists, rename it to keep that evidence before
running another comparison. Open `results/recheck/comparison.json`. The rerun's artifacts are in
`results/recheck/`; the original baseline stays unchanged. Record the command
and result. Investigate any discrepancy; never replace the baseline to make a
comparison pass. A successful rerun checks repeatability, not model validity.

Review `git diff` and `git status`, then save the actual evidence, including the
figure and executed notebook (results are ignored by default):

```bash
git add -f results/baseline.json results/steady_states.csv results/steady_state_locus.png results/baseline.executed.ipynb
git add -f results/recheck/
git commit -m "Save notebook evidence and restart comparison"
git rev-parse HEAD
```

Put that evidence commit in `docs/handoff.md`, fill its five items, then:

```bash
git add docs/handoff.md
git commit -m "Record checks and next action in handoff"
```

**Finish checklist:** instructions checked against a named source; baseline,
CSV, figure and executed notebook preserved; fresh comparison inspected;
evidence committed; five-item handoff committed. If a check or human review is
pending, label the state **partial checkpoint**. If all are done, the Session 1
exercise is complete. This does not claim the scientific model is validated.

**Early finish:** exchange handoffs. Can a neighbor find the evidence and its
producing command using only your files? At regroup, share one checked statement
and one remaining limitation.

## Between sessions

Try an instructions file, baseline, or handoff on your own research. Bring one
observation. Finishing extraction is not homework. Open the supplied anchor
source before Session 2; additional papers are optional extension work.

## Session 2 — Check three claims and revise one

Today: choose **one numerical, one citation-based, and one model/behavior
claim** in `report/audit_fallback.tex`; check them and revise one. A complete
package, extra papers, and a new report are not required. Read the `.tex` as
text; a PDF is optional. A three-claim sample is not a whole-report audit.

### 1. Open evidence and select claims (about 10 minutes)

Read your handoff. If `results/recheck/` already exists from Session 1, rename
it (for example, `mv results/recheck results/session1-recheck`) to preserve it;
choose a different archive name if that name already exists. If a baseline
exists, run `python scripts/baseline.py compare`
and use the fresh CSV in `results/recheck/`, recording its path. If none exists
and the starter source is untouched, run `python scripts/baseline.py capture`
and use `results/steady_states.csv`. A first snapshot is allowed now; an old
snapshot must not be overwritten. If the notebook was modified before capture,
record that limitation and use only evidence whose provenance you can explain;
a source-only claim audit is still useful.

Paste three exact quotations and section names into
`docs/claim_evidence_audit.md` **before** requesting verdicts. Ask the agent for a
short candidate list if choosing is difficult. A full inventory is optional.

For the citation row, open [Woolf et al., section 11.6, Common Control Loops and
Model for Temperature Control](https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Chemical_Process_Dynamics_and_Controls_(Woolf)/11:_Control_Architectures/11.06:_Common_control_loops_and_model_for_temperature_control),
**CSTR Temperature Control → Exothermic Reactor Temperature Control Loops**,
Figure 2. Record the actual subsection/figure or passage you used. Supplied notes
in `docs/literature.md` help you navigate; they are not proof that you opened the
source. If access fails, record **notes only; primary-source check pending**.
Do not mark a publication claim VERIFIED from notes alone.

### 2. Check the three claims (about 20 minutes)

> **Prompt.** Keep each original quotation exact. State the evidence needed,
> then open it and show its location. For every numerical value, show reported
> value, artifact value, unit conversion, rounded comparison, and result in a
> separate row. Locate CSV records by coolant temperature and branch index,
> not guessed line numbers. For a citation, record source opened or notes only,
> the actual passage, and what it supports. Assign a verdict only after these
> comparisons. Do not mark a compound claim VERIFIED if one part disagrees or
> remains unchecked. Keep proposed revisions separate from original quotations.

Use this decision sequence: contradicted → **MISMATCH**; missing evidence →
**CANNOT VERIFY**; comparison under different conditions → **NOT COMPARABLE**;
only narrower wording supported → **SUPPORTED WITH LIMITATIONS**; all parts
directly supported → **VERIFIED**. Explain the evidence; a defensible reason
matters more than choosing between adjacent labels. Open at least one evidence
location yourself and record human confirmation separately from agent work.

### 3. Revise, save, and hand off (about 15 minutes)

Apply one reviewed revision, or explain why all three claims can stay. Preserve
the original quotation and proposed/applied revision in the audit. If you add
an omitted assumption, identify it as an omission, not an original statement.
Inspect the source diff. If human review is pending, the agent may save a
proposed revision or a clearly labeled draft; do not claim human approval.

For an optional PDF, copy the figure from the evidence directory you used and
build **after** editing the report:

```bash
cp results/steady_state_locus.png report/figures/  # use results/recheck/ if that was your evidence
cd report
latexmk -pdf audit_fallback.tex
cd ..
```

Record the source filename and build command/result. A build before the edit
does not check the revised source. If skipped or failed, write **source-only;
revised PDF not built**. Save the audit, report source and handoff; stage only
files actually changed, plus any generated evidence you relied on:

```bash
git diff
git status
git add docs/claim_evidence_audit.md report/audit_fallback.tex
# Preserve newly captured evidence if these files exist:
git add -f results/baseline.json results/steady_states.csv results/steady_state_locus.png results/baseline.executed.ipynb
# If you ran compare, also preserve its fresh evidence:
git add -f results/recheck/
git commit -m "Audit three selected claims and record revision"
git rev-parse HEAD
# Put this commit and the actual checks in the five-item handoff.
git add docs/handoff.md
git commit -m "Record audit handoff and remaining checks"
```

**Finish checklist:** three exact original claims; evidence and comparisons;
honest verdicts; one revision or justification; diff inspected; revised build
or explicit source-only status; saved handoff. Pending human checks mean a
partial checkpoint. At regroup, show one evidence location and explain exactly
what it establishes.

### Optional prepared-baseline extension: extract one function

Only begin if your baseline is checked and committed and its restart comparison
passes. This extension is not needed to complete Session 2. Keep time for the
three-claim audit; otherwise do the extension after the meeting.

Extract only `arrhenius_rate_constant(T, params)` into `src/cstr_workshop/model.py`.
Read parameters from YAML in calling/test code. Before editing, capture expected
values from the original notebook function at chosen inputs. Compare the new
function at those inputs; do not derive the expected values from the new code.
Save a regression check, observe it fail after a small deliberate local change,
undo that change, and confirm it passes again. Keep the source notebook and
baseline unchanged. Record the checks, diff, and any unfinished step. The full
activity files explain optional modularization and corpus/report extensions.
