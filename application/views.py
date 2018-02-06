from flask import Response
from application import app
from webargs.flaskparser import use_args
from webargs import fields
import json
import os


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


quotes_args = {
    'query': fields.String(required=True)
}

file_address = os.getcwd() + '/data_collection/quotes.json'

with open(file_address, 'r') as f:
    quotes = json.load(f)


@app.route('/quotes')
@use_args(quotes_args)
def get_quotes(args):
    query = args['query']
    quote_hits = []
    # TODO Spelling isoform finding is required
    for quote in quotes:
        if query in quote['quote']:
            hit = "{} ---- Movie: {} ({})".format(quote['quote'],
                                                  quote['movie_name'],
                                                  quote['movie_year'])
            quote_hits.append(hit)
    return Response(json.dumps(quote_hits), status=200)