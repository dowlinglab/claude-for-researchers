# Activity 2: audit an analysis against trusted references

**The case.** A colleague sends you a Jupyter notebook and a short write-up of a statistical analysis of penguin body measurements, along with a few open statistics references. Before anyone builds on it, audit it. The materials contain deliberate problems of different kinds and difficulty. We do not say how many.

**The goal is not that Claude finds every problem.** The goal is to learn how to audit an analysis with an AI assistant, and how to judge the audit you get back. You are the reviewer of the audit as well as of the analysis.

Work in the pattern the whole workshop uses: **ask, inspect, verify, iterate.** Do not work in the pattern that goes prompt, trust, done.

**Time.** The in-room block is 45 minutes. You will probably finish the first pass and part of the verification. That is a good outcome. Save the checkpoint at minute 40 and continue afterward if you like.

## Get the materials

Download [`workshop2_activity.zip`](https://raw.githubusercontent.com/dowlinglab/claude-for-researchers/main/resources/workshops/stats_audit/workshop2_activity.zip) and unzip it. Its README lists the files. Then get at least one reference text into `references/pdfs/` by following `references/README.md`. Open the unzipped `audit-project/` folder in Claude. If Claude cannot find the reference files, tell it their exact names.

## Optional Step 0: make the changes easy to review

*Optional. If you are already comfortable with Git and Python.* If you are new to either, skip this step. You are not behind, and the audit works the same way without it.

**Why it exists.** A notebook is convenient for interactive work, but it is awkward for an AI agent to edit and for a person to review. A notebook file is one large block of JSON that holds code, saved outputs, and images together. When Claude edits a cell and reruns it, the diff shows the code with escaped quotation marks, every changed output, and any figure as one enormous line of image data. Changing one number in a plotting cell changed a line of about 35,000 characters in our own test. Plain-text Python files produce diffs that show only the code that changed. That friction is a lesson in itself.

The right representation depends on the task. For substantial agentic editing and review, plain-text source files often make changes easier to understand and to audit. For exploration, a notebook is often the better tool. This is a trade-off, not a rule.

**What to do, in this order:**

1. If the folder is not yet a Git repository, make it one. Establish a clean baseline commit **before** anything changes, so you can always see what changed later.
2. Refactor so that the substantive analysis code lives in readable Python files, and the notebook becomes a thin interface that calls them. Check that the notebook's behavior and outputs are preserved.
3. Commit the refactor separately from everything else.
4. Then start the audit.

Doing the baseline first and the refactor second means every later change shows against a known starting point. Doing the refactor before the audit means the corrections Claude proposes land in files whose diffs you can actually read.

A starter prompt:

> Before we audit this analysis, I want to make it easier to review changes. First inspect the project and establish a clean Git baseline. Then help me refactor the notebook so that the substantive analysis lives in readable Python files while preserving the notebook's behavior and outputs. Explain the proposed structure before changing anything. Keep the refactor separate from any statistical corrections so that I can review the changes independently.

If you want to see the problem first, ask Claude to change one small thing in the notebook, rerun it, and show you the Git diff. Then do the same in a Python file.

Give Step 0 at most 15 minutes. If it is unfinished, start the audit anyway. The audit is the point of the session.

## The audit, step by step

This is a thinking workflow, not a script. Change the wording to fit what you see.

### 1. Inspect before changing anything

Read the write-up and skim the notebook yourself first, for two minutes. Then ask Claude to read everything and tell you what it found, without editing any file.

> Read `writeup.md`, the notebook, and the data documentation. Do not change any files. Summarize what analysis was done and what the write-up concludes.

### 2. Ask Claude to list the claims

An audit needs a list of things to check. Ask for the substantive statistical and scientific claims, each with its location in the write-up or the notebook.

> List every substantive claim in the write-up: numbers, comparisons, interpretations, and conclusions. For each, give its location and say which cell or file it depends on.

Read the list. Is anything you noticed missing?

### 3. Audit the claims against the references

> For each claim, check it against the reference texts in `references/pdfs/`. Classify it as supported, questionable, incorrect, or insufficient evidence. Cite the specific chapter, section, or principle you relied on and say what it states. Keep what the reference says separate from your own reasoning.

Insist on the four categories. "Insufficient evidence" is a legitimate answer. A claim that Claude cannot verify from these files is different from a claim it has shown to be wrong.

### 4. Audit the code as well as the prose

> Read the code, not just the write-up. Check that what the code does matches what the write-up says it does, and that every number in the write-up matches the notebook's output.

If your setup allows it, let Claude rerun the notebook and compare the new outputs with the saved ones.

### 5. Ask for proposed corrections, and their reasons

> For each problem you found, explain why it is a problem and propose a correction. Do not apply anything yet.

### 6. Verify a sample of the findings yourself

This is the step that most separates auditing from accepting. Choose at least three findings, including one you are inclined to believe and one that surprised you. For each:

- open the reference at the location Claude cited and read what it says;
- find the notebook cell or write-up sentence Claude points to;
- recompute the number, or rerun the check, yourself.

Record what you did. "Claude said so" is not verification.

### 7. Iterate

If the first pass missed things or seemed shallow, change the prompt or the context rather than accepting it. Some ideas:

- ask Claude to recompute every number in the write-up independently and report mismatches;
- ask it to list the assumptions behind each test and say whether the data support them;
- ask which conclusions go beyond what these data can show;
- ask what it could not check from these files, and why;
- ask for a second pass by a fresh conversation that has not seen the first result, and compare.

Notice which change helped. That is part of what you are here to learn.

### 8. Revise, then review the changes

Apply the corrections you accept, either to a copy of the write-up and notebook or on a Git branch. Then look at the changes yourself rather than taking Claude's summary of them. A good correction changes as little as it can and explains why.

## Judge the audit

Keep a short log as you go, and write down which Claude model and setup you used (for example, whether it could run code and open the reference files). How much to trust an audit depends on that. Use a table like the one on your handout, with these columns:

| Finding | What Claude cited | How I checked it | Real problem? | Reference cited correctly? |
|---|---|---|---|---|

At the end, look at the whole log and ask:

- Which problems did Claude find? Which did it miss, as far as you can tell?
- Did it report anything that was not a problem? How did you find out?
- Were its citations to the references accurate? Did any section say something different from what Claude claimed?
- Were its explanations convincing? Could you check them independently?
- What additional prompt or context improved the audit?
- What kinds of problems was Claude good at finding? What kinds were harder?

At regroup, we compare your logs with what is actually in the materials. Expect the result to be uneven. A useful audit that misses some problems and needs your verification is the normal outcome, and knowing where it tends to fail is what makes the tool safe to use.

## Checkpoints

- [ ] I read the write-up and skimmed the notebook before asking Claude to.
- [ ] Claude listed the claims, and I checked the list for gaps.
- [ ] Every finding has a status, a reference location, and a proposed correction.
- [ ] I personally verified at least three findings, and I wrote down how.
- [ ] I know at least one thing Claude got wrong, missed, or could not check.
- [ ] I reviewed the changes myself before accepting them.
- [ ] My log is filled in.

## Stuck?

Ask Claude about the tool, not only about the statistics:

> I do not understand the last step. Explain it without assuming I know Git.

> Before you change anything, tell me how I could undo it if something goes wrong.

> You cited a section. Quote the sentence you are relying on and tell me where to find it.

If you are stuck on the setup for five minutes, ask for help or pair up with someone whose setup works.
