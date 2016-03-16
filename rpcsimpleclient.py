import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://127.0.0.1:8888/")

hasil_tambah = proxy.tambah(1, 2)
hasil_kurang = proxy.kurang(3, 2)

print "Hasil tambah", hasil_tambah
print "Hasil kurang", hasil_kurang
