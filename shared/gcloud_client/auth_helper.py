'''
This module maintains access token that can be used by other gcloud calls.
'''
import time
from typing import Any

import jwt
from django.conf import settings
from shared.http.http_helper import send_http_request

ACCESS_TOKEN_LIFE_SPAN_SECONDS = 3600


class AuthHelper:
    '''The class to maintain a valid access token.'''
    def __init__(self):
        self.access_token = None
        self.access_token_type = None
        self.access_token_exp_time = None

    def get_access_token(self) -> str:
        '''Return the currently valid access token or a new one.'''
        current_time = time.time()
        if self.access_token and current_time < self.access_token_exp_time - 60:
            # 60 seconds buffer
            return self.access_token

        # refresh the token
        new_token = get_new_access_token()
        self.access_token = new_token['access_token']
        self.access_token_type = new_token['token_type']
        self.access_token_exp_time = current_time + new_token['expires_in']
        return self.access_token


def get_new_access_token() -> Any:
    '''Get a new access token from gcloud.'''
    token_url = 'https://oauth2.googleapis.com/token'
    token_data = {
        'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
        'assertion': generate_jwt(),
    }
    token_headers = {'Content-Type': 'application/json'}

    response = send_http_request(
        method='POST', url=token_url, json=token_data, headers=token_headers
    )
    return response.json()


def generate_jwt() -> str:
    '''Generate a signed JWT.'''
    print(settings.GCLOUD_SERVICE_ACCT_INFO)
    client_email = settings.GCLOUD_SERVICE_ACCT_INFO['client_email']
    private_key_id = settings.GCLOUD_SERVICE_ACCT_INFO['private_key_id']
    private_key = settings.GCLOUD_SERVICE_ACCT_INFO['private_key']

    iat = time.time()
    exp = iat + ACCESS_TOKEN_LIFE_SPAN_SECONDS
    payload = {
        'iss': client_email,
        'scope': 'https://www.googleapis.com/auth/cloud-platform',
        'aud': 'https://oauth2.googleapis.com/token',
        'iat': iat,
        'exp': exp,
    }
    headers = {'kid': private_key_id}
    return jwt.encode(payload, private_key, algorithm='RS256', headers=headers)
