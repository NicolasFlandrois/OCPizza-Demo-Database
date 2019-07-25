#!/usr/bin/python3.7
# UTF8
# Date: Tue 23 Jul 2019 16:00:00 CEST
# Author: Nicolas Flandrois


import json
from connection import connect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
# from sqlalchemy import Index
# from sqlalchemy.orm import relationship, backref
from models import Pizza, Ingredient, Recipe, Stock, Payement_status, Order_status
from models import Client, Vat, Order, Pizza_ordered, Address

# Base = declarative_base() # Normalement ne sera pas utiliser
session = connect('ocpizza')

# 1/Read json raw data file
with open("data.json") as f:
    data = json.load(f)

# 2/store in memory relevent parsed data?

# for i in data['vat']:
#     vat = Vat(rate = i)
#     session.add(vat)  # Ok Works

# for i in data['pay_status']:
#     p_status = Payement_status(status = i)
#     session.add(p_status)  # Ok Works

# for i in data['order_status']:
#     o_status = Order_status(status = i)
#     session.add(o_status)  # Ok Works

# for i in data['ingredients']:
#     ingredient = Ingredient(name = i['name'], delivunit = i['delivunit'],
#         storunit = i['storunit'], storqty_delivunit = i['storqty_delivunit'],
#         produnit = i['produnit'], prodqty_storunit = i['prodqty_storunit'], cost = i['cost'])
#     session.add(ingredient)  # Ok Works

# for i in data['clients']:
#     client = Client(family_name = i['family_name'], first_name = i['first_name'],
#         email = i['email'], phone = i['phone'])
#     session.add(client)  # Ok Works

# for i in data['clients']:
#     name = [(n.id, n.family_name) for n in session.query(Client).all()]
#     for n in name:
#         if n[1] == i['family_name']:
#             for address in i['address']:
#                 addresses = Address(client = n[0], address = address)
#                 session.add(addresses)

# for i in data['pizzas']:
#     vat = [(n.id, n.rate) for n in session.query(Vat).all()]
#     for n in vat:
#         if n[1] == i['vat']:
#             pizza = Pizza(name = i['name'], price = i['price'], vat = n[0])
#             session.add(pizza)  # Ok Works

# for i in data['recipes']:
#     name = [(n.id, n.name) for n in session.query(Pizza).all()]
#     for n in name:
#         if n[1] == i['name']:
#             for rep in i['recipe']:
#                 ingr = [(n.id, n.name) for n in session.query(Ingredient).all()]
#                 for ningr in ingr:
#                     if ningr[1] == rep[0]:
#                         recipe = Recipe(pizza = n[0], ingredient = ningr[0], quantity = rep[1])
#                         session.add(recipe)  # Ok Works

# for i in data['stocks']:
#     name = [(n.id, n.name) for n in session.query(Ingredient).all()]
#     for n in name:
#         if n[1] == i['name']:
#             stock = Stock(ingredient = n[0], quantity = i['quantity'])
#             session.add(stock)  # Ok Works

for i in data['orders']:
    print(i)
    # Parse Data
    # Client.id > i['client_name'] == client.name
    # Order_status.id > i['order_status'] = order_status.status
    # Payment_status.id > i['pay_status'] = payement_status.status
    # Datetime > use datetime.date(yr, mth, day, hr, min, sec) & i['datetime']
    # session.add(order)
    
# for i in data['orders']:
#     print(i)
    # Parse Data > filter by datetime
    # order.id
    # pizza.id > i['pizza_name'] == pizza.name
    # same model as 'recipe'
    # session.add(pizza_ordered)

session.commit()
# Wrap it all up in a single function, then call that function in setup.py, Automatic all.
