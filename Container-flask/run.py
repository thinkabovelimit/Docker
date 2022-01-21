#!/usr/bin/env python
# encoding: utf-8
import json
import os
from flask import Flask, jsonify, make_response, abort

app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({'version': '1.0',
                       'state': 'Application is up and running'})


all_framework_response = json.load(open(f"{os.getcwd()}/response_files/all_frame_works.json"))
framework_one_response = json.load(open(f"{os.getcwd()}/response_files/frame_work_1.json"))
framework_two_response = json.load(open(f"{os.getcwd()}/response_files/frame_work_2.json"))
cei_score_framework_one_response = json.load(open(f"{os.getcwd()}/response_files/frame_work_score_one.json"))
cei_score_framework_two_response = json.load(open(f"{os.getcwd()}/response_files/frame_work_score_two.json"))

@app.route('/api/v1/rcm/framework', methods=['GET'])
def get_all_frameworks():
    return jsonify(all_framework_response)

@app.route('/api/v1/rcm/framework/1', methods=['GET'])
def get_framework_one():
    return jsonify(framework_one_response)

@app.route('/api/v1/rcm/framework/2', methods=['GET'])
def get_framework_two():
    return jsonify(framework_two_response)

@app.route('/api/v1/rcm/framework/1/score', methods=['POST'])
def post_cei_score_frame_work_one():
    return jsonify(cei_score_framework_one_response)

@app.route('/api/v1/rcm/framework/2/score', methods=['POST'])
def post_cei_score_frame_work_two():
    return jsonify(cei_score_framework_two_response)

@app.errorhandler(405)
def not_allowed(error):
    return make_response(jsonify({'error': 'Method not allowed'}), 405)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)