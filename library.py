from book import Book
from member import Member

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []     # list of Book objects
        self.members = []   # list of Member objects

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' removed from the library.")
        else:
            print(f"Book '{book.title}' not found in the library.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print(f"\nBooks in {self.name}:")
            for book in self.books:
                print(f" - {book}")

    def list_members(self):
        if not self.members:
            print("No registered members.")
        else:
            print("\nRegistered Members:")
            for member in self.members:
                print(f" - {member.name} (ID: {member.member_id})")

if __name__ == "__main__":
    # Create books
    book1 = Book("The Alchemist", "Paulo Coelho", "1111")
    book2 = Book("Harry Potter", "J.K. Rowling", "2222")

    # Create members
    member1 = Member("John", 1)
    member2 = Member("Emma", 2)

    # Create library
    my_library = Library("City Library")

    # Add books
    my_library.add_book(book1)
    my_library.add_book(book2)

    # Register members
    my_library.register_member(member1)
    my_library.register_member(member2)

    # Show books and members
    my_library.list_books()
    my_library.list_members()

