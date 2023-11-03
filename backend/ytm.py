from ytmusicapi import YTMusic
from dataclasses import dataclass
import re

yt = YTMusic('oauth.json')

@dataclass
class Song:
    artist: str
    title: str


def clean_song_info(song: Song) -> Song:
    artist, title = song.artist, song.title
    title = re.sub('\(.*', '', title)          # Remove everything after '(' including '('
    title = re.sub('ft.*', '', title)          # Remove everything after 'ft' including 'ft'
    title = re.sub(',.*', '', title)           # Remove everything after ',' including ','
    artist = re.sub('\sx\s.*', '', artist)     # Remove everything after ' x ' including ' x '
    artist = re.sub('\(.*', '', artist)        # Remove everything after '(' including '('
    artist = re.sub('ft.*', '', artist)        # Remove everything after 'ft' including 'ft'
    artist = re.sub(',.*', '', artist)         # Remove everything after ',' including ','
    return Song(artist.strip(), title.strip())  # Remove whitespaces from start and end

def getTracks(oldPlaylistId):
  res = yt.get_playlist(oldPlaylistId)
  tracks = []
  for track in res['tracks']:
    yt_title = track["title"]
    yt_artist = track["artists"][0]["name"]
    song = clean_song_info(Song(yt_artist, yt_title))
    tracks.append(song)
  return tracks

def createPlaylist(tracks, newPlaylistName):
  playlistId = yt.create_playlist(newPlaylistName, '', 'PUBLIC')
          
  yt.add_playlist_items(playlistId, tracks)
  return f"https://www.youtube.com/playlist?list={playlistId}"

# print(getTracks("PLgOz3T0yuNAdauvB1xdDXMGq9A5a_wmFw"))