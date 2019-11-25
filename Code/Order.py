# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 02:26:52 2019

@author: iqbalsublime
"""

class Order:


    # Initializer / Instance Attributes
    def __init__(self, oid,date, Customer):
        self.oid = oid
        self.date = date
        self.Customer = Customer
        self.menus = []

    def addMenu(self, menu):
        self.menus.append(menu)

#order1= Order(1,"20-11-2019", 160,"Fast Food")
#print(rest1.description())