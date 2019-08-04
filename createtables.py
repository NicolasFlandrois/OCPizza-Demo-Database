#!/usr/bin/python3.7
# UTF8
# Date: Tue 23 Jul 2019 15:45:15 CEST
# Author: Nicolas Flandrois

from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey
from sqlalchemy import Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from connection import engine


def createtables(name):
    """Create tables in OC Pizza DB"""
    Base = declarative_base()
    engin = engine(name)
    metadata = MetaData(bind=engin)

    vat = Table(
        'vat', metadata,
        Column('id', Integer, primary_key=True),
        Column('rate', Float(decimal_return_scale=4))
        )

    payment_status = Table(
        'payment_status', metadata,
        Column('id', Integer, primary_key=True),
        Column('status', String(50))
        )

    order_status = Table(
        'order_status', metadata,
        Column('id', Integer, primary_key=True),
        Column('status', String(50))
        )

    client = Table(
        'client', metadata,
        Column('id', Integer, primary_key=True),
        Column('family_name', String(20), nullable=False),
        Column('first_name', String(20), nullable=False),
        Column('email', String(50), nullable=False),
        Column('phone', String(10), nullable=False),
        )

    address = Table(
        'address', metadata,
        Column('id', Integer, primary_key=True),
        Column('client', Integer, ForeignKey('client.id'), nullable=False),
        Column('address', String(500), nullable=False),
        Column('invoice', Boolean, nullable=False)
        )

    pizza = Table(
        'pizza', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50)),
        Column('price', Float(4, decimal_return_scale=2)),
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

    recipe_ingredient = Table(
        'recipe_ingredient', metadata,
        Column('id', Integer, primary_key=True),
        Column('pizza', Integer, ForeignKey('pizza.id'), nullable=False),
        Column('ingredient', Integer, ForeignKey('ingredient.id'),
            nullable=False),
        Column('quantity', Float(4, decimal_return_scale=2))
        )

    restaurant = Table(
        'restaurant', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50))
        )

    stock = Table(
        'stock', metadata,
        Column('id', Integer, primary_key=True),
        Column('stock_loc', Integer, ForeignKey('restaurant.id'),
            nullable=False),        
        Column('ingredient', Integer, ForeignKey('ingredient.id'),
            nullable=False),
        Column('quantity', Integer)
        )

    order_cd = Table(
        'order_cd', metadata,
        Column('id', Integer, primary_key=True),
        Column('date', DateTime),
        Column('client', Integer, ForeignKey('client.id'), nullable=False),
        Column('order_status', Integer, ForeignKey('order_status.id'),
            nullable=False),
        Column('payment_status', Integer, ForeignKey('payment_status.id'),
            nullable=False)
        )

    pizza_ordered = Table(
        'pizza_ordered', metadata,
        Column('id', Integer, primary_key=True),
        Column('order_cd', Integer, ForeignKey('order_cd.id'), nullable=False),
        Column('pizza', Integer, ForeignKey('pizza.id'), nullable=False)
        )
    
    # Creat all tables
    metadata.create_all(engin)