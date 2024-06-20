class EmptyError(Exception):
    pass
class LinkedQueue:
    class _Node:
        __slots__= '_element' , '_next'
        def __init__(self,e,next):
            self._element = e
            self._next = next
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0 
    def len(self):
        return self._size
    def is_empty(self):
        return self._size == 0 
    def first(self):
        if self.is_empty():
            raise EmptyError("The Linked Queue is Empty")
        return self._head._element
    def last(self):
        if self.is_empty():
            raise EmptyError("The Linked Queue is Empty")
        return self._tail._element
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
            raise EmptyError("The Linked Queue is Empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
# def main():
#     Q = LinkedQueue()
#     Q.enqueue(5)        # contents: [5]
#     Q.enqueue(3)        # contents: [5, 3]
#     print(Q.len())      # contents: [5, 3]; outputs 2
#     print(Q.dequeue())  # contents: [3]; outputs 5
#     print(Q.is_empty()) # contents: [3]; outputs False
#     print(Q.dequeue())  # contents: [ ]; outputs 3
#     print(Q.is_empty()) # contents: [ ]; outputs True
#     Q.enqueue(7)        # contents: [7]
#     Q.enqueue(9)        # contents: [7, 9]
#     print(Q.first())    # contents: [7, 9]; outputs 7
#     Q.enqueue(4)        # contents: [7, 9, 4]
#     print(Q.len())      # contents: [7, 9, 4]; outputs 3
#     print(Q.dequeue())  # contents: [9, 4]; outputs 7
# if __name__ == '__main__':
#     main()
