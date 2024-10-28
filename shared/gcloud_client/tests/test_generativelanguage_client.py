from django.test import TestCase
import json
import unittest
from unittest.mock import patch

from shared.gcloud_client.generativelanguage_client import GenerativeLanguageClient

class GenerativeLanguageClientTests(TestCase):
    def setUp(self):
        pass

    @patch('shared.gcloud_client.generativelanguage_client.send_http_post_request')
    def test_generate_content(self, http_post_mock):
        mock_http_response = {
            "candidates": [{
                "content": {
                    "parts": [{
                        "text": "Gemini Result"
                    }],
                    "role": "model"
                },
            }]
        }

        http_post_mock.return_value = json.dumps(mock_http_response)
        generative_language_client = GenerativeLanguageClient()
        prompt = 'What is the distance between the Earth and the Mars'
        resp = generative_language_client.generate_content(prompt)
        http_post_mock.assert_called_once()
        self.assertEqual(resp, 'Gemini Result')
        
