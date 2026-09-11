# Working with AI Agents in a Research Project

**What this is.** Practices for using an AI coding agent (Claude Code, Codex, or similar) as part of a research project rather than as a chat window. Distilled from roughly a year of real projects — refactors, manuscript audits, package releases — including the parts that did not work.

**When to reach for it.** Before your first agent session on a project, and again whenever a project starts sprawling: too many notes files, a stale plan, work you can't hand to another machine or another tool.

**How to read it.** Sections are numbered and stable, so you can point an agent at a specific one (`follow §5 of working_with_ai_agents.md`). Sections 11–12 include dated tool-specific details.

---

## 1. Context, not conversation

A conversation is not project memory. It is not versioned, not visible to collaborators, not searchable six months later, and gone when the session ends. Everything you want to survive has to be in a file.

The failure mode is concrete and common: a commit message that says *"see the conversation for the full inventory and the plan."* That conversation no longer exists. The change is still in the repository; the reasoning behind it is not.

Three kinds of context are worth distinguishing, because they live in different places:

- **Persistent** — goals, conventions, terminology, how to run things. True across sessions. Belongs in a project entry-point file (§2).
- **Authoritative** — the papers, code, data, and results that actually determine what is true. Belongs wherever it already lives; the agent is pointed at it, never asked to remember it.
- **Task** — what you are asking for right now. Belongs in the prompt, and in a saved copy of the prompt if the task matters (§4).

**Rule:** if a decision exists only in a conversation, it does not exist. Write it into a file in the same session you make it.

## 2. The project entry point

Keep one file that an agent reads first. Give it a tool-neutral name (`PROJECT.md`, `RESUME_HERE.md`, `context.md`) so any tool can be pointed at it, and see §11 for how to make tool-specific files point at it.

What earns a place in it:

- **What this project is**, in three sentences.
- **Where things are** — the repositories involved and each one's role, using repo-relative paths (§8).
- **How to run it** — environment name, the exact interpreter or activation command, the three commands that matter.
- **Conventions** — anything an agent would otherwise guess wrong, especially conventions that encode a past failure.
- **Current state**, with a resume pointer: what was last done, what is in flight, what is uncommitted.
- **Open questions only you can answer** — kept in one place, so they don't scatter (§7).

Two habits keep it usable:

- **Route, don't inline.** The entry point says where the detail lives; it does not reproduce it. A long entry point stops being read.
- **If the file is chronological, put a staleness pointer at the top.** For example: *"For current state, start at the bottom. Everything above is historical log, kept for narrative continuity, not as a to-do list."* This is a repair, not a design — a single "Current state" section rewritten in place is better where you can manage it.

## 3. Document lifecycle: living, dated, superseded

Agents generate documentation eagerly. Left unmanaged, a project accumulates notes files that all look authoritative and are quietly wrong. Sort every document into one of three categories and treat each differently.

**Living** — must be current. The project entry point, the decision queue, the running log. **Cap this set at three or four per project.** Every additional living document is another thing that can silently go stale.

**Dated records** — frozen by definition, and therefore never stale. A run record dated 27 August is still correct in December, because it describes that run. Prefer this category: a dated record costs nothing to maintain. Give them dated names and never edit them after the fact.

**Superseded** — either delete, or add a banner at the top naming the successor:

> **Superseded.** Do not source a number from this file. `analysis/regen_deltas.md` is the sourcing authority as of 2026-08-10.

**The rule that stops sprawl:** an agent may append to the running log and may create dated records freely. It may **not** create a new living document unless you ask for one. Most documentation sprawl is an agent creating a living document that nobody adopted.

**Logs are append-only.** Corrections go in as later entries, never as rewrites of earlier ones — the reasoning trail is the point. Where an earlier conclusion was overturned, keep it with a dated note saying so.

**Name a single sourcing authority** for each class of number. When someone asks "where does 4.7% come from?", exactly one file should be the answer.

