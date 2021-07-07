from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

@app.route('/')
def start():

    url = 'http://backend:9000'

    r = requests.get(url)

    num = json.loads(r.content)

    number = num['num']

    return render_template('index.html',num=number)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
