# The Iris Logo

This folder hosts the the *sources* for producing the Iris logo and favicon.
We provide the pre-compiled official logos in SVG, PDF and ICO formats in the `/gfx` folder:

* Logo: [SVG](../gfx/logo.svg) | [PDF](../gfx/logo.pdf)
* Icon: [SVG](../gfx/favicon.svg) | [PDF](../gfx/favicon.pdf) | [ICO](../gfx/favicon.ico)

In case of discrepancies between the formats, SVG is the authoritative source.

If you just need to include the logo in other documents we recommend using the above pre-compiled files, as the exact output from sources may depend on the versions of the LaTeX packages installed.

This folder contains the sources from which the official logos can be produced. Note however that the output may vary depending on the platform and LaTeX distribution.

The `design` folder contains the LaTeX/TikZ sources used to experiment with designs of the logo/favicon.
They offer various parameters and switches to produce (unofficial) variants of the logo.
They are preserved here as an archive and in case of a redesign.

## Compiling the Logo

The official SVG logo can be obtained using

    latexmk -dvi logo

This will produce the SVG by first compiling to DVI then to SVG using [`dvisvgm`][dvisvgm] (see below for installation notes).

The official PDF logo is obtained by running

    latexmk -pdf logo

To clean up:

    latexmk -c logo # gets rid of auxiliary files (including DVI)
    latexmk -C logo # gets rid of SVG output too

The preferred format for use in interactive media is SVG, for print material use PDF.
In the cases where a vector format is not suitable,
the SVG logo can be converted to a PNG using Export function of [Inkscape][ink].

The SVG or PDF logo can also be converted to a PNG using
[ImageMagik][magik]'s `convert`:

    convert -density 1200 logo.svg logo.png

Note that ImageMagik may use different SVG engines in different systems with varying output quality. Converting from a PDF may give better quality and more reproducible results.
For best results, use Inkscape (which has a CLI interface).

## Favicon

Similar commands deal with the favicon:

    latexmk -dvi favicon # produce favicon.svg via dvisvgm
    latexmk -pdf favicon # produce favicon.pdf

Then the SVG (or PDF) can be converted to an ICO file
for compatibility with older browsers,
using [ImageMagik][magik]'s `convert`:

    convert -density 256x256 favicon.svg -define icon:auto-resize=256,32,16 -colors 64 favicon.ico

The `density` parameter controls the resolution of the initial rasterisation,
the `icon:auto-resize` flag instructs the program to scale down the icon to the listed sizes and store the scaled versions in the ICO (storing versions of the icon at different sizes is one of the purposes of the ICO format).
The `color` parameter determines the number of distinct colors in the palette.

To convert to a PNG, follow the instructions for the logo.

To clean up:

    latexmk -c favicon # clean auxiliary files
    latexmk -C favicon # clean output too


## Installation of `dvisvgm`

The [`dvisvgm`][dvisvgm] program is shipped with TeXLive.
To work properly, however, it needs Ghostscript installed (specifically, `libgs`). If it is not installed the tool still produces an SVG but with just the letters, which can be quite confusing.
The issue is made worse by the fact that the standard way to install GhostScript on MacOs does not set up the paths in a way that [`dvisvgm`][dvisvgm] can independently find, so you need to specify the path to `libgs` in the `LIBGS` environment variable:

    brew install ghostscript
    export LIBGS=/usr/local/Cellar/ghostscript/9.53.3_1/lib/libgs.dylib

(see https://github.com/mgieseki/dvisvgm/issues/66 for reference).

[dvisvgm]: https://dvisvgm.de/
[magik]: https://imagemagick.org/index.php
[ink]: https://inkscape.org/