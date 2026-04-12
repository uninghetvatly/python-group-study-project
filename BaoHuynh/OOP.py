
# Classes are blueprints. Objects (instances) are created from those blueprints.
# Use PascalCase for class names (e.g., MyClass).

class Book:
    # 1. The Constructor (__init__) and Instance Attributes
    # Runs automatically when a new object is created.
    # 'self' refers to the specific object being created.
    def __init__(self, title, author):
        # Instance attributes belong to the specific object
        self.title = title
        self.author = author
        self.is_read = False

    # 2. Instance Methods
    # Functions that belong to the object and can modify its state.
    def read_book(self):
        self.is_read = True
        print(f"You have read '{self.title}' by {self.author}.")


# Creating objects (Instances)
book1 = Book("Bách hóa Giấc mơ của ngài Dollargut", "Lee Mi-ye")
book2 = Book("Tôi bị bố bắt cóc", "Mitsuyo Kakuta")

# Accessing attributes and calling methods
print(book1.title)
book1.read_book()


# 13. Intermediate OOP - Composition and Class Attributes

# 3. Class Attributes
# A variable shared by ALL instances of the class. Defined outside __init__.
class LibraryBook(Book):
    total_books_created = 0  # Class attribute

    def __init__(self, title, author):
        super().__init__(title, author)  # Calls the parent Book class constructor
        LibraryBook.total_books_created += 1  # Increment for every new book


# 4. Composition
# A class can contain objects of another class as attributes.
class Library:
    def __init__(self, name):
        self.name = name
        self.collection = []  # Will store a list of book objects

    def add_book(self, book_obj):
        self.collection.append(book_obj)
        print(f"Added '{book_obj.title}' to {self.name}.")


my_library = Library("Thư viện Cá nhân")
my_library.add_book(book1)
my_library.add_book(book2)


# 5. Inheritance
# Creating a Child class that inherits attributes and methods from a Parent class.
class EBook(Book):
    def __init__(self, title, author, file_size):
        # super() calls the Parent class's constructor
        super().__init__(title, author)
        self.file_size = file_size  # Extra attribute specific to the child class (in MB)

    # 6. Polymorphism (Method Overriding)
    # The Child class provides its own specific implementation of a Parent's method.
    def read_book(self):
        self.is_read = True
        print(f"You read '{self.title}' on your e-reader. ({self.file_size}MB)")


ebook1 = EBook("Key to IELTS writing task 2", "Pauline Cullen", 5.2)
ebook1.read_book()  # Calls the overridden method in EBook
book2.read_book()  # Calls the original method in the parent Book class


# 15. Expert OOP - Encapsulation, Magic Methods, and Decorators

class StoreItem:
    def __init__(self, name, price):
        self.name = name

        # 7. Encapsulation (Public, Protected, Private)
        # Public: Accessible anywhere (self.name)
        # Protected: Starts with '_' (e.g., self._discount). Conventionally meant for internal use.
        self._discount = 0.0
        # Private: Starts with '__'. Python hides it to prevent direct access from outside.
        self.__price = price

        # Getters and Setters: Safe, controlled ways to interact with private attributes

    def get_price(self):
        return self.__price * (1 - self._discount)

    def set_price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            print("Invalid price.")

    # 8. Magic/Dunder Methods
    # Special built-in methods starting and ending with '__'
    # __str__ defines how the object looks when converted to a string (like in print())
    def __str__(self):
        return f"Item: {self.name}, Price: ${self.get_price():.2f}"

    # 9. Class Methods (@classmethod)
    # Takes 'cls' instead of 'self'. Can access and modify class-level state, not instance state.
    @classmethod
    def instantiate_from_csv(cls):
        print("Pretending to load multiple objects from a CSV file...")

    # 10. Static Methods (@staticmethod)
    # Behaves like a normal function but lives inside the class for logical organization.
    # Takes neither 'self' nor 'cls'.
    @staticmethod
    def is_integer(num):
        return isinstance(num, int)


# Testing Expert Concepts
item = StoreItem("Laptop", 1000)

# print(item.__price) # ERROR: Cannot access private attribute directly
item.set_price(1200)  # Using setter to modify
print(f"Current price: ${item.get_price():.2f}")  # Using getter to read

print(item)  # Automatically triggers the __str__ magic method

StoreItem.instantiate_from_csv()  # Calling a class method directly on the class
print(f"Is 5 an integer? {StoreItem.is_integer(5)}")  # Calling a static method