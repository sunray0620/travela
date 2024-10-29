'''
The module that contains the unit tests.
'''
from django.test import TestCase
from django.urls import reverse

class AudioIntroViewsTests(TestCase):
    '''The class that contains the unit tests for AudioIntroViews.'''

    def setUp(self):
        pass

    def test_audio_intro_view(self):
        '''test the audio_intro view.'''
        url = reverse('audio_intro', kwargs={})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'audiointro/get_audio_intro.html')
