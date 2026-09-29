# Two session decks share main.tex and sections/.
MAIN ?= main

.PHONY: all part1 part2 combined notes watch clean distclean
all: part1 part2

part1:
	latexmk -pdf part1.tex

part2:
	latexmk -pdf part2.tex

combined:
	latexmk -pdf main.tex

# Instructor copies with each frame's speaker notes beside it. Not part of `all`.
notes:
	for n in 1 2; do \
	  latexmk -pdf -jobname=part$${n}_notes \
	    -pdflatex='pdflatex -interaction=nonstopmode -halt-on-error -file-line-error %O "\def\shownotes{1}\input{%S}"' \
	    part$${n}.tex || exit 1; \
	done

watch:
	latexmk -pdf -pvc $(MAIN).tex

clean:
	latexmk -c main.tex part1.tex part2.tex

distclean:
	latexmk -C main.tex part1.tex part2.tex
	rm -f part1_notes.* part2_notes.*
