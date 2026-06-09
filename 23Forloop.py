"""
PYTHON FOR LOOPS – COMPLETE GUIDE
=================================
A `for` loop is used to iterate over a sequence (list, tuple, dictionary, set, or string).
Unlike traditional C-style for loops, Python's `for` loop works like an iterator.
It automatically handles the indexing, meaning you don't need to define an index variable beforehand.
"""

# =============================================================================
# 1. BASIC FOR LOOPS & ITERABLES
# =============================================================================

# 🔹 Looping through a List
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(f"Fruit: {x}")

#  Looping through a String
# Strings are iterable objects; the loop goes through each character.
for char in "banana":
    print(char)

# 🌟 My Example: Looping through a Dictionary
# By default, looping over a dict yields its KEYS.
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
for student in student_scores:
    print(f"Checking scores for {student}...")


# =============================================================================
# 2. THE `break` STATEMENT
# =============================================================================
# The `break` statement immediately stops the loop, even if there are items left.

# 🔹 Example A: Break AFTER printing
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break  # Loop stops here. 'cherry' is never printed.
# Output: apple, banana

# 🔹 Example B: Break BEFORE printing
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break  # Loop stops here. 'banana' and 'cherry' are never printed.
    print(x)
# Output: apple

# 🌟 My Example: Finding the first even number
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"✅ First even number found: {num}")
        break


# =============================================================================
# 3. THE `continue` STATEMENT
# =============================================================================
# The `continue` statement skips the current iteration and jumps to the next one.

# 🔹 Example from text: Do not print "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue  # Skips the print() below and moves to "cherry"
    print(x)
# Output: apple, cherry

#  My Example: Filtering out vowels from a word
word = "beautiful"
consonants_only = ""
for char in word:
    if char.lower() in "aeiou":
        continue  # Skip vowels
    consonants_only += char
print(f"Consonants in '{word}': {consonants_only}")  # Output: btf


# =============================================================================
# 4. THE `range()` FUNCTION
# =============================================================================
# `range()` generates a sequence of numbers. It is often used with for loops.
# Syntax: range(start, stop, step)
# - start: Optional. Defaults to 0.
# - stop: Required. The loop stops BEFORE this number.
# - step: Optional. Defaults to 1.

# 🔹 Basic range (0 to 5)
for x in range(6):
    print(x)  # Prints 0, 1, 2, 3, 4, 5

#  Specifying the start value
for x in range(2, 6):
    print(x)  # Prints 2, 3, 4, 5

# 🔹 Specifying the step (increment)
for x in range(2, 30, 3):
    print(x)  # Prints 2, 5, 8, 11, 14, 17, 20, 23, 26, 29

# 🌟 My Example: Counting backwards
for x in range(5, 0, -1):
    print(x)  # Prints 5, 4, 3, 2, 1


# =============================================================================
# 5. THE `else` CLAUSE IN FOR LOOPS
# =============================================================================
# The `else` block runs EXACTLY ONCE when the loop finishes naturally.
# ️ CRITICAL: The `else` block is SKIPPED if the loop is stopped by a `break`.

# 🔹 Example A: Loop finishes naturally (else RUNS)
for x in range(6):
    print(x)
else:
    print("✅ Finally finished!")

# 🔹 Example B: Loop stopped by break (else is SKIPPED)
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")  # This will NOT print.

# 🌟 My Example: Searching for an item (The "For-Else" pattern)
# This is a very common Pythonic pattern!
target_id = 42
user_ids = [10, 25, 33, 42, 50]

for uid in user_ids:
    if uid == target_id:
        print(f"🎯 Found user {target_id}!")
        break
else:
    # This only runs if we NEVER hit the 'break'
    print(f" User {target_id} was not found in the list.")


# =============================================================================
# 6. NESTED LOOPS
# =============================================================================
# A loop inside another loop. The "inner loop" runs completely for 
# every single iteration of the "outer loop".

# 🔹 Example from text: Adjectives and fruits
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
# Output: red apple, red banana, red cherry, big apple...

#  My Example: Generating a simple multiplication table (1 to 3)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")  # Separator after each inner loop finishes


# =============================================================================
# 7. THE `pass` STATEMENT
# =============================================================================
# `for` loops cannot be empty. If you need a placeholder (e.g., while drafting code),
# use `pass` to avoid an IndentationError. It does nothing.

for x in [0, 1, 2]:
    pass  # TODO: Add logic here later

# 🌟 My Example: Stubbing out a complex processing loop
data_packets = [101, 102, 103]
for packet in data_packets:
    pass  # I will write the decryption logic here tomorrow.