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
        tmpX, tmpY, signal = data.decode().split(",")
        if (signal != "Already hit"):
            print(signal + " en : " + tmpX + "," + tmpY)
            SetMap.l_map[int(tmpY)][int(tmpX)] = signal
            return True
        else:
            print("Please try another position")
            return False

    def run(self):
        SetMap.l_map = [["#" for x in range(10)] for y in range(10)]  # Cette liste contiendra la map en 2D

        while (self.conn.recv(30).decode() == "waitingForAdmin"):
            user = ""
            password = ""
            while user == "":
                user = input("Please enter your username :")
            self.conn.send(user.encode())
            self.conn.recv(10)
            while password == "":
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

            graphic.showTableClient(SetMap.l_map)
            carrier = ["1", "1", "1", "1", "1"]
            battleship = ["2", "2", "2", "2"]
            cruiser = ["3", "3", "3"]
            submarine = ["4", "4", "4"]
            destroyer = ["5", "5"]
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
                graphic.showTableClient(SetMap.l_map)

        else:
            print("You are not Admin. Please wait for him ...")

        ###Gaming part###
        gameOver = 0
        done = False
        while done==False: #While not at least 17 hits
            if(not isAdmin): #Only players can play
                print("Waiting for others to play ...\n")
                update = self.conn.recv(30)
                tmpX, tmpY, signal = update.decode().split(",")
                self.conn.send("ok".encode())
                if((tmpX=="End" and tmpY=="Of" and signal=="Game")):
                    print("Game is Over")
                    done = True
                else:
                    while((tmpX!="Your" and tmpY!="Turn" and signal!="Play")):
                        if ((tmpX == "End" and tmpY == "Of" and signal == "Game")):
                            print("Game is Over")
                            done = True
                            break
                        else:
                            SetMap.l_map[int(tmpY)][int(tmpX)] = signal
                            graphic.showTableClient(SetMap.l_map)
                            print("Waiting for others to play ...\n")
                            update = self.conn.recv(30)
                            tmpX, tmpY, signal = update.decode().split(",")
                            self.conn.send("ok".encode())
                    if(done==False):
                        graphic.showTableClient(SetMap.l_map)
                        while(not self.isPositionValid(user)):
                            print("")
                        self.conn.send("ok".encode())
                        temp = self.conn.recv(30).decode()  # Number of points
                        nbPoints = int(temp)
                        self.conn.send("ok".encode())
                        gameOver = int(self.conn.recv(30).decode())
                        graphic.showTableClient(SetMap.l_map)
                        print(user + " : " + str(nbPoints) + " points !")
                        print("Total shots : " + str(gameOver))
            else: #if Admin
                update = self.conn.recv(30)
                tmpX, tmpY, signal = update.decode().split(",")
                self.conn.send("ok".encode())
                if ((tmpX == "End" and tmpY == "Of" and signal == "Game")):
                    print("Game is Over")
                    done = True
                    break
                else:
                    SetMap.l_map[int(tmpY)][int(tmpX)] = signal
                    graphic.showTableClient(SetMap.l_map)
                    print("Waiting for others to play ...\n")

        self.conn.close()