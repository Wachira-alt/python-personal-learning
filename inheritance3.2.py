#inheritance is where a child class inherits methods and attributes from a parent class
# There is superclass and subclass
class Animal:
  def speak(self):
    print ("Animal speaks")

class Dog(Animal):    #Dog inherits from animal
  pass

d = Dog()
d.speak()  #inerited from animal



class Animal:
  def __init__ (self, name):
    self.name = name
@property
def name(self):
  return self._name
@name.setter
def name(self, value):
  if isinstance (value, str) and  1 <= len(value) <= 25 :
    self._name = value
  else:
    raise NameError ("name must be a string between 1-25 characters")

class Dog(Animal):
  def __init__ (self, name, breed):
    super().__init__(name) #call the parent class constructor
    self.breed = breed
  @property
  def breed(self):
    return self._breed
  @breed.setter
  def breed (self, value):
    if isinstance (value, str) and 1 <= len(value) <= 25:
      self._breed = value
    else:
      raise NameError ("breed must be a string of between 1 -25 characters")
    


#WHEN TO USE INHERITANCE AND WHEN TO USE COMPOSITION

# a dog is an ani animal --- inheritance
# a car has an engine -- composition


#COMPOSITION
class Engine:
  def start(self):
    print ("engine starts")

class Car:
  def __init__(self):
    self.engine = Engine() #car has an engine

  def drive (self):
    self.engine.start()
    print("car drives")

car = Car()
car.drive()

#Decorators add functionality to a function without changing the function itself - think of a phone in  a case, it is still the same phone just enhanced
#REAL WORLD SCENARIO - you are building a website and want to restrict access to certain pages- users must be logged in to access them - instead of adding login checks to every function manually, use a decorator
def login_required(func):
  def wrapper(user):
    if user.get("authenticated"):
      return func(user)
    else:
      return "Access Denied: Please login"
  return wrapper

#use decorator
@login_required
def view_dashboard(user):
  return f"welcome to your dashboard, {user['username']}"

#Testing

user1 = {"username": "dennis", "authenticated": True}
print(view_dashboard(user1))

user2 = {"username": "guest", "authenticated": False}
print(view_dashboard(user2))


#Example of super usage
#super() helps if you want to add to not replace the parents method


class Car:
  def __init__ (self, wheel_size, wheel_number):
    self.wheel_size = wheel_size
    self.wheel_number = wheel_number
  def go(self):
    return "VROOOOOOM"
@property
def wheel_size(self):
 return self._wheel_size
@wheel_size.setter
def wheel_size(self, value):
  if isinstance (value, int) and len(value) == 1:
   self._wheel_size = value
  else:
    raise NameError("wheel size must be an integer greater or equal to 1")
  

class Toyota(Car):
  def __init__(self, wheel_size, wheel_number, year):
    super().__init__(wheel_size, wheel_number) #calls car's __init__
    self.year = year
  def go(self):
    parent_sound = super().go() #calls car's go
    return parent_sound + "But a Toyota Sounds louder!"
  


# REAL WORLD SCENARIO FOR A WEBSITE
# Situation:
# You have a website with different types of users:

# User (base class): Every user has a name and email.

# Admin (subclass): Admin users can manage the site.

# Customer (subclass): Customers can buy products.

class User:
  def __init__ (self, name, email):
    self.name = name
    self.email = email
  def login(self):
    return f"{self.name} logged in"
  def logout(self):
    return f"{self.name} logged out"
  
#defining subclasses that inherit from user
class Admin(User):
  def __init__ (self, name, email, admin_level):
    super().__init__(name, email)
    self.admin_level = admin_level
  def access_dashboard(self):
    return f"Admin {self.name}with level{self.admin_level} accessed the dashboard"

class Customer(User):
  def __init__(self, name, email, customer_id):
    super().__init__(name, email)
    self.customer_id = customer_id
  def make_purchase(self, product):
    return f"{self.name} purchased {product}"
  
admin1 = Admin("Alice", "alice@example.com", admin_level=5)
customer1 = Customer("Bob", "bob@example.com", customer_id=12345)

print(customer1.login()) 


