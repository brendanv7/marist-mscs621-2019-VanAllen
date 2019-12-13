import os
from urllib.parse import urlparse
import json

from flask import Flask
from flask import render_template
from flask import request

import redis

app = Flask(__name__)
port = int(os.getenv('PORT', 8000))

if 'VCAP_SERVICES' in os.environ:
    vcap_services = json.loads(os.environ['VCAP_SERVICES'])
    if 'databases-for-redis' in vcap_services:
        credentials = vcap_services['databases-for-redis'][0]['credentials']
        redis_conn = credentials['connection']['rediss']
        connection_string = redis_conn['composed'][0]

parsed = urlparse(connection_string)

r = redis.StrictRedis(
    host=parsed.hostname,
    port=parsed.port,
    password=parsed.password,
    ssl=True,
    ssl_ca_certs='09c041b8-5c74-11e9-ac1d-12d9018fe92f',
    decode_responses=True)


@app.route('/')
# top-level page display
def serve_page():
    return render_template('index.html')


@app.route('/words', methods=['PUT'])
def handle_words():
    r.hset("words", request.form['word'], request.form['definition'])
    return ('', 204)


@app.route('/words', methods=['GET'])
def display_find():
    cursor_obj = r.hgetall('words')

    keys_list = list(cursor_obj.keys())
    values_list = list(cursor_obj.values())

    results_list = [{'word': word, 'definition': definition}
        for word, definition in zip(keys_list, values_list)]

    return json.dumps(results_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
