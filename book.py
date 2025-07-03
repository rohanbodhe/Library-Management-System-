class Book:
    def __init__(self, title, author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

    def __str__(self):
        status = 'Available' if self.available else "Not available"
        return f"{self.title} by {self.author} (ISBN :{self.isbn} - {status})"


if __name__ == "__main__":
    book1 = Book("1984" ,"George Orwell" , "123456789")
    print(book1)

    book1.borrow()
    print(book1)

    book1.return_book()
    print(book1)