## 4. Roles and division of labor

Separating planning from execution works better than doing both in one long session, and it produces a reviewable record.

- **One session plans and reviews.** It writes the plan, drafts the task, and checks the result against the source.
- **Another session executes** one bounded task at a time, writes its outputs, and reports back.
- **The reviewer commits, not the executor.** The worker lists the files it produced; the reviewer stages exactly the verified set. This single rule prevents the most common bad outcome — a large, plausible, unreviewed change landing in the history.
- **Save the prompt before dispatching it.** A prompt is a research artifact: it records what you asked, which is half of what a result means. A directory of numbered prompts plus the git log makes the work replayable.

**Cross-model review is a technique, not a nuisance.** Having a second tool audit the first one's work catches things a same-model recheck misses. When you do it, say so explicitly in the prompt:

> A prior audit already covered these six items. **Do not assume that pass was exhaustive or that its fixes are beyond question** — re-derive each from the primary source yourself. The point of a second audit by a different tool is to catch what the first one missed.

## 5. Standing rules to give an agent

These are the instructions that repeatedly earned their keep. Put them in the project entry point once rather than retyping them per session.

- **Do not fabricate numbers.** Every quantitative value must come from a named source — a results file, a manifest, a specific table. If two sources disagree, use the authoritative one and **flag the discrepancy in place**; never silently overwrite.
- **Surface, don't guess.** When something is ambiguous, leave a visible marker and ask, rather than resolving it plausibly. A flagged question is cheap; a plausible wrong answer is expensive and invisible.
- **Preserve honest caveats.** Results that weaken the argument must survive the edit. State this explicitly, because the default drift of AI-assisted writing is toward a cleaner, more one-sided story than the evidence supports.
- **Report uncertainty as a status, not as hedging prose.** "Cannot verify" is a legitimate, useful outcome (see `manuscript_audit.md`). Vague hedging is not.
- **Do not re-litigate settled questions.** Record negative results — approaches tried and rejected — and instruct the agent not to repeat them. Agents will happily re-run a settled experiment.
- **Do not silently reduce scope to finish.** If a task won't complete within its budget, report the last completed stage and stop. Quietly halving the number of runs to fit the window produces a result that looks finished and isn't.

## 6. Guardrails and boundaries

- **Make the subject read-only.** When auditing or porting something, the material under examination is never modified. Say so in every prompt, and keep the workspace in a separate directory.
- **State write boundaries explicitly** when more than one repository is involved: this one is EDIT, that one is READ-ONLY.
- **No credentialed actions.** Publishing a package, pushing a tag, registering a publisher, uploading to a journal — these stay with you. An agent can prepare all of it and write the checklist; it does not execute it.
- **State the autonomy budget and the stop conditions** for long-running work: how many hours, how many concurrent processes, what to do when the budget expires.
- **Expect hard external kills, not just your own stop conditions.** An organizational spend limit, a rate limit, or a crashed session can terminate an agent mid-task with no warning — this is a different failure than a self-imposed budget running out. Commit or checkpoint often enough that a mid-task kill loses minutes, not hours, and treat resuming after one as reconciliation — what actually landed, what's half-done and needs finishing or discarding — not a clean restart.
- **Review the diff.** Not the summary of the diff. Prefer many small, understandable changes to one large one that passes its tests.

## 7. Ending a session: the handoff block

Before you stop, write down the state. This is what makes tomorrow's session, another machine, or another tool possible.

```
## State snapshot — 2026-09-02

Git: `main` is at a1b2c3d, identical to origin/main. Working tree clean.
     Branch `refactor/case-study` is 12 commits ahead, pushed.
In flight: baseline capture running; results land in results/2026-09-02/.
Resume point: read notes/findings.md §4, then run tools/verify_baseline.py.
Open for me (not the agent): whether Table 3 uses the pooled or per-run estimate.
```

