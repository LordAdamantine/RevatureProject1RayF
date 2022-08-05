import re
import logging
from pymongo import MongoClient
import os
from conversion_kit import conversion
clear = lambda: os.system('cls')        # Noticed ones like this can just be put outside to give every module inside access to these easy actions.

'''
Administrate orders and issue refunds.
'''

def orders_administration(users, orders, client):
    while True:
        clear()
        try:
            menu_option = str(input("\n\n\t\tOrders Administrator Actions:\n\tView Orders\n\tView Accounts\n\tRefund Order\n\tQuit\n\t"))
            menu_option = menu_option.lower()
        except ValueError as ve:
            print("Invalid input, please try again.")
            logging.error("Invalid admin menu input, trying again...")

        if "ord" in menu_option:
            clear()
            order_history = orders.find().sort('Username')
            print("Order History")
            for elem in order_history:      
                if elem != None:
                    user_name = str(elem.get('User'))
                    value = conversion(elem.get('Spent'))
                    category = str(elem.get('Category'))
                    item_name = str(elem.get('Bought'))
                    print("User: " + f"{user_name:20}", end=" | ")
                    print("Amount Spent: " + f"{value:>15}", end=" | ")
                    print("Item Bought: " + f"{item_name:40}", end=" | ")
                    print("Category: " + f"{category:>10}", end=" | \n")
            input("Press any key to continue.")
        elif "refun" in menu_option:
            clear()
            print("Refunding Order.")
            refund(users, orders, client)
        elif "acc" in menu_option:
            clear()
            accounts_print(users)
        elif "qui" in menu_option:
            clear()
            break

def accounts_print(users):      # copied from another module, easier to just pull the method out.
    user_list = users.find({}, {'First Name':1,'Username':1, 'Status':1, 'Wallet':1, '_id':0}).sort('Status', -1)
    
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

def refund(users, orders, client):
    while True:
        clear()
        try:
            uname = str(input("\n\n\t\tPlease enter username to receive a refund.\n\t"))
        except ValueError as ve:
            print("Invalid input, please try again.")
            logging.error("Invalid refund, trying again...")
        existing = users.find_one({'Username':str(uname)})
        if existing == None:        # Makes sure they're using an existing login.
            print("Username not detected, please try again.")
            logging.error("Username not found, trying again...")
            continue

        order_history = orders.find({'User': f'{uname}'}).sort('name')

        for elem in order_history:      # Print just that user's orders for easy reference.
            user_name = elem.get('User')
            value = conversion(elem.get('Spent'))
            category = elem.get('Category')
            item_name = elem.get('Bought')
            print("User: " + f"{user_name:20}", end=" | ")
            print("Amount Spent: " + f"{value:>15}", end=" | ")
            print("Item Bought: " + f"{item_name:40}", end=" | ")
            print("Category: " + f"{category:>10}", end=" | \n")

        while True:
            try:
                menu_option = str(input("\n\tWhat item will be refunded?\n\t"))
            except ValueError as ve:
                print("Invalid input, please try again.")
                logging.error("Invalid refund input, trying again...")
            refunded = orders.find_one({'Bought': menu_option, 'User':uname})
            # for elem in refunded:
            #     print(elem)
            # input()
            # break
            if refunded != None:        # These blocks I think were causing weird None issues at the ends of blocks, pulled them to keep things simple and functional.
                # user_name = elem.get('User')
                # value = conversion(elem.get('Spent'))
                # category = elem.get('Category')
                # item_name = elem.get('Bought')
                # print("User: " + f"{user_name:20}", end=" | ")
                # print("Amount Spent: " + f"{value:>15}", end=" | ")
                # print("Item Bought: " + f"{item_name:40}", end=" | ")
                # print("Category: " + f"{category:>10}", end=" | \n")
                # input("Press enter key to initiate refund.")
                print("Processing. .. ...")
                oldWallet = users.find_one({'Username':uname})
                oldWallet = oldWallet.get('Wallet')
                refund_value = refunded.get('Spent')
                newWallet = oldWallet + refund_value
                logging.info(f"{uname} has been refunded their {menu_option} for {refund_value}.")
                with client.start_session() as session:
                    with session.start_transaction():
                        users.update_one({'Username':str(uname)}, { "$set": { 'Wallet': newWallet}})
                with client.start_session() as session:
                    with session.start_transaction():
                        orders.delete_one({'Bought': menu_option})
                print("Item refunded.")
                input("Press enter key to continue.")
                return orders
            else:
                print("Refund not found, please try again.")
                logging.error("Refund not found, trying again...")

