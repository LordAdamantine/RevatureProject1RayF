
def conversion(amount):     # Converts cost values into 5E currencies for aesthetic.
    # Initialize base variables for comparison.

    base_value = int(amount)
    new_value = base_value
    coppers = 0
    silvers = 0
    golds = 0
    plats = 0
    value = ""

    # Tried to make it detect just solid blocks of coins, but it kept causing issues, so it's gone.
    # if base_value < 10:
    #     value = f"{base_value} CP"
    #     return value
    # if (base_value % 10) == 0:
    #     if (base_value % 100) == 0:
    #         if (base_value % 1000) == 0:
    #             new_value = int(base_value / 1000)
    #             value = f"{new_value} PP"
    #             return value
    #         new_value = int(base_value / 100)
    #         value = f"{new_value} GP"
    #         return value
    #     new_value = int(base_value / 10)
    #     value = f"{new_value} SP"
    #     return value


    while True:     # Cycles amount through, tabulating amount of each coin before appending them to a string at the end.

        if new_value < 10:
            coppers = new_value
            #print("Copper test")
            break
        if new_value > 9:
            if new_value > 99:
                if new_value > 999: #Used to handle platinum coins but decided they were too cumbersome for the interface and everyone likes gold anyway.
                    new_value -= 1000
                    golds += 10
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
    
    # if plats > 0:
    #     value += (f"{plats} PP ")
    if golds > 0:
        value += (f"{golds} GP ")
    if silvers > 0:
        value += (f"{silvers} SP ")
    if coppers > 0:
        value += (f"{coppers} CP ")

    return value
    