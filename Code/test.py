# # # __________________________________________LinkidList__________________________________________


# # #! Singly LinkidList
# # class EmptyError(Exception):
# #     pass


# # class Node:
# #     __slots__ = ("_element", "_next")

# #     def __init__(self, element, next):
# #         self._element = element
# #         self._next = next


# # class LinkidList:  # Node -> Next Head  - Size - is_empty - addLast - addFirst - removeFirst
# #     def __init__(self):
# #         self.__head = None
# #         self.__tail = None
# #         self.__size = 0

# #     def is_empty(self):
# #         return self.__size == 0

# #     def len(self):
# #         return self.__size

# #     def addFirst(self, e):
# #         node = Node(e, None)
# #         node._next = self.__head
# #         self.__head = node
# #         self.__size += 1
# #         if self.__tail is None:
# #             self.__tail = node

# #     def addLast(self, e):
# #         node = Node(e, None)
# #         if self.is_empty():
# #             self.__head = self.__tail = node
# #         else:
# #             self.__tail._next = node
# #             self.__tail = node
# #         self.__size += 1

# #     def removeFirst(self):
# #         if self.is_empty():
# #             raise EmptyError
# #         oldHead = self.__head
# #         self.__head = oldHead._next
# #         if self.__head is None:
# #             self.__tail = None
# #         self.__size -= 1
# #         return oldHead._element

# #     def printValues(self):
# #         current = self.__head
# #         while current != None:
# #             print(current._element, end=" -> ")
# #             current = current._next
# #         print("None")


# # # s =LinkidList()
# # # s.addFirst("moh")
# # # s.printValues()

# # #!===================== Singly LinkedStack =====================================


# # class LinkidStack:
# #     def __init__(self):
# #         self.__head = None
# #         self.__size = 0

# #     def is_empty(self):
# #         return self.__size == 0

# #     def len(self):
# #         return self.__size

# #     def push(self, e):
# #         node = Node(e, self.__head)
# #         self.__head = node
# #         self.__size += 1

# #     def pop(self):
# #         if self.is_empty():
# #             raise EmptyError
# #         oldHead = self.__head._element
# #         self.__head = self.__head._next
# #         self.__size += 1
# #         return oldHead


# # #!===================== Singly LinkedQueue =====================================
# # class LinkedQueue:
# #     def __init__(self):
# #         self.__head = None
# #         self.__tail = None
# #         self.__size = 0

# #     def is_empty(self):
# #         return self.__size == 0

# #     def len(self):
# #         return self.__size

# #     def first(self):
# #         return self.__head._element

# #     def dequeue(self):
# #         if self.is_empty():
# #             raise EmptyError
# #         oldHead = self.__head
# #         self.__head = oldHead._next
# #         self.__size -= 1
# #         if self.is_empty():
# #             self.__tail = None
# #         return oldHead._element

# #     def enqueue(self, e):
# #         newest = Node(e, None)
# #         if self.is_empty():
# #             self.__head = self.__tail = newest
# #         else:
# #             self.__tail._next = newest
# #         self.__tail = newest
# #         self.__size += 1

# #     def printValues(self):
# #         current = self.__head
# #         while current != None:
# #             print(current._element, end=" -> ")
# #             current = current._next
# #         print("None")


# # # Q = LinkedQueue()
# # # Q.enqueue(5)
# # # Q.enqueue(3)


# # #!===================== Circular LinkedList =====================================
# # class CircularQueue:
# #     class Node:
# #         __slots__ = (
# #             "_element",
# #             "_next",
# #         )

# #         def __init__(self, element, next):
# #             self._element = element
# #             self._next = next

# #     def __init__(self):
# #         self.__tail = None
# #         self.__size = 0

# #     def is_empty(self):
# #         return self.__size == 0

# #     def len(self):
# #         return self.__size

# #     def first(self):
# #         if self.is_empty():
# #             raise EmptyError
# #         head = self.__tail._next
# #         return head._element

# #     def dequeue(self):
# #         if self.is_empty():
# #             raise EmptyError
# #         oldHead = self.__tail._next
# #         if self.__size == 1:
# #             self.__tail = None
# #         else:
# #             self.__tail = oldHead._next
# #         self.__size -= 1
# #         return oldHead._element

