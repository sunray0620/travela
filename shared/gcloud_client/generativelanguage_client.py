'''
This module interacts with GenerativeLanguage on Google Cloud.
'''

from shared.http.http_helper import send_http_request
from django.conf import settings

GEMINI_MODEL = 'gemini-1.5-pro'
GENERATIVE_LANGUAGE_API_KEY = settings.GENERATIVE_LANGUAGE_API_KEY

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
            f':generateContent?key={GENERATIVE_LANGUAGE_API_KEY}'
        )
        request = {
            'contents': [{
                'parts': [{
                    'text': prompt
                }]
            }]
        }
        resp = send_http_request(
            method='POST', url=gemini_url, json=request, headers=headers
        )
        resp = resp.json()
        return resp['candidates'][0]['content']['parts'][0]['text']
