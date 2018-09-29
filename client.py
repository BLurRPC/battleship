import socket
from ClientThreadClient import ClientThreadClient
import argparse

host = '127.0.0.1' #server's IP
port = 2004 #server's port

#Get IP and port
parser = argparse.ArgumentParser(description='IP and port.')
parser.add_argument('-n', default=host, help='The server\'s IP address')
parser.add_argument('-p', default= port, type=int, help='The server\'s port')
args = parser.parse_args()
#Save IP and port
host = args.n
port = args.p
#Connect to server
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))
#The game starts
newThread = ClientThreadClient(tcpClientA)
newThread.start()
