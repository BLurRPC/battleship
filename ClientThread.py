import socket, os
from threading import Thread
from Authentification import *
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

        ###Waiting for admin part###

        personne = Personne("","") #By default
        if(share.isAdminConnected):
            currentStatus = "adminConnected"
        else:
            currentStatus = "waitingForAdmin"
        self.conn.send(currentStatus.encode())
        while(not share.isAdminConnected): #While admin not connected
            personne = waitingForAdmin(self.conn) #Ask for user/password

        ###Gaming part###

        while True :
            print("personne : "+ str(personne.isAdmin))
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