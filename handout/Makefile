LATEXMK ?= latexmk
.PHONY: all part1 part2 clean
all: part1 part2
part1 part2:
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error $@_handout.tex
clean:
	$(LATEXMK) -c part1_handout.tex part2_handout.tex
