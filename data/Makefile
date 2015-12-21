NOTEBOOKS=$(wildcard *.ipynb)
MARKDOWN=$(NOTEBOOKS:.ipynb=.markdown)

HTMLARGS =  --standalone \
            --number-sections \
            --table-of-contents

LATEXARGS = --standalone \
            --chapters \
            --table-of-contents



all: $(MARKDOWN)


html: $(MARKDOWN)
	pandoc $(HTMLARGS) *.md > book.html

latex: $(MARKDOWN)
	pandoc $(LATEXARGS) *.md -t latex > book.tex

pdf: latex
	pdflatex book.tex
	pdflatex book.tex

%.markdown: $(NOTEBOOKS)
	ipython nbconvert --execute --to=markdown $^

cleanpdf:
	rm -f *.aux *.log *.log *.toc *.out

clean:
	rm -f $(MARKDOWN)
	rm -f book.*
