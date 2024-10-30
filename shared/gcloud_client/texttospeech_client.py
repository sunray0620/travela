
'''
This module interacts with TextToSpeech on Google Cloud.
'''
from shared.gcloud_client.auth_helper import AuthHelper
from shared.http.http_helper import send_http_request

class TextToSpeechClient:
    '''TextToSpeech Client.'''

    def __init__(self):
        self.auth = AuthHelper()

    def generate_speech(self, text) -> str:
        '''Get audio speech content.'''
        access_token = self.auth.get_access_token()
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        url = 'https://texttospeech.googleapis.com/v1beta1/text:synthesize'
        request = {
            'audioConfig': {
                'audioEncoding': 'MP3',
                'effectsProfileId': [
                    'handset-class-device'
                ],
                'pitch': 0,
                'speakingRate': 0
            },
            'input': {
                'text': text
            },
            'voice': {
                'languageCode': 'en-US',
                'name': 'en-US-Journey-F'
            }
        }
        resp = send_http_request(
            method='POST', url=url, json=request, headers=headers
        )
        print(f'generate_speech: {resp}')
        resp = resp.json()
        return resp['audioContent']
