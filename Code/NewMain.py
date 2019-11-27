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
from datetime import datetime


#cust1= Customer(1,"Iqbal", "0167****671")
rest1= Restaurent(1,"Farmgate", "102 Kazi Nazrul Islam Ave, Dhaka")
#reserve1=Reserve(1, "20-11-2019",cust1, rest1)

#menu1= Menu(1,"Burger", 160,"Fast Food",4)
#menu2= Menu(2,"Pizza", 560,"Fast Food",2)
#menu3= Menu(3,"Biriani", 220,"Indian",1)
#menu4= Menu(4,"Pitha", 50,"Bangla",5)

"""
order1= Order(1,datetime.now(), customer)
order1.addMenu(menu1)
order1.addMenu(menu2)
order1.addMenu(menu3)
order1.addMenu(menu4)
"""

def getRestaurentMenu(customer):
    menus=[]
    menu1= Menu(1,"Burger", 160,"Fast Food",0)
    menu2= Menu(2,"Pizza", 560,"Fast Food",0)
    menu3= Menu(3,"Biriani", 220,"Indian",0)
    menu4= Menu(4,"Pitha", 50,"Bangla",0)
    menus=[menu1, menu2, menu3, menu4]
    return menus

def reserveRestaurent():
    print("Enter Customer Name: ")
    name=input()
    print("Enter Customer Mobile no: ")
    mobile=input()
    cust1= Customer(1,name, mobile)
    reserve1=Reserve(1, datetime.now(),cust1, rest1)
    
    print("******Reservation*******")
    print("Reserve ID:{}, Date: {} Customer Name: {}, Mobile:{}, Branch: {}".format(reserve1.reserveid, 
          reserve1.date.strftime("%c"), reserve1.customer.name, reserve1.customer.mobile, reserve1.restaurent.bname))
    #print(reserve1.description())
    print("******Reservation*******")
    
def orderFood():
    orderID=0
    print("Enter Customer Name: ")
    name=input()
    print("Enter Customer Mobile no: ")
    mobile=input()
    customer=Customer(orderID, name, mobile)
    orderID=orderID+1
    menus=getRestaurentMenu(customer)
    foodId=-1
    quantity=-1
    order1= Order(1,datetime.now(), customer)
    
    print("Welcome", name,"\n")
    
    
    print("Please select your food...\n")
    
    print("--------Menu--------\n")
        
    for menu in menus:
        
        print("ID--Name--Price")
        print(menu.mid, menu.name, menu.price)
    orderFlag=-1
    while(orderFlag !=0):
        print("Enter 1 to order food, enter 0 to close the Menu")
        orderFlag=input()
        if(int(orderFlag)==0):
            break
        if(int(orderFlag)==1):
            print("Please enter food Id")
            foodId=input()
            print("Please enter quantity")
            quantity=input()
            #menus[foodId]
            #print(menus[int(foodId)])
            orderedMenu=menus[int(foodId)]
            orderedMenu.quantity=quantity
            order1.addMenu(orderedMenu)
            
        
    print("******Invoice*******")
    print("Order ID:{}, Date: {} Customer Name: {}, Mobile:{}".format(order1.oid, 
          order1.date.strftime("%c"), order1.Customer.name, order1.Customer.mobile))
    totalBill=0.0
    serial=1
    print("SL---Food----Price---Qy----total") 
    for order in order1.menus:
        print(serial,order.name, order.price, order.quantity, (float(order.price)*float(order.quantity)))
        totalBill=float(totalBill)+(float(order.price)*float(order.quantity))
        serial=serial+1
    print("Grand Total :", totalBill) 
    print("******Invoice*******")   

def main():
    print("Please select option")
    print("1. Reserve 2. Order 3. Payment")
    option= input()
    if(int(option)==1):
        reserveRestaurent()
    elif(int(option)==2):
        orderFood()
    elif(int(option)==3):
        print("Under developement...")   
    else:
        print("Please select right option")
        

if __name__ == '__main__':
    main()
