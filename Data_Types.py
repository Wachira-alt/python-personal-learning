'''
python Shell - an interactive interpreter that can be accessed from the cli
data types - a specific kind of data
exception - a predictable error that can be handled without making a program to crash
codeblock-  a group of code that can be interpreted together
function - a named codeblock that performs a series of actions when called
scope - an area in your program where a specific variable can be called
'''

                          #DATA TYPES
                                                            #1. strings
dog_name = "Lucy"
print(f"Say hello to my dog {dog_name}")


price_1 = 3
price_2 = 2.5

                        #example2

price_1 = 3
price_2 = 2.5

print(f"Item 1 costs ${price_1:.2f}")
# => Item 1 costs $3.00
print(f"Item 2 costs ${price_2:.2f}")
# => Item 2 costs $2.50

                    #example3


"hello"
# "hello"
"hello".upper()
# "HELLO"
"HELLO".lower()
# "hello"
"hello".capitalize()
# "Hello"
"hello" + "world"
# "helloworld"
"hello" * 3
# "hellohellohello"

                #example4

type("hello")
# => <class 'str'>             

'''
Using the dir() function on any Python object will display a list of all the methods that object responds to (you'll see upper, lower, capitalize and more in that list):
'''

dir("hello")
# => ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', ... ]


                                                              #2 Numbers

#unlike js there are two types of numbers ints and floats

                  #example1 -convertingb to float and int
int("1")
# => 1
int(1.1)
# => 1
float("1.1")
# => 1.1



                    #SEQUENCE TYPES
'''
Python has a number of different data types that are useful for storing data. Each of these types can store any type of data inside; what differs between them are the rules for organizing and accessing the data.
'''

                                                                  #1 LISTS
# Any set of comma separated data enclosed in brackets is a list. 

        #example1

[1, 3, 400, 7]
# => [1, 3, 400, 7]

#creating an empty list
list()
# => []

      #Accessing elements in a list

list_abc = ['a','b','c']
list_abc[0]
# => 'a'
list_abc[1]
# => 'b'
list_abc[2]
# => 'c'

        #operating on lists

len([1, 3, 400, 7])
# 4
sorted([5, 100, 234, 7, 2])
# [2, 5, 7, 100, 234]
list_123 = [1, 2, 3]
list_123.pop()
# 3
list_123.remove(1)
print(list_123)
# [2]



                                                                  #2 TUPLES
'''Tuples are nearly identical to lists, with two key differences:

first, tuples are created with open and close parentheses (in place of square brackets). The tuple() class constructor function can also be used to cast lists and other iterable data types to tuples.
'''
(1, 2, 3)
# => (1, 2, 3)
tuple([1, 2, 3])
# => (1, 2, 3)

#Second, tuples are immutable. This means that once a tuple has been created, the tuple itself cannot be changed.


                                                            #3 SETS AND DICTS

#SETS
'''
A set is unindexed, unordered, and unchangeable. It can be initiated with curly brackets or the set() class constructor. The set() class constructor takes a list or tuple as its only argument (remember those brackets and parentheses!) The elements of a set are unique:
'''
set()
# => {}

set(3, 2, 3, 'a', 'b', 'a')
# => TypeError: set expected at most 1 argument, got 6

set([3, 2, 3, 'a', 'b', 'a'])
# => {2, 3, 'a', 'b'}

'''
NOTE: Immutable and unchangeable mean different things when we're talking about data types in Python. A set is immutable because its overall structure cannot be changed; it can't be made shorter or longer. It is unchangeable because an element cannot be changed into something else.
'''

s = {1, 2, 3}
s.pop()
# => 1
s.remove(3)
# => {2}

#DICTIONARIES
#Dictionaries are Python's equivalent of a plain old JavaScript object.

my_dict = { "key1": "value1", "key2": "value2" }
print(my_dict["key3"])
# => KeyError: 'key3'

print(my_dict.get("key3"))
# => None

#Unlike JavaScript, you cannot use the dot notation to access keys on dictionaries — only the bracket notation will work:

my_dict = { "key1": "value1", "key2": "value2" }
my_dict.key2
# => AttributeError: 'dict' object has no attribute 'key2'

#You can also create dictionaries using the dict()
dict(x = 1, y = 2)
# => {'x': 1, 'y': 2}

                                                                    #4 NONE
'''
In Python, there is one special value that represents the absence of a value, None.
Unlike JavaScript, Python won't let you create a variable without assigning a value. You must explicitly assign a value of None if you want an "empty" variable:
'''


# => NameError: name 'no_value' is not defined

no_value = None
print(no_value)
# => None

                                                                #5 BOOLEANS
#There are only two values of the Boolean data type: True and False
type(True)
# => <class 'bool'>
type(False)
# => <class 'bool'>

'''Python, like JavaScript, has the concept of "truthy" and "falsy" values as well: values which, when coerced to their equivalent boolean value, or evaluated as part of a conditional statement, return either True or False:
'''

not True
# => False
not False
# => True
not 1
# => False
not 0
# => True
not ''
# => True
not None
# => True
not []
# => True
not ()
# => True
not {}
# => True

'''
NOTE: not is the operator that reverses the truth value of a value, variable, or statement. ! still plays a role in Python, but it is only used in the != operator that asserts that two values are not equal.
'''