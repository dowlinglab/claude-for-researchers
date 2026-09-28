LATEXMK ?= latexmk
.PHONY: all part1 part2 combined clean
all: part1 part2
part1 part2:
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error $@.tex
combined:
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error main.tex
clean:
	$(LATEXMK) -c part1.tex part2.tex main.tex
