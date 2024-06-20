
#! Sets 
#!______________________________________
#? x1.isdisjoint(x2) isTrue, thenx1 & x2is the empty set
#?  x1 |= x2 union x1 U x2
#? x1 &= x2 Modify a set by intersection
#? x1-=x2 Modify a set by difference updates x1,removing elements found in x2
#? x1 ^= x2 Modify a set by symmetric difference updates x1 , retaining elements found in either x1 or x2 but not both 
#? 
#! methos 
#? .discared(elem) not rasing exception 
#? .remove(elem)
#? .add(elem)

#!_______________________________________
#! See the standard mathematical set operations difference in slide 2 

# # Define two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print()

# # Union (U): Combines all unique elements from two sets
# union_set = set1 | set2  # Mathematical symbol: A ∪ B
# print("Union (set1 ∪ set2):", union_set)  # Output: {1, 2, 3, 4, 5}

# # Intersection (∩): Returns the common elements between two sets
# intersection_set = set1 & set2  # Mathematical symbol: A ∩ B
# print("Intersection (set1 ∩ set2):", intersection_set)  # Output: {3}

# # Difference (−): Returns elements in the first set but not in the second
# difference_set = set1 - set2  # Mathematical symbol: A − B
# print("Difference (set1 − set2):", difference_set)  # Output: {1, 2}

# # Symmetric Difference (△): Returns elements in either set, but not both
# symmetric_difference_set = set1 ^ set2  # Mathematical symbol: A △ B
# print("Symmetric Difference (set1 △ set2):", symmetric_difference_set)  # Output: {1, 2, 4, 5}

# # Subset (⊆): Checks if one set is a subset of another
# is_subset = set1 <= set2  # Mathematical symbol: A ⊆ B
# print("Is set1 a subset of set2? (set1 ⊆ set2):", is_subset)  # Output: True

# # Superset (⊇): Checks if one set is a superset of another
# is_superset = set2 >= set1  # Mathematical symbol: A ⊇ B
# print("Is set2 a superset of set1? (set2 ⊇ set1):", is_superset)  # Output: True



#!_____________________________________

x1 = {1,3,5}
x2 = {2,4,6}
x1.isdisjoint(x2)
