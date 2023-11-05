import ytm
import spot

def go(oldPlaylistID):
    tracks = spot.getTracks(oldPlaylistID)
    shareURL = ytm.createPlaylist(tracks, "ugh")
    print(shareURL)

go("00XQytNtiEhjTigH2s0WMc")

