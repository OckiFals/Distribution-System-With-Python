import Pyro4


class Aritmatika():
    def __init__(self):
        pass

    @staticmethod
    def tambah(a, b):
        return a + b

    @staticmethod
    def kurang(a, b):
        return a - b


t = Aritmatika()
r = Aritmatika()

daemon = Pyro4.Daemon(host='', port=8888)

Pyro4.Daemon.serveSimple(
    {
        # register object
        t: 'penghitung',
        r: 'penghitung_2'
    },
    # name server
    ns=False,
    # server daemon
    daemon=daemon
)
