#!/usr/bin/python3.7
# UTF8
# Date: Thu 11 Jul 2019 16:06:15 CEST
# Author: Nicolas Flandrois

import json

from sqlalchemy.orm import sessionmaker, query

from connection import connect, createdb, checkdb
from datetime import datetime


# from createtables import createtables

from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey, Float
from sqlalchemy.types import DateTime
# from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from connection import connect, engine

startTime = datetime.now()
print("Setup in progress. Please wait.")

if checkdb('ocpizza') == True:
    createdb('ocpizza')
    session = connect('ocpizza')

    # createtables('ocpizza')

    Base = declarative_base()
    engine = engine('ocpizza')
    metadata = MetaData(bind=engine)

    vat = Table(
        'vat', metadata,
        Column('id', Integer, primary_key=True),
        Column('rate', Float(decimal_return_scale=4))
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

    pizza = Table(
        'pizza', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50)),
        Column('price_ht', Float(4, decimal_return_scale=2)),
        Column('vat', Integer, ForeignKey('vat.id'))
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
        Column('storqty_delivunit', Integer, nullable=False),
        # Unit used during production
        Column('produnit', String(10), nullable=False),
        # Quantity of unit use during production in 1 storage unit
        Column('prodqty_storunit', Integer, nullable=False),
        # Purchasing cost in Delivery units (in local currency)
        Column('cost', Float(4, decimal_return_scale=2))
        )

    recipe = Table(
        'recipe', metadata,
        Column('id', Integer, primary_key=True),
        Column('pizza', Integer, ForeignKey('pizza.id'), nullable=False),
        Column('ingredient', Integer, ForeignKey('ingredient.id'),
            nullable=False),
        Column('quantity', Float(4, decimal_return_scale=2))
        )

    stock = Table(
        'stock', metadata,
        Column('id', Integer, primary_key=True),
        Column('ingredient', Integer, ForeignKey('ingredient.id'),
            nullable=False),
        Column('quantity', Integer)
        )

    order = Table(
        'order', metadata,
        Column('id', Integer, primary_key=True),
        Column('date', DateTime),
        Column('client', Integer, ForeignKey('client.id')),
        Column('pizza', Integer, ForeignKey('pizza.id')),  # What if ordered for more than 1 product?
        Column('order_status', Integer, ForeignKey('order_status.id')),
        Column('payment_status', Integer, ForeignKey('payement_status.id'))
        )   
    
    # Creat all tables
    metadata.create_all(engine)

    # Then populate the DB
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
