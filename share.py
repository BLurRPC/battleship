global l_map
l_map = []
global players
players = []
global isAdminConnected
global isGameReady
isAdminConnected=False
isGameReady=False

def initTable():
    for i in range(10):
        l_map.append([0] * 10) #Ajoute 10 colonnes de 10 entiers(int) ayant pour valeurs 0