NOTEBOOKS=$(wildcard *.ipynb)
MARKDOWN=$(NOTEBOOKS:.ipynb=.md)

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

fc-data:
	mkdir -p fc-data
	cd fc-data; log2csv ../LAUNCH/flightcomputer.log

%.md: fc-data $(NOTEBOOKS)
	ipython nbconvert --execute --to=markdown --template=output-format.tlp $^

cleanpdf:
	rm -f *.aux *.log *.log *.toc *.out

clean:
	rm -f $(MARKDOWN)
	rm -f book.*
