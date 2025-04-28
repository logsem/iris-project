all:
	python3 generate.py speakers.csv >schedule.html

# Finding non-ASCII characters in speakers.csv
ascii:
	pcregrep --color='auto' -n "[\x80-\xFF]" speakers.csv
