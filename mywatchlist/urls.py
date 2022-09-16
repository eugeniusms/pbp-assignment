from django.urls import path
from katalog.views import show_katalog

app_name = 'watchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
]
