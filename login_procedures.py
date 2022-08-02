import os
import logging
from pymongo import MongoClient
import re

def login(users):
    clear = lambda: os.system('cls')

    while True:     # This block is simple input filtering.
        while True:
            try:
                menu_option = str(input("Login/Signup/Quit\n\t>>>\t\t"))
                menu_option = menu_option.lower()
            except ValueError as ve:
                print("Invalid input, please try again.")
                logging.error("Invalid login menu input, trying again...")
            else:
                break
        
        if menu_option == "login":
            option = 1
            break
        elif menu_option == "signup":
            option = 2
            break
        elif menu_option == "quit":
            option = 3
            break
        else:
            print("Invalid input, please try again.")
            logging.error("Options exceeded on login menu input, trying again...")

    if option == 1:     # Existing user login
        success = True
        invalid_attempts = 0
        while success:
            if invalid_attempts >2:
                input("Security error, please contact administrator.")
                return None
            while True:
                try:
                    uname = str(input("\t\tPlease enter your user name:\t\t"))
                    check = re.search("," or "@" or "!" or "#" or "$" or "%" or "&", uname)
                    existing = users.find_one({'Username':str(uname)})
                    if check != None:
                        raise ValueError
                    if existing == None:        # Makes sure they're using an existing login.
                        print("Username not detected, please try again.")
                        logging.error("Username not found, trying again...")
                        continue
                except ValueError as ve:
                    print("Warning, improper input detected.")
                    logging.error("Attempted illegal character in username, trying again...")
                    continue
                else:

                    break

            pw_attempts = 0
            pword_check = existing.get('Password')      # Preloads user password for checking, probably wouldn't be safe in an actual application but works for here.
            while True:
                if pw_attempts >2:
                    print("Sorry, let's try this again.")
                    break
                try:
                    pword = str(input("\t\tPlease enter your password:\t\t"))
                    if pword != pword_check:
                        raise ValueError
                except ValueError as ve:
                    print("Wrong password, try again.")
                    logging.error("Wrong password, trying again...")
                    pw_attempts += 1
                    continue
                else:
                    success = False
                    break
            invalid_attempts += 1.
        
        # Returns with user info loaded from successful login.
        return existing


    if option == 2:         # New user account creation.
        print("Welcome!  Let's get you set up!")

        while True:
            try:
                uname = str(input("\t\tPlease create a user name:\t\t"))
                check = re.search("," or "@" or "!" or "#" or "$" or "%" or "&", uname)
                existing = users.find_one({'Username':str(uname)})
                if check != None:
                    raise ValueError
                if existing != None:        # Prevents duplicate usernames.
                    print("Username detected, please try again.")
                    logging.error("Attempted duplicate Username, trying again...")
                    continue
            except ValueError as ve:
                print("Warning, improper input detected.")
                logging.error("Attempted illegal character in username, trying again...")
                continue
            else:
                break

        while True:     # Simple input checking for these steps.
            try:
                fname = str(input("\t\tPlease input your first name:\t\t"))
                check = re.search('[0-9]+', fname)
                if check != None:
                    raise ValueError
            except ValueError as ve:
                print("Warning, improper input detected.")
                logging.error("Attempted illegal integer in name, trying again...")
                print(check)
                continue
            else:
                break

        while True:
            try:
                lname = str(input("\t\tPlease input your first name:\t\t"))
                check = re.search('[0-9]+', lname)
                if check != None:
                    raise ValueError
            except ValueError as ve:
                print("Warning, improper input detected.")
                logging.error("Attempted illegal integer in name, trying again...")
                print(check)
                continue
            else:
                break
        
        success = True
        while success:
            while True:
                try:
                    pword = str(input("\t\tPlease enter a password:\t\t"))
                    if check != None:
                        raise ValueError
                    if len(pword) < 8:
                        print("Password must have at least 8 characters.")
                        continue
                except ValueError as ve:
                    print("Warning, improper input.")
                    logging.error("Attempted illegal special characters in name, trying again...")
                    continue
                else:
                    break
            
            pw_attempts = 0
            while True:
                if pw_attempts >3:
                    print("Sorry, let's try this again.")
                    break
                try:
                    pword_check = str(input("\t\tPlease re-enter password:\t\t"))
                    if pword_check != pword:
                        raise ValueError
                except ValueError as ve:
                    print("Warning, improper input.")
                    logging.error("Attempted illegal special characters in name, trying again...")
                    pw_attempts += 1
                    continue
                else:
                    success = False
                    break
        
        # First instance of writing to the database to occur in the code so far.
        users.insert_one({'First Name':str(fname), 'Last Name':str(lname), 'Username':str(uname), 'Password':str(pword), 'Status':"Customer"})
        new_user = users.find_one({'Username':str(uname)})
        return new_user
        

    if option == 3:
        input("\t\tQuitting back to menu.\n")
        clear()
        return None