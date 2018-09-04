import socket, os
from threading import Thread
from socketserver import ThreadingMixIn


# Multithreaded Python server : TCP Server Socket Thread Pool for client updates
class ClientThreadUpdate(Thread):

    def __init__(self, ip, port, conn):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = conn
        print("[+] New server socket thread (update) started for " + ip + ":" + str(port))

    def run(self):

        while True:

            try:
                nature, positionx, positiony = update.split(",")
                print("success")
            except ValueError:
                print("Failure / Wrong format ? (x,y)")

            print("position x : " + positionx)
            print("position y : " + positiony)
            self.conn.send(message.encode())  # send message to the client


