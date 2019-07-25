#!/usr/bin/python3.7
# UTF8
# Date: Thu 11 Jul 2019 16:06:15 CEST
# Author: Nicolas Flandrois


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
    # Function to populate the entire DB > HERE <

    finishTime = datetime.now()
    timeDetla = finishTime-startTime

    print("Setup is finished. Your database is available now.")
    print("The process was completed in : " + str(
        timeDetla.total_seconds()) + "s.")

else:
    print("Your database already exists.")
