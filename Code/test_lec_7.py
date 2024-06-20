# class EmptyError(Exception):
#     pass

# class ArrayQueue:
#     DEFAULT_CAPACITY = 10
#     def __init__(self):
#         self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
#         self._front = 0 # index
#         self._size = 0
#     def len(self):
#         return self._size
#     def is_empty(self):
#         return self._size == 0
#     def first(self):
#         if self.is_empty():
#             raise EmptyError
#         return self._data[self._front]
#     def enqueue(self,e):
#         if self._size == len(self._data):
#             self.resize(2 * self._size * 2)
#         avail = (self._front + self._size) % len(self._data)
#         self._data[avail] = e
#         self._size += 1
#     def dequeue(self):
#         if self.is_empty():
#             raise EmptyError
#         answer = self._front
#         self._data[answer] = None
#         self._size -= 1
#         return self._data.pop()


# def main():
#     Q = ArrayQueue()
#     print(Q.enqueue(5))
#     print("len",Q.len() ,"front",Q.first())
#     print(Q.enqueue(3))
#     print("len",Q.len() ,"front",Q.first())
#     print(Q.len())
#     print("Dequeue",Q.dequeue())
#     print(Q.is_empty())
#     print("len",Q.len() ,"front",Q.first())
#     print("Dequeue",Q.dequeue())
#     print(Q.is_empty())
#     # print("Dequeue",Q.dequeue())
#     print(Q.enqueue(7))
#     print(Q.enqueue(9))
#     print(Q.first())
#     print(Q.enqueue(4))
#     print(Q.len())
#     print("Dequeue",Q.dequeue())

# if __name__ == "__main__":
#     main()


#! plaindrome
class EmptyError(Exception):
    pass


# ? ArrayQueue
class ArrayQueue:  # First in First Out
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def len(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def dequeue(self):
        if self.is_empty():
            raise EmptyError
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        # print(answer)
        return answer

    def first(self):
        if self.is_empty():
            raise EmptyError
        return self._data[self._front]

    def enqueue(self, e):
        if len(self._data) == self._size:
            self.resize(self._size * 2)
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, cav):
        old = self._data
        walk = self._front
        self._data = [None] * cav
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(self._data)
        self._front = 0


class ArrayStack:  # First in First out
    def __init__(self):
        self._data = []

    def len(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        return self._data[-1]

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            raise EmptyError
        # print("Popped : ", self._data[-1])
        return self._data.pop()


# while True:
#     S = ArrayStack()
#     Q = ArrayQueue()
#     txt = input("Enter txt for plainDrome : ").lower()
#     if txt == "q":
#         break
#     # Declare Each Word
#     for t in txt.split(" "):
#         for c in t:
#             S.push(c)
#             Q.enqueue(c)

#         isPlainDrome = True
#         for i in t:
#             if S.pop() != Q.dequeue():
#                 isPlainDrome = False
#                 break
#         print(f"isPlainDrome = {isPlainDrome}")

def is_palindrome(s):
    stack = ArrayStack()  # Stack for reverse order
    queue = ArrayQueue()  # Queue for forward order
    # Normalize the input by keeping only alphanumeric characters and converting to lowercase
    normalized_s = ''.join([c.lower() for c in s if c.isalnum()])

    # Populate the stack and queue
    for c in normalized_s:
        stack.push(c)
        queue.enqueue(c)

    # Check if the sequence is a palindrome
    still_palindrome = True
    while not stack.is_empty() and still_palindrome:
        stack_char = stack.pop()
        queue_char = queue.dequeue()
        if stack_char != queue_char:
            still_palindrome = False

    return still_palindrome

# print(is_palindrome("A man, a plan, a canal, Panama"))  # True
# print(is_palindrome("racecar"))  # True
# print(is_palindrome("hello"))

class ArrayDeque:
    DEFAULT_ARRAY_DEQUE = 10
    def __init__(self) -> None:
        self._data = [None] * ArrayDeque.DEFAULT_ARRAY_DEQUE 
        self._first = 0
        self._last = -1
        self._size = 0
    def is_empty(self):
        return self._size == 0 
    def add_last(self,value):
        self._last += 1  
        self._data[self._last] = value
        self._size += 1
    def add_first(self,value):
        old = self._data[self._first]
        self._first = (self._first + 1) % len(self._data)
        # self._data = 
    def first(self):
        if self.is_empty():
            raise EmptyError
        return self._data[self._first]
    def last(self):
        if self.is_empty():
            raise EmptyError
        return self._data[self._last]

D = ArrayDeque()
while True:
    print(eval(input(">>>")))

