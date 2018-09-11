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

        #print(self.person.username + " : " + str(person.isAdmin))
        data = self.conn.recv(30) #receive message from client
        message = data.decode()
        print(message) #decode
        try:
            positionx, positiony = message.split(",")
            print("Success")
        except ValueError:
            print("Failure / Wrong format ? (x,y)")

        print("position x : " + positionx)
        print("position y : " + positiony)
        if(share.l_map[int(positionx)][int(positiony)] == 0):
            message = "Good job"
            share.l_map[int(positionx)][int(positiony)] = 1
        else:
            message = "Already hit"
        self.conn.send(message.encode())  # send message to the client