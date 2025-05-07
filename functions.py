def my_function(param):
  return param +1 

                      #ARGUMENTS

'''
UNLIKE JS In Python, thankfully, when we run a method/function without passing in the required arguments it will give us an error message:
'''

def say_hi(name):
    print(f"Hi there, {name}!")

say_hi()
# => TypeError: say_hi() missing 1 required positional argument: 'name'


                      #DEFAULT ARGUMENTS
def say_hi(name="Engineer"):
    print(f"Hi there, {name}!")

say_hi()
# => "Hi there, Engineer!"

say_hi("Sunny")
# => "Hi there, Sunny!"

                          #PASS
'''
There will be times when you're writing out your code and know that you will need a function later, but you don't quite know what to put in there yet. A good practice in Python development is to make use of the pass keyword in empty functions until they are ready to be fleshed out
'''

def my_future_function():
    pass

'''
Python developers typically opt for pass over return None because it is a statement rather than an expression. It does not terminate the function like a return statement would do. You can even put code after your pass and it will be executed! A pass statement reminds you that there is work to be done without interfering with your development.
'''