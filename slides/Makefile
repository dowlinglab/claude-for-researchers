# Two session decks share main.tex and sections/.
MAIN ?= main

.PHONY: all part1 part2 combined watch clean distclean
all: part1 part2

part1:
	latexmk -pdf part1.tex

part2:
	latexmk -pdf part2.tex

combined:
	latexmk -pdf main.tex

watch:
	latexmk -pdf -pvc $(MAIN).tex

clean:
	latexmk -c main.tex part1.tex part2.tex

distclean:
	latexmk -C main.tex part1.tex part2.tex
