import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer


def add(a, b):
    return a+b

def substract(a, b):
    return a-b

server = SimpleXMLRPCServer(('', 8888))
server.register_function(add, 'tambah')
server.register_function(substract, 'kurang')

server.serve_forever()