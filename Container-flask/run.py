#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({'version': '1.0',
                       'state': 'Application is up and running'})
app.run(host="0.0.0.0")