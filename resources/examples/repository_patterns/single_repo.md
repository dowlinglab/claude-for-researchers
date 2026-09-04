# Repository pattern: one repo, code and reproduction together

**What this is.** A worked decision for a specific, common case: you're turning research code behind a paper into an installable package, and you're deciding whether the paper's reproduction material (figures, the specific case study, the full result archive) gets its own repository or lives inside the package repo.

**When to reach for it.** You've decided to release code as a package (see [`../../practices/private_code_to_public_package.md`](../../practices/private_code_to_public_package.md)) and are now laying out the repository itself.

---

## The real decision this is built from

Task 4 of the seminar this repo supports (`slides/sections/03_act2_build.tex`) is a git-verified conversion of a paper's research code into a public package. The repository layout decision behind it, locked on day one and never revisited, was:

- **One repo, no separate paper repo.** The private, pre-conversion research repo (bloated git history, large intermediate files) stays private as the archive of record. The paper's reproduction code migrates *into* the new public package repo — it does not get a third repo of its own.
- **Examples and paper-reproduction are repo-only, not shipped in the installed package.** Only the importable library ships in the built wheel. `examples/` holds a reusable case study built on the public API; `paper/` holds thin reproduction scripts that *import from* `examples/` rather than duplicating logic, plus a `golden/` directory of regression values and a `DATA.md` describing what's committed and what isn't. Both directories are importable in development and CI via a `sys.path` insert in `tests/conftest.py` — not via installing the package.
- **A curated data subset, not the full archive.** The figures needed a self-contained reproduction path, so a ~30–50 MB subset of plot inputs was committed to `paper/data/` — enough for anyone to regenerate every figure without the private archive. The full run (564 MB) stayed in the private predecessor repo. No third-party archive (e.g. Zenodo) was used; the private repo *is* the archive of record.

The result: one clone gets you the installable library, a runnable example, and a reproducible version of the paper's own figures — with no separate repo to keep in sync, and no ambiguity about which repo is authoritative for which artifact.

## When this is the right call

- The paper has one case study (or a small, related family) that the package's public API can express directly — the example *is* the paper's own use case, not a stand-in for it.
- The full result archive is large enough that committing it is impractical, but a small, curated subset can make the published figures self-contained.
- You want one thing to clone, one CI pipeline, one version number, and one place a reader lands when they follow a citation.

## When it's the wrong call (reach for a split instead)

- The paper's analysis genuinely doesn't share code with the package's public API — the "example" would just be a pile of one-off scripts with no home in the library's own structure.
- The manuscript itself (LaTeX source, journal-specific formatting, submission history) needs a lifecycle independent of the software's — different collaborators, different release cadence, a different license.
- The full data archive is required for reproduction and is too large or too sensitive to curate down to a committed subset.

*(A worked example of the split pattern, with the provenance-manifest connection that keeps a manuscript repo and a code repo honestly linked, is planned but not yet built — see the main [`../../README.md`](../../README.md)'s "Also planned" section.)*

## Checklist

- [ ] The package's public API can express the paper's own case study without special-casing
- [ ] `examples/` and any paper-reproduction code are excluded from the built package, but importable in dev/CI
- [ ] Paper-reproduction scripts import from `examples/` rather than re-implementing it
- [ ] A `DATA.md` (or equivalent) states exactly what data is committed, what's curated versus complete, and where the full archive lives
- [ ] The pre-conversion private repo is the named archive of record — not silently orphaned, not assumed to be permanent without saying so
- [ ] The decision is written down once, at the start (a `REFACTOR_PLAN.md`-style locked-decisions section), not re-litigated per pull request

## Using this with an AI assistant

> We're converting `<private repo path>` into a public package. Propose a repository layout following the single-repo pattern in `resources/examples/repository_patterns/single_repo.md`: what goes in `src/`, what goes in `examples/`, what (if anything) belongs in a `paper/` reproduction directory, and what data — if any — should be curated into the repo versus left in the private archive. Justify each choice against the "when this is the right call" criteria before proposing file paths.
