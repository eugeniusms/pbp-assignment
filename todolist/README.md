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
    <b>Kekurangan:</b>
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
    <b>Kekurangan:</b>
    - Meningkatkan waktu akses website
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
    <b>Kekurangan:</b>
    - Halaman belum tampil secara sempurna hingga file CSS selesai dipanggil


