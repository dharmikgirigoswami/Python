"""
PYTHON range() FUNCTION – COMPLETE GUIDE
========================================
The built-in `range()` function returns an immutable sequence of numbers.
It is most commonly used in `for` loops to repeat an action a specific number of times.

Key Characteristics:
- Data Type: `range`
- Immutable: Cannot be modified (added to, removed from, or changed) after creation.
- Memory Efficient: It generates numbers on-the-fly rather than storing them all in memory at once.
"""

# =============================================================================
# 1. CREATING RANGES (1, 2, and 3 Arguments)
# =============================================================================
# Syntax: range(start, stop, step)
# - start: The first number (inclusive). Defaults to 0.
# - stop:  The last number (EXCLUSIVE). The sequence stops BEFORE this number.
# - step:  The difference between each number. Defaults to 1.

# 🔹 1 Argument: range(stop)
# Starts at 0, stops before 'stop'.
r1 = range(5)       # Represents: 0, 1, 2, 3, 4

# 🔹 2 Arguments: range(start, stop)
# Starts at 'start', stops before 'stop'.
r2 = range(2, 6)    # Represents: 2, 3, 4, 5

# 🔹 3 Arguments: range(start, stop, step)
# Starts at 'start', stops before 'stop', increments by 'step'.
r3 = range(0, 10, 2) # Represents: 0, 2, 4, 6, 8

#  Self-Generated Example: Countdown using a negative step
countdown = range(5, 0, -1) # Represents: 5, 4, 3, 2, 1


# =============================================================================
# 2. DISPLAYING RANGES
# =============================================================================
# A range object doesn't print the actual numbers directly. 
# To see the numbers, convert it to a list using `list()`.

print("1 Argument:", list(range(5)))          # [0, 1, 2, 3, 4]
print("2 Arguments:", list(range(1, 6)))      # [1, 2, 3, 4, 5]
print("3 Arguments:", list(range(5, 20, 3)))  # [5, 8, 11, 14, 17]
print("Negative Step:", list(range(5, 0, -1)))# [5, 4, 3, 2, 1]


# =============================================================================
# 3. USING RANGES IN LOOPS
# =============================================================================
# The most common use case: iterating a specific number of times.

# 🔹 Basic loop
for i in range(3):
    print(f"Loop iteration: {i}") 
    # Output: 0, 1, 2

#  Self-Generated Example: Looping through a list by index
# This is useful when you need to modify the list or compare adjacent items.
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Index {i} contains {fruits[i]}")


# =============================================================================
# 4. SLICING AND INDEXING RANGES
# =============================================================================
# Because ranges are sequences, you can access specific items or slice them.

r = range(10) # 0 to 9

# 🔹 Indexing: Get a single value at a specific index
print(r[2])  # Output: 2 (The number at index 2)

#  Slicing: Get a subsequence (returns a NEW range object)
sub_range = r[:3] 
print(list(sub_range))  # Output: [0, 1, 2]

# 🌟 Self-Generated Example: Getting every third item from a range
every_third = range(0, 20, 3)
print(list(every_third[1:4])) # Slices the sequence: [3, 6, 9]


# =============================================================================
# 5. MEMBERSHIP TESTING & LENGTH
# =============================================================================
# Ranges support standard sequence operations like `in` and `len()`.

r = range(0, 10, 2) # 0, 2, 4, 6, 8

# 🔹 Membership Testing (`in`)
# Checks if a number exists in the sequence. (Highly optimized in Python!)
print(6 in r)  # True  (6 is in the sequence)
print(7 in r)  # False (7 is not in the sequence)

# 🔹 Length (`len()`)
# Returns the total number of items in the range.
print(len(r))  # 5 (The numbers are 0, 2, 4, 6, 8)


# =============================================================================
# 6. REAL-WORLD SCENARIOS (Self-Generated)
# =============================================================================

# 🔹 Scenario A: Generating a grid of coordinates
# Using nested ranges to create (x, y) pairs
print("\n--- Grid Coordinates ---")
for x in range(2):
    for y in range(2):
        print(f"({x}, {y})")
# Output: (0,0), (0,1), (1,0), (1,1)

# 🔹 Scenario B: Creating a simple progress bar simulation
print("\n--- Progress Bar ---")
total_steps = 5
for i in range(1, total_steps + 1):
    progress = (i / total_steps) * 100
    print(f"Progress: {progress:.0f}% [{'#' * i}{'.' * (total_steps - i)}]")

# 🔹 Scenario C: FizzBuzz (Classic Interview Question)
print("\n--- FizzBuzz ---")
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)