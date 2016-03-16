#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama 135150207111060
"""
from SimpleXMLRPCServer import SimpleXMLRPCServer


class RPCnodeServer:
    def __init__(self, ip, port):
        self.targetip = ip
        self.targetport = port

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
        server.register_function(self.division, 'bagi')
        server.serve_forever()