Verified git state, stated literally, is worth more than a summary — "everything is pushed" is a belief; a commit hash is a fact. Keep a **single decision queue** for the questions only you can answer, with a recommendation on each, and a closing list of items already decided so they don't get reopened.

## 8. Working across tools and machines

Switching between agents is often deliberate and good (§4). What breaks is portability, and it breaks in three predictable ways.

- **Tool-specific configuration does not travel.** One vendor's context file is not read by another's tool, and local permission settings are usually untracked, so they vanish on clone. Keep the durable content in a tool-neutral file (§2) and let tool-specific files point at it (§11).
- **Absolute paths go stale.** The same repository sits at different absolute paths on different machines, and directories get reorganized. **Use repo-relative paths in every document and link.** This rule is easy to write down and easy to violate; check it when you review.
- **Unpushed work is invisible work.** Before switching machines, push. Two related traps: a default branch that has not moved in months while all real work lives on a feature branch, and a local checkout sitting on the wrong branch entirely. Anyone who clones — a collaborator, a reviewer, you on another laptop — gets the stale state.

## 9. Rules must be checkable, not just written

This is the honest limit of everything above. **Instructions in a markdown file are advisory, and they degrade.** In practice, project context files go stale — including ones that warn about staleness, and ones containing absolute paths right below a rule forbidding absolute paths.

What holds is anything with a mechanical failure mode: a test suite that exits non-zero, a verification script that fails a gate, a runtime check that raises before work starts, a linter that blocks a commit.

**So: decide which of your rules actually matter, and give each one something that fails.** The general form is to determine status from evidence rather than recollection. If you need to know whether a correction was applied, don't remember — test whether the uncorrected text is still present.

The lesson stated plainly, from a case where a status report was given from memory and was wrong for eleven items:

> The remedy is not to be more careful but to stop deriving status from recollection at all.

Cheap things worth automating: a check that every internal link resolves; a check that living documents are newer than the last commit that changed what they describe; a check that each supersession banner names a file that exists.

## 10. Recording and disclosing AI use

- **Use commit trailers consistently** (`Co-Authored-By:` or an equivalent convention). Inconsistent attribution is worse than none: if trailers appear for one month and stop while the work continues, the record no longer supports a later claim about how the work was done.
- **Put the reasoning in the commit message.** The diff shows what changed; the message is the only place the *why* can live. This matters more with agent-scale changes: a 40-file commit with a one-line message is unreviewable.
- **Disclose in the paper according to the venue's policy**, and describe what the tools did and did not do. If an agent refactored the numerical methods, that is a methods-section fact, not a copy-editing footnote.
- **Record the venue-policy check itself** — which policy, which date, what it required. Policies change faster than manuscripts move.
- **Track review status per unit of content, not just once per document.** A one-time disclosure line ("AI assisted with this manuscript") tells a reader that AI was involved somewhere; it doesn't tell you — or them — which specific sections you've actually checked since the last AI pass. A stronger pattern: give every AI-touched unit (a section, a paragraph, a course page) an explicit state — `unreviewed` / `reviewed` / `reviewed-stale` (content changed after review; needs a fresh look) / `exempt` (not AI-drafted) — and never let a change silently keep a `reviewed` status; force it back to `reviewed-stale` instead. This generalizes past any one kind of document: on a proposal it shows a coauthor exactly which sections you've read since Codex or Claude last touched them; on a manuscript it can gate submission on zero `unreviewed` sections remaining. Where the audience is someone relying on the content in real time — a student, a coauthor — make the status visible to *them*, not only to you.

## 11. Tool-specific mechanics

> ⚠️ **This section dates fastest.** It describes tools as of September 2026 and will drift. Everything in §1–§10 is meant to outlive it. Check the vendor's current documentation before relying on any detail here.

A project instruction file is a **startup briefing**: text supplied to the model before the task. “Pre-context” is a useful informal analogy, but it is still part of the context window, not a separate training stage or an enforcement mechanism. Instructions do not grant filesystem access or override tool permissions.

