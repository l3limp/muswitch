import ytm
import spot

def go(oldPlaylistID):
    tracks = ytm.getTracks(oldPlaylistID)
    shareURL = spot.createPlaylist(tracks, "ugh")
    print(shareURL)

go("PLp8ZPiISv8ODceSfBckot2EFg9RLJHYE6")

