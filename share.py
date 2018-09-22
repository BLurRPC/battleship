global l_map
global players
global isAdminConnected
global isGameReady

def initTable():
    for i in range(10):
        l_map.append([0] * 10) #Ajoute 10 colonnes de 10 entiers(int) ayant pour valeurs 0