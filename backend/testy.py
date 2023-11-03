import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost/"
os.environ["SPOTIPY_CLIENT_ID"] = "18e4421b16cc40a3a4da722568760bda"
os.environ["SPOTIPY_CLIENT_SECRET"] = "b004e1a1c2f1404892dd60f47e717563"

get_songs_from_playlist_uri = 'spotify:playlist:3hkPZB2uv17vQSudT6EBgo'

scope = "playlist-modify-public"
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="18e4421b16cc40a3a4da722568760bda", client_secret="b004e1a1c2f1404892dd60f47e717563", redirect_uri="http://localhost/", scope="playlist-modify-public"))
creds = SpotifyOAuth(scope=scope, client_id="18e4421b16cc40a3a4da722568760bda", client_secret="b004e1a1c2f1404892dd60f47e717563", redirect_uri="http://localhost/")
sp = spotipy.Spotify(auth_manager=creds)
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

print(f"Fetching songs from playlist id: {get_songs_from_playlist_uri}")
results = spotify.playlist(get_songs_from_playlist_uri)
# print(results)
items = results["tracks"]['items']
names = []
uris = []

for each in items:
    names.append(each["track"]["name"])
    uris.append(each["track"]["uri"])
    
print(names)
print(uris)

playlist_name = "wowow"
username = "313zhz5rxhviwdzleb5iw5unwf3q"


# token = creds.get_cached_token
created_playlist = sp.user_playlist_create(username, playlist_name, public=True, collaborative=True)
playlist_id = created_playlist['id']
share_link = created_playlist['external_urls']['spotify']

print(f"Share link: {share_link}")
print(f"Songs added to: {playlist_name} id: {playlist_id}")

sp.playlist_add_items(playlist_id, uris)