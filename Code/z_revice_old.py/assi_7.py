class Empty(Exception):
    pass
class SingleLinkedList:
    class _Node:
        __slots__ = '_element' , '_next'
        def __init__(self,element,next):
            self._element = element
            self._next = next
    def __init__(self):
        self._head = None
        self._size = 0 
    def len(self):
        return self._size
    def is_empty(self):
        return self._size == 0 
    def add_first(self,e):
        node = self._Node(e,None)
        if self.is_empty():
            self._head = node
        else:
            node._next = self._head
            self._head = node
        self._size += 1 
    def add_last(self,e):
        node = self._Node(e,None)
        if self.is_empty():
            self._head = node
            self._size += 1
            return
        current = self._head
        while current._next :
            current = current._next
        current._next  = node
        self._size += 1
    def remove_first(self):
        if self.is_empty():
            raise Empty("Single Linked List is Empty")
        oldhead = self._head
        self._head = self._head._next
        self._size -= 1
        element = oldhead._element
        oldhead._next = oldhead._element = None # diprecated head 
        return element
    def remove_last(self):
        if self.is_empty():
            raise Empty("Singe Linked List is Empty")
        if self._size == 1 :
            element = self._head._element
            self._head = None
            self._size -= 1
            return element
        current = self._head
        prev = self._head
        while current._next:
                prev = current
                current = current._next
        element = prev._element
        prev._next = None
        self._size -= 1
        return element
    def __iter__(self):
        current = self._head
        while current :
            yield current._element
            current = current._next
    def display(self):
        current = self._head
        while current :
            print(current._element)
            current = current._next
    def __contains__(self,e):
        if self.is_empty():
            return False
        current = self._head
        while current:
            if current._element == e :
                return True 
            current = current._next
        return False
    def insert_before(self, e1, e2):
        if not self.__contains__(e1):
            raise Exception("Element Not Found")

        # Create a dummy node that points to the head of the list
        dummy = self._Node(None, self._head)
        current = dummy

        while current._next:
            if current._next._element == e1:
                current._next = self._Node(e2, current._next)
                self._size += 1
                self._head = dummy._next  # Update head in case it was the head node
                return
            current = current._next

        raise Exception("Element Not Found")

    def insert_after(self,e1,e2):
        if not self.__contains__(e1):
            raise Exception("Element Not found ")
        current = self._head
        while current:
            if current._element == e1:
                node = self._Node(e2,current._next)
                current._next = node
                self._size += 1
                return
            current = current._next
    def remove_item(self,e):
        if self._head._element == e:
            self._head = self._head._next
            self._size -= 1 
            return
        current = self._head._next
        while current or current._next :
            if current._next._element == e :
                current._next = current._next._next
                self._size -= 1
                return
            current = current._next
        raise Exception("Element Not found ")
    @staticmethod
    def ConcatLists(list1, list2):
        if list1.is_empty():
            return list2
        if list2.is_empty():
            return list1

        new_list = SingleLinkedList()
        current = list1._head
        while current:
            new_list.add_last(current._element)
            current = current._next

        current = list2._head
        while current:
            new_list.add_last(current._element)
            current = current._next

        return new_list
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

s = SingleLinkedList()
s.add_first(6)
s.add_first(1)
s.add_last(10)
s.add_last(4)
# s.remove_last()
s.insert_before(10,100)
s.remove_item(10)
# s.insert_after(int(input("Enter value : ")),500)
# s.add_first(11)
# s.add_first(20)
# for i in iter(s):
#     print(i)
# s.remove_first()
s.display()
print(f"Contains 6: {s.__contains__(6)}")

list1 = SingleLinkedList()
list1.add_last(1)
list1.add_last(2)
list1.add_last(3)

list2 = SingleLinkedList()
list2.add_last(4)
list2.add_last(5)
list2.add_last(6)

# Concatenating the lists
concatenated_list = SingleLinkedList.ConcatLists(list1, list2)

# Displaying the elements of the new list
concatenated_list.display()