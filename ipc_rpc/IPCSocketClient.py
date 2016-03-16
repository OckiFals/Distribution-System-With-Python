#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama 135150207111060
"""

import sys
import json
import socket


class IPCSocketClient:
    def __init__(self):
        self.targetip = '127.0.0.1' if len(sys.argv) is not 2 else sys.argv[1]
        self.targetport = '8080' if len(sys.argv) is not 3 else sys.argv[2]

    def createconnection(self):
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.connect((self.targetip, int(self.targetport)))
        return tcpsock

    @staticmethod
    def parsingtojson(operasi, a, b):
        return json.dumps({
            'operasi': operasi,
            'a': a,
            'b': b
        })

    def readinput(self):
        print 'Operasi Aritmatika\n1. tambah \n2. kurang\n3. kali\n4. bagi\n0. keluar'
        try:
            operasi = int(raw_input('Pilih operasi:'))

            if operasi not in range(0, 4):
                print 'operasi tidak tersedia\n'
                return self.readinput()

            if operasi is 0:
                exit()

            a = int(raw_input('Masukkan variabel a:'))
            b = int(raw_input('Masukkan variabel b:'))
            return self.parsingtojson(operasi, a, b)
        except Exception:
            print 'Masukan tidak cocok\n\n'
            return self.readinput()

    def sendoversocket(self):
        json_data = self.readinput()
        sock = self.createconnection()
        sock.send(json_data)
        sock.close()

    def run(self):
        while 1:
            self.sendoversocket()


client = SocketClient()
client.run()