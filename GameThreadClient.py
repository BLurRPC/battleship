from threading import Thread
from Authentification import *
from socketserver import ThreadingMixIn
import share as share

# Multithreaded Python server : TCP Server Socket Thread Pool
class GameThreadClient(Thread):

    def __init__(self, conn):
        Thread.__init__(self)
        self.conn = conn
        print("[+]Second thread started for : " + str(conn))

    def run(self):

        while True:
            data = self.conn.recv(30) #receive message from client
            message = data.decode()
            print(message) #decode