from django.urls import path
from katalog.views import show_katalog

from mywatchlist.views import show_html
from mywatchlist.views import show_xml
from mywatchlist.views import show_json

app_name = 'watchlist'

urlpatterns = [
    path('', show_html, name='show_watchlist'), # http://localhost:8000/watchlist/
    path('html/', show_html, name='show_html'), # http://localhost:8000/watchlist/html/
    path('xml/', show_xml, name='show_xml'), # http://localhost:8000/watchlist/xml/
    path('json/', show_json, name='show_json'), # http://localhost:8000/watchlist/json/
]
