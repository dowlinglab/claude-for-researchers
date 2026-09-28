# Your route through the two sessions

**Start here for both meetings.** Follow the linked Workshop 1 activity for the
four-gate notebook handoff; Workshop 2 uses the report in the separate full starter.
Each meeting has **35 minutes presentation, 10 Q&A, 45 hands-on, 15 regroup**.
Work in your own private repository. Build the Workshop 1 environment from the
notebook imports. For Session 2, open the anchor source below; LaTeX is optional
for the core exercise.

Ask for help after five minutes stuck on a tool. Pair with someone whose setup
works if necessary, and record who ran the commands. At minute 40, save your
handoff even if unfinished. A partial checkpoint with honest missing checks is
useful. An agent can inspect evidence; it cannot claim that you reviewed it.
**Save and commit draft work even while human review is pending.** A local commit
preserves work; it is not approval, publication, or a claim that the exercise is
complete. Label it “draft — human review pending.”

## Session 1 — Inherit the notebook and build a project

Use the [four-step Workshop 1 activity](01_notebook_to_reproducible_project.md) and its [extension choices](workshop1_extensions.md). Download the small notebook handoff, initialize your own private Git repository, create a Conda environment, run and audit the notebook, extract tested Python functions, and choose one extension. The printed handout contains the in-room route. A 45-minute block may leave later gates pending; save a precise checkpoint at minute 40 and continue between sessions.

## Between sessions

Finish the extraction and one extension in your private repository. Bring the baseline commit, a test result, and one open scientific question to Session 2. The separate full CSTR starter in this public repository supplies the report and literature materials for the second workshop.

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
proposed revision or a clearly labeled draft edit. Record **applied draft;
human review pending** if source text changed, or **proposal only; not applied**
if it did not. In both cases commit the evidence, audit and handoff now. Do not
wait for approval to preserve local work or claim approval that did not occur.

For an optional PDF, run this from the project root **after** editing the report.
The helper copies the figure and runs LaTeX in the correct directory:

```bash
python scripts/build_report.py --evidence results
# Use --evidence results/recheck if that is the evidence you audited.
python scripts/build_report.py --check
```

The receipt in `report/build_receipt.json` identifies the source inputs, figure,
PDF and build command. `--check` detects later changes or failed builds; an old
PDF alone is not proof of success. After any source edit, rebuild or explicitly
record source-only status. A successful build does not verify report claims.

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
# Run the next line only if results/recheck exists:
git add -f results/recheck/
# If you built the report, preserve its figure and receipt too:
git add -f report/figures/steady_state_locus.png report/build_receipt.json
git commit -m "Audit three selected claims and record revision"
git rev-parse HEAD
# Put this commit and the actual checks in the five-item handoff.
git add docs/handoff.md
git commit -m "Record audit handoff and remaining checks"
```

Run the [final consistency check](#final-consistency-check-both-sessions) below.

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

## Final consistency check (both sessions)

Do this after the last edit/build/commit, including for a partial checkpoint:

```bash
git status --short
git log -2 --oneline
git show --stat --oneline HEAD
```

- Open the audit and handoff together. Does applied/proposal status match the
  actual source diff? Does build status match the latest receipt (or say skipped)?
  Replace stale “not built,” “no commit,” or resolved-warning statements.
- Open each cited source location and check the quoted excerpt. Keep one row per
  numeric value, including values grouped in one sentence.
- Confirm the named evidence commit contains the cited files, and the later
  handoff commit contains `docs/handoff.md`. Empty `git status` alone does not
  prove ignored evidence was committed; inspect the evidence commit's file list
  with `git show --stat EVIDENCE_HASH` (replace the placeholder).
- If files remain uncommitted, save them with the commands above or name the
  actual blocker. Pending human review is a status to preserve, not a blocker.
  If you correct these documents, commit the correction and check status again.

Write the next action from the state that now exists. Do not ask the reader to
repeat a completed build or commit. Keep human confirmation pending until it
actually happens.
