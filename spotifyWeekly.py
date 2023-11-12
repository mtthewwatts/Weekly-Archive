# man this is crazy
# ladadiiiii ladadaaaaaa

import spotipy
import time #importing time library ?? ?? ? ? ? ? ?? ? 
from spotipy.oauth2 import SpotifyOAuth

from flask import Flask, request, url_for, session, redirect

# everything is flashing red because it's unused, i think it's fine
# also ran pip install flask spotipy in terminal

app = Flask(__name__)

app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'

app.secret_key = 'aowihOAWIDHaowidhAs38q92'

TOKEN_INFO = 'token_info' #constant set to token info string

@app.route('/')
def login():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirect_page():
    session.clear()
    code = request.args.get('code')
    token_info = create_spotify_oath().get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('save_discover_weekly', external = True))

@app.route('/saveDiscoverWeekly')
def save_discover_weekly():
    try:
        token_info = get_token()
    except:
        print("User not logged in")
        return redirect('/')
    
    return ("OAUTH SUCCESSFUL")


def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        redirect(url_for('login', external=False))
    
    now = int(time.time())

    is_expired = token_info['expires_at'] - now < 60
    if(is_expired):
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info



def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = "6c767823b9884751b130fc11bce31ed9",
        client_secret = "11b161692d344f5cb42927cfebdd970b",
        redirect_url = url_for('redirect_page', _external = True),
        scope = 'user-library-read playlist-modify-public playlist-modify-private'
        )
#client ID copied and pasted from Spotify Dashboard

app.run(debug=True) #To use a Flask App, it needs to be ran, to run the flask app, app.run needs to be written on bottom
#to run it, type in terminal python3 spotifyWeekly.py
