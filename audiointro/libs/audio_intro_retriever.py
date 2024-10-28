'''The module that retrieves audio intro.'''
from shared.gcloud_client.generativelanguage_client import GenerativeLanguageClient

class AudioIntroRetriever:
    '''The class that retrieves audio intro.'''
    def __init__(self, generativelanguage_client: GenerativeLanguageClient):
        self.generativelanguage_client = generativelanguage_client

    def get_audio_intro(self, prompt) -> str:
        '''Get an audio intro based on the prompt.'''
        return self.generativelanguage_client.generate_content(prompt)
