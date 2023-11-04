import ytm
import spot

def go(oldPlaylistID):
    tracks = ytm.getTracks(oldPlaylistID)
    shareURL = spot.createPlaylist(tracks, "goated")
    print(shareURL)

go("PLk3-z5xiI6hgUR2MQdWtnsDafXUMH1UdT")

