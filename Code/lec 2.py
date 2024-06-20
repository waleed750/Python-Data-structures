

#! Dictionaries
#! .keys() | .values() | .items() | .get(key) | .copy() | .clear()
#! .update()
#To iterate through keys
#? .keys()

# d = {'Fred': 44, 'Tom': 56, 'Jim': 32, 'Bob': 60}
# for k in d.keys():
#     print(k, end=' ')
# print()
# # OR
# for i in d:
#     print(i, end=' ')
# print()


#To it iterate through values
#? .values()

# for v in d.values() :
#     print(v ,end=' ')
# print()

#To iterate in pais use 
#? .items()
# for k,v in d.items():
#     print(k,v)


#!____________________________________________

#? >>> d = {'Fred': 44, 'Tom': 56, 'Jim': 32, 'Bob': 60}
#? >>> c = d.copy()
#* >>> c
#? {'Fred': 44, 'Tom': 56, 'Jim': 32, 'Bob': 60}
#? >>> d.get('Tom')
#* 56
#? >>> d.get('Sam')
#? >>> d.get('Sam', 66)
#* 66
#? >>> d
#? {'Fred': 44, 'Tom': 56, 'Jim': 32, 'Bob': 60}
#? >>> d.setdefault('sam', 66)
#* 66
#? >>> d
#* {'Fred': 44, 'Tom': 56, 'Jim': 32, 'Bob': 60, 'sam': 66}

#? >>> d.setdefault('sam')
#* 66
#? >>> d.setdefault('sara')
#? >>> d.update({'Paul':87, 'Peter':90})
#? >>> d
#* {'Fred': 44, 'Tom': 56, 'Jim': 32, 'Bob': 60, 'sam': 66, 'sara': None, 'Paul': 87, 'Peter': 90}
#? >>> d.keys()
#* dict_keys(['Fred', 'Tom', 'Jim', 'Bob', 'sam', 'sara', 'Paul', 'Peter'])
#? >>> d.values()
#? dict_values([44, 56, 32, 60, 66, None, 87, 90])
#? >>> d.clear()
#? >>> d
#* {}


#!____________________________________________________________

#!  Example 1:Consider the problem of implementing a 
#!  simple telephone contact list. 

# contacts = {} # The global telephone contact list
# running = True
# while running:
#     command = input('A)ddD)eleteL)ookup Q)uit: ')
#     if command.lower() == 'a':
#         name = input("Enter new Name : ")
#         contacts[name] = input("Enter phone number : ")
#     elif command.lower() == 'd':
#         name = input("Enter new Name : ")
#         del contacts[name]
#     elif command == 'D' or command == 'd':
#         name = input('Enter name to delete :')
#         del contacts[name]
#     elif command == 'L' or command == 'l':
#         name = input('Enter name :')
#         print(name, contacts[name])
#     elif command == 'Q' or command == 'q':
#         running = False
#     elif command == 'dump': # Secret command
#         print(contacts)
#     else:
#         print(command, 'is not a valid command')


#!____________________________________________________________

#! Function to count word occurrences in a text file

# def main():
#     """Counts the words in a text file."""
#     filename = input('Enter the name of a text file: ')  # Ask for filename
#     counters = {}  # Initialize the counting dictionary
    
#     with open(filename, 'r') as f:  # Open the file for reading
#         content = f.read()  # Read the entire file content
#         words = content.split()  # Create a list of individual words
    
#     # Iterate through each word and count occurrences
#     for word in words:
#         word = word.upper()  # Make the word all caps (case-insensitive)
        
#         if word not in counters:
#             counters[word] = 1  # First occurrence, add the counter
#         else:
#             counters[word] += 1  # Increment existing counter
    
#     # Report the counts for each word
#     for word, count in counters.items():
#         print(word, count)  # Display word and its count


# # If this script is being run directly, execute the main function
# if __name__ == '__main__':
#     main()  # Call the main function


#! line list comprehension
s = " 85, 54 , 13,     17, 44 ,31   , 80, 35,    30, 54, 78    " 
int_list= [int(x.strip()) for x in s.split(",")]
print(int_list)

#! _______________________________________________

#! Groupingwith Dictionaries
# Function to group words by their length
def main():
    """Counts the words in a text file and groups them by length."""
    filename = input('Enter the name of a text file: ')  # Ask for filename
    groups = {}  # Initialize the grouping dictionary
    
    with open(filename, 'r') as f:  # Open the file for reading
        content = f.read()  # Read the entire file content
        words = content.split()  # Create a list of individual words
    
    # Iterate through each word and group them by length
    for word in words:
        word = word.upper()  # Make the word all caps (case-insensitive)
        size = len(word)  # Compute the word's length
        
        if size in groups:
            if word not in groups[size]:  # Avoid duplicates
                groups[size].append(word)  # Add the word to its group
        else:
            groups[size] = [word]  # Create a new group for this length
    
    # Show the groups
    for size, group in groups.items():
        print(f"Words of length {size}: {group}")  # Print the group by word length


# If this script is being run directly, execute the main function
if __name__ == '__main__':
    main()  # Call the main function
