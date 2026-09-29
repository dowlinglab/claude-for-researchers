# Your route through the two sessions

**Start here for both meetings.** Each meeting has **35 minutes of presentation, 10 of Q&A, 45 hands-on, and 15 regroup**. In both, Claude is your tutor and your auditor, and you are the one who checks. The pattern is **ask, inspect, verify, iterate**, not prompt, trust, done.

You do not need to memorize commands. When you need one, ask Claude to explain what it does and why before it runs, and how to undo it.

Ask for help after five minutes stuck on a tool. Pair with someone whose setup works if necessary. At minute 40, save where you are, even if unfinished. A partial checkpoint with honest missing checks is useful. An agent can inspect evidence. It cannot claim that you reviewed it.

## Session 1: turn a folder into a GitHub repository

Follow the [Activity 1 guide](01_notebook_to_reproducible_project.md). Download the inherited notebook, open its folder in Claude, and ask Claude to walk you through creating a clean GitHub repository, explaining each major step. The guide has a starter prompt, questions to ask, checkpoints, and troubleshooting prompts. It has no command sequence, on purpose.

## Between sessions

Use the two weeks to experiment on your own research. If you like, continue the "keep going" paths in the Activity 1 guide: run and audit the notebook, extract tested functions, or try one [extension](workshop1_extensions.md). None of it is homework.

## Session 2: audit an analysis against references

Follow the [Activity 2 guide](../../stats_audit/activity.md). You receive a colleague's notebook and write-up, and open statistics references. You ask Claude to audit them, verify a sample of what it reports, and judge the quality of the audit. There is an optional Step 0 for people who are comfortable with Git and Python; skip it freely.

## Optional second audit: the reactor report

A longer, chemical-engineering audit is available for practice after the session. It uses the same habits on a different kind of artifact: a short report about the reactor notebook, checked against results and a source.

Use `report/audit_fallback.tex` in this folder. Read the `.tex` file as text. A PDF is optional.

1. **Open fresh evidence.** Ask Claude to regenerate the notebook's results with the baseline helper (`scripts/baseline.py`) and to record where the evidence is saved. If you kept a baseline from Session 1, compare against it and preserve the earlier evidence rather than overwriting it. If the notebook was changed before any results were saved, say so, and use only evidence whose origin you can explain.
2. **Choose three claims** before asking for any verdict: one numerical, one citation-based, and one about model behavior. Copy each exact quotation and its section name into `docs/claim_evidence_audit.md`.
3. **Open the cited source.** For the citation claim, open [Woolf et al., section 11.6, Common Control Loops and Model for Temperature Control](https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Chemical_Process_Dynamics_and_Controls_(Woolf)/11:_Control_Architectures/11.06:_Common_control_loops_and_model_for_temperature_control), **CSTR Temperature Control → Exothermic Reactor Temperature Control Loops**, Figure 2. Record the passage you used. The supplied notes in `docs/literature.md` help you navigate; they are not proof that you opened the source. If access fails, record **notes only; primary-source check pending**.
4. **Check, then judge.**

   > Keep each original quotation exact. State the evidence needed, then open it and show its location. For every numerical value, show reported value, artifact value, unit conversion, rounded comparison, and result in a separate row. Locate CSV records by coolant temperature and branch index, not guessed line numbers. For a citation, record source opened or notes only, the actual passage, and what it supports. Assign a verdict only after these comparisons. Do not mark a compound claim VERIFIED if one part disagrees or remains unchecked. Keep proposed revisions separate from original quotations.

   Use this decision sequence: contradicted → **MISMATCH**; missing evidence → **CANNOT VERIFY**; comparison under different conditions → **NOT COMPARABLE**; only narrower wording supported → **SUPPORTED WITH LIMITATIONS**; all parts directly supported → **VERIFIED**. Open at least one evidence location yourself and record that confirmation separately from the agent's work.
5. **Revise one claim**, or explain why all three can stay. Preserve the original quotation. If you add an omitted assumption, identify it as an omission, not an original statement. Review the change to the source yourself.
6. **Save your work and leave a note.** Ask Claude to help you commit the audit and the report source with a message that says human review is pending, and to write a short handoff: the evidence you used and where it is, the checks you did personally, what is pending, and the next step. A commit preserves a draft. It does not certify human review.

Optionally build the report PDF with `scripts/build_report.py`. A successful build does not verify the report's claims. If you skip it, write **source-only; revised PDF not built**.

Before you stop, ask Claude to summarize the state of the repository, then check that the audit, the report source, and the handoff agree with each other. Replace any stale statements.

### Optional extension: extract one function

Only begin if you have a checked baseline. Extract only `arrhenius_rate_constant(T, params)` into `src/cstr_workshop/model.py`, reading parameters from the YAML file. Before editing, capture expected values from the original notebook function at chosen inputs. Compare the new function at those inputs; do not derive the expected values from the new code. Save a regression check, watch it fail after a small deliberate change, undo the change, and confirm it passes again. The [full activity file](02_evidence_linked_report.md) describes the longer report and literature workflow.
