from django.test import TestCase
import json
import unittest
from unittest.mock import patch

from shared.gcloud_client.auth_helper import AuthHelper

class AuthHelperTests(TestCase):
    def setUp(self):
        pass

    @patch('shared.gcloud_client.auth_helper.get_access_token')
    def test_get_access_token(self, http_post_mock):
        test_access_token_json = {
            'access_token': 'test_access_token',
            'token_type': 'test_token_type',
            'expires_in': 100,
        }
        http_post_mock.return_value = test_access_token_json

        auth_helper = AuthHelper()
        access_token_1 = auth_helper.get_access_token()
        access_token_2 = auth_helper.get_access_token()
        http_post_mock.assert_called_once()
        self.assertEqual(access_token_1, access_token_2)
