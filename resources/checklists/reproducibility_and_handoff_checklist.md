# Checklist: reproducibility and handoff

**The one test both halves of this checklist share:** can someone else — a labmate inheriting your project, a reviewer, your own future self after six months away — install it, understand it, and extend it, using only what's in the repository?

**Two directions, one test.** Task 2's problem ("inherit a messy project, reconstruct its context") is Task 4's problem in reverse ("release something someone else can pick up"). The checklist is the same either way; only which end of it you're standing on changes. Use the **Receiving** half when you're the one inheriting; use the **Leaving** half before you hand something off, archive it, or release it.

This is a checklist, not a practice file — it doesn't re-argue the reasoning. Each item cites the practice file that does: [`../practices/working_with_ai_agents.md`](../practices/working_with_ai_agents.md), [`../practices/scientific_computing_workflow.md`](../practices/scientific_computing_workflow.md), [`../practices/private_code_to_public_package.md`](../practices/private_code_to_public_package.md).

---

## Receiving (Task 2: inheriting a project)

**Before you change anything:**

- [ ] The project entry point exists and you've read it (`working_with_ai_agents.md` §2) — if it doesn't exist, write one from what you can reconstruct before doing anything else
- [ ] You have run the code, unchanged, and watched it work or fail (`scientific_computing_workflow.md` §3)
- [ ] You know which files are inputs, which are generated, and which are dead — not from memory, from actually opening them
- [ ] You've found (or reconstructed) the three kinds of context: what's persistent, what's authoritative, what's specific to the last thing worked on (`working_with_ai_agents.md` §1–§2)
- [ ] Environment is pinned and running, with the reasons for any non-obvious pin written down, not just the version numbers

**Before you trust anything in it:**

- [ ] A numerical baseline exists (or you've captured one) from the code as you found it, before any refactor (`scientific_computing_workflow.md` §3)
- [ ] You know what the last person actually verified versus what they assumed — these are usually not the same list

## Leaving (Task 4: releasing or handing off)

**Before someone else opens this:**

- [ ] A stranger can install it and run the primary example following only the README — actually test this, ideally on a clean environment, not from memory of how it's supposed to work
- [ ] The project entry point states current state, not history — "working on X, resume at Y," not a changelog of everything ever done (`working_with_ai_agents.md` §3)
- [ ] Every number that will reach a manuscript has a manifest entry connecting it to the commit, script, config, and output that produced it ([`../templates/results_manifest.md`](../templates/results_manifest.md))
- [ ] Private data, credentials, and anything that shouldn't be public are isolated and confirmed absent from git history, not just the working tree (`private_code_to_public_package.md` §2)
- [ ] The handoff block is written: verified git state (a commit hash, not "everything is pushed"), what's in flight, the resume point, and a decision queue of what only the receiving person can answer (`working_with_ai_agents.md` §7)

**Before you archive or stop maintaining it:**

- [ ] The full/bloated archive (large intermediate files, sensitive data, superseded history) has a named, stated location — not silently assumed to live somewhere forever (`private_code_to_public_package.md` §10)
- [ ] Anyone following a citation or a link to this repo lands somewhere that still resolves — check the links, don't assume they still do

---

## The gap this closes

Most of the individual line items above are already covered, in more depth, by the practice files this checklist cites. What a checklist adds that a practice file can't: it's the same fifteen minutes whether you're the one arriving or the one leaving, so a project can be handed off and inherited using one shared standard instead of two people's different ideas of "done."

## Using this with an AI assistant

**On inheriting a project:**

> Work through the "Receiving" half of `checklists/reproducibility_and_handoff_checklist.md` against this repository. For each item, report done / not done / cannot determine, with the evidence you checked. Do not fix anything yet — just report.

**Before a release or handoff:**

> Work through the "Leaving" half of `checklists/reproducibility_and_handoff_checklist.md`. For the install/run-the-example item, actually attempt it in a clean environment and report what broke, rather than inspecting the README and guessing it would work.
