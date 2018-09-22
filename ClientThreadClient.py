from threading import Thread
import getpass
from graphic import *
import graphic
import SetMap

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThreadClient(Thread):

    def __init__(self, conn):
        Thread.__init__(self)
        self.conn = conn

    def isPositionValid(self, user):
        coordinates = input(user + " : Enter coordinates (x,y)\n")
        while True:
            try:
                positionx, positiony = coordinates.split(",")
                if (0 <= int(positionx) <= 9 and 0 <= int(positiony) <= 9):
                    break
                else:
                    print("Failure : Not in range [0-9]")
                    coordinates = input(user + " : Enter coordinates (x,y)\n")
            except ValueError:
                print("Failure : Wrong format (x,y)")
                coordinates = input(user + " : Enter coordinates (x,y)\n")

        self.conn.send(coordinates.encode())
        data = self.conn.recv(30)
        print("Received from server : " + data.decode())
        if (data.decode() != "Already hit"):
            return True
        else:
            print("Please try another position")
            return False

    def run(self):
        user=""
        SetMap.l_map = [["##" for x in range(10)] for y in range(10)]  # Cette liste contiendra la map en 2D

        while (self.conn.recv(30).decode() == "waitingForAdmin"):
            user = input("Please enter your username :")
            self.conn.send(user.encode())
            self.conn.recv(10)
            password = getpass.getpass("Please enter a password " + user + " :\n")
            self.conn.send(password.encode())
            self.conn.send("ok".encode())
        print("Waiting for others to connect...\n")
        ###Admin part before begining###

        amIAdmin = self.conn.recv(30)
        isAdmin = False
        if(amIAdmin.decode() == "youAreAdmin"):
            isAdmin = True
            ###Admin set the game here cote client
            print("You are Admin.\nYou can configure the game here")

            graphic.showTable(SetMap.l_map)
            carrier = ["ca", "ca", "ca", "ca", "ca"]
            battleship = ["ba", "ba", "ba", "ba"]
            cruiser = ["cr", "cr", "cr"]
            submarine = ["su", "su", "su"]
            destroyer = ["de", "de"]
            ships = [(carrier, 1), (battleship, 2), (cruiser, 3), (submarine, 4), (destroyer, 5)]
            shipsPlaced = []
            count = 0
            while count != 5:
                myShipNum = SetMap.choose_ship()
                for ship, shipNum in ships:
                    if (int(shipNum) == int(myShipNum)):
                        if SetMap.check_available_ships(ship, shipsPlaced):
                            SetMap.place_ship()
                            x, y = SetMap.coordinates.split(",")
                            x = int(x)
                            y = int(y)
                            if (SetMap.checkShipTable(ship, x, y)):
                                SetMap.updateShipTable(ship, x, y)
                                shipsPlaced.append(ship)
                                message = str(shipNum) + "," + str(x) + "," + str(y) + "," + SetMap.orientation_of_ship
                                self.conn.send(message.encode())
                                count+=1
                            else:
                                print("There is a collision here. Please try another position")
                        else:
                            print("Ship already placed")
                graphic.showTable(SetMap.l_map)

        else:
            print("You are not Admin. Please wait for him ...")

        ###Gaming part###
        gameOver = 0
        while gameOver<=17: #While not at least 17 hits
            if(not isAdmin): #Only players can play
                print("Waiting for others to play ...\n")
                temp = self.conn.recv(30).decode()  #Number of points
                nbPoints = int(temp)
                self.conn.send("ok".encode())
                graphic.showTable(SetMap.l_map)
                print(user + " : " + str(nbPoints) + " points !")
                while(not self.isPositionValid(user)):
                    print("")
                self.conn.send("ok".encode())
                gameOver = int(self.conn.recv(30).decode())
                print(str(gameOver))
