# Workshop materials

The seminar is being expanded into two 1.75-hour workshops built around one
continuous nonisothermal CSTR case study:

1. convert an exploratory reactor notebook into a reproducible Python project;
2. use computational artifacts and a small literature corpus to draft and audit
   an evidence-linked LaTeX report.

The student-facing starter project is [`cstr/`](cstr/README.md): the executable
notebook, the environment, both activity instruction files, the literature and
LaTeX templates, and the fallback report used by the claim audit.

The detailed design and build sequence are in
[`cstr_two_workshop_plan.md`](cstr_two_workshop_plan.md). The handoff prompt for
building the materials with Claude Code is in
[`claude_build_goal.md`](claude_build_goal.md).

## Repository boundary

- **This repository, `claude-for-researchers`, is the student-facing public
  source.** It will hold the starter notebook, activity instructions, templates,
  and general workshop resources.
- **`claude-for-researchers-private` is the private instructor repository.** It
  will hold `activity_answers/`, reference implementations, reference results,
  rubrics, mutation tests, and teaching notes.
- Students will create their own private GitHub repositories from the released
  starter material. In the workshop instructions, call this a *private GitHub
  repository*, not a GitHub Project.

Answers must never be committed to this public repository, including on another
branch or in earlier history. An instruction telling an agent not to inspect an
accessible answer folder is not an access control.

