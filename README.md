# json-to-pdf

Simple CLI tool to convert JSON to PDF.
For each indent level, a new heading is created. 
The first level is a <h1>, the second level is a <h2>, etc.

The generatd HTML is then converted to PDF using [wkhtmltopdf](https://wkhtmltopdf.org/).

## Installation

    git clone

## Usage example

[cli.sh](cli.sh) is an example of how to use the cli.py script.

    python cli.sh

## Watch

Use nodejs:

    npm install simple-file-watch -g

And then run:

    simple-file-watch --delay=1000 --extension='py,html,json' --path='.' --command='python cli.py'

View generated HTML:

    python -m http.server --directory html/ 
