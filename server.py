from ClientThread import ClientThread
import socket
import share as share

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = ''
TCP_PORT = 2004

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

share.initTable()

while True:
    tcpServer.listen(5)
    print ("Multithreaded Python server : Waiting for connections from TCP clients...")
    (conn, (ip,port)) = tcpServer.accept()
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
