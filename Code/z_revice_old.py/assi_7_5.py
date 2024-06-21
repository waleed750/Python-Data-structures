class EmptyError(Exception):
    pass
class LinkedStack:
    class _Node:
        __slots__ = '_element' , '_next'
        def __init__(self,element,next):
            self._element = element
            self._next = next
    def __init__(self):
        self._head = None
        self._size = 0 

    def len(self):
        return self._size
    def is_empty(self):
        return self._size == 0 
    def top(self):
        if self.is_empty():
            raise EmptyError("Linked Stack is Empty")
        return self._head._element
    def push(self,e):
        self._head = self._Node(e,self._head)
        self._size += 1
    def pop(self):
        if self.is_empty():
           raise EmptyError("Linked Stack is Empty") 
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
    def display(self):
        
        if self.is_empty():
            raise EmptyError("Linked Stack is Empty")
        print("Stack contains : ",end="")
        current = self._head
        while current :
            print(current._element,end=" ") 
            current = current._next
        print()
s = LinkedStack()
s.push(10)
s.push(50)
s.push(20)
s.push(30)
print(s.len())
print(s.pop())
print(s.is_empty())
# s.display()

#! 6.1 for 7.5
#! 6.1 a. 
# if s.is_empty() and s.len() < 2:
#     raise EmptyError("Linked Stack is Empty")
# s.pop()
# secondElement = s.pop()
# print(f"Second Element : {secondElement}")
# s.display()
#! 6.1 b. Set bottom equal to the bottom element in s, leaving s empty. 
# while not s.is_empty() :
#     last = s.pop()
# print("Bottom Element : ",last)
#! 6.1 c. Set bottom equal to the bottom element in s, leaving s unchanged. 
# temp_stack = LinkedStack()
# while not s.is_empty() :
#     temp_stack.push(s.pop())
# print("Bottom Element after Leaving stack Empty : ",temp_stack.top())
# # restore Stack
# while not temp_stack.is_empty() :
#     s.push(temp_stack.pop())
# s.display()
#! 6.1 d. Make a copy of s, leaving s unchanged. 
# Assume s is already populated
# if s.is_empty():
#     raise Exception("Stack is empty")

# copy_stack = LinkedStack()
# temp_stack = LinkedStack()

# # Transfer elements from s to temp_stack to reverse the order
# while not s.is_empty():
#     temp_stack.push(s.pop())

# # Transfer elements back to s and also to copy_stack
# while not temp_stack.is_empty():
#     element = temp_stack.pop()
#     s.push(element)
#     copy_stack.push(element)

# s.display()
# copy_stack.display()

#! 6.2 Get Even int orders only without odd order 
# # this is a random even or odd loop
# random_stack = LinkedStack()
# print("Random stack before even numbers : ",end="")
# numbers1 = [23, 44, 12, 57, 9, 31, 28, 65, 84, 10]
# numbers2 = [7, 18, 92, 37, 54, 81, 6, 45, 72, 29]
# numbers2 = reversed(numbers2)
# for i in numbers2:
#     random_stack.push(i)
# random_stack.display()
# temp_stack = LinkedStack()
# # store ony even numbers in temp_stack
# while not random_stack.is_empty():
#     element = random_stack.pop()
#     if element % 2 == 0 :
#         temp_stack.push(element)
# # restore even numbers the same order 
# while not temp_stack.is_empty():
#     random_stack.push(temp_stack.pop())

# random_stack.display()


#! 6.3 
# n = 120 
# i = 2
# f = []
# def prime_factors_linked_stack(n):
#     """Returns a list of all prime factors of the nonnegative integer n."""
#     i = 2 
#     temp_stack = LinkedStack()
#     while i * i <= n :
#         if n % i :
#             i += 1
#         else:
#             n //= i 
#             temp_stack.push(i)
#     if n > 1 :
#         temp_stack.push(n)
#     factors = LinkedStack()
#     while not temp_stack.is_empty():
#         factors.push(temp_stack.pop())
#     return factors
# factors = prime_factors_linked_stack(int(input("Enter a number : ")))
# factors.display()

#!_________Queue_________
class LinkedQueue:
    class _Node:
        def __init__(self,element,next):
            self._element = element
            self._next = next
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0 
    def len(self):
        return self._size
    def first(self):
        if self.is_empty():
            raise EmptyError
        return self._head._element
    def is_empty(self):
        return self._size == 0 
    def enqueue(self,e):
       newest = self._Node(e,None)
       if self.is_empty():
           self._head = newest
       else:
           self._tail._next = newest
       self._tail = newest
       self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyError("Empty Queue")
        oldest = self._head
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return oldest._element
    def display(self):
        if self.is_empty():
            raise EmptyError("Empty Queue")
        current = self._head
        print("Linked Queue : ",end=" ")
        while current != None:
            print(current._element, end=" -> ")
            current = current._next
        print()
print(f"{'_'*20}Queue{'_'*20} \n")
# original front two elements.
q = LinkedQueue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
q.display()
#! 6.4 a.Set secondElement to the second element in myQueue, leaving myQueue without its 
# q.dequeue()
# secondElement = q.dequeue()
# print(f"After Deleting the two top elements : {secondElement}")
# q.display()
#! 6.4 b. Set last equal to the rear element in myQueue, leaving myQueue empty.
# while not q.is_empty():
#     last = q.dequeue()
# print(f"Last : {last}")
#! 6.4 c.
# last = q.last()
#! 6.4 d.

#!6.5
txt = input("Enter txt sperated by ':' ")
def match(txt):
    if ":" not in txt:
        raise ValueError("Missing ':'")
    lens = txt.split(":")
    left = lens[0]
    right = lens[1]
    len1 = len(left)
    len2 = len(right)
    q = LinkedQueue()
    for i in range(len1):
        q.enqueue(txt[i])
    if len1 == len2:
        match = True
        i = 0 
        while not q.is_empty():
            if right[i] != q.dequeue():
                match = False
                break
            i += 1
        if match:
            print("The left and right parts are exactly the same.")
        else:
            print("The left and right parts have the same length but are different.")
    elif len1 > len2:
        print("The left part (before the colon) is longer than the right part.")
    else : 
        print("The right part (after the colon) is longer than the left part.")        

