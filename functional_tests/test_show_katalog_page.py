from selenium import webdriver
from katalog.models import CatalogItem
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

class TestShowKatalogPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver')

    def tearDown(self):
        self.browser.close()

    def test_user_is_redirected_to_katalog(self):
        self.browser.get(self.live_server_url)

        self.assertEquals(self.browser.current_url, self.live_server_url)