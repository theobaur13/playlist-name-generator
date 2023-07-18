from app import app
from flask import render_template, redirect, url_for, request
from app.apple_music import get_token, time
from app.forms import RefreshButton, PickPlaylistButton, HomeButton
from app.gpt import generate_playlist_name
from keys import apple_secret_key, apple_key_id, apple_team_id
import os

@app.route('/', methods=['GET', 'POST'])
def home():
    access_token = check_token()

    if request.method == 'POST':
        try:
            return redirect(url_for("playlists"))
        except:
            return redirect(url_for("home"))
    return render_template('home.html', access_token=access_token)

@app.route("/playlists")
def playlists():
    access_token = check_token()
    return render_template("playlists.html", access_token=access_token)

@app.route("/playlist/<id>", methods=["GET", "POST"])
def playlist(id):
    refresh_button = RefreshButton()
    pick_playlist_button = PickPlaylistButton()
    home_button = HomeButton()

    access_token = check_token()

    if refresh_button.validate_on_submit():
        return redirect(url_for("playlist", id=id))

    return render_template("playlist.html", access_token=access_token, refresh_button=refresh_button, pick_playlist_button=pick_playlist_button, home_button=home_button, playlist_id=id)

@app.route("/process_tracks", methods=["POST"])
def process_tracks():
    playlist_info = request.get_data(as_text=True)
    playlist_name = generate_playlist_name(playlist_info)
    return playlist_name

def check_token():
    token = os.getenv("DEVELOPER_TOKEN")
    expiry = os.getenv("EXPIRY")

    if token is None or expiry is None or int(expiry) < int(time.time()):
        new_token = get_token(apple_secret_key, apple_key_id, apple_team_id)
        token, expiry = new_token["token"], new_token["expiry"]
        os.environ["DEVELOPER_TOKEN"] = token
        os.environ["EXPIRY"] = str(expiry)
    return token