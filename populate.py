#!/usr/bin/python3.7
# UTF8
# Date: Tue 23 Jul 2019 16:00:00 CEST
# Author: Nicolas Flandrois


import json
import datetime
from connection import connect
from models import Pizza, Ingredient, Recipe_ingredient, Stock, Payment_status
from models import Client, Vat, Order, Pizza_ordered, Address, Order_status
from models import Restaurant


def populate(dbname, jsondata):
    """docstring for populate"""
    session = connect(dbname)

    with open(jsondata) as f:
        data = json.load(f)

    for i in data['vat']:
        vat = Vat(rate=i)
        session.add(vat)

    for i in data['pay_status']:
        p_status = Payment_status(status=i)
        session.add(p_status)

    for i in data['order_status']:
        o_status = Order_status(status=i)
        session.add(o_status)

    for i in data['ingredients']:
        ingredient = Ingredient(name=i['name'], delivunit=i['delivunit'],
                                storunit=i['storunit'],
                                storqty_delivunit=i['storqty_delivunit'],
                                produnit=i['produnit'],
                                prodqty_storunit=i['prodqty_storunit'],
                                cost=i['cost'])
        session.add(ingredient)

    for i in data['clients']:
        client = Client(family_name=i['family_name'],
                        first_name=i['first_name'], email=i['email'],
                        phone=i['phone'])
        session.add(client)

    for i in data['clients']:
        name = [(n.id, n.family_name) for n in session.query(Client).all()]
        for n in name:
            if n[1] == i['family_name']:
                for index, address in enumerate(i['address']):
                    if index == 0:
                        addresses = Address(client=n[0], address=address,
                                            invoice=True)
                        session.add(addresses)
                    else:
                        addresses = Address(client=n[0], address=address,
                                            invoice=False)
                        session.add(addresses)

    for i in data['pizzas']:
        vat = [(n.id, n.rate) for n in session.query(Vat).all()]
        for n in vat:
            if n[1] == i['vat']:
                pizza = Pizza(name=i['name'], price=i['price'], vat=n[0])
                session.add(pizza)

    for i in data['recipes']:
        name = [(n.id, n.name) for n in session.query(Pizza).all()]
        for n in name:
            if n[1] == i['name']:
                for rep in i['recipe']:
                    ingr = [(n.id, n.name) for n in
                            session.query(Ingredient).all()]
                    for ningr in ingr:
                        if ningr[1] == rep[0]:
                            recipe = Recipe_ingredient(pizza=n[0],
                                                       ingredient=ningr[0],
                                                       quantity=rep[1])
                            session.add(recipe)

    for i in data['restaurants']:
        restaurant = Restaurant(name=i)
        session.add(restaurant)

    for i in data['stocks']:
        restaurant = [(n.id, n.name) for n in session.query(Restaurant).all()]
        for r in restaurant:
            if r[1] == i['stock_loc']:
                name = [(n.id, n.name) for n in
                        session.query(Ingredient).all()]
                for n in name:
                    if n[1] == i['name']:
                        stock = Stock(stock_loc=r[0], ingredient=n[0],
                                      quantity=i['quantity'])
                        session.add(stock)

    for i in data['orders']:
        name = [(n.id, n.family_name) for n in session.query(Client).all()]
        for n in name:
            if n[1] == i['client_name']:
                o_status = [(n.id, n.status) for n in
                            session.query(Order_status).all()]
                for o in o_status:
                    if o[1] == i['order_status']:
                        p_status = [(n.id, n.status) for n in
                                    session.query(Payment_status).all()]
                        for p in p_status:
                            if p[1] == i['pay_status']:
                                dstring = i['datetime']
                                dt = datetime.datetime.strptime(dstring,
                                                                '%Y, %m, %d, \
%H, %M, %S')
                                order = Order(date=dt, client=n[0],
                                              order_status=o[0],
                                              payment_status=p[0])
                                session.add(order)

    for i in data['orders']:
        dstring = i['datetime']
        dt = datetime.datetime.strptime(dstring, '%Y, %m, %d, %H, %M, %S')
        order = [(n.id, n.date) for n in session.query(Order).all()]
        for o in order:
            if o[1] == dt:
                pizza = [(n.id, n.name) for n in session.query(Pizza).all()]
                for o_pizza in i['pizza_name']:
                    for p in pizza:
                        if p[1] == o_pizza:
                            pizza_ordered = Pizza_ordered(order_cd=o[0],
                                                          pizza=p[0], quantity=1)
                            session.add(pizza_ordered)

    session.commit()
