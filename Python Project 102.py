#!/usr/bin/python
from thread import start_new_thread
from sys import *
def ShowClients():
    print 'All Clients'
    EnterToMenu()
def SendACommand():
    print 'sending command'
    EnterToMenu()
def SendAFile():
    print 'sending file'
    EnterToMenu()
def install():
    print 'install'
    EnterToMenu()
def remove():
    print 'remove'
    EnterToMenu()
def OpenAShell():
    print 'Shell is Open'
    EnterToMenu()
def NotFound():
    print 'Option not found, try again'
    menu(men=1)
def EnterToMenu():
    try:
        input('Hot a key to go back to Menu')
    except:
        menu(men=1)

def menu(men):
    print """
    ########################################################
    
        Python 102                   Name: Dudu
        
    ########################################################

    1. Show all clients
    2. Send commands to all client
    3. Transfer file to all clients
    4. Install something on all clients
    5. Remove something from all clients
    6. Open Linux Shell """

    ChooseAnOption = raw_input("Choose An Option: ")
    Options = {"1": ShowClients, "2":SendACommand, "3":SendAFile, "4":install, "5":remove, "6":OpenAShell}
    Options.get(ChooseAnOption, NotFound)()

start_new_thread(menu, (77,))
