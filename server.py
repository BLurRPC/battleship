from ClientThread import ClientThread
from Authentification import *
from queue import Queue
import socket, select
import share as share

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

def accept_client():
    (conn, (ip, port)) = tcpServer.accept()
    conns.append(conn)
    ClientThread(ip, port, conn, work_queue).start()

accept_client()

while not work_queue.empty():
    server_ready, _, _ = select.select(rlist,[],[], .25)
    if tcpServer in server_ready:
        print("Multithreaded Python server : Waiting for connections from TCP clients...")
        accept_client()

for conn in conns:
    message = "youAreNotAdmin"
    for conn2,player in share.players:
        print(str(conn)+"\n"+str(conn2)+"\n"+str(player))
        if(conn==conn2 and player.isAdmin):
            message="youAreAdmin"
    conn.send(message.encode())

while True:
    for conn in conns:
        conn.send("It's your turn".encode())
        data = conn.recv(30)  # receive message from client
        message = data.decode()
        print(message)  # decode
        try:
            positionx, positiony = message.split(",")
            print("Success")
        except ValueError:
            print("Failure / Wrong format ? (x,y)")

        print("position x : " + positionx)
        print("position y : " + positiony)
        if (share.l_map[int(positionx)][int(positiony)] == 0):
            message = "Good job"
            share.l_map[int(positionx)][int(positiony)] = 1
        else:
            message = "Already hit"
        conn.send(message.encode())  # send message to the client