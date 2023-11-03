import ytm
import spot

def go(oldPlaylistID):
    tracks = spot.getTracks(oldPlaylistID)
    shareURL = ytm.createPlaylist(tracks, "goated")
    print(shareURL)

go("2KfqENKgmYIt6Sma2OWQCv")

