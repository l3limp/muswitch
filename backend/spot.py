import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from urllib.parse import quote
from dataclasses import dataclass


@dataclass
class Song:
    artist: str
    title: str

os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8080"
os.environ["SPOTIPY_CLIENT_ID"] = "c85c86b5bcd44d998917d4be40ffa6ac"
os.environ["SPOTIPY_CLIENT_SECRET"] = "b45bf7f7330c44c794c07879cf99a387"

def getTracks(playlistID):
    uri = f"spotify:playlist:{playlistID}"
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    results = spotify.playlist(uri)
    songs = results["tracks"]['items']
    tracks = []
    for song in songs:
        tracks.append(song['track']['uri'])
    return tracks

def createPlaylist(tracks, newPlaylistName):
    scope = "playlist-modify-public"
    creds = SpotifyOAuth(scope=scope, client_id="c85c86b5bcd44d998917d4be40ffa6ac", client_secret="b45bf7f7330c44c794c07879cf99a387", redirect_uri="http://localhost:8080")
    sp = spotipy.Spotify(auth_manager=creds)
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    user_id = sp.me()['id']
    created_playlist = sp.user_playlist_create(user_id, newPlaylistName)
    playlist_id = created_playlist['id']
    share_link = created_playlist['external_urls']['spotify']
    uris = []
    for song in tracks:
        search_query = quote(f'{song.artist} {song.title}')
        tracks_found = spotify.search(search_query, limit=1, type='track')
        if tracks_found:
            uris.append(tracks_found['tracks']['items'][0]['uri']) 
    sp.playlist_add_items(playlist_id, uris)
    return share_link