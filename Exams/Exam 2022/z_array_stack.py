class EmptyError(Exception):
    pass
class ArrayStack:
    def __init__(self):
        self._data = []
    def len(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0 
    def top(self):
        if self.is_empty():
            raise EmptyError("Stack is Empty")
        return self._data[-1]
    def push(self,e):
        self._data.append(e)
    def pop(self):
        if self.is_empty():
            raise EmptyError("Stack is Empty")
        return self._data.pop()
    