from conversion_kit import conversion
import re
import logging
import os
clear = lambda: os.system('cls')

# Purchase module for weapons, will be considered the default for explaining structures and providing documentation on the purchase order modules.

def purchase_weapon(weapons, orders, user, users, discount):
    logging.info("Entered weapons purchase module.")
    while True:
        purchasing = False
        clear()
        try:        # main menu
            menu_option = str(input(f"\n\tAvailable Funds: {conversion(user.get('Wallet'))}\n\tSort by: Weaponry\n\tClassification\n\tName\n\tCost\n\tDamage\n\tProperties\n\tPurchase\n\tQuit\n\t"))
            menu_option = menu_option.lower()
        except ValueError as ve:
            print("Invalid input, please try again.")
            logging.error("Invalid store menu input, trying again...")

        if "class" in menu_option:      # Searches for weapons of particular classes
            while True:
                menu_option = str(input(f"\n\tSort by: Classification\n\tSimple Melee\n\tMartial Melee\n\tSimple Ranged\n\tMartial Ranged\n\tAll\n\tPurchase\n\tQuit\n\t"))
                menu_option = menu_option.lower()
                printing = False
                purchasing = False

                if "simple" in menu_option:     # decided easiest way to do it was to just account for all combinations through a few nested ifelse blocks.
                    if "melee" in menu_option:
                        weapons_test = weapons.find({'classification':'simple melee'})
                        printing = True
                    elif "ranged" in menu_option:
                        weapons_test = weapons.find({'classification':'simple ranged'})
                        printing = True
                    else:
                        weapons_test = weapons.find({'classification': {'$regex': 'simple', '$options': 'i'}})
                        printing = True
                elif "martial" in menu_option:
                    if "melee" in menu_option:
                        weapons_test = weapons.find({'classification':'martial melee'})
                        printing = True
                    elif "ranged" in menu_option:
                        weapons_test = weapons.find({'classification':'martial ranged'})
                        printing = True
                    else:
                        weapons_test = weapons.find({'classification': {'$regex': 'martial', '$options': 'i'}})
                        printing = True
                if "melee" in menu_option:
                    if "simple" in menu_option:
                        weapons_test = weapons.find({'classification':'simple melee'})
                        printing = True
                    elif "martial" in menu_option:
                        weapons_test = weapons.find({'classification':'martial melee'})
                        printing = True
                    else:
                        weapons_test = weapons.find({'classification': {'$regex': 'melee', '$options': 'i'}})
                        printing = True
                elif "ranged" in menu_option:
                    if "simple" in menu_option:
                        weapons_test = weapons.find({'classification':'simple ranged'})
                        printing = True
                    elif "martial" in menu_option:
                        weapons_test = weapons.find({'classification':'martial ranged'})
                        printing = True
                    else:
                        weapons_test = weapons.find({'classification': {'$regex': 'ranged', '$options': 'i'}})
                        printing = True
                elif "full" in menu_option:     # Just lists all items
                    weapons_test = weapons.find({}).sort('classification')
                    printing = True
                elif "all" in menu_option:
                    weapons_test = weapons.find({}).sort('classification')
                    printing = True
                elif "purchase" in menu_option:     # any of these cause a break to the end where the final purchase is processed
                    purchasing = True
                    break
                elif "buy" in menu_option:
                    purchasing = True
                    break
                elif "quit" in menu_option:
                    break
                else:
                    print("Invalid input, please try again.")
                    logging.error("Invalid store menu input, trying again...")

                if printing:        # Specifically prints to specification of the menu, where much of the bulk of these modules comes from
                    print("\n" + "Weapons Stock - classification")
                    for elem in weapons_test:
                        if int(elem.get('stock')) != 0:
                            item_class = str(elem.get('classification'))
                            item_price = conversion(elem.get('cost'))
                            item_name = str(elem.get('name'))
                            item_count = str(elem.get('stock'))
                            print("Class: " + f"{item_class:20}", end=" | ")
                            print("Price: " + f"{item_price:>15}", end=" | ")
                            print("Item: " + f"{item_name:40}", end=" | ")
                            print("Count: " + f"{item_count:>5}", end=" | \n")
                    print("\n\n")
        elif "name" in menu_option:     # Search by name function, compares a regular expression to the names of all entries.
            while True:
                weapons_test = None
                menu_option = str(input(f"\n\tInput search terms, purchase, or quit\n\t"))
                menu_option = menu_option.lower()
                printing = False
                purchasing = False

                # initialize first to see if it's empty
                weapons_test = weapons.find({'name': {'$regex': menu_option, '$options': 'i'}}).sort('name')

                if type(weapons_test) == None:
                    print("Invalid input, please try again.")
                    logging.error("Invalid store menu input, trying again...")
                if "purch" in menu_option:
                    purchasing = True
                    break
                elif "buy" in menu_option:
                    purchasing = True
                    break
                elif "quit" in menu_option:
                    break
                else:
                    printing = True

                if printing:        # Prints selected details about items
                    print("\n" + "Weapons Stock - Search")
                    for elem in weapons_test:
                        if int(elem.get('stock')) != 0:
                            item_name = str(elem.get('name'))
                            item_class = str(elem.get('classification'))
                            item_damage = str(elem.get('damage'))
                            item_price = conversion(elem.get('cost'))
                            item_weight = str(elem.get('weight'))
                            item_count = str(elem.get('stock'))
                            print("Item: " + f"{item_name:40}", end=" | ")
                            print("Class: " + f"{item_class:20}", end=" | ")
                            print("Damage: " + f"{item_damage:20}", end=" | ")
                            print("Price: " + f"{item_price:>15}", end=" | ")
                            print("Weight: " + f"{item_weight:>5} lbs", end=" | ")
                            print("Count: " + f"{item_count:>5}", end=" | \n")
                    print("\n\n")
        elif "cost" in menu_option:
            while True:
                menu_option = str(input(f"\n\tSort by: Cost\n\tAscending\n\tDescending\n\tPurchase\n\tQuit\n"))
                menu_option = menu_option.lower()
                printing = False
                purchasing = False

                if "asc" in menu_option:
                    weapons_test = weapons.find({}).sort('cost', 1)
                    printing = True
                elif "up" in menu_option:
                    weapons_test = weapons.find({}).sort('cost', 1)
                    printing = True
                elif "des" in menu_option:
                    weapons_test = weapons.find({}).sort('cost', -1)
                    printing = True
                elif "down" in menu_option:
                    weapons_test = weapons.find({}).sort('cost', -1)
                    printing = True
                elif "pur" in menu_option:
                    purchasing = True
                    break
                elif "buy" in menu_option:
                    purchasing = True
                    break
                elif "quit" in menu_option:
                    break
                else:
                    print("Invalid input, please try again.")
                    logging.error("Invalid store menu input, trying again...")

                if printing:
                    print("\n" + "Weapons Stock - Price")
                    for elem in weapons_test:
                        if int(elem.get('stock')) != 0:
                            item_price = conversion(elem.get('cost'))
                            item_name = str(elem.get('name'))
                            item_count = str(elem.get('stock'))
                            print("Price: " + f"{item_price:>15}", end=" | ")
                            print("Item: " + f"{item_name:40}", end=" | ")
                            print("Count: " + f"{item_count:>5}", end=" | \n")
                    print("\n\n")
        elif "damage" in menu_option:
            while True:     # Forgot to add leniency in input, accidentally had it anyway because of my use of regex, high five!
                menu_option = str(input(f"\n\tSort by: Damage Type\n\tSlashing\n\tPiercing\n\tBludgeoning\n\tOther\n\tPurchase\n\tQuit\n\t"))
                menu_option = menu_option.lower()
                printing = False
                purchasing = False

                weapons_test = weapons.find({'damage': {'$regex': menu_option, '$options': 'i'}}).sort('damage')

                if "other" in menu_option:
                    weapons_test = weapons.find().sort('damage')
                    printing = True
                elif "pur" in menu_option:
                    purchasing = True
                    break
                elif "buy" in menu_option:
                    purchasing = True
                    break
                elif "quit" in menu_option:
                    break
                elif type(weapons_test) != None:
                    printing = True
                else:
                    print("Invalid input, please try again.")
                    logging.error("Invalid store menu input, trying again...")

                if printing:
                    print("\n" + "Weapons Stock - classification")
                    for elem in weapons_test:
                        if int(elem.get('stock')) != 0:
                            item_damage = str(elem.get('damage'))
                            item_name = str(elem.get('name'))
                            item_price = conversion(elem.get('cost'))
                            item_count = str(elem.get('stock'))
                            print("Damage: " + f"{item_damage:20}", end=" | ")
                            print("Item: " + f"{item_name:40}", end=" | ")
                            print("Price: " + f"{item_price:>15}", end=" | ")
                            print("Count: " + f"{item_count:>5}", end=" | \n")
                    print("\n\n")
        elif "prop" in menu_option:
            while True:     # Only one that interacts with the arrays that hold the property values.
                weapons_test = None
                menu_option = str(input(f"\n\tInput property search terms, purchase, or quit\n\t"))
                menu_option = menu_option.lower()
                printing = False
                purchasing = False

                weapons_test = weapons.find({'properties': {'$regex': menu_option, '$options': 'i'}}).sort('name')

                if type(weapons_test) == None:
                    print("Invalid input, please try again.")
                    logging.error("Invalid store menu input, trying again...")
                if "purch" in menu_option:
                    purchasing = True
                    break
                elif "buy" in menu_option:
                    purchasing = True
                    break
                elif "quit" in menu_option:
                    break
                else:
                    printing = True

                if printing:
                    print("\n" + "Weapons Stock - Properties")
                    for elem in weapons_test:
                        if int(elem.get('stock')) != 0:
                            item_name = str(elem.get('name'))
                            item_price = conversion(elem.get('cost'))
                            item_count = str(elem.get('stock'))
                            print("Item: " + f"{item_name:40}", end=" | ")
                            print("Price: " + f"{item_price:>15}", end=" | ")
                            print("Count: " + f"{item_count:>5}", end=" | \n")
                            for item_property in elem.get('properties'):        # The magic code that made it somehow work.
                                print(item_property, end=", ")
                            print("")
                    print("\n\n")
        elif "buy" in menu_option:
            purchasing = True
        elif "pur" in menu_option:
            purchasing = True
        elif "quit"  in menu_option:
            break
        else:
            print("Error, try again.")
            logging.error("Store option limit exceeded, trying again...")

        if purchasing:      # Actually onto buying something, selecting by name, input protected of course
            confirmed = True
            while confirmed:
                try:
                    purchase_name = input("\n\tPlease enter the name of the item you would like to purchase:\n>>> ")
                except ValueError as ve:
                    print("Invalid input, please try again.")
                    logging.error("Invalid store menu input, trying again...")

                if "quit" in purchase_name:
                    break

                cart = weapons.find_one({'name': {'$regex': f'{purchase_name}', '$options': 'i'}})

                if cart == None:
                    print("Error, item does not exist, try again.")
                    logging.error("Item not found, trying again...")
                    continue
                elif int(cart.get('stock')) == 0:
                    print("I'm sorry, that item is out of stock, please select another item.")
                    logging.stock("Item out of stock")
                    continue
                elif int(cart.get('cost')) > int(user.get('Wallet')):
                    print("I'm sorry, you cannot seem to afford that, please select another item.")
                    logging.stock("Insufficient funds attempt.")
                    continue

                print("\n" + "Please confirm your selection.")
                item_name = str(cart.get('name'))
                item_class = str(cart.get('classification'))
                item_damage = str(cart.get('damage'))
                item_price = conversion(cart.get('cost'))
                item_weight = str(cart.get('weight'))
                item_count = str(cart.get('stock'))
                print("Item: " + f"{item_name}", end=" | ")
                print("Class: " + f"{item_class:20}", end=" | ")
                print("Damage: " + f"{item_damage:20}", end=" | ")
                print("Price: " + f"{item_price:>15}", end=" | ")
                print("Weight: " + f"{item_weight:>5} lbs", end=" | ")
                print("Count: " + f"{item_count:>5}", end=" | \n")
                for item_property in cart.get('properties'):
                    print(item_property, end=", ")
                print("")

                while True:     # User confirmation input checking.
                    try:
                        confirmation = str(input("Is this the correct item? Y/N? >>> "))
                        confirmation = confirmation.lower()
                    except ValueError as ve:
                        print("Improper input detected, try again.")
                        logging.error("Invalid confirmation, trying again...")
                    
                    if "y" in confirmation:
                        pw_checking = input("\nPlease input your password to confirm purchase:\n\t>>>\t")
                        if str(pw_checking) == str(user.get('Password')):
                            confirmed = False
                            break
                        else:
                            print("Password incorrect.")
                            logging.error("Incorrect password input, trying again...")
                    elif "n" in confirmation:
                        print("Please try again.")
                        logging.info("Reconfirming item.")
                        break
                    else:
                        print("Improper input detected, try again.")
                        logging.error("Invalid confirmation, trying again...")

            # Confirmed order pushed to orders database.
            if confirmed == False:
                print(f"Thank you for purchasing a {cart.get('name')}! Enjoy your purchase!")
                logging.info("Pushing order to database.")
                newOrder = {'User':str(user.get('Username')), 'Spent':int(cart.get('cost')), 'Bought':str(cart.get('name')), 'Category':'Weapon'}
                orders.insert_one(newOrder)
                newStock = int(cart.get('stock')) - 1
                weapons.update_one({'name':str(cart.get('name'))}, { "$set": { 'stock': newStock } })
                if discount:
                    discounted = cart.get('cost') * 0.90
                    newWallet = int(user.get('Wallet')) - int(discounted)
                else:
                    newWallet = int(user.get('Wallet')) - int(cart.get('cost'))
                users.update_one({'Username':str(user.get('Username'))}, { "$set": { 'Wallet': newWallet}})
                input()
