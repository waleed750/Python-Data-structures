
#! III) Define depth and height 
from z_sorted_table_map import SortedTableMap


def depth(self,p):
    if self.is_root(p):
        return 0
    return 1 + (self.depth(self.parent(p)))
def height(self,p):
    if self.is_leaf(p):
        return  0
    return 1 + max(self.height(c) for c in self.children(p))

#!____________________________________
# 2- Create class called Empoyees 
class Empoyees:
    def __init__(self):
        self.emplist = SortedTableMap()
    def Add_Update_Emp(self,name,salaryBonus):
        try:
            value = self.emplist.__getitem__(name)
            if value is None:
                raise KeyError("Employee does not found")
            value += salaryBonus
            self.emplist(name,value)
        except KeyError : # in case of new Employee
            self.emplist.__setitem__(name,int(salaryBonus))
        finally:
            print("Employee Addition /update")
    def Remove_Emp(self,name):
        try:
            self.emplist.__delitem__(name)
            print("Employee Removed")
        except KeyError:
            print("Employee does not found")
    def DisplayEmps(self):
        for key in self.emplist.__iter__():
            print(key,self.emplist[key])
e = Empoyees()
while True:
    choice = input("Enter A)dd/R)emove/D)isplay/E)xit :")
    if choice == 'A' or choice == 'a':
        name = input("Enter Name :")
        salaryBonus = int(input("Enter salaryBonus :"))
        e.Add_Update_Emp(name,salaryBonus)
    elif choice == 'R' or choice == 'r':
        name = input("Enter Name :")
        e.Remove_Emp(name)
    elif choice == 'D' or choice == 'd':
        e.DisplayEmps()
    elif choice == 'E' or choice == 'e':
        break