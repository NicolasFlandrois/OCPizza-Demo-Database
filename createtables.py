#!/usr/bin/python3.7
# UTF8
# Date: Tue 23 Jul 2019 15:45:15 CEST
# Author: Nicolas Flandrois

from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey, Float
from sqlalchemy.types import DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from connection import engine

from models import Pizza, Ingredients, Recipe, Stock, Payement_status, Order_status, Client, Vat, Orders

def createtables(name):
    """Create tables in OC Pizza DB"""
    Base = declarative_base()
    engin = engine(name)
    metadata = MetaData(bind=engin)

    Vat(Base)
    Payement_status(Base)
    Order_status(Base)
    Ingredients(Base)
    Client(Base)
    Pizza(Base)
    Recipe(Base)
    Stock(Base)
    Orders(Base)

    # vat = Table(
    #     'vat', metadata,
    #     Column('id', Integer, primary_key=True),
    #     Column('rate', Float(decimal_return_scale=4))
    #     )

    # payement_status = Table(
    #     'payement_status', metadata,
    #     Column('id', Integer, primary_key=True),
    #     Column('status', String(20))
    #     )

    # order_status = Table(
    #     'order_status', metadata,
    #     Column('id', Integer, primary_key=True),
    #     Column('status', String(20))
    #     )

    # client = Table(
    #     'client', metadata,
    #     Column('id', Integer, primary_key=True),
    #     Column('family_name', String(20), nullable=False),
    #     Column('first_name', String(20), nullable=False),
    #     Column('email', String(50), nullable=False),
    #     Column('phone', String(10), nullable=False),
    #     Column('address1', String(100), nullable=False),
    #     Column('address2', String(100)),
    #     Column('address3', String(100)),
    #     Column('invoice_address', String(100), nullable=False)
    #     )

    # pizza = Table(
    #     'pizza', metadata,
    #     Column('id', Integer, primary_key=True),
    #     Column('name', String(50)),
    #     Column('price_ht', Float(4, decimal_return_scale=2)),
    #     Column('vat', Integer, ForeignKey('vat.id'))
    #     )

    # ingredient = Table(
    #     'ingredient', metadata,
    #     Column('id', Integer, primary_key=True),
    #     Column('name', String(50), nullable=False),
    #     # Delivery Unit
    #     Column('delivunit', String(10), nullable=False),
    #     # Unit of Storage
    #     Column('storunit', String(10), nullable=False),
    #     # Storage quantity per delivery unit
    #     Column('storqty_delivunit', Integer, nullable=False),
    #     # Unit used during production
    #     Column('produnit', String(10), nullable=False),
    #     # Quantity of unit use during production in 1 storage unit
    #     Column('prodqty_storunit', Integer, nullable=False),
    #     # Purchasing cost in Delivery units (in local currency)
    #     Column('cost', Float(4, decimal_return_scale=2))
    #     )

    # recipe = Table(
    #     'recipe', metadata,
    #     Column('id', Integer, primary_key=True),
    #     Column('pizza', Integer, ForeignKey('pizza.id'), nullable=False),
    #     Column('ingredient', Integer, ForeignKey('ingredient.id'),
    #         nullable=False),
    #     Column('quantity', Float(4, decimal_return_scale=2))
    #     )

    # stock = Table(
    #     'stock', metadata,
    #     Column('id', Integer, primary_key=True),
    #     Column('ingredient', Integer, ForeignKey('ingredient.id'),
    #         nullable=False),
    #     Column('quantity', Integer)
    #     )

    # order = Table(
    #     'order', metadata,
    #     Column('id', Integer, primary_key=True),
    #     Column('date', DateTime),
    #     Column('client', Integer, ForeignKey('client.id')),
    #     Column('pizza', Integer, ForeignKey('pizza.id')),  # What if ordered for more than 1 product?
    #     Column('order_status', Integer, ForeignKey('order_status.id')),
    #     Column('payment_status', Integer, ForeignKey('payement_status.id'))
    #     )   
    
    # Creat all tables
    Base.metadata.create_all(engin)