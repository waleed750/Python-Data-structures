class Empty(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self._data = []

    def len(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("The stack is empty")
        else:
            return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("The stack is empty")
        else:
            return self._data.pop()


s = ArrayStack()
s.push(5)
s.push(6)

#! a.

# print(s._data)
# stack = ArrayStack()
# stack.push(s.top())
# s.pop()
# s.pop()
# print(stack._data)

#! b.
# bottom = 0
# while not s.is_empty() :
#     print(s.len())
#     bottom = s.pop()
# print(bottom)

#! c.

# bottom = 0
# stack_copy = ArrayStack()
# while not s.is_empty():
#     stack_copy.push(s.pop())
# bottom = stack_copy.top()
# while stack_copy.is_empty():
#     s.push(stack_copy.pop())
# print(s._data)
# print(bottom)

#! d.
# s_copy = ArrayStack()
# s_temp = ArrayStack()
# while not s.is_empty():
#     s_temp.push(s.pop())

# while not s_temp.is_empty():
#     element = s_temp.pop()
#     s.push(element)
#     s_copy.push(element)

# print(s._data)
# print(s_copy._data)

#!_________________________________6.2__________________________

# integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Befroe : ",integers)
# stack = ArrayStack()
# # initialize Array Stack but in reverse order
# for i in reversed(integers):
#     if i % 2 == 0:
#         stack.push(i)

# even_integers = []

# # intialize the new list using pop in Stack
# while not stack.is_empty():
#     even_integers.append(stack.pop())

# print("After : ",even_integers)

#!_________________________________6.3__________________________

# def prime_factors(n):
#     factors = []

#     # Get the number of 2s that divide n
#     while n % 2 == 0:
#         factors.append(2)
#         n //= 2

#     # n must be odd at this point, so we can skip even numbers
#     for i in range(3, int(n**0.5) + 1, 2):
#         while n % i == 0:
#             factors.append(i)
#             n //= i

#     # If n is a prime number greater than 2, then add it to the factors
#     if n > 2:
#         factors.append(n)

#     return factors
# def main():
#     s = ArrayStack()
#     n = int(input("Enter Positive Integer : "))
#     primes = prime_factors(n)
#     for p in primes:
#         s.push(p)
#     # display
#     while not s.is_empty():
#         print(s.pop() , end = " ")

# main()


#!_________________________________6.4__________________________
class EmptyError(Exception):
    pass


class ArrayQueue:

    def __init__(self):
        self.__data = [None] * 10
        self.__front = 0
        self.__size = 0

    def len(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def first(self):
        if self.is_empty():
            raise EmptyError
        return self.__data[self.__front]

    def dequeue(self):
        if self.is_empty():
            raise EmptyError
        old = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__front = (self.__front + 1) % len(self.__data)
        self.__size -= 1
        return old

    def enqueue(self, e):
        if self.__size == len(self.__data):
            self.resize(self.__size * 2)
        avail = (self.__front + self.__size) % len(self.__data)
        self.__data[avail] = e
        self.__size += 1

    def resize(self, cav):
        old = self.__data
        walk = self.__front
        self.__data = [None] * cav
        for k in self.__size:
            self.__data[k] = old[walk]
            walk = (walk + 1) % len(self.__data)
        self.__front = 0


Q = ArrayQueue()
Q.enqueue(2)
Q.enqueue(6)
Q.enqueue(3)

#! a.
# Q.dequeue()
# myQueue = Q.dequeue()

# print(myQueue)


#! b.

# lastQ = 0
# while not Q.is_empty():
#     lastQ = Q.dequeue()
# print("Last : ",lastQ)

#! c. 

# temp_queue = ArrayQueue()  # Create a temporary queue

# last_element = None
# # Transfer elements from the original queue to the temporary queue
# while not Q.is_empty():
#     last_element = Q.dequeue()  # Dequeue and update the last element
#     temp_queue.enqueue(last_element)  # Save elements in temporary queue
# # Restore the original queue by transferring back from temp_queue
# while not temp_queue.is_empty():
#     temp = temp_queue.dequeue()
#     print(temp)
#     Q.enqueue(temp)  


#! d. 
# copy = ArrayQueue()
#     # Use a temporary queue to avoid modifying the original
# temp_queue = ArrayQueue()
# # Transfer elements from the original queue to the temporary queue
# while not Q.is_empty():
#     item = Q.dequeue()
#     temp_queue.enqueue(item)
#     copy.enqueue(item)  # Add to the copy queue
#     # Restore the original queue
# while not temp_queue.is_empty():
#     Q.enqueue(temp_queue.dequeue()) 



#!_________________________________6.5__________________________

def main():
    q = ArrayQueue()  # Create a queue
    user_input = input("Enter a string in the form string1:string2: ")
    left, right = user_input.split(':')  # Split input into two parts
    len1, len2 = len(left), len(right)

    # Enqueue all characters from the left part into the queue
    for i in range(len1):
        q.enqueue(left[i])

    match = True  # To track if the left and right parts are identical
    if len1 == len2:  # Check if the lengths are the same
        for i in range(len2):
            if q.is_empty():
                match = False
                break
            if right[i] != q.dequeue():  # Compare characters
                match = False
                break

    if len1 == len2 and match:
        print("The left and right parts are exactly the same.")
    elif len1 == len2 and not match:
        print("The left and right parts have the same length but are different.")
    elif len1 > len2:
        print("The left part (before the colon) is longer than the right part.")
    elif len1 < len2:
        print("The right part (after the colon) is longer than the left part.")


main()  # Execute the main function