import socket
from graphic import *
import getpass

host = '127.0.0.1' #server's IP
port = 2004 #server's port

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

l_map = [] #Cette liste contiendra la map en 2D
for i in range(10):
    l_map.append([0] * 10) #Ajoute 10 colonnes de 10 entiers(int) ayant pour valeurs 0

###Waiting for admin part###

isAdminConnected = tcpClientA.recv(30)
while (isAdminConnected.decode() == "waitingForAdmin"):
    user = input("Please enter your username :")
    tcpClientA.send(user.encode())

    password = getpass.getpass("Please enter a password "+user+" :\n")
    tcpClientA.send(password.encode())
    isAdminConnected = tcpClientA.recv(30)

###Gaming part###

showTable(l_map)
while True :
    coordinates = input(user + " : Enter coordinates (x,y)\n")
    while True :
        try:
            positionx, positiony = coordinates.split(",")
            if(0 <= int(positionx) <= 9 and 0 <= int(positiony) <= 9):
                print("success")
                break
            else:
                print("Failure : Not in range [0-9]")
                coordinates = input(user + " : Enter coordinates (x,y)\n")
        except ValueError:
            print("Failure : Wrong format (x,y)")
            coordinates = input(user + " : Enter coordinates (x,y)\n")

    tcpClientA.send(coordinates.encode())
    data=tcpClientA.recv(1000)
    print("Received from server : " + data.decode())
