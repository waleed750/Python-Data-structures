from books import Book


class BooksLib:
    def __init__(self,filename) : 
        self.booksLists = {}
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line :
                    continue
                parts = line.split(",")
                #               subject,isbn,title
                # list in dictionary
                found  = parts[0] not in self.booksLists.keys()
                if not found:
                    self.booksLists[parts[0]].append(Book(parts[1],parts[2]))
                else:
                    self.booksLists[parts[0]] = [Book(parts[1],parts[2])]

    def display(self):
        for c in self.booksLists.keys():
            print("Category ",c ,end=": \n")
            for b in self.booksLists[c]:
                print(b ,end=" , ")
            print("\n","_"*20)
        print()
    def addBook(self,subject,isbn,title):
        if subject not in self.booksLists.keys():
            self.booksLists[subject] = [Book(title,isbn)]
        else:
            self.booksLists[subject].append(Book(title,isbn))
    def removeBook(self,subject,title):
        try:
            if subject not in self.booksLists.keys():
                raise Exception
            found = False
            for i in range(len(self.booksLists[subject])):
                if self.booksLists[subject][i].title == title:
                    lst = self.booksLists[subject]
                    lst.pop(i)
                    found = True
                    break
            if not found: 
                raise Exception 
            print("Book removed successfully")
        except:
            print("Book not found")
