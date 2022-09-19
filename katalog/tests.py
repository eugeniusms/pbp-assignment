from django.test import TestCase, Client

# https://codereview.stackexchange.com/questions/249173/test-django-urls
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
# https://stackoverflow.com/questions/44160666/valueerror-missing-staticfiles-manifest-entry-for-favicon-ico

class TestKatalog(TestCase):

    # Test katalog.urls
    def test_katalog_url(self):
        response = Client().get('/katalog/')
        self.assertEqual(response.status_code, 200)

    # Test katalog.views
    def test_katalog_view(self):
        response = Client().get('/katalog/')
        self.assertTemplateUsed(response, 'katalog.html')