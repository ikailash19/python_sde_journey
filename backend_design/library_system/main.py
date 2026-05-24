from Book import Book
from Library import Library
book1 = Book("Harry Potter", "JK Rowling")
book2 = Book("Half Girlfriend", "Chetan Bhagat")

library = Library()
library.add_book(book1)
library.add_book(book2)
available_books = library.show_available_books()
for book in available_books:
    print(book)
library.borrow_book(book1)
print("After borrowing:")

available_books = library.show_available_books()
for book in available_books:
    print(book)