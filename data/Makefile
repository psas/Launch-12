NOTEBOOKS=$(wildcard *.ipynb)
MARKDOWN=$(NOTEBOOKS:.ipynb=.md)

HTMLARGS =  --standalone \
            --number-sections \
            --table-of-contents

LATEXARGS = --standalone \
            --chapters \
            --table-of-contents



all: data-unwrap $(MARKDOWN)


html: data-unwrap  $(MARKDOWN)
	pandoc $(HTMLARGS) *.md > book.html

latex: data-unwrap $(MARKDOWN)
	pandoc $(LATEXARGS) *.md -t latex > book.tex

pdf: latex
	pdflatex book.tex
	pdflatex book.tex

data-unwrap: fc-data tele-data

fc-data:
	mkdir -p fc-data
	cd fc-data; log2csv ../LAUNCH/flightcomputer.log

tele-data:
	mkdir -p tele-data
	cd tele-data; log2csv ../LAUNCH/telemetry.log

%.md: $(NOTEBOOKS)
	ipython nbconvert --execute --to=markdown --config ipython_convert.py --template=output-format.tlp $^

cleanpdf:
	rm -f *.aux *.log *.log *.toc *.out

clean:
	rm -f $(MARKDOWN)
	rm -f book.*
