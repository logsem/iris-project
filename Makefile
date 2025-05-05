# This command compiles and runs the Web site locally.
# Access it at http://localhost:4000/
all:
	bundle exec jekyll serve --livereload

# This command opens the workshop's speakers.csv in Excel.
speakers:
	open -a "/Applications/Microsoft Excel.app/" workshop-2025/schedule/speakers.csv
