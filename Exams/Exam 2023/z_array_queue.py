class EmptyError(Exception):
    pass
class ArrayQueue:
    DEFAULT_CAPCITY = 10
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPCITY
        self._front = 0
        self._size = 0 
    def len(self):
        return self._size
    def is_empty(self):
        return self._size == 0 
    def first(self):
        if self.is_empty():
            raise EmptyError("Queue is empty")
        return self._data[self._front]
    def dequeue(self):
        if self.is_empty():
            raise EmptyError("Empty Queueu")
        old = self._data[self._front]
        self._data[self._front] = None
        self._front  = (self._front + 1 ) % len(self._data)
        self._size -=1 
        return old
    def enqueue(self,e):
        if len(self._data) == self._size :
            self._resize(self._size ** 2)
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        

    def _resize(self,cap):
        old = self._data
        walk = self._front
        self._data = [None] * cap
        for k in self._size:
            self._data[k] = old[walk]
            walk = (walk + 1) % len(self._data)
        self._front = 0 