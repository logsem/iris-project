#!/usr/bin/python3
import sys, csv, string
from datetime import date
from itertools import groupby
# usage: python3 generate.py participants.csv >schedule.html

def find_column(header, name):
    '''Find the column named `name` and return its index'''
    idx = 0
    for column in header:
        if column == name:
            return idx
        idx += 1
    raise Exception(f"Column {name} not found")

def mk_id(name):
    return ''.join(
        filter(lambda x: x in string.ascii_letters, name)
    )

class Talk:
    name = None
    affil = None
    title = None
    day = None
    time = None
    html = None

f = csv.reader(open(sys.argv[1], newline=''))
header = next(f)

name_col = find_column(header, 'Name Tag')
affil_col = find_column(header, 'Affiliation')
title_col = find_column(header, 'title')
abstract_col = find_column(header, 'abstract')
time_col = find_column(header, 'talk_time')
slides_col = find_column(header, 'slides')
html_col = find_column(header, 'raw_html')

# output variable
talks = []

for row in f:
    talk = Talk()
    talk.name = row[name_col]
    talk.affil = row[affil_col]
    talk.title = row[title_col]
    talk.abstract = row[abstract_col]
    talk.slides = row[slides_col]
    talk.html = row[html_col]
    time = row[time_col]
    if time:
        (day, time) = time.split(' ')
        talk.day = date.fromisoformat(day)
        talk.time = time
        talks.append(talk)

talks.sort(key = lambda talk: talk.day)
for (day, day_talks) in groupby(talks, lambda talk: talk.day):
    print(f"<h3>{day:%A (%d %B)}</h3>")
    print("<ul>")
    day_talks = sorted(day_talks, key = lambda talk: talk.time)
    for talk in day_talks:
        if talk.html:
            print(f"<li>{talk.time}: {talk.html}</li>")
        else:
            id = mk_id(talk.name)
            print(f"<li>{talk.time}: {talk.name} ({talk.affil})</a>: {talk.title}")
            print(f"<a href=\"#{id}\" data-bs-toggle=\"collapse\">[abstract]</a>")
            if talk.slides:
                url = talk.slides if talk.slides.startswith("https://") else "slides/"+talk.slides
                print(f"<a href=\"{url}\">[slides]</a>")
            # nested div makes the show/hide animation properly smooth
            print(f"<div id=\"{id}\" class=\"collapse\"><div class=\"abstract\">{talk.abstract}</div></div>")
            print("</li>")
    print("</ul>")
