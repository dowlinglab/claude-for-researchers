# Visual assets in the session decks

The slides use actual project outputs or interface screenshots. Each asset below is under `figures/` and is used by the section file named in the second column. Frame numbers change often, so [`storyboard.md`](storyboard.md) owns them.

| Asset | Section file | Purpose |
|---|---|---|
| `grad_visit_schedule_10.png` | `00_open` | Published scheduler output; inputs and regeneration instructions in [`grad_visit_schedule_10_source/`](figures/grad_visit_schedule_10_source/README.md) |
| `grad_scheduler_screenshot_crop.png` | `00_open` | Scheduler documentation screenshot |
| `tal_logo.png` | `00b_roadmap` | This American Life structural reference |
| `claude_desktop_projects_blurred.png`, `claude_vscode_extension.jpg`, `claude_terminal_agent_view.jpg` | `02_act1_understand` | Desktop, editor, and terminal interfaces; attribution appears on the slides |
| `github_desktop_branch.png` | `02_act1_understand` | GitHub Desktop branch selection; [source](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop) |
| `bits_for_gaps_graphical_abstract.png` | `03_act2_build` | Published software case study |
| `overleaf_github_sync.png` | `03b_act2_literature` | Overleaf GitHub synchronization dialog; [source](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization) |
| `github_desktop_diff.png`, `manuscript_diff.pdf` | `03b_act2_literature` | Source diff and compiled manuscript diff; [GitHub source](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop) and [illustrative LaTeX source pair](../resources/examples/manuscript_revision/README.md) |
| `august_2026_calendar.tex`, `coursepack_sources.png`, `coursepack_gap.png` | `04_act3_challenge` | Course sprint calendar and coursepack excerpts; calendar generator in [`august_2026_calendar_source/`](figures/august_2026_calendar_source/make_calendar.py) |
| `kitchen_organizer_telescope_shelf.jpeg`, `filter_families.pdf` | `05_epilogue` | Hobby design and personalized textbook figure |
| `cstr_notebook_preview.png` | `09_part1_activity` | The downloadable notebook |
| `cstr_steady_state_locus.png` | `09a_part1_case` | Original notebook output. The reactor diagram on the same slide is editable TikZ |
| `git_recap/*.tex` | `07b_part2_git_recap` | Native TikZ diagrams for the Git and GitHub recap: local folder to GitHub, commit history, repository layout, and storage. See [`figures/git_recap/README.md`](figures/git_recap/README.md) |

The Notre Dame marks come from the vendored theme under `theme/logos/`. Screenshots keep their interface colors, and native content uses the deck palette. The Claude desktop screenshot blurs other project names while leaving the radio textbook entry readable. The editable workflow diagrams and tables stay in the LaTeX sources under `sections/`.

The August calendar shading and 1,452-commit total (1,084 private and 368 public, August 17 to 31) were generated from dated Git logs in the course repositories. August 17 marks the start of the sprint; August 24 marks the first lecture.
