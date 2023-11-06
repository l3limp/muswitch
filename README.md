# Muswitch

Converts a youtube music playlist to spotify playlist or vice-versa.

## Setup

### Spotify Developer Account

1. Create a new app: https://developer.spotify.com/dashboard
2. Set "Redirect URI" to `http://localhost:8080/`
3. Copy the "Client ID" and "Client Secret" to use later

### Setting Environment Variables

1. Create a file called `.env` in the main folder.
2. Edit the file by adding your credentials
3. The structure of the `.env` file is given below

```sh
SPOTIPY_CLIENT_ID = <your_spotify_client_id>
SPOTIPY_CLIENT_SECRET = <your_spotify_client_secret>
```

## Usage

```sh
$ cd muswitch
$ npm start
$ cd ..
$ cd server
$ python server.py
```

