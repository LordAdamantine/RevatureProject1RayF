import os
import logging
from pymongo import MongoClient
import re
from conversion_kit import conversion
from purchase_order_weapons import purchase_weapon
from purchase_order_armor import purchase_armor
from purchase_order_gear import purchase_gear
clear = lambda: os.system('cls')

def purchase(armor, weapons, gear, misc, orders, user, users, discount):
    clear()
    
    while True:
        
        try:
            menu_option = str(input(f"\n\n\tAvailable Funds: {conversion(user.get('Wallet'))}\n\tCategories:\n\tArmor\n\tWeapons\n\tAdventuring Gear\n\tOther\n\tQuit\n\t"))
            menu_option = menu_option.lower()
        except ValueError as ve:
            print("Invalid input, please try again.")
            logging.error("Invalid store menu input, trying again...")
        
        if "weap" in menu_option:
            purchase_weapon(weapons, orders, user, users, discount)
        elif "arm" in menu_option:
            purchase_armor(armor, orders, user, users, discount)
        elif "adven" in menu_option:
            purchase_gear(gear, orders, user, users, discount)
        elif "gear" in menu_option:
            purchase_gear(gear, orders, user, users, discount)
        elif "magic" in menu_option:
            print("Coming soon...")
        elif "misc" in menu_option:
            print("Coming soon...")
        elif "other" in menu_option:
            print("Coming soon...")
        elif "quit"  in menu_option:
            break
        else:
            print("Error, try again.")
            logging.error("Store option limit exceeded, trying again...")

# Separated purchase definitions into separate modules due to large size from unique modifications necessary for each.
        