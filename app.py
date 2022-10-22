from flask import Flask, request, jsonify

app = Flask(__name__)
votes = set()
likes = [0] * 100
dislikes = [0] * 100

@app.route('/<int:id>//<int:decision>', methods=['GET'])
def vote(id, decision):
    global votes
    ip_addr = request.remote_addr
    vote = str(ip_addr) + str(id)
    if not vote in votes:
        votes.add(vote)
        if decision == 0:
            likes[id % 100] += 1
        else:
            dislikes[id % 100] += 1
    return ('', 204)


@app.route('/reset', methods=['GET'])
def reset():
    votes.clear()
    likes[:] = [0 for _ in likes]
    dislikes[:] = [0 for _ in likes]
    return ('', 204)


@app.route('/results', methods=['GET'])
def results():
    result = {}
    for i in range(1, 100):
        result[2*i-1] = likes[i]
        result[2*i] = dislikes[i]
    return (jsonify(result))


if __name__ == '__main__':
    app.run()
