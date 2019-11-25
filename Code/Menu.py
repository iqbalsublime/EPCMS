# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 02:24:12 2019

@author: iqbalsublime
"""


class Menu:
    CAT = ('Fast Food', 'Bangla', 'Indian', 'Misc')
    # Initializer / Instance Attributes
    def __init__(self, mid, name, price, category, quantity):
        if category not in self.CAT:
            raise ValueError("%s is not a valid category." % category)
        self.mid = mid
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity


menu1= Menu(1,"Burger", 160,"Fast Food",2)
#print(rest1.description())