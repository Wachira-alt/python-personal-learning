#INTRO - what i will learn
#MODULE - a single python file with functions, classes and variables
#PACKAGE - A folder containi ng multiple modules and a n __init__.py file that groups them
# organizing code into reusable pieces

#IMPORTING- bring functions, classes or whole modules into the current script
#Expand app functionality by reusing code

#PyPI and pip
#PyPI - The official repo of thousand of python packages
#PIP - The command line tool to install packages from PyPI
#Understand how to search, download, and use thirdparty packages like pytest for testing

#VIRTUAL ENVIRONMENTS
#Isolate project depedencies so they don't crash with other python projects on my machine
#use tools like pipenv to create, manage and activate virtual environments



            #WHY THIS MATTERS
#Helps structure large projects cleanly
#Allows code reuse and sharing
#Let's you leverage powerful libraries instead of reinventing the wheel
#Keeps my project dependencies manageable and isolated
"""
🧠 CONFIGURING PYTHON APPLICATIONS - LEARNING NOTES
Author: Dennis Wachira
This file contains beginner-friendly notes and examples on:
- Modules
- Packages
- Imports (absolute & relative)
- Virtual environments (Pipenv)
- Using external packages (PyPI)
"""
# =============================
# 🔹 WHAT IS __init__.py?
# =============================

# __init__.py makes a folder behave like a Python package.
# It's what allows you to import modules from a folder.

# Example folder:
# mypackage/
# ├── __init__.py
# └── module1.py

# In __init__.py, you can initialize things or re-export:
# from .module1 import some_function

# Now you can do:
# from mypackage import some_function

# It’s good practice to include it even if it's empty.

# =============================
# 🔹 1. MODULES
# =============================
# A module is just a .py file that contains Python code (functions, variables, etc.)
# You can reuse that code in another file using `import`.

# Example: (Assume we have a file called greetings.py with a function)
# greetings.py
# def say_hello(name):
#     return f"Hello, {name}!"

# main.py
# from greetings import say_hello
# print(say_hello("Dennis"))  # Output: Hello, Dennis!

# =============================
# 🔹 2. IMPORT STATEMENTS
# =============================

# ✅ Importing a whole module
# import math
# print(math.sqrt(16))  # Output: 4.0

# # ✅ Importing only a specific function from a module
# from math import pow
# print(pow(2, 3))  # Output: 8.0

# # ⚠️ Importing everything from a module (not recommended)
# from math import *
# print(factorial(5))  # Output: 120
# Bad practice because it pollutes your namespace (can overwrite variables)

# =============================
# 🔹 3. PACKAGES
# =============================
# A package is a folder that contains multiple modules and has an __init__.py file inside.
# Example structure:
# shapes/
# ├── __init__.py
# ├── circle.py  (def area(radius): ...)
# └── square.py  (def area(side): ...)

# You can import like this:
# from shapes.circle import area

# =============================
# 🔹 4. ABSOLUTE IMPORTS
# =============================
# These use the full path from the project root to the module

# Project structure:
# myapp/
# ├── main.py
# └── tools/
#     └── helper.py

# In main.py:
# from tools.helper import greet

# ✅ Advantage: Clear where each module comes from
# ❌ Disadvantage: Long paths in deeply nested packages

# =============================
# 🔹 5. RELATIVE IMPORTS
# =============================
# Use dots to import relative to the current file
# . = current directory
# .. = one directory up

# Example (inside tools/app.py):
# from .helper import greet      # same folder
# from ..utils import formatter  # one folder up

# ⚠️ Must run as a module:
# python -m tools.app

# =============================
# 🔹 6. PYPI & EXTERNAL PACKAGES
# =============================
# PyPI (https://pypi.org) is where you can find 3rd-party packages
# You install packages with pip or pipenv

# Example: Install `requests` using pipenv
# $ pipenv install requests

#import requests
#response = requests.get("https://api.github.com")
#print(response.status_code)  # Output: 200

# =============================
# 🔹 7. VIRTUAL ENVIRONMENTS
# =============================
# A virtual environment keeps dependencies isolated per project

# 📦 Pipenv is one tool for managing this:
# $ pipenv install <package-name>   # install and create env
# $ pipenv shell                    # activate environment

# This keeps your global Python clean and project-specific

# =============================
# 🔹 8. SUMMARY BEST PRACTICES
# =============================

# ✅ Group related functions into modules
# ✅ Organize modules into packages with __init__.py
# ✅ Use absolute imports for clarity, relative for local logic
# ✅ Use pipenv to isolate environments
# ✅ Only import what you need to keep code readable

"""
End of Notes
"""



                                #FILE I/O
# stands for file input and output
#input - reading from a file
#Output - writing to a file

# Python allows us to:

    # Read data stored in a file.

    # Write data to a file (like saving logs, user info, or results).

    # Append (add) data to a file.

    # This is helpful when your program needs to store information permanently.


                    #OPENING A FILE
file = open("example.txt", mode="r", encoding= "utf-8")
        # 'example.txt' is the name of the file.

        # mode='r' tells Python to read the file.

        # encoding='utf-8' makes sure characters like ä, é, ñ are handled correctly.
# A file has to be opened before reading or writing


                    #Reading a File
# Reading an entire file as a single string

with open('example.txt', 'r', encoding ='utf-8') as filee:
  content = file.read()
  print (content)

# readline() - reads one line at a time
# readlines() - returns a list of all lines in the file


# for line in file - efficient way to read a big file line by line

with open('example.txt', 'r', encoding = 'utf-8') as fileee:
  for line in file:
    print(line.strip()) #strip() - removes extra new lines or spaces




                      #WRITING TO A FILE
