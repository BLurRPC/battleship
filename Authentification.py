#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import share
from getpass import getpass

class Personne(object):

    """Classe définissant une personne caractérisée par :

    - son  username

    - son  mdp"""

    Admin_username = "Admin"
    Admin_password = "Admin"
    isAdmin = False

    def __init__(self, username, password):
        super(Personne, self).__init__()
        self.username = username
        self.password = password

def waitingForAdmin(conn):
    """ Asking for id/password, and if admin then send adminConnected to all
        Return an object personne"""

    identifiant = conn.recv(30)
    motDePasse = conn.recv(30)
    currentStatus = "waitingForAdmin"
    personne = Personne(identifiant, motDePasse)
    if(identifiant.decode()==personne.Admin_username and motDePasse.decode()==personne.Admin_password and not share.isAdminConnected):
        personne.isAdmin = True
    if((identifiant.decode()==personne.Admin_username and motDePasse.decode()==personne.Admin_password) or share.isAdminConnected):
        share.isAdminConnected=True
        currentStatus = "adminConnected"
    conn.send(currentStatus.encode())
    return personne