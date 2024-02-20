from http import client
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

###
# These two need to be global
###
lastPlayed = ""
lastProgress = 0

def update(track_id, _dict):
    _dict[track_id] = _dict.get(track_id, 0) + 1
    return _dict

if __name__ == "__main__":
    data = {}
    while True:
        time.sleep(30)
        scope = 'user-read-currently-playing'

        SPOTIPY_CLIENT_ID = ""
        SPOTIPY_CLIENT_SECRET = ""

        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET),auth_manager=SpotifyOAuth(scope=scope, username='__', client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri="http://127.0.0.1:9090"))


        curr = sp.currently_playing()
        if curr["is_playing"]:
            track_id = curr["item"]["uri"]
            if track_id == lastPlayed: # current song is the last one checked
                if curr["progress_ms"] > lastProgress:
                    #progress gone forward, don't update
                    lastProgress = curr["progress_ms"]
                else:
                    data = update(track_id, data)
                    lastProgress = curr["progress_ms"]
            else:
                data = update(track_id, data)
                lastProgress = curr["progress_ms"]
                lastPlayed = track_id
        else:
            print("Nothing Playing")
        print(data)
