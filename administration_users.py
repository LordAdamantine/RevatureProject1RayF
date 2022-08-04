import re
import logging
from pymongo import MongoClient
import os
from conversion_kit import conversion
from login_procedures import signup
clear = lambda: os.system('cls')        # Noticed ones like this can just be put outside to give every module inside access to these easy actions.

def user_administration(users, client):
    while True:
        clear()
        try:
            menu_option = str(input("\n\n\t\tAccount Administrator Actions:\n\tView Accounts\n\tModify User Access\n\tDelete User\n\tAdd New Customer\n\tQuit\n\t"))
            menu_option = menu_option.lower()
        except ValueError as ve:
            print("Invalid input, please try again.")
            logging.error("Invalid admin menu input, trying again...")

        if "view" in menu_option:
            clear()
            accounts_print(users)
        elif "mod" in menu_option:
            clear()
            print("Modifying user access credentials.")
            modify_accounts(users, client)
        elif "del" in menu_option:
            clear()
            remove_accounts(users, client)
        elif "rem" in menu_option:
            clear()
            remove_accounts(users, client)
        elif "add" in menu_option:
            clear()
            signup(users, client)
        elif "new" in menu_option:
            clear()
            signup(users, client)
        elif "qui" in menu_option:
            clear()
            break

def accounts_print(users):
    user_list = users.find({}, {'First Name':1,'Username':1, 'Status':1, 'Wallet':1, '_id':0})
    
    for elem in user_list:
        if elem != None:
            user_name = str(elem.get('First Name'))
            username = str(elem.get('Username'))
            user_status = str(elem.get('Status'))
            user_wallet = conversion(elem.get('Wallet'))
            print("User: " + f"{user_name:20}", end=" | ")
            print("Username: " + f"{username:20}", end=" | ")
            print("Account type: " + f"{user_status:>15}", end=" | ")
            print("Available Funds: " + f"{user_wallet:>15}", end=" | \n")
    input("Press enter to continue.")

        
def remove_accounts(users, client):
    while True:
        while True:
            try:
                uname = str(input("\t\tPlease enter target user name:\t\t"))
                check = re.search("," or "@" or "!" or "#" or "$" or "%" or "&", uname)
                existing = users.find_one({'Username':str(uname)})
                if check != None:
                    raise ValueError
                if existing == None:        # Makes sure they're using an existing login.
                    print("Username not detected, please try again.")
                    logging.error("Username not found, trying again...")
                    continue
            except ValueError as ve:
                print("Warning, improper input detected.")
                logging.error("Attempted illegal character in username, trying again...")
                continue
            else:

                break
        uname = str(existing.get('Username'))
        fname = str(existing.get('First Name'))
        status = str(existing.get('Status'))
        print(uname + " : " + fname + " : " + status + "\n")

        while True:
            try:
                menu_option = str(input(f"\n\n\t\tWould you like to delete account of {uname}? Yes or No?"))
                menu_option = menu_option.lower()
            except ValueError as ve:
                print("Invalid input, please try again.")
                logging.error("Invalid admin menu input, trying again...")

            if "y" in menu_option:
                break
            else:
                return
        
        with client.start_session() as session:
            with session.start_transaction():
                users.delete_one({'Username':str(uname)})
        break

def modify_accounts(users, client):
    while True:
        try:
            uname = str(input("\t\tPlease enter target user name:\t\t"))
            check = re.search("," or "@" or "!" or "#" or "$" or "%" or "&", uname)
            existing = users.find_one({'Username':str(uname)})
            if check != None:
                raise ValueError
            if existing == None:        # Makes sure they're using an existing login.
                print("Username not detected, please try again.")
                logging.error("Username not found, trying again...")
                continue
        except ValueError as ve:
            print("Warning, improper input detected.")
            logging.error("Attempted illegal character in username, trying again...")
            continue
        else:

            break
    
    while True:
        try:
            menu_option = str(input(f"\n\n\t\tWhat level of access {existing.get('First Name')} have?\n\tCustomer\n\tEmployee\n\tAdmin\n\tQuit\n\t"))
            menu_option = menu_option.lower()
            if "quit" in menu_option:
                return
        except ValueError as ve:
            print("Invalid input, please try again.")
            logging.error("Invalid admin menu input, trying again...")

        if "cust" in menu_option:
            access = "Customer"
            break
        elif "emp" in menu_option:
            access = "Employee"
            break
        elif "admin" in menu_option:
            access = "Admin"
            break
    
    with client.start_session() as session:
        with session.start_transaction():
            users.update_one({'Username':str(uname)}, { "$set": { 'Status': access}})
        
