FAVICON=favicon
LOGO=logo

all: gfx/favicon.svg gfx/favicon.ico gfx/logo.svg
.PHONY: all

iris-logo/%.svg: iris-logo/%.tex
	cd iris-logo && latexmk $(basename $(notdir $<))

gfx/favicon.svg: iris-logo/${FAVICON}.svg
	cp $< $@

gfx/favicon.ico: iris-logo/${FAVICON}.svg
	convert $< $@

gfx/logo.svg: iris-logo/${LOGO}.svg
	cp $< $@

clean:
	cd iris-logo && latexmk -C ${FAVICON}
	cd iris-logo && latexmk -C ${LOGO}
.PHONY: clean
