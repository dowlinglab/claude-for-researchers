# Workshop activities

Each part of the seminar has one hands-on activity, a 45-minute block in the room:

| | Activity | Folder |
|---|---|---|
| **Part 1** | Use Claude as a tutor to turn an inherited reactor notebook folder into a clean GitHub repository, with optional paths on to a reproducible Python project (a nonisothermal CSTR case study) | [`cstr/`](cstr/README.md) |
| **Part 2** | Audit a colleague's statistical analysis of the public Palmer Penguins data against open statistics references, and judge the quality of the audit | [`stats_audit/`](stats_audit/README.md) |

The reactor case also supports a longer, optional evidence-linked report audit for working on your own after Part 1. The [session guide](cstr/activities/session_guide.md) explains how the two sessions and the between-session working time fit together.

The downloads for both activities are attached to each [release](https://github.com/dowlinglab/claude-for-researchers/releases), so an activity matches the slides it accompanies.

## Repository boundary

- **This repository, `claude-for-researchers`, is the student-facing public source.** It holds the starter material, activity instructions, templates, and general workshop resources.
- **`claude-for-researchers-private` is the private instructor repository.** It holds the answer keys, reference implementations, reference results, rubrics, mutation tests, and teaching notes.
- Participants create their own private GitHub repositories from the downloaded activity material. In the instructions, call this a *private GitHub repository*, not a GitHub Project.

Answers are never committed to this public repository, including on another branch or in earlier history. An instruction telling an agent not to inspect an accessible answer folder is not an access control.
