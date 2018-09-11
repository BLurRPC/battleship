from threading import Thread
import getpass
from graphic import *

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThreadClient(Thread):

    def __init__(self, conn):
        Thread.__init__(self)
        self.conn = conn
        print("[+]Thread started")

    def run(self):

        l_map = []  # Cette liste contiendra la map en 2D
        for i in range(10):
            l_map.append([0] * 10)  # Ajoute 10 colonnes de 10 entiers(int) ayant pour valeurs 0
        user=""

        while (self.conn.recv(30).decode() == "waitingForAdmin"):
            user = input("Please enter your username :")
            self.conn.send(user.encode())
            password = getpass.getpass("Please enter a password " + user + " :\n")
            self.conn.send(password.encode())

        ###Admin part before begining###

        amIAdmin = self.conn.recv(30)
        if(amIAdmin.decode() == "youAreAdmin"):
            ###Admin set the game here cote client
            print("You are Admin.\nYou can configure the game here")
        else:
            print("You are not Admin")

        ###Gaming part###

        showTable(l_map)
        while True:
            print("Waiting for others ...\n")
            self.conn.recv(30)
            print("It's your turn !")
            coordinates = input(user + " : Enter coordinates (x,y)\n")
            while True:
                try:
                    positionx, positiony = coordinates.split(",")
                    if (0 <= int(positionx) <= 9 and 0 <= int(positiony) <= 9):
                        print("success")
                        break
                    else:
                        print("Failure : Not in range [0-9]")
                        coordinates = input(user + " : Enter coordinates (x,y)\n")
                except ValueError:
                    print("Failure : Wrong format (x,y)")
                    coordinates = input(user + " : Enter coordinates (x,y)\n")

            self.conn.send(coordinates.encode())
            data = self.conn.recv(30)
            print("Received from server : " + data.decode())
