from flask import Flask, request, jsonify
import redis

r = redis.Redis(host="ec2-34-255-23-118.eu-west-1.compute.amazonaws.com",
                port=24360, password="p4fd8396dff901c7c43ad2341e8afa136b004a47214118360491ee4d38edd6966", ssl=True, ssl_cert_reqs=None)
app = Flask(__name__)
votes = {}
l = list(range(200))
for i in range(200):
    votes[i] = 0


def initDB():
    global votes
    r.flushall()
    r.mset(votes)


@app.route('/<int:id>//<int:decision>', methods=['GET'])
def vote(id, decision):
    ip_addr = request.remote_addr
    vote = str(ip_addr) + str(id)
    if not r.exists(vote):
        r.set(vote, 0)
        if decision == 0:
            r.incr(id)
        else:
            r.incr(id + 100)
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
    for i in range(100):
        result[2*i] = int(db_res[i])
        result[2*i + 1] = int(db_res[i+100])
    return (jsonify(result))


if __name__ == '__main__':
    initDB()
    app.run()
