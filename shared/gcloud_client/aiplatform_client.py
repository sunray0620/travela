import json

from shared.gcloud_client.auth_helper import AuthHelper
from shared.http.http_helper import send_http_post_request

PROJECT_NAME = 'procon-1'
LOCATION = 'us-central1'

class AiPlatformClient:
    def __init__(self):
        self.auth = AuthHelper()

    def generate_content(self, prompt):
        access_token = self.auth.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        gemini_url = f"https://{LOCATION}-aiplatform.googleapis.com/v1beta1/projects/{PROJECT_NAME}/locations/{LOCATION}/endpoints/openapi/chat/completions"
        data = {
            "model": "google/gemini-1.5-flash-001",
            "messages": [{
                "role": "user",
                "content": prompt
            }]
        }
        response_text = send_http_post_request(gemini_url, data=None, json=data, headers=headers)
        resp = json.loads(response_text)
        return resp['choices'][0]['message']['content']