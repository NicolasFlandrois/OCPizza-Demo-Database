#!/usr/bin/python3.7
# UTF8
# Date: Thu 11 Jul 2019 16:06:15 CEST
# Author: Nicolas Flandrois

import json

from sqlalchemy import Column, Integer, String, Boolean, Table
from sqlalchemy import create_engine, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, query
from sqlalchemy.ext.declarative import declarative_base

from connection import connect, createdb
from datetime import datetime

from models import Pizza, Ingredients, Recipe, Stock, Payementstatus
from models import Orderstatus, Client, Vat, Orders


startTime = datetime.now()
print("Setup in progress. Please wait.")

if createdb('ocpizza'):

    # 2/connect to database
    Base = declarative_base()    
    engine = connect('ocpizza')

    # Create tables in DB
    metadata = MetaData(engine) # Create and factor this in Connect function

    pizza = Table(
        'pizza', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50)),
        Column('price_ht', Float(4, scale=2))
        )

    ingredient = Table(
        'ingredient', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50), nullable=False),
        # Delivery Unit
        Column('delivunit', String(10), nullable=False),
        # Unit of Storage
        Column('storunit', String(10), nullable=False),
        # Storage quantity per delivery unit
        Column('storqty_delivunit', Integer(4), nullable=False),
        # Unit used during production
        Column('produnit', String(10), nullable=False),
        # Quantity of unit use during production in 1 storage unit
        Column('prodqty_storunit', Integer(4), nullable=False),
        # Purchasing cost in Delivery units (in local currency)
        Column('cost', Float(4, scale=2))
        )

    recipe = Table(
        'recipe', metadata,
        Column('id', Integer, primary_key=True),
        Column('pizza', Integer, ForeignKey('pizza.id'), nullable=False),
        Column('ingredient', Integer, ForeignKey('ingredient.id'), nullable=False),
        Column('quantity', Float(4, scale=2))
        )

    stock = Table(
        'stock', metadata,
        Column('id', Integer, primary_key=True),
        Column('ingredient', Integer, ForeignKey('ingredient.id'), nullable=False),
        Column('quantity', Integer(10))
        )

    payement_status = Table(
        'payement_status', metadata,
        Column('id', Integer, primary_key=True),
        Column('status', String(20))
        )

    order_status = Table(
        'order_status', metadata,
        Column('id', Integer, primary_key=True),
        Column('status', String(20))
        )

    client = Table(
        'client', metadata,
        Column('id', Integer, primary_key=True),
        Column('family_name', String(20), nullable=False),
        Column('first_name', String(20), nullable=False),
        Column('email', String(50), nullable=False),
        Column('phone', String(10), nullable=False),
        Column('address1', String(100), nullable=False),
        Column('address2', String(100)),
        Column('address3', String(100)),
        Column('invoice_address', String(100), nullable=False)
        )

    vat = Table(
        'vat', metadata,
        Column('id', Integer, primary_key=True),
        Column('rate', Float(scale=4))
        )

    order = Table(
        'vat', metadata,
        Column('id', Integer, primary_key=True),
        Column('date', Datetime()),
        Column('client', Integer, ForeignKey('client.id')),
        Column('pizza', Integer, ForeignKey('pizza.id')),  # What if ordered for more than 1 product?
        Column('vat', Integer, ForeignKey('vat.id')),
        Column('total_price_ht', Integer, ForeignKey('pizza.price')),   # In local currency
        Column('order_status', Integer, ForeignKey('order_status.id')),
        Column('payment_status', Integer, ForeignKey('payement_status.id'))
        )

    # Creat all tables
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
