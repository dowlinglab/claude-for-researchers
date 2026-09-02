#!/usr/bin/env bash
# Verify a LaTeX revision with a word-level diff before you commit it.
#
# An AI-assisted (or human) editing pass can quietly change what a sentence
# claims -- "more than double" softened to "substantially increase", a number
# tightened, a hedge added -- in ways a normal re-read misses because the
# sentence still reads fine. This compiles a colored, word-level diff against
# the last committed version so you review exactly what changed before it
# becomes permanent. See practices/grant_proposal_writing.md #5.
#
# Usage:
#   latexdiff_check.sh main.tex                  # diff against HEAD
#   latexdiff_check.sh -r v1-submitted main.tex   # diff against a tag/ref
#   latexdiff_check.sh -o review main.tex         # name the output review-*
#   latexdiff_check.sh -k main.tex                # keep the diff .tex source
#
# Writes <basename>-diff.pdf next to MAIN_TEX (plus build byproducts, unless
# -k). Never modifies MAIN_TEX or touches git state -- read-only against the
# repository. Requires: git, latexdiff, and latexmk (or pdflatex as a
# fallback). Exits non-zero on any failure, so it can gate a commit hook.

set -euo pipefail

ref="HEAD"
out_base=""
keep_tex=0

usage() {
  sed -n '2,17p' "$0" | sed 's/^# \{0,1\}//'
  exit "${1:-0}"
}

while getopts ":r:o:kh" opt; do
  case "$opt" in
    r) ref="$OPTARG" ;;
    o) out_base="$OPTARG" ;;
    k) keep_tex=1 ;;
    h) usage 0 ;;
    \?) echo "error: unknown option -$OPTARG" >&2; usage 1 ;;
    :)  echo "error: -$OPTARG requires an argument" >&2; usage 1 ;;
  esac
done
shift $((OPTIND - 1))

if [ $# -ne 1 ]; then
  echo "error: expected exactly one argument, the .tex file to check" >&2
  usage 1
fi
main_tex="$1"

for tool in git latexdiff; do
  command -v "$tool" >/dev/null 2>&1 || {
    echo "error: '$tool' is not on PATH. Install it (TeX Live includes latexdiff)." >&2
    exit 2
  }
done
if ! command -v latexmk >/dev/null 2>&1 && ! command -v pdflatex >/dev/null 2>&1; then
  echo "error: neither 'latexmk' nor 'pdflatex' is on PATH." >&2
  exit 2
fi

[ -f "$main_tex" ] || { echo "error: '$main_tex' not found" >&2; exit 2; }

repo_root=$(git -C "$(dirname "$main_tex")" rev-parse --show-toplevel 2>/dev/null) || {
  echo "error: '$main_tex' is not inside a git repository" >&2
  exit 2
}

tex_dir=$(cd "$(dirname "$main_tex")" && pwd)
tex_name=$(basename "$main_tex")
tex_base="${tex_name%.tex}"
: "${out_base:=${tex_base}-diff}"

rel_path=$(git -C "$repo_root" ls-files --full-name "$tex_dir/$tex_name" 2>/dev/null | head -1)
if [ -z "$rel_path" ]; then
  echo "error: '$main_tex' is not tracked by git, so there is nothing to diff" \
       "against. Commit it first, or pass -r to compare two committed refs." >&2
  exit 2
fi

old_tmp=$(mktemp -t latexdiff_old.XXXXXX.tex)
trap 'rm -f "$old_tmp"' EXIT

if ! git -C "$repo_root" show "${ref}:${rel_path}" > "$old_tmp" 2>/dev/null; then
  echo "error: '${rel_path}' does not exist at ref '${ref}'." \
       "Nothing to diff against yet -- this may be the first commit of this file." >&2
  exit 2
fi

if diff -q "$old_tmp" "$main_tex" >/dev/null 2>&1; then
  echo "No changes since ${ref}: ${rel_path}. Nothing to diff."
  exit 0
fi

echo "Diffing working copy of ${rel_path} against ${ref}..."
diff_tex="${tex_dir}/${out_base}.tex"
diff_err="${tex_dir}/${out_base}.latexdiff.err"

# Run in tex_dir so \input, \bibliography, and figure paths resolve normally.
# > always creates diff_tex even on failure, so an aborted run must not leave
# a broken file behind for the next invocation to trip over.
if ! ( cd "$tex_dir" && latexdiff "$old_tmp" "$tex_name" > "$diff_tex" 2> "$diff_err" ); then
  echo "error: latexdiff failed:" >&2
  sed 's/^/  /' "$diff_err" >&2
  rm -f "$diff_tex" "$diff_err"
  exit 3
fi
rm -f "$diff_err"

echo "Compiling diff..."
compile_log="${tex_dir}/${out_base}.compile.log"
if command -v latexmk >/dev/null 2>&1; then
  ( cd "$tex_dir" && latexmk -pdf -interaction=nonstopmode -halt-on-error "${out_base}.tex" ) \
    > "$compile_log" 2>&1 || {
      echo "error: compiling the diff failed. See $compile_log" >&2
      exit 3
    }
else
  ( cd "$tex_dir" && pdflatex -interaction=nonstopmode -halt-on-error "${out_base}.tex" ) \
    > "$compile_log" 2>&1 || {
      echo "error: compiling the diff failed. See $compile_log" >&2
      exit 3
    }
fi
rm -f "$compile_log"

diff_pdf="${tex_dir}/${out_base}.pdf"
if [ ! -f "$diff_pdf" ]; then
  echo "error: expected $diff_pdf but it was not produced." >&2
  exit 3
fi

if [ "$keep_tex" -eq 0 ]; then
  rm -f "$diff_tex"
fi
# Remove latexmk/pdflatex byproducts, but never the diff PDF or (if kept) .tex.
( cd "$tex_dir" && rm -f "${out_base}".{aux,bbl,bcf,blg,fdb_latexmk,fls,log,out,run.xml,synctex.gz,toc} )

cat <<EOF

Wrote: ${diff_pdf}

Read it before you commit -- word-level additions and deletions are colored
and underlined/struck through. This is the check, not a formality: it is what
catches a softened claim, a changed number, or an accidental self-reference
that a normal re-read of the final text would not.

This diffed against '${ref}'. Consider re-running against the last
*submitted* version (a tag, if you have one) before a final submission, not
just the last commit.
EOF
