# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:14:15 2020

@author: Harshita Pawar
"""


course = "python"
print(course)
print(type(course))

task = True
print(type(task))

'''
list
dynamic, growable and indexable list
allow duplicates
'''

student = ['abc','def','xyz']
print(student)
print(type(student))

'''
dictionary - key:value pair
doesnt allow duplicates
'''

dict = {"abc":123,"efg":456}
print(dict)
print(type(dict))

'''
tuples
constant list
once created cant be modified
'''

statelist = ('karnataka','ap')
print(type(statelist))

'''
set
mathematical set - no duplicates
'''

even = {2,4,6,8}
print(type(even))

'''
loops
'''

start = 1
end =10
while (start <= end):
    print(start)
    start += 1
    
x = 10
for i in range(1,x+1):
    print(i)

for i in range(2,21,2):
    print(i)

for m in student:
    print(m)

age = 19
if(age<18):
    print("Not eligible to vote")
else:
    print("Eligible to vote")
    


'''
functions and user inputs
'''

def greet():
    print("Hello world!")
    
greet()


def greet(name):
    print("Hello",name)
    
greet("rita")


name = input("Enter your name")
greet(name)


'''
simple interest
'''

def SI(p,r,t):
    return((p*r*t)/100)

r = float(input("Enter rate of interest"))
p = int(input("Enter principle"))
t = int(input("Enter Time"))

si = SI(p,r,t) 

print("Simple interest is ",si)   


'''
list demo
growable(no fixed length)

CRUD - CREATE, READ, UPDTE AND DELETE
'''

'''
create
'''
data = [30,40,50,60]
print("Original list ",data)
data.append(70)
print("After appending ",data)

'''
read
'''

for d in data:
    print(d)

'''
update
'''

data[2]=55
print("After update ",data)


'''
delete
'''

del data[0]
print("after deleting 1st element ",data)


'''
slicing
'''

data1 = [30,40,50,60,70,80,90,100]
print(data1[0:3])

'''
length
'''
length = len(data1)
print("Length of data1 is ",length)

'''
max
'''
maximum = max(data1)
print(maximum)

'''
min
'''

minimum = min(data1)
print("minimum ",minimum)

'''
sum
'''

res = sum(data1)
print("sum is", res)


'''
Dynamically a list of marks
'''

sub = int(input("Enter the number of subjects"))

markslist = []

for i in range(sub):
    marks = int(input("Enter the marks"))
    markslist.append(marks)
print("markslist ",markslist)
    

'''
Corona Dashboard
'''

coronadash = []
headerlist = []
state = []
col = int(input("Enter the number of columns in the corona dashboard"))

for i in range(col):
    headerlist.append(input("Enter the header name"))
coronadash.append(headerlist)

states = int(input("Enter the number of states"))
s=[]
for j in range(1,col):
s[j] = 0
for i in range(states):
    for j in range(col):
        state.append(input("Enter the data"))
    coronadash.append(state)
    for j in range(1,col):
        s[j] = 0
    for j in range(1,col):
        s[j] += state[j]
    coronadash.append(s)
    
        

print(coronadash)    


'''
dictionary
'''

phonedict = {}

phonedict['abc'] = 123

phonedict.update({'xyz':456})

print(phonedict)
print(phonedict.values())
print(phonedict.keys())

del phonedict['abc']

for k,v in phonedict.items():
    print('keys ',k,' values ',v)
    


'''
corona dash - dictionary
'''

coronadict1 = []
headerdict = {}
headerdict['State'] = ['total','cured','active','death']
coronadict1.append(headerdict)

s = int(input("Enter the number of states"))
for i in range(s):
    bodydict = eval(input("Enter the name of state, total, cured, active cases and death (dictionary)"))
    coronadict1.append(bodydict)
print(coronadict1)

'''
eval - takes any type of input (list, dictionary, tuple, set)
'''

'''
classes
'''

class corona():
    '''
    instance variables
    '''
    state = ''
    totalcases = 0
    active = 0
    cured = 0
    death = 0
    
    '''
    methods
    '''
    
    def addCases(self,state,totalcases,active,cured,death):
        self.state = state
        self.totalcases = totalcases
        self.active = active
        self.cured = cured
        self.death = death
    
    def info(self):
        return "state ",self.state," totalcases ",self.totalcases      
    
'''
function call - pass by value
'''


kar = corona()
kar.addCases("karnataka",1000,800,150,50)
print(kar.info())

    
tn = corona()
tn.addCases("tamil nadu",2000,1800,180,20)
print(tn.info())


'''
constructors
'''
import random

class Account():
    def __init__(self,name,address,email,mobile,idproof,aadhar = None):
        self.name = name
        self.address = address
        self.email = email
        self.mobile = mobile
        self.idproof = idproof
        if(aadhar):
            self.aadhar = aadhar
        self.acctno = int(random.random()*1000)
        self.balance = 0
        
    def deposit(self,acctno,amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self,acctno,amount):
        self.balance = self.balance - amount
        return self.balance
    
    def checkBalance(self,acctno):
        return self.balance
    
    def info(self):
        print("Name - ",self.name," balance - ",self.balance)
        
        
acctList = []

        
myact = Account("abc","bangalore","abc@gmail.com","1234523456","234")
print("account number ",myact.acctno)

acctno = myact.acctno
balance = myact.deposit(acctno, 10000)
print("balance after deposit ",balance)
balance = myact.deposit(acctno, 15000)
print("balance after deposit ",balance)
balance = myact.withdraw(acctno, 5000)
print("balance after withdrawal ",balance)
balance = myact.checkBalance(acctno)
print("current balance ",balance)


acctList.append(myact)

myact1 = Account("abc","bangalore","abc@gmail.com","1234523456","234","2019")
print("account number ",myact1.acctno)
balance = myact1.deposit(acctno, 50000)
print("balance after deposit ",balance)

acctList.append(myact1)

total = 0
for act in acctList:
    print("Info ",act.info())
    total = total + act.balance
    
print("Total Balance ",total)






























