from double_linked_base import _DoubleLinkedBase
from circular_queue import EmptyError

class LinkedDeque(_DoubleLinkedBase):
    # return the element in the front of the Deque 
    def first(self):
        if self.is_empty():
            raise EmptyError("Deque is Empty")
        return self._header._next._element
    def last(self):
        if self.is_empty():
            raise EmptyError("Deque is Empty")
        return self._trailer._prev._element
    def insert_first(self,e):
        return self.insert_between(e,self._header , self._header._next)
    def insert_last(self,e):
        return self.insert_between(e,self._trailer._prev,self._trailer)
    def delete_first(self):
        if self.is_empty():
            raise EmptyError("Deque is Empty")
        return self._delete_node(self._header._next)
    def delete_last(self):
        if self.is_empty():
            raise EmptyError("Deque is Empty")
        return self._delete_node(self._trailer._prev)

def main():
    D = LinkedDeque()
    D.insert_last(5) 
    D.insert_first(3) 
    D.insert_first(7) 
    print(D.len())  # outputs 3

    # contents: [7, 3, 5]
    print(D.first())  # outputs 7

    # contents: [7, 3, 5]
    print(D.delete_last())  # outputs 5

    # contents: [7, 3]
    print(D.last())  # outputs 3

    print(D.len())  # outputs 2

    # contents: [7, 3]
    print(D.delete_last())  # outputs 3

    # contents: [7]
    print(D.delete_last())  # outputs 7

    # contents: []
    print(D.is_empty())  # outputs True

    D.insert_first(6)

    # contents: [6]
    print(D.last())  # outputs 6

    D.insert_first(8)

    # contents: [8, 6]
    print(D.is_empty())  # outputs False

    print(D.last())  # outputs 6

    print(D.delete_first())  # outputs 8

    # contents: [6]
    print(D.first())  # outputs 6
if __name__ == "__main__":
    main()