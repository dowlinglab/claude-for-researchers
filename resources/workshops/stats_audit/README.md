# Statistical audit workshop

A short, self-contained exercise for Part 2. Participants audit a colleague's statistical analysis of the public Palmer Penguins data against open statistics references, then judge the quality of the audit they got.

The exercise is domain-neutral. It needs no chemical engineering, no special software beyond an AI assistant, and no prior Git or Python experience for the core route.

| Path | Contents |
|---|---|
| [`activity.md`](activity.md) | The participant instructions for Activity 2, including the optional Step 0 for people comfortable with Git and Python |
| [`audit-project/`](audit-project/README.md) | The project participants work in: a write-up, a notebook with saved outputs, the data, and a reference guide |
| [`workshop2_activity.zip`](workshop2_activity.zip) | The same project as a download. Rebuild it with `python build_audit_zip.py` after any change to `audit-project/` |

The write-up and notebook contain deliberate problems. The instructor's list of them, with the correct reasoning, is kept in the separate private repository, so nothing in this folder answers the exercise.

## Reference texts

The activity uses open references (an open textbook, the NIST e-Handbook, and the ASA statement on p-values). They are not stored here. [`audit-project/references/README.md`](audit-project/references/README.md) explains where to get them and where to save them.

## The data

Palmer Penguins, licensed CC0. See [`audit-project/data/README.md`](audit-project/data/README.md).
