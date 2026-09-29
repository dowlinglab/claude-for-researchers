# Two session decks share main.tex and sections/.
MAIN ?= part1_slides

.PHONY: all part1 part2 runsheets watch clean distclean
all: part1 part2

part1:
	latexmk -pdf part1_slides.tex

part2:
	latexmk -pdf part2_slides.tex

# One-page facilitator run sheets, for printing. Not part of `all` or the release.
runsheets:
	latexmk -pdf -outdir=run_sheets run_sheets/part1_run_sheet.tex run_sheets/part2_run_sheet.tex

watch:
	latexmk -pdf -pvc $(MAIN).tex

clean:
	latexmk -c part1_slides.tex part2_slides.tex
	latexmk -c -outdir=run_sheets run_sheets/part1_run_sheet.tex run_sheets/part2_run_sheet.tex

distclean:
	latexmk -C part1_slides.tex part2_slides.tex
	latexmk -C -outdir=run_sheets run_sheets/part1_run_sheet.tex run_sheets/part2_run_sheet.tex
