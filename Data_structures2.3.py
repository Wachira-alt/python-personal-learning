# Main Python Data Structures (Built-In)

# 1. List []
# ✅ Ordered, indexed
# ✅ Mutable (you can change it)
# ✅ Can hold mixed types
example_list = ["Dennis", 23, True]

# 2. Tuple ()
# ✅ Ordered, indexed
# ❌ Immutable (can’t change once made)
example_tuple = ("Nairobi", "Kenya")

# 3. String ""
# ✅ Ordered, indexed
# ❌ Immutable
# ✅ Iterable
example_string = "Python"
# You can access characters like:
print(example_string[0])  # 'P'

# 4. Range
# Used to create a sequence of numbers
example_range = range(5)  # → 0, 1, 2, 3, 4

# 5. Set {}
# ❌ Not ordered (no index)
# ✅ Unique items only (no duplicates)
# ✅ Mutable
example_set = {1, 2, 3}

# 6. Dictionary (Map) { key: value }
# ✅ Stores data by key, not position
# ✅ Fast for lookup
example_dict = {"name": "Dennis", "age": 23}


# STEP 1: Lists
# ✅ Creating a list
fruits = ["apple", "banana", "mango"]
print(fruits)  # ['apple', 'banana', 'mango']

# ✅ Accessing items (indexing)
print(fruits[0])     # 'apple'
print(fruits[-1])    # 'mango'

# ✅ Adding items
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'mango', 'orange']

# ✅ Inserting in the middle
fruits.insert(1, "grape")
print(fruits)  # ['apple', 'grape', 'banana', 'mango', 'orange']

# ✅ Removing items
fruits.remove("banana")
print(fruits)  # ['apple', 'grape', 'mango', 'orange']

last = fruits.pop()
print(last)    # 'orange'
print(fruits)  # ['apple', 'grape', 'mango']


# STEP 2: Tuples
# ✅ Creating and accessing a tuple
dimensions = (10, 20)
print(dimensions[0])  # 10

# ✅ Tuple is immutable
# dimensions[0] = 15  # ❌ Error: 'tuple' object does not support item assignment


# STEP 3: Ranges
# ✅ Using range in a list
even_numbers = list(range(2, 10, 2))
print(even_numbers)  # [2, 4, 6, 8]

# ✅ Range in loops
for i in range(3):
    print(i)  # 0, 1, 2


# STEP 4: Strings
# ✅ Index and slice strings
text = "hello"
print(text[0])     # 'h'
print(text[-1])    # 'o'
print(text[1:4])   # 'ell'

# ✅ String methods
print(text.upper())              # 'HELLO'
print(text.replace("l", "z"))    # 'hezzo'


# STEP 5: Shared Sequence Operations
# ✅ Length, min, max
numbers = [3, 1, 5, 2]
print(len(numbers))  # 4
print(min(numbers))  # 1
print(max(numbers))  # 5

# ✅ Membership
print("apple" in fruits)     # True
print("berry" not in fruits) # True

# ✅ Slicing
print(fruits[1:3])    # ['grape', 'mango']
print(fruits[::-1])   # reverse: ['mango', 'grape', 'apple']


# 🔪 Quick Tip: Think of ':' like a knife cutting between elements
colors = ["red", "purple", "green", "yellow"]
# Index:    0      1         2         3
# Slice points are between them.

print(colors[:3])  # → ['red', 'purple', 'green']
