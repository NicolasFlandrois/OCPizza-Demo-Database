#!/usr/bin/python3.7
# UTF8
# Date: 
# Author: Nicolas Flandrois

from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from connection import connect

session = connect()

Base = declarative_base()


class Pizza(Base):
    """docstring for Pizza"""
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Float(scale=2))
    

class Ingredients(Base):
    """docstring for Ingredient"""
    __tablename__ = "ingredient"
    id = Column(Integer, primary_key=True)
    ingredient = Column(String(50))

class Recipe(Base):
    """docstring for Recipe"""
    __tablename__ = "recipe"
    id = Column(Integer, primary_key=True)
    pizza = Column(Integer, ForeignKey('pizza.id'))
    ingredient = Column(Integer, ForeignKey('ingredient.id'))

class Units(Base):
    """docstring for Units Quantity Units Delivered/Stored/Used"""
    __tablename__ = "units"
    id = Column(Integer, primary_key=True)

class Stock(Base):
    """docstring for Stock"""
    __tablename__ = "stock"
    id = Column(Integer, primary_key=True)

class Payementstatus(Base):
    """docstring for PayementStatus"""
    __tablename__ = "payementstatus"
    id = Column(Integer, primary_key=True)

class Orderstatus(Base):
    """docstring for Order Status"""
    __tablename__ = "orderstatus"
    id = Column(Integer, primary_key=True)

class Client(Base):
    """docstring for Client"""
    __tablename__ = "Client"
    id = Column(Integer, primary_key=True)

class Vat(Base):
    """docstring for Vat"""
    __tablename__ = "Vat"
    id = Column(Integer, primary_key=True)

class Orders(Base):
    """docstring for Orders"""
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True)
    date = Column(Datetime()) # Using SQLALCHEMY Date or Datetime?
    client = Column(Integer, ForeignKey('client.id'))
    pizza = Column(Integer, ForeignKey('pizza.id'))
    vat = Column(Integer, ForeignKey('vat.id'))
    totalpriceht = Column(Integer, ForeignKey('pizza.price'))
    orderstatus = Column(Integer, ForeignKey('orderstatus.id'))
    paymentstatus = Column(Integer, ForeignKey('payementstatus.id'))
