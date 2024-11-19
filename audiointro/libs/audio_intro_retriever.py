'''The module that retrieves audio intro.'''

from typing import Dict
from shared.gcloud_client.generativelanguage_client import GenerativeLanguageClient
from shared.gcloud_client.texttospeech_http_client import TextToSpeechHttpClient


class AudioIntroRetriever:
    '''The class that retrieves audio intro.'''

    def __init__(
        self,
        generativelanguage_client: GenerativeLanguageClient,
        texttospeech_http_client: TextToSpeechHttpClient,
    ):
        self.generativelanguage_client = generativelanguage_client
        self.texttospeech_http_client = texttospeech_http_client

    def get_audio_intro(self, query: str) -> Dict:
        '''Get an audio intro based on the prompt.'''
        result_text = self.generativelanguage_client.generate_content(query)
        result_audio = self.texttospeech_http_client.generate_speech(result_text)
        return {
            'query': query,
            'result_text': result_text,
            'result_audio': result_audio,
        }
