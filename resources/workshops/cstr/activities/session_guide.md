# Your route through the two sessions

Bring the same private CSTR project to both meetings. Each session lasts 105
minutes: **35 minutes presentation, 10 Q&A, 45 hands-on, 15 regroup**. Complete
[Activity 1 setup](01_notebook_to_reproducible_project.md#phase-0--setup-20-min)
before September 28. Check the LaTeX installation before October 12.

The longer activity files explain the full workflow. Their phase budgets are
reference estimates, not today's timetable. Use the bounded exercises below in
the room. Finishing the session exercise does not mean you have completed every
phase of the full workflow.

You may stop at any checkpoint and save a useful result. We expect different
amounts of progress. Most participants should have something left to do; write
the next action down before regrouping. Ask for help after five minutes stuck on
one tool problem. Pair with someone whose environment works if setup prevents
you from starting, and record who ran the commands.

## Session 1 — Can someone else check your baseline?

**Question:** What evidence would let your future self tell whether a refactor
changed the computation?

Keep the model and notebook unchanged throughout this session. Work through
Activity 1 Phases 1–2, then review the evidence you saved. Extraction begins in
Session 2, including for participants who finish early today.

### First checkpoint: one instruction you can defend

Ask the agent to inspect the project without edits, using Activity 1 Phase 1.
Check one project-specific statement against a named notebook cell or the
parameter file. Draft and review the short instructions file, remove generic
advice, and commit it. Use `git add AGENTS.md` if that is the file you chose.

**Show:** the instruction, its source, and the commit. You have practiced checking
an agent's account of a project even if you have not captured a baseline yet.

### Working checkpoint: the untouched result is saved

Run the notebook from the project root. Use Activity 1 Phase 2 to capture
`results/baseline.json` from the actual output. Preserve the CSV and figure.
Check one nominal-state record and one sweep record directly against the
notebook or CSV. Mark the remaining baseline fields as unchecked in your
handoff until you inspect them. Commit the evidence with a message that states
what you checked; a partial check is not the full Phase 2 gate.

**Show:** the producing command, two source locations you opened, and the saved
baseline. If capture is still in progress, save the draft and the next check.

### Complete session exercise: the evidence survives a cold restart

Finish checking the baseline fields listed in Phase 2, including parameters,
units, solver settings, and software versions. Close the notebook, then reopen
the project from your saved instructions. Confirm you can locate the producing
command, the committed evidence, and its provenance without reading the chat.
Run the untouched notebook again and compare its output to the saved baseline;
keep that baseline unchanged. Record any discrepancy instead of replacing it.

Review `git diff` and `git status`. Complete `docs/handoff.md` with the evidence
commit, commands actually run, unchecked items, and a next action. Commit the
handoff separately; its commit field identifies the evidence commit it describes.

**Done means:** project instructions, a checked baseline, and a handoff that
lets someone resume without the conversation. Full package extraction is next
session's work.

**If you finish early:** exchange handoffs with a neighbor. Try to locate their
baseline and generating command using only their files. Give one concrete
improvement, then apply that review to your own handoff.

### At minute 40, everyone saves a handoff

Save your current state, even if the baseline is incomplete. At minute 45 stop
for regroup. Discuss: Which statement from the agent did you check? What is now
recorded in files that would otherwise have lived only in the chat? What remains
unchecked?

## Between sessions

Experiment with one of these habits on your own research: a short instructions
file, a saved baseline, or a handoff. Bring one observation or difficulty.
Finishing CSTR extraction is not homework. If you want a little follow-up, finish
checking today's baseline or improve the handoff; incomplete work can also be
resumed at the beginning of Session 2.

For the audit, open the supplied anchor source and confirm you can access it
(see `literature/README.md`). Additional sources are optional preparation for the
longer Activity 2 workflow. Do not spend the fortnight trying to finish the full
literature review. Missing evidence is a legitimate audit result.

## Session 2 — Does a small change preserve the evidence?

**Question:** Can you check both a code change and a written claim without
letting the agent become the authority for either?

### Minutes 0–20: resume and extract one function

Read your handoff and reopen the saved baseline. If it is incomplete, complete
the necessary baseline checks first. Do not change the notebook or overwrite its
baseline to catch up. If you cannot reach that gate today, record the blocker
and inspect a partner's extraction while keeping attribution clear.

Use Activity 1 Phase 3 to migrate just `arrhenius_rate_constant(T, params)` into
your private copy of `src/cstr_workshop/model.py`. Leave other stubs for later.
Read parameters from the YAML file in your calling/test code; a complete
parameter-loader implementation is not needed for this small step.

> **Prompt.** Propose the smallest extraction of this one function from the
> notebook. Preserve the equation and units, pass parameters explicitly, and
> leave the notebook and baseline unchanged. Before editing, show how you will
> compare the extracted function against the original computation at inputs
> chosen from the notebook. Do not implement other stubs.

Review the plan, then the diff. Compare both implementations at the same inputs
and save one regression check with its expected value captured from the original
computation. Explain why the check would notice a changed function. Review a
small deliberate local change, observe the check fail, then undo that change
and rerun. Keep this experiment in your own private project.

**First checkpoint:** one importable function, a comparison you inspected, and
an honest record of the check. Partial extraction is a useful result.

**At minute 20, switch to the audit even if extraction is unfinished.** Save the
diff and next action. The unchanged notebook supplies the audit evidence, so
unfinished migration does not lock you out of the second half.

### Minutes 20–40: audit a small claim set

Use `report/audit_fallback.tex` as the shared report. If you do not have a working
reproduction command, generate current evidence with the unchanged notebook:

```bash
python scripts/run_notebook.py
cp results/steady_state_locus.png report/figures/
cd report
latexmk -pdf audit_fallback.tex
cd ..
```

If LaTeX fails, read the `.tex` directly and record that you did not verify the
rendered report. This keeps the evidence exercise accessible without pretending
the build passed. The notebook runner writes the CSV and figure, not the saved
`baseline.json`.

Inventory the report's claims using Activity 2 Phase 5. Then choose **three**:
one quantitative claim, one source-based claim, and one other claim you want to
check. Record the quotations and locations before asking the agent for verdicts.
These are your chosen samples, not a complete audit of the report.

Start with one row in `docs/claim_evidence_audit.md`. Ask the agent to identify evidence,
then open that evidence yourself. Record the file or source location, what it
actually establishes, and your verdict. `CANNOT VERIFY` is useful when it names
the missing evidence. A proposed citation alone does not verify a claim.

**Working checkpoint:** the extraction checkpoint plus one independently checked
audit row, or an explicit extraction blocker plus that row. Save the distinction.

**Complete session exercise:** check all three selected claims, revise one claim
that needs a narrower statement (or explain why each can stay), inspect the
diff, and save the handoff. Preserve both the original quotation and your
revision in the audit record. A three-claim sample never licenses a statement
that the whole report is verified.

### Minutes 40–45: save, then regroup

Record the code state, checks actually run, claims checked, evidence you could
not obtain, and the next action. Commit the reviewed changes and handoff. During
the 15-minute regroup, share one evidence location you opened and explain what
it supports. Compare reasoning rather than how many rows people completed.

**Follow-up:** finish the selected claim set and review the handoff. The rest of
Activity 1's modularization and Activity 2's full corpus/report workflow are
extensions. On your own project, repeat this small cycle on one function or one
claim before attempting a large rewrite.
