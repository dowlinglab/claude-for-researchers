# The vendored ND theme lives in theme/ rather than beside main.tex, so that
# the source root stays readable. beamerthemeNotreDame.sty loads its colour
# theme by name (\usecolortheme{NotreDame}), which searches the TeX path -- so
# theme/ has to be on it.
$ENV{'TEXINPUTS'} = './theme//:' . ($ENV{'TEXINPUTS'} // '');

$pdf_mode = 1;
$pdflatex = 'pdflatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$clean_ext = 'nav snm vrb synctex.gz';
