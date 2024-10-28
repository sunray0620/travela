'''
This module maintains access token that can be used by other gcloud calls.
'''
import time
from typing import Dict, Any

import jwt
from shared.gcloud_client.constants import SERVICE_ACCT_INFO
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
        new_token = get_new_access_token(SERVICE_ACCT_INFO)
        self.access_token = new_token['access_token']
        self.access_token_type = new_token['token_type']
        self.access_token_exp_time = current_time + new_token['expires_in']
        return self.access_token


def get_new_access_token(service_account_info: Dict[str, str]) -> Any:
    '''Get a new access token from gcloud.'''
    token_url = service_account_info['token_uri']
    token_data = {
        'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
        'assertion': generate_jwt(service_account_info),
    }
    token_headers = {'Content-Type': 'application/json'}

    response = send_http_request(
        method='POST', url=token_url, json=token_data, headers=token_headers
    )
    return response.json()


def generate_jwt(service_account_info: Dict[str, str]) -> str:
    '''Generate a signed JWT.'''
    iat = time.time()
    exp = iat + ACCESS_TOKEN_LIFE_SPAN_SECONDS
    payload = {
        'iss': service_account_info['client_email'],
        'scope': 'https://www.googleapis.com/auth/cloud-platform',
        'aud': 'https://oauth2.googleapis.com/token',
        'iat': iat,
        'exp': exp,
    }
    headers = {'kid': service_account_info['private_key_id']}
    return jwt.encode(
        payload, service_account_info['private_key'], algorithm='RS256', headers=headers
    )
