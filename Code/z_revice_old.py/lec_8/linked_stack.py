class EmptyError(Exception):
    pass
class LinkedStack:
    class _Node:
        __slots__ = '_element' , '_next'
        def __init__(self,e,next):
            self._element = e 
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
        """Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise EmptyError("Linked Stack is Empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
def main():
    S = LinkedStack()
    S.push(5) # contents: [5]
    S.push(3) # contents: [5, 3]
    print(S.len()) # contents: [5, 3]; outputs 2
    print(S.pop( )) # contents: [5]; outputs 3
    print(S.is_empty()) # contents: [5]; outputs False
    print(S.pop( )) # contents: [ ]; outputs 5
    print(S.is_empty()) # contents: [ ]; outputs True
    S.push(7) # contents: [7]
    S.push(9) # contents: [7, 9]
    print(S.top( )) # contents: [7, 9]; outputs 9
    S.push(4) # contents: [7, 9, 4]
    print(S.len()) # contents: [7, 9, 4]; outputs 3
    print(S.pop( )) # contents: [7, 9]; outputs 4
    S.push(6) # contents: [7, 9, 6]
# if __name__ == '__main__':
#     main()