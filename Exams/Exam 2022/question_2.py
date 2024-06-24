
#! II) 
# 1- Define TERMS : 
# A) Singly Linked List 
"""
Singly Linked List :  in its simplest form, is a collection of 
nodes that collectively form a linear sequence. 
◼ Each node stores:
 ❑ a reference to an object that is an elementof the 
sequence, 
❑ a reference to the next node of the list
"""
# B) Double lInked List 

"""
Header and trailer sentinels are special nodes placed at the beginning and end of a
 doubly linked list, serving as placeholders without 
 storing actual data, thus enabling unified and simplified operations across the list.
 
 """
# _______________________________________
#! 2- 
#! Create Double linked List class

#! Double linked Base

class EmptyError(Exception):
    pass
class DoubleLinkedList:
    class _Node:
        __slots__ = "_element", "_next", "_prev"

        def __init__(self, element, prev, next):
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail  # trailer is after header
        self._tail._prev = self._head  # header is before trailer
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
        return element # return Deleted Element
    def add_last(self,e):
        return self.insert_between(e,self._tail._prev , self._tail)
    def iter(self):
        if self.is_empty():
            return None
        current = self._head._next
        while current._next._next:
            yield current
            current = current._next
        yield current # for tail
    def remove_first(self):
        return self._delete_node(self._head._next)

#! Testing دي مش تبع  الاجابة 
# D = DoubleLinkedList()

# for i in range(10):
#     D.add_last(i)

# print(D.len())

# for i in D.iter():
#     print(i._element , end=" ")
# D.remove_first()
# D.remove_first()

# print("\nAfter Delete : ")

# for i in D.iter():
#     print(i._element , end=" ")