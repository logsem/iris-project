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
