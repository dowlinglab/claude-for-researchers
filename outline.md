# Talk Outline — 40 minutes

Status: draft, timed, not yet built into slides. See [notes/seminar_design.md](notes/seminar_design.md) for the rationale behind these choices and [notes/demo_ideas.md](notes/demo_ideas.md) for the candidate stories referenced below.

The seminar slot is 1 hour: 40 minutes of talk, 20 minutes of questions. This outline covers the 40-minute talk only.

This outline follows the research lifecycle — **Explore → Ground → Build → Record → Write → Verify** — rather than a tour of AI products. Every section not listed here (journal selection, the full DOI checker walkthrough, LaTeX/Overleaf mechanics, the Amateur Radio anecdote, etc.) has been deliberately pushed to the handout and `resources/`. See "Cut from the live talk" at the end.

## At a glance

| # | Section | Time | Cumulative |
|---|---|---|---|
| 0 | Open | 2 min | 0:02 |
| 1 | AI ecosystem, briefly | 3 min | 0:05 |
| 2 | The core shift: context, not conversation | 5 min | 0:10 |
| 3 | Explore & Ground: literature | 4 min | 0:14 |
| 4 | Build: notebook → reproducible codebase | 7 min | 0:21 |
| 5 | Record: the research log | 3 min | 0:24 |
| 6 | Write: manuscripts as structured artifacts | 5 min | 0:29 |
| 7 | Verify: audit before the reviewers do | 6 min | 0:35 |
| 8 | Responsible use & closing | 4 min | 0:39 |
| — | Buffer | 1 min | 0:40 |

Verify and Write keep their full time on purpose — they're the most differentiated content. The cuts to reach 40 minutes came out of the more expository early sections (1, 2, 3, 5), one minute each; see [notes/seminar_notes.md](notes/seminar_notes.md) for when this was decided.

---

## 0. Open (2 min)

**Teaching point:** This talk is about workflow integration, not a tool tutorial.

**Supporting ideas:**
- State the thesis directly: the most powerful uses of GenAI in research go beyond asking a chatbot questions or polishing prose.
- Name-drop the frame story once, to be resolved at the close: helping a project cross the finish line when a graduate student is graduating — sometimes with them still around to help, sometimes after they've gone. Real, anonymized project; no student identified. See [notes/demo_ideas.md](notes/demo_ideas.md) story #5.
- One sentence on why now: Anthropic's academic Team plan means many in the room have (or can soon get) a Claude seat.

**Demo/example:** none — this is framing only.

**Students should remember:** Today isn't "how to use Claude." It's how to build a research workflow AI can actually participate in.

---

## 1. AI ecosystem, briefly (3 min)

**Teaching point:** Don't become loyal to one model. Become good at working with models.

**Supporting ideas:**
- One compact table: Google (Gemini, NotebookLM) / OpenAI (ChatGPT, ChatGPT Projects, Codex) / Anthropic (Claude, Claude Projects, Claude Code, Team for Scientists).
- Notre Dame's data-classification rule, confirmed directly on `ai.nd.edu` (see [notes/references.md](notes/references.md)): Gemini, ChatGPT EDU, and NotebookLM are cleared for Public/Internal/Sensitive data; **Claude is currently approved for Public data only** — an Enterprise Claude license is "coming soon" but not yet available. Say this plainly rather than glossing over it — it's real, useful, and slightly complicates "Why Claude?"
- One-line compliance caveat, quoted directly from `ai.nd.edu`: researchers with DoD/DoW-funded contracts or agreements are currently prohibited from using any Anthropic products (Claude.ai, API, Claude Code) — contact `researchsecurity@nd.edu` with questions. Generalize it: if you're a grad student or postdoc, check with your PI or project lead about any special considerations on your specific project (DoD/DoW, export control, sponsor data terms) before adopting any AI tool — don't assume what's fine for one project is fine for another.
- Capabilities and rankings will keep changing regardless of any of the above.

**Demo/example:** the ecosystem table as a single slide, plus the ND data-classification tiers (🟢🟡🟠🔴) as a second small graphic — strong, concrete, institution-specific.

**Students should remember:** Pick tools by task and access, not brand loyalty. At Notre Dame specifically, don't put non-public research data into Claude yet — and whatever your institution, check with your PI about project-specific restrictions before you adopt any AI tool.

---

## 2. The core shift: context, not conversation (5 min)

**Teaching point:** The filesystem/repository is the source of truth. The AI conversation is not.

