"""
PYTHON TUPLES – COMPLETE GUIDE
================================

A tuple is a built-in data structure in Python used to store multiple items
in a single variable. It is one of Python’s core collection types, alongside
lists, sets, and dictionaries.

Key Features:
- Ordered: Items appear in a fixed sequence.
- Immutable: Cannot be changed after creation (no adding, removing, or modifying).
- Allows duplicates: Because items are accessed by index.
- Can hold any data type—including mixed types.

Tuples are ideal when you need to store data that should not change,
such as coordinates, RGB color values, or database records.
"""

# 1. Creating a Basic Tuple
# -------------------------
# Use parentheses () to define a tuple.
fruits = ("apple", "banana", "cherry")
print("Basic tuple:", fruits)


# 2. Ordered & Indexed
# --------------------
# The first item is at index 0, second at 1, etc.
print("\nAccessing items:")
print("First fruit:", fruits[0])      # apple
print("Last fruit:", fruits[-1])      # cherry (negative indexing works too)


# 3. Immutability (Unchangeable)
# ------------------------------
# Once created, you cannot modify the contents.
# Uncommenting the line below would raise an error:
# fruits[1] = "orange"  # TypeError: 'tuple' object does not support item assignment


# 4. Duplicates Are Allowed
# -------------------------
# Since tuples use indices, repeated values are fine.
colors = ("red", "blue", "red", "green")
print("\nTuple with duplicates:", colors)


# 5. Getting the Length
# ---------------------
# Use len() to count how many items are in the tuple.
print("\nNumber of fruits:", len(fruits))  # 3


# 6. Single-Item Tuple – The Comma Rule
# -------------------------------------
# A single value in parentheses is NOT a tuple unless followed by a comma.
single = ("hello",)    # This IS a tuple
not_single = ("hello") # This is just a string

print("\nSingle-item tuple type:", type(single))     # <class 'tuple'>
print("Without comma type:", type(not_single))       # <class 'str'>


# 7. Mixed Data Types
# -------------------
# Tuples can contain different types in the same collection.
person = ("Alex", 28, True, 5.9)
print("\nMixed-type tuple:", person)
# Example use: name, age, is_student, height


# 8. Checking the Type
# --------------------
# All tuples belong to the 'tuple' class.
print("\nData type of 'fruits':", type(fruits))


# 9. Creating a Tuple with the Constructor
# ----------------------------------------
# You can also use the tuple() function.
# Note: Pass an iterable (like a list) inside.
numbers = tuple([10, 20, 30])
print("\nTuple from constructor:", numbers)

# You can even convert a string into a tuple of characters:
letters = tuple("Python")
print("String as tuple:", letters)  # ('P', 'y', 't', 'h', 'o', 'n')


# 10. Why Use Tuples?
# -------------------
# - Safety: Prevent accidental changes to data.
# - Performance: Slightly faster than lists for fixed data.
# - Hashable: Can be used as dictionary keys (lists cannot).
coordinates = (40.7128, -74.0060)  # Latitude/longitude of NYC
location_map = {coordinates: "New York City"}
print("\nTuple as dict key:", location_map)



"""
ACCESSING ITEMS IN PYTHON TUPLES
================================

Tuples support several ways to retrieve their elements:
- Positive indexing (starts at 0)
- Negative indexing (starts at -1 from the end)
- Slicing (extract a range of items)

All these methods return existing data—they never modify the tuple.
"""

# Sample tuple for all examples
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("Full tuple:", fruits)


# 1. Positive Indexing
# --------------------
# Index 0 = first item, index 1 = second, etc.
print("\n1. Positive Indexing:")
print("First fruit:", fruits[0])      # apple
print("Second fruit:", fruits[1])     # banana


# 2. Negative Indexing
# --------------------
# -1 = last item, -2 = second last, etc.
print("\n2. Negative Indexing:")
print("Last fruit:", fruits[-1])      # mango
print("Second last:", fruits[-2])     # melon


# 3. Slicing – Range of Indexes
# -----------------------------
# Syntax: tuple[start:end] → includes 'start', excludes 'end'
print("\n3. Slicing (Range of Indexes):")
print("Items 2 to 4 (indices 2,3,4):", fruits[2:5])
# Returns: ('cherry', 'orange', 'kiwi')


# 4. Slice from Start
# -------------------
# Omit start → starts at index 0
print("\n4. From Beginning to Index 4 (excluded):")
print("First four items:", fruits[:4])
# Returns: ('apple', 'banana', 'cherry', 'orange')


# 5. Slice to End
# ---------------
# Omit end → goes to the last item
print("\n5. From Index 2 to End:")
print("From 'cherry' onward:", fruits[2:])
# Returns: ('cherry', 'orange', 'kiwi', 'melon', 'mango')


# 6. Negative Slicing
# -------------------
# Use negative numbers to slice from the end
print("\n6. Negative Slicing:")
print("From -4 (included) to -1 (excluded):", fruits[-4:-1])
# Returns: ('orange', 'kiwi', 'melon')
# Explanation:
#   -1 → 'mango' (excluded)
#   -2 → 'melon'
#   -3 → 'kiwi'
#   -4 → 'orange' (included)


# 💡 Key Reminder:
# - Slicing always returns a NEW tuple.
# - Original tuple remains unchanged (tuples are immutable).
# - Indexes are zero-based.
# - End index in slicing is NEVER included.

print("\n✅ All examples complete!")




"""
UPDATING TUPLES IN PYTHON
=========================

Tuples are immutable: you cannot change, add, or remove items directly.
However, Python allows indirect updates by converting to a list (mutable),
making changes, and converting back to a tuple.

Important: These methods create NEW tuples—they do not modify the original.
"""

