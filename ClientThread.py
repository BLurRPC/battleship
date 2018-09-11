from threading import Thread
from Authentification import *
from GameThread import GameThread
from socketserver import ThreadingMixIn
import share as share

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):

    def __init__(self,ip,port,conn, queue=None):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = conn
        self.queue = queue
        print("[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):

        if self.queue:
            self.queue.put(1)

        currentStatus = "waitingForAdmin"
        self.conn.send(currentStatus.encode())
        while (not share.isAdminConnected):  # While admin not connected
            user = self.conn.recv(30)
            password = self.conn.recv(30)
            person = Personne(user.decode(), password.decode())
            if ((user.decode() == person.Admin_username and password.decode() == person.Admin_password)):
                # ADMIN configure la game ici cote serveur
                share.isAdminConnected = True
                person.isAdmin = True
                currentStatus = "adminConnected"
            if(share.isAdminConnected):
                share.isAdminConnected = True
                currentStatus = "adminConnected"
                share.players.append([self.conn, person])
            self.conn.send(currentStatus.encode())
        if self.queue:
            self.queue.get_nowait()