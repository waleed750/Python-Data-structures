#! Double linked Base
from linked_queue import EmptyError


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
        return element # return Deleted Element
