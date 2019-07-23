#!/usr/bin/python3.7
# UTF8
# Date: Thu 11 Jul 2019 16:05:53 CEST
# Author: Nicolas Flandrois

from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import DateTime
from connection import connect

session = connect('ocpizza')

Base = declarative_base()


class Pizza(Base):
    """docstring for Pizza"""
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price_ht = Column(Float(4, decimal_return_scale=2))  # In local currency
    vat = Column(Integer, ForeignKey('vat.id'))
    

class Ingredients(Base):
    """docstring for Ingredient"""
    __tablename__ = "ingredient"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    # Delivery Unit
    delivunit = Column(String(10), nullable=False)
    # Unit of Storage
    storunit = Column(String(10), nullable=False)
    # Storage quantity per delivery unit
    storqty_delivunit = Column(Integer, nullable=False)
    # Unit used during production
    produnit = Column(String(10), nullable=False)
    # Quantity of unit use during production in 1 storage unit
    prodqty_storunit = Column(Integer, nullable=False)
    # Purchasing cost in Delivery units (in local currency)
    cost = Column(Float(4, decimal_return_scale=2))

class Recipe(Base):
    """docstring for Recipe"""
    __tablename__ = "recipe"
    id = Column(Integer, primary_key=True)
    pizza = Column(Integer, ForeignKey('pizza.id'), nullable=False)
    ingredient = Column(Integer, ForeignKey('ingredient.id'), nullable=False)
    quantity = Column(Float(4, decimal_return_scale=2))

class Stock(Base):
    """docstring for Stock"""
    __tablename__ = "stock"
    id = Column(Integer, primary_key=True)
    ingredient = Column(Integer, ForeignKey('ingredient.id'), nullable=False)
    quantity = Column(Integer)

class Payement_status(Base):
    """docstring for PayementStatus"""
    __tablename__ = "payement_status"
    id = Column(Integer, primary_key=True)
    status = Column(String(20))

class Order_status(Base):
    """docstring for Order Status"""
    __tablename__ = "order_status"
    id = Column(Integer, primary_key=True)
    status = Column(String(20))

class Client(Base):
    """docstring for Client"""
    __tablename__ = "Client"
    id = Column(Integer, primary_key=True)
    family_name = Column(String(20), nullable=False)
    first_name = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(10), nullable=False)
    address1 = Column(String(100), nullable=False)
    address2 = Column(String(100))
    address3 = Column(String(100))
    invoice_address = Column(String(100), nullable=False)


class Vat(Base):
    """docstring for Vat"""
    __tablename__ = "Vat"
    id = Column(Integer, primary_key=True)
    rate = Column(Float(decimal_return_scale=4))

class Orders(Base):
    """docstring for Orders"""
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    client = Column(Integer, ForeignKey('client.id'))
    pizza = Column(Integer, ForeignKey('pizza.id'))  # What if ordered for more than 1 product?
    order_status = Column(Integer, ForeignKey('order_status.id'))
    payment_status = Column(Integer, ForeignKey('payement_status.id'))
