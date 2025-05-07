                                                                #OPERATORS
'''
Just like JavaScript, Python has several ways we can control the flow of execution in our programs:

We can use conditional statements like if/else and try/except
We can use looping constructs like for and while
Using these control flow constructs means we're taking our code out of the normal flow of execution (top-to-bottom, one line at a time) and instead providing some instructions to change that order
'''

#COMPARISON OPERATORS

'''
In Python, many built-in classes have the following functions that can be used to compare two values:

>: greater than
>=: greater than or equal to
<: less than
<=: less than or equal to
==: equal to
!=: not equal to
'''

#LOGICAL OPERATORS

'''
Python has the same logical operators you'll find in many other languages, including JavaScript:

and: and. Returns True if both statements are true.
or: or. Returns True if one of the two statements is true.
not: not. Coerces the data to its boolean equivalent, then reverses it (True becomes False, and vice versa).
'''
                                                      #CONDITIONAL STATEMENTS

#1 if/else statements
#JS
'''
// JavaScript
let dog = "cuddly";
let owner;

if (dog === "hungry") {
  owner = "Refilling food bowl.";
} else if (dog === "thirsty") {
  owner = "Refilling water bowl.";
} else if (dog === "playful") {
  owner = "Playing tug-of-war.";
} else if (dog === "cuddly") {
  owner = "Snuggling.";
} else {
  owner = "Reading newspaper.";
}
'''
# Here's how we can write the equivalent statement in Python:

# Python
dog = "cuddly"

if dog == "hungry":
    owner = "Refilling food bowl."
elif dog == "thirsty":
    owner = "Refilling water bowl."
elif dog == "playful":
    owner = "Playing tug-of-war."
elif dog == "cuddly":
    owner = "Snuggling."
else:
    owner = "Reading newspaper."

#2 Truthy/Falsy Values
'''
In order to use control flow effectively, it's important to know what values Python treats as "truthy" and "falsy".

As we saw in the lesson on data types, there are many values Python considers falsy:

Empty lists []
Empty tuples ()
Empty dictionaries {}
Empty sets set()
Empty strings '' or ""
Zero of any numeric type (0, 0.0)
None
And, of course, False
Using those values in control flow means the condition will be False:
'''
def control_flow(value):
    if value:
        # if the value is truthy
        print("yep!")
    else:
        # if the value is falsy
        print("nope!")

control_flow(False)
# "nope!"
control_flow(None)
# "nope!"
control_flow(True)
# "yep!"
control_flow("")
# "nope!"
control_flow(0)
# "nope!"
control_flow("0")
# "yep!"

#3 CONDITIONAL EXPRESSIONS
'''
Python also allows us to use conditional expressions (or ternary operators) to evaluate the truthiness of complex statements in a single line.
'''
age = 1

is_baby = 'baby' if age < 2 else 'not a baby'

#This is the equivalent of the following if/else statement:

age = 1
if age < 2:
  is_baby = 'baby'
else:
  is_baby = 'not a baby'


#4 TRY/EXCEPT STATEMENTS

'''
Throughout our Python assignments so far, we have seen a number of different Exceptions. As we learned in our "Error Messages" lesson, Exceptions are a type of error that we can intercept so that our Python application can continue to run. try/except statements are the tool that allow us to perform these interceptions.
'''
def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except:
        print("An error occurred")
'''
Did you find any arguments that gave you trouble? The divide() function will fail to perform its primary task if num2 is 0 or either of the numbers is of a non-numerical type. Our try/except statement allowed our function to run to completion, but "An error occurred" is not a particularly helpful message.
'''

def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float")
    finally:
        print("Isn't division fun?")
'''
Use of the finally keyword at the end of a try/except statement allows us to perform actions that we want to occur regardless of whether or not an exception has been thrown.
'''

#4 DICTIONARY MAPPING
'''
Unlike JavaScript, Python does not have switch/case statements. Python can handle switch/case logic in if/else statements, but for very long sets of conditions, it may be worthwhile to use dictionary mapping instead.
'''
# Let's take a look at how we might do that with an if/elif/else statement in Python:
# Python
dog = "cuddly"

if dog == "hungry":
    owner = "Refilling food bowl."
elif dog == "thirsty":
    owner = "Refilling water bowl."
elif dog == "playful":
    owner = "Playing tug-of-war."
elif dog == "cuddly":
    owner = "Snuggling."
else:
    owner = "Reading newspaper."
#Now let's look at how we would handle this with dictionary mapping

dog = "cuddly"

dict_map = {
    "hungry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "Playing tug-of-war.",
    "cuddly": "Snuggling.",
}

# Remember that a dictionary's .get() method lets us set a default value!
owner = dict_map.get(dog, "Reading newspaper.")