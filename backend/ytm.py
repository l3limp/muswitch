from ytmusicapi import YTMusic

yt = YTMusic('oauth.json')

def getTracks(oldPlaylistId):
  res = yt.get_playlist(oldPlaylistId)
  tracks = []
  for track in res['tracks']:
    #   print(track['title'])
      tracks.append(track['videoId'])
  return tracks

def createPlaylist(tracks, newPlaylistName):
  playlistId = yt.create_playlist(newPlaylistName, '', 'PUBLIC')
          
  yt.add_playlist_items(playlistId, tracks)
  return f"https://www.youtube.com/playlist?list={playlistId}"