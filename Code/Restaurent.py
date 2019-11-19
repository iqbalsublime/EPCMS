# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:25:25 2019

@author: iqbalsublime
"""

class Restaurent:


    # Initializer / Instance Attributes
    def __init__(self, rid, bname, address):
        self.rid = rid
        self.bname = bname
        self.address = address

    def getBranchName(self):
        return self.bname
    # instance method
    def description(self):
        return "Address of branch {} is: {}".format(self.bname, self.address)

rest1= Restaurent(1,"Farmgate", "102 Kazi Nazrul Islam Ave, Dhaka")
#print(rest1.description())