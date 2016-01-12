NOTEBOOKS=$(wildcard *.ipynb)
NBMARKDOWN=$(NOTEBOOKS:.ipynb=.md)

LATEXARGS = --standalone \
            --table-of-contents \
            --chapters \
            --metadata=title:"Launch 12 Data Overview" \
            --metadata=author:"Portland State Aerospace Society" \
            --metadata=date:"January 16, 2016"

# List the files we want to build our pdf
PDF=introduction.markdown \
    IMU.md pressure.md \
    venus.md \
    RNH.md \
    vibration.md \
    telemetrum.md \
    arts2.md \
    alt-comparison.md \
    flightcomputer.md \
    temperature.md \
    simulation.md

all: PSAS-launch-12-overview.pdf

PSAS-launch-12-overview.pdf: $(PDF)
	pandoc $(LATEXARGS) $(PDF) -f markdown -o PSAS-launch-12-overview.pdf

%.md: %.ipynb
	ipython nbconvert --execute --config=ipython_convert.py --to=markdown --template=nb-markdown.tpl $^

%.tex: %.ipynb
	ipython nbconvert --execute --config formatting/ipython_convert.py --to=latex --template=formatting/nb-latex.tplx $^

clean:
	rm -f $(NBMARKDOWN)
	rm -rf *_files/
	rm -f PSAS-launch-12-overview.pdf
