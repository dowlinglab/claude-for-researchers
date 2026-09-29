# Design rationale

Why the seminar is built the way it is. History lives in Git; this file keeps only the reasons that still govern decisions. The slide sequence is in [`slides/storyboard.md`](../slides/storyboard.md), the narrative in [`outline.md`](../outline.md), and open items in [`open_questions.md`](open_questions.md).

## Thesis and tone

The seminar's claim is that the most useful AI work in research goes beyond chatbot Q&A and sits inside a deliberate, reproducible, auditable workflow whose state lives in files and Git.

- Never claim a step *requires* AI. Logging, testing, and auditing predate GenAI. Frame AI as making them easier, faster, or more consistent.
- Keep recommendations model-independent where possible. Claude is the hook, not the subject.
- Return ownership to the researcher. The talk ends on responsibility, not on a capability demo.
- Avoid inflated language ("revolutionize") in slides, handouts, and resources.
- Nothing project-identifying. Examples are generalized, with no former group members named and no framing of a project as "in bad shape".

## Structure

A five-part narrative (prologue, three acts, epilogue) organized around six research tasks, not around vendor products. A product tour would reward whichever vendor is trendiest and force constant context-switching. Organizing by task means every section answers "where does this fit in a project I already have?".

- Tasks 1 and 2 are Part 1. Tasks 3 to 6 are Part 2. The split falls at the start of Task 3.
- Related workflows are taught once and named as variations: the manuscript audit modes are one prompt file, and the literature folder and DOI checker are one "bibliography hygiene" mention.
- Mechanics that a slide walkthrough cannot teach (LaTeX, Overleaf, style-guide derivation) live in the practice guides, not on slides.

## Format

Two sessions, two weeks apart, each 105 minutes: 35 presentation, 10 Q&A, 45 hands-on, 15 regroup. The gap is working time. Participants experiment on their own research between sessions, and anyone who did not finish Activity 1 can finish it then.

Design each activity so that a participant with some coding experience and occasional Git use gets roughly halfway in the hands-on block, a power user may finish, and a novice completes a useful first fifth. These are targets to pilot, not measured completion rates. Progress means artifacts a participant can inspect and resume.

Generous hands-on time is the strongest part of the design. Do not fill it with lecture.

## Activities

- **Teach the mental model, not a command recipe.** Part 1 showed that a public step-by-step recipe confuses beginners, prescribes one route among many, and lets an agent reproduce the expected solution instead of reasoning. Activity 1 gives an objective, a mental model, starter prompts, questions to ask, and conceptual checkpoints.
- **Claude as tutor.** The live demonstration that worked had Claude explain each step and stop for questions. The handouts reproduce that.
- **Activity 2 audits a public dataset.** A general-purpose statistics analysis (Palmer Penguins, CC0) replaced the reactor domain so the exercise suits any audience. The objective is calibration, not detection: how to audit systematically and how to judge the audit. Participants record which model and setup they used, because in agent tests the model changed the audit a great deal, and a weaker model marked wrong claims as verified.
- **Step 0 is optional.** Notebooks are awkward for agentic editing and for review. Baseline commit, then refactor into plain-text files, then audit. The right representation depends on the task, so this is not a rule.
- **Answers stay private.** The instructor repository holds keys and solutions. An instruction telling an agent not to read an accessible answer folder is not an access control.

## Resources

- **Tool-agnostic by default.** Vendor conventions (`CLAUDE.md`, `AGENTS.md`, settings) drift, so the durable layer is tool-neutral markdown, and tool-specific mechanics sit in clearly marked sections.
- **Docs go stale.** Use a living, dated, and superseded taxonomy, cap living documents at three or four per project, and determine status from evidence. `resources/scripts/check_docs.py` checks links, staleness, and supersession banners.
- **Written instructions are advisory.** Anything that must hold needs a mechanical check. A test that leaves a recurring problem fixed is worth more than a reminder.
- **Phase-matched verification.** Tests help when consolidating and refactoring and obstruct discovery, so more tests is not universally better.
- **Style guides are worked examples.** A file named for one author teaches students to adopt that author's voice, so the guide is an example plus "derive your own".

## Slide layout

- A `list` or `center` environment as the first element of a frame carries its own `\topsep`, which reads as padding and can push the last line onto the corner logo. LaTeX never warns about it. `slides/check_layout.py` measures the gaps from the rendered PDF, and a human should look at what it flags.
- Screenshots and figures crop to about 8 to 10 lines of legible text, capped at 12.
- Commit placeholders instead of leaving a slide empty, so the layout settles early.
