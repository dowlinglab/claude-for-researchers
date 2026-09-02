# Seminar design rationale

Why the talk is organized the way it is, what got cut and why, and the bank of candidate stories to draw from. This is the "why" behind [outline.md](../outline.md); day-to-day decisions and actions live in [seminar_notes.md](seminar_notes.md); unresolved items in [open_questions.md](open_questions.md).

## Why lifecycle, not a product tour

The original charter lists 14 major topics — each defensible as its own talk. Organizing around Google/OpenAI/Anthropic products would force constant context-switching and reward whichever vendor is trendiest this month, which cuts against the charter's own stated lesson: *"Do not become loyal to one model. Become good at working with models."*

Organizing around the research lifecycle (Explore → Ground → Build → Record → Write → Verify) instead means:
- Every section answers "where does this fit in a project I already have," not "what does tool X do."
- The persistent/authoritative/task-context distinction (Section 2 of the outline) can be introduced once and then reused as the throughline for literature, code, the log, writing, and verification — instead of re-explained per topic.
- It naturally produces the closing synthesis: AI's role changes at each stage, but the discipline (put things in files, ground claims in sources, review before trusting) doesn't.

## Scope discipline: charter topics → where they landed

| Charter section | Outline section | Notes |
|---|---|---|
| 1. Ecosystem overview | 1 | Deliberately kept to 3 min; table + one ND-specific caveat, no deep dives |
| 2. Persistent project context | 2 | Promoted to the conceptual spine of the whole talk, not a standalone topic |
| 3. Literature research/brainstorming | 3 | Full |
| 4. Literature-folder workflow | 3 (mention only) | Full version is a resource + handout section, not walked through live |
| 5. DOI/reference checking | 3 (mention only) | Same treatment as #4 — a resource, not a live demo (network dependency risk during a live talk, too) |
| 6. Research software/reproducibility | 4 | Full |
| 7. Repository organization (one vs. two repos) | 4 (brief) | Surfaced, not resolved live — see `resources/examples/repository_patterns/` |
| 8. "Organize this research repo" prompt | 4 (referenced) | Takeaway resource, not demoed step-by-step |
| 9. Writing papers / AI slop / style guide | 6 | Style-guide derivation process is handout material; live talk shows the pattern, not the method |
| 10. LaTeX/Overleaf/Git | 6 (one line) | Mechanics are handout-only |
| 11. Group/journal-specific instruction files | 6 | Framed explicitly as the Section 2 pattern applied to writing |
| 12. Journal selection | 6 (one bullet) | Resolved 2026-09-02: kept as a single bullet, not cut, not handout-only — see [open_questions.md](open_questions.md) |
| 13. Scientific auditing | 7 | This is the intended climax — see below |
| 14. Responsible AI use | 8 (+ woven throughout) | Compressed at the close; individual principles surface inline elsewhere rather than saved for one ethics slide |

## Duplication resolved

- **Sections 6 and 7 of the charter** (research software maturity, and one-repo-vs-two-repo) are really one theme — "what does a mature, auditable research project's files look like" — with the repo-split question as a sub-decision inside it. Outline Section 4 treats them as one arc; the two-vs-one-repo tradeoff gets a brief mention plus a pointer, not equal time.
- **The three audit types** (quantitative-claim, methods-vs-code, figure-vs-text) plus the journal-guideline compliance check are structurally the same move: *trace a claim/artifact back to its authoritative source and report match/mismatch/cannot-verify.* Teaching one worked example (quantitative-claim) in full and naming the other two as variations avoids repeating the same demo three times. All four become modes of one resource, `resources/prompts/manuscript_audit.md`, rather than four files.
- **The literature-folder workflow and DOI checker** are both "bibliography hygiene" tasks that combine deterministic scripts with AI judgment. They get one combined mention in Section 3 rather than two separate demos.

## Cut entirely (or reduced to a handout line) from the live talk, with rationale

- **Journal selection (charter §12).** Originally recommended for a full cut as a decision-support workflow adjacent to, but not part of, the core "AI reads/writes/checks your artifacts" narrative. Alex's call (2026-09-02): keep it, but only as a single bullet in Section 6 — cheap enough not to dilute the climax, and it rounds out the writing stage.
- **Full LaTeX/Overleaf mechanics (charter §10).** Useful, but mechanical enough that a slide walkthrough adds little beyond "AI can check labels and acronyms too" — better delivered as a handout checklist.
- **Amateur Radio textbook anecdote (charter, personal experiences #4).** Excellent illustration of "AI transforms a curated source corpus into a new structured artifact," but it's not an academic-research example, and the talk already has five strong candidate stories from real research (see [demo_ideas.md](demo_ideas.md)). Resolved (2026-09-02): a single spoken aside in Section 3, with a link to the now-public repo — never a standalone case study competing for slide time.

## The verify section as climax

Section 7 (audit) is placed second-to-last and given the clearest single visual (the claim-tracing table) deliberately: it's the payoff that makes every earlier practice legible as worthwhile. A researcher who has been logging, keeping tests, and structuring context arrives at this stage able to actually run the audit; one who hasn't, can't. Placing it right before the responsible-use closing also sets up the closing line — auditing is what "AI helps us challenge our own work" looks like in practice, not an abstract virtue.

## Tone guardrail

Per the charter's final constraint, this is not a celebration of AI for its own sake. Concretely, that means:
- No slide claims a workflow step "requires" AI — always frame as "AI makes this easier/faster/more consistent," since every one of these practices (logging, testing, auditing) predates GenAI and remains valuable without it.
- The closing section actively returns ownership to the researcher rather than ending on a capability demo.
- Avoid the word "revolutionize" and similar inflation throughout slides, handout, and resources — practice what Section 6 preaches.

## Story bank

See [demo_ideas.md](demo_ideas.md) for the full write-up of each candidate example (the five personal experiences from the charter) and which outline section each best supports. Open design choice: which story opens/bookends the talk vs. which are used as inline section demos — tracked in [open_questions.md](open_questions.md).
