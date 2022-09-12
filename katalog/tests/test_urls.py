from django.test import SimpleTestCase
from django.urls import reverse, resolve
from katalog.views import show_katalog

class TestUrls(SimpleTestCase):

    def test_url_is_resolved(self):
        url = reverse('show_katalog') # dari katalog.urls name
        print(resolve(url))
        self.assertEquals(resolve(url).func)
