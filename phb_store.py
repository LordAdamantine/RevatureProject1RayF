import re
import logging
from pymongo import MongoClient
import os
from login_procedures import login
from transactions import purchase, conversion

'''
To Do:
Introduction - Done
    preload certain functions and data
Login options - Done
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
    orders = db.orders
    logging.info("Loading database records...")

    # clear()
    # test = weapons.find_one({'name':'Longsword'})
    # print(test.get('name'))
    # return 0

    # stock_print(armor, weapons, gear, misc)
    # accounts_print(users)
    # return 0


    clear()
    # Welcome ascii art, I worked very hard on it
    with open('welcome.txt') as f:
        intro = f.read()
    print(str(intro))

    
    while True: #Keep majority of code, probably including login, inside while True loop.
        # Welcome screen and login.
        input("\t\t\t\tWelcome to the Sharpest Tool in the Shed!\n\t\t\t\tPlease log in or create an account!")
        clear()
        

        # Probably separate module/s with login functionality/account creation/quit option.
        administration = False
        shopping = False
        discount = False
        user = login(users)
        # account() module to login/create account.
        if user == None:
            break


        if user.get('Status') == "Admin":
            administration = True
            logging.info("Administrator login detected.")
        if user.get('Status') != "Customer":
            discount = True
        if user.get('Status') != "Admin":
            shopping = True

        while administration:
            while True:
                try:
                    menu_option = str(input("\t\tAdministrator Actions\n\tStock\n\tAccounts\n\tOrders\n\tShop\n\tQuit"))
                    menu_option = menu_option.lower()
                except ValueError as ve:
                    print("Invalid input, please try again.")
                    logging.error("Invalid admin menu input, trying again...")
                else:
                    break
            match menu_option:
                case "stock":
                    stock_print(armor, weapons, gear, misc)
                    input("\n")
                case "accounts":
                    accounts_print(users)
                    input("\n")
                case "orders":
                    pass
                case "shop":
                    shopping = True
                    break
                case "quit":
                    break

        while shopping:
            clear()
            try:
                menu_option = str(input(f"\t\tWhat would you like to do today?\n\tMake a Purchase\n\tOrder History\n\tDeposit Funds\n\tQuit\t\t{conversion(user.get('Wallet'))}"))
                menu_option = menu_option.lower()
            except ValueError as ve:
                print("Invalid input, please try again.")
                logging.error("Invalid store menu input, trying again...")
            else:
                break
            
            if "shop" in menu_option:
                purchase(armor, weapons, gear, misc, orders, user)
            elif "purchase" in menu_option:
                purchase(armor, weapons, gear, misc, orders, user)
            elif "store" in menu_option:
                purchase(armor, weapons, gear, misc, orders, user)
            elif "order" in menu_option:
                pass
            elif "history" in menu_option:
                pass
            elif "deposit" in menu_option:
                pass
            elif "quit"  in menu_option:
                break
            else:
                print("Error, try again.")
                logging.error("Store option limit exceeded, trying again...")

            # By putting most functionality into modules, reduce main code clutter, especially for looping actions.
        
        # Already naturally loops back to start to where there's an option to break out.

    # Include some kind of parting farewell thanking the customer upon breaking out and quitting.
    clear()
    with open("thanks.txt") as f:
        outro = f.read()
    print(str(outro))
    logging.info("Closing store interface.")
    input()
    return 0




def accounts_print(users):
    user_list = users.find({}, {'First Name':1, 'Status':1, 'Wallet':1, '_id':0})
    
    for elem in user_list:
        user_name = str(elem.get('First Name'))
        user_status = str(elem.get('Status'))
        user_wallet = conversion(elem.get('Wallet'))
        print("User: " + f"{user_name:20}", end=" | ")
        print("Account type: " + f"{user_status:>10}", end=" | ")
        print("Available Funds: " + f"{user_wallet:>5}", end=" | \n")

def stock_print(armor, weapons, gear, misc):
    armor_test = armor.find({}, {'name':1, 'cost':1, 'stock':1, '_id':0})
    weapons_test = weapons.find({}, {'name':1, 'cost':1, 'stock':1, '_id':0})
    gear_test = gear.find({}, {'name':1, 'cost':1, 'stock':1, '_id':0})
    misc_test = misc.find({}, {'name':1, 'cost':1, 'stock':1, '_id':0})

    print("\n" + "Armor Sets")
    for elem in armor_test:
        item_name = str(elem.get('name'))
        item_price = conversion(elem.get('cost'))
        item_count = str(elem.get('stock'))
        print("Item: " + f"{item_name:40}", end=" | ")
        print("Price: " + f"{item_price:>10}", end=" | ")
        print("Count: " + f"{item_count:>5}", end=" | \n")
    print("\n" + "Weapons")
    for elem in weapons_test:
        item_name = str(elem.get('name'))
        item_price = conversion(elem.get('cost'))
        item_count = str(elem.get('stock'))
        print("Item: " + f"{item_name:40}", end=" | ")
        print("Price: " + f"{item_price:>10}", end=" | ")
        print("Count: " + f"{item_count:>5}", end=" | \n")
    print("\n" + "Miscellaneous Gear")
    for elem in gear_test:
        item_name = str(elem.get('name'))
        item_price = conversion(elem.get('cost'))
        item_count = str(elem.get('stock'))
        print("Item: " + f"{item_name:40}", end=" | ")
        print("Price: " + f"{item_price:>10}", end=" | ")
        print("Count: " + f"{item_count:>5}", end=" | \n")
    print("\n" + "Magical Baubles")
    for elem in misc_test:
        item_name = str(elem.get('name'))
        item_price = conversion(elem.get('cost'))
        item_count = str(elem.get('stock'))
        print("Item: " + f"{item_name:40}", end=" | ")
        print("Price: " + f"{item_price:>10}", end=" | ")
        print("Count: " + f"{item_count:>5}", end=" | \n")
    print("\n")


if __name__ == "__main__":
    main()