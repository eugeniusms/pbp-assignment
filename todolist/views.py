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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
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
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def todolist(request):
    
    return render(request, "todolist.html")

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        # Mengambil data request melalui TaskForm
        form = TaskForm(request.POST)
        # Jika form yang di POST valid
        if form.is_valid():
            # cek data yang masuk ke dalam form melalui request.POST
            print(form.cleaned_data) 
            # Menyusun task sesuai model Task untuk dimasukkan ke database
            task = Task(
                user = request.user, # Generate user berdasarkan user yang login
                date = datetime.now(), # Generate date sesuai datetime saat POST
                title = form.cleaned_data['title'], # Mengambil title dari form di atas
                description = form.cleaned_data['description'] # Mengambil description dari form di atas
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

# References:
# 1. https://www.youtube.com/watch?v=3XOS_UpJirU