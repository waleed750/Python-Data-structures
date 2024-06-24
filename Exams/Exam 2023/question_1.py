
#!1-  Define the following operations that can be performed
#A) Contstructor
"""
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount  # Transformer method to modify balance

    def withdraw(self, amount):
        self.balance -= amount  # Transformer method to modify balance
"""
#B) Transformer
"""
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount  # Transformer method to modify balance

    def withdraw(self, amount):
        self.balance -= amount  # Transformer method to modify balance
"""
#C) observer
"""
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def get_model(self):
        return self.model  # Observer method to get the model

    def get_year(self):
        return self.year  # Observer method to get the year

"""
# _____________________________________________________
#! I) 2- 
# from random import choice


# counteries = {
#     'EGYPT' : 'CAIRO ', 
#     'FRANCE' : 'PARIS' , 
#     'UK' : 'LONDON' ,
#     'USA' : 'WASHINGTON' , 
#     'ITALY' : 'ROME'
# }
# while True:
#     country = input("Enter country : ").upper()
#     if len(country) < 1 :
#         break
#     if country not in counteries.keys():
#         print("No such country")
#     else:
#         print(f"{country} it's capital {counteries[country]}")
    
#!_______________________

#! 3- Using Array Queue
from z_array_queue import ArrayQueue


txt = input("Enter text seperated by ':'  :")
lst =  txt.split(":")
left = lst[0]
right = lst[1]
len1 = len(left)
len2 = len(right)

Q = ArrayQueue()

for c in left:
    Q.enqueue(c)

i = 0 
match = True
while not Q.is_empty():
    if right[i] != Q.dequeue():
        match = False
        break
    i += 1 
if len1 == len2 and match :
  print("The left and right parts are exactly the same")
elif len1 == len2 and not match :
  print("The left and right parts have the same length "
                        + "but are different.")
elif len1 > len2 :
  print("The left part (before the colon) is longer than "
                    + "the right part.")
elif len1 < len2 :
  print("The right part (after the colon) is longer than "
                    + "the left part.") 