
                                                  #WHILE LOOP
'''
in javascript
let i = 0;
while (i < 5) {
  console.log("Looping!");
  i++;
}
'''
# Python has a while construct too, which works in much the same way:

i = 0
while i < 5:
  print("Looping!")
  i += 1

                                                    #FOR LOOP
'''
JavaScript has a for loop, which is commonly used to run some condition a set number of times:

for (let i = 0; i < 10; i++) {
  console.log(`Looping!`);
  console.log(`i is: ${i}`);
}
'''     

# Python also has a for loop (with slightly simpler syntax!):
for i in range(10):
    print("Looping!")
    print(f"i is: {i}")
'''
A for loop in Python automatically proceeds to the next element of the iterable object in its constructor; there is no need to specify that the loop is stopping at a certain point or increasing after each iteration.
'''

#converting heights to inches

player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

player_heights = [height * 7920 for height in player_heights]

#That's it! Another benefit of list comprehensions is that you can easily reuse the name of your original sequence without worrying about conflicting names: