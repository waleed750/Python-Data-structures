
#! III) 
# 1- Define TERMS :

# A) Spanning subgraph
"""
A spanning subgraph of G is a subgraph of G that 
contains all the vertices of the graph G
"""
# B) Preorder traversal of a tree
"""
the root of T is visited 
first and then the subtrees rooted at its children are 
traversed recursively
"""

#_____________________________________________

#! 2- Create clas BookList

from z_unsorted_map import UnSortedTableMap


class BookList:
    def __init__(self):
        self.borrowList = UnSortedTableMap()
        while True:
            student = input("Enter student name or done to finish : ")
            if student.lower() == 'done': 
                break
            book = input("Enter Book title ")
            self.borrowList.__setitem__(student,book)
    def Return(self,k):
        try:
            # get item gives error in case it is not found 
            item = self.borrowList.__getitem__(k)
            self.borrowList.__delitem__(k)
            return item
        except KeyError:
            return None
    def getBookTitle(self,k):
        try:
            return self.borrowList.__getitem__(k)
        except KeyError:
            return None
    def display(self):     
        print("Student / book Title : ")
        for key in iter(self.borrowList):
            print(f"{key}/{self.borrowList.__getitem__(key)}")
brwdBks = BookList()
brwdBks.display()
studentName = input("Enter Student Name to Return : ")
foundBook = brwdBks.Return(studentName)
if foundBook:
    print(f"Student {studentName} returned the book {foundBook}")
else:
    print("Student not found ")