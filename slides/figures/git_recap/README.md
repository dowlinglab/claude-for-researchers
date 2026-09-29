# Git and GitHub recap figures

TikZ sources for the Part 2 recap slides in [`sections/07b_part2_git_recap.tex`](../../sections/07b_part2_git_recap.tex). Each file is a single `tikzpicture` that `\input`s into a frame. They depend on the `nd box` and `nd highlight` styles and the `\good` and `\bad` macros in [`main.tex`](../../main.tex), so build them by compiling the deck (`make -C slides part2`) rather than on their own.

| File | Shows |
|---|---|
| `local_to_github.tex` | Project folder, local repository, and GitHub, with commit, push, and pull |
| `commit_history.tex` | A history of four commits, and which of them are on GitHub |
| `github_vs_storage.tex` | Which kinds of files tend to belong in GitHub and which in cloud or institutional storage |
| `nested_repositories.tex` | One repository next to a repository nested inside another |

The layout is drawn for a full-width frame. Scale a figure with `\resizebox{\linewidth}{!}{...}` if a slide needs it.
