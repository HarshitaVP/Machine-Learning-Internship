class product():
	def __init__(self,name,manufacturer,price):
    	self.name = name
        self.manufacturer = manufacturer
        self.price = price
    
    def info(self):
    	print("Name ",self.name," manufacturer ".self.manufacturer,
        " price ",self.price)
        
prodlist = []   	
total = 0
prod1 = product("HP Laptop","HP",70000)
prodlist.append(prod1)
prod1.info()
maximum = prod1.price
minimum = prod1.price
prod2 = product("MI TV","Xiaomi",50000)
prodlist.append(prod2)
prod2.info()
prod3 = product("Canon Printer","Canon",35000)
prodlist.append(prod3)
prod3.info()

for prod in prodlist:
	total += prod.price
	if(prod.price>=maximum)
    	maximum=prod.price
    if(prod.price<=minimum)
    	minimum=prod.price

print(total)
print(maximum)
print(minimum)