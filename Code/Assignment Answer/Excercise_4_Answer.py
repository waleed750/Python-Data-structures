#!4.1
# lst = [5, 15, 35, 8, 98]
# for i in enumerate(lst):
#     print(f"index {i[0]} = {i[1]}")


#! 4.2
# lst = [12,24,35,70,88,120,155]
# new_lst = [v for (i,v) in enumerate(lst) if v not in [lst[0] , lst[4] , lst[5]]]
# #print the values after removing the 0th 4th 5th
# for i in new_lst:
#     print(i)

#! 4.3
# titles = ["Everyday Italian", "XQuery Kick Start", "Learning XML"]
# authors = ["Giada De Laurentiis", "James McGovern", "Erik T. Ray"]
# years = [2005, 2003, 2007]

# # gather them in form of 1.(title , "("year ")","by" author)
# books = enumerate(zip(titles, years, authors))
# for i, book in books:
#     print(f"{i+1}.{book[0]} ({book[1]}) by {book[2]}")

#! 4.4
# lst = [12,24,35,70,88]
# print(f"Current List: {lst}")

# while True :
#     print("Enter index and the value to write the value : ")
#     index = int(input("index = "))
#     value = int(input("value = "))
#     try:
#         lst[index] = value
#         print(f"Updated List : {lst}")
#     except IndexError:
#         print("You are attempting to access an out of bounds element")
    
#!4.5
# def factorial(n):
#   if n < 0:
#     raise ValueError("Factorial expects non-negative integers")
#   if n == 0:
#     return 1
#   else:
#     return n * factorial(n-1)
  
# try:
#     print(factorial(5))
    
#     print(factorial(-2))
# except ValueError:
#     print("Factorial expects non-negative integers")

#!4.6
# def capitalize_last_name(name):
#     # if the value is no str object
#     if type(name) != str:
#         raise TypeError
    
#     fullname = name.split(" ")
#     if len(fullname) < 2:
#         raise ValueError
#     firstname = fullname[0][0].upper() + fullname[0][1:].lower()
#     lastname = fullname[1].upper()
#     return firstname +" " + lastname
# try:
#     print(capitalize_last_name("waleed Ashraf"))

#     # print(capitalize_last_name(1)) ##To Test Tyoe Error 

#     print(capitalize_last_name("waleed"))## To Test Value Error 
# except TypeError:
#     print("You Should Enter String only")
# except ValueError:
#     print("You should Enter two Names")

#!4.7
#Custom Exception 
class FormulaError(Exception):
    pass
def caluclate(txt):
    try:
        num1 = float(txt[0])
        num2 = float(txt[2])
        operator = txt[1]
        if operator == "+": return num1 + num2

        elif operator == "-" : return num1 - num2

        elif operator == "/" : return num1 / num2

        elif operator == "*" : return num1 * num2

        else:
            raise FormulaError
    
    except (ValueError,ZeroDivisionError):
        raise FormulaError
while True:
    n = input("Enter formulat like this eg.(1 + 1) or quit : ")
    if n.lower() == "quit": break

    txt = n.split(" ")

    if len(txt) < 3 : raise FormulaError

    
    try:
        print(n, " = ", caluclate(txt))
    except FormulaError:
            print("Formula Error Occured")

