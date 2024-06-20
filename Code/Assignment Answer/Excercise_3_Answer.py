#!3.1
# set1 = { "George", "Jim", "John", "Blake", "Kevin", "Michael"}
# set2 = {"George", "Katie", "Kevin", "Michael", "Ryan"}

# print(f'Union : {set1 | set2}')
# print(f'Difference : {set1 - set2}')
# print(f'Symmetric Difference : {set1 ^ set2}')
# print(f'Intersection: {set1 & set2}')

#!3.2
# def set_even_only(nums):
#     # all check if all n is true
#     # in our case means that if all even
#     return all(n % 2 ==0 for n in nums)
# set_nums = {2,4,5,6,8,9,10}

# set_even = {2,4,6,8,10,22}
# print(f"{set_nums} are even ? {set_even_only(set_nums)}")
# print(f"{set_even} are even ? {set_even_only(set_even)}")


#! 3.3
# # A longer sequence of whitespace-separated words with some duplicates
# words_sequence = (
#     "this is a sample text to test the script "
#     "this text contains some duplicated words and some unique words "
#     "please make sure to find duplicated words and report them "
#     "test the code with different sequences to ensure it works"
# )

# # Split the sequence into a list of words
# words_list = words_sequence.split()

# # Track unique words and find duplicates
# unique_words = set()

# # Check each word in the list
# for word in words_list:
#     unique_words.add(word)

# # Display the list of duplicate words
# print("Duplicate words:", sorted(unique_words))  # Output: {'words', 'and', 'to', 'test', 'the', 'this'}

#!3.4
# values = input("Enter a set of values separated by commas: ")
# set_values = {int(value.strip()) for value in values.split(",")}
# MIN = list(set_values)[0]
# MAX = list(set_values)[0]
# for i in set_values:
#     if MAX < i:
#         MAX = i
#     if MIN > i:
#         MIN = i
# print("Max : ", MAX, "Min", MIN)

#! 3.5
# list1 = [1, 2, 3, 4, 5 , 6]
# list2 = [3, 4, 5, 6, 7]
# list3 = [5, 6, 7, 8, 9]

# common_values = set(list1) & set(list2) & set(list3)
# print(common_values)

#! 3.6
# # Given list with duplicates
# input_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

# # Set to track unique values
# seen = set()

# # List to store the result without duplicates
# unique_list = []

# # Iterate through the original list
# for item in input_list:
#     # If the item has not been seen before, add it to the set and the unique list
#     if item not in seen:
#         seen.add(item)
#         unique_list.append(item)

# print("List after removing duplicates:", unique_list)  # Output: [12, 24, 35, 88, 120, 155]


#! 3.7
# # Define the set of vowels
# vowels = {"a", "e", "i", "o", "u"}

# # Given string to check
# input_string = "This is a simple example to demonstrate counting vowels using sets."

# # Convert the string to lowercase for case-insensitive comparison
# input_string_lower = input_string.lower()

# # Count the number of vowels
# vowel_count = 0

# # Iterate through each character in the string
# for char in input_string_lower:
#     # If the character is a vowel, increment the count
#     if char in vowels:
#         vowel_count += 1

# print("Number of vowels in the string:", vowel_count)

#! 3.8
# pair_list = [(6, 7), (2, 3), (7, 6)]

# pairs = set()
# for i in pair_list:
#     reversed_list = (i[1], i[0])
#     if reversed_list in pair_list:
#         if reversed_list not in pairs and i not in pairs:
#             pairs.add(i)
# print(pairs)


#!3.9
def power_set(items):
    lst_items = list(items) 
    N = len(lst_items)
    all_subsets = []

    # Iterate over all possible subsets
    for i in range(2 ** N):
        combo = []
        for j in range(N):
            # If the jth bit in i is set, include the jth item in the subset
            if (i >> j) % 2 == 1:
                combo.append(lst_items[j])
        # Add the subset to the list of all subsets
        all_subsets.append(combo)

    return all_subsets


#! 3.10
def subsets_of_size(power_set, k):
    # Filter the power set to only include subsets of size k
    return [set(subset) for subset in power_set if len(subset) == k]


# Example usage
my_set = {1, 2, 3}
power_set_result = power_set(my_set)

# Get subsets of size 2
new_subsets_of_size = subsets_of_size(power_set_result, 2)

print("Subsets of size 2 from set", my_set, ":", new_subsets_of_size)

s2 = {1, 2, 3, 4}
k2 = 3
result2 = power_set(s2)
new_subsets_of_size = subsets_of_size(result2,3)
print("Subsets of size", k2, "from set", s2, ":", new_subsets_of_size)