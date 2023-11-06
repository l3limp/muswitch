import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from urllib.parse import quote
import utils
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")


os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8080"
os.environ["SPOTIPY_CLIENT_ID"] = client_id
os.environ["SPOTIPY_CLIENT_SECRET"] = client_secret

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
    creds = SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri="http://localhost:8080")
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