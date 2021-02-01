#!/usr/bin/env python

import os
from flask import current_app
from authlib.integrations.flask_client import OAuth

def setup():
    AUTH0_CLIENT_ID=os.environ['AUTH0_CLIENT_ID']
    AUTH0_CLIENT_SECRET=os.environ['AUTH0_CLIENT_SECRET']
    AUTH0_DOMAIN=os.environ['AUTH0_DOMAIN']

    oauth = OAuth(current_app)
    auth0 = oauth.register(
        'auth0',
        client_id=AUTH0_CLIENT_ID,
        client_secret=AUTH0_CLIENT_SECRET,
        api_base_url='https://{}'.format(AUTH0_DOMAIN),
        access_token_url='https://{}/oauth/token'.format(AUTH0_DOMAIN),
        authorize_url='https://{}/authorize'.format(AUTH0_DOMAIN),
        client_kwargs={
            'scope': 'openid profile email'
        },
    )

    return auth0
