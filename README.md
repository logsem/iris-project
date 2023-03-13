# iris-project

## How do I update the site?

Updating is just a matter of commiting and pushing your changes. Github-pages will automatically observe the change and in a matter of seconds the main home-page will be updated. 

## How do I test the site locally?

Assuming you have a working and decently recent Ruby installation with `bundler` (`gem install bundler`) you should be able to set everything up by running at the root of the repository to install all dependencies (including Jekyll).
```bash
bundle config set --local path '.bundle'
bundle update
```
You should then be able to run the following command to have Jekyll serve the site at [http://127.0.0.1:4000](http://127.0.0.1:4000).
```bash
bundle exec jekyll serve
```

Alternately, you can use Docker (and Docker Compose). Run `docker-compose up
--build` to build and run the container, then navigate to `localhost:4000`.

## How to add publications

To add a new publication simply edit `_data/publications.json`, find
```json
  "publications": [
```
and insert a new entry of the following form right below it.
```json
    {
      "title": "Strong Logic for Weak Memory: Reasoning About Release-Acquire Consistency in Iris",
      "authors": [
        "Jan-Oliver Kaiser",
        "Hoang-Hai Dang",
        "Derek Dreyer",
        "Ori Lahav",
        "Viktor Vafeiadis"
      ],
      "where_published": "In ECOOP 2017: European Conference on Object-Oriented Programming",
      "awards": [ "ECOOP 2017 Distinguished Paper Award" ],
      "dblp_url": "https://dblp.uni-trier.de/rec/conf/ecoop/KaiserDDLV17.html",
      "pdf_url": "http://drops.dagstuhl.de/opus/volltexte/2017/7275/pdf/LIPIcs-ECOOP-2017-17.pdf",
      "other_urls": [
        { "name": "website", "url": "http://plv.mpi-sws.org/igps" }
      ]
    },
```

The `"awards"`, `"dblp_url"` and `"other_urls"` fields are optional.

The `"dblp_url"` field should only be included if a DBLP entry exists for the paper. The URL is the one of the DBLP page where you can view the bibtex entry for the paper (without any GET data, so just cut at the `?`).

A similar method can be used to insert a draft papers, PhD dissertations and other stuff. Look for `"draft_papers"`, `"phd_dissertations"` and `"others"` respectively.

# Some useful notes on the JSON data

The bibliography data used to generate the webpage are all contained in the
JSON file `_data/publications.json`. This is the file you need to modify if
you with to add one of your publications to the webpage.

The file `_data/publications.json` contains four lists:
- `publications` containing metadata for all the publications,
- `phd_dissertations` containing metadata for all PhD dissertations,
- `draft_papers` contains metadata for all the draft papers,
- `others` contains metadata for other stuff (MSc theses, talks, ...).

## DBLP data (for possible use in the webpage)

Items under `publications` and `phd_dissertations` have, whenever available, a
field `dblp_url` giving the base DBLP url for the entry. It can be used to get
additional metadata from DBLP in several format (by replacing the extension):
- `.html` (as stored in our metadata) gives you the URL to the document's page
  on DBLP, where you can then access all the usual data,
- `.xml` gives you a XML record containing the document's metadata,
- `.bib` gives you a bibtex file for the document. Note that in this case, you
  can use the GET parameter `param` with value `0`, `1`, or `2` to control the
  version of the bibtex you get (condensed, standard, or with crossref).

# Iris logo

The sources for the Iris logo and favicon are found in the `iris-logo` folder.
The images currently used by the webpage are recorded in the `gfx` directory,
but these images are updated using the `Makefile` (just run `make` to update
the images after editing the sources). Variables in the `Makefile` are used to
control which variant of the logo and favicon are to be used.
