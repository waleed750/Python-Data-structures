class EmptyError(Exception):
    pass
class _DoubleLinkedBase:
    class _Node:
        __slots__ = "_element", "_next", "_prev"

        def __init__(self, element, prev, next):
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer  # trailer is after header
        self._trailer._prev = self._header  # header is before trailer
        self._size = 0  # number of elements

    def len(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insert_between(self, e, predessor, successor):
        newest = self._Node(e, predessor, successor)  # linked to Neighbours
        predessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node: _Node):
        if self.is_empty():
            raise EmptyError("Double linked List is Empty")
        predessor = node._prev
        succesor = node._next
        predessor._next = succesor
        succesor._prev = predessor
        element = node._element # record deleted ELement 
        node._element = node._next = node._prev = None # deprecte node 
        self._size -= 1
        return element
class DoubleLinkedStack(_DoubleLinkedBase):
    def top(self):
        if self.is_empty():
            raise EmptyError("Empty DoubleLinkedStack")
        return self._header._next._element
    def push(self,e):
        return self.insert_between(e,self._header,self._header._next)
    def pop(self):
        return self._delete_node(self._header._next)
    def display(self):
        current = self._trailer._prev
        while current._prev:
            print(current._element)
            current = current._prev

#! __testing 
# ds = DoubleLinkedStack()
# d10 = ds.push(10)
# d20 = ds.push(20)
# d30 = ds.push(30)
# print(f"Top : {ds.top()}")
# print(f"Size : {ds.len()}")
# ds.display()
# ds.pop()
# print(f"Top : {ds.top()}")
# print(f"Size : {ds.len()}")
# ds.display()

class LinkedQueue(_DoubleLinkedBase):
    def first(self):
        return self._header._next._element
    def enqueue(self, e):
        return self.insert_between(e,self._trailer._prev,self._trailer)
    def dequeue(self):
        return self._delete_node(self._header._next)
    def display(self):
        current = self._header._next
        while current._next:
            print(current._element)
            current = current._next
#!__ Testing 
# print(f"{"_"*20} Double Linked Queue {"_"*20}")
# dq = LinkedQueue()
# dq.enqueue(10)
# dq.enqueue(20)
# dq.enqueue(30)
# print(f"Size : {dq.len()}")
# dq.display()
# print("Deleted : ",dq.dequeue())
# print("First : ",dq.first())
# print("Deleted : ",dq.dequeue())
# print("First : ",dq.first())
# print("Deleted : ",dq.dequeue())
# print(f"Size : {dq.len()}")
# dq.display()
#! 7.5 

#! 7.6
class CircularQueue:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next
    def __init__(self):
        self._tail = None
        self._size = 0
    def len(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty() :
            newest._next = newest
        else:
            newest._next =self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        return newest
    def dequeue(self):
        if self.is_empty():
            raise EmptyError("Empty CircularQueue")
        old = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = old._next
        self._size -= 1
        return old._element
    def first(self):
        if self.is_empty():
            raise EmptyError("Empty CircularQueue")
        return self._tail._next._element
    def display(self):
        if self.is_empty():
            raise EmptyError("Empty CircularQueue")
        current = self._tail._next
        while current != self._tail:
            print(current._element)
            current = current._next
        print(current._element) # to print the tail element
# c = CircularQueue()
# c.enqueue("A")
# c.enqueue("B")
# c.enqueue("C")
# print("First : ",c.first())
# c.display()
# print(f"Size : {c.len()}")
# print("Deleted : ",c.dequeue())
# print("First : ",c.first())
# print("Deleted : ",c.dequeue())
# print("First : ",c.first())
# print("Deleted : ",c.dequeue())


