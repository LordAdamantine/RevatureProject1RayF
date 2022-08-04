from conversion_kit import conversion
import re
import logging
import os
clear = lambda: os.system('cls')

# Simplest of the purchase order modules due to minimal details about products.

def purchase_gear(gear, orders, user, users, discount, client, userWallet):
    logging.info("Entered gear purchase module.")
    while True:
        purchasing = False
        clear()
        try:
            menu_option = str(input(f"\n\tAvailable Funds: {conversion(userWallet)}\n\tSort by: Adventuring Gear\n\tName\n\tCost\n\tWeight\n\tPurchase\n\tQuit\n\t"))
            menu_option = menu_option.lower()
        except ValueError as ve:
            print("Invalid input, please try again.")
            logging.error("Invalid store menu input, trying again...")
        if "name" in menu_option:     # Search by name function
            while True:
                gear_test = None
                menu_option = str(input(f"\n\tInput search terms, purchase, or quit\n\t"))
                menu_option = menu_option.lower()
                printing = False
                purchasing = False

                gear_test = gear.find({'name': {'$regex': menu_option, '$options': 'i'}}).sort('name')

                if type(gear_test) == None:
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
                    print("\n" + "Gear Stock - Search")
                    for elem in gear_test:
                        if int(elem.get('stock')) != 0:
                            item_name = str(elem.get('name'))
                            item_price = conversion(elem.get('cost'))
                            item_weight = str(elem.get('weight'))
                            item_count = str(elem.get('stock'))
                            print("Item: " + f"{item_name:40}", end=" | ")
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
                    gear_test = gear.find({}).sort('cost', 1)
                    printing = True
                elif "up" in menu_option:
                    gear_test = gear.find({}).sort('cost', 1)
                    printing = True
                elif "des" in menu_option:
                    gear_test = gear.find({}).sort('cost', -1)
                    printing = True
                elif "down" in menu_option:
                    gear_test = gear.find({}).sort('cost', -1)
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
                    print("\n" + "Gear Stock - Price")
                    for elem in gear_test:
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
                    gear_test = gear.find({}).sort('weight', 1)
                    printing = True
                elif "up" in menu_option:
                    gear_test = gear.find({}).sort('weight', 1)
                    printing = True
                elif "des" in menu_option:
                    gear_test = gear.find({}).sort('weight', -1)
                    printing = True
                elif "down" in menu_option:
                    gear_test = gear.find({}).sort('weight', -1)
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
                    print("\n" + "Gear Stock - Price")
                    for elem in gear_test:
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

                cart = gear.find_one({'name': {'$regex': f'{purchase_name}', '$options': 'i'}})

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
                item_price = conversion(cart.get('cost'))
                item_weight = str(cart.get('weight'))
                item_count = str(cart.get('stock'))
                print("Item: " + f"{item_name:40}", end=" | ")
                print("Price: " + f"{item_price:>15}", end=" | ")
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
                oldWallet = userWallet
                username = user.get('Username')
                ware = cart.get('name')
                price = cart.get('cost')
                print(f"Thank you for purchasing a {ware}! Enjoy your purchase!")
                logging.info(f"Pushing order to database, charging user: {username}.")
                newOrder = {'User':str(username), 'Spent':int(price), 'Bought':str(ware), 'Category':'Gear'}
                with client.start_session() as session:
                    with session.start_transaction():
                        orders.insert_one(newOrder)
                newStock = int(cart.get('stock')) - 1
                with client.start_session() as session:
                    with session.start_transaction():
                        gear.update_one({'name':str(ware)}, { "$set": { 'stock': newStock } })
                if discount:
                    price *= 0.90
                newWallet = int(oldWallet) - int(price)
                with client.start_session() as session:
                    with session.start_transaction():
                        users.update_one({'Username':str(username)}, { "$set": { 'Wallet': newWallet}})
                UserName = user.get('Username')
                user = users.find_one({'Username':str(UserName)})
                userWallet = newWallet
                input()
