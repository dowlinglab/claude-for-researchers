# Slide storyboard

Frame numbers refer to the rendered PDFs and change whenever frames are added or cut. This file is their only home, so update it when the decks change. Each session runs **35 minutes of presentation, 10 Q&A, 45 hands-on, and 15 regroup**.

Both decks are built from the same sources (`main.tex` and `sections/*.tex`). The title slide's `\part` declaration records the session without adding a divider frame. Task 1 establishes the workspace. Tasks 2 and 3 build software and literature-grounded documents. Tasks 4 to 6 audit, draft, and modernize. Hobbies are an unnumbered extension. Tasks 1 and 2 are Part 1, and Tasks 3 to 6 are Part 2. An act divider opens Acts I to III and the Epilogue, and a task divider (the six tasks, with the current one highlighted) opens each task.

## Part 1

| Frames | Section | Content |
|---|---|---|
| 1 | Title | Session title and event details |
| 2–8 | Prologue: Tinker | The faculty-visitor scheduler and the notebook-to-package story; the takeaway; borrowed structure; the roadmap; which model and how much of it you get; everything is on GitHub |
| 9–27 | Act I: Understand | An agent works on your file system; version control; Git and GitHub basics in five figures (local history versus the hosted copy, commits as save points, the repository root and `.gitignore`, nested repositories, and what belongs in GitHub versus cloud storage); desktop app, editor extension, and terminal; the Task 1 divider; Task 1 (inherit a project); branches and pull requests; `CLAUDE.md` and `AGENTS.md`; asking for help writing the task; drafting, reviewing, and launching overnight work |
| 28–33 | Act II: Build | The Task 2 divider; Task 2: convert code from a published paper into a package |
| 34 | Best practices | Best practices and the research tasks |
| 35–36 | Activity case | The reactor model and the notebook result |
| 37–39 | Activity 1 | Turn a folder into a GitHub repository; the tutor-style starter prompt; conceptual checkpoints and troubleshooting |
| 40 | Regroup | How far did you get? |
| 41 | Recap | Part 1 recap: ask, inspect, verify, iterate |

## Part 2

| Frames | Section | Content |
|---|---|---|
| 1–2 | Title and Part 1 recap | Session title; the Part 1 recap |
| 3–11 | Act II: Build (Task 3) | The act and Task 3 dividers; LaTeX; Overleaf and GitHub; three repositories; literature search, corpus, and editing; source and manuscript diffs |
| 12–26 | Act III: Challenge (Tasks 4–6) | The act divider, then a divider before each task; manuscript audit and claim tracing; the DOI checker; drafting a manuscript; the graduate elective and coursepack; failures as tests; handoffs |
| 27–35 | Epilogue: Trust | Data policy at Notre Dame; two notes; the six tasks as one workflow; how the talk was built; ownership of claims; hobbies; from workshop activities to research workflows |
| 36–41 | The analysis handed over | The folder (data, notebook, figures, write-up, references); the data; the notebook's text, code, and saved outputs; its sections; the write-up's structure; the two figures |
| 42–49 | Activity 2 | The scenario (a teammate hands you an analysis); the setup (data, questions, what to check against); getting the materials; the starter prompt; ask, inspect, verify, iterate; the four claim statuses; optional Step 0; judging the audit |
| 50 | Regroup | How good was the audit? |
| 51 | Feedback | The workshop feedback survey and the SAI Sparks tutorials, each with a QR code |

## Sequencing rationale

- **Version control comes before where to run an agent.** The question "desktop app, editor, or terminal?" is only worth answering once the files the agent touches are under version control. Five figures explain Git and GitHub in between: Activity 1 asks participants to build a repository, so they meet the root, commits, `.gitignore`, and pushing before it rather than in a Part 2 recap. The three interfaces follow, one per frame, ordered from easiest to most sophisticated.
- **Act I ends on overnight work.** The example prompt asks for help writing the *task* for the inherited-project scenario, and the next frame covers reviewing the planning document before launching a long-running run.
- **Task 3 makes the LaTeX case once,** and the Overleaf and GitHub mechanics it implies follow immediately. Act III reuses the same evidence to audit and draft a manuscript, and the course-modernization capstone opens with its motivation and the commit calendar before showing the coursepack it produced.
- **Trust and the talk's own provenance close the lecture,** and an immediately runnable exercise follows.
- **Pacing.** Rehearse each lecture against its 35 minutes. Frames are not allocated equal time. The facilitator run sheets in [`run_sheets/`](run_sheets/) mark where to stop talking and list candidate cuts.
- **The public regroup asks participants to show evidence before discussion.** Private instructor builds append the corresponding answer reveals to the same deck. Handouts are the primary in-room navigation aid: one two-sided sheet per part.
