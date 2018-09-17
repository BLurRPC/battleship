global l_map
global orientation_of_ship
global coordinates

def choose_ship():
    print (" 1:Carrier "+" 2:Battleship " + " 3:Cruiser " + " 4:Submarine "+ " 5:Destroyer ")
    while True:
        myShip = input("Choose your ship :\n")
        if(myShip == "1"):
            return 1
            break
        elif (myShip == "2"):
            return 2
            break
        elif (myShip == "3"):
            return 3
            break
        elif (myShip == "4"):
            return 4
            break
        elif (myShip == "5"):
            return 5
            break

    ### Check if the Ships are available  ###
def check_available_ships(myShip, shipsPlaced):
    for tmpShip in shipsPlaced:
        if myShip == tmpShip:
            return False
    return True

def checkShipTable(myShip, x,y):
    global l_map
    global orientation_of_ship
    for i, ship in enumerate(myShip):
        if (orientation_of_ship == "E" and (x+i > 9 or l_map[y][x+i] != "##")):
            return False
        elif (orientation_of_ship == "N" and (y+i > 9 or l_map[y+i][x] != "##")):
            return False
        elif (orientation_of_ship == "W" and (x-i < 0 or l_map[y][x-i] != "##")):          # SUD
            return False
        elif (orientation_of_ship == "S" and (y-i < 0 or l_map[y-i][x] != "##")):
            return False
    return True


def updateShipTable(myShip, x,y): #choose orientation for your ship
    #s is the letter for the ship location
    #place ship based on orientation
    global l_map
    global orientation_of_ship
    print("test " + myShip[0])
    print(orientation_of_ship)
    for i, ship in enumerate(myShip):
        if orientation_of_ship == "E":
            l_map[y][x+i] = myShip[i]
        elif orientation_of_ship == "N":
            l_map[y+i][x] = myShip[i]
        elif orientation_of_ship == "W":          # SUD
            l_map[y][x-i] = myShip[i]
        elif orientation_of_ship == "S":
            l_map[y-i][x] = myShip[i]

def place_ship():
    global coordinates
    global orientation_of_ship
    coordinates = input("Enter coordinates (x,y)\n")
    while True:
        try:
            x, y = coordinates.split(",")
            if (0 <= int(x) <= 9 and 0 <= int(y) <= 9):
                break
            else:
                print("Failure : Not in range [0-9]")
                coordinates = input("Enter coordinates (x,y)\n")
        except ValueError:
            print("Failure : Wrong format (x,y)")
            coordinates = input("Enter coordinates (x,y)\n")

    print ("Enter your orientation, like S,N,W,E:")
    orientation_of_ship = input("Orientation: ")
    orientation_boolean = True
    while orientation_boolean:
        if((orientation_of_ship == "E") or (orientation_of_ship == "W") or (orientation_of_ship == "S") or (orientation_of_ship == "N")):
            orientation_boolean = False
        else:
            print ("Tu t'es foutu de ma gueule ou tu sais pas lire")
            orientation_of_ship = input("Orientation: ")
    print(orientation_of_ship)
