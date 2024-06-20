class EmptyError(Exception):
    pass
class ArrayDeque:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0 
    def len(self):
        return self._size
    def is_empty(self):
        return self._size == 0 
    def first(self):
        if self.is_empty():
            raise EmptyError("Empty Deque")
        return self._data[self._front]
    def last(self):
        if self.is_empty():
            raise EmptyError("Empty Deque")
        back = (self._front + self._size -1 ) % len(self._data)
        return self._data[back]
    def add_last(self,e): # enque
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1 
    def add_first(self,e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1
    def delete_first(self):
        if self.is_empty():
            raise EmptyError("Empty Deque")
        old = self._data[self._front]
        self._data[self._front] = None # help garbage collector
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return old
    def delete_last(self):
        if self.is_empty():
            raise EmptyError("Empty Deque")
        back = (self._front + self._size - 1)  % len(self._data) 
        old = self._data[back]
        self._data[back] = None # help garbage Collector
        self._size -= 1
        return old 
    def _resize(self,cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in self._size:
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0
    def elements(self):
        print("Deque Elements : ",end=" ")
        walk = self._front
        for _ in range(self._size):
            e = self._data[walk]
            walk = (walk + 1) % len(self._data)
            print(e , end=" ")
        print()
d = ArrayDeque()
d.add_last(5)
d.add_first(3)
d.add_first(7)
d.elements()
print(f"First : {d.first()} , Last : {d.last()}")
print(d.len())
print(f"Deleted : {d.delete_last()}")
d.elements()
d.add_first(6)
print(f"After Adding  ")
print('*'*10)
d.elements()
print('*'*10)
print(d.last())
d.add_first(8)
print(d.is_empty())
print(d.last())
