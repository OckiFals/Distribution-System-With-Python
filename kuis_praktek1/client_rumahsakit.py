import json
import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://127.0.0.1:6666/")


try:
    while True:
        print ""
        print "Sistem Informasi Pasien"
        print "1. Masukkan data pasien"
        print "2. Lihat data pasien"
        print "3. Keluar"
        operasi = input("Pilih operasi : ")
        if operasi == 1:
            print ""
            print "Masukkan data pasien"
            nik = raw_input("NIK : ")
            nama = raw_input("Nama : ")
            alamat = raw_input("Alamat : ")
            penyakit = raw_input("Penyakit : ")
            poli = input("Pilihan poli : 1) Umum, 2) Jantung, 3) Paru : ")

            print proxy.tambahdata(
                json.dumps({
                    'nik': nik,
                    'nama': nama,
                    'alamat': alamat,
                    'penyakit': penyakit,
                    'poli': poli
                })
            )

        elif operasi == 2:
            print ""
            nik = raw_input("NIK Pasien : ")
            print "Data Pasien dengan NIK ", nik
            print proxy.bacadata(
                json.dumps({
                    'nik': int(nik)
                })
            )

        else:
            print ""
            print "Keluar dari program"
            break
except KeyboardInterrupt:
    print "Keluar dari program"
