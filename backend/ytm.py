from ytmusicapi import YTMusic
import utils

yt = YTMusic('oauth.json')


def getTracks(oldPlaylistId):
  res = yt.get_playlist(oldPlaylistId)
  tracks = []
  for track in res['tracks']:
    yt_title = track["title"]
    yt_artist = track["artists"][0]["name"]
    song = utils.clean_song_info(utils.Song(yt_artist, yt_title))
    tracks.append(song)
  return tracks
    

def createPlaylist(tracks, newPlaylistName):
  playlistId = yt.create_playlist(newPlaylistName, '', 'PUBLIC')
  
  Ids = []  
  for song in tracks:
    query = song.artist + song.title
    tracks_found = yt.search(query, limit=1, filter='songs')
    if(tracks_found): 
      temp = tracks_found[0]['videoId']
      print(temp)
      # yt.add_playlist_items(playlistId, [temp])
      Ids.append(temp)
          
  yt.add_playlist_items(playlistId, Ids)
  return f"https://music.youtube.com/playlist?list={playlistId}"

# print(getTracks("PLgOz3T0yuNAdauvB1xdDXMGq9A5a_wmFw"))