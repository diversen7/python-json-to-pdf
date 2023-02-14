# python-json-to-pdf

Simple CLI tool to convert JSON to PDF.
For each indent level, a new heading is created. 
The first level is a `<h1>`, the second level is a `<h2>`, etc.

The generatd HTML is then converted to PDF using [wkhtmltopdf](https://wkhtmltopdf.org/).

## Installation

    git clone git@github.com:diversen7/python-json-to-pdf.git

    cd python-json-to-pdf

    virtualvenv venv

    source venv/bin/activate
    
    pip install -r requirements.txt

## Usage example

[cli.py](cli.py) is an example of how to use the cli.py script.

    python cli.py

## Watch

Use nodejs:

    npm install simple-file-watch -g

And then run (something like this):

    simple-file-watch --delay=1000 --extension='py,html,json' --path='.' --command='python cli.py'

View generated HTML:

    python -m http.server --directory output/

# License

MIT ©
