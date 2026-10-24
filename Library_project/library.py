class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.available = copies

    def info(self):
        return f"{self.title} by {self.author} is Available : {self.available}"


class Library:
    def __init__(self):
        self.books = []

    def has_books(self):
        return len(self.books)>0

    def add_book(self, title, author, copies):
        title = title.strip()
        author = author.strip()

        if not title or not author:
            return "Title and author are needed."

        try:
            copies = int(copies)
        except ValueError:
            return "Copies must be a number."

        if copies<=0 :
            return "Copies must be greater than zero."

        book = Book(title, author, copies)
        self.books.append(book)

        return "Book added successfully."


    def show_books(self):
        if not self.has_books():
            return "No books available."

        result = "\nBooks:\n"

        for index, book in enumerate(self.books, start=1):
            result += f"{index}. {book.info()}\n"

        return result

    
    def borrow_book(self, book_number):

        try:
            index = int(book_number) - 1

        except ValueError:
            return "Enter a valid book number."

        if index < 0 or index >= len(self.books):
            return "Book not found."

        book = self.books[index]

        if book.available == 0:
            return "This book is not available."

        book.available -= 1

        return f"You borrowed '{book.title}'."

    
    def return_book(self, book_number):
        try:
            index = int(book_number) - 1
        except ValueError:
            return "Enter a valid book number."

        if index < 0 or index >= len(self.books):
            return "Book not found."

        book = self.books[index]

        if book.available == book.copies:
            return "This book is already fully returned."

        book.available += 1

        return f"You returned '{book.title}'."