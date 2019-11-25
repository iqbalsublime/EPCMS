# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 01:33:18 2019

@author: iqbalsublime
"""

from Customer import Customer
from Restaurent import Restaurent
from Reserve import Reserve
from Menu import Menu
from Order import Order



cust1= Customer(1,"Iqbal", "0167****671")
rest1= Restaurent(1,"Farmgate", "102 Kazi Nazrul Islam Ave, Dhaka")
reserve1=Reserve(1, "20-11-2019",cust1, rest1)
print("******Reservation*******")
print("Reserve ID:{}, Date: {} Customer Name: {}, Mobile:{}, Branch: {}".format(reserve1.reserveid, 
      reserve1.date, reserve1.customer.name, reserve1.customer.mobile, reserve1.restaurent.bname))
#print(reserve1.description())
print("******Reservation*******")

menu1= Menu(1,"Burger", 160,"Fast Food")
menu2= Menu(2,"Pizza", 560,"Fast Food")
menu3= Menu(3,"Biriani", 220,"Indian")
menu4= Menu(4,"Pitha", 50,"Bangla")


order1= Order(1,"20-11-2019", cust1)
order1.addMenu(menu1)
order1.addMenu(menu2)

print("******Invoice*******")
print("Order ID:{}, Date: {} Customer Name: {}, Mobile:{}".format(order1.oid, 
      order1.date, order1.Customer.name, order1.Customer.mobile))
totalBill=0.0
serial=1
print("SL---Food----Price") 
for order in order1.menus:
    print(serial,order.name, order.price)
    totalBill=totalBill+order.price
print("Total :", totalBill) 
print("******Invoice*******")    