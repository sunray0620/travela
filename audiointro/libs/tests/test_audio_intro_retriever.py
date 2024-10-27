from django.test import TestCase
from audiointro.libs.audio_intro_retriever import get_audio_intro

class AudioIntroRetrieverTests(TestCase):
    def setUp(self):
        pass

    def test_get_audio_intro(self):
        actual_ret = get_audio_intro()
        self.assertEqual(actual_ret, 'test_audio_intro')