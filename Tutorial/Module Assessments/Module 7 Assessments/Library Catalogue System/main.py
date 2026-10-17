class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def check_out(self):
        if not self.available:
            print(f"Sorry, '{self.title}' is already checked out.")
            return False
        self.available = False
        print(f"You checked out '{self.title}'.")
        return True

    def return_book(self):
        if self.available:
            print(f"'{self.title}' was not checked out.")
            return False
        self.available = True
        print(f"You returned '{self.title}'. Thank you!")
        return True

    def display_info(self):
        status = "Available" if self.available else "Checked out"
        print(f"{self.title} by {self.author} - {status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title):
        book = self.find_book(title)
        if book is None:
            print(f"'{title}' is not in the catalogue.")
            return False
        return book.check_out()

    def return_book(self, title):
        book = self.find_book(title)
        if book is None:
            print(f"'{title}' is not in the catalogue.")
            return False
        return book.return_book()

    def display_all(self):
        if len(self.books) == 0:
            print("The catalogue is empty.")
            return
        for book in self.books:
            book.display_info()


def main():
    library = Library()

    print("--- Adding books ---")
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("Pride and Prejudice", "Jane Austen"))

    print("\n--- Catalogue ---")
    library.display_all()

    print("\n--- Adding a new book ---")
    library.add_book(Book("The Hobbit", "J.R.R. Tolkien"))

    print("\n--- Checking out 1984 ---")
    library.check_out_book("1984")

    print("\n--- Checking out 1984 again ---")
    library.check_out_book("1984")

    print("\n--- Returning 1984 ---")
    library.return_book("1984")

    print("\n--- Checking out The Hobbit ---")
    library.check_out_book("The Hobbit")

    print("\n--- Final catalogue ---")
    library.display_all()

main()