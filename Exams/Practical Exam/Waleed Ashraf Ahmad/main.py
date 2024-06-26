from bookslib import BooksLib


def main():
    BLib = BooksLib("books.dat")
    while True:
        choice = input("'A' for add, 'R' for remove, 'D' for display, 'X' for exit: ")
        if choice == "A" or choice == "a":
            subject = input("Subject: ")
            isbn = input("ISBN: ")
            title = input("Title: ")
            BLib.addBook(subject,isbn,title)
        elif choice == "R" or choice == "r":
            subject = input("Subject: ")
            title = input("Title: ")
            BLib.removeBook(subject,title)
        elif choice == "D" or choice == "d":
            BLib.display()
        elif choice == "X" or choice == "x":
            break
        else:
            print("Invalid choice")

main()