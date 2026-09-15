# Current slide storyboard

Revised September 14, 2026 after Alex's annotated read-through of the September 11 deck and the
follow-up rounds in the same session (changes recorded in
[../notes/seminar_notes.md](../notes/seminar_notes.md)). The deck now contains **55 slides**
for a 40-minute talk, followed by 20 minutes of discussion. The title retains DRAFT, now set in
Notre Dame green rather than red.

Task 1 establishes the workspace. Tasks 2–3 build software and literature-grounded documents.
Tasks 4–6 audit, draft, and modernize. Hobbies are an unnumbered extension.

## Prologue: Tinker (slides 1–12)

1. Title and event details
2. Creating faculty-visitor schedules for graduate student recruitment
3. Jupyter Notebook → public Python package in ~10 hours
4. Takeaway message for today
5. Borrowed structure
6. Today: my lessons learned and recommended practices
7. Project context and agent actions are complementary
8. Desktop app: supervise several tasks at once
9. Editor extension: a tight edit-review loop
10. Terminal: scriptable, and the same engine underneath
11. Which model, and how much of it do you get
12. Everything today is on GitHub

## Act I: Understand (slides 13–22)

13. Act divider
14. An agent works on your file system
15. Use version control with (almost) every agentic project
16. Task 1 starts the way most projects start
17. Task 1: Set up an agent workspace and inherit a project
18. Branches isolate a change; pull requests invite review
19. Project instructions: CLAUDE.md and AGENTS.md
20. A concise instruction file routes the agent to evidence
21. Ask for help writing the task, not just the work
22. Then draft, review, and launch

## Act II: Build (slides 23–34)

23. Act divider
24. Task 2: Convert code from a published paper into a package
25. Task 2: The package conversion recipe
26. Task 2: Establish a reproducible baseline
27. Task 2: Decompose, generalize, then port
28. Task 3: Why LaTeX makes the agent useful
29. Overleaf and local edits meet through GitHub
30. Three repositories keep development, writing, and release separate
31. Task 3, step 1: Search, read, and search again
32. Task 3, step 2: Build a literature corpus an agent can use
33. Task 3, step 3: Edit the document against the curated corpus
34. Review the source diff and the manuscript diff

## Act III: Challenge (slides 35–46)

35. Act divider
36. Task 4: Audit a manuscript before submission
37. Task 4: Trace each claim to evidence
38. The DOI checker has two verification modes
39. Task 5: Draft a manuscript from the previous tasks
40. Task 5: Figures first, then outline, sections, and revision
41. Modernize my graduate elective
42. Four Goals... Starting One Week Before the First Lecture
43. Task 6: Coursepack sources and strategic gaps
44. Task 6: The course uses two repositories
45. Task 6: Each failure became a repeatable test
46. Task 6: Git and handoffs bridge tools and computers

## Epilogue: Trust (slides 47–55)

47. Act divider
48. Currently, Claude is approved for public data only at ND
49. Two important notes
50. The six tasks form one research workflow
51. This talk was built with the practices it recommends
52. You own every claim, whatever helped you make it
53. Hobbies: AI can amplify your curiosity
54. Hobbies: Create a textbook customized for you
55. Getting started later today

## Narrative and pacing

The opening software story shows a concrete payoff. The workspace question now gets one slide per
mode (8–10), each carrying a full-width screenshot with a single annotation and a shared
*Desktop app / Editor extension / Terminal* strip for orientation; the order runs easiest to most
sophisticated. Act I then moves **agent → file system → repository**: slide 14 establishes that an
agent works on real files, slide 15 argues good/better/best from a conversation to a file system to
a repository, and slide 16 states the problem the rest of Act I solves — inheriting a zip file and a
paper from a departed group member. Slides 21–22 close Act I on overnight work: the example prompt
asks for help writing the *task* for exactly that inherited-project scenario, then slide 22 covers
reviewing the planning document before launching a Codex Goal, `/goal`, or `/loop` run.

Act II moves from code packaging to literature and writing; the LaTeX case is made once (slide 26)
and immediately followed by the Overleaf/GitHub mechanics it implies. Act III reuses the same
evidence to audit and draft a manuscript, then the course-modernization capstone opens with its
motivation and the August 2026 commit calendar before showing the coursepack artifact it produced.
Trust, the talk's own provenance, and an immediately runnable first exercise close the talk.

Planning allocation, to validate in rehearsal: prologue 7 minutes; Understand 8; Build 10;
Challenge 10; Trust 5. **This allocation is now the deck's weakest assumption.** The hooks slide
was cut, but Act I gained two slides and the prologue gained two more when the workspace comparison
became three slides, so the deck is 55 rather than the 52 that was rehearsed. The prologue and
Act I are the segments most at risk. The three workspace slides are the obvious candidates to
re-merge if a timed rehearsal comes up short.
