import socket
from graphic import *

host = '127.0.0.1' #server's IP
port = 2004 #server's port

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

l_map = [] #Cette liste contiendra ma map en 2D
for i in range(10):
    l_map.append([0] * 10) #Ajoute 10 colonnes de 10 entiers(int) ayant pour valeurs 0

showTable(l_map)

while True :
    message = input("tcpClientA: Enter message\n")
    while True :
        try:
            positionx, positiony = message.split(",")
            print("success")
            break
        except ValueError:
            print("Failure / Wrong format ? (x,y)")
            message = input("tcpClientA: Enter message\n")

    tcpClientA.send(message.encode())
    data=tcpClientA.recv(1000)
    print("Received :" + data.decode())
