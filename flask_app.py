from flask import Flask

app = Flask(__name__)
counter = {}


@app.route('/count/<key>')
def count_views(key):
    if key in counter:
        counter[key] += 1
    else:
        counter[key] = 1
    return counter[key]

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