# #     def enqueue(self, e):
# #         newest = self.Node(e, None)
# #         if self.is_empty():
# #             newest._next = newest
# #         else:
# #             newest._next = self.__tail._next
# #             self.__tail._next = newest
# #         self.__tail = newest
# #         self.__size += 1

# #     def rotate(self):
# #         if self.__size > 0:
# #             self.__tail = self.__tail._next


# # # Q = CircularQueue()
# # # Q.enqueue(5)        # contents: [5]
# # # Q.enqueue(3)        # contents: [5, 3]


# # class _Node:
# #     """Lightweight, nonpublic class for storing a doubly linked
# #     node."""

# #     __slots__ = "_element", "_prev", "_next"  # streamline memory

# #     def __init__(self, element, prev, next):  # initialize node’s fields
# #         self._element = element  # user’s element
# #         self._prev = prev  # previous node reference
# #         self._next = next  # next node reference


# # class _DoublyLinkedBase:
# #     def __init__(self):
# #         self._header = _Node(None, None, None)
# #         self._tailer = _Node(None, None, None)
# #         self._header._next = self._tailer
# #         self._tailer._prev = self._header
# #         self.__size = 0

# #     def is_empty(self):
# #         return self.__size == 0

# #     def len(self):
# #         return self.__size

# #     def _insert_between(self, e, predecessor, sucessor):

# #         newest = _Node(e, predecessor, sucessor)
# #         predecessor._next = newest
# #         sucessor._prev = newest
# #         self.__size += 1
# #         return newest

# #     def _delete_node(self, node):
# #         if self.is_empty():
# #             raise EmptyError
# #         predecessor = node._prev
# #         successor = node._next
# #         predecessor._next = successor
# #         successor._prev = predecessor
# #         self.__size -= 1
# #         element = node._element  # record deleted element
# #         node._prev = node._next = node._element = None  # deprecate node
# #         return element


# # class LinkedDeque(_DoublyLinkedBase):
# #     def first(self):
# #         if self.is_empty():
# #             raise EmptyError
# #         return self._header._next._element

# #     def last(self):
# #         if self.is_empty():
# #             raise EmptyError
# #         return self._tailer._prev._element

# #     def insert_first(self, e):
# #         """Add an element to the front of the deque."""
# #         self._insert_between(e, self._header, self._header._next)  # after header

# #     def insert_last(self, e):
# #         """Add an element to the back of the deque."""
# #         self._insert_between(e, self._tailer._prev, self._tailer)  # before trailer

# #     def delete_first(self):
# #         """Remove and return the element from the front of the deque.
# #         Raise Empty exception if the dequeis empty."""
# #         if self.is_empty():
# #             raise EmptyError("Dequeis empty")
# #         return self._delete_node(self._header._next)  # use inherited method

# #     def delete_last(self):
# #         """Remove and return the element from the back of the deque.
# #         Raise Empty exception if the dequeis empty."""
# #         if self.is_empty():
# #             raise EmptyError("Dequeis empty")
# #         return self._delete_node(self._tailer._prev)  # use inherited method


# # D = LinkedDeque()
# # D.insert_last(5)
# # D.insert_first(3)
# # D.insert_first(7)

# class Node:
#     __slots__ = "_element" , "_next"
#     def __init__(self,element,next) :
#         self._element = element
#         self._next = next
# class EmptyError(Exception):
#     pass

# class SinglyLinkedStack : # Last-in-First-out => Head
#     def __init__(self) -> None:
#         self.__head = None
#         self.__size = 0
#     def is_empty(self):
#         return self.__size == 0
#     def len(self):
#         return self.__size
#     def first(self):
#         if self.is_empty():
#             raise EmptyError
#         return self.__head._element
#     def add_first(self,e):
#         newest = Node(e,self.__head)
#         self.__head = newest
#         self.__size +=1

