from flask import *
import random

app = Flask(__name__)

@app.route('/ping')
def ping_pong():

    return jsonify({"ping":"pong"})

@app.route('/')
def start():

    num = random.randint(0,100)

    return jsonify({"num":num})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=9000, debug=True)
