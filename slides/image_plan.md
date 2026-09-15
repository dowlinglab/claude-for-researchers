# Current visual inventory

Revised September 14, 2026 after Alex's annotated read-through and the follow-up rounds. Slide
numbers follow the current 55-slide [storyboard](storyboard.md). Earlier plans remain in Git history. Earlier capture plans remain in Git history through `2c55c74`. Screenshots are evidence and interface examples, not decorative images.

## Assets used in the 55-slide deck

| Slide | Asset under `figures/` | Purpose and source |
|---:|---|---|
| 2 | `grad_visit_schedule_10.png` | Real package output: ten fictional visitors, four thirty-minute slots, and an enforced free slot for changing buildings. Regenerated September 14 with `grad-visitor-scheduler`. Inputs, run command, and the reasoning behind every solver setting are in [`grad_visit_schedule_10_source/README.md`](figures/grad_visit_schedule_10_source/README.md). Faculty names and buildings are real; visitors are not |
| 3 | `grad_scheduler_screenshot_crop.png` | Public documentation; existing asset |
| 5 | `tal_logo.png` | This American Life structural reference; existing asset |
| 18 | `github_desktop_branch.png` | Branch selection in GitHub Desktop; [official documentation](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop), [original image](https://docs.github.com/assets/cb-38142/images/help/desktop/select-branch-from-dropdown.png), accessed September 11 |
| 24 | `bits_for_gaps_graphical_abstract.png` | Published software case study; existing asset |
| 29 | `overleaf_github_sync.png` | Explicit push/pull dialog; [Overleaf GitHub synchronization documentation](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization), accessed September 11. Exported the rendered page's `Github_modal.png` asset; converted AVIF to PNG without changing its content. |
| 34 | `github_desktop_diff.png` | Source-file diff; [official documentation](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop), [original image](https://docs.github.com/assets/cb-66158/images/help/desktop/diff-selection.png), accessed September 11 |
| 34 | `manuscript_diff.pdf` | Actual compiled `latexdiff` output from the [illustrative source pair](../resources/examples/manuscript_revision/README.md); not research results |
| 43 | `coursepack_sources.png`, `coursepack_gap.png` | Existing working-tree coursepack excerpts: source cross-references and a student activity gap; cropped in LaTeX, original images preserved |
| 53 | `kitchen_organizer_telescope_shelf.jpeg` | AI-assisted hobby design examples; existing asset |
| 54 | `filter_families.pdf` | Reproducible figure from the personalized textbook; existing asset |

The Notre Dame marks come from the vendored theme under `theme/logos/`. External screenshot attribution is also clickable in the relevant slide footer. Screenshots retain the vendor's interface colors; native content follows the deck palette.

## Editable visuals

The act strip, agent diagram, instruction-file example, three-repository comparison, claim-tracing table, DOI capability paths, manuscript-task stack, drafting sequence, course timeline, source architecture, and policy/task tables remain editable LaTeX/TikZ objects.

The workspace comparison is now three slides, 8 through 10, one per mode, each with a full-width
screenshot and a single gold annotation. Slides 9 and 10 use official Claude Code documentation
screenshots, attributed in the slide footer the way slides 18, 29, and 34 already handle GitHub
Docs and Overleaf: `claude_vscode_extension.jpg` from the
[VS Code page](https://code.claude.com/docs/en/vs-code) and `claude_terminal_agent_view.jpg` from
the [agent view page](https://code.claude.com/docs/en/agent-view), both accessed September 14.
**Slide 8 is still a placeholder**: the documentation has no screenshot of the desktop app, so that
one has to come from Alex's own setup. See [open_questions.md](../notes/open_questions.md).

Slide 42 carries a generated TikZ calendar, `figures/august_2026_calendar.tex`. Its day-by-day
shading and the 1,452-commit total (1,084 private, 368 public, August 17–31) come from
`git log --format=%ad --date=short` in `optimization-private` and `ndcbe/optimization`; the
generator is `figures/august_2026_calendar_source/make_calendar.py`. August 17, outlined in gold, is when the course
sprint began; August 24, outlined in ND blue, was the first lecture, per `org/calendar.md` in the public repository.

The [Antigravity ineligibility screenshot](../notes/evidence/antigravity_account_ineligible_2026-09-11.png) is evidence for the slide 7 access statement, not a separate live slide. Its provenance is Alex's ND-account check on September 11.
