from django.urls import path

from todolist.views import todolist

app_name = 'todolist'

urlpatterns = [
    path('', todolist, name='todolist'), # http://localhost:8000/todolist/
]
