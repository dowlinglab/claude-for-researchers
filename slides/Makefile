# Build the seminar deck.  `make` is enough; .latexmkrc handles TEXINPUTS.

MAIN := main

.PHONY: all watch clean distclean

all:
	latexmk -pdf $(MAIN).tex

# Rebuild on save, for drafting.
watch:
	latexmk -pdf -pvc $(MAIN).tex

clean:
	latexmk -c

distclean:
	latexmk -C
