# #! Array Stack 
# class Node:
#     __slots__ = "_element" , "_next"
#     def __init__(self,element,next):
#         self._element = element
#         self._next = next
# class EmptyError: 
#     pass
# class ArrayQueue:
#     def __init__(self) :
#         self.__data = [None] * 10
#         self.__front = 0    
#         self.__size = 0
#     def is_empty(self):
#         return self.__size == 0
#     def len(self):
#         return self.__size
    
#     def dequeue(self):
#         if self.is_empty():
#             raise EmptyError
#         element = self.__data[self.__front]
#         self.__data[self.__front] = None
#         self.__front = (self.__front + 1 ) % len(self.__data)
#         self.__size -= 1
#         return element
#     def enqueue(self,e):
#         if self.__size == len(self.__data):
#             self.resize(self.__size * 2)
#         avail = (self.__front + self.__size) % len(self.__data)
#         self.__data[avail] = e
#         self.__size += 1
        
#     def first(self):
#         if self.__size == 0 :
#             raise EmptyError
#         return self.__data[self.__front]
#     def last(self):
#         if self.is_empty():
#             raise 
#         return self.__data[(self.__front + self.__size -1 ) % len(self.__data)]
#     def resize(self,cav):
#         walk = self.__front
#         old = self.__data
#         self.__data = [None] * cav
#         for k in self.__size:
#             self.__data[k] = old[walk]
#             walk = (walk + 1 ) % len(self.__data)
#         self.__front = 0 
# q = ArrayQueue()

# # q.enqueue(10)
# # q.enqueue(20)
# # q.enqueue(30)
# # print(q.first())
# # print(q.last())
# # print(q.dequeue())
# # print(q.dequeue())

# class LinkedList:
#     def __init__(self) :
#         self.__head = None
#         self.__size = 0
#     def is_empty(self):
#         return self.__size == 0
#     def len(self):
#         return self.__size
#     def front(self):
#         if self.is_empty():
#             raise EmptyError
#         return self.__head._element
#     def push(self,e):
#         node = Node(e,self.__head)
#         if self.__size == 0:
#             self.__head = node
#         else:
#             self.__head._next = node
#         self.__size += 1
#     def pop(self):
#         if self.is_empty():
#             raise EmptyError
#         old = self.__head._element
#         self.__head = self.__head._next
#         self.__size += 1
#         return old


# l = LinkedList()
# l.push(10)
# l.push(20)
# l.push(30)
# while l.front():
#     print(l.pop()) 

# def 



def power_set(s):
    power_set = set()
    elements 