#A class is a template/blueprint- used to create multiple similar objects
# example a class Dog can be used as a factory of creating many other dogs
#instance- this is an actual object created using a class - a real thing based on the blueprint- each instance is unique although they are created from the same class

#Term	- Simple Explanation
#class	- A blueprint for creating objects
#object / instance	- A thing created from a class
#instantiate	- To create an object from a class

# class pipe:
#   def __init__(self, length, diameter, material):
#     self.length = length
#     self.diameter = diameter
#     self.material = material
#   def flow_water(self):
#     print("water is flowing through the pipe")
# my_pipe = pipe(10, 5, "pvc")
# my_pipe.flow

#class attributes - belong to the class itself and are shared by all instances
#instance attributes - belong to each individual instance and can be different from one object to another

class Human:
    species = "Homo sapiens"  # class attribute

    def __init__(self, name):
        self.name = name       # instance attribute


# property() function
# it is a built in function that allows defining custom logic for getting, setting or deleting an attribute
# importance - it helps protect your data nad enforce rules by not allowing any random value to be assigned to an attribute

#simple example without property()

# class Dog:
#    def __init__ (self, name):
#       self.name = name
# dog = Dog("simba")
# dog.name = 124 # this should not be allowed

#using property() to control access

# class Dog:
#    def __init__(self, name):
#       self._name = name  # _name means "internal use only"

#    def get_name(self):
#       print ("Getting name")
#       return self._name
   
#    def set_name(self, value):
#       print("setting name....")
#       if isinstance(value, str) and 1 <= len(value) >= 25:
#          self.name = value
#       else:
#          raise ValueError("Name must be a string with 1-25 characters")
#    #the magic happens here:
#    name = property(get_name, set_name)
   
# dog = Dog("simba")


# dog.name = "zazu"
# print (dog.name)

#using the @property Decorator (pythonic style)

#this allows keeping the simple .notation

class Dog:
   def __init__ (self, name):
      self._name = name #internal, raw attribut
   @property
   def name(self):
      print("Getting name..")
      return self._name
   @name.setter
   def name(self, value):
      print("setting name...")
      if isinstance(value, str) and 1 <= len(value) <= 25:
         self._name = value
      else:
         raise ValueError("name must be a string with 1-25 characters")
dog = Dog("Michael")
print (dog.name)

Approved_Breeds = [
   "Mastiff", "Chihuahua", "Corgi", "Shar Pei", 
    "Beagle", "French Bulldog", "Pug", "Pointer"
]

class Dog:
   def __init__ (self, name = "fido", breed = "Mastiff"):
      self.name = name
      self.breed = breed 
   @property
   def name(self):
      return self._name #safe, private access
   
   @name.setter
   def name(self, value):
      if isinstance(value, str) and 1<=len(value)<= 25:
         self._name = value.Title #capitalize nicely
      else:
         raise ValueError("name must be a string between 1-25 characters")
   @property
   def breed(self):
      return self._breed
   
   @breed.setter
   def breed(self, value):
      if value in Approved_Breeds:
         self._breed = value
      else:
         raise ValueError("Breed must be in the list of approved breeds")
         

