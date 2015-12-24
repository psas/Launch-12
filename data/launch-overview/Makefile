NOTEBOOKS=$(wildcard *.ipynb)
LATEX=$(NOTEBOOKS:.ipynb=.tex)
MARKDOWN=$(wildcard *.md)
MLATEX=$(MARKDOWN:.md=.tex)

LATEXARGS = --standalone \
            --table-of-contents \
            --include-in-header header.latex \
            --metadata=title:"Launch 12 Data Overview" \
            --metadata=author:"Portland State Aerospace Society"

all: pdf

latex: $(MLATEX) $(LATEX)
	pandoc $(LATEXARGS) *.tex -f latex --parse-raw  -t latex > launch-overview.tex

pdf: latex
	pdflatex launch-overview.tex
	pdflatex launch-overview.tex

%.tex: %.md
	pandoc $^ -f markdown --parse-raw -t latex -o $@

%.tex: %.ipynb
	ipython nbconvert --execute --config ipython_convert.py --to=latex --template=nb-latex.tplx $^

cleanpdf:
	rm -f *.aux *.log *.log *.toc *.out

clean:
	rm -f $(LATEX)
	rm -f $(MLATEX)
	rm -rf *_files/
	rm -f launch-overview.*
