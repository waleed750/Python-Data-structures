class ArrayStack:
    def __init__(self) :
        self._data = []
    def len(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0 
    def push(self,e):
        self._data.append(e)
    def pop(self):
        if self.is_empty():
            raise EmptyError("Empty Stack")
        return self._data.pop()
    def top(self):
        if self.is_empty():
            raise EmptyError("Empty Stack")
        return self._data[-1]
    
class EmptyError(Exception):
    pass
class ArrayQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self) -> None:
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._front = 0 
        self._size = 0 
    def len(self):
        return self._size
    def is_empty(self):
        return self._size == 0 
    def first(self):
        if self.is_empty():
            raise EmptyError("The Queue is Empty")
        return self._data[self._front]
    def dequeue(self):
        if self.is_empty():
            raise EmptyError("The Queue is Empty")
        old = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return old 
    def enqueue(self,e):
        if self._size == len(self._data) - 1:
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    def _resize(self,cap):
        old = self._data
        walk = self._front
        self._data = [None] * cap
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0 
    
# Q = ArrayQueue()
# Q.enqueue(5)        # contents: [5]
# Q.enqueue(3)        # contents: [5, 3]
# print(Q.len())      # contents: [5, 3]; outputs 2
# print(Q.dequeue())  # contents: [3]; outputs 5
# print(Q.is_empty()) # contents: [3]; outputs False
# print(Q.dequeue())  # contents: [ ]; outputs 3
# print(Q.is_empty()) # contents: [ ]; outputs True
# Q.enqueue(7)        # contents: [7]
# Q.enqueue(9)        # contents: [7, 9]
# print(Q.first())    # contents: [7, 9]; outputs 7
# Q.enqueue(4)        # contents: [7, 9, 4]
# print(Q.len())      # contents: [7, 9, 4]; outputs 3
# print(Q.dequeue())  # contents: [9, 4]; outputs 7

def is_palindrome(s):
    stack = ArrayStack()
    queue = ArrayQueue()

    # Normalize the input and fill the stack and queue
    for char in s:
        if char.isalpha():  # Consider only alphabetic characters
            char = char.lower()
            stack.push(char)
            queue.enqueue(char)

    still_palindrome = True

    # Check if the string is a palindrome
    while (not stack.is_empty()) and (not queue.is_empty()) and still_palindrome:
        char1 = stack.pop()
        char2 = queue.dequeue()
        if char1 != char2:
            still_palindrome = False

    return still_palindrome

def main():
    test_strings = [
        "A man, a plan, a canal, Panama",
        "amanaplanacanalpanama",
        "This is not a palindrone!",
        "aaaaaaaaaaa",
        "a",
        "aaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "aAaaaaaaaabaaaaaaAaaa",
        "This string is too long xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "bob",
        "dan",
        "Madam, I'm Adam.",
        "eve",
        "Eve"
    ]

    for s in test_strings:
        result = is_palindrome(s)
        print(f"Is the string '{s}' a palindrome? {result}")

if __name__ == "__main__":
    main()