**Supporting ideas:**
- Distinguish three kinds of context: **persistent** (goals, conventions, style — true across sessions), **authoritative** (the papers, code, data, guidelines that actually determine truth), and **task** (what I'm asking right now).
- A chat history is a poor substitute for all three: it's not versioned, not shared with collaborators, and silently vanishes in usefulness once it's long.
- Introduce the project-instructions-file pattern (`CLAUDE.md` or equivalent) as the concrete mechanism — a short file an AI assistant reads at the start of every session.
- This idea recurs for the rest of the talk: every later section is really "what persistent/authoritative context looks like at this stage of the lifecycle."

**Demo/example:** side-by-side — a chat that has lost track of a project's conventions after a long back-and-forth, versus a short `CLAUDE.md`-style file that restates them in ten lines. (See `resources/templates/CLAUDE.md.example`, planned.)

**Students should remember:** Before asking an AI to do more, put your project's goals, conventions, and authoritative sources in a file it can read — don't re-explain them in every chat.

---

## 3. Explore & Ground: literature (4 min)

**Teaching point:** AI suggestion → locate source → inspect source → cite source. Never cite a paper because an AI says it exists.

**Supporting ideas:**
- Early-stage uses that are genuinely good: terminology discovery, conceptual maps, competing hypotheses, turning a vague idea into a research question, search-strategy brainstorming.
- The failure mode: treating brainstorming output as literature evidence.
- Once you have an actual corpus, AI gets much more useful when it's grounded in it — summarizing, comparing methods, building a literature matrix, flagging apparent tensions or untested assumptions. The evidence-first prompt pattern: ask the model to show what in the provided papers caused it to flag something, not just assert a conclusion.
- One-line pointer to the literature-folder workflow (renaming, dedup, `literature.md`) as a takeaway resource rather than a live walkthrough.
- Brief aside (a few seconds, with a link on the slide): the same "curate source material → structured, purpose-built artifact" pattern is how Alex built a study guide for an Amateur Radio license exam — [github.com/adowling2/radio-extra-book](https://github.com/adowling2/radio-extra-book). Not a research example; included only to show the pattern generalizes.

**Demo/example:** one prompt shown on-screen — "Based only on these papers, identify apparent tensions, unanswered questions, and combinations of ideas that haven't been explored. For each, show the evidence." Show real (or realistic) output with citations back to specific papers.

**Students should remember:** Use AI to explore and to organize a corpus you already trust — never as the citation itself.

---

## 4. Build: notebook → reproducible codebase (7 min)

**Teaching point:** "The student's code works" is a different claim from "the research software is an auditable artifact someone else can install, understand, test, and extend."

**Supporting ideas:**
- Notebooks are excellent for exploration, poor as a long-term repository of scientific logic (hidden state, duplicated cells, manual execution order, hard-coded paths). The point is not "notebooks are bad" — it's *prototype in notebooks, promote mature logic into modules*.
- What "maturing" a project looks like concretely: extract functions, separate plotting from calculation, add a config file, add tests, make it `pip install`-able.
- Git as the actual audit trail: diffs, commit messages, `.gitignore` hygiene. The explicit warning — **review the diff; don't accept a large AI refactor just because the tests pass.** Prefer small, understandable changes.
- Briefly surface the one-repo vs. split-repo (code + Overleaf manuscript) decision and point to the resource rather than resolving it live — there is no universally correct answer.

**Demo/example:** the graduate-student-code-to-package story — a before/after file tree (organically-grown scripts vs. `src/`, `tests/`, `pyproject.toml`) shown as a single slide, not a live refactor.

**Students should remember:** Treat "AI made my code work" and "AI made my code reviewable, testable, and installable by someone else" as two different, both-worth-pursuing goals — and always read the diff.

---

## 5. Record: the research log (3 min)

**Teaching point:** Log now, ask later — a written log answers "what did we learn from experiments 14–27?" without relying on memory or a giant AI chat history.

**Supporting ideas:**
- What belongs in an entry: date, research question, experiment/calculation, code commit, configuration, datasets used, key outputs, interpretation, failed approaches, next questions.
- Why this matters *especially* with AI in the loop: an AI assistant can only reconstruct project history from what was actually written down, not from what you remember or what's buried in a chat from three months ago.
- Frame as low-effort, high-payoff — a plain Markdown file, not new tooling.

**Demo/example:** one realistic log entry, shown in full, including a "failed approach" line (deliberately, since that's the part people skip).

**Students should remember:** A five-minute log entry after each experiment is cheaper than reconstructing three months of reasoning later — for you and for an AI assistant.

---

## 6. Write: manuscripts as structured artifacts (5 min)

**Teaching point:** Use AI as an editor held to a standard, not an autopilot author.

**Supporting ideas:**
- Treat the manuscript as files (`main.tex`, `sections/*.tex`, `bibliography.bib`), not a blob — this is what lets AI do notation checks, undefined-acronym checks, and reference hygiene without seeing "the whole paper" as one intimidating unit.
- Name the recognizable AI-prose failure modes briefly (inflated importance, generic transitions, homogeneous rhythm) — goal is preserving the researcher's actual voice, not making AI writing undetectable. Point to the personal writing-style-guide resource.
- Group/journal-specific instruction files (`WRITING_STYLE.md`, `FIGURE_GUIDELINES.md`, `JOURNAL_GUIDELINES.md`) as a second example of the "context, not conversation" idea from Section 2, now applied to writing: *"Check this manuscript against the journal instructions and report violations with the specific rule cited."*
- One bullet on journal selection: AI can help build a comparison (scope, audience, methodological fit) across candidate journals from their scope statements and a few representative papers — a support tool for the decision, not a substitute for it.

**Demo/example:** one prompt + one guideline file + one flagged violation, shown as a compact before/after.

**Students should remember:** Give AI your actual writing/journal standards as a file, then ask it to check *against* that file — don't ask it to just "make this sound better."

---

## 7. Verify: audit before the reviewers do (6 min) — the climax

**Teaching point:** Use AI to attack the paper before the reviewers do — and treat "cannot verify" as a successful result, not a failure.

**Supporting ideas:**
- Walk one concrete audit chain: identify a quantitative claim → find the archived output that should support it → trace it back → recompute or check where feasible → flag what can't be verified.
- Show the claim-tracing table as the payoff artifact (see below) — this is the single most memorable image of the talk.
- Briefly name the sibling audits without walking through them: methods-vs-code ("does the paper accurately describe what the code does?") and figure-vs-text ("does the plotted data actually support the caption's claim?"). Full prompts live in `resources/`.
- Explicit principle, said out loud: AI should never fill a provenance gap by guessing. "Cannot verify" is the system working correctly.

**Demo/example:** the claim-audit table —

| Manuscript claim | Location | Source | Status |
|---|---|---|---|
| Costs decrease by 17% | Results §4.2 | `results/cost.csv` | Verified |
| "Approximately doubles" | Abstract | Unknown | Cannot verify |

**Students should remember:** Before you submit, have AI build a table like this for your own paper. A "cannot verify" row is a bug you just found for free.

---

## 8. Responsible use & closing (4 min)

**Teaching point:** The most mature use of these tools is not asking them to create something for us — it's giving them enough structured access to our own research artifacts that they can help us understand, organize, challenge, verify, and improve our own work.

**Supporting ideas:**
- Compress the recurring principles into a short, spoken list (not a bullet-dump slide): scientific judgment stays with the researcher; AI output is not evidence; generated citations need verification; code changes need review; sensitive/restricted data only in institutionally approved systems.
- Return to the frame story from the open and resolve it — name what got faster or safer for that graduating student's project with a research log, an auditable repo, and a claim-tracing pass in place. Keep it about *expediting a finish*, not just recovering from someone leaving.
- Point once, clearly, to the handout and `resources/` as where the reusable material lives, and to the Anthropic Team-for-Scientists application link for anyone who wants a Claude seat.

**Demo/example:** none — this is the synthesis.

**Students should remember:** The one thing to change Monday morning: pick *one* practice from today (a `CLAUDE.md` file, a research log, or a claim-audit pass on a paper you're finishing) and try it on a real project this week.

---

## Cut from the live talk (handout / `resources/` only)

These were in the original charter but don't fit in 40 minutes as full sections without diluting the lifecycle narrative above. Each still becomes a polished resource or a handout section (or, for two items, a single confirmed one-liner in the live talk) — see [resources/README.md](resources/README.md) and [notes/seminar_design.md](notes/seminar_design.md) for where each one landed and why.

- Full literature-folder processing workflow (metadata inspection, renaming, dedup) — handout + `resources/prompts/literature_workflow.md`.
- DOI checker — mentioned in passing in Section 3 at most; full capability description lives in `resources/scripts/doi_checker/` (to be adapted from an existing Alex script, not built from scratch).
- Journal-selection decision matrix — resolved: kept as one bullet in Section 6, full matrix workflow (if built at all) stays handout/resource-only.
- LaTeX/Overleaf mechanics (label checking, acronym consistency details) — folded into one line of Section 6; details in handout.
- Full results/provenance manifest example and single-repo vs. split-repo tradeoff discussion — handout + `resources/examples/repository_patterns/`.
- Methods-vs-code and figure-vs-text audits, in full — `resources/prompts/manuscript_audit.md` (bundled with the quantitative-claim audit as one toolkit).
- The Amateur Radio textbook anecdote — resolved: a single spoken aside with a link, in Section 3. Not a case study in the live talk.
- The research-repository organization prompt (Section 8 of the charter) — not walked through live; it's a takeaway resource (`resources/prompts/organize_research_repo.md`), referenced once in Section 4.
