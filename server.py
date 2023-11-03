from flask import Flask
import os
import ytm

app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/meow/<From>')
def catto(From):
  tracks = ytm.getTracks(From)
  return ytm.createPLaylist(tracks)

HOST = os.environ.get('SERVER_HOST', 'localhost')
app.run(host=HOST, port=8080)
