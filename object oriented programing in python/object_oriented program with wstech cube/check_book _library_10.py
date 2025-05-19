# class library:
#     def __init__(self):
#         self.librar={}
#     def add_book(self,book_name,copies):
#         self.librar[book_name]=copies
#         return self.librar
#     def barrow_book(self,item):
#         if self.librar==item:
#             return f"the:{self.librar}"
#         else:
#             return "your book is not avalible for your choice is "
            
#     def show_total(self):
#         print(f"the print :{self.librar}")


# lib=library()
# lib.add_book('basic python',5)
# lib.barrow_book('basic python')
# lib.show_total()
class Library:
    def __init__(self):
        self.books = {}  # Dictionary to store books and available copies

    def add_book(self, title, copies):
        """Adds a book with the specified number of copies."""
        if title in self.books:
            self.books[title] += copies  # If book exists, increase copies
        else:
            self.books[title] = copies  # Add new book
        print(f"{copies} copies of '{title}' added to the library.")

    def borrow_book(self, title):
        """Allows a user to borrow a book if available."""
        if title in self.books and self.books[title] > 0:
            self.books[title] -= 1
            print(f"You have borrowed '{title}'. Enjoy reading!")
        else:
            print(f"Sorry, '{title}' is not available right now.")

    def return_book(self, title):
        """Allows a user to return a borrowed book."""
        if title in self.books:
            self.books[title] += 1
            print(f"Thank you for returning '{title}'.")
        else:
            print(f"'{title}' does not belong to this library.")

    def check_availability(self, title):
        """Checks how many copies of a book are available."""
        if title in self.books:
            print(f"'{title}' has {self.books[title]} copies available.")
        else:
            print(f"'{title}' is not in the library.")

# Creating a Library object
my_library = Library()

# Adding books to the library
my_library.add_book("Python Basics", 3)
my_library.add_book("Data Science 101", 2)

# Borrowing books
my_library.borrow_book("Python Basics")

# Checking book availability
my_library.check_availability("Python Basics")

# Returning a book
my_library.return_book("Python Basics")

# Checking availability again
my_library.check_availability("Python Basics")
