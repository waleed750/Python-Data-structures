#! 3.1
s1 = {"George", "Jim", "John", "Blake", "Kevin", "Michael"}
s2 = {"George", "Katie", "Kevin", "Michelle", "Ryan"}

# print(f'Union : {s1 | s2}')
# print(f'Difference : {s1 - s2}')
# print(f'Symmetric Difference : {s1 ^ s2}')
# print(f'Intersection: {s1 & s2}')


def set_even_only(nums):
    # all check if all n is true
    # in our case means that if all even
    return all(n % 2 == 0 for n in nums)


# set_nums = {2,4,5,6,8,9,10}

# set_even = {2,4,6,8,10,22}
# print(f"{set_nums} are even ? {set_even_only(set_nums)}")
# print(f"{set_even} are even ? {set_even_only(set_even)}")


def remove_duplicated(lst: list):
    s = set(lst)
    lst = list(s)
    return " ".join(sorted(lst))


# txt = input("Enter text : ")
# txt = remove_duplicated(txt.split(" "))
# print(txt)


def max_min(s: set):
    return (max(s), min(s))
# s = {1, 2, 3, 15, 20, 1, 15, 30}
# temp = max_min(s)
# print(f"Max : {temp[0]} ,Min : {temp[1]}")

# write 3 diffrenet lists with common in 3 
# lst1 = [1, 2, 3, 15, 20, 1, 15, 30]
# lst2 = [12, 24, 35, 24, 88, 120 ,30, 155, 88, 120, 155]
# lst3 = [12 ,20 , 40 , 80 , 30 , 65 , 14 , 31 , 49]
# s1 = set(lst1)
# s2 = set(lst2)
# s3 = set(lst3)

# print("3 elements common in 3 lists : ", s1 & s2 & s3)
# def count_number_vowels(txt):
#     vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#     return sum(1 for w in txt if w in vowels)
# txt = input("Enter text : ")
# print("Number of vowels : ", count_number_vowels(txt))

# def is_symmetric(lst):
#     s = set()
#     for i in lst:
#         temp_num = (i[1] , i[0])
#         if temp_num in lst : 
#             if i not in s and temp_num not in s:
#                 s.add(i)            
#     return s
# #! sets 
# test_list = [(6,7) , (2 , 3 ) , ( 7, 6 )]
# test_list2 = [(6,7) , (2 , 3 )]
# print(f"Test_list 1: {is_symmetric(test_list)}")
# print(f"Test_list 2: {is_symmetric(test_list2)}")



#! 3.9
def power_set(s):
    # Convert the set to a list for easier indexing
    s_list = sorted(list(s))
    n = len(s_list)
    power_set = []

    # There are 2^n subsets for a set of size n
    for i in range(2**n):
        subset = []
        for j in range(n):
            # Check if the j-th bit in the binary representation of i is set
            if i & (1 << j):
                subset.append(s_list[j])
        power_set.append(subset)
    
    return power_set

# # Example usage
# S = {'a', 'b', 'c','d'}
# P = power_set(S)
# # Convert lists to sets for better representation
# P = [set(subset) for subset in P]
# print(P)



#! 4.1 Enumerate 
# lst = [12,24,35,70,88,120,155] 
# for t in enumerate(lst):
#     print(t)    

# #! 4.2 list comperhinshion 
# new_lst = [ lst[x[0]] for x in enumerate(lst) if x[0] not in [0,4,5]]
# print(list(new_lst)) 

# #! 4.3 zip function pairs up elements from two different sequences.
# titles = ["Everyday Italian", "XQuery Kick Start", "Learning XML"] 
# authors = ["James McGovern", "Erik T. Ray", "Giada De Laurentiis"] 
# years = [2003, 2007, 2005] 

# books = [b for b in zip(titles,years,authors)]
# for b in enumerate(books):
#     # 1. Everyday Italian (2005), by Giada De Laurentiis 
#     print(f"{b[0]+1}. {b[1][0]} ({b[1][1]}) by {b[1][2]}")
#! 4.4 
# from random import randint
# lst = [ randint(0,x) for x in range(10)]
# while True: 
#     try : 
#         index = int(input("Enter index : "))
#         if index > len(lst) : raise IndexError
#         value = int(input("Enter value : "))
#         print(f"Value at index {index} : {lst[index]}")
#     except IndexError :
#         print("Index out of bounds")
#         continue
#     finally:
#         print(f"lst : {lst}")

