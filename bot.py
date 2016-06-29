from test import *

from flask import Flask, request, Response, jsonify
import json
import requests
import os

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

@app.route("/check", methods = ['POST'])
def interact(url = None):
    if request.method == 'POST':
    	url = request.args.get('url', '')
    	output = doIt(url)
    	j = {'trump_present' : output}
    	return jsonify(**j)

@app.route('/')
def hello():
    return "hello"

# launch
if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0')
