
from shared.gcloud_client.generativelanguage_client import GenerativeLanguageClient

class AudioIntroRetriever:
    def __init__(self, generativelanguage_client):
        self.generativelanguage_client = generativelanguage_client

    def get_audio_intro(self, prompt):
        return self.generativelanguage_client.generate_content(prompt)
