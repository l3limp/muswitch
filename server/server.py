from flask import Flask, request, jsonify
import os
import ytm
import spot

app = Flask('app')

@app.route('/')
def siu():
  return 'messi obv'

@app.route('/createNew')
def createNew():
  fromPlatform = request.args.get('fromPlatform', None)
  toPlatform = request.args.get('toPlatform', None)
  oldPlaylistID = request.args.get('oldPlaylistID', None)
  newPlaylistName = request.args.get('newPlaylistName', None)
  
  if fromPlatform.lower() == 'ytm' or fromPlatform.lower() == 'youtube' or fromPlatform.lower() == 'youtubemusic':
    tracks = ytm.getTracks(oldPlaylistID)
    shareURL = spot.createPlaylist(tracks, newPlaylistName)
    response = jsonify({'rez': shareURL})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
  else:
    tracks = spot.getTracks(oldPlaylistID)
    shareURL = ytm.createPlaylist(tracks, newPlaylistName)
    response = jsonify({'rez': shareURL})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

HOST = os.environ.get('SERVER_HOST', 'localhost')
app.run(host=HOST, port=8080)
