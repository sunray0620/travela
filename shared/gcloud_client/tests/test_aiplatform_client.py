'''
The module that contains the unit tests for aiplatform_client.
'''
from unittest.mock import patch, MagicMock

from django.test import TestCase
from shared.gcloud_client.aiplatform_client import AiPlatformClient


class AiPlatformClientTests(TestCase):
    '''The class that contains the unit tests for aiplatform_client.'''
    def setUp(self):
        pass

    @patch('shared.gcloud_client.aiplatform_client.send_http_request')
    @patch('shared.gcloud_client.aiplatform_client.AuthHelper.get_access_token')
    def test_generate_content(self, auth_mock, http_post_mock):
        '''Test get content from AI platform.'''
        auth_mock.return_value = {
            'access_token': 'test_access_token',
            'token_type': 'test_token_type',
            'expires_in': 100,
        }
        mock_http_response = {
            'choices': [{
                'finish_reason': 'stop',
                'index': 0,
                'logprobs': None,
                'message': {
                    'content': 'Gemini Result',
                    'role': 'assistant'
                }
            }]
        }
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_http_response
        http_post_mock.return_value = mock_response

        ai_platform_client = AiPlatformClient()
        prompt = 'test prompt'
        resp = ai_platform_client.generate_content(prompt)
        http_post_mock.assert_called_once()
        self.assertEqual(resp, 'Gemini Result')
