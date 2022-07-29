import re
import logging
import mysql.connector
import mysql_config as c
import os

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
    clear = lambda: os.system('cls')    #use clear() within code to clear console between certain screens.

    
    while True: #Keep majority of code, probably including login, inside while True loop.
        # Welcome screen and login.
        print("\t\tWelcome to the Sharpest Tool in the Shed!\n\t\t\tPlease log in or create account!")
        # Probably separate module/s with login functionality/account creation/quit option.
        # # account() module to login/create account.
        clear()
        while True:
            # Modules depending on account class.
                #User: purchase, history, reserve, etc.
                #Admin: view all orders, view customer lists, modify accounts and inventory.
            # Close out all files and remember to commit all db changes on log out...
            clear()
            pass
        # Loop back around to login
        pass
    # Include some kind of parting farewell thanking the customer.
    pass



if __name__ == "__main__":
    main()