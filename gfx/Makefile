FAVICON=favicon
LOGO=logo

all: favicon.svg favicon.ico logo.svg
.PHONY: all

../iris-logo/%.pdf: ../iris-logo/%.tex
	cd ../iris-logo && latexmk -pdf $(notdir $<)

../iris-logo/%.svg: ../iris-logo/%.tex
	cd ../iris-logo && latexmk -dvi $(notdir $<)

favicon.svg: ../iris-logo/${FAVICON}.svg
	cp $< $@

favicon.ico: ../iris-logo/${FAVICON}.svg
	convert $< $@

logo.svg: ../iris-logo/${LOGO}.svg
	cp $< $@

clean:
	rm -f ../iris-logo/*.aux ../iris-logo/*.log ../iris-logo/*.svg ../iris-logo/*.pdf favicon.svg favicon.ico logo.svg
.PHONY: clean
