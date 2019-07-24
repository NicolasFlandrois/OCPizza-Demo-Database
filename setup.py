#!/usr/bin/python3.7
# UTF8
# Date: Thu 11 Jul 2019 16:06:15 CEST
# Author: Nicolas Flandrois

import json

from sqlalchemy.orm import sessionmaker, query

from connection import connect, createdb, checkdb
from datetime import datetime


from createtables import createtables



startTime = datetime.now()
print("Setup in progress. Please wait.")

if checkdb('ocpizza') == True:
    createdb('ocpizza')
    session = connect('ocpizza')

    createtables('ocpizza')

    

    # Then populate the DB
    # 5/ Create a configured "Session" class
    # Session = sessionmaker(bind=engine) # Create and factor this in Connect function
    # 6/ Create a Session
    # session = Session() # Create and factor this in Connect function

    # 8/ Mesuring time to setup, and informing user, the database was created
    # successfully.
    finishTime = datetime.now()
    timeDetla = finishTime-startTime

    print("Setup is finished. Your database is now available.")
    print("The process was completed in : " + str(
        timeDetla.total_seconds()) + "s.")

# If the database already exist, then inform the user about it.
else:
    print("Your database already exists.")
