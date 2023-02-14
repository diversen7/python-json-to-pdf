# json-to-pdf

Simple CLI tool to convert JSON to PDF.
For each indent level, a new heading is created. 
The first level is a title, the second level is a subtitle, etc.

## Installation

    git clone

## Watch

Use nodejs:

    npm install simple-file-watch -g

And then run:

    simple-file-watch --delay=1000 --extension='py,html,json' --path='.' --command='python cli.py'

Run test server:

    python -m http.server --directory html/ 