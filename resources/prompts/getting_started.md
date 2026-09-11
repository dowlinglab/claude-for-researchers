# Prompt: get started with this repo, for you specifically

For right after you clone this repo. Point any chatbot or coding assistant at it — Claude, ChatGPT, Gemini, Codex, whatever you already have access to — and get advice scoped to your actual project instead of a generic tour of the folder.

**What it does not do:** hand you a one-size-fits-all checklist. It asks about your project first, then points at the specific practice files that match where you actually are — a student six months from a defense needs different pages than one who just inherited a folder of scripts.

**Companion reading:** [`../README.md`](../README.md) has the full map of what's in this repo, if you want to browse first instead of asking.

---

## Explore the repo, then connect it to your research

Create a Claude or ChatGPT account and a GitHub account. Install GitHub Desktop
and your choice of Claude or ChatGPT. Clone this repository with GitHub Desktop,
then open the folder in an agent that can read local files and paste:

```text
Explore this repository and explain its main resources.
Then use "The prompt" in resources/prompts/getting_started.md
to interview me about my research and recommend where to start.
Do not edit any files yet.
```

Inspect the resources the agent points to, then answer its questions about your
project. The goal is to leave with a few resources that fit your next work session.
If you use a chat window without file access, follow the file-pasting instructions below.

## The prompt

```markdown
# Task: help me get started with the resources in this repo

I just cloned this repository (github.com/dowlinglab/claude-for-researchers)
after a seminar on using AI assistants in research. I want advice specific
to my own project, not a generic tour of the folder.

## How we work

1. If you can browse or read files directly, start with `resources/README.md`
   — it maps every file to what it's for. If you can't read files (a plain
   chat window with no attachments), ask me to paste in `resources/README.md`
   and whichever specific file ends up being relevant, once we know which
   one that is.
2. Ask me the questions below, one at a time or a few at a time — however
   feels natural. Don't move to recommendations until you have real
   answers, not guesses.
3. Then recommend 2-4 specific files from this repo that match my actual
   situation, in priority order, and say why each one first.

## Questions to ask me

1. In one or two sentences, what is my research project actually about?
2. What stage is it at: brand new, inherited from someone else, actively
   running, or wrapping up toward a paper/proposal/thesis chapter?
3. Is the code (if there is code) already under version control? If yes,
   where does it live?
4. Do I already have a file an AI assistant reads for context (a
   `CLAUDE.md`, `AGENTS.md`, or similar), or does every conversation start
   from zero?
5. What AI tools do I currently use, if any — a chat window, a coding
   assistant, both, neither?
6. What is genuinely frustrating me right now about this project? (Not
   what I think I "should" be struggling with — what actually is.)
7. Is my next real deliverable a paper, a proposal, a released package, a
   thesis chapter, or something else?
8. Do I work on this mostly alone, or with active collaborators?
9. Is there anything about this project — unpublished data, sponsor-
   restricted results, a collaborator's unreleased code — that you should
   treat as sensitive and not suggest posting, uploading, or sharing
   anywhere as part of your advice?
10. If this went well, what would be different about how I work on this a
    month from now?

## After the questions

- Name the 2-4 files in `resources/` (practices, prompts, templates, or
  scripts) that fit best, in the order I should look at them.
- For each, say in one sentence what it would actually change about my
  next work session — not a summary of what the file contains.
- If nothing in this repo fits my situation well, say so directly rather
  than forcing a recommendation.
```

---

## Notes on using it

**Answer 9 honestly.** This repo's own resources exist partly to teach that discipline — see [`../practices/scientific_computing_workflow.md`](../practices/scientific_computing_workflow.md) and the data-classification guidance from the seminar itself. An assistant can only respect a boundary you actually state.

**If your assistant can't read files at all,** the conversation still works — paste in `resources/README.md` first, then whichever specific practice/prompt file it recommends once you both know what you're looking for. The questions matter more than the file access.

**This is a starting conversation, not a one-shot fix.** The point is to leave with 2-4 specific files worth reading, not a finished plan. Come back to this prompt again in a few months — question 2's answer will have changed.
