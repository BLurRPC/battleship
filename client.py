import socket

host = '127.0.0.1' #server's IP
port = 2004 #server's port

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

MESSAGE = input("tcpClientA: Enter message")
while True :
    print("ok")
    tcpClientA.send(MESSAGE.encode())
    data=tcpClientA.recv(1000)
    print("Received :" + data.decode())
    MESSAGE = input("tcpClientA: Enter message")

