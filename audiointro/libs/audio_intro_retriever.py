'''The module that retrieves audio intro.'''

from typing import Dict
from shared.gcloud_client.generativelanguage_client import GenerativeLanguageClient
from shared.gcloud_client.texttospeech_client import TextToSpeechClient


class AudioIntroRetriever:
    '''The class that retrieves audio intro.'''

    def __init__(
        self,
        generativelanguage_client: GenerativeLanguageClient,
        texttospeech_client: TextToSpeechClient,
    ):
        self.generativelanguage_client = generativelanguage_client
        self.texttospeech_client = texttospeech_client

    def get_audio_intro(self, query: str) -> Dict:
        '''Get an audio intro based on the prompt.'''
        result_text = self.generativelanguage_client.generate_content(query)
        print(f'result_text: {result_text}')
        result_audio = self.texttospeech_client.generate_speech(result_text)
        print(f'Got result audio for {result_text}')

        return {
            'query': query,
            'result_text': result_text,
            'result_audio': result_audio,
        }
