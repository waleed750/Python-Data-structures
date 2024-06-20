# __________________________________________LinkidList__________________________________________


#! Singly LinkidList
class EmptyError(Exception):
    pass


class Node:
    __slots__ = ("_element", "_next")

    def __init__(self, element, next):
        self._element = element
        self._next = next


class LinkidList:  # Node -> Next Head  - Size - is_empty - addLast - addFirst - removeFirst
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def len(self):
        return self.__size

    def addFirst(self, e):
        node = Node(e, None)
        node._next = self.__head
        self.__head = node
        self.__size += 1
        if self.__tail is None:
            self.__tail = node

    def addLast(self, e):
        node = Node(e, None)
        if self.is_empty():
            self.__head = self.__tail = node
        else:
            self.__tail._next = node
            self.__tail = node
        self.__size += 1

    def removeFirst(self):
        if self.is_empty():
            raise EmptyError
        oldHead = self.__head
        self.__head = oldHead._next
        if self.__head is None:
            self.__tail = None
        self.__size -= 1
        return oldHead._element

    def printValues(self):
        current = self.__head
        while current != None:
            print(current._element, end=" -> ")
            current = current._next
        print("None")


# s =LinkidList()
# s.addFirst("moh")
# s.printValues()

#!===================== Singly LinkedStack =====================================


class LinkedStack:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def len(self):
        return self.__size

    def push(self, e):
        node = Node(e, self.__head)
        self.__head = node
        self.__size += 1

    def pop(self):
        if self.is_empty():
            raise EmptyError
        oldHead = self.__head._element
        self.__head = self.__head._next
        self.__size += 1
        return oldHead


#!===================== Singly LinkedQueue =====================================
class LinkedQueue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def len(self):
        return self.__size

    def first(self):
        return self.__head._element

    def dequeue(self):
        if self.is_empty():
            raise EmptyError
        oldHead = self.__head
        self.__head = oldHead._next
        self.__size -= 1
        if self.is_empty():
            self.__tail = None
        return oldHead._element

    def enqueue(self, e):
        newest = Node(e, None)
        if self.is_empty():
            self.__head = self.__tail = newest
        else:
            self.__tail._next = newest
        self.__tail = newest
        self.__size += 1

    def printValues(self):
        current = self.__head
        while current != None:
            print(current._element, end=" -> ")
            current = current._next
        print("None")


# Q = LinkedQueue()
# Q.enqueue(5)
# Q.enqueue(3)


#!===================== Circular LinkedList =====================================
class CircularQueue:
    class Node:
        __slots__ = (
            "_element",
            "_next",
        )

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self.__tail = None
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def len(self):
        return self.__size

    def first(self):
        if self.is_empty():
            raise EmptyError
        head = self.__tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise EmptyError
        oldHead = self.__tail._next
        if self.__size == 1:
            self.__tail = None
        else:
            self.__tail = oldHead._next
        self.__size -= 1
        return oldHead._element

    def enqueue(self, e):
        newest = self.Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self.__tail._next
            self.__tail._next = newest
        self.__tail = newest
        self.__size += 1

    def rotate(self):
        if self.__size > 0:
            self.__tail = self.__tail._next


# Q = CircularQueue()
# Q.enqueue(5)        # contents: [5]
# Q.enqueue(3)        # contents: [5, 3]


class _Node:
    """Lightweight, nonpublic class for storing a doubly linked
    node."""

    __slots__ = "_element", "_prev", "_next"  # streamline memory

    def __init__(self, element, prev, next):  # initialize node’s fields
        self._element = element  # user’s element
        self._prev = prev  # previous node reference
        self._next = next  # next node reference


class _DoublyLinkedBase:
    def __init__(self):
        self._header = _Node(None, None, None)
        self._tailer = _Node(None, None, None)
        self._header._next = self._tailer
        self._tailer._prev = self._header
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def len(self):
        return self._size

    def _insert_between(self, e, predecessor, sucessor):

        newest = _Node(e, predecessor, sucessor)
        predecessor._next = newest
        sucessor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        if self.is_empty():
            raise EmptyError
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element  # record deleted element
        node._prev = node._next = node._element = None  # deprecate node
        return element


class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise EmptyError
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise EmptyError
        return self._tailer._prev._element

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)  # after header

    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._tailer._prev, self._tailer)  # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque.
        Raise Empty exception if the dequeis empty."""
        if self.is_empty():
            raise EmptyError("Dequeis empty")
        return self._delete_node(self._header._next)  # use inherited method

    def delete_last(self):
        """Remove and return the element from the back of the deque.
        Raise Empty exception if the dequeis empty."""
        if self.is_empty():
            raise EmptyError("Dequeis empty")
        return self._delete_node(self._trailer._prev)  # use inherited method


D = LinkedDeque()
D.insert_last(5) 
D.insert_first(3) 
D.insert_first(7) 

while not D.is_empty():
        print(D.delete_first())
# contents: [7, 3, 5]; 