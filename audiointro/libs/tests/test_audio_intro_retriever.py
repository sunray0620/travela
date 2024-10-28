'''
The module that contains the unit tests for audio_intro_retriever.
'''
from unittest.mock import patch
from django.test import TestCase
from audiointro.libs.audio_intro_retriever import GenerativeLanguageClient


class AudioIntroRetrieverTests(TestCase):
    '''The class that contains the unit tests for audio_intro_retriever.'''

    def setUp(self):
        pass

    @patch(
        'shared.gcloud_client.generativelanguage_client.GenerativeLanguageClient.generate_content'
    )
    def test_get_audio_intro(self, generate_content_mock):
        '''Test get audio intro successfully.'''
        generate_content_mock.return_value = 'test_result'
        generative_language_client = GenerativeLanguageClient()
        prompt = 'test_prompt'
        actual_ret = generative_language_client.generate_content(prompt)
        self.assertEqual(actual_ret, 'test_result')
