import logging
from flask import Flask, request
app = Flask(__name__)

votes = {}


@app.route('/', methods=['POST', 'GET'], defaults={'path': ''})
@app.route('/<path:path>', methods=['POST', 'GET'])
def index(path):
    print(path)
    return "True"


app.run(host='0.0.0.0')
