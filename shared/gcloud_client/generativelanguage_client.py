'''
This module interacts with GenerativeLanguage on Google Cloud.
'''

from shared.gcloud_client.constants import API_KEY
from shared.http.http_helper import send_http_request

GEMINI_MODEL = 'gemini-1.5-flash'


class GenerativeLanguageClient:
    '''GenerativeLanguage Client.'''

    def __init__(self):
        pass

    def generate_content(self, prompt: str) -> str:
        '''GenerativeLanguage Client.'''
        headers = {
            'Content-Type': 'application/json'
        }
        gemini_url = (
            f'https://generativelanguage.googleapis.com/v1beta/models'
            f'/{GEMINI_MODEL}'
            f':generateContent?key={API_KEY}'
        )
        request = {
            'contents': [{
                'parts': [{
                    'text': prompt
                }]
            }]
        }
        resp = send_http_request(
            method='POST', url=gemini_url, data=None, json=request, headers=headers
        )
        resp = resp.json()
        return resp['candidates'][0]['content']['parts'][0]['text']
