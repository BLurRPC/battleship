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
	
	//To do

        data = self.conn.recv(4) #receive message from server
        message = data.decode() #decode
        self.conn.send(message.encode())  # sent message to the server
                

