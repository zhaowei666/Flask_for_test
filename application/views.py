from flask import Response
from application import app
from webargs.flaskparser import use_args
from webargs import fields
import json
import os
import operator


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
    query = args['query'].lower().split(' ')
    query_words = [w for w in query if w]
    quote_hits = []
    print query_words
    # TODO Spelling isoform finding is required
    for quote in quotes:
        quote_words = quote['text'].lower().split(' ')
        score = 0
        for word in query_words:
            if word in quote_words:
                score += 1
        if score:
            quote['score'] = score / len(query_words)
            quote_hits.append(quote)
    quote_hits.sort(key=operator.itemgetter('score'), reverse=True)

    return Response(json.dumps(quote_hits), status=200)
