import socket, os
from threading import Thread
from socketserver import ThreadingMixIn
import share as share

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):

    def __init__(self,ip,port,conn):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = conn
        print("[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):

        while True :
            data = self.conn.recv(30) #receive message from client
            message = data.decode()
            print(message) #decode
            try:
                positionx, positiony = message.split(",")
                print("success")
            except ValueError:
                print("Failure / Wrong format ? (x,y)")
            
            print("position x : " + positionx)
            print("position y : " + positiony)
            if(share.l_map[int(positionx)][int(positiony)] == 0):
                message = "Bravo"
                share.l_map[int(positionx)][int(positiony)] = 1
            else:
                message = "Marche pas"
            self.conn.send(message.encode())  # send message to the client


