
'''
The module that contains the unit tests for generativelanguage_client.
'''
from unittest.mock import patch, MagicMock

from django.test import TestCase
from shared.gcloud_client.generativelanguage_client import GenerativeLanguageClient


class GenerativeLanguageClientTests(TestCase):
    '''The class that contains the unit tests for generativelanguage_client.'''
    def setUp(self):
        pass

    @patch('shared.gcloud_client.generativelanguage_client.send_http_request')
    def test_generate_content(self, http_post_mock):
        '''Test get content from Generative Language.'''
        mock_http_response = {
            'candidates': [{
                'content': {
                    'parts': [{
                        'text': 'Gemini Result'
                    }],
                    'role': 'model'
                },
            }]
        }

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_http_response
        http_post_mock.return_value = mock_response

        generative_language_client = GenerativeLanguageClient()
        prompt = 'test prompt'
        resp = generative_language_client.generate_content(prompt)
        http_post_mock.assert_called_once()
        self.assertEqual(resp, 'Gemini Result')
