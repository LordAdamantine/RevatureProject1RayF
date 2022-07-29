import re
import logging
from pymongo import MongoClient
import os
import login

'''
To Do:
Introduction
    preload certain functions and data
Login options
    User vs Admin vs account creation
Store functionality
    Purchase, order history, admin management
Multiple data tables
Manipulating said tables
Event Logging


Merchandise database:
PHB weapons, armor, gear, limited magic items.
Different collections for each to help differentiate.
'''

def main():

    # Pre initialize vital files
    logging.basicConfig(filename = "store.log", level = logging.DEBUG, format = '%(asctime)s :: %(message)s')
    clear = lambda: os.system('cls')    #use clear() within code to clear console between certain screens.
    client = MongoClient()
    db = client.get_database("Project1")

    armor = db.armor
    weapons = db.weapons
    gear = db.gear
    misc = db.misc
    users = db.users
    logging.info("Loading database records...")

    # Welcome ascii art, I worked very hard on it
    with open('welcome.txt') as f:
        intro = f.read()
    print(str(intro))
    
    while True: #Keep majority of code, probably including login, inside while True loop.
        # Welcome screen and login.
        input("\t\t\t\tWelcome to the Sharpest Tool in the Shed!\n\t\t\t\tPlease log in or create an account!")
        
        '''test_print(armor, weapons, gear, misc)'''

        # Probably separate module/s with login functionality/account creation/quit option.

        #login()
        # account() module to login/create account.
        #clear()

        while True:
            # Modules depending on account class.
                #User: purchase, history, reserve, etc.
                #Admin: view all orders, view customer lists, modify accounts and inventory.
            # Close out all files and remember to commit all db changes on log out...
            #clear()
            break

        # Loop back around to login until quit
        break

    # Include some kind of parting farewell thanking the customer upon breaking out and quitting.
    with open("thanks.txt") as f:
        outro = f.read()
    print(str(outro))
    return 0


def test_print(armor, weapons, gear, misc):
    armor_test = armor.find({}, {'name':1, '_id':0})
    weapons_test = weapons.find({}, {'name':1, '_id':0})
    gear_test = gear.find({}, {'name':1, '_id':0})
    misc_test = misc.find({}, {'name':1, '_id':0})

    print("\n" + "Armor Sets")
    for elem in armor_test:
        print(elem)
    print("\n" + "Weapons")
    for elem in weapons_test:
        print(elem)
    print("\n" + "Miscellaneous Gear")
    for elem in gear_test:
        print(elem)
    print("\n" + "Magical Baubles")
    for elem in misc_test:
        print(elem)
    print("\n")


if __name__ == "__main__":
    main()