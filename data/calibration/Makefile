all: magnetometer.md

%.md: %.ipynb
	ipython nbconvert --execute --config=ipython_convert.py --to=markdown --template=nb-markdown.tpl $^
