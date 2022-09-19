from django.test import TestCase, Client

# https://codereview.stackexchange.com/questions/249173/test-django-urls
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
# https://stackoverflow.com/questions/44160666/valueerror-missing-staticfiles-manifest-entry-for-favicon-ico

class TestMyWatchListViews(TestCase):

    # Test response status code show_html
    def test_watchlist_show_html(self):         
        response = Client().get('/mywatchlist/html/')
        self.assertEquals(response.status_code,200)
    
    # Test response status code show_xml
    def test_watchlist_show_xml(self):         
        response = Client().get('/mywatchlist/json/')
        self.assertEquals(response.status_code,200)
    
    # Test response status code show_json
    def test_watchlist_show_json(self):         
        response = Client().get('/mywatchlist/xml/')
        self.assertEquals(response.status_code,200)