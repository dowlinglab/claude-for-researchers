# Handoff

The document that lets you — or anyone else — resume this project cold.

Update it at the end of each work session, and whenever you stop mid-task. The
test: if you came back in three months having forgotten everything, could you
start working from this file alone?

Keep it short. A handoff nobody rereads is not a handoff.

---

## State

**Date:**
**Branch:**
**Commit:**
**Working tree:** clean / has uncommitted changes (list them)

## What is done

-

## What is in progress

What you were in the middle of, and what the next concrete action is. Not "keep
working on tests" — the actual next step.

-

## Verified gates

Which checks were actually run, when, and what they returned. A gate you believe
passes but did not run does not belong here.

| Check | Command | Last run | Result |
|---|---|---|---|
| Environment | `python -c "import cstr_workshop"` | | |
| Notebook executes | `python scripts/run_notebook.py --check` | | |
| Tests | `pytest tests` | | |
| Reproduction | `python scripts/reproduce.py` | | |
| Report compiles | `cd report && latexmk -pdf report.tex` | | |

## Decisions and their reasons

Non-obvious choices, with the *why*. This is the part that is expensive to
reconstruct and cheap to write down.

-

## Open questions

Things you do not know yet, including the ones you decided to defer.

-

## Known limitations

What this project does not establish. Carry these forward — they are the
starting point for the claim audit.

-
