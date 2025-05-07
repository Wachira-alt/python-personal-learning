"""
"Scope" refers to the areas of your program in which certain data is available to you. Any variable created outside of a function will be considered global and made available to all functions in your module. Any variable created inside of your function (including parameters!) is considered local and only available inside of the function.
"""

# To change the value of a global variable from a local scope, we need to use the global keyword:

change_the_world = "change yourself"

def change_yourself():
    global change_the_world
    change_the_world = "world changed"

# Now when we run our function again, we should see the desired output:

 #change_yourself()
 #print(change_the_world)
 #world changed

'''
 Conclusion
Remember: A local variable defined inside a function can't leave that function. It is not available to your program outside of the function. A global variable defined outside of a function is accessible inside the function, just as in JavaScript. Global variables can only be modified from the global scope or by using the global keyword.
 '''