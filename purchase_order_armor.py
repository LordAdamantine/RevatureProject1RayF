from conversion_kit import conversion
import re
import logging
import os
clear = lambda: os.system('cls')

def purchase_armor(armor, orders, user, users, discount, client, userWallet):
    logging.info("Entered armor purchase module.")
    quit = True
    while quit:
        purchasing = False
        clear()
        try:
            menu_option = str(input(f"\n\tAvailable Funds: {conversion(userWallet)}\n\tSort by: Armor\n\tClassification\n\tName\n\tCost\n\tWeight\n\tOther\n\tPurchase\n\tQuit\n\t"))
            menu_option = menu_option.lower()
        except ValueError as ve:
            print("Invalid input, please try again.")
            logging.error("Invalid store menu input, trying again...")
        UserName = user.get('Username')
        user = users.find_one({'Username':str(UserName)})

        if "clas" in menu_option:
            while True:
                menu_option = str(input(f"\n\tSort by: Classification\n\tLight\n\tMedium\n\tHeavy\n\tAll\n\tPurchase\n\tQuit\n\t"))
                menu_option = menu_option.lower()
                printing = False
                purchasing = False

                if "lig" in menu_option:
                    armor_test = armor.find({'classification':'light'})
                    printing = True
                elif "med" in menu_option:
                    armor_test = armor.find({'classification':'medium'})
                    printing = True
                elif "hea" in menu_option:
                    armor_test = armor.find({'classification':'heavy'})
                    printing = True
                elif "full" in menu_option:
                    armor_test = armor.find({}).sort('classification')
                    printing = True
                elif "all" in menu_option:
                    armor_test = armor.find({}).sort('classification')
                    printing = True
                elif "pur" in menu_option:
                    purchasing = True
                    break
                elif "buy" in menu_option:
                    purchasing = True
                    break
                elif "qui" in menu_option:
                    break
                else:
                    print("Invalid input, please try again.")
                    logging.error("Invalid store menu input, trying again...")

                if printing:
                    print("\n" + "Armor Stock - classification")
                    for elem in armor_test:
                        if int(elem.get('stock')) != 0:
                            item_class = str(elem.get('classification'))
                            item_price = conversion(elem.get('cost'))
                            item_name = str(elem.get('name'))
                            item_count = str(elem.get('stock'))
                            print("Class: " + f"{item_class:10}", end=" | ")
                            print("Price: " + f"{item_price:>15}", end=" | ")
                            print("Item: " + f"{item_name:40}", end=" | ")
                            print("Count: " + f"{item_count:>5}", end=" | \n")
                    print("\n\n")
        elif "name" in menu_option:     # Search by name function
            while True:
                armor_test = None
                menu_option = str(input(f"\n\tInput search terms, purchase, or quit\n\t"))
                menu_option = menu_option.lower()
                printing = False
                purchasing = False

                armor_test = armor.find({'name': {'$regex': menu_option, '$options': 'i'}}).sort('name')

                if type(armor_test) == None:
                    print("Invalid input, please try again.")
                    logging.error("Invalid store menu input, trying again...")
                if "purc" in menu_option:
                    purchasing = True
                    break
                elif "buy" in menu_option:
                    purchasing = True
                    break
                elif "quit" in menu_option:
                    break
                else:
                    printing = True

                if printing:        # one of the more complicated print blocks just because of the large number of values and how long some are
                    print("\n" + "Armor Stock - Search")
                    for elem in armor_test:
                        if int(elem.get('stock')) != 0:
                            item_name = str(elem.get('name'))
                            item_class = str(elem.get('classification'))
                            item_AC = str(elem.get('AC'))
                            item_price = conversion(elem.get('cost'))
                            armor_stealth = str(elem.get('stealth'))
                            armor_strength = str(elem.get('strength'))
                            item_weight = str(elem.get('weight'))
                            item_count = str(elem.get('stock'))
                            print("Item: " + f"{item_name:40}", end=" | ")
                            print("Class: " + f"{item_class:20}", end=" | ")
                            print("Armor Class: " + f"{item_AC:20}", end=" | ")
                            print("Price: " + f"{item_price:>15}", end=" | ")
                            print("\n")
                            print("Stealth: " + f"{armor_stealth:>15}", end=" | ")
                            print("Strength: " + f"{armor_strength:>15}", end=" | ")
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
                    armor_test = armor.find({}).sort('cost', 1)
                    printing = True
                elif "up" in menu_option:
                    armor_test = armor.find({}).sort('cost', 1)
                    printing = True
                elif "des" in menu_option:
                    armor_test = armor.find({}).sort('cost', -1)
                    printing = True
                elif "down" in menu_option:
                    armor_test = armor.find({}).sort('cost', -1)
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
                    print("\n" + "Armor Stock - Price")
                    for elem in armor_test:
                        if int(elem.get('stock')) != 0:
                            item_price = conversion(elem.get('cost'))
                            item_name = str(elem.get('name'))
                            item_count = str(elem.get('stock'))
                            print("Price: " + f"{item_price:>15}", end=" | ")
                            print("Item: " + f"{item_name:40}", end=" | ")
                            print("Count: " + f"{item_count:>5}", end=" | \n")
                    print("\n\n")
        elif "wei" in menu_option:
            while True:
                menu_option = str(input(f"\n\tSort by: Weight\n\tAscending\n\tDescending\n\tPurchase\n\tQuit\n"))
                menu_option = menu_option.lower()
                printing = False
                purchasing = False

                if "asc" in menu_option:
                    armor_test = armor.find({}).sort('weight', 1)
                    printing = True
                elif "up" in menu_option:
                    armor_test = armor.find({}).sort('weight', 1)
                    printing = True
                elif "des" in menu_option:
                    armor_test = armor.find({}).sort('weight', -1)
                    printing = True
                elif "down" in menu_option:
                    armor_test = armor.find({}).sort('weight', -1)
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
                    print("\n" + "Armor Stock - Price")
                    for elem in armor_test:
                        if int(elem.get('stock')) != 0:
                            item_weight = str(elem.get('weight'))
                            item_name = str(elem.get('name'))
                            item_price = conversion(elem.get('cost'))
                            item_count = str(elem.get('stock'))
                            print("Weight: " + f"{item_weight:>5} lbs", end=" | ")
                            print("Item: " + f"{item_name:40}", end=" | ")
                            print("Price: " + f"{item_price:>15}", end=" | ")
                            print("Count: " + f"{item_count:>5}", end=" | \n")
                    print("\n\n")
        elif "other" in menu_option:
            while True:
                armor_test = None
                menu_option = str(input(f"\n\tCheck for strength requirements or disadvantage on stealth, purchase, or quit\n\t"))
                menu_option = menu_option.lower()
                printing = False
                purchasing = False

                if "stre" in menu_option:
                    armor_test = armor.find({'strength': {'$regex': 'requi', '$options': 'i'}}).sort('name')
                    printing = True
                elif "req" in menu_option:
                    armor_test = armor.find({'strength': {'$regex': 'requi', '$options': 'i'}}).sort('name')
                    printing = True
                elif "dis" in menu_option:
                    armor_test = armor.find({'stealth': {'$regex': 'disad', '$options': 'i'}}).sort('name')
                    printing = True
                elif "stea" in menu_option:
                    armor_test = armor.find({'stealth': {'$regex': 'disad', '$options': 'i'}}).sort('name')
                    printing = True
                elif "purch" in menu_option:
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
                    print("\n" + "Armor Stock - Special Properties")
                    for elem in armor_test:
                        if int(elem.get('stock')) != 0:
                            item_name = str(elem.get('name'))
                            armor_stealth = str(elem.get('stealth'))
                            armor_strength = str(elem.get('strength'))
                            item_price = conversion(elem.get('cost'))
                            item_count = str(elem.get('stock'))
                            print("Item: " + f"{item_name:40}", end=" | ")
                            print("Stealth: " + f"{armor_stealth:>15}", end=" | ")
                            print("Strength: " + f"{armor_strength:>15}", end=" | ")
                            print("Price: " + f"{item_price:>15}", end=" | ")
                            print("Count: " + f"{item_count:>5}", end=" | \n")
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
                    purchasing = False
                    break

                cart = armor.find_one({'name': {'$regex': f'{purchase_name}', '$options': 'i'}})

                if cart == None:
                    print("Error, item does not exist, try again.")
                    logging.error("Item not found, trying again...")
                    continue
                elif int(cart.get('stock')) == 0:
                    print("I'm sorry, that item is out of stock, please select another item.")
                    logging.stock("Item out of stock")
                    continue
                elif int(cart.get('cost')) > int(userWallet):
                    print("I'm sorry, you cannot seem to afford that, please select another item.")
                    logging.stock("Insufficient funds attempt.")
                    continue

                print("\n" + "Please confirm your selection.")
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
                print("\n" + "Stealth: " + f"{armor_stealth:>15}", end=" | ")
                print("Strength: " + f"{armor_strength:>15}", end=" | ")
                print("Weight: " + f"{item_weight:>5} lbs", end=" | ")
                print("Count: " + f"{item_count:>5}", end=" | \n")

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
                username = user.get('Username')
                print(f"Thank you for purchasing a {cart.get('name')}! Enjoy your purchase!")
                logging.info(f"Pushing order to database, charging user: {username}.")
                newStock = int(cart.get('stock')) - 1
                with client.start_session() as session:
                    with session.start_transaction():
                        armor.update_one({'name':str(cart.get('name'))}, { "$set": { 'stock': newStock } })
                if discount:
                    discounted = cart.get('cost') * 0.90
                    newWallet = int(userWallet) - int(discounted)
                    price = discounted
                else:
                    newWallet = int(userWallet) - int(cart.get('cost'))
                    price = cart.get('cost')
                newOrder = {'User':str(user.get('Username')), 'Spent':int(price), 'Bought':str(cart.get('name')), 'Category':'Armor'}
                with client.start_session() as session:
                    with session.start_transaction():
                        orders.insert_one(newOrder)
                with client.start_session() as session:
                    with session.start_transaction():
                        users.update_one({'Username':str(user.get('Username'))}, { "$set": { 'Wallet': newWallet}})
                userWallet = newWallet
                UserName = user.get('Username')
                user = users.find_one({'Username':str(UserName)})
                quit = False
                input()
