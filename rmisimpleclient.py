import Pyro4


remote_obj = Pyro4.Proxy("PYRO:penghitung@127.0.0.1:8888")
remote_obj_2 = Pyro4.Proxy("PYRO:penghitung_2@127.0.0.1:8888")

print 'From obj 1.tambah(1, 2) = %s' % (remote_obj.tambah(1, 2))
print 'From obj 2.kurang(2, 2) = %s' % (remote_obj_2.kurang(2, 2))
