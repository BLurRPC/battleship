from threading import Thread
from Authentification import *
from socketserver import ThreadingMixIn
import share as share
from graphic import *

from termios import tcflush, TCIOFLUSH


import keyboard,sys,time
global coordinates

l_map = []  # Cette liste contiendra la map en 2D
for i in range(10):
    l_map.append([0] * 10)  # Ajoute 10 colonnes de 10 entiers(int) ayant pour valeurs 0
print (l_map)
user=""

x=0
y=0
ori =""
s=""

def choose_ships():
	Ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2} #size of each ship
	ship = [['Carrier', 1,x,y], ['Battleship', 1,x,y], ['Cruiser', 1,x,y], ['Submarine', 1,x,y], ['Destroyer', 1,x,y]] #number of ships to place

	print ("Choose your ships:")
	print (" 1:Carrier "+" 2:Battleship " + " 3:Cruiser " + " 4:Submarine "+ " 5:Destroyer ")
	while True:#making a loop
        		 
        		if (keyboard.is_pressed('1')):#if key '1' is pressed
        			print("\n")
        			tcflush(sys.stdin, TCIOFLUSH)
        			time.sleep(2)
        			ori=coor(x,y) #get coordinates of the ship
        			print(Ships)
        			orientation_ship(l_map,ship,s,ori,x,y)
        			return False
        			


	### Check if the Ships are available  ###
#def check_available_ships()
		#for i in Admin_Ships: #place ships
	#    r = 0
	    #while i[1] > 0: #check there's ships available
	       #type = i[0]
	       # ship_size = Ships[i[0]]
	         # None is often a good pick
	       # x, y = coordinates.split(",")
	       # coordinates = input(user + " : Enter coordinates (x,y)\n")
	       # print (coordinates)
	       # if check is True: # function check, confirm if the emplacement is available 
	       #     i[1] -= 1
	       # else:
	       #     print("Can't place ship here.")



def orientation_ship(l_map,ship,s,ori,x,y): #choose orientation for your ship
	#s is the letter for the ship location
	#place ship based on orientation
	if ori == "N":
		for i in range(ship): # NORD
			l_map[x+i][y] = s 
	elif ori == "W":
		for i in range(ship): # OUEST
			l_map[x][y-i] = s
	elif ori == "S":          # SUD
		for i in range(ship):
			l_map[x-i][y] = s
	elif ori == "E":
		for i in range(ship): # EST
			l_map[x][y+i] = s

	return l_map

def coor(x,y):
	
	print("please enter your coordinates with the format (x,y)")
	x=0
	coordinates = input("enter your coordinates here!: ")
	x,y = coordinates.split(",")
	print ("Enter your orientation, like S,N,W,E:")
	orientation_of_ship = input("Orieintation: ")
	orientation_boolean = True
	while orientation_boolean is True:
		if((orientation_of_ship is  "E") or (orientation_of_ship is  "W") or (orientation_of_ship is  "S") or (orientation_of_ship is  "N")):
			orientation_boolean = False
			

		else:
			print ("Tu t'es foutu de ma gueule ou tu sais pas lire")
			orientation_of_ship = input("Orieintation: ")

	print(coordinates)
	coor_boolean=False
	while(coor_boolean is False):

		if (0 <= int(x) <= 9 and 0 <= int(y) <= 9):
			print("coordinates are correct to the map")
			coor_boolean = True
			return orientation_of_ship
		else:
			print ("error")
			return True
			ori=0
			

choose_ships()