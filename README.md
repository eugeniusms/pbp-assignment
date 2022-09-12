# PBP Tugas 02
Eugenius Mario Situmorang (NPM 2106750484)
<br/>
Link Deploy: https://pbp-tugas-02-eugeniusms.herokuapp.com/katalog/
<br/>

## Bagan request client dan response - Django
![Django Flow by Eugenius Mario Situmorang](https://github.com/eugeniusms/pbp-tugas-02/blob/main/assets/images/django-flow.jpg?raw=true)

## Mengapa perlu virtual environment?

Virtual environment diperlukan agar sistem dapat berjalan di lingkungan terisolasi.
Di mana setiap proyek memiliki kebutuhan/dependensi yang berbeda-beda antara proyek satu
dengan proyek yang lainnya. Dengan virtual environment, maka proyek dapat berjalan sesuai
dependensinya tanpa melakukan konfigurasi pada sistem operasi yang digunakan. "requirements.txt"
digunakan sebagai pencatatan daftar dependensi dari suatu proyek yang dijalankan dalam virtual
environment tertentu. Hanya dengan mengetahui daftar dependensi yang ada melalui "requirements.txt" sebuah mesin host contohnya "heroku" dapat mengetahui apa saja dependensi yang harus digunakan untuk menjalankan server. Hal ini juga memudahkan dalam proses penyimpanan di mana user
tidak perlu melakukan push pada virtual environment karena sudah dicatat dengan baik di "requirements.txt" (virtual environment adalah directory yang cukup memakan penyimpanan repository/host sehingga menghilangkannya dengan .gitignore dapat merampingkan proyek)

## Cara Menggunakan

Apabila kamu ingin menggunakan repositori ini sebagai repositori awalan yang nantinya akan kamu modifikasi:

1. Buka laman GitHub repositori templat kode, lalu klik tombol "**Use this template**"
   untuk membuat salinan repositori ke dalam akun GitHub milikmu.
2. Buka laman GitHub repositori yang dibuat dari templat, lalu gunakan perintah
   `git clone` untuk menyalin repositorinya ke suatu lokasi di dalam sistem
   berkas (_filesystem_) komputermu:

   ```shell
   git clone <URL ke repositori di GitHub> <path ke suatu lokasi di filesystem>
   ```
3. Masuk ke dalam repositori yang sudah di-_clone_ dan jalankan perintah berikut
   untuk menyalakan _virtual environment_:

   ```shell
   python -m venv env
   ```
4. Nyalakan environment dengan perintah berikut:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```
5. Install dependencies yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut:

   ```shell
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi Django menggunakan server pengembangan yang berjalan secara
   lokal:

   ```shell
   python manage.py runserver
   ```
7. Bukalah `http://localhost:8000` pada browser favoritmu untuk melihat apakah aplikasi sudah berjalan dengan benar.

## Contoh Deployment 

Pada template ini, deployment dilakukan dengan memanfaatkan GitHub Actions sebagai _runner_ dan Heroku sebagai platform Hosting aplikasi. 

Untuk melakukan deployment, kamu dapat melihat instruksi yang ada pada [Tutorial 0](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-0).

Untuk contoh aplikasi Django yang sudah di deploy, dapat kamu akses di [https://django-pbp-template.herokuapp.com/](https://django-pbp-template.herokuapp.com/)

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.