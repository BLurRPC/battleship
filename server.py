from ClientThread import ClientThread
from GameThread import GameThread
from Authentification import *
from queue import Queue
import socket, select
import share as share
import graphic

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = ''
TCP_PORT = 2004

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
tcpServer.listen(5)

share.initTable()
rlist = [tcpServer]
work_queue = Queue()
conns = []
conns2 = []
share.l_map = [["##" for x in range(10)] for y in range(10)]  # Cette liste contiendra la map en 2D

def isPositionValid(conn):
    data = conn.recv(30)  # receive message from client
    message = data.decode()
    print(message)  # decode
    try:
        positionx, positiony = message.split(",")
    except ValueError:
        print("Failure / Wrong format ? (x,y)")

    print("position x : " + positionx)
    print("position y : " + positiony)
    return (hitAnswer(int(positionx), int(positiony), conn))

def hitAnswer(x , y, conn):
    if share.l_map[y][x]== "C" or share.l_map[y][x]== "C" == "T":
        print("Already hit")
        conn.send("Already hit".encode())
        return False
    elif share.l_map[y][x] == "##":
        print("Coule")
        conn.send("C".encode())
    else:
        print("Touche")
        conn.send("T".encode())
    return True

def accept_client():
    (conn, (ip, port)) = tcpServer.accept()

    if(conn in conns):
        conns2.append(conn)
        #GameThread(ip, port, conn).start()
    else:
        conns.append(conn)
        ClientThread(ip, port, conn, work_queue).start()

accept_client()

while not work_queue.empty():
    server_ready, _, _ = select.select(rlist,[],[], .25)
    if tcpServer in server_ready:
        print("Multithreaded Python server : Waiting for connections from TCP clients...")
        accept_client()

### Game part###
while True:
    graphic.showTable(share.l_map)
    for conn in conns:
        conn.send("It's your turn".encode())
        while(not isPositionValid(conn)):
            print("Wrong position")
