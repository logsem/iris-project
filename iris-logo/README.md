# The Iris Logo

## Logo

The official logo can be obtained, in SVG form, via

    latexmk logo

This will produce the SVG by first compiling to DVI then to SVG using `dvisvgm`.
Alternatively, by running

    latexmk -pdf logo

one gets a PDF and an SVG obtained by running `pdf2svg`.

To clean up:

    latexmk -c logo # gets rid of auxiliary files (including DVI and PDF)
    latexmk -C logo # gets rid of SVG output too


## Favicon

Similar commands deal with the favicon:

    latexmk favicon # produce favicon.svg via dvisvgm
    latexmk -pdf favicon # produce favicon.svg via pdf2svg
    
    # for old browsers:
    convert favicon.pdf favicon.ico
    # Converting to ico from pdf yields better results in my tests

    latexmk -c favicon # clean auxiliary files
    latexmk -C favicon # clean output too


## Design folder

The `design` folder contains the LaTeX/TikZ sources used to experiment with designs of the logo/favicon.
They offer various parameters and switches to produce variants of the logo.
They are preserved here for archive and in case of a redesign.