class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book: {book.title} added")

    def borrow_book(self, book):
        if book.availability:
            book.availability = False
            return True
        else:
            print("Book not available")

    def return_book(self, book):
        book.availability = True

    def show_available_books(self):
        return [b for b in self.books if b.availability]