#     def add_last(self, element):
#         new_node = Node(element,None)  # Create a new node
#         if self.is_empty():
#             self.__head = new_node  # If empty, head points to new node
#         else:
#             current = self.__head
#             while current._next != None:
#                 current = current._next
#             current._next = new_node
#         self.__size += 1  # Increment size
#     def remove_last(self):
#         if self.is_empty():
#             raise EmptyError
#         if self.__size == 1 :
#             old = self.__head._element
#             self.__head = None
#             self.__size -= 1
#             return old
#         else:
#             current = self.__head
#             while current._next._next is None:
#                 current = current._next
#             old = current._next
#             current._next = None
#             self.__size -= 1
#             return old._element

#     def remove_first(self):
#         if self.is_empty():
#             raise EmptyError
#         removed_element = self.__head._element
#         self.__head = self.__head._next
#         self.__size -= 1
#         return removed_element

#     def display(self):
#         elements = []
#         current = self.__head
#         while current != None:
#             elements.append(current._element)
#             current = current._next
#         return elements
#     def contains(self,e):
#         current  = self.__head
#         while current._next != None:
#             if current._element == e :
#                 return True
#             current = current._next
#         return False
#     def insert_before(self,target,new_element):
#         if self.is_empty():
#             raise EmptyError
#         if self.__head._element == target:
#             self.add_first(new_element)
#             return
#         current = self.__head
#         while current._next:
#             if current._next._element == target:
#                 new_node = Node(new_element, current._next)
#                 current._next = new_node
#                 self.__size += 1
#                 break
#             current = current._next
#     def insert_after(self,target,new_element):
#         if self.is_empty():
#             raise EmptyError
#         current = self.__head
#         while current:
#             if current._element == target:
#                 new_element = Node(new_element,current._next)
#                 current._next = new_element
#                 self.__size +=1
#                 return
#             current = current._next
#         raise Exception("Not found")
#     def remove_item(self,item):
#         if self.is_empty():
#             raise EmptyError
#         current = self.__head
#         if current._element == item:
#             self.__head = self.__head._next
#             return current._element
#         while current._next:
#             if current._next._element == item:
#                 removed_item = current._next._element
#                 current._next = current._next._next
#                 self.__size -= 1
#                 return removed_item
#             current = current._next
#         raise Exception("Not Found")

#     def concatLists(list1,list2):
#         result = list1.display() + list2.display()
#         return result

# # linked_list = SinglyLinkedStack()
# # linked_list.add_first(10)  # List: 10
# # linked_list.add_first(20)  # List: 20 -> 10
# # linked_list.add_first(30)  # List: 30 -> 20 -> 10

# # print(linked_list.display())
# # linked_list.add_last(50)
# # linked_list.add_last(65)
# # # print(linked_list.len())
# # # print(linked_list.display())

# # # linked_list.remove_item(50)
# # # print(linked_list.display())

# # linked_list2 = SinglyLinkedStack()
# # linked_list2.add_first(10)  # List: 10
# # linked_list2.add_first(20)  # List: 20 -> 10
# # linked_list2.add_first(30)  # List: 30 -> 20 -> 10

# # l = SinglyLinkedStack.concatLists(linked_list,linked_list2)
# # print(l)


# #! CircularLinkedList

# class Node:
#     __slots__ = ("_element", "_next")

#     def __init__(self, element, next):
#         self._element = element
#         self._next = next
# class CircularLinkedList:
#     def __init__(self):
#         self.__tail = None
#         self.__size = 0
#     def len(self):
#         return self.__size
#     def is_empty(self):
#         return self.__size == 0
#     def first(self):
#         if self.is_empty():
#             raise EmptyError
#         return self.__tail._next._element
#     def last(self):
#         if self.is_empty():
#             raise EmptyError
#         return self.__tail._element

#     def remove(self):
#         if self.is_empty():
#             raise EmptyError
#         removed_element = self.__tail._element
#         if self.__size == 1 :
#             self.__tail = None
#         else:
#             self.__tail = self.__tail._next

#         self.__size -= 1
#         return removed_element
#     def add(self,e):
#         newset = Node(e,None)
#         if self.__size == 0 :
#             self.__tail = newset
#         else:
#             old self._tail
#             self.__tail = newset
#         self.__size += 1

# c = CircularLinkedList()
# c.add(10)
# c.add(20)
# c.add(30)
# print(c.first())
# try:
#     while True:
#         print(c.remove())
# except EmptyError:
#     print("")


