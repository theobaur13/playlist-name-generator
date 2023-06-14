from app import app
from flask import render_template, redirect, url_for, request, session
from app.spotify import create_oauth, get_token, spotipy
from app.forms import SubmitButton

@app.route('/', methods=['GET', 'POST'])
def home():
    button = SubmitButton()
    if button.validate_on_submit():
        oauth = create_oauth()
        auth_url = oauth.get_authorize_url()
        return redirect(auth_url)
    return render_template('home.html', button=button)

@app.route('/callback')
def callback():
    oauth = create_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = oauth.get_access_token(code)
    session["token_info"] = token_info
    return redirect(url_for("playlists"))

@app.route("/playlists")
def playlists():
    try:
        token_info = get_token()
    except:
        return redirect(url_for("home"))
    
    sp = spotipy.Spotify(auth = token_info["access_token"])
    playlists = sp.current_user_playlists()["items"]

    return render_template("playlists.html", playlists=playlists)

@app.route("/playlist/<id>")
def playlist(id):
    try:
        token_info = get_token()
    except:
        return redirect(url_for("home"))
    
    sp = spotipy.Spotify(auth = token_info["access_token"])
    playlist = sp.playlist(id)
    tracks = playlist["tracks"]["items"]
    
    return render_template("playlist.html",tracks=tracks)