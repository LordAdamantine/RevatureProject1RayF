import re
import logging
from pymongo import MongoClient
import os
from login_procedures import login
from transactions import purchase, conversion

def main():

    client = MongoClient()
    db = client.get_database("Project1")

    armor = db.armor
    weapons = db.weapons
    gear = db.gear
    misc = db.misc
    users = db.users
    orders = db.orders

    # weapons_test = weapons.find({}, {'name':1, 'cost':1, 'stock':1, '_id':0}).sort('cost', -1)
    # print("\n" + "Weapons Stock - Price")
    # for elem in weapons_test:
    #     if int(elem.get('stock')) != 0:
    #         item_price = conversion(elem.get('cost'))
    #         item_name = str(elem.get('name'))
    #         item_count = str(elem.get('stock'))
    #         print("Price: " + f"{item_price:>15}", end=" | ")
    #         print("Item: " + f"{item_name:40}", end=" | ")
    #         print("Count: " + f"{item_count:>5}", end=" | \n")

    ## Conversion module test cases
    # print(conversion(1))        # 1 CP
    # print(conversion(50))       # 5 SP
    # print(conversion(400))      # 4 GP
    # print(conversion(3000))     # 3 PP
    # print(conversion(321))      # 3 GP 2 SP 1 CP
    # print(conversion(1098))     # 1 PP 9 SP 8 CP

    pass

if __name__ == "__main__":
    main()





# if printing:
#     print("\n" + "Weapons Stock - Search")
#     for elem in weapons_test:
#         if int(elem.get('stock')) != 0:
#             item_name = str(elem.get('name'))
#             item_class = str(elem.get('classification'))
#             item_damage = str(elem.get('damage'))
#             item_price = conversion(elem.get('cost'))
#             item_weight = str(elem.get('weight'))
#             item_count = str(elem.get('stock'))
#             print("Item: " + f"{item_name:40}", end=" | ")
#             print("Class: " + f"{item_class:20}", end=" | ")
#             print("Damage: " + f"{item_damage:20}", end=" | ")
#             print("Price: " + f"{item_price:>15}", end=" | ")
#             print("Weight: " + f"{item_weight:>5} lbs", end=" | ")
#             print("Count: " + f"{item_count:>5}", end=" | \n")