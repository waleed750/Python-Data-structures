# t = (1 , 2 , 3 , 15 , 20 , 1 , 15 , 30)
# lst = list(t)
# lst.append(100)
# t = tuple(lst)
# print(t)

# #! remove an tiem from t 
# lst = list(t)
# index = int(input('enter the index you want to delete: '))
# lst.pop(index)
# t = tuple(lst)
# print(t)

# #! remove duplicates from t 
# lst = []
# for i in t :
#     if i not in lst :
#         lst.append(i)
# t = tuple(lst)
# print("Tuple without duplicates : " , t)
# index = t.index(20)
# print(f"index of  20 = {index}")

# #! 1.2
# def orderedTuple(t,ascending = True):
#     lst = list(t)
#     sorted_lst  = sorted(lst)
#     if ascending:
#         return sorted_lst == lst
#     else : 
#         return [x for x in reversed(sorted_lst)] == lst

# # and those are use cases to test your function
# def test_orderedTuple():

#     print(orderedTuple((1, 2, 3)))# True
#     print(orderedTuple((3, 2, 1),False)) # False
#     print(orderedTuple((2, 1, 3)))
#     print(orderedTuple((1, 2, 2, 3)))
#     print(orderedTuple((-1, 0, 1)))
#     print(orderedTuple((1.0, 2.5, 3.0)))
#     print(orderedTuple((1, 15, 2)))
#     print(orderedTuple((3, 2, 1), ascending=False))

# test_orderedTuple()

#! 1.3
test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (782, )]
k = int(input("Enter K  = "))
tuples = []
for t in test_list:
    t1 = len(str(t[0]))
    if len(t) == 2: 
        t2 =  len(str(t[1]))
    else: 
        t2 = 0
    if ( t1 == k or t1 == 0 ) and (t2 == k or t2 == 0 ):
        tuples.append(t)
print(f"All tuples have numbers with {k} digits: {tuples}")