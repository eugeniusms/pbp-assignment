## Perbedaan Asynchronous dengan Synchronous Programming

1.  Asynchronous programming memiliki pendekatan pemrograman yang tidak terikat pada I/O Protocol. Pemrograman asynchronous tidak melakukan pekerjaannya dengan cara lama (eksekusi baris program satu persatu sesuai paradigma dan urutan program dalam kode). Asynchronous programming menjalankan program tanpa harus terikat dengan proses lain atau dapat disebut program berjalan secara independen.

2.  Synchronous programming memiliki pendekatan pemrograman gaya lama. Program akan dieksekusi satu persatu sesuai dengan urutan dan prioritasnya. Hal ini memiliki kekurangan pada lama waktu eksekusi karena masing-masing pekerjaan harus menunggu pekerjaan lain selesai untuk diproses terlebih dahulu.

## Penerapan Paradigma Event-Driven Programming

Event-driven adalah suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event yang merupakan keluaran atau tindakan pengguna, atau bisa berupa pesan dari program lainnya. 

Penerapan paradigma tersebut dalam tugas ini contohnya adalah ketika pengguna menekan tombol "Create New Task", maka program akan menampilkan modal berisikan form. Lalu ketika pengguna mengisi form tersebut dan menekan tombol "Add Todo", maka program akan menambahkan data baru ke dalam Todolist sehingga Todolist saat ini bertambah sejumlah satu todo. Tombol yang diklik dalam alur tersebut disebut sebagai event.


## Penerapan Asynchronous Programming pada AJAX

1.  Tambahkan `<script>` yang memuat sebuah program JavaScript
2.  Tambahkan library AJAX berikut pada `<head>`
    ```
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    ```
3.  Tambahkan program AJAX di dalam tag tersebut seperti $.ajax({...}) sesuai dengan alur dan fitur program yang diinginkan
4.  Saat pengguna memiliki sebuah event atau permintaan ke server, maka event dari user ini akan diproses ke AJAX
5.  AJAX akan menampung semua event dari pengguna dan melakukan transfer data
6.  Data yang berasal dari pengguna kemudian diproses secara server-side dengan metode asynchronous
7.  Hasil dari proses data ini akan kemudian akan memperbarui halaman secara langsung
8.  Pengguna tidak perlu melakukan reload halaman, halaman telah terperbarui dengan data baru di dalamnya

## Implementasi Proyek

1.  Membuat view baru bernama show_json yang digunakan untuk mengembalikan seluruh data berupa json sesuai dengan filter `user=request.user` (user yang sedang login)
2.  Membuat path baru di dalam urls.py `/todolist/json` yang mengarah ke fungsi show_json dalam views.py
4.  Membuat template baru todolist_ajax.html untuk template yang menerapkan konsep AJAX dan mengarahkan url utama dari `/todolist` ke todolist_ajax.html
5.  Menambahkan library ajax yaitu `<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>` ke dalam head dari template
6.  Menambahkan AJAX GET ke alamat `/todolist/json`
    `AJAX GET`
    ```
    $.get('/todolist/json', function (todolist) {
        todolist.map((todo) => {
            if (todo.fields.is_finished) {
                $('#todo-finish-card').append(todoCard(todo))
            } else {
                $('#todo-unfinish-card').append(todoCard(todo))
            }
            deleteTodoCard(todo)
        })
    })
    ```
    AJAX GET tersebut digunakan untuk mendapatkan data yang diperoleh dari json sesuai alamat tertera, data yang masuk akan diproses jika is_finished maka akan ditambahkan ke dalam container dengan id="todo-finish-card" jika sebaliknya akan ditambahkan ke dalam container dengan id="todo-unfinish-card"
