FAVICON=favicon
LOGO=official-logo

all: gfx/favicon.svg gfx/logo.svg
.PHONY: all

iris-logo/%.pdf: iris-logo/%.tex
	cd iris-logo && pdflatex $(notdir $<)

iris-logo/%.svg: iris-logo/%.pdf
	pdf2svg $< $@

gfx/favicon.svg: iris-logo/${FAVICON}.svg
	cp $< $@

gfx/logo.svg: iris-logo/${LOGO}.svg
	cp $< $@

clean:
	rm -f iris-logo/*.aux iris-logo/*.log iris-logo/*.svg iris-logo/*.pdf
.PHONY: clean
