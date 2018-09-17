import share

def updateShipTable(myShipName, size, orientation, x,y): #choose orientation for your ship
    #s is the letter for the ship location
    #place ship based on orientation

    print("test " + myShipName)
    print(orientation)
    for i in range(size):
        if orientation == "E":
            share.l_map[y][x+i] = myShipName
        elif orientation == "N":
            share.l_map[y+i][x] = myShipName
        elif orientation == "W":          # SUD
            share.l_map[y][x-i] = myShipName
        elif orientation == "S":
            share.l_map[y-i][x] = myShipName

def convertShip(shipNum):
    if(shipNum == 1):
        return ["ca", 5]
    elif(shipNum == 2):
        return ["ba", 4]
    elif(shipNum == 3):
        return ["cr", 3]
    elif(shipNum == 4):
        return ["su", 3]
    elif(shipNum == 5):
        return ["de", 2]