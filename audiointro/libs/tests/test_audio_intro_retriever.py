'''
The module that contains the unit tests for audio_intro_retriever.
'''
from unittest.mock import MagicMock, patch
from django.test import TestCase

from audiointro.libs.audio_intro_retriever import AudioIntroRetriever


class AudioIntroRetrieverTests(TestCase):
    '''The class that contains the unit tests for audio_intro_retriever.'''

    def setUp(self):
        pass

    @patch('shared.gcloud_client.generativelanguage_client.GenerativeLanguageClient')
    @patch('shared.gcloud_client.texttospeech_client.TextToSpeechClient')
    def test_get_audio_intro(
        self, mock_texttospeech_client, mock_generativelanguage_client
    ):
        '''Test get audio intro successfully.'''
        # Set up the mock clients
        mock_generativelanguage_client = MagicMock()
        mock_generativelanguage_client.generate_content.return_value = (
            'test_result_text'
        )
        mock_texttospeech_client = MagicMock()
        mock_texttospeech_client.generate_speech.return_value = 'test_result_audio'

        audio_intro_retriever = AudioIntroRetriever(
            mock_generativelanguage_client, mock_texttospeech_client
        )
        query = 'test_query'
        actual_ret = audio_intro_retriever.get_audio_intro(query)
        self.assertDictEqual(actual_ret, {
            'query': query,
            'result_text': 'test_result_text',
            'result_audio': 'test_result_audio',
        })
