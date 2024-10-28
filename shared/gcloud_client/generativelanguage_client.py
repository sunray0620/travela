import json

from shared.gcloud_client.constants import API_KEY
from shared.http.http_helper import send_http_post_request

GEMINI_MODEL = 'gemini-1.5-pro'

class GenerativeLanguageClient:
    def __init__(self):
        pass

    def generate_content(self, prompt):
        headers = {
            "Content-Type": "application/json"
        }
        gemini_url = f'https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={API_KEY}'
        request = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }]
        }
        response_text = send_http_post_request(gemini_url, data=None, json=request, headers=headers)
        response = json.loads(response_text)
        return response['candidates'][0]['content']['parts'][0]['text']