| Mechanism | Claude Code | Codex |
|---|---|---|
| Project file | `CLAUDE.md` | `AGENTS.md` |
| Discovery | Ancestor guidance at startup; nested guidance when those files are read | Global guidance, then project-root-to-working-directory guidance at startup; nearer guidance takes precedence |
| Setup helper | `/init` drafts instructions; `/memory` inspects loaded files | `/init` scaffolds `AGENTS.md`; review the result against the actual project |
| Sharing rules | `@AGENTS.md` in `CLAUDE.md` imports a shared file | Reads `AGENTS.md` by default; other filenames require explicit configuration or instructions |

Checked September 11, 2026: [Claude memory](https://code.claude.com/docs/en/memory), [Codex instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md), and [Codex commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli).

Keep the root file short: purpose, paths, verified setup/build commands, conventions that matter, and write boundaries. Put task plans and detailed history elsewhere and link to them. Claude recommends under 200 lines per `CLAUDE.md`; Codex defaults to a 32 KiB combined project-instruction limit. These are different measures, neither a target to fill. After setup, ask the agent to identify its loaded guidance and run one listed verification command. Correct incorrect commands before adding more rules.

For this repo's portable template, either keep a tool-neutral `PROJECT.md` with thin pointers from both files, or use `AGENTS.md` as the shared core and import it from `CLAUDE.md`:

```markdown
@AGENTS.md
```

Imports load the referenced content too; splitting a large file into imports does not make its startup context smaller. A normal pointer to background documentation lets the agent read that material when the task needs it.

### Claude hooks

Hooks respond to lifecycle events. A command hook executes a script; prompt or agent hooks can evaluate conditions. They are configured in `.claude/settings.json` and can be inspected with `/hooks`.

| Event | Research example |
|---|---|
| `PreToolUse` | Inspect a proposed edit and reject it if it targets a protected baseline. |
| `PostToolUse` | Run a formatter or focused check after an edit. |
| `Stop` | Check whether the required evidence exists before accepting completion. |

For example, a command hook can receive the proposed tool call as JSON on standard input. In a `PreToolUse` command hook, exit code 2 blocks the action and returns the script's error message. Ordinary test exit code 1 is **not** automatically equivalent to a blocking hook: write the adapter for the documented event semantics and test it. A hook that watches `Edit|Write` alone will not catch every possible file mutation through shell commands. Keep filesystem permissions and final verification in place. Guard Stop hooks against endless retries.

Use [Anthropic's hooks guide](https://code.claude.com/docs/en/hooks-guide) for the current event schema and examples. Hooks run with the process's access; inspect a script before enabling it. Do not enable a new hook just because it was suggested by a repository you downloaded.

## 12. Independent work overnight or over a weekend

Before leaving, save an execution plan in the repository. A usable plan names the intended artifact, completion evidence, source authority, permitted edits, reversible decisions, checks between phases, resource/time budget, and conditions that require your judgment. Agree on the review point before starting. “Work for 12 hours” alone does not define success.

The seminar's examples use a 12-hour lecture revision plan and a 24-hour feasibility-study plan. The lecture plan reserves ambiguous annotations and major teaching changes for instructor review. The study plan reserves changes to the scientific question and baseline discrepancies for researcher review. These are planning budgets, not claims that a service guarantees uninterrupted runtime.

An adaptable task brief:

```text
Objective: Reproduce the selected result and prepare a reviewable revision.
Authority: Use the specified paper, input data, and committed baseline.
Write scope: This feature branch; do not edit reference outputs.
Phases: inventory -> baseline -> bounded revision -> verification -> handoff.
Gate: Compare each changed result with its saved reference before continuing.
Autonomy: Fix reversible implementation defects within the agreed scope.
Stop: Ambiguous data, scientific choices, changed scope, or budget exhaustion.
Budget: Up to 12 hours; record work remaining instead of weakening checks.
Handoff: Commit verified changes; list commands, artifacts, failures, and
         decisions for me. Do not push or publish unless authorized.
```

Choose the mechanism for the job:

- **Codex Goal** pursues a persistent objective across turns. Set a concrete completion condition; current app commands include `/goal`. Availability depends on the installed surface. See [Codex commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli).
- **Claude Code `/goal`** checks a condition after each turn and can continue the current session. Its evaluator judges the evidence surfaced by the agent; it is not an independent reproduction of the result. See [goals](https://code.claude.com/docs/en/goal).
- **Claude Code `/loop`** repeats a prompt at an interval, useful for polling a running computation. It needs a running session; it is not a guarantee of continuous progress toward a research outcome. See [scheduling](https://code.claude.com/docs/en/scheduled-tasks).
- **Scheduled tasks** are for starting work later or on a recurring schedule. Local execution requires a machine that remains available; cloud jobs need the right repository, dependencies, and authorized data access.

Before an unattended local run, verify the environment, usage allowance, permissions, machine wakefulness, checkpoint location, and resume procedure with one short trial. Do not bypass approval or data-access controls to make it run unattended. Review the actual diffs and output artifacts in the morning; a completion message is not sufficient evidence.

---

## Checklist

Before your first agent session on a project:

- [ ] A tool-neutral project entry point exists and says what the project is, where things are, and how to run it
- [ ] Paths in it are repo-relative
- [ ] Standing rules (§5) and guardrails (§6) are written down once, not retyped per session
- [ ] The set of living documents is named, and is three or four files

During a session:

- [ ] The task is bounded, and its prompt is saved if the result matters
- [ ] Write boundaries are stated when more than one repository is in scope
- [ ] You reviewed the diff, not a summary of it
- [ ] Uncertain items came back flagged rather than resolved

Before you stop:

- [ ] A handoff block records verified git state, what's in flight, and the resume point
- [ ] Decisions made this session are in a file, not only in the conversation
- [ ] New documents are categorized: living, dated, or superseded
- [ ] Work that another machine needs is pushed
- [ ] AI-touched content has a review status (§10), not just a one-time disclosure line

## Anti-patterns

- **Deferring to the conversation.** "See the chat for the full plan." The chat is gone.
- **A growing pile of living documents.** Six notes files that all look current, three of which are wrong.
- **The plan that stopped being maintained.** A plan file abandoned within days, while the work continued for months in commit messages only.
- **Attribution that lapses.** Trailers for one month, none for the next three, during the most agent-intensive period.
- **A rule with no gate.** Every rule you actually need enforced but only wrote down.
- **Treating a mid-task kill as data loss instead of a checkpoint to reconcile.** The work since the last commit is gone either way; the difference is whether you knew what was in flight.
- **A disclosure line that doesn't survive an edit.** "AI assisted with this" said once, at the start, while half the document has since changed underneath it.
- **The big green suite.** A passing test run that says nothing, because it doesn't execute the code you changed (see `scientific_computing_workflow.md`).
- **Stale absolute paths**, in a document that tells you not to use absolute paths.

## Using this file with an AI assistant

**As standing project context** — add a pointer to your project entry point:

> Follow `practices/working_with_ai_agents.md`, especially §5 (standing rules) and §6 (guardrails), for all work in this repository.

**As a setup task:**

> Read `practices/working_with_ai_agents.md`. Draft a project entry point for this repository following §2: what it is, where things are (repo-relative paths only), how to run it, and current state. Inspect the repo to fill it in — do not guess. Flag anything you cannot determine rather than inventing it.

**As an audit:**

> Audit this repository against `practices/working_with_ai_agents.md` §3 (document lifecycle) and §8 (portability). For each markdown file, classify it as living, dated, or superseded, and flag any that claim to be current but describe a state that no longer holds. List every absolute path and every internal link that does not resolve. Report findings as a table; change nothing.