mode = 'w' #WRITE mode
      # overwrites the file if it exists
      # creates the file if it doesn't exist

with open ('log.txt', mode = 'w', encoding = 'utf-8') as file:
  file.write("This is the first log entry.\n")


mode = 'a' # APPEND mode
#Adds content to the end of the file
#Keeps old content

with open('log.txt', mode = 'a', encoding = 'utf-8') as file:
  file.write("This is an appended log entry.\n")


                      #CLOSING A FILE
#you must close a file after using it to
      #free up memory
      #prevent bugs or file locking
file = open ('example.txt', 'r')
file.close()

# to make the work easier by using with the file is closed automatically for you

with open ('example.txt', 'r', encoding ='utf-8') as file:
  data = file.read()


#  6. File Modes Summary
# Mode	Meaning
# 'r'	Read (default)
# 'w'	Write (overwrites file)
# 'a'	Append (adds to end of file)
# 'rb'	Read binary (e.g. images)
# 'wb'	Write binary

#REAL WORLD EXAMPLE

with open('journal.txt', mode = 'w', encoding = 'utf-8') as journal:
  journal.write("Day 1: i learnt how to write to a file in python.\n")

#adding another entry - append

with open('journal.txt', mode = 'a', encoding= 'utf-8') as journal:
  journal.write("Day 2: i learnt how to append to a file.\n")
  
#Reading and displaying all entries

with open ("journal.txt", mode = 'r', encoding = 'utf-8') as journal:
  for line in journal:
    print (line.strip())




                    #ENVIRONMENT SETUP
#Pyenv
# Helps in installation and switching between different versions of python
#Global python - the one the system uses unless told otherwise

#Pipenv
#Helps you create a virtual environment (like a private workspace for each project)
# manages project dependencies
# makes the app use exact version of python and packages


                 #Pyenv setup and use (PYTHON VERSION MANAGER)

'''checking python version installed'''
          #  $ pyenv versions

'''setting Global python version'''
#         $ pyenv global 3.11


                #Pipenv setup and use (VIRTUAL ENVIRONMENT SETUP)
'''creating a new virtual environment using python 3.8.20'''
#       $  $pipenv --python 3.8.20

# This creates two files:

          # Pipfile — defines Python version and dependencies

          # Pipfile.lock — locks all package versions exactly

'''INSTALL A PACKAGE - eg requests'''

#   $ pipenv install requests

#    $pipenv install requests==2.28.1

'''INSTALLING dev-only TOOLS(like testing libraries)'''

#    $ pipenv install pytest --dev

              # '''ACTIVATE AND RUN IN THE VIRTUAL ENVIRONMENT'''

#ACTIVATE THE VIRTUAL ENVIRONMENT
#   $ pipenv shell

# EXITING THE VIRTUAL ENVIRONMENT
#   $exit

#REMOVING VIRTUAL ENVIRONMENT
#   $pipenv --rm

# 📦 Key Terms (Simplified)
# Term	What it Means
# Module	A single Python file with code you can reuse (like math, random)
# Package	A group of modules (like a folder with many .py files)
# import	Keyword to use code from a module or package
# PyPI	A website (Python Package Index) where all Python packages live
# pip	A tool to install packages from PyPI
# Virtual Environment	A mini Python setup just for one project
# pipenv	A tool to manage virtual environments and packages easily


                      #SCRIPTING

#A python script is a .py file that automates tasks by directly running it
#eg- Automatically backup photos, send a whatsapp message at a certain time

"""
===============================
🐍 PYTHON SCRIPTING CHEAT SHEET
===============================

📌 WHAT IS A SCRIPT?
--------------------
- A script is a Python file meant to be **run directly**, not imported.
- Great for automating repetitive tasks (e.g., clean folders, batch rename files).

🧠 SCRIPT vs MODULE
--------------------
| Script (run)           | Module (import)         |
|------------------------|--------------------------|
| python script.py       | import module_name       |
| Executes directly      | Provides reusable code   |

📍 BASIC SCRIPT STRUCTURE
--------------------------
#!/usr/bin/env python3       # ← Shebang (Linux/Mac)
import sys, os               # ← Modules used in scripts

if __name__ == "__main__":   # ← Entry point
    print("This is a script!")

📥 COMMAND LINE ARGUMENTS (sys.argv)
-------------------------------------
import sys
name = sys.argv[1]  # Takes input from command line
print(f"Hello, {name}!")

# Run using:
# $ python script.py Dennis

🛠 SHELL COMMANDS (os.system)
------------------------------
import os
os.system('ls -l')  # Runs a shell command

🧼 EXAMPLE: DELETE .tmp FILES
------------------------------
import os
for file in os.listdir():
    if file.endswith('.tmp'):
        os.remove(file)
        print(f"Deleted {file}")

🔒 MAKE A SCRIPT EXECUTABLE (Linux/Mac)
----------------------------------------
1. Add shebang: #!/usr/bin/env python3
2. chmod +x script.py
3. Run using: ./script.py

📝 BASH SCRIPT VS PYTHON SCRIPT
-------------------------------
# Bash (.sh)
#!/bin/bash
echo "Listing files:"
ls -a

# Python (.py)
#!/usr/bin/env python3
import os
os.system('ls -a')

✅ PRO TIPS
-----------
- Use scripts to automate boring stuff.
- Keep them short and task-focused.
- Use virtual environments for dependencies.

🧪 TEST SCRIPT QUICKLY
-----------------------
python3 -c 'print("hello world")'

📁 RECOMMENDED STRUCTURE
-------------------------
project/
├── scripts/
│   ├── clean.py
│   ├── greet.py
├── README.md

===============================
"""
