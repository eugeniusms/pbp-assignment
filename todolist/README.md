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


