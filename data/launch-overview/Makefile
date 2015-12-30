NOTEBOOKS=$(wildcard *.ipynb)
LATEX=$(NOTEBOOKS:.ipynb=.tex)
NBMARKDOWN=$(NOTEBOOKS:.ipynb=.md)
MARKDOWN=$(wildcard *.md)
MLATEX=$(MARKDOWN:.md=.tex)

LATEXARGS = --standalone \
            --table-of-contents \
            --chapters \
            --include-in-header header.latex \
            --metadata=title:"Launch 12 Data Overview" \
            --metadata=author:"Portland State Aerospace Society"

MARKARGS  = --standalone

all: pdf

pdf: $(MLATEX) $(LATEX)
	pandoc $(LATEXARGS) *.tex -f latex --parse-raw  -o launch-overview.pdf

markdown: $(NBMARKDOWN)
	cat *.md > README.markdown
	sed -i -- 's/.pdf/.png/g' README.markdown
	rm $(NBMARKDOWN)

%.tex: %.md
	pandoc $^ -f markdown --parse-raw -t latex -o $@

%.tex: %.ipynb
	ipython nbconvert --execute --config ipython_convert.py --to=latex --template=nb-latex.tplx $^

%.md: %.ipynb
	ipython nbconvert --execute --config ipython_convert.py --to=markdown --template=markdown.tpl $^


cleanpdf:
	rm -f *.aux *.log *.log *.toc *.out

clean:
	rm -f $(LATEX)
	rm -f $(MLATEX)
	rm -rf *_files/
	rm -f launch-overview.*
