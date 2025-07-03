from book import Book
from member import Member
from library import Library

def display_menu():
    print("\n===== Library Management Menu =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. View All Books")
    print("4. View All Members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Exit")

# Create the library
library = Library("City Library")

# Store books and members by ID/title for quick access
book_lookup = {}
member_lookup = {}

while True:
    display_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        book = Book(title, author, isbn)
        library.add_book(book)
        book_lookup[title.lower()] = book

    elif choice == "2":
        name = input("Enter member name: ")
        member_id = input("Enter member ID: ")
        member = Member(name, member_id)
        library.register_member(member)
        member_lookup[member_id] = member

    elif choice == "3":
        library.list_books()

    elif choice == "4":
        library.list_members()

    elif choice == "5":
        member_id = input("Enter your member ID: ")
        title = input("Enter book title to borrow: ").lower()

        member = member_lookup.get(member_id)
        book = book_lookup.get(title)

        if member and book:
            member.borrow_book(book)
        else:
            print("Invalid member ID or book title.")

    elif choice == "6":
        member_id = input("Enter your member ID: ")
        title = input("Enter book title to return: ").lower()

        member = member_lookup.get(member_id)
        book = book_lookup.get(title)

        if member and book:
            member.return_book(book)
        else:
            print("Invalid member ID or book title.")

    elif choice == "7":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
