import re
import logging
from pymongo import MongoClient
import os
from login_procedures import login
from transactions import purchase
from conversion_kit import conversion
from administration_users import user_administration
from administration_orders import orders_administration
from administration_stock import stock_administration

'''
To Do:
Introduction - Done
    preload certain functions and data
Login options - Done
    User vs Admin vs account creation
Store functionality - Done
    Purchase, order history, admin management
Multiple data tables - Done
Manipulating said tables - Done
Event Logging - Done


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
    # user = users.find_one({'Username':'admin'})
    # orderHistory(orders, user)
    # return 0


    clear()
    # Welcome ascii art, I worked very hard on it
    with open('welcome.txt') as f:
        intro = f.read()
    print(str(intro))

    
    while True: #Keep majority of code, probably including login, inside while True loop.
        # Welcome screen and login.
        input("\t\t\t\tWelcome to the Sharpest Tool in the Shed!\n\t\t\t\tPlease log in or create an account!\n")
        clear()
        

        # Probably separate module/s with login functionality/account creation/quit option.
        administration = False
        shopping = False
        discount = False
        userName = None
        # account() module to login/create account.
        user = login(users, client)
        if user == None:
            break
        UserName = user.get('Username')
        user = users.find_one({'Username':str(UserName)})
        userWallet = user.get('Wallet')     # My workaround to a strange issue with everything else working but the wallet, strangely, not updating in application, only on launch.
        logging.info(f"{UserName} has logged in.")
        # for elem in user:
        #     print(elem)
        # login_test = user.get('First Name')
        # print(login_test)


        if user.get('Status') == "Admin":
            administration = True
            logging.info("Administrator login detected.")
        if user.get('Status') != "Customer":
            discount = True
        if user.get('Status') != "Admin":
            shopping = True

        while administration:       # Only admin status allows access to this menu.

            try:
                menu_option = str(input("\n\n\t\tAdministrator Actions\n\tStock\n\tAccounts\n\tOrders\n\tShop\n\tQuit\n\t"))
                menu_option = menu_option.lower()
            except ValueError as ve:
                print("Invalid input, please try again.")
                logging.error("Invalid admin menu input, trying again...")

            if "shop" in menu_option:       # Other accounts default to the shopping menu, these allow the admins to use the employee discount.
                shopping = True
                break
            elif "pur" in menu_option:
                shopping = True
                break
            elif "store" in menu_option:
                shopping = True
                break
            elif "buy" in menu_option:
                shopping = True
                break
            elif "ord" in menu_option:      # Input freedom achieved through modules and elif substring in blocks.
                orders_administration(users, orders, client)
            elif "hist" in menu_option:
                orders_administration(users, orders, client)
            elif "acc" in menu_option:
                user_administration(users, client)
            elif "stock" in menu_option:
                stock_administration(armor, weapons, gear, misc, client)
            elif "qui"  in menu_option:
                break
            else:
                print("Error, try again.")
                logging.error("Administration option limit exceeded, trying again...")
                    

        clear()

        while shopping:
            clear()
            
            UserName = user.get('Username')
            user = users.find_one({'Username':str(UserName)})
            try:
                menu_option = str(input(f"\nYou have: {conversion(userWallet)}\n\t\tWhat would you like to do today?\n\tMake a Purchase\n\tOrder History\n\tDeposit Funds\n\tQuit\n\t"))
                menu_option = menu_option.lower()
            except ValueError as ve:
                print("Invalid input, please try again.")
                logging.error("Invalid store menu input, trying again...")
                
            
            clear()

            if "shop" in menu_option:       # Again, input freedom.
                userWallet = purchase(armor, weapons, gear, misc, orders, user, users, discount, client, userWallet)
            elif "pur" in menu_option:
                userWallet = purchase(armor, weapons, gear, misc, orders, user, users, discount, client, userWallet)
            elif "store" in menu_option:
                userWallet = purchase(armor, weapons, gear, misc, orders, user, users, discount, client, userWallet)
            elif "buy" in menu_option:
                userWallet = purchase(armor, weapons, gear, misc, orders, user, users, discount, client, userWallet)
            elif "order" in menu_option:
                orderHistory(orders, user, orders)
            elif "hist" in menu_option:
                orderHistory(orders, user, orders)
            elif "dep" in menu_option:      #Only place where funds are added like this, not even repeated option functions like the above orderHistory.
                depositing = True
                while depositing:

                    while True:
                        try:
                            print(conversion(userWallet))
                            deposit = int(input("Please enter how many coppers you would like to add to your account.\nRemember! Coppers, Silvers, and Golds are orders of 10.\n\t>>> "))
                        except ValueError as ve:
                            print("Improper input, please try again.")
                            logging.error("Invalid input on deposit, trying again.")
                        else:
                            break

                    while True:
                        try:
                            confirmation = str(input(f"Is {conversion(deposit)} right?\t\t"))
                        except ValueError as ve:
                            print("Improper input, please try again.")
                            logging.error("Invalid input on deposit confirmation, trying again.")
                        if "y" in confirmation: # Adaptive deposit logging.
                            UserName = user.get('Username')
                            user = users.find_one({'Username':str(UserName)})
                            print(f"Thank you for your deposit! {conversion(deposit)} have been added to your account!\n")
                            logging.info(f"{conversion(deposit)} amount added to account: {UserName}")
                            newWallet = int(user.get('Wallet')) + deposit
                            logging.info(f"{UserName} has deposited {conversion(deposit)} into their account.")
                            with client.start_session() as session:
                                with session.start_transaction():
                                    users.update_one({'Username':UserName}, { "$set": { 'Wallet': newWallet}})
                            userWallet += deposit
                            UserName = user.get('Username')
                            user = users.find_one({'Username':str(UserName)})
                            depositing = False
                            break
                        if "n" in confirmation:
                            break
                        if "q" in confirmation:
                            depositing = False
                            break

            elif "qui"  in menu_option:
                break
            else:
                print("Error, try again.")
                logging.error("Store option limit exceeded, trying again...")
            # By putting most functionality into modules, reduce main code clutter, especially for looping actions.
        clear()
        logging.info(f"{UserName} has logged out.")
        # Already naturally loops back to start to where there's an option to break out.

    # Include some kind of parting farewell thanking the customer upon breaking out and quitting.
    with open("thanks.txt") as f:
        outro = f.read()
    print(str(outro))
    logging.info("Closing store interface.")
    return 0


def orderHistory(orders, user, users):
    print("\n")
    UserName = user.get('Username')
    user = users.find_one({'Username':str(UserName)})
    order_history = orders.find({'User': f'{UserName}'}).sort('name')

    for elem in order_history:
        if elem != None:
            user_name = elem.get('User')
            value = conversion(elem.get('Spent'))
            category = elem.get('Category')
            item_name = elem.get('Bought')
            print("User: " + f"{user_name:20}", end=" | ")
            print("Amount Spent: " + f"{value:>15}", end=" | ")
            print("Item Bought: " + f"{item_name:40}", end=" | ")
            print("Category: " + f"{category:>10}", end=" | \n")
    input("Press any key to continue.")



# Following were for testing and templating.  Left for posterity.

def accounts_print(users):
    user_list = users.find({}, {'First Name':1, 'Status':1, 'Wallet':1, '_id':0})
    
    for elem in user_list:
        if elem != None:
            user_name = str(elem.get('First Name'))
            user_status = str(elem.get('Status'))
            user_wallet = conversion(elem.get('Wallet'))
            print("User: " + f"{user_name:20}", end=" | ")
            print("Account type: " + f"{user_status:>15}", end=" | ")
            print("Available Funds: " + f"{user_wallet:>15}", end=" | \n")
    input("Press any key to continue.")

def stock_print(armor, weapons, gear, misc):
    armor_test = armor.find({}, {'name':1, 'cost':1, 'stock':1, '_id':0})
    weapons_test = weapons.find({}, {'name':1, 'cost':1, 'stock':1, '_id':0})
    gear_test = gear.find({}, {'name':1, 'cost':1, 'stock':1, '_id':0})
    misc_test = misc.find({}, {'name':1, 'cost':1, 'stock':1, '_id':0})

    print("\n" + "Armor Sets")
    for elem in armor_test:
        if elem != None:
            item_name = str(elem.get('name'))
            item_price = conversion(elem.get('cost'))
            item_count = str(elem.get('stock'))
            print("Item: " + f"{item_name:40}", end=" | ")
            print("Price: " + f"{item_price:>15}", end=" | ")
            print("Count: " + f"{item_count:>5}", end=" | \n")
    print("\n" + "Weapons")
    for elem in weapons_test:
        if elem != None:
            item_name = str(elem.get('name'))
            item_price = conversion(elem.get('cost'))
            item_count = str(elem.get('stock'))
            print("Item: " + f"{item_name:40}", end=" | ")
            print("Price: " + f"{item_price:>15}", end=" | ")
            print("Count: " + f"{item_count:>5}", end=" | \n")
    print("\n" + "Miscellaneous Gear")
    for elem in gear_test:
        if elem != None:
            item_name = str(elem.get('name'))
            item_price = conversion(elem.get('cost'))
            item_count = str(elem.get('stock'))
            print("Item: " + f"{item_name:40}", end=" | ")
            print("Price: " + f"{item_price:>15}", end=" | ")
            print("Count: " + f"{item_count:>5}", end=" | \n")
    print("\n" + "Magical Baubles")
    for elem in misc_test:
        if elem != None:
            item_name = str(elem.get('name'))
            item_price = conversion(elem.get('cost'))
            item_count = str(elem.get('stock'))
            print("Item: " + f"{item_name:40}", end=" | ")
            print("Price: " + f"{item_price:>15}", end=" | ")
            print("Count: " + f"{item_count:>5}", end=" | \n")
    print("\n")
    input("Press any key to continue.")


if __name__ == "__main__":
    main()