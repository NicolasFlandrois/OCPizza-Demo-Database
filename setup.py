#!/usr/bin/python3.7
# UTF8
# Date: Thu 11 Jul 2019 16:06:15 CEST
# Author: Nicolas Flandrois

import json
from sqlalchemy import Column, Integer, String, Boolean, Table
from sqlalchemy import create_engine, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, query
from sqlalchemy_utils import create_database, database_exists
from models import xxxxxxxxxxxxxxxx
from connection import connect
from datetime import datetime


startTime = datetime.now()
print("Setup in progress. Please wait.")

# 1/ create DB in mysql named: off1
with open("config.json") as f:
    config = json.load(f)

username = config["username"]
password = config["password"]
host = config["host"]
port = config["port"]

if not database_exists(f'mysql+pymysql://{username}:{password}@{host}/ocpizza'):
    create_database(f'mysql+pymysql://{username}:{password}@{host}/ocpizza')

    # 2/connect to database: off1
    Base = declarative_base()
    engine = connect()

    # 3/ Create tables in DB, named: category & product
    metadata = MetaData(engine) # Create and factor this in Connect function

    pizza = Table(
        'product', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50)),
        Column('price', Float(scale=2)),
        )

    category = Table(
        'category', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50)),
        )

    # 5/ creat all tables
    metadata.create_all(engine) # Create and factor this in Connect function

    # 4/ Fill in info to database according to tables, with seed data.
    # 4.1/ Fill Category table with category data.
    # categories = ("pâte à tartiner", "confiture", "sirop")
    # for i in categories:
    #     engine.execute(category.insert(), name=i)
    
    # import all raw data from json Files

    # 4.3/ Parsing and inserting all data.
    # for index, (
    #   ean, name, category, substitute, substituted) in enumerate(prods):
    #     engine.execute(product.insert(), ean=ean, name=name,
    #                    category=category, substituted=substituted)

    # 5/ Create a configured "Session" class
    Session = sessionmaker(bind=engine) # Create and factor this in Connect function
    # 6/ Create a Session
    session = Session() # Create and factor this in Connect function

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
