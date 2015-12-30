NOTEBOOKS=$(wildcard *.ipynb)
LATEX=$(NOTEBOOKS:.ipynb=.tex)
NBMARKDOWN=$(NOTEBOOKS:.ipynb=.md)
MARKDOWN=$(wildcard *.md)
MLATEX=$(MARKDOWN:.md=.tex)

LATEXARGS = --standalone \
            --table-of-contents \
            --chapters \
            --include-in-header formatting/header.latex \
            --metadata=title:"Launch 12 Data Overview" \
            --metadata=author:"Portland State Aerospace Society" \
            --metadata=date:"January 01, 2016"

all: pdf

pdf: $(MLATEX) $(LATEX)
	pandoc $(LATEXARGS) *.tex -f latex --parse-raw  -o launch-overview.pdf

%.tex: %.md
	pandoc $^ -f markdown --parse-raw -t latex -o $@

%.tex: %.ipynb
	ipython nbconvert --execute --config formatting/ipython_convert.py --to=latex --template=formatting/nb-latex.tplx $^

cleanpdf:
	rm -f *.aux *.log *.log *.toc *.out

clean:
	rm -f $(LATEX)
	rm -f $(MLATEX)
	rm -f $(NBMARKDOWN)
	rm -rf *_files/
	rm -f launch-overview.*
