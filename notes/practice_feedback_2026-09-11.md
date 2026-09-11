# Practice-talk feedback implemented — September 11, 2026

This dated record maps Alex's practice-talk notes to the revised deck. “Original slide” means the 52-slide practice version described by the supplied feedback, not the intermediate 50-slide working PDF. The six-task reorganization was already partly present in uncommitted files at the start of this pass and was preserved and completed.

## Task structure

| Act | Current tasks |
|---|---|
| Understand | 1. Set up an agent workspace and inherit a project |
| Build | 2. Convert published paper code into a package; 3. Create a literature-grounded report or proposal |
| Challenge | 4. Audit a manuscript; 5. Draft a manuscript from accumulated evidence; 6. Modernize a course |

Hobbies remain an unnumbered epilogue extension. The first slide of each task names the deliverable. Writing now runs continuously from literature/report preparation into audit and manuscript drafting.

## Feedback disposition

| Feedback | Implementation |
|---|---|
| Original 6: modernize a course | Task preview, task title, and recap use “Modernize.” |
| Original 7: account access and product distinctions | Slide 7 separates context from actions, acknowledges combined agent modes, and states Antigravity is not included in ND's Google plan. Alex's account check is preserved in the evidence folder and reference log. |
| Overnight/weekend agents, loops and goals | Slide 19 plus agent guide §12: completion evidence, phases, boundaries, budget, checkpoints, morning handoff, and differences among Goal, `/goal`, `/loop`, and scheduled work. Checked the course and feasibility-study plans read-only. |
| Original 16: stronger setup | Slide 15 merges Git setup and inheritance into Task 1; environment, agent instructions, permissions, and baseline reproduction are explicit. Expanded setup prompt. |
| Original 17: instruction files and helpers | Slides 17–18: comparison table, `/init` in both tools, Claude `/memory`, concise example, and pointers to evidence. “Startup briefing” replaces ambiguous “pre-context”; instructions remain part of context and are not enforced permissions. |
| Claude hooks | Slide 20 and agent guide §11 distinguish event-triggered checks from written guidance. |
| Original 18: expand literature workflow | Slides 26, 28–30: task goal, chatbot + Scholar search, iterative batches, verified corpus, and writing against sources. Details carried into literature guide. |
| Original 19 subtitle | Act II now says “Create reusable software and literature-grounded documents.” |
| Original 20–21: task goal and release | Task 2 keeps the clear goal and an explicit license/PyPI/GitHub Actions release step. |
| Original 24–25: remove bug detour and niche cleanup | Removed from the live sequence; package/release practices remain in companion guides. |
| Three repositories and file sizes | Slide 27 and LaTeX guide §1 distinguish private development, private Overleaf writing, and public release history. Roughly 10 MB is Alex's convention; vendor recommendations and limits are separately sourced. Large PDFs can live on Google Drive; text artifacts stay in Git. |
| Original 26: place writing together; explain LaTeX | Task 3 in Act II includes LaTeX, literature, Overleaf, and review. No jump back to an earlier act. |
| Branches and pull requests | Slide 16 uses a GitHub Desktop screenshot. Slide 31 shows the explicit Overleaf sync dialog; guide §3 covers incorporating coauthors' latest edits before merging. Branches do not eliminate conflicts. |
| Original 27: cut proposal-compliance slide | Removed; journal author-instruction compliance is a Task 4 audit question. Proposal-specific detail stays in the guide. |
| Original 28: reduce text, show diffs | Slide 32 pairs a GitHub Desktop screenshot with real compiled `latexdiff` output. The illustrative source pair is distributed as a reproducible example. |
| Original 31–32: prerequisites and relatable checks | Slide 34 names the setup/corpus prerequisites; slide 35 retains the percentage, mechanism, and missing-evidence examples. |
| Original 33: DOI capabilities | Slide 36 shows existing-DOI and missing-DOI paths. Labels match the implementation: Crossref title and first-author checks, candidate proposals, and a report; not automatic bibliography editing or claim validation. |
| Original 34–38: cut/rebuild | Removed the repeated incident and inherited-project slides. Slides 37–38 show manuscript drafting as accumulated tasks, then figures → outline → sections → revision. The case is generic; no student/topic is named. |
| Original 39–40: course history and goals | Jupyter replaces Sakai; `nbpages` and `JupyterBook` use the same typeface; website wording replaces sprint-rebuild wording. Four goals use sub-bullets and the requested week-before-class framing. |
| Original 44: show the actual coursepack | Slide 44 uses the existing source-reference and strategic-gap excerpts. The captions explicitly connect literature cross-references with active learning. |
| Original 50: larger hobby image | Enlarged image and centered columns retained from the in-progress feedback revision; layout reviewed with the rest of the deck. |
| More visuals and a hands-on invitation | GitHub Desktop branch/diff and Overleaf screenshots, actual manuscript diff, coursepack excerpts, and a runnable public-repo exercise on slide 52. |
| Direct Overleaf documentation links | Clickable slide footer plus distributed resources index and LaTeX guide links to the official sync documentation. |

## Editorial choices

- Keep the 40-minute talk focused on research outcomes. The added screenshots demonstrate an action the audience can recognize; a general gallery of desktop apps was not added.
- Keep the printed handout unbuilt, as before. Its plan now references the current talk arc; all detailed workflows remain online.
- Retain the submitted abstract and the requested DRAFT label.
- Preserve earlier planning rationale in Git and dated notes; current storyboard and resource indexes use the new numbering.

## Verification

The final build and visual inspection results are recorded in the corresponding September 11 entry of [the seminar log](seminar_notes.md). Source and screenshot provenance is in [references](references.md) and the [visual inventory](../slides/image_plan.md).
