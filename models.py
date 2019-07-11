#!/usr/bin/python3.7
# UTF8
# Date: Thu 11 Jul 2019 16:05:53 CEST
# Author: Nicolas Flandrois

from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from connection import connect

session = connect()

Base = declarative_base()


class Pizza(Base):
    """docstring for Pizza"""
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    priceht = Column(Float(scale=2))
    

class Ingredients(Base):
    """docstring for Ingredient"""
    __tablename__ = "ingredient"
    id = Column(Integer, primary_key=True)
    ingredient = Column(String(50), nullable=False)
    # Delivery Unit
    delivunit = Column(String(10), nullable=False)
    # delivqty  # Quantity of unit in a delivery
    # Unit of Storage
    storunit = Column(String(10), nullable=False)
    # Storage quantity per delivery unit
    storqty_delivunit = Column(Integer(10), nullable=False)
    # Unit used during production
    produnit = Column(String(10), nullable=False)
    # quantity of unit use during production in 1 storage unit
    prodqty_storunit = Column(Integer(10), nullable=False)

class Recipe(Base):
    """docstring for Recipe"""
    __tablename__ = "recipe"
    id = Column(Integer, primary_key=True)
    pizza = Column(Integer, ForeignKey('pizza.id'), nullable=False)
    ingredient = Column(Integer, ForeignKey('ingredient.id'), nullable=False)

# class Units(Base):
#     """Conversion Table Units Quantity Units Delivered/Stored/Used"""
#     __tablename__ = "units"
#     id = Column(Integer, primary_key=True)

class Stock(Base):
    """docstring for Stock"""
    __tablename__ = "stock"
    id = Column(Integer, primary_key=True)
    product = Column(Integer, ForeignKey('ingredient.id'), nullable=False)
    quantity = Column(Integer(10))

class Payementstatus(Base):
    """docstring for PayementStatus"""
    __tablename__ = "payementstatus"
    id = Column(Integer, primary_key=True)
    status = Column(String(20))

class Orderstatus(Base):
    """docstring for Order Status"""
    __tablename__ = "orderstatus"
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
    invoiceaddress = Column(String(100), nullable=False)


class Vat(Base):
    """docstring for Vat"""
    __tablename__ = "Vat"
    id = Column(Integer, primary_key=True)
    vat = Column(Float(scale=4))

class Orders(Base):
    """docstring for Orders"""
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True)
    date = Column(Datetime()) # Using SQLALCHEMY Date or Datetime?
    client = Column(Integer, ForeignKey('client.id'))
    pizza = Column(Integer, ForeignKey('pizza.id'))  # What if ordered for more than 1 product?
    vat = Column(Integer, ForeignKey('vat.id'))
    totalpriceht = Column(Integer, ForeignKey('pizza.price'))
    orderstatus = Column(Integer, ForeignKey('orderstatus.id'))
    paymentstatus = Column(Integer, ForeignKey('payementstatus.id'))
