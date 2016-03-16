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
        self.port = '8082' if len(sys.argv) is not 3 else sys.argv[2]
        self.statecounter = 0
        self.operand = ''

    def createipcconnection(self):
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.bind(('', int(self.port)))
        return tcpsock

    @staticmethod
    def createrpcconncetion(port):
        return xmlrpclib.ServerProxy(
            "http://127.0.0.1:%s/" % port
        )

    def roundrobin(self):
        # rpc nodes port numbers
        rpc_node_ports = [8084, 8086, 8088]

        rpc_conn = self.createrpcconncetion(
            rpc_node_ports[self.statecounter]
        )

        if self.statecounter is 2:
            # back to 1
            self.statecounter = 0
        else:
            # counter increment by 1
            self.statecounter += 1

        return rpc_conn

    def rpccall(self, json_):
        proxy = self.roundrobin()
        operate_in_int = int(json_['operasi'])

        if 1 is operate_in_int:
            self.operand = 'tambah'
            return proxy.tambah(int(json_['a']), int(json_['b']))
        elif 2 is operate_in_int:
            self.operand = 'kurang'
            return proxy.kurang(int(json_['a']), int(json_['b']))
        elif 3 is operate_in_int:
            self.operand = 'kali'
            return proxy.kali(int(json_['a']), int(json_['b']))
        elif 4 is operate_in_int:
            self.operand = 'bagi'
            return proxy.bagi(int(json_['a']), int(json_['b']))

    def receiveoversocket(self):
        sock = self.createipcconnection()
        sock.listen(1)
        try:
            while 1:
                conn, addr = sock.accept()
                data = conn.recv(1024)
                json_ = json.loads(data)
                print json_
                result = str(self.rpccall(json_))
                conn.send(
                    "Hasil pemanggilan %s(%s, %s) = %s \nDilayani oleh RPC server %s" % (
                        self.operand,
                        json_['a'],
                        json_['b'],
                        result,
                        3 if (self.statecounter is 0) else self.statecounter
                    )
                )
        except KeyboardInterrupt:
            sock.close()

    def run(self):
        self.receiveoversocket()


server = IPCSocketServer()
server.run()
