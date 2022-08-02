import os
import logging
from pymongo import MongoClient
import re

def purchase(armor, weapons, gear, misc, orders, user):
    clear = lambda: os.system('cls')

    



def conversion(amount):     # Converts cost values into 5E currencies for aesthetic.
    # Initialize base variables for comparison.

    base_value = amount
    new_value = base_value
    coppers = 0
    silvers = 0
    golds = 0
    plats = 0
    value = ""

    while True:     # Cycles amount through, tabulating amount of each coin before appending them to a string at the end.
        if new_value < 10:
            coppers = new_value
            #print("Copper test")
            break
        if new_value > 9:
            if new_value > 99:
                if new_value > 999:
                    new_value -= 1000
                    plats += 1
                    #print("Plat test")
                    continue
                new_value -= 100
                golds += 1
                #print("Gold test")
                continue
            new_value -= 10
            silvers += 1
            #print("Silver test")
            continue
    
    if plats > 0:
        value += (f"{plats} PP ")
    if golds > 0:
        value += (f"{golds} GP ")
    if silvers > 0:
        value += (f"{silvers} SP ")
    if coppers > 0:
        value += (f"{coppers} CP")

    return value
    
        