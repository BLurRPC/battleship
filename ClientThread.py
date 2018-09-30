from threading import Thread
from Authentification import *
import SetMapServer
import share as share

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):

    def __init__(self,ip,port,conn, queue=None):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = conn
        self.queue = queue
        print("[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):
        count=0
        if self.queue:
            self.queue.put(1)

        currentStatus = "waitingForAdmin"
        self.conn.send(currentStatus.encode())
        while (not share.isAdminConnected or count==0):  # While admin not connected
            user = self.conn.recv(30)
            print(user.decode())
            self.conn.send("ok".encode())
            password = self.conn.recv(30)
            print(password.decode())
            person = Personne(user.decode(), password.decode())
            count+=1
            if ((user.decode() == person.Admin_username and password.decode() == person.Admin_password)):
                share.isAdminConnected = True
                person.isAdmin = True

            if(share.isAdminConnected):
                currentStatus = "adminConnected"
            self.conn.send(currentStatus.encode())

        if(not person.isAdmin): #If not admin, add to list of players
            share.players.append([self.conn, person])
        adminInfo = "youAreNotAdmin"
        
        if (person.isAdmin):
            adminInfo = "youAreAdmin"
        self.conn.recv(10)
        self.conn.send(adminInfo.encode())
        while not share.isGameReady:
            if (person.isAdmin):
                for i in range(5):
                    data = self.conn.recv(30)
                    message = data.decode()
                    shipNum, x, y, orientation = message.split(",")
                    print(shipNum + " : " + " " + orientation + " " + x + " " + y)
                    shipName, size = SetMapServer.convertShip(int(shipNum))
                    SetMapServer.updateShipTable(shipName,size,orientation,int(x), int(y))
                share.isGameReady = True
        if self.queue:
            self.queue.get_nowait()
