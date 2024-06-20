
#!_________________________________________1.1_______________________________________

#!  Write a Python code to do the following operations on a given tuple t:

# ? (a) add an item to the end of t.
# t = 1,2,3,5
# lst = list(t)
# lst.append(int(input("enter the item you want to add: ")))
# t = tuple(lst)
# print(t)


# ? (b) remove an item from t, given its index.
# lst = list(t)
# index = int(input('enter the index you want to delete: '))
# lst.remove(lst[index])
# t = tuple(lst)
# print(t)

# ? (c) remove duplicates from t.
# t = 1,2, 3, 1, 5 ,6 ,4, 2, 10 ,10
# lst = list(t)
# s = set(lst)
# t = tuple(s)
# print(t)

# ? (d) find the index of the first occurrence of an item in t.
# t = 1,2, 3, 1, 5 ,6 ,4, 2, 10 ,10
# lst = list(t)
# where = int(input("Enter the item you want to find: "))
# for i in range(len(lst)):
#     if lst[i] == where:
#         print(i)
#         break

#!_________________________________________1.2_______________________________________

# ?  Write a function, named orderedTuple(t,  ascending), which checks whether a
# ? given tuple t is ordered in ascending order or descending order. If you pass true
# ? to the ascending argument, the function checks for ascending order, otherwise it
# ? checks for descending order. Then, write a main program that tests this function.


# def orderedTuple(asc, t):
#     if asc:
#         lst = list(t)
#         temp = lst + []
#         lst.sort()
#         return temp == lst
#     else:
#         lst = list(t)
#         temp = lst + []
#         lst.sort()
#         temp.reverse()
#         print(lst, "||", temp)
#         return lst == temp


# t = (1, 2, 3, 1, 5, 6, 4, 2, 10, 10)
# print(orderedTuple(True, t))

#!_________________________________________1.3_______________________________________
# ?  Given a list of tuples, write a Python program to extract all tuples having K digit
# test_list1 = [(54, 2), (34, 55), (222, 23), (12, 45), (78,)]
# test_list2 = [(54, 2), (34, 55), (222, 23), (12, 45), (782,)]
# k = int(input("Enter what you search for : "))
# allTuples = []
# for t in test_list2:
#     k_digits = True
#     for d in t:
#         if len(str(d)) != k:
#             k_digits = False
#             break
#     if k_digits:
#         allTuples.append(t)

# print(allTuples)
#!_________________________________________1.4_______________________________________
# ? Given a tuple of lists, using tuple(), sorted(), and tuple comprehension, write a
# ? Python program to sort each list in the given tuple.
# ? Example:
# ? The original tuple is: ([7, 5, 4], [8, 2, 4], [0, 7, 5])
# ? The tuple after sorting lists: ([4, 5, 7], [2, 4, 8], [0, 5, 7])


# t = ([7, 5, 4], [8, 2, 4], [0, 7, 5])
# # tuple after sorted
# sortedTuple = tuple(sorted(sub) for sub in t)
# print(sortedTuple)
#!_________________________________________1.5_______________________________________
# lst =  [("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")] 
# #initialize the first item in a list 
# tuple_list = [i[0] for i in lst]
# tuple_list.sort()
# sorted_tuple = []
# # as the list is sorted by the first item 
# # we will loop untill we find the item depending on the sorted list 
# # for example tuple_list[0] => "Amana"
# # we will loop untill we found Amna and the added to the list 
# # so tuples within the list will be sorted 
# for item in tuple_list:
#     for t in lst:
#         if item in t :
#             sorted_tuple.append(t)
# print(sorted_tuple)   
 
#!_________________________________________1.6_______________________________________
# lst = [('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]
# result = ""
# for t in lst:
#     for num in t : result += num + " "
# print(result)

# #!_________________________________________1.7_______________________________________
# lst =  [('hi', 'bye'), ('Geeks', 'forGeeks'), ('a', 'b'), ('hi', 'bye'), ('a', 'b')]
# tup = tuple(input("Enter tuple : "))# becareful tuple take each char and convert it to as single value like this 
# # a, b => ('a' , ',' , 'b' ) ❌ False
# #* ab => ('a', 'b') ✔️ True
# count = 0 
# for t in lst :
#     if tup[0] == t[0] and tup[1] == tup[1] : count += 1
    
# print(f"{tup} count is {count}") 



#!_________________________________
def power_set(s):
    power_lst = [set()]
    for elem in sorted(list(s)):
        new_subsets = []
        for i in power_lst:
            copy_subset = i.copy()
            copy_subset.add(elem)
            new_subsets.append(copy_subset)
        power_lst.extend(new_subsets)
    return power_lst
S = {"a", "b", "c"}
result = power_set(S)
for subset in result:
    print(subset , end =" ")
print()



