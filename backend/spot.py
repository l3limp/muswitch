import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from urllib.parse import quote
import utils


os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8080"
os.environ["SPOTIPY_CLIENT_ID"] = "0d708d2325a145acb74efd84b9809139"
os.environ["SPOTIPY_CLIENT_SECRET"] = "614bfe52cdc44df880d4836d7d934800"

def getTracks(playlistID):
    uri = f"spotify:playlist:{playlistID}"
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    results = spotify.playlist(uri)
    tracks = []
    for track in results["tracks"]['items']:
        spot_title = track['track']['name']
        spot_artist = track['track']['artists'][0]['name']
        song = utils.clean_song_info(utils.Song(spot_artist, spot_title))
        tracks.append(song)
    return tracks

def createPlaylist(tracks, newPlaylistName):
    scope = "playlist-modify-public"
    creds = SpotifyOAuth(scope=scope, client_id="0d708d2325a145acb74efd84b9809139", client_secret="614bfe52cdc44df880d4836d7d934800", redirect_uri="http://localhost:8080")
    sp = spotipy.Spotify(auth_manager=creds)
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    user_id = sp.me()['id']
    created_playlist = sp.user_playlist_create(user_id, newPlaylistName)
    playlist_id = created_playlist['id']
    share_link = created_playlist['external_urls']['spotify']
    uris = []
    for song in tracks:
        # search_query = quote(f'{song.artist} {song.title}')
        tracks_found = spotify.search(song.title + song.artist, limit=1, type='track')
        if tracks_found:
            if len(tracks_found['tracks']['items']) > 0:
                uris.append(tracks_found['tracks']['items'][0]['uri']) 
    sp.playlist_add_items(playlist_id, uris)
    return share_link