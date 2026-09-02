# Template: research log

A dated, append-only record of what you tried, what happened, and what you concluded.

**Why bother.** Six months later, neither you nor an AI assistant can reconstruct why experiment 14 was abandoned or which configuration produced the number in the abstract. A chat history won't help: it isn't versioned, isn't shared, and isn't searchable by your collaborators. A log entry costs about five minutes and is the difference between *"what did we learn from experiments 14–27?"* being answerable and not.

**The rule that makes it work: append only.** Corrections go in as *later* entries, never as edits to earlier ones. The reasoning trail is the point — an entry that was wrong, followed by the entry that corrected it, is more useful than a tidy file that pretends the first one never happened.

**Keep it cheap.** The fields below are a menu, not a form. Question / what I did / result / next is a complete entry. Everything else is optional. A log you actually keep beats a thorough one you abandon in March.

**Where it goes.** `notes/research_log.md`, or `LOG.md` at the repository root. It is one of your three or four living documents ([`../practices/working_with_ai_agents.md`](../practices/working_with_ai_agents.md) §3).

---

## The template

```markdown
# Research log — <project>

Append-only. Newest entries at the bottom. Corrections are new entries, never
edits to old ones. Every number cited here should name the file it came from.

---

## <YYYY-MM-DD> — <one-line title>

**Question.** <What was I trying to find out? One sentence.>

**What I did.** <Script, command, and configuration. Enough to rerun it.>
- commit: `<hash>`
- command: `<python scripts/run.py --config configs/x.yaml --seed 42>`
- data: `<data/processed/batch3.csv>`

**Result.** <The numbers, with the file they live in — not from memory.>
- <metric: value>  → `results/2026-09-02/summary.csv`

**Interpretation.** <What this means. Say how confident you are, and why.>

**Didn't work.** <What you tried that failed, and how it failed. Write this one
even when — especially when — you would rather not. It is the field that saves
the most time later, for you and for anyone who inherits the project.>

**Next.** <The question this opens, or the next thing to run.>
```

---

## A worked entry

```markdown
## 2026-08-14 — Does the temperature-dependent isotherm change the ranking?

**Question.** The May result said physics features don't help. That conflicts
with my intuition about the low-temperature branch. Is the ranking an artifact
of the isotherm fit feeding the baseline?

**What I did.** Refit the pure-component isotherms with the T-dependent form,
regenerated the baseline, reran experiment 13 unchanged otherwise — same split
seeds, same dataset rows, so the isotherm is the only variable.
- commit: `e976ed6`
- command: `python scripts/run_experiment.py --exp 13 --isotherm td --seed 20260705`
- data: `data/processed/co2_ch4_v2.csv` (unchanged from exp 13)

**Result.** Ranking reverses. Physics-informed model now wins on 4 of 5 splits.
- RMSE, physics vs. plain: 0.041 vs. 0.058 → `results/2026-08-14/exp13_td/metrics.csv`
- Regression suite: 38/38, with the 6 baseline values updated deliberately —
  reason recorded in the same commit.

**Interpretation.** The May conclusion was an artifact of the isotherm fit, not
a property of the features. Reasonably confident: the only change was the
isotherm, the seeds and rows are identical, and the corrected baseline agrees
more closely with the independent reference implementation than the old one did.
Not yet checked whether this holds for the second mixture.

**Didn't work.** First attempt rescaled the fit inside the analysis step rather
than at the baseline, which changed the metrics *and* the split assignment — two
variables at once, so the run was uninterpretable and I threw it away. Rerun
with the rescaling moved upstream.

**Next.** Repeat on the Xe–Kr mixture. If the reversal holds there too, the
manuscript's central claim needs rewriting, not just a corrected number.
```

---

## What to log, and when

**Log an entry when:** a run finishes and you formed an opinion about it; you made a decision that would be expensive to re-derive; something failed in a way that would waste an hour if repeated; you're stopping for the day mid-thread.

**Don't log:** every command. The log is for conclusions and dead ends, not a shell history.

**Cite files, not memory.** "RMSE improved to 0.041 (`results/2026-08-14/metrics.csv`)" is checkable. "RMSE improved" is not, and in six months you won't be able to tell whether it was 0.041 or 0.14.

**Note when a run is superseded.** Don't delete the entry — add a later one saying which result replaced it and why. Same for results directories: quarantine with the reason in the name rather than deleting.

## Using it with an AI assistant

The log's real payoff is that an assistant can reconstruct project history from evidence rather than from your recollection. Three things this enables:

**Ask it to summarize a stretch of work:**

> Read `notes/research_log.md`. Summarize what was learned from the entries between 2026-06-01 and 2026-08-31: what was established, what was ruled out, and what questions are still open. Quote the entry dates you're drawing on. Where entries conflict, say so rather than reconciling them.

**Have it draft the entry, and check it:**

> Draft a research log entry for the run we just did, following `templates/research_log.md`. Pull the commit, command, config, and result file paths from what actually happened — do not fill in a number from memory or from this conversation. Leave the Interpretation section blank; I'll write that.

**Have it flag when the log has drifted from the repository:**

> Compare the last ten entries in `notes/research_log.md` against the git log and `results/`. Flag entries citing a commit that doesn't exist, a results file that isn't there, or a number that doesn't match the file it cites. Report only; change nothing.

One caution: the Interpretation field is yours. An assistant can summarize what happened and check that citations resolve. What a result *means* — and how much you believe it — is the part that has to come from the person who will defend it.
