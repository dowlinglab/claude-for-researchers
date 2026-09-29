# A draft analysis to audit

A member of your team gave you a Jupyter notebook and a short write-up of a statistical analysis of body measurements from three penguin species. How can you use an LLM to augment your critical thinking and check it? Before anyone builds on it, audit it: check the write-up and the code against trusted statistics references, and decide which claims you would let stand.

This is a teaching exercise. The notebook and the write-up contain deliberate problems of different kinds and difficulty. The number is not stated. Some are easy to spot and some are subtle, so finding every one is not the goal. The goal is to learn how to audit an analysis with an AI assistant, and how to judge the quality of the audit it gives you.

## What is here

| Path | Contents |
|---|---|
| `writeup.md` | The colleague's short results write-up |
| `notebooks/penguin_analysis.ipynb` | The analysis, with its outputs saved |
| `data/penguins.csv` | The public Palmer Penguins data ([source and license](data/README.md)) |
| `figures/` | Figures the notebook saves |
| `references/` | [Where to get the reference texts](references/README.md) |
| `environment.yml` | Optional. Only needed if you want to rerun the notebook |

You do not need to run the notebook to audit it, because its outputs are saved. Rerunning lets Claude check that the saved outputs match the code.

## How to start

1. Put this folder where you keep your projects. Open it in Claude (desktop app, editor extension, or terminal).
2. Save the reference texts into `references/pdfs/`, following the [reference guide](references/README.md). That folder is ignored by Git.
3. Follow the [Activity 2 guide](https://github.com/dowlinglab/claude-for-researchers/blob/main/resources/workshops/stats_audit/activity.md) or the Part 2 handout.

Keep the original files as they are until you have reviewed Claude's findings. If you want Claude to edit anything, ask it to work on a copy or a branch.
