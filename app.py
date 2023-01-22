from flask import Flask, request, jsonify
import redis

r = redis.Redis(host="redis-17001.c226.eu-west-1-3.ec2.cloud.redislabs.com",
                port=17001, password="fPvlGTuJe7kWPbAxDlzHE8CF2GGInGgQ")
app = Flask(__name__)
votes = {}
l = list(range(50))
for i in range(50):
    votes[i] = 0


def initDB():
    global votes
    r.flushall()
    r.mset(votes)


@app.route('/<int:id>//<int:decision>', methods=['GET'])
def vote(id, decision):
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    vote = str(ip_addr) + str(id)
    if not r.exists(vote):
        r.set(vote, 0)
        if decision == 0:
            r.incr(id)
        else:
            r.incr(id + 25)
    return ('', 204)


@app.route('/reset', methods=['GET'])
def reset():
    initDB()
    return ('', 204)


@app.route('/results', methods=['GET'])
def results():
    global l
    result = {}
    db_res = r.mget(l)
    for i in range(25):
        result[2*i] = int(db_res[i])
        result[2*i + 1] = int(db_res[i+25])
    return (jsonify(result))


if __name__ == '__main__':
    initDB()
    app.run()
