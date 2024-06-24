class EmptyError(Exception):
    pass    
class SingleLinkedList:
    class _Node:
        __slots__= '_element' , '_next'
        def __init__(self,e,next) -> None:
            self._element = e 
            self._next = next
    def __init__(self):
        self._head = None
        self._size = 0 
    def len(self):
        return self._size
    def first(self):
        if self.is_empty():
            raise EmptyError("Empty Linked List")
        return self._head._element
    def is_empty(self):
        return self._size == 0 
    def insert_before(self,e1,e2):
        current = self._head
        prev = self._head
        while current:
            if current._element == e1 :
                old = prev._next
                prev._next = self._Node(e2,old)
                self._size += 1
            prev = current
            current = current._next
    def remove_last(self):
        if self.is_empty():
            raise EmptyError("Empty Linked List")
        if self._size == 1 :
            element = self._head._element
            self._head = None
            self._size -= 1
            return element
        current = self._head
        prev = self._head
        while current:
            if current._next is None:
                break
            prev = current
            current = current._next
        prev._next = None
        self._size -= 1
        return prev._element
    def display(self):
        current = self._head
        while current:
            print(current._element)
            current = current._next

#! just for testing مش تبع الاجابة 
# S = SingleLinkedList()
# S._head = S._Node(1,None)
# S._size = 1
# S.insert_before(S.first(),10)
# S.insert_before(S.first(),20)
# S.insert_before(S.first(),30)
# S.display()
# S.remove_last()
# S.remove_last()
# S.remove_last()
# S.display()
# S.remove_last()
# S.display()

#!___________________________

# 2- using sets 
def vowel_count(txt):
    s = {'a','e','i','o','u'}
    count = 0 
    for c in txt:
        if c in s:
            count += 1
    return count