# Original tuple
fruits = ("apple", "banana", "cherry")
print("Original tuple:", fruits)


# 1. Changing a Value
# -------------------
# Convert to list → modify → convert back to tuple
print("\n1. Changing 'banana' to 'kiwi':")
temp_list = list(fruits)
temp_list[1] = "kiwi"
fruits = tuple(temp_list)
print("Updated tuple:", fruits)


# 2. Adding Items
# ---------------

# Method A: Via list conversion
print("\n2A. Adding 'orange' using list conversion:")
temp_list = list(fruits)
temp_list.append("orange")
fruits = tuple(temp_list)
print("After adding via list:", fruits)

# Method B: Add one tuple to another
print("\n2B. Adding 'grape' by concatenating tuples:")
new_item = ("grape",)  # ← comma is essential!
fruits += new_item
print("After tuple concatenation:", fruits)


# 3. Removing an Item
# -------------------
# Again, use list conversion
print("\n3. Removing 'apple':")
temp_list = list(fruits)
temp_list.remove("apple")  # removes first occurrence
fruits = tuple(temp_list)
print("After removal:", fruits)


# 4. Deleting the Entire Tuple
# ----------------------------
# Use 'del' to remove the variable entirely
print("\n4. Deleting the tuple...")
backup = fruits  # keep a copy for demo
del fruits
# print(fruits)  # ❌ This would cause NameError

# Confirm it's gone:
try:
    print(fruits)
except NameError as e:
    print("Error:", e)


# 💡 Best Practices & Notes:
# - Tuples should be used for data that *should not change*.
# - Frequent updates? Consider using a list instead.
# - Tuple concatenation (+=) creates a new tuple each time—can be inefficient for many additions.
# - Always include a comma for single-item tuples: ("item",) ✅ vs ("item") ❌

print("\n✅ Workarounds demonstrated!")



"""
TUPLE UNPACKING IN PYTHON
=========================

"Packing" = assigning multiple values into a tuple.
"Unpacking" = extracting tuple values into individual variables.

Rules:
- Number of variables must match number of items (unless using *).
- Order matters: first variable gets first item, etc.
"""

# 1. Basic Packing & Unpacking
# ----------------------------
print("1. Basic Unpacking:")
fruits = ("apple", "banana", "cherry")  # ← packing
(green, yellow, red) = fruits           # ← unpacking

print("Green fruit:", green)   # apple
print("Yellow fruit:", yellow) # banana
print("Red fruit:", red)       # cherry


# 2. What If Counts Don't Match?
# ------------------------------
# This would cause an error:
# (a, b) = ("x", "y", "z")  # ValueError: too many values to unpack

# But Python offers a solution: the * operator!


# 3. Using * to Handle Extra Values
# ---------------------------------
# The * collects remaining items into a list.
print("\n2. Unpacking with * (asterisk):")
colors = ("red", "blue", "green", "yellow", "purple")

# First two get assigned; rest go into 'others'
(first, second, *others) = colors
print("First:", first)      # red
print("Second:", second)    # blue
print("Others:", others)    # ['green', 'yellow', 'purple']

# You can also put * in the middle or at the start:
(*start, last) = colors
print("Start:", start)      # ['red', 'blue', 'green', 'yellow']
print("Last:", last)        # purple


# 4. Real-World Use Case
# ----------------------
# Unpacking is great for functions that return multiple values.
print("\n3. Practical Example – Coordinates:")
def get_location():
    return (40.7128, -74.0060, "New York")

latitude, longitude, city = get_location()
print(f"City: {city}")
print(f"Coordinates: ({latitude}, {longitude})")


# 💡 Key Notes:
# - Unpacking makes code cleaner and more readable.
# - Always ensure variable count matches—unless using *.
# - The * always creates a list (even if zero or one item remains).

print("\n✅ Unpacking complete!")



"""
JOINING AND MULTIPLYING TUPLES IN PYTHON
========================================

Tuples support two key operations using operators:
- Joining: Use + to combine two or more tuples.
- Multiplying: Use * to repeat a tuple’s contents.

Both operations create NEW tuples—originals remain unchanged.
"""

# 1. Joining Tuples with +
# ------------------------
print("1. Joining Two Tuples:")
letters = ("a", "b", "c")
numbers = (1, 2, 3)

combined = letters + numbers
print("Combined tuple:", combined)
# Output: ('a', 'b', 'c', 1, 2, 3)


# You can even join more than two:
print("\nJoining Three Tuples:")
symbols = ("!", "@", "#")
all_together = letters + numbers + symbols
print("All together:", all_together)


# 2. Multiplying Tuples with *
# ----------------------------
print("\n2. Multiplying a Tuple:")
fruits = ("apple", "banana", "cherry")

doubled = fruits * 2
tripled = fruits * 3

print("Doubled:", doubled)
# Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

print("Tripled:", tripleled)
# Output: ('apple', 'banana', 'cherry', ...) repeated 3 times


# 3. Practical Use Cases
# ----------------------
# - Repeating default values
print("\n3. Practical Examples:")

# Create a tuple of 5 placeholders:
placeholders = ("_",) * 5
print("Placeholders:", placeholders)

# Build a pattern:
pattern = ("start", "middle") * 2 + ("end",)
print("Pattern:", pattern)


# 💡 Important Notes:
# - The + operator requires both operands to be tuples.
#   ❌ This fails: ("a",) + [1, 2] → TypeError
# - The * operator must use an integer (not float or string).
# - Both operations are memory-safe and efficient for small data.

print("\n✅ Tuple joining and multiplication complete!")




