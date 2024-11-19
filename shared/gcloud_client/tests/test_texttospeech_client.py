'''
The module that contains the unit tests for texttospeech_client.
'''
from unittest.mock import patch, MagicMock

from django.test import TestCase
from shared.gcloud_client.texttospeech_http_client import TextToSpeechHttpClient


class TextToSpeechClientTests(TestCase):
    '''The class that contains the unit tests for texttospeech_client.'''

    def setUp(self):
        pass

    @patch('shared.gcloud_client.texttospeech_http_client.send_http_request')
    @patch('shared.gcloud_client.texttospeech_http_client.AuthHelper.get_access_token')
    def test_generate_speech(self, auth_mock, http_post_mock):
        '''Test get speech from TextToSpeech.'''
        auth_mock.return_value = {
            'access_token': 'test_access_token',
            'token_type': 'test_token_type',
            'expires_in': 100,
        }
        mock_http_response = {
            'audioContent': 'result audio content',
            'timepoints': [],
            'audioConfig': {
                'audioEncoding': 'MP3',
                'speakingRate': 0,
                'pitch': 0,
                'volumeGainDb': 0,
                'sampleRateHertz': 24000,
                'effectsProfileId': []
            }
        }
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_http_response
        http_post_mock.return_value = mock_response

        texttospeech_http_client = TextToSpeechHttpClient()
        text = 'test prompt'
        resp = texttospeech_http_client.generate_speech(text)
        http_post_mock.assert_called_once()
        self.assertEqual(resp, 'result audio content')
