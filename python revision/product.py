# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:35:29 2020

@author: Harshita Pawar
"""


class product():
    
    def __init__(self,code,name,manufacturer,price):
        self.code = code
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        
    def info(self):
        print("Code ",self.code," Name ", self.name," manufacturer ",self.manufacturer," price ",self.price)
        
total = 0
productList = []

prod1 = product(123,"Xiaomi Phone","Xiaomi",16000)
maximum = prod1.price
minimum = prod1.price
productList.append(prod1)

prod2 = product(456,"HP Laptop","HP",75000)
productList.append(prod2)

prod3 = product(789,"Sony TV","Sony",60000)
productList.append(prod3)


for pro in productList:
    pro.info()
    total = total + pro.price
    if(pro.price >= maximum):
        maximum = pro.price
    if(pro.price <= minimum):
        minimum = pro.price

print("total ",total)
print("maximum price ",maximum)
print("minimum price ",minimum)

