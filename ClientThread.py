import socket, os
from threading import Thread
from socketserver import ThreadingMixIn

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
            message = data.decode() #decode
            position = message.split(",")
            
            print("position x :" + position[0])
            print("position y :" + position[1])
            self.conn.send(message.encode())  # send message to the client


