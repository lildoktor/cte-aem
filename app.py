import os
import redis
from flask import Flask

app = Flask(__name__)
db=redis.from_url(os.environ['redis://default:hhzGbM0eRTNRSiXTwC8asXCAuAME0sqj@redis-16661.c242.eu-west-1-2.ec2.cloud.redislabs.com:16661'])


@app.route('/')
def hello_world():
    name=db.get('name') or'World'
    return 'Hello %s!' % name

@app.route('/setname/<name>')
def setname(name):
    db.set('name',name)
    return 'Name updated.'

if __name__ == '__main__':
    app.run()
