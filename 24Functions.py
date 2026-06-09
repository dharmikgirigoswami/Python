"""
PYTHON FUNCTIONS – COMPLETE MASTER GUIDE
========================================
This file covers everything about Python functions:
- Basics, Arguments, and Return Values
- *args, **kwargs, and Special Parameters
- Variable Scope (LEGB Rule)
- Decorators
- Lambda Functions
- Recursion
- Generators
"""

# =============================================================================
# 1. FUNCTION BASICS & RETURN VALUES
# =============================================================================
# A function is a reusable block of code defined with the `def` keyword.
# It only runs when it is called.

def greet_user(name):
    """Returns a greeting string."""
    return f"Hello, {name}! Welcome back."

# Calling the function
message = greet_user("Alice")
print(message)  # Output: Hello, Alice! Welcome back.

# 🔹 Self-Generated Example: Reusable Data Formatter
def format_currency(amount, currency="USD"):
    """Formats a number into a currency string."""
    symbols = {"USD": "$", "EUR": "€", "GBP": "£"}
    symbol = symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f}"

print(format_currency(1234.5))      # $1,234.50
print(format_currency(99.9, "EUR")) # €99.90


# =============================================================================
# 2. ARGUMENTS: POSITIONAL, KEYWORD, AND DEFAULT
# =============================================================================
# - Parameters: Variables listed in the function definition.
# - Arguments: Actual values passed when calling the function.

def create_profile(username, role="viewer", active=True):
    print(f"User: {username} | Role: {role} | Active: {active}")

# Positional arguments (order matters)
create_profile("admin01", "admin") 

# Keyword arguments (order doesn't matter)
create_profile(active=False, username="guest123") 

# Mixing positional and keyword (positional MUST come first)
create_profile("moderator", active=True, role="moderator")


# =============================================================================
# 3. SPECIAL ARGUMENTS: *args, **kwargs, /, and *
# =============================================================================

#  *args (Arbitrary Positional Arguments)
# Collects extra positional arguments into a TUPLE.
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))  # Output: 10

# 🔹 **kwargs (Arbitrary Keyword Arguments)
# Collects extra keyword arguments into a DICTIONARY.
def build_config(**kwargs):
    return kwargs

config = build_config(host="localhost", port=8080, debug=True)
print(config)  # {'host': 'localhost', 'port': 8080, 'debug': True}

# 🔹 Positional-Only (/) and Keyword-Only (*)
# Parameters before `/` MUST be positional.
# Parameters after `*` MUST be keyword.
def process_data(a, b, /, *, c, d):
    return a + b + c + d

# result = process_data(1, 2, 3, 4)  #  Error: c and d must be keywords
result = process_data(1, 2, c=3, d=4)  # ✅ Correct
print(result)  # 10

# 🔹 Unpacking Arguments
# Use * to unpack lists/tuples, and ** to unpack dictionaries.
def multiply(a, b, c):
    return a * b * c

nums = [2, 3, 4]
print(multiply(*nums))  # Unpacks to multiply(2, 3, 4) -> 24

opts = {"a": 5, "b": 5, "c": 5}
print(multiply(**opts)) # Unpacks to multiply(a=5, b=5, c=5) -> 125


# =============================================================================
# 4. VARIABLE SCOPE & THE LEGB RULE
# =============================================================================
# LEGB Rule: Python searches for variables in this order:
# L - Local (inside current function)
# E - Enclosing (inside enclosing/nested functions)
# G - Global (top level of the script)
# B - Built-in (Python's built-in names like print, len)

global_var = "I am Global"

def outer_func():
    enclosing_var = "I am Enclosing"
    
    def inner_func():
        local_var = "I am Local"
        print(local_var)       # L
        print(enclosing_var)   # E
        print(global_var)      # G
        print(len([1, 2]))     # B (Built-in function)
        
    inner_func()

outer_func()

# 🔹 Modifying Global and Enclosing variables
counter = 0

def increment():
    global counter  # Tells Python to use the global variable
    counter += 1

def outer():
    x = 10
    def inner():
        nonlocal x  # Tells Python to use the enclosing variable
        x += 5
    inner()
    print("Enclosing x is now:", x)

increment()
print("Global counter:", counter)  # 1
outer()                             # Enclosing x is now: 15


# =============================================================================
# 5. DECORATORS
# =============================================================================
# A decorator is a function that takes another function and extends its behavior.
# Applied using the `@decorator_name` syntax.

import functools
import time

# 🔹 Basic Decorator with functools.wraps (preserves original metadata)
def timer_decorator(func):
    @functools.wraps(func)  # Crucial for preserving __name__ and __doc__
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"️ {func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    """Simulates a slow task."""
    time.sleep(0.1)
    return "Done"

slow_function()
print("Function name:", slow_function.__name__)  # 'slow_function' (not 'wrapper')

# 🔹 Decorator with Arguments (Decorator Factory)
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello(name):
    print(f"Hello {name}")

say_hello("Bob")


# =============================================================================
# 6. LAMBDA FUNCTIONS
# =============================================================================
# Anonymous, single-expression functions. Syntax: lambda args: expression

# Basic lambda
square = lambda x: x ** 2
print(square(5))  # 25

# 🔹 Real-world use: Built-in functions (map, filter, sorted)
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort list of dictionaries by 'grade'
top_students = sorted(students, key=lambda s: s["grade"], reverse=True)
print(top_students[0]["name"])  # Bob

# Filter out students with grade < 80
passed = list(filter(lambda s: s["grade"] >= 80, students))
print([s["name"] for s in passed])  # ['Alice', 'Bob']


# =============================================================================
# 7. RECURSION
# =============================================================================
# A function that calls itself. MUST have a base case to prevent infinite loops.

# 🔹 Classic Example: Factorial
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # 120

# 🔹 Self-Generated Example: Flattening a nested list
def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))  # Recursive call
        else:
            flat.append(item)
    return flat

nested = [1, [2, [3, 4], 5], 6]
print(flatten_list(nested))  # [1, 2, 3, 4, 5, 6]

# Note: Python has a recursion limit (usually 1000).
# import sys; sys.setrecursionlimit(2000) # Use with caution!


# =============================================================================
# 8. GENERATORS
# =============================================================================
# Functions that use `yield` instead of `return`.
# They pause execution and save state, making them highly memory-efficient.

# 🔹 Basic Generator
def count_up_to(max_val):
    count = 1
    while count <= max_val:
        yield count  # Pauses here and returns the value
        count += 1

# Iterating through the generator
for num in count_up_to(3):
    print(num)  # 1, 2, 3

# 🔹 Using next() manually
gen = count_up_to(2)
print(next(gen))  # 1
print(next(gen))  # 2
# print(next(gen)) # ❌ Raises StopIteration

# 🔹 Generator Expressions (Memory efficient alternative to list comprehensions)
# List comp: Creates entire list in memory [x*x for x in range(1000000)]
# Gen exp: Creates one item at a time (x*x for x in range(1000000))
gen_exp = (x * x for x in range(5))
print(list(gen_exp))  # [0, 1, 4, 9, 16]

# 🔹 Self-Generated Example: Infinite Fibonacci Generator
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_gen()
# Get the first 7 Fibonacci numbers without storing the whole sequence
first_seven = [next(fib) for _ in range(7)]
print(first_seven)  # [0, 1, 1, 2, 3, 5, 8]