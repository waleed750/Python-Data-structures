
#! Thelist:     a sequence of related data
#!Thetuple:     a list whose elements may not be modified
#!1- Adictionary: a list of values that are accessed through their associated keys.
# print("waleed")

#!2- Tuple unpacking
# t = 1 , 'A' , [1,2,3]
# var , c , lst = t
# print(var,c,lst)

#!3- Converting a tupleto a list
# newLst = list(t)
# print(type(newLst))

#!4-  Converting a listto a tupleusing the tuplefunction
# tup = tuple(newLst)
# print(tup)

#!5- zip function pairs up elements from two different sequences.
# ?  If one of the sequences is shorter than
# ?  the other, the zip function stops at the
# ?  shorter sequence and ignores the
# ?  remainder of the longer sequence

# lst1 = [1, 2, 3, 4, 5, 6, 7]
# lst2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# for t in zip(lst1,lst2):
#     print(t)

# def gen(n):
#     """ Generates the first n perfect squares, starting with zero:
#     0, 1, 4, 9, 16,..., (n -1)ˆ2. """
#     for i in range(n):
#         yield i**2
# for p in zip([10, 20, 30, 40, 50, 60], gen(4)):
#         print(p, end=' ')
# print()

#!comperhension
# print([x + y for (x, y) in zip([1, 2, 3, 4, 5], [10, 11, 12, 13, 14])])
# for p in zip([1, 2, 3, 4, 5], [10, 11, 12, 13, 14]):
#     print(p)

#! Arbitary Argument List
def sum(*nums):
    print(nums) # See what numsreally is
    s = 0 # Initialize sum to zero
    for num in nums:     # Consider each argument passed to the function
        s += num # Accumulate their values
    return s # Return the sum
print(sum(2,3,5,6,7))