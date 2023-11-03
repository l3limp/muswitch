from ytmusicapi import YTMusic

yt = YTMusic('oauth.json')

# res = yt.get_playlist("PLgOz3T0yuNAfv2iEvQiM4qrroDH26Q1NL")
# tracks = []
# for track in res['tracks']:
#     print(track['title'])
#     tracks.append(track['videoId'])
# # print(res)

# playlistId = yt.create_playlist('rachit', 'test description', 'PUBLIC')
        
# yt.add_playlist_items(playlistId, tracks)
# print(f"Link of the playlist created: https://www.youtube.com/playlist?list={playlistId}")

def getTracks(playlistId):
  res = yt.get_playlist(playlistId)
  tracks = []
  for track in res['tracks']:
      print(track['title'])
      tracks.append(track['videoId'])
  return tracks

def createPLaylist(tracks):
  playlistId = yt.create_playlist('rachit', 'test description', 'PUBLIC')
          
  yt.add_playlist_items(playlistId, tracks)
  return f"https://www.youtube.com/playlist?list={playlistId}"