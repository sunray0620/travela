'''
This module interacts with AiPlatform on Google Cloud.
'''

from shared.gcloud_client.auth_helper import AuthHelper
from shared.http.http_helper import send_http_request

PROJECT_NAME = 'procon-1'
LOCATION = 'us-central1'
GEMINI_MODEL = 'google/gemini-1.5-flash-001'


class AiPlatformClient:
    '''AiPlatform Client.'''

    def __init__(self):
        self.auth = AuthHelper()

    def generate_content(self, prompt):
        '''Get AI content.'''
        access_token = self.auth.get_access_token()
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        gemini_url = (
            f'https://{LOCATION}-aiplatform.googleapis.com/v1beta1/projects'
            f'/{PROJECT_NAME}/locations/{LOCATION}/endpoints/openapi/chat/completions'
        )
        data = {
            'model': GEMINI_MODEL,
            'messages': [{'role': 'user', 'content': prompt}],
        }
        resp = send_http_request(
            method='POST', url=gemini_url, json=data, headers=headers
        )
        resp = resp.json()
        return resp['choices'][0]['message']['content']
