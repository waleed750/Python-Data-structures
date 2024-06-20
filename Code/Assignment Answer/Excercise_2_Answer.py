
#! 2.1 

# n = int(input("Enter Num : "))
#! As comperhension
# dit = {x : x*x for x in range(1,n+1)}
# dit = {}
# for i in range(1,n+1):
#     dit[i] = i
# print(dit)

#! 2.2 
# dit = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# sum = 0 
# for i in dit.values():
#     sum += i
# print(sum)

#! 2.3
# dit = {1: 15, 2: 22, 3: 8, 4: 31, 5: 10}

# MAX = dit[1]
# MIN = dit[1] 
# for value in dit.values():
#     print(value)
#     # to get Max 
#     MAX = max(MAX,value)
#     MIN = min(MIN,value)
# print(MAX , MIN)

#! 2.4 
# d1 = {'a': 100, 'b': 200, 'c':300} 
# d2 = {'a': 300, 'b': 200, 'd':400} 

# result = {}
# # Combine the first dictionary into the result
# for key in d1.keys():
#     result[key] = d1[key] 
    
# # Combine the second dictionary and add values for common keys
# for key in d2.keys():
#     if key in result:
#         result[key] += d2[key]
#     else:
#         result[key] = d2[key]
# print(result)
#! 2.5
# with open('excersice_2.txt','r') as fil:
#     words = fil.read().split(" ")
#     dit = {}
#     for w in words:
#         if w.strip() in dit :
#             dit[w.strip()] +=1 
#         else :
#             dit[w.strip()] = 0 
#     # print non duplicate only
#     for key,value in dit.items():
#         if value == 1 : print(key)

#! 2.6
# lst = [('hi', 'bye'), ('Geeks', 'forGeeks'), ('a', 'b'), ('hi', 'bye'), ('a', 'b')]  
# dit = {}
# for i in lst:
#     if i in dit:
#         dit[i] += 1
#     else:
#         dit[i] = 1
# print(dit)

# #! 2.7
# test_list = [('Gfg', 10), ('best', 3), ('CS', 8), ('Geeks', 7)]

# ord_list = ['Geeks', 'best', 'CS', 'Gfg']
# # Create a dictionary from the test_list
# tuple_dict = {item[0]: item for item in test_list}

# # Use list comprehension to order the tuples according to ord_list
# ordered_tuples = [tuple_dict[key] for key in ord_list]
# print(ordered_tuples)


#! 2.8 
# country_capitals = {
#     "United States": "Washington, D.C.",
#     "United Kingdom": "London",
#     "Canada": "Ottawa",
#     "Australia": "Canberra",
#     "India": "New Delhi",
#     "Japan": "Tokyo",
#     "France": "Paris",
#     "Germany": "Berlin",
#     "Brazil": "Brasília",
#     "South Africa": "Pretoria",
# }
# count = 0 
# country = "France"
# print(country)
# while count < 3:
#     capital = input(f"Enter capital of {country} : ")
#     if capital == country_capitals[country] : 
#         print("correct Answer")
#         break
#     else: 
#         print("Your answer is wrong")
#     count+=1
# else:
#     print("You guessed 3 times")
