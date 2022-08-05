import os
import logging
from pymongo import MongoClient
import re
from conversion_kit import conversion
from purchase_order_weapons import purchase_weapon
from purchase_order_armor import purchase_armor
from purchase_order_gear import purchase_gear
clear = lambda: os.system('cls')

def purchase(armor, weapons, gear, misc, orders, user, users, discount, client, userWallet):
    
    while True:         # Handles the different purchase modules to separate the syntaxes.
        clear()
        UserName = user.get('Username')
        user = users.find_one({'Username':str(UserName)})
        userWallet = user.get('Wallet')
        try:
            menu_option = str(input(f"\n\n\tAvailable Funds: {conversion(userWallet)}\n\tCategories:\n\tArmor\n\tWeapons\n\tAdventuring Gear\n\tOther\n\tQuit\n\t"))
            menu_option = menu_option.lower()
        except ValueError as ve:
            print("Invalid input, please try again.")
            logging.error("Invalid store menu input, trying again...")
        
        if "weap" in menu_option:
            userWallet = purchase_weapon(weapons, orders, user, users, discount, client, userWallet)
        elif "arm" in menu_option:
            userWallet = purchase_armor(armor, orders, user, users, discount, client, userWallet)
        elif "adven" in menu_option:
            userWallet = purchase_gear(gear, orders, user, users, discount, client, userWallet)
        elif "gear" in menu_option:
            userWallet = purchase_gear(gear, orders, user, users, discount, client, userWallet)
        elif "magic" in menu_option:
            input("Coming soon...")
        elif "misc" in menu_option:
            input("Coming soon...")
        elif "other" in menu_option:
            input("Coming soon...")
        elif "quit"  in menu_option:
            return userWallet
        else:
            print("Error, try again.")
            logging.error("Store option limit exceeded, trying again...")

# Separated purchase definitions into separate modules due to large size from unique modifications necessary for each.
# Could technically be moved into the main module, but can't be bothered to when this works.
        