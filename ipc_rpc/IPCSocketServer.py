#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama 135150207111060
"""

import sys
import json
import socket
import xmlrpclib


class IPCSocketServer:
    def __init__(self):
        self.targetip = '0.0.0.0' if len(sys.argv) is not 2 else sys.argv[1]
        self.targetport = '8082' if len(sys.argv) is not 3 else sys.argv[2]

    def createipcconnection(self):
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.bind(('', int(self.targetport)))
        return tcpsock

    @staticmethod
    def createrpcconncetion(port):
        return xmlrpclib.ServerProxy(
            "http://127.0.0.1:8088/"
        )

    def roundrobin(self):
        pass

    def rpccall(self):
        proxy = self.createrpcconncetion(8080)
        return proxy.tambah(1, 2)

    def receiveoversocket(self):
        sock = self.createipcconnection()
        sock.listen(1)
        try:
            while 1:
                conn, addr = sock.accept()
                data = conn.recv(100)
                dictionary_mhs = json.loads(data)
                print dictionary_mhs
        except KeyboardInterrupt:
            sock.close()

    def run(self):
        self.rpccall()
        # self.receiveoversocket()


server = SocketServer()
server.run()
