from flask import Flask
app = Flask(__name__)

votes = {}


@app.route('/')
def home():
    return "QQQ"


app.run()
