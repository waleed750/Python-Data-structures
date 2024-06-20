
#!9.1 Guessing the capitals
# map of countries with their capitals
import random
country_capitals = {
        "United States": "Washington, D.C.",
        "United Kingdom": "London",
        "Canada": "Ottawa",
        "Australia": "Canberra",
        "India": "New Delhi",
        "Japan": "Tokyo",
        "France": "Paris",
        "Germany": "Berlin",
        "Brazil": "Brasília",
        "South Africa": "Pretoria",
        }

def exec_9_1():
        
        country = random.choice(list(country_capitals.keys()))
        count = 0
        while True:
             user = input(f"what is the capital of {country} :")
             if user.lower() == country_capitals[country].lower() :
                print(f"correct Answer after {count} gusses")
                break
             else:
                 print(f"Incorrect Try again")
                 count += 1
             if count == 3 :
                print(f"Game Over the right answer is {country_capitals[country]}")
                break
from unsorted_table_map import UnsortedTableMap , print_map
def exec_9_2():
    M = UnsortedTableMap()
    for key in country_capitals.keys():
        M.__setitem__(key, country_capitals[key])
    print_map(M)
    country = random.choice(list(iter(M)))
    count = 0
    while True:
        if count == 3 :
            print(f"Game Over the right answer is {M.__getitem__(country)}")
            break
        user = input(f"what is the capital of {country} :")
        item = M.__getitem__(country).lower()
        if user.lower() == item :
            print(f"correct Answer after {count} gusses")
            break
        else:
            print("incorrect Try again")
        
        count += 1
exec_9_2()