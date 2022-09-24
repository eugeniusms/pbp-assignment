from django.urls import path

from todolist.views import todolist, login_user, register, create_task, logout_user

app_name = 'todolist'

urlpatterns = [
    path('', todolist, name='todolist'), # http://localhost:8000/todolist/
    path('login/', login_user, name='login'), # http://localhost:8000/todolist/login
    path('register/', register, name='register'), # http://localhost:8000/todolist/register
    path('create-task/', create_task, name='create_task'), # http://localhost:8000/todolist/create-task
    path('logout/', logout_user, name='logout'), # http://localhost:8000/todolist/logout
]
