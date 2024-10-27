from django.test import TestCase
from django.urls import reverse

class AudioIntroViewsTests(TestCase):

    def setUp(self):
        pass

    def test_index_view(self):
        url = reverse('index', kwargs={})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'myapp/book_detail.html')
        self.assertContains(response, "audiointro")