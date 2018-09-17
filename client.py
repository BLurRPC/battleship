import socket
from ClientThreadClient import ClientThreadClient
from GameThreadClient import GameThreadClient

host = '127.0.0.1' #server's IP
port = 2004 #server's port

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))
#tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#tcpClientB.connect((host, port))
###Waiting for admin part###

newThread = ClientThreadClient(tcpClientA)
newThread.start()

#newThread = GameThreadClient(tcpClientB)
#newThread.start()