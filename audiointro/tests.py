'''
The module that contains the unit tests.
'''
from unittest.mock import patch
from django.test import TestCase
from django.urls import reverse

class AudioIntroViewsTests(TestCase):
    '''The class that contains the unit tests for AudioIntroViews.'''

    def setUp(self):
        pass

    @patch(
        'audiointro.libs.audio_intro_retriever.AudioIntroRetriever.get_audio_intro'
    )
    def test_index_view(self, get_audio_intro_mock):
        '''test the index view.'''
        get_audio_intro_mock.return_value = 'test content'
        url = reverse('index', kwargs={})
        response = self.client.get(url, data={'prompt': 'test prompt'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test content')
        get_audio_intro_mock.assert_called_once_with('test prompt')


    def test_index_view_no_prompt(self):
        '''test the index view.'''
        url = reverse('index', kwargs={})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'error')
