# CLASS ATTRIBUTES AND METHODS IN PYTHON
#instance attributes - this belong to individual objects
#class attributes - belong to the class itself and are shared accross the entire class
#class methods - methods that operate on the class itself not just an instance

# 🧠 Real-World Example: Library Book Tracking System
# Let’s say you’re creating a system for a library to track how many books have been checked out in total, and manage details about individual books.
# you access it like Book.total_books_checked_out

class Book:
  #class attribute
  total_books_checked_out = 0

  def __init__ (self, title, author):
    self.title = title     #instance attribute (defined inside __init__ )
    self.author = author    #instance attribute
    self.checked_out = False

  def checkout(self):
    if not self.checked_out:
      Book.total_books_checked_out += 1
      self.checked_out = True
      print(f"Checked out: {self.title}")
    else:
      print(f"{self.title} is already checked out")

book1 = Book("Atomic Habits", "James Clear")
book2 = Book("Deep Work", "Cal Newport")

book1.checkout()
book2.checkout()
book1.checkout()

print(Book.total_books_checked_out)

# 🧠 Explanation:

# total_books_checked_out is a class attribute shared by all instances.

# Each time any book is checked out, we increment the counter at the class level.




# ✅ Step 2: Class Method
# decorated with @classmethod
#cls refers to the class itself
#used when the logic applies to the class, not a specific instance
# Now let’s say we want to get a message about how many books have been checked out—this is a class-level concern.

class Book:
  total_books_checked_out = 0 #class attribute

  def __init__(self, author, title):
    self.author = author
    self.title = title
    self.checked_out = False

  def checkout(self):
    if not self.checked_out:
      Book.total_books_checked_out += 1
      self.checked_out = True
  @classmethod
  def report(cls):
    return f"{cls.total_books_checked_out} books have been checked out in total"
book1 = Book("1984", "George Orwell")
book2 = Book("Brave New World", "Aldous Huxley")


book1.checkout()
book2.checkout()

print(Book.report())


# ✅ Step 3: Static Method
# Let’s say you want a utility method to check if a book title is valid. This doesn’t depend on the class or instance data—so we use a static method.

class Book:
  @staticmethod
  def is_valid_title(title):
    return isinstance (title, str) and len(title.strip()) > 0

print(Book.is_valid_title("   "))          
print(Book.is_valid_title("Clean Code")) 


# ✅ 5. Class Constants
# Use ALL CAPS by convention.

# Indicate values that shouldn’t change.

# Still accessible & modifiable (Python doesn't enforce immutability).

class Albu:
  GENRES = ["Hip Hop", "Pop", "Jazz"] #class constant

  @classmethod
  def check_genre(cls, genre):
    return genre in cls.GENRES
  

  #full EXAMPLE

class Album:
  GENRES = ["Hip Hop", "Pop", "Jazz"]
  album_count =0


  def __init__ (self, genre, date):
    if self.check_genre(genre):
      self.genre = genre
      self.release_date = date
      self.increase_album_count()

@classmethod
def check_genre(cls, genre):
  return genre in cls.GENRES

@classmethod
def increase_album_count (cls, increment=1):
  cls.album_count += increment

# ❗ Remember:
# Class methods/attributes are for general rules or tracking.

# Instance methods/attributes are for individual data/behavior.
