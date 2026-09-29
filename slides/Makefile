# Two session decks share main.tex and sections/.
MAIN ?= part1_slides

.PHONY: all part1 part2 notes watch clean distclean
all: part1 part2

part1:
	latexmk -pdf part1_slides.tex

part2:
	latexmk -pdf part2_slides.tex

# Instructor copies with each frame's speaker notes beside it. Not part of `all`.
notes:
	for n in 1 2; do \
	  latexmk -pdf -jobname=part$${n}_slides_notes \
	    -pdflatex='pdflatex -interaction=nonstopmode -halt-on-error -file-line-error %O "\def\shownotes{1}\input{%S}"' \
	    part$${n}_slides.tex || exit 1; \
	done

watch:
	latexmk -pdf -pvc $(MAIN).tex

clean:
	latexmk -c part1_slides.tex part2_slides.tex

distclean:
	latexmk -C part1_slides.tex part2_slides.tex
	rm -f part1_slides_notes.* part2_slides_notes.*
