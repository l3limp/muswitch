from flask import Flask, request
import os
import ytm

app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/createNew')
def createNew():
  fromPlatform = request.args.get('fromPlatform', None)
  toPlatform = request.args.get('toPlatform', None)
  oldPlaylistID = request.args.get('oldPlaylistID', None)
  newPlaylistName = request.args.get('newPlaylistName', None)
  
  #this is ytm to ytm only abhi, if else daalna padega
  tracks = ytm.getTracks(oldPlaylistID)
  return ytm.createPlaylist(tracks, newPlaylistName)

HOST = os.environ.get('SERVER_HOST', 'localhost')
app.run(host=HOST, port=8080)
