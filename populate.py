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
from models import Pizza, Ingredients, Recipe, Stock, Payement_status, Order_status, Client, Vat, Orders

# Base = declarative_base() # Normalement ne sera pas utiliser
session = connect('ocpizza')

# 1/Read json raw data file
with open("data.json") as f:
    data = json.load(f)
    print(data)

# Raised error:

# 2/store in memory relevent data?

# 3/attach relevent data to a class from models
# cf: http://www.lizsander.com/programming/2015/09/08/SQLalchemy-part-2.html
# 4/Append each tables & Commit to DB