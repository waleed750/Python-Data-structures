class Book:
    __slots__ = 'isbn' , 'title' 
    def __init__(self, title, isbn) -> None:
      self.isbn = isbn
      self.title = title
    def  getTitle(self):
        return self.title
    def getISBN(self):
        return self.isbn
    def __str__(self) -> str:
        return f"({self.getTitle()}) {self.getISBN()}"
    