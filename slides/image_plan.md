# Visual assets in the session decks

Frame numbers below refer to the rendered Part 1 and Part 2 PDFs. The slides use
actual project outputs or interface screenshots. Unused intermediate figure
variants have been removed; original captures and regeneration sources remain.

| Deck, frame | Asset under `figures/` | Purpose |
|---|---|---|
| Part 1, 2 | `grad_visit_schedule_10.png` | Published scheduler output; inputs and regeneration instructions in [`grad_visit_schedule_10_source/`](figures/grad_visit_schedule_10_source/README.md) |
| Part 1, 3 | `grad_scheduler_screenshot_crop.png` | Scheduler documentation screenshot; the full capture is retained as its source |
| Part 1, 5 | `tal_logo.png` | This American Life structural reference |
| Part 1, 12–14 | `claude_desktop_projects_blurred.png`, `claude_vscode_extension.jpg`, `claude_terminal_agent_view.jpg` | Desktop, editor, and terminal interfaces; attribution appears on the slides |
| Part 1, 17 | `github_desktop_branch.png` | GitHub Desktop branch selection; [source](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop) |
| Part 1, 23 | `bits_for_gaps_graphical_abstract.png` | Published software case study |
| Part 1, 28–30 | `cstr_steady_state_locus.png`, `cstr_notebook_preview.png` | Reactor diagram is editable TikZ; the plot is original notebook output and the preview shows the downloadable notebook |
| Part 2, 3–7 | `figures/git_recap/*.tex` | Native TikZ diagrams for the Git and GitHub recap: local folder to GitHub, commit history, repository layout, and storage. See [`figures/git_recap/README.md`](figures/git_recap/README.md) |
| Part 2, 9 | `overleaf_github_sync.png` | Overleaf GitHub synchronization dialog; [source](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization) |
| Part 2, 14 | `github_desktop_diff.png`, `manuscript_diff.pdf` | Source diff and compiled manuscript diff; [GitHub source](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop) and [illustrative LaTeX source pair](../resources/examples/manuscript_revision/README.md) |
| Part 2, 22–23 | `august_2026_calendar.tex`, `coursepack_sources.png`, `coursepack_gap.png` | Course sprint calendar and coursepack excerpts; calendar generator in [`august_2026_calendar_source/`](figures/august_2026_calendar_source/make_calendar.py) |
| Part 2, 33–34 | `kitchen_organizer_telescope_shelf.jpeg`, `filter_families.pdf` | Hobby design and personalized textbook figure |

The Notre Dame marks come from the vendored theme under `theme/logos/`.
Screenshots retain their interface colors; native content uses the deck palette.
The Claude desktop screenshot blurs other project names while leaving the radio
textbook entry readable. The editable workflow diagrams and tables stay in the
LaTeX sources under `sections/`.

The August calendar shading and 1,452-commit total (1,084 private and 368 public,
August 17–31) were generated from dated Git logs in the course repositories.
August 17 marks the start of the sprint; August 24 marks the first lecture.
