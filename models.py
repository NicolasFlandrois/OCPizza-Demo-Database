#!/usr/bin/python3.7
# UTF8
# Date: Thu 11 Jul 2019 16:05:53 CEST
# Author: Nicolas Flandrois

from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy import DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from connection import connect

session = connect('ocpizza')

Base = declarative_base()


class Pizza(Base):
    """docstring for Pizza"""
    __tablename__ = "pizza"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Float(4, decimal_return_scale=2))  # In local currency
    vat = Column(Integer, ForeignKey('vat.id'))


class Ingredient(Base):
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


class Recipe_ingredient(Base):
    """docstring for Recipe"""
    __tablename__ = "recipe_ingredient"
    id = Column(Integer, primary_key=True)
    pizza = Column(Integer, ForeignKey('pizza.id'), nullable=False)
    ingredient = Column(Integer, ForeignKey('ingredient.id'), nullable=False)
    quantity = Column(Float(4, decimal_return_scale=2))


class Restaurant(Base):
    """docstring for Restaurant"""
    __tablename__ = "restaurant"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Stock(Base):
    """docstring for Stock"""
    __tablename__ = "stock"
    id = Column(Integer, primary_key=True)
    stock_loc = Column(Integer, ForeignKey('restaurant.id'), nullable=False)
    ingredient = Column(Integer, ForeignKey('ingredient.id'), nullable=False)
    quantity = Column(Integer)


class Payment_status(Base):
    """docstring for PaymentStatus"""
    __tablename__ = "payment_status"
    id = Column(Integer, primary_key=True)
    status = Column(String(50))


class Order_status(Base):
    """docstring for Order Status"""
    __tablename__ = "order_status"
    id = Column(Integer, primary_key=True)
    status = Column(String(20))


class Client(Base):
    """docstring for Client"""
    __tablename__ = "client"
    id = Column(Integer, primary_key=True)
    family_name = Column(String(20), nullable=False)
    first_name = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(10), nullable=False)


class Address(Base):
    """docstring for Adresses"""
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    client = Column(Integer, ForeignKey('client.id'), nullable=False)
    address = Column(String(500), nullable=False)
    invoice = Column(Boolean, nullable=False)


class Vat(Base):
    """docstring for Vat"""
    __tablename__ = "vat"
    id = Column(Integer, primary_key=True)
    rate = Column(Float(decimal_return_scale=4))


class Order(Base):
    """docstring for Orders"""
    __tablename__ = "order_cd"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    client = Column(Integer, ForeignKey('client.id'), nullable=False)
    order_status = Column(Integer, ForeignKey('order_status.id'),
                          nullable=False)
    payment_status = Column(Integer, ForeignKey('payment_status.id'),
                            nullable=False)


class Pizza_ordered(Base):
    """docstring for Pizza_ordered"""
    __tablename__ = "pizza_ordered"
    id = Column(Integer, primary_key=True)
    order_cd = Column(Integer, ForeignKey('order_cd.id'), nullable=False)
    pizza = Column(Integer, ForeignKey('pizza.id'), nullable=False)
