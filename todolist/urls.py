from django.urls import path

from todolist.views import todolist, login_user, register, create_task, change_status, delete_task, logout_user, show_json, add_todo

app_name = 'todolist'

urlpatterns = [
    path('', todolist, name='todolist'), # http://localhost:8000/todolist/
    path('login/', login_user, name='login'), # http://localhost:8000/todolist/login
    path('register/', register, name='register'), # http://localhost:8000/todolist/register
    path('create-task/', create_task, name='create_task'), # http://localhost:8000/todolist/create-task
    path('change-status/<int:id>', change_status, name='change_status'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('logout/', logout_user, name='logout'), # http://localhost:8000/todolist/logout
    path('json/', show_json, name='show_json'), # http://localhost:8000/todolist/json
    path('add/', add_todo, name="add_todo"), # http://localhost:8000/todolist/add
]
