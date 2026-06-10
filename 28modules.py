"""
PYTHON MODULES – COMPLETE GUIDE
===============================
A module is simply a Python file (.py) containing code (functions, variables, classes).
Think of it as a "code library" that allows you to organize your code and reuse it 
across different projects without rewriting it.

This file covers creating, importing, aliasing, and exploring modules.
"""

# =============================================================================
# 1. CREATING & USING A MODULE
# =============================================================================
# To create a module, you just save your code in a file with a .py extension.
# 
# For example, if you create a file named `mymodule.py` with this code:
# --- mymodule.py ---
# def greeting(name):
#     print("Hello, " + name)
# 
# person1 = {
#     "name": "John",
#     "age": 36,
#     "country": "Norway"
# }
# -------------------
#
# You can then import it into your main script using the `import` keyword.
# Syntax to call a function: module_name.function_name()

# (Since we don't have an actual `mymodule.py` file here, we'll use a built-in 
# module to demonstrate the exact same syntax):

import platform

# Calling a function from the module
os_name = platform.system()
print(f"Operating System: {os_name}")


# =============================================================================
# 2. VARIABLES IN A MODULE
# =============================================================================
# Modules can contain variables of all types (arrays, dictionaries, objects, etc.).
# You access them using the dot notation: module_name.variable_name

# Conceptual Example:
# import mymodule
# age = mymodule.person1["age"]
# print(age)  # Output: 36


# =============================================================================
# 3. RENAMING A MODULE (Aliasing)
# =============================================================================
# You can create an alias when importing a module using the `as` keyword.
# This is highly useful for long module names or to avoid naming conflicts.

import platform as pl

# Now we use the alias 'pl' instead of 'platform'
print(f"Python Version: {pl.python_version()}")

# 🌟 Self-Generated Example: Standard Data Science Aliases
# In the Python ecosystem, it is standard practice to alias heavy libraries:
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


# =============================================================================
# 4. BUILT-IN MODULES
# =============================================================================
# Python comes with a massive "Standard Library" of built-in modules you can use anytime.

import math
import random

# 🌟 Self-Generated Example: Using the math module
radius = 5
area = math.pi * (radius ** 2)
print(f"\nArea of a circle with radius {radius}: {area:.2f}")

#  Self-Generated Example: Using the random module
random_num = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_num}")


# =============================================================================
# 5. THE dir() FUNCTION
# =============================================================================
# The built-in `dir()` function lists all the defined names (functions, variables, 
# classes) inside a module. It's a great tool for exploring what a module offers.

# List all names in the math module
math_contents = dir(math)

# Printing just the first 5 items so it doesn't clutter the console
print("\nFirst 5 items in the math module:", math_contents[:5])

# 💡 Note: You can use dir() on built-in modules AND your own custom modules!


# =============================================================================
# 6. IMPORTING SPECIFIC PARTS (from ... import ...)
# =============================================================================
# Instead of importing the entire module, you can import only specific functions 
# or variables using the `from` keyword.
# 
# ⚠️ IMPORTANT: When using `from`, you DO NOT use the module name prefix 
# when calling the imported items.

from math import sqrt, pi
from random import choice

# Notice we just write `sqrt()`, NOT `math.sqrt()`
square_root = sqrt(16)
print(f"\nSquare root of 16: {square_root}")
print(f"Value of Pi: {pi}")

# 🌟 Self-Generated Example: Using `choice` to pick a random item
colors = ["red", "blue", "green", "yellow"]
random_color = choice(colors)
print(f"Randomly chosen color: {random_color}")

# Conceptual Example for custom modules:
# from mymodule import person1
# print(person1["name"])  # Notice: no 'mymodule.' prefix needed!


# =============================================================================
# 💡 BEST PRACTICES & PRO-TIPS
# =============================================================================
# 1. IMPORT LOCATION: Always put your `import` statements at the very TOP of your file.
# 
# 2. NAMESPACE CLASHES: Never name your own Python file the same as a built-in module.
#    (e.g., DO NOT name your file `math.py` or `random.py`. If you do, Python will 
#    import your file instead of the actual built-in library, causing massive errors!)
# 
# 3. KEEP IT CLEAN: Use `from module import specific_function` when you only need 
#    one or two things. It keeps your code cleaner and avoids typing the module name 
#    repeatedly.
# 
# 4. WILDCARD IMPORT (Avoid): You might see `from math import *`. Avoid this! 
#    It imports everything into your namespace and can cause hidden naming conflicts.