# Activity 1: turn an inherited folder into a GitHub repository

**The case.** A former student sends you a zip file containing an exploratory notebook and a parameter file for a cooled, nonisothermal continuous stirred-tank reactor (CSTR). The notebook appears to run, but there is no repository, no record of the environment, and no way to tell which computation produced its figure. The notebook is a teaching model, not a measured reactor.

**The goal.** End with a well-organized repository for this folder, on your computer and on GitHub, that you can explain to someone else. You do not need to know Git. Claude will teach you as it works.

**How to work.** You are collaborating with Claude, not following a tutorial. The pattern is **ask, inspect, verify, iterate**:

- *Ask* Claude to explain each major step before it does it.
- *Inspect* what happened: read what Claude says it did, and look at the result.
- *Verify* the parts you can check yourself. Ask Claude how.
- *Iterate*: ask again when something is unclear or does not look right.

There is no single correct sequence of commands. Claude can generate whichever commands are needed. Your job is to understand what each step is for, and to decide whether it is a good idea.

**Time.** The in-room block is 45 minutes. Most people finish the first goal and start the next. Save a note about where you stopped at minute 40 (see the end of this page).

## Get started

1. Download [`workshop1_notebook.zip`](https://raw.githubusercontent.com/dowlinglab/claude-for-researchers/main/resources/workshops/cstr/workshop1_notebook.zip) and unzip it. Put the enclosed `cstr-project/` folder where you keep research projects.
2. Open that folder in Claude (desktop app, editor extension, or terminal). Open the folder itself, not a single file inside it.
3. Have a GitHub account ready. GitHub Desktop is optional; Claude can guide either route.

## A starter prompt

Change the wording to fit you.

> I want to turn this folder into a clean GitHub repository. I am new to Git and GitHub. Please walk me through the process step by step using good practices. Start by inspecting the folder. Before each major step, explain what it accomplishes, and stop periodically so I can inspect what happened and ask questions.

## The mental model

Three things, in a chain:

1. **A folder of files.** What you have now.
2. **A repository on your computer.** The same folder, plus a history of saved checkpoints that Git keeps.
3. **A copy on GitHub.** A second copy of that repository on the web, for backup and sharing.

You are building that chain, one explained step at a time. The order in which Claude does things can vary. What matters is that you understand why each step happens.

## Questions worth asking Claude

Use these when you are stuck, or before you agree to something. They are examples, not a sequence.

- "Before changing anything, inspect this folder and tell me what you think should and should not be tracked in Git."
- "Explain what `.gitignore` is and recommend what this project should ignore."
- "Explain what a commit represents in plain language."
- "Show me how to check what Git thinks has changed before we commit anything."
- "I don't understand the last command. Explain it without assuming I know Git."
- "Before making this change, tell me how I could undo it if something goes wrong."

## You are done when

- [ ] I know which folder is the repository root.
- [ ] Git is set up in that folder, and not inside another repository.
- [ ] I understand broadly which files Git is tracking.
- [ ] Large or inappropriate files are left out where appropriate. That includes environments, credentials, and private data.
- [ ] I have a first commit that records the original files as received, before any change.
- [ ] I can say how my local repository differs from GitHub.
- [ ] The repository is connected to GitHub, if I am ready for that.
- [ ] I can ask Claude to explain the current state of the repository, and the answer makes sense to me.

If the push to GitHub fails because of authentication, a local repository with the push pending is an acceptable checkpoint. Write down that it is pending.

## Words you will hear

| Word | Meaning |
|---|---|
| Repository | A project folder plus the history Git keeps about it |
| Root | The folder that contains the repository's `.git` folder. Git tracks the project relative to it |
| Commit | A labeled checkpoint of the project, with a message. Not the same as saving a file |
| `.gitignore` | A list of files Git should skip, such as caches, environments, and regenerable output |
| GitHub | A website that hosts a copy of your repository |
| Push, pull | Send your commits to GitHub, or bring changes from GitHub back |

## If something goes wrong

- "The push failed. Explain the error and my options."
- "I think I opened the wrong folder. How do I check where the repository root is?"
- "Show me what changed since the last commit, and whether anything unexpected is included."
- "Undo the last step and tell me exactly what state we are back to."
- If Claude stops to ask permission at every step, tell it how much to do at once: "Do the next three steps, then stop and summarize."
- If Claude did many things at once, ask: "Explain each thing you just did, in order, and how I would undo each one."

If you have been stuck on a tool for five minutes, ask for help or pair up with someone whose setup works.

## Keep going

If you finish early, or between sessions, stay in the same conversation and ask Claude to help with the next things, described here by purpose rather than by step:

- **Run and audit the notebook.** Ask for a recorded environment and a fresh run from the project folder. Before changing anything, read the equations, assumptions, and units; compare the parameters typed in the notebook with `data/reactor_parameters.yml`; check the sign of the heat term, absolute temperatures, the solver's convergence flag and residuals, and how distinct steady states are identified; and look at the figure for false connections. A rerun checks repeatability. It does not prove physical validity, root completeness, or stability.
- **Save the starting point before refactoring.** Ask Claude to explain why the original notebook and its results should be committed before the code changes, and how you would later compare the new code with them.
- **Turn the code into tested Python functions.** One bounded function at a time, with tests you understand, and a comparison against the saved results.
- **Extend the analysis in one direction.** See the [extension guide](workshop1_extensions.md) for starting ranges and limits.

At each of these, keep asking Claude to explain, and keep checking its work.

## At minute 40, leave a note

Ask Claude to help you write a short note in the repository, such as `docs/handoff.md`, that records where you are: what is done, what you checked yourself, what is pending, and the next step. Someone else, or you in two weeks, should be able to resume from your files with the chat closed.

## Reflect

- What did Claude explain that you would not have known to ask?
- Where did you accept a step you did not understand? What would you ask now?
- What did you verify yourself?
