#!/usr/bin/python3
import sys, csv, re, string
from html import escape
from datetime import date
from itertools import groupby
# usage: python3 generate.py speakers.csv >schedule.html

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

def display_time(time):
    return time.split('-', 1)[0].split(' ', 1)[0]

def label_text(html):
    label = re.sub('<[^>]+>', '', html).strip()
    return label.rstrip(':')

class Talk:
    name = None
    affil = None
    title = None
    day = None
    time = None
    html = None

# encoding='utf-8-sig' is required if the CSV file has a BOM prefix U+FEFF
# encoding='utf-8' can be used otherwise
f = csv.reader(open(sys.argv[1], newline='', encoding='utf-8-sig'), delimiter=';')
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
        (day, time) = time.split(' ', 1)
        talk.day = date.fromisoformat(day)
        talk.time = time
        talks.append(talk)

talks.sort(key = lambda talk: talk.day)
for (day, day_talks) in groupby(talks, lambda talk: talk.day):
    print(f"<h3>{day:%A (%-d %B)}</h3>")
    print('<table class="schedule">')
    print('<colgroup><col class="schedule-time-col"><col class="schedule-rule-col"><col></colgroup>')
    print("<tbody>")
    day_talks = sorted(day_talks, key = lambda talk: talk.time)
    for talk in day_talks:
        classes = ["schedule-row"]
        if talk.title:
            classes.append("schedule-talk")
            is_invited = label_text(talk.html) == "Invited talk"
            if is_invited:
                classes.append("schedule-invited")
            id = mk_id(talk.name)
            speaker = escape(talk.name)
            if talk.affil:
                speaker += f" ({escape(talk.affil)})"
            title_class = "schedule-title"
            if talk.title == "TBD":
                title_class += " schedule-tba"
            print(f'<tr class="{" ".join(classes)}">')
            print(f'<th scope="row" class="schedule-time">{escape(display_time(talk.time))}</th>')
            print('<td class="schedule-rule"><span></span></td>')
            print('<td class="schedule-detail">')
            print('<div class="schedule-line">')
            if talk.html and not is_invited:
                print(f'<span class="schedule-kind">{escape(label_text(talk.html))}</span><span class="schedule-separator"> &middot; </span>', end='')
            print(f'<span class="schedule-speaker">{speaker}</span>: ')
            print(f'<span class="{title_class}">{escape(talk.title)}</span>', end='')
            if is_invited:
                print(' <span class="schedule-kind">(invited talk)</span>', end='')
            if talk.abstract:
                print(f" <a href=\"#{id}\" data-bs-toggle=\"collapse\">[abstract]</a>")
            if talk.slides:
                url = talk.slides if talk.slides.startswith("https://") else "slides/"+talk.slides
                print(f"<a href=\"{url}\">[slides]</a>")
            print("</div>")
            # nested div makes the show/hide animation properly smooth
            if talk.abstract:
                print(f"<div id=\"{id}\" class=\"collapse\"><div class=\"abstract\">{talk.abstract}</div></div>")
            print("</td>")
            print("</tr>")
        else:
            classes.append("schedule-event-row")
            print(f'<tr class="{" ".join(classes)}">')
            print(f'<th scope="row" class="schedule-time">{escape(display_time(talk.time))}</th>')
            print('<td class="schedule-rule"><span></span></td>')
            print(f'<td class="schedule-detail"><div class="schedule-event">{talk.html}</div></td>')
            print("</tr>")
    print("</tbody>")
    print("</table>")
