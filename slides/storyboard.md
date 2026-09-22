# Current slide storyboard

The original 54-slide sequence below remains intact, split at the Task 3 opener.
Original numbers remain as stable editorial references. The shared sources build
**Part 1: 27 frames** and **Part 2: 31 frames**, including titles and closings.
DRAFT remains on both title slides.

| Build | Rendered frame mapping |
|---|---|
| Part 1, September 28 | Frames 1–26: original 1–26, with a session-specific title; frame 27: baseline closing |
| Part 2, October 12 | Frame 1: new title; frame 2: reconnect to the saved baseline; frames 3–30: original 27–54; frame 31: evidence/handoff closing |

Each session: **35 minutes presentation, 10 Q&A, 45 hands-on, 15 regroup**.
The original Act II source is split before Task 3 into code and literature files,
used by both the session builds and the combined build. Nothing is duplicated or
cut. The title's `\part` declaration records the session boundary without an
extra divider slide.

Part 1's activity establishes project instructions and a saved baseline. Part 2
resumes extraction, then audits the shared report. The first session's closing
reserves extraction for October 12 and frames the fortnight as experimentation
on participants' own research. The second session's reconnect and closing make
that continuity explicit.

Task 1 establishes the workspace. Tasks 2–3 build software and literature-grounded documents.
Tasks 4–6 audit, draft, and modernize. Hobbies are an unnumbered extension.

## Prologue: Tinker (slides 1–8)

1. Title and event details
2. Creating faculty-visitor schedules for graduate student recruitment
3. Jupyter Notebook → public Python package in ~10 hours
4. Takeaway message for today
5. Borrowed structure
6. Today: my lessons learned and recommended practices
7. Which model, and how much of it do you get
8. Everything today is on GitHub

## Act I: Understand (slides 9–21)

9. Act divider
10. An agent works on your file system
11. Use version control with (almost) every agentic project
12. Desktop app: supervise several tasks at once
13. Editor extension: a tight edit-review loop
14. Terminal: scriptable, and the same engine underneath
15. Task 1 starts the way most projects start
16. Task 1: Set up an agent workspace and inherit a project
17. Branches isolate a change; pull requests invite review
18. Project instructions: CLAUDE.md and AGENTS.md
19. A concise instruction file routes the agent to evidence
20. Ask for help writing the task, not just the work
21. Then draft, review, launch, and explore

## Act II: Build (slides 22–33)

22. Act divider
23. Task 2: Convert code from a published paper into a package
24. Task 2: The package conversion recipe
25. Task 2: Establish a reproducible baseline
26. Task 2: Decompose, generalize, then port
27. Task 3: Idea to a literature review, report, or proposal
28. Overleaf and local edits meet through GitHub
29. Three repositories keep development, writing, and release separate
30. Task 3, step 1: Search, read, and search again
31. Task 3, step 2: Build a literature corpus an agent can use
32. Task 3, step 3: Edit the document against the curated corpus
33. Review the source diff and the manuscript diff

## Act III: Challenge (slides 34–45)

34. Act divider
35. Task 4: Audit a manuscript before submission
36. Task 4: Trace each claim to evidence
37. The DOI checker has two verification modes
38. Task 5: Draft a manuscript from the previous tasks
39. Task 5: Figures first, then outline, sections, and revision
40. Modernize my graduate elective
41. Four Goals... Starting One Week Before the First Lecture
42. Task 6: Coursepack sources and strategic gaps
43. Task 6: The course uses two repositories
44. Task 6: Each failure became a repeatable test
45. Task 6: Git and handoffs bridge tools and computers

## Epilogue: Trust (slides 46–54)

46. Act divider
47. Currently, Claude is approved for public data only at ND
48. Two important notes
49. The six tasks form one research workflow
50. This talk was built with the practices it recommends
51. You own every claim, whatever helped you make it
52. Hobbies: AI can amplify your curiosity
53. Hobbies: Create a textbook customized for you
54. Getting started later today

## Narrative and pacing

The opening software story shows a concrete payoff. The prologue no longer surveys the tool
landscape; it goes straight from the story to the model table and the repository.

Act I builds the workspace in order. Slide 10 establishes that an agent works on real files, slide
11 argues good/better/best from a conversation to a file system to a repository, and **only then**
do slides 12–14 show the three places you can run an agent — desktop app, editor extension,
terminal — one per slide, each with a full-width screenshot, a single annotation, and a shared
strip for orientation, ordered easiest to most sophisticated. Putting them after version control
is deliberate: the question "where do I run this" is only worth answering once the files it will
touch are under version control. Slide 15 then states the problem the rest of Act I solves —
inheriting a zip file and a paper from a departed group member. Slides 20–21 close Act I on
overnight work: the example prompt asks for help writing the *task* for exactly that
inherited-project scenario, then slide 21 covers reviewing the planning document before launching a
Codex Goal, `/goal`, or `/loop` run.

Act II moves from code packaging to literature and writing. Slide 27 opens Task 3 and makes the
LaTeX case once, and the Overleaf/GitHub mechanics it implies follow immediately. Act III reuses the same
evidence to audit and draft a manuscript, then the course-modernization capstone opens with its
motivation and the August 2026 commit calendar before showing the coursepack artifact it produced.
Trust, the talk's own provenance, and an immediately runnable first exercise close the talk.

Rehearse against 35 presentation minutes in each part. The frame counts leave
about 78 seconds per Part 1 frame and 68 seconds per Part 2 frame on average;
these are pacing checks, not equal allocations to every slide. Reserve the full
45-minute hands-on block and 15-minute regroup. A live rehearsal remains open.
