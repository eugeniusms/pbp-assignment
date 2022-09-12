from django.test import TestCase, Client
from django.urls import reverse
from katalog.models import CatalogItem
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('show_katalog')

    def test_show_katalog_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'katalog/katalog.html')