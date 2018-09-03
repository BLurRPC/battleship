import socket
from cryptology import *
from Payment import *

host = '127.0.0.1' #server's IP
port = 2004 #server's port

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

MESSAGE = "undo"
tcpClientA.send(MESSAGE.encode()) #send "undo" to server

data = tcpClientA.recv(KEY_WORD_SIZE)

tcpClientA.close() 
