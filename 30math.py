"""
PYTHON MATH – COMPLETE GUIDE
============================
Python provides a robust set of mathematical tools. 
These are divided into two categories:
1. Built-in Math Functions: Always available without importing anything.
2. The `math` Module: A built-in library that must be imported to access 
   advanced mathematical functions and constants.
"""

# =============================================================================
# 1. BUILT-IN MATH FUNCTIONS
# =============================================================================
# These functions are part of Python's core and require no imports.

# 🔹 min() and max()
# Used to find the lowest or highest value in a sequence or among arguments.
numbers = [12, 45, 7, 89, 23]
lowest = min(5, 10, 25)
highest = max(numbers)

print(" Lowest value:", lowest)    # 5
print("📈 Highest value:", highest)  # 89

# 🔹 abs()
# Returns the absolute (positive) value of a number.
negative_val = -7.25
absolute_val = abs(negative_val)

print("🔢 Absolute value:", absolute_val)  # 7.25

# 🔹 pow(x, y)
# Returns the value of x raised to the power of y (x^y).
# pow(4, 3) is the same as 4 * 4 * 4.
power_result = pow(4, 3)
print("⚡ Power result (4^3):", power_result)  # 64

# 🌟 Self-Generated Example: Calculating the "Range" of a dataset
# Range is the difference between the max and min values.
dataset = [15, 22, 10, 35, 28]
data_range = max(dataset) - min(dataset)
print(f"📊 Dataset Range: {data_range}")  # 35 - 10 = 25


# =============================================================================
# 2. THE MATH MODULE
# =============================================================================
# To use advanced math functions, you must import the built-in `math` module.
import math

#  math.sqrt()
# Returns the square root of a number.
sqrt_result = math.sqrt(64)
print("\n Square root of 64:", sqrt_result)  # 8.0

#  Self-Generated Example: Pythagorean Theorem (Hypotenuse)
# c = sqrt(a^2 + b^2)
side_a = 3
side_b = 4
hypotenuse = math.sqrt(pow(side_a, 2) + pow(side_b, 2))
print(f"📐 Hypotenuse of a {side_a}-{side_b} triangle: {hypotenuse}")  # 5.0


# =============================================================================
# 3. ROUNDING FUNCTIONS (ceil and floor)
# =============================================================================
# Unlike the built-in round() function, these always round in a specific direction.

# 🔹 math.ceil()
# Rounds a number UPWARDS to its nearest integer.
ceil_result = math.ceil(1.4)
print("\n️ Ceil of 1.4:", ceil_result)  # 2

#  math.floor()
# Rounds a number DOWNWARDS to its nearest integer.
floor_result = math.floor(1.4)
print("⬇️ Floor of 1.4:", floor_result)  # 1

# 🌟 Self-Generated Example: Shipping Box Calculator
# If you have 105 items and each box holds 10, you need 10.5 boxes.
# You can't ship half a box, so you must round UP (ceil).
total_items = 105
items_per_box = 10
boxes_needed = math.ceil(total_items / items_per_box)
print(f"📦 Boxes needed for {total_items} items: {boxes_needed}")  # 11

# 🌟 Self-Generated Example: Calculating Full Days
# If a task takes 50 hours, how many *full* 24-hour days is that?
total_hours = 50
full_days = math.floor(total_hours / 24)
print(f" Full days in {total_hours} hours: {full_days}")  # 2


# =============================================================================
# 4. MATH CONSTANTS
# =============================================================================
# The math module provides highly accurate mathematical constants.

# 🔹 math.pi
# Returns the value of PI (3.141592653589793).
pi_value = math.pi
print("\n Value of Pi:", pi_value)

#  math.e (Bonus)
# Returns Euler's number (2.718281828459045), useful in calculus and growth formulas.
e_value = math.e
print("📈 Value of e:", e_value)

#  Self-Generated Example: Circle Area and Circumference
radius = 7
area = math.pi * pow(radius, 2)
circumference = 2 * math.pi * radius

print(f"\n⭕ Circle with radius {radius}:")
print(f"   Area: {area:.2f}")          # 153.94
print(f"   Circumference: {circumference:.2f}")  # 43.98


# =============================================================================
# 5. BONUS: OTHER USEFUL MATH MODULE FEATURES
# =============================================================================

# 🔹 math.factorial(x)
# Returns the factorial of a number (x!).
fact_result = math.factorial(5)  # 5 * 4 * 3 * 2 * 1
print("\n🧮 Factorial of 5:", fact_result)  # 120

# 🔹 math.gcd(a, b)
# Returns the Greatest Common Divisor of two numbers.
gcd_result = math.gcd(12, 18)
print("🔗 GCD of 12 and 18:", gcd_result)  # 6

# 🔹 math.inf and math.nan
# Represents Infinity and "Not a Number".
print("♾️ Infinity:", math.inf)
print("❓ NaN:", math.nan)


# =============================================================================
# 💡 QUICK RECAP & BEST PRACTICES
# =============================================================================
# 1. Use BUILT-IN functions (min, max, abs, pow) for simple, everyday math.
# 2. Use the MATH MODULE (import math) for geometry, trigonometry, and constants.
# 3. Remember the difference between ceil (UP) and floor (DOWN).
# 4. When formatting floats (like Pi or square roots), use f-strings with 
#    precision limits (e.g., f"{value:.2f}") to keep your output clean.