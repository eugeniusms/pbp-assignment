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
