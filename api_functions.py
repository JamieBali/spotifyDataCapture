import os
import json
import base64
import requests

with open("tokens.json") as json_data:
    tokens_file = json.load(json_data)
    json_data.close()

access_token = tokens_file["access_token"]
refresh_token = tokens_file["refresh_token"]

header={"Authorization": ("Bearer " + access_token), "Content-Type": "application/json"}

#r = requests.put("https://api.spotify.com/v1/me/player/play", headers=header)

# https://developer.spotify.com/documentation/web-api/reference/transfer-a-users-playback
# To update with device ID of player for perpetual playback
#r = requests.put("https://api.spotify.com/v1/me/player", headers={"Authorization": ("Bearer " + access_token)}, data='''{
#    "device_ids": [
#        "<id>"
#    ]
#}''')

# https://developer.spotify.com/documentation/web-api/reference/start-a-users-playback
# intialises playback on device, then sets repeat mode to "context"
r = requests.put("https://api.spotify.com/v1/me/player/play", headers=header, data='''{
    "context_uri":"spotify:playlist:7EjYABm3jqOty0PxhzMYER",
    "offset":{
        "position":0
    },
    "position_ms":0
}''')

r = requests.put("https://api.spotify.com/v1/me/player/repeat?state=context", headers=header)

# print(r)

# print(r.content)

# r = requests.get("https://api.spotify.com/v1/me/player/devices", headers=header)
