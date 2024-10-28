from django.test import TestCase
import json
import unittest
from unittest.mock import patch

from shared.gcloud_client.aiplatform_client import AiPlatformClient

class AiPlatformClientTests(TestCase):
    def setUp(self):
        pass

    @patch('shared.gcloud_client.aiplatform_client.send_http_post_request')
    @patch('shared.gcloud_client.aiplatform_client.AuthHelper.get_access_token')
    def test_generate_content(self, auth_mock, http_post_mock):
        auth_mock.return_value = {
            'access_token': 'test_access_token',
            'token_type': 'test_token_type',
            'expires_in': 100,
        }
        mock_http_response = {
            "choices": [{
                    "finish_reason": "stop",
                    "index": 0,
                    "logprobs": None,
                    "message": {
                        "content": "Gemini Result",
                        "role": "assistant"
                    }
            }]
        }
        http_post_mock.return_value = json.dumps(mock_http_response)
        ai_platform_client = AiPlatformClient()
        prompt = 'What is the distance between the Earth and the Mars'
        resp = ai_platform_client.generate_content(prompt)
        http_post_mock.assert_called_once()
        self.assertEqual(resp, 'Gemini Result')
