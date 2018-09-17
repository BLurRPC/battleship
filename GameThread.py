from threading import Thread
from Authentification import *
from socketserver import ThreadingMixIn
import share as share

# Multithreaded Python server : TCP Server Socket Thread Pool
class GameThread(Thread):

    def __init__(self,ip,port,conn):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = conn
        #self.person = person
        print("[+]Still on " + ip + ":" + str(port))

    def run(self):

        print("A faire")