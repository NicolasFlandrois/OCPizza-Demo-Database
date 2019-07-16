#!/usr/bin/python3.7
# UTF8
# Date: Thu 11 Jul 2019 16:06:15 CEST
# Author: Nicolas Flandrois

import json

from sqlalchemy.orm import sessionmaker, query

from connection import connect, createdb, checkdb
from datetime import datetime

from models import Pizza, Ingredients, Recipe, Stock, Payement_status
from models import Order_status, Client, Vat, Orders

from createtables import createtables


startTime = datetime.now()
print("Setup in progress. Please wait.")

if checkdb('ocpizza') == True:
    createdb('ocpizza')
    engine = connect('ocpizza')

    createtables('ocpizza')

    # 4/ Fill in info to database according to tables, with seed data.
    # 4.1/ Fill Category table with category data.
    # categories = ("pâte à tartiner", "confiture", "sirop")
    # for i in categories:
    #     engine.execute(category.insert(), name=i)
    
    # import all raw data from json Files HERE

    # 4.3/ Parsing and inserting all data.
    # for index, (
    #   ean, name, category, substitute, substituted) in enumerate(prods):
    #     engine.execute(product.insert(), ean=ean, name=name,
    #                    category=category, substituted=substituted)

    # 5/ Create a configured "Session" class
    # Session = sessionmaker(bind=engine) # Create and factor this in Connect function
    # 6/ Create a Session
    # session = Session() # Create and factor this in Connect function

    # 8/ Mesuring time to setup, and informing user, the database was created
    # successfully.
    finishTime = datetime.now()
    timeDetla = finishTime-startTime

    print("Setup is finished. Your database is available now.")
    print("The process was completed in : " + str(
        timeDetla.total_seconds()) + "s.")

# If the database already exist, then inform the user about it.
else:
    print("Your database already exists.")
