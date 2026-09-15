# Literature corpus

A small, verified corpus. Three sources is enough for this workshop; a hundred
unread entries is worse than three read ones.

## What is here

| File | Role |
|---|---|
| `source_manifest.csv` | One row per source: identity, access, licence, verification status, and what the source can and cannot support |
| `pdfs/` | Local PDF copies. **Git-ignored.** |
| `../report/ref.bib` | BibTeX for sources you have actually opened |
| `../docs/literature.md` | Your notes: what each source says, under what conditions, and where |

## The anchor source

One source is supplied, already verified:

> Woolf, P., et al. *Chemical Process Dynamics and Controls*, section 11.6,
> "Common Control Loops and Model for Temperature Control". Engineering
> LibreTexts, page ID 22513. Licensed CC BY 3.0.
> <https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Chemical_Process_Dynamics_and_Controls_(Woolf)/11:_Control_Architectures/11.06:_Common_control_loops_and_model_for_temperature_control>

It describes multiple steady states in an exothermic CSTR using heat-generation
and heat-removal curves, and argues which of them are stable.

Two things about it are worth noticing before you cite it.

1. **It is a course text, not a peer-reviewed article.** That does not make it
   wrong. It does mean it is the wrong thing to cite as the authority for a
   quantitative claim about a specific reactor.
2. **Its stability argument is a dynamic argument.** It compares the *rates* of
   heat generation and heat removal on either side of an intersection. Your
   computation produces a locus of steady states of the algebraic balances. The
   source's conclusion does not transfer to your results just because both
   involve three steady states — you did not do the calculation it did.

## Find two more

- **One source for the model**: governing equations, assumptions, sign
  conventions, or parameter values.
- **One source for the behavior**: multiple steady states, ignition and
  extinction, thermal runaway, stability, or a reactor application where this
  matters.

Search phrases that work: `nonisothermal CSTR multiple steady states`,
`CSTR ignition extinction diagram`, `exothermic CSTR thermal runaway`,
`continuous stirred tank reactor bifurcation`.

## Rules

1. **Verify from the document itself.** Open it. Check the title, authors, year,
   and DOI against the article, not against a search result, a citation in
   another paper, or an AI summary. Citations are copied wrong constantly, and a
   DOI that resolves to a different paper than you think is the most common way
   a reference list goes bad.
2. **Never cite a source you have not opened.** If a tool suggests a reference,
   that is a lead, not a citation. A plausible-looking reference that does not
   exist is the single most damaging thing an agent can put in your manuscript.
3. **Do not commit PDFs** unless you have checked that the licence permits
   redistribution — and even then, prefer not to. `pdfs/` is ignored for this
   reason. Commit the metadata and your notes.
4. **Record what a source cannot support**, not only what it says. That column
   is what makes the claim audit in Workshop 2 possible.

## Filling in the manifest

Every column is there because leaving it out causes a specific problem later:

- `local_filename` — which PDF on your disk you actually read.
- `doi` / `url` — the identifier you verified, not the one you assumed.
- `source_type` — peer-reviewed article, book, course text, preprint, thesis,
  software documentation. Different weights of evidence.
- `license` — decides whether the file may be redistributed.
- `verified` / `verified_by` / `verified_date` — `no` is a perfectly good value,
  and far better than a wrong `yes`.
- `relevance` — model, behavior, or application, and in one clause why.
- `notes` — conditions, parameter ranges, and the limits of what it supports.
