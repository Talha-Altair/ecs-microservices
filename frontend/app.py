from flask import Flask, render_template
import requests
import json

URL =  'http://tram-backend-service.api:9000'

app = Flask(__name__)

@app.route('/')
def start():

    url = URL

    try:
      r = requests.get(url)
    except:
      r = requests.get('http://backend:9000')

    num = json.loads(r.content)

    number = num['num']

    return render_template('index.html',num=number)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
