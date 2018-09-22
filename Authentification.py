#!/usr/bin/python
# -*- coding: latin-1 -*-
import share

class Personne(object):

    """Classe définissant une personne caractérisée par :

    - son  username

    - son  mdp"""

    Admin_username = "Admin"
    Admin_password = "Admin"
    endOfTheGame = 0 #Count each time someone hits, when it is equal to 17 the game is over

    def __init__(self, username, password):
        super(Personne, self).__init__()
        self.username = username
        self.password = password
        self.isAdmin = False
        self.nbPoints = 0