#! 4.5
# def factorial(n):
#     if n < 0 :
#         raise ValueError('Factorial expects non-negative integers')
#     if n == 0 :
#         return 1
#     return n * factorial(n-1)
# print(factorial(-5))

#! 4.6
class EmptyError(Exception):
    pass
class ArrayStack:
    def __init__(self) :
        self._data = []
    def len(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0 
    def push(self,e):
        self._data.append(e)
    def pop(self):
        if self.is_empty():
            raise EmptyError("Empty Stack")
        return self._data.pop()
    def top(self):
        if self.is_empty():
            raise EmptyError("Empty Stack")
        return self._data[-1]
# S = ArrayStack( ) # contents: [ ]
# S.push(5) # contents: [5]
# S.push(3) # contents: [5, 3]
# print(S.len()) # contents: [5, 3]; outputs 2
# print(S.pop( )) # contents: [5]; outputs 3
# print(S.is_empty()) # contents: [5]; outputs False
# print(S.pop( )) # contents: [ ]; outputs 5
# print(S.is_empty()) # contents: [ ]; outputs True
# S.push(7) # contents: [7]
# S.push(9) # contents: [7, 9]
# print(S.top( )) # contents: [7, 9]; outputs 9
# S.push(4) # contents: [7, 9, 4]
# print(S.len()) # contents: [7, 9, 4]; outputs 3
# print(S.pop( )) # contents: [7, 9]; outputs 4
# S.push(6) # contents: [7, 9, 6]

# s = ArrayStack()
# f = open('test_stack.txt','r')
# for line in f :
#     s.push(line.rstrip("\n"))
# f.close()
'''
5
10
11
20
30
78'''
# save changes in reverse order 
# f = open('test_stack.txt','w')
# while not s.is_empty() : 
#     f.write(f"{s.pop()}\n")
# f.close()


#! Hande Expression  [(5+x)-(y+z)]
def matching_delimiters(expr):
    left = '({['
    right = ')}]'

    S = ArrayStack()

    for c in expr:
        if c in left:
            S.push(c)
        elif c in right:
            if S.is_empty():
                return False
            if right.index(c) != left.index(S.pop()):
                return False
    return S.is_empty()
print(f"Handle Expression : {matching_delimiters("[(5+x)-(y+z)]")}")

def infix_to_postifix(expr):
    postifix_expr = []
    lefty = '('
    righty = ')'
    operators = "+-*/"
    precedence = {
        '+' : 1 , 
        '-' : 1 , 
        '*' : 2 , 
        '/' : 2 , 
    }
    S = ArrayStack()
    for c in expr :
        if c.isnumeric(): # numbers 
            postifix_expr.append(c)
        elif c == lefty : # Left operand 
            S.push(c)
        elif c == righty : # Right operand 
            while not S.is_empty() and S.top() != lefty : 
                postifix_expr.append(S.pop())
            S.pop() 
        elif c in operators :
            while ( not S.is_empty() 
            and S.top() in operators 
            and precedence[S.top()] >= precedence[c]
            ):
                postifix_expr.append(S.pop())
            S.push(c) # push the current operand 
    while not S.is_empty():
        postifix_expr.append(S.pop())  # Pop any remaining operators from the stack
    return "".join(postifix_expr)
expr_infix_to_postifix  = infix_to_postifix("( 6 - ( 2 + 3 ) ) * ( 3 + 8 / 2 ) + 2 ") 
print(expr_infix_to_postifix)


def Evaluate_Postfix(expr):
    S = ArrayStack()
    for c in expr:
        if c.isnumeric():
            S.push(c)
        else:
            op2 = int(S.pop())
            op1 = int(S.pop())
            S.push(eval(f"{op1} {c} {op2}"))
    return S.pop()
print(Evaluate_Postfix(expr_infix_to_postifix))