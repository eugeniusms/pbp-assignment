# PBP Tugas 02
Eugenius Mario Situmorang (NPM 2106750484)
<br/>
Link Deploy: https://pbp-tugas-02-eugeniusms.herokuapp.com/katalog/
<br/>

## Bagan request client dan response - Django
![Django Flow by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/django-flow.jpg?raw=true)
Penjelasan:
1. Client membuka browser untuk mengakses website
2. Client masuk ke dalam website, maka web server melayani request dari client
3. WSGI memproses HTTP server untuk website berbasis Python 
4. Middleware menjembatani integrasi teknologi yang digunakan dalam proyek untuk memproses request
5. URL Router mengarahkan alamat proyek sesuai permintaan client (urls.py), dari sini diarahkan 
   menuju fungsi yang berada di views.py
6. Views (views.py) menyusun apa saja yang akan ditampilkan ke template (html), data yang 
   diproses diambil dari database yang telah disusun dengan ORM di dalam models.py
7. Context processor menembakkan data dari views.py menuju template (html)
8. Template (html) menampilkan tampilan depan dari proyek berdasarkan data context yang ditembak 
   dari views.py dan alur logika dari template tags
9. Middleware menjembatani integrasi teknologi yang digunakan dalam proyek untuk memproses 
   response
10. WSGI memproses HTTP server untuk website berbasis Python
11. Web server melayani response dari server untuk dikirimkan ke client
12. Client mendapatkan response dari web server

## Mengapa perlu virtual environment?

Virtual environment diperlukan agar sistem dapat berjalan di lingkungan terisolasi.
Di mana setiap proyek memiliki kebutuhan/dependensi yang berbeda-beda antara proyek satu
dengan proyek yang lainnya. Dengan virtual environment, maka proyek dapat berjalan sesuai
dependensinya tanpa melakukan konfigurasi pada sistem operasi yang digunakan. "requirements.txt"
digunakan sebagai pencatatan daftar dependensi dari suatu proyek yang dijalankan dalam virtual
environment tertentu. Hanya dengan mengetahui daftar dependensi yang ada melalui "requirements.txt" sebuah mesin host contohnya "heroku" dapat mengetahui apa saja dependensi yang harus digunakan untuk menjalankan server. Hal ini juga memudahkan dalam proses penyimpanan di mana user
tidak perlu melakukan push pada virtual environment karena sudah dicatat dengan baik di "requirements.txt" (virtual environment adalah directory yang cukup memakan penyimpanan repository/host sehingga menghilangkannya dengan .gitignore dapat merampingkan proyek)

## Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Jika hanya dilakukan di dalam lingkungan local server maka hal ini dapat dilakukan. Pengguna dapat hanya dengan menggunakan environment Python bawaan dari komputer (root) untuk menginstal dependensi yang dibutuhkan proyek Django sehingga proyek Django dapat berjalan di server "local." Akan tetapi, jika untuk dijalankan di online hoster hal ini cukup susah dilakukan karena server host akan mencari daftar dependensi yang ada di dalam "requirements.txt" untuk disesuaikan dengan paket dependensi yang dimiliki mesin hosting. Jika "requirements.txt" tidak ada karena tidak diinisialisasikan virtual environmentnya, maka mesin host tidak pernah tahu dependensi apa saja yang diperlukan untuk menjalankan server sehingga proyek juga tidak akan berjalan.

## Implementasi struktur proyek
1. Membuat fungsi show_katalog yang digunakan untuk melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah html
   `/katalog/views.py`
   ![Django Implementasi 1 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/implementasi-01.jpg?raw=true)
2. Membuat sebuah routing untuk memetakan fungsi show_katalog. Routing: "katalog/" menuju katalog.urls
   `/project_django/urls.py`
   ![Django Implementasi 2 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/implementasi-02.jpg?raw=true)
3. Pada urls.py yang ada di katalog path "" langsung memetakan fungsi show_katalog
   `/katalog/urls.py`
   ![Django Implementasi 3 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/implementasi-03.jpg?raw=true)
4. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template
   `/katalog/templates/katalog.html`
   ![Django Implementasi 4 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/implementasi-04.jpg?raw=true)
5. Menggunakan css di static untuk menghias tampilan template katalog.html
   `/katalog/static/katalog.css`
   ![Django Implementasi 5 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/implementasi-05.jpg?raw=true)
6. Membuat aplikasi di Heroku dan menyambungkannya dengan GitHub
   `https://dashboard.heroku.com/`
   ![Django Implementasi 6 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/implementasi-06.jpg?raw=true)
7. Menambahkan Secrets di GitHub repository
   `https://github.com/eugeniusms/pbp-tugas-02`
   ![Django Implementasi 7 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/implementasi-07.jpg?raw=true)
8. Menjalankan ulang workflows yang gagal
   `https://github.com/eugeniusms/pbp-tugas-02`
   ![Django Implementasi 8 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/implementasi-08.jpg?raw=true)
9. Mengakses laman proyek yang telah dideploy
   `https://pbp-tugas-02-eugeniusms.herokuapp.com/katalog/`
   ![Django Implementasi 9 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/implementasi-09.jpg?raw=true)

## Test
References:
- https://www.youtube.com/playlist?list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM
- https://docs.djangoproject.com/en/4.1/ref/urlresolvers/
- https://github.com/TheDumbfounds/django-testing-tutorial
- https://www.educba.com/django-reverse/

### Unit Tests
- Test one piece independently of other pieces
- Fastest to run
```shell
python manage.py test katalog
```

### Integration Tests
- Test multiple pieces together to assure that they work well with one together

### Functional Tests
- Test that everything works from the end-user's point of view
- Slowest to run
```shell
python manage.py test functional_tests
```

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.