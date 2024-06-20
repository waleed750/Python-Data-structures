# Node class representing individual elements in the linked list
class Node:
    def __init__(self, element, next_node=None):
        self.element = element  # The data stored in the node
        self.next = next_node  # Reference to the next node


# Custom exception for empty list errors
class EmptyError(Exception):
    pass


# SinglyLinkedList class with required operations
class SinglyLinkedList:
    def __init__(self):
        self._head = None  # Points to the first node
        self._size = 0  # Tracks the size of the list

    def is_empty(self):
        return self._head is None  # Return True if the list is empty

    def len(self):
        return self._size  # Return the number of elements in the list

    def add_first(self, element):
        new_node = Node(element, self._head)  # Create a new node
        self._head = new_node  # Update head to point to the new node
        self._size += 1  # Increment size

    def add_last(self, element):
        new_node = Node(element)  # Create a new node
        if self.is_empty():
            self._head = new_node  # If empty, head points to new node
        else:
            # Traverse to the last node and update its 'next' pointer
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1  # Increment size

    def remove_last(self):
        if self.is_empty():
            raise EmptyError("Cannot remove from an empty list")

        # If there's only one element, remove it and reset the list
        if self._head.next is None:
            removed_element = self._head.element
            self._head = None
            self._size -= 1
            return removed_element

        # Otherwise, traverse to the second-to-last node
        current = self._head
        while current.next.next:
            current = current.next

        removed_element = current.next.element
        current.next = None  # Set the second-to-last node's next to None
        self._size -= 1  # Decrement size
        return removed_element

    def remove_first(self):
        if self.is_empty():
            raise EmptyError("Cannot remove from an empty list")

        removed_element = self._head.element
        self._head = self._head.next  # Move the head to the next node
        self._size -= 1  # Decrement size
        return removed_element

    def display(self):
        # Display elements of the list as an array
        elements = []
        current = self._head
        while current:
            elements.append(current.element)
            current = current.next
        return elements

    def contains(self, item):
        # Return True if the list contains the item
        current = self._head
        while current:
            if current.element == item:
                return True
            current = current.next
        return False  # If not found, return False

    def insert_before(self, target, new_element):
        if self.is_empty():
            raise EmptyError("Cannot insert in an empty list")

        # If the head is the target, insert before it
        if self._head.element == target:
            self.add_first(new_element)
            return

        current = self._head
        while current.next:
            if current.next.element == target:
                new_node = Node(new_element, current.next)
                current.next = new_node
                self._size += 1
                return
            current = current.next

        raise ValueError("Target item not found")

    def insert_after(self, target, new_element):
        if self.is_empty():
            raise EmptyError("Cannot insert in an empty list")

        current = self._head
        while current:
            if current.element == target:
                new_node = Node(new_element, current.next)
                current.next = new_node
                self._size += 1
                return
            current = current.next

        raise ValueError("Target item not found")

    def remove_item(self, item):
        if self.is_empty():
            raise EmptyError("Cannot remove from an empty list")

        # If the head is the item to be removed
        if self._head.element == item:
            self.remove_first()
            return

        current = self._head
        while current.next:
            if current.next.element == item:
                current.next = current.next.next
                self._size -= 1
                return
            current = current.next

        raise ValueError("Item not found in the list")

    def reverse(self):
        # Reverse the list
        prev = None
        current = self._head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self._head = prev  # Update the head to the new first node

    def concatLists(list1, list2):
        result = list1.display() + list2.display()
        return result


# def test_linked_list():
#     # Test adding to the beginning
#     linked_list = SinglyLinkedList()
#     linked_list.add_first(10)  # List: 10
#     linked_list.add_first(20)  # List: 20 -> 10
#     linked_list.add_first(30)  # List: 30 -> 20 -> 10

#     # Print the current list

#     result = []

#     # Test adding to the end
#     linked_list.add_last(40)  # List: 30 -> 20 -> 10 -> 40
#     linked_list.add_last(50)  # List: 30 -> 20 -> 10 -> 40 -> 50

#     print(linked_list.display())
#     # Test removing the last element

#     removed_element = linked_list.remove_last()  # List: 30 -> 20 -> 10 -> 40
#     print("Removed element:", removed_element)

#     result = []

#     # Test removing until empty
#     while not linked_list.is_empty():

#         print(f"removed {linked_list.remove_last()} and Length {linked_list.len()}  ")

#     try:
#         linked_list.remove_last()  # Should raise EmptyError
#     except EmptyError as e:
#         print("EmptyError caught, as expected:", str(e))


# if __name__ == "__main__":
#     test_linked_list()


#!___________________________________DoublyLinkedBase___________________________________
class _Node:
    __slots__ = "_element", "_prev", "_next"

    def __init__(self, element, prev, next):
        self._element = element
        self._next = next
        self._prev = prev


class _DoubleLinkedBase:

    def __init__(self):
        self._header = _Node(None, None, None)
        self._tailer = _Node(None, None, None)
        self._header._next = self._tailer
        self._tailer._prev = self._header
        self._size = 0

    def is_empty(self):
        return self.len() == 0

    def len(self):
        return self._size

    def insert_between(self, e, predeccor, successor):
        newest = _Node(e, predeccor, successor)
        predeccor._next = newest
        successor._prev = newest
        self._size += 1

    def delete_node(self, node):
        if self.is_empty():
            raise EmptyError
        element = node._element  # record deleted element
        predcessor = node._prev
        sucessor = node._next
        predcessor._next = sucessor
        sucessor._prev = predcessor
        node._prev = node._next = node._element = None  # deprecate node
        self._size -= 1
        return element


