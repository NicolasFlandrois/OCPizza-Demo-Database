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
from models import Pizza, Ingredient, Recipe, Stock, Payement_status, Order_status, Client, Vat, Orders

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
#         email = i['email'], phone = i['phone'], address1 = i['address1'],
#         address2 = i['address2'], address3 = i['address3'], invoice_address = i['invoice_address'])
#     session.add(client)  # Ok Works

# for i in data['pizzas']:
#     vat = [(n.id, n.rate) for n in session.query(Vat).all()]
#     for n in vat:
#         if n[1] == i['vat']:
#             pizza = Pizza(name = i['name'], price = i['price'], vat = n[0])
#             session.add(pizza)  # Ok Works

session.commit()

# 3/attach relevent data to a class from models
# cf: http://www.lizsander.com/programming/2015/09/08/SQLalchemy-part-2.html
# 4/Append each tables & Commit to DB