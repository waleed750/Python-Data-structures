#! ArrayStack 
class EmptyError(Exception):
    pass
class ArrayStack:
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def top(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._data[-1]
    def push(self,value):
        self._data.append(value)
    def pop(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._data.pop()
    


def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    
    S = ArrayStack()

    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

# print(is_matched('[(5+x-(y+z)]'))
print(is_matched('[(5+x)-(y+z)]'))

    