7.  Membuat tombol "Add Task" yang membuka sebuah modal dengan form menambahkan task
    `button trigger modal`
    ```
    <button id="addTodoButton" class="add-task-button">Create New Task</button>
    ```
    `modal`
    ```
    <div id="modalTodo" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <div class="create-task-container">
                <div class="create-task">
                <h1>Create New Task</h1>
        
                <div class="task-form">
                    <form action="" method="POST">
                        {% csrf_token %}
                        <table>
                        <tr>
                            <td><span>Title</span></td>
                            <td><input type="text" name="title" id="title" placeholder="title" required/></td>
                        </tr>
                        <tr>
                            <td><span>Description&nbsp;&nbsp;</span></td>
                            <td><input type="textarea" name="description" id="description" placeholder="description" required/></tr>
                        </tr>
                        </table>
                        <button type="submit" id="add-todo">Add Todo</button>
                    </form>   
                </div>
        
                </div>  
            </div>
        </div>
    </div>
    ```
    `style`
    ```
    .modal {
        display: none; /* Hidden by default */
        position: fixed; /* Stay in place */
        z-index: 1; /* Sit on top */
        padding-top: 100px; /* Location of the box */
        left: 0;
        top: 0;
        width: 100%; /* Full width */
        height: 100%; /* Full height */
        overflow: auto; /* Enable scroll if needed */
        background-color: rgb(0,0,0); /* Fallback color */
        background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
    }
    
    /* Modal Content */
    .modal-content {
        background-color: #1B1B1D;
        margin: auto;
        padding: 20px;
        border: 1px solid #888;
        border-radius: 10px;
        width: 30%;
    }

    /* The Close Button */
    .close {
        color: #aaaaaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
    }

    .close:hover, .close:focus {
        color: #e05d43;
        text-decoration: none;
        cursor: pointer;
    }

    .task-form {
        display: flex;
        justify-content: center;
        padding: 20px 20px; 
        background-color: #E3E3E3;
        border-radius: 8px;
    }

    .task-form form input {
        margin-bottom: 12px;
        padding: 6px;
        border-radius: 6px;
        border: none;
        color: #1B1B1D;
        width: 260px;
    }

    .task-form form button {
        background-color: #1B1B1D;
        border: none;
        padding: 8px 28px;
        margin-top: 20px;
        border-radius: 6px;
        color:white;
    }

    .task-form form button:hover {
        background-color: #25C2A0;
        color: white;
    }

    .task-form form span {
        color: #1B1B1D;
        font-weight: 600;
    }
    ```
8.  Membuat view baru dalam views.py untuk menambahkan task baru ke dalam database. View yang saya buat bernama "add_todo" dengan csrf_exempt.
9.  Menambahkan path yang mengarah ke view add_todo yaitu `/todolist/add`
10. Menghubungkan form yang telah disusun ke path `/todolist/add`
    `AJAX POST`
    ```
    $('#add-todo').click(function () {
        if ($('#title').val() && $('#description').val()) {
            $.post(
                url = '/todolist/add/',
                data = {
                    title: $('#title').val(),
                    description: $('#description').val(),
                },
            )
        }
    })
    ```
    Untuk HTML tag dengan id="add-todo" jika diklik maka akan melakukan POST data title dan description ke url = `/todolist/add/`
11. Modal akan otomatis tertutup ketika user berhasil menambahkan todo

## BONUS

1.  Membuat AJAX DELETE untuk tiap button delete pada setiap card yang ada dalam todolist
    `AJAX DELETE`
    ```
    const deleteTodoCard = (todo) => {
        $(`#${todo.pk}-delete`).click(function () {
        $.ajax({
                headers: {
                    'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                },
                url: `/todolist/delete-task/${todo.pk}`,
                type: 'DELETE',
                success: function (response) {
                    $(`#${todo.pk}`).remove()
                },
            })
        })
    }
    ```
    Jika user melakukan klik pada tag HTML (button delete) yang memiliki id="{todo.pk}-delete" secara dinamis maka card object dengan id="{todo.pk}" akan dihapus dari halaman
2.  Membuat view dalam views.py yang mengarahkan penghapusan data dengan id tertentu
3.  Membuat path /todolist/delete/{id} yang menerima ID dari path dan meneruskannya kepada view
4.  Membuat fungsi JavaScript "deleteTodoCard" fungsi dapat dilihat di atas (digunakan untuk memanggil endpoint penghapusan task yaitu `/todolist/delete-task/${todo.pk}`)  
