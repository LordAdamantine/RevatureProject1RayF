import re
import logging
from pymongo import MongoClient
import os
from conversion_kit import conversion
clear = lambda: os.system('cls')

def stock_administration(armor, weapons, gear, misc, client):
    while True:

        while True:
            clear()
            try:
                menu_option = str(input("\n\n\t\tStock Administrator Actions:\n\tView Armor\n\tView Weapons\n\tView Gear\n\tView Misc\n\tRemove Item from Stock\n\tRestock Item\n\tQuit\n\t"))
                menu_option = menu_option.lower()
            except ValueError as ve:
                print("Invalid input, please try again.")
                logging.error("Invalid stock admin menu input, trying again...")
            # Quickly print all items for each category for reference.
            # Cycles through the print options until you quit out or decide to edit stock.
            # Did not have time to implement adding stock through the interface.
            if "arm" in menu_option:
                clear()
                armor_print(armor)
            elif "weap" in menu_option:
                clear()
                weapons_print(weapons)
            elif "gear" in menu_option:
                clear()
                gear_print(gear)
            elif "adv" in menu_option:
                clear()
                gear_print(gear)
            elif "misc" in menu_option:
                clear()
                input("Soon...")
            elif "mag" in menu_option:
                clear()
                input("Soon...")
            elif "oth" in menu_option:
                clear()
                input("Soon...")
            elif "rem" in menu_option:
                selection = "discontinue"
                clear()
                break
            elif "del" in menu_option:
                selection = "discontinue"
                clear()
                break
            elif "res" in menu_option:
                selection = "restock"
                clear()
                break
            elif "qui" in menu_option:
                clear()
                return

        while True:
            try:
                menu_option = input(f"What item category would you like to {selection}?\n\t>>> ")
            except ValueError as ve:
                print("Invalid input, please try again.")
                logging.error(f"Invalid {selection} input, trying again...")

            
            if "arm" in menu_option:
                category = armor
                break
            elif "weap" in menu_option:
                category = weapons
                break
            elif "gear" in menu_option:
                category = gear
                break
            elif "adv" in menu_option:
                category = gear
                break
            elif "misc" in menu_option:
                input("Soon...")
            elif "mag" in menu_option:
                input("Soon...")
            elif "oth" in menu_option:
                input("Soon...")
            elif "qui" in menu_option:
                clear()
                return

        while True:
            try:
                menu_option = input(f"What item would you like to {selection}?\n\t>>> ")
            except ValueError as ve:
                print("Invalid input, please try again.")
                logging.error(f"Invalid {selection} input, trying again...")
            if "qui" in menu_option:
                print("Aborting process.")
                break
            target = category.find_one({'name': {'$regex': menu_option, '$options': 'i'}})
            if target != None:
                item_name = target.get('name')
                description = item_name + " | "
                if target.get('classification') != None:
                    description += (target.get('classification') + " | ")
                if target.get('damage') != None:
                    description += (target.get('damage') + " | ")
                if target.get('AC') != None:
                    description += (target.get('AC') + " | ")
                description += (conversion(target.get('cost')) + " | ")
                print(description)
                if "y" in input(f"Would you like to {selection} the {item_name}? "):
                    stock_edit(target, category, selection, client)
                    input("Press enter to continue.")
                    break
            
def stock_edit(target, category, selection, client):
    if selection == "discontinue":
        with client.start_session() as session:
            with session.start_transaction():
                category.delete_one({'name': target.get('name')})
        print(f"The {target.get('name')} has been discontinued.")
        logging.info(f"The {target.get('name')} has been discontinued.")
    else:
        with client.start_session() as session:
            with session.start_transaction():
                category.update_one({'name':target.get('name')}, { "$set": { 'stock': 10}})
        print(f"The {target.get('name')} is back in stock!")
        logging.info(f"The {target.get('name')} is back in stock!")



def armor_print(armor):
    stock = armor.find()
    print("\n\tArmor Sets")
    for cart in stock:
        item_name = str(cart.get('name'))
        item_class = str(cart.get('classification'))
        item_AC = str(cart.get('AC'))
        item_price = conversion(cart.get('cost'))
        armor_stealth = str(cart.get('stealth'))
        armor_strength = str(cart.get('strength'))
        item_weight = str(cart.get('weight'))
        item_count = str(cart.get('stock'))
        print("Item: " + f"{item_name:40}", end=" | ")
        print("Class: " + f"{item_class:20}", end=" | ")
        print("Armor Class: " + f"{item_AC:20}", end=" | ")
        print("Price: " + f"{item_price:>15}", end=" | ")
        print("\n\t\t" + "Stealth: " + f"{armor_stealth:15}", end=" | ")
        print("Strength: " + f"{armor_strength:15}", end=" | ")
        print("Weight: " + f"{item_weight:>5} lbs", end=" | ")
        print("Count: " + f"{item_count:>5}", end=" | \n")
    input("Press enter to continue.")

def weapons_print(weapons):
    stock = weapons.find()
    print("\n\tWeapons")
    for cart in stock:
        item_name = str(cart.get('name'))
        item_class = str(cart.get('classification'))
        item_damage = str(cart.get('damage'))
        item_price = conversion(cart.get('cost'))
        item_weight = str(cart.get('weight'))
        item_count = str(cart.get('stock'))
        print("Item: " + f"{item_name:20}", end=" | ")
        print("Class: " + f"{item_class:20}", end=" | ")
        print("Damage: " + f"{item_damage:20}", end=" | ")
        print("Price: " + f"{item_price:>15}", end=" | ")
        print("Weight: " + f"{item_weight:>5} lbs", end=" | ")
        print("Count: " + f"{item_count:>5}", end=" | \n")
        for item_property in cart.get('properties'):
            print(item_property, end=", ")
        print("\n")
    input("Press enter to continue.")

def gear_print(gear):
    stock = gear.find()
    print("\n\tAdventuring Gear")
    for cart in stock:
        item_name = str(cart.get('name'))
        item_price = conversion(cart.get('cost'))
        item_weight = str(cart.get('weight'))
        item_count = str(cart.get('stock'))
        print("Item: " + f"{item_name:40}", end=" | ")
        print("Price: " + f"{item_price:>15}", end=" | ")
        print("Weight: " + f"{item_weight:>5} lbs", end=" | ")
        print("Count: " + f"{item_count:>5}", end=" | \n")
    input("Press enter to continue.")
