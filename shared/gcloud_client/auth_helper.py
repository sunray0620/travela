import time
import jwt
import json
from typing import Dict

from shared.http.http_helper import send_http_post_request
from shared.gcloud_client.constants import SERVICE_ACCT_INFO

ACCESS_TOKEN_LIFE_SPAN_SECONDS = 3600

class AuthHelper:
    def __init__(self):
        self.access_token = None
        self.access_token_type = None
        self.access_token_exp_time = None

    def get_access_token(self):
        current_time = time.time()
        if self.access_token and current_time < self.access_token_exp_time - 60:
            # 60 seconds buffer
            return self.access_token
        
        # refresh the token
        new_token = get_access_token(SERVICE_ACCT_INFO)
        self.access_token = new_token['access_token']
        self.access_token_type = new_token['token_type']
        self.access_token_exp_time = current_time + new_token['expires_in']
        return self.access_token


def get_access_token(service_account_info):
    token_url = service_account_info['token_uri']
    # token_url = 'https://oauth2.googleapis.com/token'
    token_data = {
        'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
        'assertion': generate_jwt(service_account_info),
    }
    token_headers = {
        'Content-Type': 'application/json'
    }

    response_str = send_http_post_request(url=token_url, data=None, json=token_data, headers=token_headers)
    return json.loads(response_str)


def generate_jwt(service_account_info: Dict):
    iat = time.time()
    exp = iat + ACCESS_TOKEN_LIFE_SPAN_SECONDS
    payload = {
        'iss': service_account_info['client_email'],
        'scope': 'https://www.googleapis.com/auth/cloud-platform',
        'aud': 'https://oauth2.googleapis.com/token',
        'iat': iat,
        'exp': exp,
    }
    headers = {
        'kid': service_account_info['private_key_id']
    }
    return jwt.encode(payload, service_account_info['private_key'], algorithm='RS256', headers=headers)
