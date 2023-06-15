from requests import get, post
from keys import spotify_client_id, spotify_client_secret
from app.routes import url_for, session
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import base64
import time

def get_header(token):
    return {"Authorization": "Bearer " + token}

def create_oauth():
    return SpotifyOAuth(
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        redirect_uri=url_for("callback", _external=True),
        scope="user-read-private user-read-email playlist-read-private playlist-read-collaborative"
    )

def get_token():
    token_info = session.get("token_info", None)
    if not token_info:
        raise "exception"
    now = int(time.time())
    is_expired = token_info["expires_at"] - now < 60
    if is_expired:
        sp_oauth = create_oauth()
        token_info = sp_oauth.refresh_access_token(token_info["refresh_token"])
    return token_info

# get playlist tracks (requires scope: playlist-read-private) https://developer.spotify.com/documentation/web-api/reference/playlists/get-playlists-tracks/
def get_playlist_info(playlist):
    playlist_dict = {}
    for track in playlist["tracks"]["items"]:
        artists = [artist["name"] for artist in track["track"]["artists"]]
        playlist_dict[track["track"]["name"]] = artists
    return playlist_dict
    