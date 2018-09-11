#!/usr/bin/python
# -*- coding: latin-1 -*-
import share

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
        self.isAdmin = False

def waitingForAdmin(conn):
    """ Asking for id/password, and if admin then send adminConnected to all
        Return an object personne"""

    user = conn.recv(30)
    password = conn.recv(30)
    currentStatus = "waitingForAdmin"
    person = Personne(user.decode(), password.decode())
    if((user.decode()==person.Admin_username and password.decode()==person.Admin_password) or share.isAdminConnected):
        share.isAdminConnected=True
        currentStatus = "adminConnected"
    conn.send(currentStatus.encode())
    return person