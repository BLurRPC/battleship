#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
from getpass import getpass

class Personne(object):
	
	"""Classe définissant une personne caractérisée par :

    - son  username

    - son  mdp"""

	Admin_username = "Admin"
	Admin_password = "Admin"
	def __init__(self, username, password):
	    super(Personne, self).__init__()
	    self.username = username
	    self.password = password

verrouille = True
while verrouille:
	#entre_u = getpass("Tapez le username : ") # Admin
    entre_p = getpass("Tapez le mot de passe : ") # Admin
    # On doit entrer le mot de passe pour voir si c'est bien l'admin
    print("La première personne à se connecter, doit être l'admin")
    a=True #variable boolean pour la confirmation de la connection de l'admin
    while a:
	    if entre_p == Personne.Admin_password: #& entre_u == Personne.Admin_username:	
	    	verrouille = False
	    	print ("Bienvenue !" + "Mr l'" + Personne.Admin_username)
	    	a=False	
	    else:
	    	print ("Le mot de passe est incorrect")
	    	break