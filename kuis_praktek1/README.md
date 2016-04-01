Kuis Praktek Sistem Terdistribusi
===================================
Rancangan Sistem
----------------
Sebuah rumah sakit meminta anda untuk membuat sistem informasi untuk
mendata pasien sekaligus memberikan notifikasi ke dokter spesialis sesuai dengan jenis
poli yang dituju oleh pasien.
Pada sistem tersebut, terdapat beberapa entitas antara lain :
### A. Client Rumah Sakit
Entitas client bertugas untuk memasukkan dan melihat data pasien. Data yang
dimasukkan antara lain adalah data : NIK (Nomor Induk Kependudukan), Nama, Alamat,
Penyakit dan Pilihan Poli. Pada setiap rumah sakit terdapat beberapa pilihan poli antara
lain Poli Umum, Poli Jantung, dan Poli Paru. Data tersebut selanjutnya dikirim ke server
rumah sakit lewat mekanisme RPC. Selain itu, entitas client juga dapat dipakai untuk
melihat data pasien yang sudah tersimpan pada server.
Sebagai catatan, pada setiap entitas dalam sistem, data pasien dikirimkan/diterima
sekaligus dalam bentuk JSON.
### B. Server Rumah Sakit
Terdapat 1 server rumah sakit dengan antar muka RPC yang berperan menerima
data pasien dari client. Terhadap inputan data tersebut, server rumah sakit melakukan
dua aktifitas :

1. Menyimpan data pasien ke sebuah list/dictionary Python.
2. Melakukan publish data pasien ke subscriber dokter spesialis sesuai dengan poli

yang dituju oleh pasien dengan protokol MQTT. Data di-publish dalam formatJSON.
### C. Subscriber Dokter Spesialis
Terdapat entitas dokter spesialis yang menerima notifikasi pasien baru dari entitas
Server Rumah Sakit. Dokter spesialis hanya menerima notifikasi sesuai dengan poli
bidangnya. Contoh : dokter umum hanya menerima pasien pada Poli Umum dan dokter
spesialis jantung hanya menerima pasien pada Poli Jantung.
### D. Broker
Broker bertugas menghubungkan semua rumah sakit dengan protokol MQTT.
Ketentuan Tambahan

1. Kerangka program client dapat diunduh pada folder yang sama dengan soal ini.
2. Program untuk Client Rumah Sakit diberi nama client_rumahsakit.py
3. Program untuk Server Rumah Sakit diberi nama server_rumahsakit.py dan berjalan
pada port 6666.
4. Program Subscriber Dokter Spesialis diberi nama sesuai dengan polinya :
sub_umum.py, sub_jantung.py dan sub_paru.py.
5. Broker berjalan pada port 1883.
6. Semua file code dimasukkan dalam folder dengan format SISTER_namakelas_nim.
Contoh : SISTER_B_12000111000. Pada folder tersebut sertakan file text berisi nama
dan NIM, kemudian di zip dengan nama yang sama.
