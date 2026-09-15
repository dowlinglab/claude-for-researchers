# Current slide storyboard

Revised September 14, 2026 after Alex's annotated read-through of the September 11 deck
(marked-up PDF walked through in conversation; changes recorded in
[../notes/seminar_notes.md](../notes/seminar_notes.md)). The deck now contains **53 slides**
for a 40-minute talk, followed by 20 minutes of discussion. The title retains DRAFT, now set in
Notre Dame green rather than red.

Task 1 establishes the workspace. Tasks 2–3 build software and literature-grounded documents.
Tasks 4–6 audit, draft, and modernize. Hobbies are an unnumbered extension.

## Prologue: Tinker (slides 1–10)

1. Title and event details
2. Creating faculty-visitor schedules for graduate student recruitment
3. Jupyter Notebook → public Python package in ~10 hours
4. Takeaway message for today
5. Borrowed structure
6. Today: my lessons learned and recommended practices
7. Project context and agent actions are complementary
8. Desktop app, editor, or terminal: choose your workspace
9. Which model, and how much of it do you get
10. Everything today is on GitHub

## Act I: Understand (slides 11–20)

11. Act divider
12. An agent works on your file system
13. A repository beats a folder, and a folder beats a chat
14. Task 1 starts the way most projects start
15. Task 1: Set up an agent workspace and inherit a project
16. Branches isolate a change; pull requests invite review
17. Project instructions: CLAUDE.md and AGENTS.md
18. A concise instruction file routes the agent to evidence
19. Ask for help writing the goal, not just the work
20. Then draft, review, and launch

## Act II: Build (slides 21–32)

21. Act divider
22. Task 2: Convert code from a published paper into a package
23. Task 2: The package conversion recipe
24. Task 2: Establish a reproducible baseline
25. Task 2: Decompose, generalize, then port
26. Task 3: Why LaTeX makes the agent useful
27. Overleaf and local edits meet through GitHub
28. Three repositories keep development, writing, and release separate
29. Task 3, step 1: Search, read, and search again
30. Task 3, step 2: Build a literature corpus an agent can use
31. Task 3, step 3: Edit the document against the curated corpus
32. Review the source diff and the manuscript diff

## Act III: Challenge (slides 33–44)

33. Act divider
34. Task 4: Audit a manuscript before submission
35. Task 4: Trace each claim to evidence
36. The DOI checker has two verification modes
37. Task 5: Draft a manuscript from the previous tasks
38. Task 5: Figures first, then outline, sections, and revision
39. Modernize my graduate elective
40. Four Goals... Starting One Week Before the First Lecture
41. Task 6: Coursepack sources and strategic gaps
42. Task 6: The course uses two repositories
43. Task 6: Each failure became a repeatable test
44. Task 6: Git and handoffs bridge tools and computers

## Epilogue: Trust (slides 45–53)

45. Act divider
46. Currently, Claude is approved for public data only at ND
47. Two important notes
48. The six tasks form one research workflow
49. This talk was built with the practices it recommends
50. You own every claim, whatever helped you make it
51. Hobbies: AI can amplify your curiosity
52. Hobbies: Create a textbook customized for you
53. Getting started later today

## Narrative and pacing

The opening software story shows a concrete payoff. Act I now moves **agent → file system →
repository**: slide 12 establishes that an agent works on real files, slide 13 argues that a
versioned repository beats a bare folder, and slide 14 states the problem the rest of Act I
solves — inheriting a zip file and a paper from a departed group member. Slides 19–20 close Act I
on overnight work: first draft the *goal* with the agent's help, then review that planning
document yourself before launching a Codex Goal, `/goal`, or `/loop` run.

Act II moves from code packaging to literature and writing; the LaTeX case is made once (slide 26)
and immediately followed by the Overleaf/GitHub mechanics it implies. Act III reuses the same
evidence to audit and draft a manuscript, then the course-modernization capstone opens with its
motivation and the August 2026 commit calendar before showing the coursepack artifact it produced.
Trust, the talk's own provenance, and an immediately runnable first exercise close the talk.

Planning allocation, to validate in rehearsal: prologue 7 minutes; Understand 8; Build 10;
Challenge 10; Trust 5. The hooks slide was cut for time; the two new Act I slides (14, 20) and
the relocated talk-provenance slide (49) replace it, so the deck is one slide longer than the
practice-talk version and Act I is the segment most at risk of running over.
