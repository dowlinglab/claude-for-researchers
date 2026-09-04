# Writing in LaTeX with Collaborators: Overleaf, GitHub, and a Local Editor

**What this is.** How to keep one real history for a manuscript that multiple people edit, when the natural tools for that (a web editor for collaboration, a local editor for speed and AI assistance) don't share a history by default.

**When to reach for it.** Any multi-author LaTeX document — a paper, a proposal, a thesis chapter with committee members reading drafts — from the first outline through submission.

**Companion reading:** [`technical_writing.md`](technical_writing.md) (drafting and revising the prose itself), [`writing_style_guide.md`](writing_style_guide.md) (voice), [`manuscript_audit.md`](manuscript_audit.md) (checking claims before you submit — the same "is this actually done" discipline this file's §4 applies to open items).

**How to read it.** Sections are numbered and stable, so you can point an agent at one (`follow §3`).

---

## 1. One manuscript, one Overleaf project, one GitHub repo

The default failure mode is a new Overleaf project for every draft, revision, or resubmission — which leaves the actual history scattered across however many project copies accumulated, none of them a real record of what changed and why.

Instead: **one writing project gets one Overleaf project, synced to one GitHub repository, for its entire life.** Name the project something you and your collaborators will still recognize in a few years, not "paper\_v2\_final". Invite collaborators to the same project rather than creating a copy for each of them.

GitHub, not Overleaf's own version history, is what you rely on for a distinct, navigable edit history — Overleaf's history is real but harder to search and doesn't survive account changes the way a repository does.

## 2. Sync often, and know what it buys you

Push from Overleaf to GitHub every time you create a real new version of a file, not just before submission. This is worth doing consistently for three concrete reasons, not just "good practice":

- **A real history you can search and diff**, in a form every collaborator's tools already understand.
- **Asynchronous work.** A collaborator without Overleaf access at that moment — no internet, or between institutions — can still get the current source from GitHub.
- **Survival past graduation.** A student's university email eventually stops working, and Overleaf projects tied to it can become orphaned. A GitHub repo owned by the group (not an individual's account) keeps the manuscript's full history accessible after anyone graduates.

Keep an `archive/` (or `graveyard/`) folder inside the project for superseded source files and figures, rather than deleting them — the same instinct as `scientific_computing_workflow.md`'s "correct in place, don't silently delete."

## 3. Editing locally: sync through GitHub, never download from Overleaf

If you prefer a local LaTeX editor to Overleaf's web interface, that's fine — but the sync direction matters. **Pull the current source from GitHub, edit locally, push back to GitHub, and let that flow into Overleaf** — don't download a one-time snapshot from Overleaf and edit it in isolation, which forks the history the moment you save.

This is exactly where an AI coding assistant earns its keep on a writing project, not just a code one: debugging a cryptic LaTeX compile error, or generating and reviewing a `latexdiff` between two versions, are both mechanical, evidence-checkable tasks a CLI-based assistant handles well — see `resources/scripts/latexdiff_check.sh` for a scriptable version of the second one.

## 4. Track open items where the reader will actually look

Use a package like `todonotes` to leave visible markers directly in the compiled PDF, rather than a separate comments document, a chat thread, or an email that a collaborator has to remember to cross-reference against the draft.

This does real work beyond just "leaving a note":

- **Sending a draft implicitly asserts "this is ready except for what's marked."** If you know something is unfinished and don't mark it, a collaborator has no way to know that from the PDF alone.
- **The draft is ready to submit once every open note is resolved** — a concrete, checkable stopping condition, not a feeling.
- **Feedback you're not addressing immediately still needs a note.** If a collaborator's comment isn't going into the next revision, say so *in the document*, or they'll repeat it next round because nothing shows it was heard.
- **When you circulate a new draft, every previous open item should be either resolved or still explicitly marked.** A comment that silently disappeared between drafts reads as ignored, even if you actually addressed it — this is the same "correct in place, don't silently delete" discipline as §2's archive folder, applied to feedback instead of source files.

## 5. What to send when you share a draft

Three things, together, every time: the current PDF, a `latexdiff` (or equivalent tracked-changes) version showing what changed since the last round, and a link to the live Overleaf project. Sending only the clean PDF makes a reviewer re-find what changed by memory; sending only the diff loses the readable version. Both, plus the live link, cost nothing extra once §1–§3 are already in place.

## Anti-patterns

- **A new Overleaf project per draft or resubmission.** Scatters the history the sync discipline in §1–§2 exists to prevent.
- **Downloading the Overleaf source to edit locally, then re-uploading it.** Forks the history at exactly the moment local editing was supposed to help.
- **Feedback tracked only in chat or email.** Nothing in the PDF shows it was heard, and nothing forces it to be resolved.
- **Deleting superseded files instead of archiving them.** The next person to ask "wait, what did this look like before?" has no way to find out.
- **Sending a draft with unresolved issues and no `todonotes` marking them.** Reads as either unaware of the issue or hoping nobody notices — neither is the intended message.

## Using this with an AI assistant

**Debugging a local compile error:**

> This LaTeX file fails to compile locally: [paste the error and the relevant few lines]. The project is synced with an Overleaf project via GitHub, so don't restructure the file layout — find the specific cause and propose the smallest fix that resolves it.

**Generating and reviewing a tracked-changes version:**

> Run `latexdiff` between the version at [last-round commit or tag] and the current draft, per `resources/scripts/latexdiff_check.sh`. Then read the resulting diff yourself and flag anything that looks like an unintended change (a reflowed paragraph that altered wording, not just line breaks) before I send it to my coauthors.

**Auditing open items before sending a draft:**

> Search this manuscript for every `\todo`/`\missingfigure`-style note. For each one, report whether it looks resolved in the current text, still open, or ambiguous. Do not resolve anything yourself — I want the inventory before I decide what still needs work.
