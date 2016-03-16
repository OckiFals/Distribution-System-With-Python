#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama 135150207111060
"""

import sys
from SimpleXMLRPCServer import SimpleXMLRPCServer


class RPCnodeOne:
    def __init__(self):
        self.targetip = '127.0.0.1' if len(sys.argv) is not 2 else sys.argv[1]
        self.targetport = '8084' if len(sys.argv) is not 3 else sys.argv[2]

    def createconnection(self):
        return SimpleXMLRPCServer((self.targetip, int(self.targetport)))

    @staticmethod
    def add(a, b):
        return a+b

    @staticmethod
    def substract(a, b):
        return a-b

    @staticmethod
    def multiplication(a, b):
        return a*b

    @staticmethod
    def division(a, b):
        return a/b

    def run(self):
        server = self.createconnection()
        server.register_function(self.add, 'tambah')
        server.register_function(self.substract, 'kurang')
        server.register_function(self.multiplication, 'kali')
        server.register_function(self.division(), 'bagi')
        server.serve_forever()


node_one = RPCnodeOne()
node_one.run()