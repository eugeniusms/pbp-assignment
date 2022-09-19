# PBP Tugas 03
Eugenius Mario Situmorang (NPM 2106750484)
<br/>

Link Deploy: https://pbp-tugas-02-eugeniusms.herokuapp.com/

<br/>

HTML | XML | JSON
--- | --- | --- 
https://pbp-tugas-02-eugeniusms.herokuapp.com/mywatchlist/html/ | https://pbp-tugas-02-eugeniusms.herokuapp.com/mywatchlist/xml/ | https://pbp-tugas-02-eugeniusms.herokuapp.com/mywatchlist/json/ 

<br/>

## Perbedaan JSON, XML, dan HTML

HTML | XML | JSON
--- | --- | --- 
Berbasis markup language | Berbasis markup language | Berbasis notasi objek dalam JavaScript
Dapat memunculkan pemetaan data dari sebuah array sesuai framework yang digunakan | Tidak mendukung tipe data array | Mendukung tipe data array
Terdapat banyak argumen tag | Cukup susah dibaca dan diartikan | Struktur lebih sederhana sehingga mudah dibaca
Memiliki tag pembuka dan penutup | Memiliki tag pembuka dan penutup | Tidak memerlukan pembuka maupun penutup tag
Memiliki lebih banyak fitur terintegrasi | Lebih aman | Kurang begitu aman
Mendukung comments | Mendukung comments | Tidak mendukung comments
Mendukung banyak jenis encoding | Mendukung lebih banyak jenis encoding | Hanya mendukung encoding UTF-8
Digunakan untuk menampilkan susunan depan laman | Digunakan untuk transfer data | Digunakan untuk transfer data

## Mengapa perlu data delivery dalam pengimplementasian sebuah platform?

Implementasi di dunia nyata menuntut adanya perubahan data yang dinamis, artinya setiap data yang tersimpan di dalam laman selalu berubah kapan saja (data tidak tetap/statis). Jika hanya menggunakan data yang ada (tetap) maka pengguna hanya dapat menggunakan untuk keperluan yang sederhana tanpa adanya pemrosesan data. Dengan adanya pemrosesan data maka laman dapat melakukan transfer data antartabel di dalam database maupun antar aplikasi/website satu dan yang lain. Pemrosesan data secara masif tidak bisa hanya dilakukan oleh manusia dengan update data secara manual dari database ke laman. Oleh karena itu, HTTP Protocols membantu pengembang untuk melakukan transfer data menggunakan method-method seperti GET, POST, UPDATE, dan DELETE secara otomatis ke dalam server pengembang. Sisi server adalah sisi yang berada di belakang layar (backend), di bagian ini data diolah dengan program backend yang telah disusun pengembang backend untuk dilakukan "data delivery" ke sisi frontend agar bisa ditampilkan ke halaman website yang dapat dilihat dan digunakan oleh pengguna. Konsep data delivery dapat memudahkan pengembangan suatu aplikasi, contohnya pada efisiensi pekerjaan pengembang. Pengembang frontend hanya perlu menggunakan HTTP Protocols untuk mendapatkan serta mengirimkan data ke bagian backend. Begitu juga dengan bagian backend, pengembang hanya perlu memanfaatkan HTTP Protocols untuk menerima perintah dari bagian frontend tentang pemrosesan suatu data. Selain dalam aplikasi, data juga dapat dikirimkan untuk kebutuhan aplikasi lain.

## Implementasi struktur proyek

1. Membuat aplikasi dengan command 
   ```shell
   python manage.py startapp mywatchlist
   ```
2. Menambahkan path 
   ```shell
   path('mywatchlist/', include('mywatchlist.urls'))
   ```
   ke dalam `/project_django/urls.py`
   lalu juga path
   ```shell
   path('', show_html, name='show_watchlist')
   ```
   ke dalam `/mywatchlist/urls.py`
3. Membuat model dengan property watched, title, rating, release_date, dan review di `/mywatchlist/models.py`
   ```shell
   class MyWatchList(models.Model):
        watched = models.BooleanField()
        title = models.CharField(max_length=255)
        rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)]) 
        release_date = models.DateField() 
        review = models.TextField()
   ```
   Serta enambahkan validator untuk nilai terkecil dan terbesar rating

## Postman Screenshot
1. HTML
   `[GET] http://localhost:8000/mywatchlist/html/`
   ![Postman 1 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-03/postman-01.png?raw=true)
2. XML
   `[GET] http://localhost:8000/mywatchlist/xml/`
   ![Postman 2 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-03/postman-02.png?raw=true)
3. JSON
   `[GET] http://localhost:8000/mywatchlist/json/`
   ![Postman 3 by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/tugas-03/postman-03.png?raw=true)

### Run Tests
```shell
python manage.py collectstatic
python manage.py test
```

## Credits
Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.