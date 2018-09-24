from ClientThread import ClientThread
from Authentification import *
from queue import Queue
import socket, select
import share as share
import graphic

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = ''
TCP_PORT = 2004

share.players = []
share.isAdminConnected=False
share.isGameReady=False
share.l_map = [["##" for x in range(10)] for y in range(10)]  # Cette liste contiendra la map en 2D

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
tcpServer.listen(5)

share.initTable()
rlist = [tcpServer]
work_queue = Queue()

def isPositionValid(conn, player):
    data = conn.recv(30)  # receive message from client
    message = data.decode()
    print(message)  # decode
    try:
        positionx, positiony = message.split(",")
    except ValueError:
        print("Failure / Wrong format ? (x,y)")

    print("position x : " + positionx)
    print("position y : " + positiony)
    return (hitAnswer(int(positionx), int(positiony), player))

def checkCoule(x, y, ship):
    if(x+1<=9 and share.l_map[y][x+1] == ship):
        return False
    if (x - 1 >= 0 and share.l_map[y][x - 1] == ship):
        return False
    if (y + 1 <= 9 and share.l_map[y + 1][x] == ship):
        return False
    if (y - 1 >= 0 and share.l_map[y - 1][x] == ship):
        return False
    return True

def hitAnswer(x , y, player):
    if share.l_map[y][x]== "**":
        print("Already hit")
        return (str(x)+","+str(y)+","+"Already hit")
    elif share.l_map[y][x] == "##":
        share.l_map[y][x] = "**"
        print("Failed")
        return (str(x)+","+str(y)+","+"F")
    else:
        if(checkCoule(x, y, share.l_map[y][x])):
            print("Coule")
            player.nbPoints+=1
            Personne.endOfTheGame+=1
            share.l_map[y][x] = "**"
            return (str(x)+","+str(y)+","+"C")
        else:
            print("Touche")
            player.nbPoints += 1
            Personne.endOfTheGame += 1
            share.l_map[y][x] = "**"
            return (str(x)+","+str(y)+","+"T")

def accept_client():
    (conn, (ip, port)) = tcpServer.accept()
    ClientThread(ip, port, conn, work_queue).start()

accept_client()

while not work_queue.empty():
    server_ready, _, _ = select.select(rlist,[],[], .25)
    if tcpServer in server_ready:
        print("Multithreaded Python server : Waiting for connections from TCP clients...")
        accept_client()

### Game part###
if(share.players):
    while Personne.endOfTheGame != 17:
        graphic.showTableServer(share.l_map)
        for conn, player in share.players:
            conn.send("Your,Turn,Play".encode())
            conn.recv(10)
            tmpResult = isPositionValid(conn, player) #check position
            tmpX, tmpY, answer = tmpResult.split(",")
            conn.send(tmpResult.encode()) #send it to the client
            while(answer == "Already hit"): #while position has already been hit, retry
                tmpResult = isPositionValid(conn, player)
                tmpX, tmpY, answer = tmpResult.split(",")
                conn.send(tmpResult.encode())
            print("Points du joueur " + player.username + " : " + str(player.nbPoints))
            conn.recv(10)
            conn.send(str(player.nbPoints).encode())
            conn.recv(10)
            conn.send(str(Personne.endOfTheGame).encode())
            for conn2, player2 in share.players:
                if(conn != conn2): #send updates to everyone except the current player
                    if (int(Personne.endOfTheGame == 17)):
                        tmpX = "End"
                        tmpY = "Of"
                        answer= "Game"
                        conn2.send((tmpX + "," + tmpY + "," + answer).encode())
                        conn2.recv(10)
                    else:
                        conn2.send((tmpX + "," + tmpY + "," + answer).encode())
                        conn2.recv(10)
            if(int(Personne.endOfTheGame==17)):
                break
else:
    print("There are not any players !")

tcpServer.close()
