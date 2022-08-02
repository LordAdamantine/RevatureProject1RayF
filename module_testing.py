import re
import logging
from pymongo import MongoClient
import os
from login_procedures import login
from transactions import purchase, conversion

def main():

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