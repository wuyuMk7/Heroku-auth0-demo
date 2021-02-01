import os

from functools import wraps
from flask import Flask, jsonify, redirect, render_template, request, url_for, session
from urllib.parse import urlencode

import auth0

auth0_cursor = None

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'profile' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.before_first_request
def initialize():
    global auth0_cursor
    auth0_cursor = auth0.setup()

@app.route('/')
def home():
    return render_template("home.html")

# Functions for "login"
@app.route('/login')
def login():
    if 'profile' in session:
        return redirect(url_for('test_auth'))
    else:
        return auth0_cursor.authorize_redirect(redirect_uri=url_for('callback', _external=True))
        #return auth0_cursor.authorize_redirect(redirect_uri="http://localhost:5000/callback")

@app.route('/logout')
def logout():
    session.clear()
    params = { 'returnTo': url_for('home', _external=True), 'client_id': os.environ['AUTH0_CLIENT_ID'] }
    return redirect(auth0_cursor.api_base_url + '/v2/logout?' + urlencode(params))

@app.route('/callback')
def callback():
    auth0_cursor.authorize_access_token()
    resp = auth0_cursor.get('userinfo')
    userinfo = resp.json()

    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }

    return redirect('/test_auth')

@app.route('/test_auth')
@require_auth
def test_auth():
    return render_template("test_auth.html", profile=session['profile'])

if __name__ == '__main__':
    pass
