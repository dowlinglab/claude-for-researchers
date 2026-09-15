# Current slide storyboard

Revised September 14, 2026 after Alex's annotated read-through of the September 11 deck and the
follow-up rounds in the same session (changes recorded in
[../notes/seminar_notes.md](../notes/seminar_notes.md)). The deck now contains **54 slides**
for a 40-minute talk, followed by 20 minutes of discussion. The title retains DRAFT, now set in
Notre Dame green rather than red.

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
21. Then draft, review, and launch

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

Planning allocation, to validate in rehearsal: **this allocation is now the deck's weakest
assumption.** The original split was prologue 7 minutes; Understand 8; Build 10; Challenge 10;
Trust 5, rehearsed against 52 slides. Since then the hooks slide and the tool-ecosystem slide were
cut while Act I gained five slides, so the deck is 54 and the weight has moved decisively into
Act I, which now runs 13 slides against a budget of 8 minutes. The prologue, at 8 slides, has
slack. **Re-time before assuming this fits**; the three workspace slides are the obvious candidates
to re-merge if it does not.