#! Excersice 5
class EmptyError:
    pass


# PartA
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
            raise EmptyError("The stack is empty")
        else:
            return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise EmptyError("The stack is empty")
        else:
            return self._data.pop()


def is_matched(txt):
    lefty = "({["
    righty = ")}]"
    S = ArrayStack()

    # Iterate through each character in the text
    for c in txt:
        if c in lefty:
            S.push(c)  # Push opening brackets onto the stack
        elif c in righty:
            if (
                S.is_empty()
            ):  # If a closing bracket is found with no matching opening bracket
                return False
            popped = S.pop()
            # Check if the popped opening bracket matches the current closing bracket
            if righty.index(c) != lefty.index(popped):
                return False

    # If stack is empty, all brackets have been matched correctly
    return S.is_empty()


# txt = "[(5+x)-(y+z)]"
# print(is_matched("((2 + 3) * 5)"))  # Output: True
# print(is_matched("[(2 + 3)] * 5"))  # Output: True
# print(is_matched("[(2 + 3] * 5)"))  # Output: False
# print(is_matched("2 + 3 * 5)"))  # Output: False
# print(is_matched("[(5+x)-(y+z)]"))  # Output: True

# print(is_matched(txt))


def infix_To_Posfix(expr):
    lefty = "({["
    righty = ")}]"
    operators = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
    }
    postifix = []
    numbers = list(range(0, 10))
    S = ArrayStack()
    for c in expr:
        if c.isnumeric():
            postifix.append(c)
        elif c in lefty:
            S.push(c)
        elif c in righty:
            while not S.is_empty() and S.top() not in lefty:
                postifix.append(S.pop())
            S.pop()
        else:
            while (
                not S.is_empty()
                and S.top() in operators
                and operators[S.top()] >= operators[c]
            ):
                postifix.append(S.pop())
            S.push(c)
    while not S.is_empty():
        postifix.append(S.pop())
    return "".join(postifix)


def Evaluate_Postfix(expr):
    result = 0
    S = ArrayStack()
    operators = ["+", "-", "/", "*"]
    for c in expr:
        if c.isnumeric():
            S.push(c)
        elif c in operators:
            n2 = int(S.pop())
            n1 = int(S.pop())
            result = eval(f"{n1} {c} {n2}")
            S.push(result)
    return S.pop()


# infix_expr = "( 6 - ( 2 + 3 ) ) * ( 3 + 8 / 2 ) + 2".replace(" ","")
# result = infix_To_Posfix(infix_expr)
# print(result)

# print(Evaluate_Postfix(result))

pair_list = [(6, 7), (2, 3), (7, 6)]

# pairs = set()
# for i in pair_list:
#     reversed_list = (i[1], i[0])
#     if reversed_list in pair_list:
#         if reversed_list not in pairs and i not in pairs:
#             pairs.add(i)
# print(pairs)

def power_set_recursive(s):
    if len(s) == 0:
        return [set()]

    # Get the first element and the rest of the set
    first_element = s.pop()
    # Get the power set of the rest of the set
    rest_power_set = power_set_recursive(s)

    # Create subsets with and without the first element
    subsets_with_first = [subset | {first_element} for subset in rest_power_set]

    # Combine subsets with and without the first element
    return rest_power_set + subsets_with_first

def power_set_iterative(s):
    stack = []
    result = [set()]  # Start with the empty set

    # Initialize the stack with the given set
    stack.append(s)

    while stack:
        current_set = stack.pop()  # Pop the last set from the stack

        if len(current_set) == 0:
            continue  # If the set is empty, continue to the next iteration

        # Get the first element and the rest of the set
        first_element = current_set.pop()

        # Add the current set to the result as a subset with the first element
        subsets_with_first = [subset | {first_element} for subset in result]

        # Add the new subsets to the result
        result += subsets_with_first

        # Push the current set back to the stack to process further
        stack.append(current_set)

    return result
        
txt = "I am Waleed Ashraf one of the most fastest and smartest ones but I have some issues hope to fix them"

s = set(txt.split(" "))

print(sorted(list(s)))