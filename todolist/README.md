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
