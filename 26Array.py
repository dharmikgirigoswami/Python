"""
PYTHON ARRAYS (LISTS) – COMPLETE GUIDE
======================================
️ IMPORTANT NOTE: Python does not have built-in support for traditional 
"Arrays" like C++ or Java. Instead, Python uses LISTS to act as arrays. 
(If you need strict, high-performance arrays for math/data science, you 
would import a library like NumPy).

This file demonstrates how to use Python Lists as Arrays.
"""

# =============================================================================
# 1. WHAT IS AN ARRAY (LIST) & CREATION
# =============================================================================
# An array/list is a single variable that holds multiple values.
# Instead of creating car1, car2, car3, we store them in one list.

# Creating an array (list) containing car names
cars = ["Ford", "Volvo", "BMW"]

# Why use arrays?
# If you had 300 cars, you wouldn't want 300 variables. 
# Arrays let you store, loop through, and manage data efficiently.


# =============================================================================
# 2. ACCESSING & MODIFYING ELEMENTS
# =============================================================================
# Elements are accessed using an INDEX number.
# ⚠️ Python uses ZERO-BASED indexing (the first item is at index 0).

# 🔹 Accessing elements
first_car = cars[0]  # "Ford"
last_car = cars[2]   # "BMW"

# 🔹 Modifying elements
# You can change the value of a specific item by referring to its index.
cars[0] = "Toyota"   # Replaces "Ford" with "Toyota"
print("Modified array:", cars)  # ['Toyota', 'Volvo', 'BMW']


# =============================================================================
# 3. LENGTH OF AN ARRAY
# =============================================================================
# Use the len() function to get the total number of elements.
# 💡 Note: The length is always ONE MORE than the highest index.

num_cars = len(cars)
print(f"Total cars in array: {num_cars}")  # Output: 3


# =============================================================================
# 4. LOOPING THROUGH ARRAY ELEMENTS
# =============================================================================
# Use a `for...in` loop to iterate through all items.

print("\n--- Looping through cars ---")
for car in cars:
    print(f"Car: {car}")


# =============================================================================
# 5. ADDING & REMOVING ELEMENTS
# =============================================================================

# 🔹 Adding elements: append()
# Adds an element to the VERY END of the array.
cars.append("Honda")
print("After append:", cars)  # ['Toyota', 'Volvo', 'BMW', 'Honda']

# 🔹 Removing elements: pop()
# Removes the element at a SPECIFIC INDEX.
cars.pop(1)  # Removes the item at index 1 ("Volvo")
print("After pop(1):", cars)  # ['Toyota', 'BMW', 'Honda']

# 🔹 Removing elements: remove()
# Removes the FIRST occurrence of a SPECIFIC VALUE.
cars.append("BMW") # Adding BMW back to test remove()
cars.remove("BMW") # Removes the FIRST "BMW" it finds
print("After remove('BMW'):", cars)  # ['Toyota', 'Honda', 'BMW'] 
# Notice the second "BMW" remains because remove() only deletes the first match!


# =============================================================================
# 6. COMPREHENSIVE ARRAY/LIST METHODS
# =============================================================================
# Python provides many built-in methods to manipulate lists/arrays.

# Setup a fresh list for demonstrations
numbers = [5, 2, 9, 1, 5, 8]

#  insert(index, value): Adds an element at a SPECIFIC position
numbers.insert(0, 10) 
print("insert(0, 10):", numbers)  # [10, 5, 2, 9, 1, 5, 8]

# 🔹 extend(iterable): Adds elements from another list/iterable to the end
numbers.extend([99, 100])
print("extend([99, 100]):", numbers)  # [10, 5, 2, 9, 1, 5, 8, 99, 100]

# 🔹 index(value): Returns the index of the FIRST occurrence of a value
pos = numbers.index(9)
print("index(9):", pos)  # 3

# 🔹 count(value): Returns how many times a value appears
count_5 = numbers.count(5)
print("count(5):", count_5)  # 2

# 🔹 sort(): Sorts the list in ascending order (modifies in-place)
numbers.sort()
print("sort():", numbers)  # [1, 2, 5, 5, 8, 9, 10, 99, 100]

# 🔹 reverse(): Reverses the order of the list (modifies in-place)
numbers.reverse()
print("reverse():", numbers)  # [100, 99, 10, 9, 8, 5, 5, 2, 1]

# 🔹 copy(): Returns a shallow copy of the list
numbers_copy = numbers.copy()
print("copy():", numbers_copy)

# 🔹 clear(): Removes ALL elements from the list
numbers_copy.clear()
print("clear():", numbers_copy)  # []


# =============================================================================
# 7. SELF-GENERATED REAL-WORLD SCENARIOS
# =============================================================================

# 🔹 Scenario A: Shopping Cart Management
print("\n--- Shopping Cart Scenario ---")
cart = ["Apples", "Milk"]

# User adds items
cart.append("Bread")
cart.extend(["Eggs", "Cheese"])

# User removes an item by mistake (using index)
cart.pop(1)  # Removes "Milk"

# User changes their mind about an item (modifying by index)
cart[0] = "Green Apples"

print(f"Final Cart ({len(cart)} items): {cart}")

# 🔹 Scenario B: Processing Sensor Data (Finding Min/Max without built-in functions)
print("\n--- Sensor Data Scenario ---")
temperatures = [72, 75, 71, 78, 74, 76, 73]

# Loop through to find the highest temperature
max_temp = temperatures[0]
for temp in temperatures:
    if temp > max_temp:
        max_temp = temp

print(f"Maximum recorded temperature: {max_temp}°F")