class DoubleStack(_DoubleLinkedBase):
    def top(self):
        if self.is_empty():
            raise EmptyError
        return self._header._next._element

    def push(self, e):
        self.insert_between(e, self._header, self._header._next)

    def pop(self):
        if self.is_empty():
            raise EmptyError
        return self.delete_node(self._header._next)


stack = DoubleStack()

# 1. Test if the stack is empty initially
if stack.is_empty():
    print("Test 1: Stack is empty as expected.")
else:
    print("Test 1: Stack is not empty, unexpected.")
# # 2. Test pushing elements onto the stack
# stack.push(10)  # Stack: [10]
# stack.push(20)  # Stack: [20, 10]
# stack.push(30)  # Stack: [30, 20, 10]
# # 3. Test the top element
# top_element = stack.top()  # Expected 30
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())


#! 7.4 ___________________________________LinkedQueue___________________________________
class LinkedQueue(_DoubleLinkedBase):
    def enqueue(self,e):
        self.insert_between(e,self._tailer._prev,self._tailer)
    def top(self):
        if self.is_empty():
            raise EmptyError
        return self._header._next._element
    
    def dequeue(self):
        if self.is_empty():
            raise EmptyError
        return self.delete_node(self._header._next)
# L = LinkedQueue()
# L.enqueue(10)
# L.enqueue(20)
# L.enqueue(30)
# print(L.top())
# try:
#     while True:
#         print(L.dequeue())
# except EmptyError:
#     print("Finised")



#! Circular Linked List 

class CircularLinkedList:
    def __init__(self) :
        self.__tail = None
        self.__size = 0 
    def len(self):
        return self.__size
    def top(self):
        if self.is_empty():
            raise EmptyError
        return self.__tail.next.element
    def is_empty(self):
        return self.__size == 0 
    def add(self,e):
        newest = Node(e,None)
        if self.__size == 0 :
            newest.next = newest
        else:
            newest.next= self.__tail.next
            self.__tail.next = newest
        self.__tail = newest
        self.__size += 1
    def delete(self,target):
        if self.is_empty():
            raise EmptyError
        current = self.__tail.next  # This is the head node in circular linked lists with a tail
        prev = self.__tail
        found = False

        # Loop to find the target node
        while True:
            if current.data == target:
                found = True
                break
            prev = current
            current = current.next
            if current == self.__tail.next:
                break

        if not found:
            print(f"{target} not found in the list")
            return
        # If the node to delete is the head (after tail)
        if current == self.tail.next:
            if current.next == current:
                # Only one node in the list
                self.tail = None
            else:
                # Update tail's next to the second node
                self.tail.next = current.next
        elif current == self.tail:
            # If the node to delete is the tail
            prev.next = current.next
            self.tail = prev
        else:
            # If the node to delete is in the middle
            prev.next = current.next

        print(f"{target} deleted from the list")


# c = CircularLinkedList()
# c.push(10)
# print(c.last())
# c.push(20)
# c.push(30)
# print(c.last())
from collections import deque
class SinglyLinkedList:
    def __init__(self) :
        self._deque = deque()
    def is_empty(self):
        return self.len() == 0
    def len(self):
        return len(self._deque)
    def first(self):
        if self.is_empty():
            raise EmptyError
        return self._deque[0]
    def last(self):
        """Accesses the last element."""
        if self.is_empty():
            raise IndexError("List is empty")
        return self.deque[-1]
    
    def add_first(self,e):
        self._deque.appendleft(e)
    def add_last(self,e):
        self._deque.append(e)
    def remove_last(self):
        if self.is_empty():
            raise EmptyError
        self._deque.pop()
    def remove_first(self):
        if self.is_empty():
            raise EmptyError
        self._deque.popleft()
    def display(self):
        """Displays the elements of the list."""
        print(" -> ".join(map(str, self.deque)))
    
    def contains(self, item):
        """Returns True if the list contains an item, otherwise False."""
        return item in self.deque
    
    def remove_item(self, item):
        """Removes a specific item if it exists."""
        if item in self.deque:
            self.deque.remove(item)
            return True
        else:
            return False
    
    def insert(self, index, item):
        """Adds an element at an arbitrary position."""
        if index < 0 or index > len(self.deque):
            raise IndexError("Index out of bounds")
        self.deque.insert(index, item)
    
    def first(self):
        """Accesses the first element."""
        if self.is_empty():
            raise IndexError("List is empty")
        return self.deque[0]
    
    
    def get_elem(self, index):
        """Accesses an arbitrary element by index."""
        if index < 0 or index >= len(self.deque):
            raise IndexError("Index out of bounds")
        return self.deque[index]
    
    def modify(self, index, item):
        """Modifies an arbitrary element by index."""
        if index < 0 or index >= len(self.deque):
            raise IndexError("Index out of bounds")
        self.deque[index] = item
    
    def clear(self):
        """Clears all contents of the list."""
        self.deque.clear()
    
    def reverse(self):
        """Reverses the elements of the list."""
        self.deque.reverse()
d = SinglyLinkedList()
print(d.len())