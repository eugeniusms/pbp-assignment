from wsgiref.util import request_uri
from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.urls import reverse

from todolist.forms import TaskForm
from todolist.models import Task
from datetime import datetime

from django.http import HttpResponse
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import time

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}

    # jeda 2 detik untuk menampilkan response
    time.sleep(2)
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}

    # jeda 2 detik untuk menampilkan response
    time.sleep(2)
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        # Mengambil data request melalui TaskForm
        form = TaskForm(request.POST)
        # Jika form yang di POST valid
        if form.is_valid():
            # cek data yang masuk ke dalam form melalui request.POST
            # print(form.cleaned_data) 
            # Menyusun task sesuai model Task untuk dimasukkan ke database
            task = Task(
                user = request.user, # Generate user berdasarkan user yang login
                date = datetime.now(), # Generate date sesuai datetime saat POST
                title = form.cleaned_data['title'], # Mengambil title dari form di atas
                description = form.cleaned_data['description'], # Mengambil description dari form di atas
                is_finished = False # Default dari is_finished adalah False
            )
            # Memasukkan task ke database
            task.save()
            return HttpResponseRedirect("/todolist")
    else:
        form = TaskForm()

    # Merender create_task.html
    return render(request, "create_task.html", {
        "form": form
    })

@csrf_exempt # https://stackoverflow.com/questions/12731305/django-csrf-token-missing-or-incorrect
@login_required(login_url='/todolist/login/')
def todolist(request):
    # Mengambil data sesuai dengan user yang login
    username = request.user.username
    user_id = request.user.id
    data_todolist_dikirimkan = Task.objects.filter(user_id=user_id)

    # Merangkum context yang akan dikirimkan ke todolist.html
    context = { 
        "username": username,
        "todolist": data_todolist_dikirimkan
    }
    
    return render(request, "todolist_ajax.html", context)

@login_required(login_url='/todolist/login/')
def change_status(request, id):
    # Mengambil data task sesuai idnya
    task = Task.objects.get(id=id)

    # Switch statusnya
    if task.is_finished:
        task.is_finished = False
    else:
        task.is_finished = True

    # Menyimpan task kembali ke database
    task.save()
    # Render ke todolist.html
    return HttpResponseRedirect("/todolist")

@csrf_exempt # https://stackoverflow.com/questions/12731305/django-csrf-token-missing-or-incorrect
@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    # Mengambil data task sesuai idnya
    task = Task.objects.get(id=id)
    # Menghapus task sesuai idnya
    task.delete()
    # Render ke todolist.html
    return HttpResponseRedirect("/todolist")

# References:
# 1. https://www.youtube.com/watch?v=3XOS_UpJirU
# 2. https://www.w3schools.com/django/django_delete_record.php

def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        todo = Task.objects.create(
            user=request.user,
            title=title, 
            description=description,
            date=datetime.now(), 
            is_finished=False
        )

        context = {
            'pk':todo.pk,
            'fields':{
                'title':todo.title,
                'description':todo.description,
                'is_finished':todo.is_finished,
                'date':todo.date,
            }
        }

        return JsonResponse(context)