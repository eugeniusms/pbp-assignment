# Todolist
[Demo Link](https://pbp-assignment-eugeniusms.herokuapp.com/todolist/)

## Kegunaan {% csrf_token %} pada elemen <form>
CSRF Token merupakan sebuah string dengan susunan acak yang dimunculkan setiap kali halaman form muncul. Umumnya, CSRF Token ada di dalam POST request, token tersebut disisipkan sebagai header, form data, atau query string. CSRF sendiri merupakan salah satu bentuk serangan siber yang sederhana, tetapi cukup efektif dalam menimbulkan masalah. Dengan CSRF Token, maka form dapat mencegah serangan CSRF yang akan membuat penyerang tidak mungkin melakukan permintaan HTTP yang sepenuhnya valid dan cocok kepada korbannya karena penyerang tidak dapat menebak nilai CSRF Token pengguna. Pada akhirnya penyerang tidak dapat melakukan request dengan semua parameter yang diperlukan untuk memenuhi request tersebut.

## Apa yang terjadi jika tidak ada potongan elemen {% csrf_token %} pada <form>?
Tanpa CSRF Token, maka permintaan pengguna tidak memiliki kode token yang cukup unik sehingga hacker dapat memanfaatkan celah keamanan ini untuk mengeksekusi atau melakukan aktivitas mengubah status, seperti memperbarui, menghapus, atau membuat permintaan tanpa disadari oleh sistem. Jika pada todolist form tidak diberikan kode itu maka hacker dapat melakukan penambahan dan pengubahan serta penghapusan task yang dimiliki oleh pengguna tanpa perlu menebak kode token yang cukup sulit untuk diprediksi karena kompleksitas token itu sendiri.

## Apakah dapat membuat form secara manual (tanpa menggunakan generator seperti {{form.as_table}})?
Ya bisa, terdapat banyak cara untuk menyusun form di dalam Django. Dengan memanfaatkan fitur bawaan HTML sebenarnya sudah cukup untuk menyusun suatu form yang efektif dalam tampilan antarmuka pengguna maupun kegunaannya. Selain itu masih banyak metode lain dalam menggunakan <form> di Django.

## Gambaran besar cara membuat <form> secara manual
Secara manual, <form> dapat dibuat dengan mendeklarasikan setiap elemen <input> sebagai elemen masukan pengguna. Contohnya untuk <form> yang sesuai dengan pengisian task baru maka cara manualnya adalah sebagai berikut:
```
<form action="" method="">
    <input type="text" id="title>
    <input type="text" id="description">
    <button type="submit">Submit</button>
</form>
```
Pertama-tama kita dapat menentukan action dan method yang digunakan dalam form, kemudian menambahkan elemen input yang dibutuhkan untuk diisi oleh user nantinya, elemen input memiliki banyak argumen seperti type, id, class, placeholder, value, validasi, dan lain-lain yang digunakan untuk keperluan form. Value setiap elemen input dalam form akan dicatat oleh form lalu ketika pengguna menekan tombol bertipe submit maka form otomatis akan dikirimkan sesuai action dan method yang dideklarasikan di awal.

## Alur data dari submisi pengguna melalui HTML form hingga muncul pada template HTML
1.  Pengguna mengunjungi halaman tertentu yang mengandung form contohnya create task.
    ![Alur 1 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-04/alur-01.jpg?raw=true)

2.  Pengguna menekan tombol "Add Task" yang dalam HTML merupakan button dengan
    type="submit". Saat button dengan type="submit" diklik maka HTML otomatis mengirimkan form sesuai dengan method dan actionnya.
    ![Alur 2 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-04/alur-02.jpg?raw=true)

3.  Form melakukan penembakan url sesuai action dan methodnya, pada contoh adalah 
    `"/todolist/create-task/"`
    Artinya form menembak ke url tersebut (url dapat dilihat di dalam urls.py)
    Path sesuai url tersebut memiliki argumen kedua berupa fungsi yang dijalankan yang terletak di dalam view, yaitu "create_task"
    ![Alur 3 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-04/alur-03.jpg?raw=true)

4.  Fungsi create_task pada views.py dieksekusi. Berhubung form yang diisi sebelumnya   
    menggunakan method "POST" maka saat program masuk ke dalam blok if request.method yang sesuai yaitu request.method == "POST". Kemudian menggunakan Django Form, object TaskForm diinisiasikan berdasarkan request dari user (form yang telah diisi user di dalam tampilan depan website). Lakukan pengecekan validitas form dengan form.is_valid(), saat form telah valid maka susun sebuah object berdasarkan model yang sudah ada di dalam app, pada contoh adalah model Task. Isi semua argumen Task sesuai dengan modelnya. Pada bagian yang diminta input user maka masukkan data sesuai object TaskForm dengan memanggil variabel_form.cleaned_data['id']. Setelah menginisiasikan object sesuai model maka lakukan variabel_model.save() untuk menyimpan model data tersebut ke dalam database. Data tersebut akan tersimpan sesuai dengan tabel modelnya di dalam database. Setelah data tersimpan maka redirect dan render halaman yang ingin ditampilkan ke user.
    ![Alur 4 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-04/alur-04.jpg?raw=true)

5.  Halaman yang dirender ke user disertai context untuk mengambil semua data yang sesuai 
    di dalam halaman tersebut ke template yang sesuai juga untuk halaman tersebut. Pada contoh, todolist melakukan render todolist.html dengan contextnya berisi username dan data seluruh todolist dengan filter sesuai user_id (untuk menampilkan todolist hanya milik user tersebut)
    ![Alur 5 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-04/alur-05.jpg?raw=true)

6.  Template yang dirender akan dilihat oleh user. Pada bagian HTML terdapat pengambilan 
    data dari context memanfaatkan variabel contextnya {{ variabel_dalam_context }}. Data tersebut diolah di dalam HTML.
    ![Alur 6 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-04/alur-06.jpg?raw=true)

7.  User dapat melihat tampilan template dengan susunan data yang lebih rapi setelah HTML 
    diberikan styling.
    ![Alur 7 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-04/alur-07.jpg?raw=true)

## Implementasi Proyek
1.  Jalankan command membuat aplikasi bernama "todolist" di base directory
    ```
    python manage.py startapp todolist
    ```

2.  Menambahkan path todolist di dalam path yang ada di `/project_django/urls.py`
    ```
    path('todolist/', include('todolist.urls'))
    ```

3.  Menyusun model bernama Task dengan atribut user, date, title, dan description sesuai 
    fieldnya di dalam `/todolist/models.py`
    ```
    from django.db import models
    from django.contrib.auth.models import User

    class Task(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE) 
        date = models.DateField() 
        title = models.CharField(max_length=255)
        description = models.TextField()
    ```

4.  Mengimplementasikan form registrasi, login, dan logout pengguna.
    ### Registrasi
    Tambahkan views logic untuk registrasi di dalam `/todolist/views.py`
    ```
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
    ```
    Views mengarah ke register.html yang terdapat form register di dalamnya
    ```
    <form method="POST" >  
        {% csrf_token %}  
        <table cellspacing="0" cellpadding="0">  
            {{ form.as_table }}  
            <tr>  
                <td></td>
                <td><button type="submit" name="submit" value="Daftar"/>Sign Up</button></td>  
            </tr>  
        </table>  
    </form>
    ```
    ### Login
    Tambahkan views logic untuk login di dalam `/todolist/views.py`
    ```
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
    ```
    Views mengarah ke login.html yang terdapat form login di dalamnya
    ```
    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username</td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
            <tr>
                <td>Password</td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>
            <tr>
                <td></td>
                <td><button onClick="myFunction()" class="btn login_btn" type="submit" value="Login">Login</button></td>
                <td></td>
            </tr>
        </table>
    </form>
    ```
    ### Logout
    Tambahkan views logic untuk logout di dalam `/todolist/views.py`
    ```
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('todolist:login'))
        response.delete_cookie('last_login')
        return response
    ```
    Menambahkan tombol logout di dalam template terkait
    ```
    <a href="{% url 'todolist:logout' %}">
        <button class="logout-button"> 
            Logout
        </button>
    </a>
    ```

5. Mengatur view halaman todolist di dalam `/todolist/views.py`
    ```
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
        
        return render(request, "todolist.html", context)
    ```

6.  Membuat halaman todolist yang memuat todolist, username, tombol task baru, tombol 
    logout, serta elemen tanggal pembuatan task, judul task, dan deskripsi task
    ```
    <html>
    {% load static %}
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet"  href="{% static 'todolist.css' %}">

        <title>EuTodolist | Todolist</title>
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}"/>

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    </head>

    {% block content %}
    <body>
        <section class="navbar">
            <a href="{% url 'todolist:create_task' %}">
                <button class="add-task-button">
                    Create New Task
                </button>
            </a>
            <h1>
                Hi {{ username }}, this is your todolist!
            </h1>
            <a href="{% url 'todolist:logout' %}">
                <button class="logout-button"> 
                Logout
                </button>
            </a>
        </section>

        
        
        <div class="todolist">
            <div class="todolist-list">
                <div class="todolist-todo">
                    <h1 style="color:#e05d43;">To Do</h1>
                    {% for todo in todolist %}
                        {% if todo.is_finished == False %}
                            <div class="task-card">
                                <p class="task-judul">{{todo.title}}</p>
                                <p class="task-deskripsi">{{todo.description}}</p>
                                <p class="task-tanggal">Created {{todo.date}}</p>
                                <!-- {% if todo.is_finished %}
                                <p>Status: Selesai</p>
                                {% else %}
                                <p>Status: Belum Selesai</p>
                                {% endif %} -->
                                <div class="task-tombol">
                                    <!-- pengubahan status dilakukan di penembakan url berikut -->
                                    <a href="/todolist/change-status/{{todo.id}}">
                                        <button type="submit" class="task-change-done">Finish >></button>
                                    </a>
                                    <!-- penghapusan task dilakukan di penembakan url berikut -->
                                    <a href="/todolist/delete-task/{{todo.id}}">
                                        <button type="submit" class="task-delete">Delete</button>
                                    </a>
                                </div>
                            </div>
                            <div class="sekat-vertikal"></div>
                        {% endif %}
                    {% endfor %}
                </div>
                <div class="sekat-horizontal"></div>
                <div class="todolist-done">
                    <h1 style="color:#25C2A0;">Done</h1>
                    {% for todo in todolist %}
                        {% if todo.is_finished %}
                            <div class="task-card">
                                <p class="task-judul">{{todo.title}}</p>
                                <p class="task-deskripsi">{{todo.description}}</p>
                                <p class="task-tanggal">Created {{todo.date}}</p>
                                <!-- {% if todo.is_finished %}
                                <p>Status: Selesai</p>
                                {% else %}
                                <p>Status: Belum Selesai</p>
                                {% endif %} -->
                                <div class="task-tombol">
                                    <!-- pengubahan status dilakukan di penembakan url berikut -->
                                    <a href="/todolist/change-status/{{todo.id}}">
                                        <button type="submit" class="task-change-todo"><< Rework</button>
                                    </a>
                                    <!-- penghapusan task dilakukan di penembakan url berikut -->
                                    <a href="/todolist/delete-task/{{todo.id}}">
                                        <button type="submit" class="task-delete">Delete</button>
                                    </a>
                                </div>
                            </div>
                            <div class="sekat-vertikal"></div>
                        {% endif %}
                    {% endfor %}
                </div>
            </div>
        </div>

        <div class="sekat-vertikal"></div>
        <div class="sekat-vertikal"></div>
        <div class="sekat-vertikal"></div>

    </body>
    {% endblock content %}
    </html>
    ```
    Tampilannya sebagai berikut:
    ![Alur 7 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-04/alur-07.jpg?raw=true)

7.  Menyusun views logic untuk halaman form dari task baru
    ```
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
    ```
    Menyusun template create_task.html
    ```
    <html>
    {% load static %}
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet"  href="{% static 'create_task.css' %}">

        <title>EuTodolist | Create Task</title>
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}"/>

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    </head>

    {% block content %}
    <body>

        <div class="create-task-container">
            <div class="create-task">
            <h1>Create New Task</h1>

                <div class="task-form">
                    <form action="/todolist/create-task/" method="POST">
                        {% csrf_token %}
                        <table cellspacing="0" cellpadding="0">  
                            {{ form.as_table }}
                        </table>  
                        <button type="submit">Add Task</button>
                    </form>   
                </div>

            </div>  
        </div>

        <br>
        <div class="back-button">
            <a href="{% url 'todolist:todolist' %}">< Back</a>
        </div>

    </body>

    {% endblock content %}
    </html>
    ```

8.  Menyusun routing menuju ke semua fitur website app todolist di `/todolist/urls.py`
    ```
    urlpatterns = [
        path('', todolist, name='todolist'), # http://localhost:8000/todolist/
        path('login/', login_user, name='login'), # http://localhost:8000/todolist/login
        path('register/', register, name='register'), # http://localhost:8000/todolist/register
        path('create-task/', create_task, name='create_task'), # http://localhost:8000/todolist/create-task
        path('change-status/<int:id>', change_status, name='change_status'),
        path('delete-task/<int:id>', delete_task, name='delete_task'),
        path('logout/', logout_user, name='logout'), # http://localhost:8000/todolist/logout
    ]
    ```

9.  Melakukan deployment dengan tes workflows ke Heroku 
    https://pbp-assignment-eugeniusms.herokuapp.com/todolist/

10. Membuat dua akun dummy dan tiga dummy data di situs web Heroku.
    Silakan login menggunakan akun berikut (akun dummy publik)
    Nomor | Username | Password
    --- | --- | --- 
    1 | pacil | open1234
    2 | public | open1234 

11. Membuat sebuah README (ini READMEnya)

## BONUS

12. Menambahkan atribut is_finished pada model Task dengan default=False
    ```
    from django.db import models
    from django.contrib.auth.models import User

    class Task(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE) 
        date = models.DateField()
        title = models.CharField(max_length=255)
        description = models.TextField()
        is_finished = models.BooleanField(default=False)
    ```

13. Menambahkan status penyelesaian task dan tombol pengubahan status pada todolist.html
    ```
    <a href="/todolist/change-status/{{todo.id}}">
        <button type="submit" class="task-change-done">Finish >></button>
    </a>
    ```
    dan
    ```
    <a href="/todolist/change-status/{{todo.id}}">
        <button type="submit" class="task-change-todo"><< Rework</button>
    </a>
    ```
    Logic dibalik penggantian status ada di `/todolist/views.py`
    ```
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
    ```

14. Menambahkan tombol untuk menghapus suatu task pada todolist.html
    ```
    <a href="/todolist/delete-task/{{todo.id}}">
        <button type="submit" class="task-delete">Delete</button>
    </a>
    ```
    Logic dibalik penghapusan task ada di `/todolist/views.py`
    ```
    @login_required(login_url='/todolist/login/')
    def delete_task(request, id):
        # Mengambil data task sesuai idnya
        task = Task.objects.get(id=id)
        # Menghapus task sesuai idnya
        task.delete()
        # Render ke todolist.html
        return HttpResponseRedirect("/todolist")
    ```

# TUGAS 5

## Perbedaan, Kelebihan, dan Kekurangan dari Inline, Internal, dan External CSS
1.  Inline CSS
    CSS ditulis di dalam tag yang ada dalam HTML. Untuk menambahkan style, perlu pengubahan pada elemen-elemen sesuai tag masing-masing.
    Contoh: 
    ```
    <div style="color:white;padding:10px;" class="nama">Eugenius Mario</div>
    ```
    <b>Kelebihan:</b>
    - Berguna untuk pengujian dalam melihat perubahan
    - Berguna untuk perbaikan cepat
    - Permintaan HTTP yang lebih kecil
    <br>
    <b>Kekurangan:</b>
    <br>
    - Inline CSS harus diterapkan pada setiap elemen

2.  Internal CSS
    CSS ditulis di dalam file HTML tetapi bukan pada tag tertentu melainkan terdapat tag khusus bernama `<style>`. Semua style CSS dimasukkan ke dalam tag tersebut.
    Contoh: 
    ```
    <style>
        .nama {
            color: white;
            padding: 10px;
        }
    </style>
    <body>
        <div class="nama">Eugenius Mario</div>
    </body>
    ```
    <b>Kelebihan:</b>
    - Perubahan hanya terjadi pada 1 halaman
    - Class dan ID bisa digunakan oleh internal stylesheet
    - Tidak perlu meng-upload beberapa file karena HTML dan CSS bisa digunakan di file yang sama.
    <br>
    <b>Kekurangan:</b>
    <br>
    - Meningkatkan waktu akses website
    <br>
    - Perubahan hanya terjadi pada 1 halaman – tidak efisien bila Anda ingin menggunakan CSS yang sama pada beberapa file

3.  External CSS
    CSS ditulis di dalam file yang berbeda dengan file HTML, contoh dasarnya adalah file ditulis sesuai nama file HTML dengan format .css.
    `index.html`
    ```
    <head>
        <link rel="stylesheet" type="text/css" href="index.css" />
    </head>
    <div class="nama">Eugenius Mario</div>
    ```
    `index.css`
    ```
    .nama {
        color: white;
        padding: 10px;
    }
    ```
    <b>Kelebihan:</b>
    - Ukuran file HTML menjadi lebih kecil dan strukturnya lebih rapi
    - Kecepatan loading menjadi lebih cepat
    - File CSS yang sama bisa digunakan di banyak halaman
    <br>
    <b>Kekurangan:</b>
    <br>
    - Halaman belum tampil secara sempurna hingga file CSS selesai dipanggil

## Tag HTML

Terdapat banyak tag HTML yang sudah saya ketahui karena terbiasa bekerja sebagai Fullstack Engineer, beberapa diantaranya adalah:

TAG | TAG | TAG | TAG | TAG | TAG |
--- | --- | --- | --- | --- | --- |
`<a>` | `<b>` |  `<i>` | `<u>` | `<br>` | `<tr>`
`<body>` | `<html>` |  `<section>` | `<head>` | `<footer>` | `<header>`
`<col>` | `<row>` |  `<table>` | `<tr>` | `<th>` | `<td>`
`<form>` | `<input>` |  `<button>` | `<span>` | `<p>` | `<img>`
`<label>` | `<li>` |  `<ul>` | `<ol>` | `<option>` | `<script>`
`<style>` | `<title>` |  `<video>` | `<h1>` | `<h2>` | `<h3>`
`<h4>` | `<h5>` |  `<h6>` | `<thead>` | `<tbody>` | `<tfoot>`

<br>
Beberapa kegunaan tag tersebut di antaranya adalah:
<br>
1.  `a`: Mendefinisikan hyperlink
<br>
2.  `b``i``u`: Mendekorasi teks (bold, italic, underline)
<br>
3.  `tr`: Memberi garis horizontal
<br>
4.  `body``html``section``head``footer``header`: Container dari HTML code
<br>
5.  `col``row``table``tr``th``td`: Identifier jenis kolom/baris dalam tabel maupun HTML container lainnya
<br>
Dan seterusnya...

<br>
Dan lain-lain, biasanya saya menggunakan dokumentasi W3School dan MDN Developer Mozilla, linknya dapat diakses di bawah sini:
- https://www.w3schools.com/tags/default.asp
- https://developer.mozilla.org/en-US/docs/Web/HTML/Element

## Tipe Selector CSS

1.  Tag
    Tipe ini memilih elemen yang didekorasi berdasarkan tag HTML yang ada di dalam file HTMLnya.
    <br>
    <b>Penggunaan:</b>
    ```
    p {
        color: blue;
    }
    ```

2.  Class
    Tipe ini memilih elemen yang didekorasi berdasarkan class yang didefinisikan dalam tag HTMLnya.
    <br>
    <b>Penggunaan:</b>
    ```
    .classname {
        color: blue;
    }
    ```

3.  Id
    Tipe ini memilih elemen yang didekorasi berdasarkan id yang didefinisikan dalam tag HTMLnya.
    <br>
    <b>Penggunaan:</b>
    ```
    #id {
        color: blue;
    }
    ```

4.  Atribut
    Tipe ini memilih elemen yang didekorasi berdasarkan atribut dalam tag HTML
    <br>
    <b>Penggunaan:</b>
    ```
    input[type=text] {
        color: blue;
    }
    ```

5.  Universal
    Tipe ini memilih elemen yang didekorasi berdasarkan jangkauan tertentu, contohnya * untuk select semua elemen yang ada dalam HTML
    <br>
    <b>Penggunaan:</b>
    ```
    * {
        color: blue;
    }
    ```

6.  Pseudo
    Tipe ini memilih elemen yang didekorasi berdasarkan elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya. Ada pseudo-class dan pseudo-element.
    <br>
    <b>Penggunaan:</b>
    ```
    selector:hover {
        color: blue;
    }
    ```

## Implementasi Proyek

1.  Memilih template yang akan dilakukan styling
2.  Memulai styling dari login.html menggunakan eksternal css native login.css, setiap 
    selector CSS dalam login.css disesuaikan dengan class yang ada dalam login.html, tampilkan inspect elemen dalam browser untuk menyetel mode responsive ke device mobile dan tablet untuk menyetel CSS media dan menyusunnya dalam login.css.
    `login.html`
    ```
    <html>
    {% load static %}
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet"  href="{% static 'login.css' %}">

        <title>EuTodolist | Login</title>
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}"/>

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    </head>

    {% block content %}
    <body>
        <div class="login-container">
            <div class="login">
                <h1>EuTodolist Login</h1>
                
                <div class="login-form">
                    <form method="POST" action="">
                        {% csrf_token %}
                        <table>
                            <tr>
                                <td>Username</td>
                                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                            </tr>
                                    
                            <tr>
                                <td>Password</td>
                                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td><button onClick="myFunction()" class="btn login_btn" type="submit" value="Login">Login</button></td>
                                <td></td>
                            </tr>
                        </table>
                    </form>
                </div>
                    
                <div class="regist-ref">
                    Don't have an account yet? <a href="{% url 'todolist:register' %}">Create Account</a>
                </div>

                <div id="invalidinput">
                    {% if messages %}
                        {% for message in messages %}
                            {{ message }}
                        {% endfor %}
                    {% endif %}  
                </div>

            </div>
        </div>
    </body>
    {% endblock content %}
    <!-- script toast jika ada notification tidak valid -->
    <script>
    function myFunction() {
    var x = document.getElementById("invalidinput");
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 8000);
    }
    </script>
    </html>
    ```
    `login.css`
    ```
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    * {
        font-family: 'Poppins', sans-serif;
        cursor: pointer;
        color: white;  
    }
    
    body {
        margin-top: 32px;
        text-align:center;
        background-color: #1B1B1D;
    }

    .login-container {
        display: flex;
        justify-content: center;
        margin-top: 120px;
    }

    input {
        padding: 3px;
        border-radius: 6px;
        border: none;
        color: #1B1B1D;
        width: 160px;
    }

    .login-form {
        padding: 20px 20px; 
        background-color: #E3E3E3;
        border-radius: 8px;
    }

    td {
        color: #1B1B1D;
    }

    .login-form form table tr td {
        padding: 6px;
    }

    button {
        background-color: #1B1B1D;
        border: none;
        padding: 8px 28px;
        margin-top: 20px;
        border-radius: 6px;
    }

    button:hover {
        background-color: #25C2A0;
        color: white;
    }

    .regist-ref {
        margin-top: 20px;
        font-size: 14px;
    }

    .regist-ref a:hover {
        color: #25C2A0;
    }

    /* TOAST */

    #invalidinput {
        visibility: hidden;
        min-width: 250px;
        margin-left: -125px;
        background-color: rgb(131, 9, 9);
        color: #fff;
        text-align: center;
        border-radius: 8px;
        padding: 16px 24px;
        position: fixed;
        z-index: 1;
        left: 48%;
        bottom: 30px;
        font-size: 17px;
    }

    #invalidinput.show {
    visibility: visible;
    -webkit-animation: fadein 0.5s, fadeout 0.5s 2.5s;
    animation: fadein 0.5s, fadeout 0.5s 2.5s;
    }

    @-webkit-keyframes fadein {
    from {bottom: 0; opacity: 0;} 
    to {bottom: 30px; opacity: 1;}
    }

    @keyframes fadein {
    from {bottom: 0; opacity: 0;}
    to {bottom: 30px; opacity: 1;}
    }

    @-webkit-keyframes fadeout {
    from {bottom: 30px; opacity: 1;} 
    to {bottom: 0; opacity: 0;}
    }

    @keyframes fadeout {
    from {bottom: 30px; opacity: 1;}
    to {bottom: 0; opacity: 0;}
    }

    /* Mobile & Tab */
    @media only screen and (max-width: 768px) {
        body {
            margin-top: 32px;
            text-align:center;
            background-color: #1B1B1D;
        }
        
        .login-container .login h1 {
            font-weight: 600;
            font-size: 18px;
        }
        
        .login-form {
            padding: 10px 10px; 
            background-color: #E3E3E3;
            border-radius: 8px;
        }

        table {
            font-size: small;
        }
        
        button {
            background-color: #1B1B1D;
            border: none;
            padding: 8px 28px;
            margin-top: 10px;
            border-radius: 6px;
        }
        
        button:hover {
            background-color: #25C2A0;
            color: white;
        }
        
        .regist-ref {
            margin-top: 15px;
            font-size: 11px;
        }
        
        .regist-ref a:hover {
            color: #25C2A0;
        }
        
    }
    ```
    ![Res 1 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-05/responsive-01.jpg?raw=true)
    ![Res 2 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-05/responsive-02.jpg?raw=true)
3.  Menata halaman register.html
    `register.html`
    ```
    <html>
    {% load static %}
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet"  href="{% static 'register.css' %}">

        <title>EuTodolist | Sign Up</title>
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}"/>

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    </head>

    {% block content %}
    <div class="signup-container">
        <div class="signup">
            <h1>EuTodolist Sign Up</h1>  

                <form method="POST" >  
                    {% csrf_token %}  
                    <table cellspacing="0" cellpadding="0">  
                        {{ form.as_table }}  
                        <tr>  
                            <td></td>
                            <td><button type="submit" name="submit" value="Daftar"/>Sign Up</button></td>  
                        </tr>  
                    </table>  
                </form>

            <div class="regist-ref">
                Already have an account? <a href="{% url 'todolist:login' %}">Login Account</a>
            </div>

            <div id="invalidinput">
                {% if messages %}  
                    <ul>   
                        {% for message in messages %}  
                            <li>{{ message }}</li>  
                            {% endfor %}  
                    </ul>   
                {% endif %}
            </div>

        </div>  
    </div>
    <!-- script toast jika ada notification tidak valid -->
    <script>
        function myFunction() {
        var x = document.getElementById("invalidinput");
        x.className = "show";
        setTimeout(function(){ x.className = x.className.replace("show", ""); }, 8000);
        }
    </script>
    {% endblock content %}
    </html>
    ```
    `register.css`
    ```
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    * {
        font-family: 'Poppins', sans-serif;
        cursor: pointer;
        color: white;  
    }
    
    body {
        margin-top: 16px;
        text-align:center;
        background-color: #1B1B1D;
    }

    .signup-container {
        display: flex;
        justify-content: center;
        margin-top: 40px;
    }

    input {
        padding: 6px;
        border-radius: 6px;
        border: none;
        color: #1B1B1D;
        width: 200px;
    }

    .signup-form {
        padding: 20px 20px; 
        background-color: #E3E3E3;
        border-radius: 8px;
    }

    td {
        color: #1B1B1D;
    }

    form table tr td {
        padding: 20px;
    }

    button {
        background-color: #1B1B1D;
        border: none;
        padding: 8px 28px;
        margin-top: 20px;
        border-radius: 6px;
    }

    button:hover {
        background-color: #25C2A0;
        color: white;
    }

    .regist-ref {
        margin-top: 20px;
        font-size: 14px;
    }

    .regist-ref a:hover {
        color: #25C2A0;
    }

    table {
        background-color: #E3E3E3;
        padding: 40px 40px;
        border-radius: 8px;
        border: none;
    }

    table tbody tr th label {
        color:#1B1B1D;
    }

    .helptext {
        font-size: small;
        color:rgb(172, 94, 94);
    }

    .helptext ul li {
        font-size: small;
        color:rgb(172, 94, 94);
    }

    .errorlist li {
        color: white;
        font-size: small;
        background-color: rgb(172, 94, 94);
        padding: 4px;
        border-radius: 8px;
    }

    /* TOAST */

    #invalidinput {
        visibility: hidden;
        min-width: 250px;
        margin-left: -125px;
        background-color: rgb(131, 9, 9);
        color: #fff;
        text-align: center;
        border-radius: 8px;
        padding: 16px 24px;
        position: fixed;
        z-index: 1;
        left: 48%;
        bottom: 30px;
        font-size: 17px;
    }

    #invalidinput.show {
    visibility: visible;
    -webkit-animation: fadein 0.5s, fadeout 0.5s 2.5s;
    animation: fadein 0.5s, fadeout 0.5s 2.5s;
    }

    @-webkit-keyframes fadein {
    from {bottom: 0; opacity: 0;} 
    to {bottom: 30px; opacity: 1;}
    }

    @keyframes fadein {
    from {bottom: 0; opacity: 0;}
    to {bottom: 30px; opacity: 1;}
    }

    @-webkit-keyframes fadeout {
    from {bottom: 30px; opacity: 1;} 
    to {bottom: 0; opacity: 0;}
    }

    @keyframes fadeout {
    from {bottom: 30px; opacity: 1;}
    to {bottom: 0; opacity: 0;}
    }

    /* Mobile & Tab */
    @media only screen and (max-width: 768px) {
        table {
            background-color: #E3E3E3;
            padding: 0px 0px;
            border-radius: 8px;
            border: none;
            margin-top: 20px;
        }

        label {
            font-size: 11px;
        }

        h1 {
            font-size: 18px;
        }

        .signup-container {
            display: flex;
            justify-content: center;
            margin-top: 0px;
        }

        input {
            padding: 3px;
            border-radius: 3px;
            border: none;
            color: #1B1B1D;
            width: 150px;
        }

        .signup-form {
            padding: 10px 10px; 
            background-color: #E3E3E3;
            border-radius: 8px;
        }

        form table tr td {
            padding: 20px;
            max-width: 160px;
        }

        button {
            background-color: #1B1B1D;
            border: none;
            padding: 8px 28px;
            margin-top: 12px;
            border-radius: 6px;
        }

        .regist-ref {
            margin-top: none;
            font-size: 10px;
        }


        .helptext {
            font-size: 9px;
            color:rgb(172, 94, 94);
        }

        .helptext ul li {
            font-size: 9px;
            color:rgb(172, 94, 94);
            width: 100px;
        }

        .errorlist li {
            color: white;
            font-size: small;
            background-color: rgb(172, 94, 94);
            padding: 4px;
            border-radius: 8px;
        }
    }
    ```
    ![Res 3 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-05/responsive-03.jpg?raw=true)
    ![Res 4 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-05/responsive-04.jpg?raw=true)

4.  Menata create_task.html
    `create_task.html`
    ```
    <html>
    {% load static %}
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet"  href="{% static 'create_task.css' %}">

        <title>EuTodolist | Create Task</title>
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}"/>

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    </head>

    {% block content %}
    <body>

        <div class="create-task-container">
            <div class="create-task">
            <h1>Create New Task</h1>

                <div class="task-form">
                    <form action="/todolist/create-task/" method="POST">
                        {% csrf_token %}
                        <table cellspacing="0" cellpadding="0">  
                            {{ form.as_table }}
                        </table>  
                        <button type="submit">Add Task</button>
                    </form>   
                </div>

            </div>  
        </div>

        <br>
        <div class="back-button">
            <a href="{% url 'todolist:todolist' %}">< Back</a>
        </div>

    </body>

    {% endblock content %}
    </html>
    ```
    `create_task.css`
    ```
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    * {
        font-family: 'Poppins', sans-serif;
        cursor: pointer;
        color: white;  
    }
    
    body {
        margin-top: 32px;
        text-align:center;
        background-color: #1B1B1D;
    }

    .create-task-container {
        display: flex;
        justify-content: center;
        margin-top: 140px;
    }

    .task-form {
        padding: 20px 20px; 
        background-color: #E3E3E3;
        border-radius: 8px;
    }

    input {
        padding: 6px;
        border-radius: 6px;
        border: none;
        color: #1B1B1D;
        width: 300px;
    }

    button {
        background-color: #1B1B1D;
        border: none;
        padding: 8px 28px;
        margin-top: 20px;
        border-radius: 6px;
    }

    button:hover {
        background-color: #25C2A0;
        color: white;
    }

    table tbody tr th label {
        color:#1B1B1D;
    }

    td {
        color: #1B1B1D;
    }

    form table tr td {
        padding: 10px;
    }

    a {
        font-size: 14px;
        text-decoration: none;
    }

    a:hover {
        color: #25C2A0;
    }

    /* Mobile & Tab */
    @media only screen and (max-width: 768px) {        
        .task-form {
            padding: 10px 10px; 
            background-color: #E3E3E3;
            border-radius: 8px;
        }

        h1 {
            font-size: 18px;
        }
        
        input {
            padding: 6px;
            border-radius: 6px;
            border: none;
            color: #1B1B1D;
            width: 150px;
        }
        
        button {
            background-color: #1B1B1D;
            border: none;
            padding: 8px 20px;
            margin-top: 20px;
            border-radius: 6px;
            font-size: 11px;
        }

        table {
            font-size: small;
        }
        
        form table tr td {
            padding: 4px;
        }
        
        a {
            font-size: 11px;
            text-decoration: none;
        }
    }
    ```
    ![Res 5 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-05/responsive-05.jpg?raw=true)
    ![Res 6 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-05/responsive-06.jpg?raw=true)

5.  Menata todolist.html
    `todolist.html`
    ```
    <html>
    {% load static %}
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet"  href="{% static 'todolist.css' %}">

        <title>EuTodolist | Todolist</title>
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}"/>

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    </head>

    {% block content %}
    <body>
        <section class="navbar">
            <a href="{% url 'todolist:create_task' %}">
                <button class="add-task-button">
                    Create New Task
                </button>
            </a>
            <h1>
                Hi {{ username }}, this is your todolist!
            </h1>
            <a href="{% url 'todolist:logout' %}">
                <button class="logout-button"> 
                Logout
                </button>
            </a>
        </section>

        <section class="navbar-mobile">
            <h1 style="font-size:18px;">
                Hi {{ username }}, this is your todolist!
            </h1>
            <a href="{% url 'todolist:create_task' %}">
                <button class="add-task-button">
                    Create New Task
                </button>
            </a>
        </section>

        
        
        <div class="todolist">
            <div class="todolist-list">
                <div class="todolist-todo">
                    <h1 style="color:#e05d43;font-size:20px;">To Do</h1>
                    {% for todo in todolist %}
                        {% if todo.is_finished == False %}
                            <div class="task-card">
                                <p class="task-judul">{{todo.title}}</p>
                                <p class="task-deskripsi">{{todo.description}}</p>
                                <p class="task-tanggal">Created {{todo.date}}</p>
                                <!-- {% if todo.is_finished %}
                                <p>Status: Selesai</p>
                                {% else %}
                                <p>Status: Belum Selesai</p>
                                {% endif %} -->
                                <div class="task-tombol">
                                    <!-- pengubahan status dilakukan di penembakan url berikut -->
                                    <a href="/todolist/change-status/{{todo.id}}">
                                        <button type="submit" class="task-change-done">Finish >></button>
                                    </a>
                                    <!-- penghapusan task dilakukan di penembakan url berikut -->
                                    <a href="/todolist/delete-task/{{todo.id}}">
                                        <button type="submit" class="task-delete">Delete</button>
                                    </a>
                                </div>
                            </div>
                            <div class="sekat-vertikal"></div>
                        {% endif %}
                    {% endfor %}
                </div>
                <div class="sekat-horizontal"></div>
                <div class="todolist-done">
                    <h1 style="color:#25C2A0;font-size:20px;">Done</h1>
                    {% for todo in todolist %}
                        {% if todo.is_finished %}
                            <div class="task-card">
                                <p class="task-judul">{{todo.title}}</p>
                                <p class="task-deskripsi">{{todo.description}}</p>
                                <p class="task-tanggal">Created {{todo.date}}</p>
                                <!-- {% if todo.is_finished %}
                                <p>Status: Selesai</p>
                                {% else %}
                                <p>Status: Belum Selesai</p>
                                {% endif %} -->
                                <div class="task-tombol">
                                    <!-- pengubahan status dilakukan di penembakan url berikut -->
                                    <a href="/todolist/change-status/{{todo.id}}">
                                        <button type="submit" class="task-change-todo"><< Rework</button>
                                    </a>
                                    <!-- penghapusan task dilakukan di penembakan url berikut -->
                                    <a href="/todolist/delete-task/{{todo.id}}">
                                        <button type="submit" class="task-delete">Delete</button>
                                    </a>
                                </div>
                            </div>
                            <div class="sekat-vertikal"></div>
                        {% endif %}
                    {% endfor %}
                </div>
            </div>
        </div>

        <section class="logout-mobile">
            <a href="{% url 'todolist:logout' %}">
                <button class="logout-button"> 
                Logout
                </button>
            </a>
        </section>

        <div class="sekat-vertikal"></div>
        <div class="sekat-vertikal"></div>
        <div class="sekat-vertikal"></div>

    </body>
    {% endblock content %}
    </html>
    ```
    `todolist.css`
    ```
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    * {
        font-family: 'Poppins', sans-serif;
        cursor: pointer;
        color: #1B1B1D; 
    }
    
    body {
        margin-top: 32px;
        text-align:center;
        background-color: #1B1B1D;
    }

    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .navbar-mobile {
        display: none;
    }

    .logout-mobile {
        display: none;
    }

    .add-task-button {
        background-color: #25C2A0;
        padding: 10px 30px;
        border: none;
        margin-left: 20px;
        border-radius: 6px;
        font-weight: 600;
    }

    .logout-button {
        background-color: #e05d43;
        padding: 10px 30px;
        border: none;
        margin-right: 20px;
        border-radius: 6px;
        font-weight: 600;
    }

    .add-task-button:hover {
        color: white;
    }

    .logout-button:hover {
        color: white;
    }

    .todolist {
        display: flex;
        justify-content: center;
    }

    .todolist-list {
        display: flex;
    }

    .task-card {
        background-color: #E3E3E3;
        padding: 10px 30px 20px;
        border-radius: 12px;
        text-align: left;
        width: 25rem;
        box-shadow: 6px 6px #888888;
        /* animation */
        transform: scale(1.0);
        transition-duration: 0.2s;
        opacity: 0.9;
    }

    .task-card:hover {
        /* animation */
        transform: scale(1.03);
        transition-duration: 0.2s;
        opacity: 1;
    }

    .task-card .task-judul {
        font-weight: 800;
    }

    .task-card .task-deskripsi {
        font-size: small;
    }

    .task-card .task-tanggal {
        text-align: right;
        font-size: 11px;
        font-style: italic;
        color: #888888;
        font-weight: 300;
    }

    .task-card .task-tombol {
        display: flex;
        justify-content: space-between;
    }

    .task-card .task-tombol .task-change-done {
        background-color: #E3E3E3;
        border: 2px solid #c2c0c0;
        padding: 6px 20px;
        border-radius: 6px;
        font-size: small;
    }

    .task-card .task-tombol .task-change-done:hover {
        background-color: #66dec4;
        border: 2px solid #66dec4;
    }

    .task-card .task-tombol .task-change-todo {
        background-color: #E3E3E3;
        border: 2px solid #c2c0c0;
        padding: 6px 20px;
        border-radius: 6px;
        font-size: small;
    }

    .task-card .task-tombol .task-change-todo:hover {
        background-color: #f7b0a2;
        border: 2px solid #f7b0a2;
    }

    .task-card .task-tombol .task-delete {
        background-color: #E3E3E3;
        border: 2px solid #e05d43;
        padding: 6px 20px;
        border-radius: 6px;
        font-size: small;
        font-weight: 600;
        color: #e05d43;
    }

    .task-card .task-tombol .task-delete:hover {
        background-color: #e05d43;
        border: 2px solid #e05d43;
        color: white;
    }

    .sekat-horizontal {
        width: 40px;
    }

    .sekat-vertikal {
        height: 20px;
    }

    h1 {
        color: white;
        font-size: 24px;
    }

    /* Mobile & Tab */
    @media only screen and (max-width: 990px) {
        body {
            margin-top: 32px;
            text-align:center;
            background-color: #1B1B1D;
        }
        
        .navbar {
            display: none;
        }

        .navbar-mobile {
            display: block;
            justify-content: center;
            align-items: center;
            padding: 10px 40px;
        }

        .logout-mobile {
            display: block;
            justify-content: center;
            margin-top: 40px;
        }
        
        .add-task-button {
            background-color: #25C2A0;
            padding: 10px 20px;
            border: none;
            margin-top: 20px;
            margin-left: 0px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 11px;
        }
        
        .logout-button {
            background-color: #e05d43;
            padding: 10px 20px;
            border: none;
            margin-right: 0px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 11px;
        }
        
        .add-task-button:hover {
            color: white;
        }
        
        .logout-button:hover {
            color: white;
        }
        
        .todolist {
            display: flex;
            justify-content: center;
        }
        
        .todolist-list {
            display: block;
            margin-top: 20px;
        }
        
        .task-card {
            background-color: #E3E3E3;
            padding: 4px 30px 14px;
            border-radius: 12px;
            text-align: left;
            width: 16rem;
            box-shadow: 6px 6px #888888;
            /* animation */
            transform: scale(1.0);
            transition-duration: 0.2s;
            opacity: 0.9;
        }
        
        .task-card:hover {
            /* animation */
            transform: scale(1.03);
            transition-duration: 0.2s;
            opacity: 1;
        }
        
        .task-card .task-judul {
            font-weight: 800;
            font-size: 14px;
        }
        
        .task-card .task-deskripsi {
            font-size: 10px;
        }
        
        .task-card .task-tanggal {
            text-align: right;
            font-size: 9px;
            font-style: italic;
            color: #888888;
            font-weight: 300;
        }
        
        .task-card .task-tombol {
            display: flex;
            justify-content: space-between;
        }
        
        .task-card .task-tombol .task-change-done {
            background-color: #E3E3E3;
            border: 2px solid #c2c0c0;
            padding: 6px 20px;
            border-radius: 6px;
            font-size: 10px;
        }
        
        .task-card .task-tombol .task-change-done:hover {
            background-color: #66dec4;
            border: 2px solid #66dec4;
        }
        
        .task-card .task-tombol .task-change-todo {
            background-color: #E3E3E3;
            border: 2px solid #c2c0c0;
            padding: 6px 20px;
            border-radius: 6px;
            font-size: 10px;
        }
        
        .task-card .task-tombol .task-change-todo:hover {
            background-color: #f7b0a2;
            border: 2px solid #f7b0a2;
        }
        
        .task-card .task-tombol .task-delete {
            background-color: #E3E3E3;
            border: 2px solid #e05d43;
            padding: 6px 20px;
            border-radius: 6px;
            font-size: 10px;
            font-weight: 600;
            color: #e05d43;
        }
        
        .task-card .task-tombol .task-delete:hover {
            background-color: #e05d43;
            border: 2px solid #e05d43;
            color: white;
        }
        
        .sekat-horizontal {
            width: 40px;
        }
        
        .sekat-vertikal {
            height: 20px;
        }
        
        h1 {
            color: white;
            font-size: 24px;
        }
    }
    ```
    ![Res 7 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-05/responsive-07.jpg?raw=true)
    ![Res 8 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-05/responsive-08.jpg?raw=true)

## BONUS

Implementasi hover pada card sebagai berikut, jika dihover maka:
1. Skala bertambah 3%
2. Opacity 100%
3. Durasi perubahan adalah 0.2s
```
.task-card {
    background-color: #E3E3E3;
    padding: 10px 30px 20px;
    border-radius: 12px;
    text-align: left;
    width: 25rem;
    box-shadow: 6px 6px #888888;
    /* animation */
    transform: scale(1.0);
    transition-duration: 0.2s;
    opacity: 0.9;
}

.task-card:hover {
    /* animation */
    transform: scale(1.03);
    transition-duration: 0.2s;
    opacity: 1;
}
```