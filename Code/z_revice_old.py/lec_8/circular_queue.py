class EmptyError(Exception):
    pass
class CircularQueue:
    class _Node:
        __slots__= '_element' , '_next' 
        def __init__(self,e,next):
            self._element = e
            self._next = next
    def __init__(self):
        self._tail = None
        self._size = 0
    def len(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty():
            raise EmptyError("Circular Queue is Empty")
        return self._tail._next._element
    def enqueue(self,e):
        newest = self._Node(e,None)
        if self.is_empty():
            newest._next = newest # initialize circulary
        else:
            newest._next = self._tail._next # new node points to head 
            self._tail._next = newest # old node points to new node
        self._tail = newest
        self._size += 1
    def dequeue(self):
        if self.is_empty():
            raise EmptyError("Circular Queue is Empty")
        old = self._tail._next
        if self._size == 1 :
            self._tail = None
        else:
            self._tail._next = old._next
        self._size -= 1 
        return old._element
    def rotate(self):
        if self._size > 0 :
            self._tail = self._tail._next
def main():
 Q = CircularQueue()
 Q.enqueue(5)        # contents: [5]
 Q.enqueue(3)        # contents: [5, 3]
 print(Q.len())      # contents: [5, 3]; outputs 2
 print(Q.dequeue())  # contents: [3]; outputs 5
 print(Q.is_empty()) # contents: [3]; outputs False
 print(Q.dequeue())  # contents: [ ]; outputs 3
 print(Q.is_empty()) # contents: [ ]; outputs True
 Q.enqueue(7)        # contents: [7]
 Q.enqueue(9)        # contents: [7, 9]
 print(Q.first())    # contents: [7, 9]; outputs 7
 Q.enqueue(4)        # contents: [7, 9, 4]
 print(Q.len())      # contents: [7, 9, 4]; outputs 3
 Q.rotate()             # contents: [9, 4, 7]
 print(Q.first())       # contents: [9, 4, 7]; outputs 9
 Q.rotate()             # contents: [4, 7, 9]
 print(Q.first())       # contents: [4, 7, 9]; outputs 4 
 print(Q.dequeue())  # contents: [7, 9]; outputs 4
if __name__ == '__main__':
    main()