l_map = [] #Cette liste contiendra ma map en 2D

def initTable():
    for i in range(10):
        global l_map
        l_map.append([0] * 10) #Ajoute 10 colonnes de 10 entiers(int) ayant pour valeurs 0
